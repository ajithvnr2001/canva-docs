---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/
title: Authentication - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:22.136245+00:00
---

# Authentication - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Authentication

Learn how to add authentication to a content extension.

Copy page

If an [authentication-enabled app](https://www.canva.dev/docs/extensions/platform-concepts/authentication/) has a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/), users of the app must authenticate with a third-party platform before they can access the app's content.

This topic explains how to implement authentication in a content extension.

For guidelines on creating a delightful authentication flow, see [Optimizing the authentication flow](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/).

## Step 1: Enable authentication

By default, authentication is disabled.

To enable authentication:

  1. Navigate to an app via the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers).
  2. Click **Authentication**.
  3. Enable **This app requires authentication**.



The **Authentication** page has two fields:

  * Redirect URL
  * Authentication base URL



The purpose of these fields is explained in the following steps.

## Step 2: Check if the user is authenticated

When a user opens a content extension, Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/content/resources/find

BASH

Copy

The body of this request includes a `user` property that contains the ID of the user. Your extension can use this ID to check if the current user is associated with a user in the backend of a third-party platform.

If the ID of the Canva user is _not_ associated with a user of the third-party platform, respond to the request with the following object:
    
    
    {
    
      "type": "ERROR",
    
      "errorCode": "CONFIGURATION_REQUIRED"
    
    }

JSON

Copy

This tells Canva to render a **Connect** button. Users can select the button to begin the authentication flow.

The user's ID is obfuscated and unique to each app. If an app has multiple extensions, each extension will receive the same ID for a user, but different apps will receive different IDs for the same user.

If the ID of the Canva user _is_ associated with a user of the third-party platform, respond with the content that Canva should render in the side panel:
    
    
    {
    
      "type": "SUCCESS",
    
      "resources": []
    
    }

JSON

Copy

Typically, this content will belong to the authenticated user.

Canva includes the ID of the user's [team⁠(opens in a new tab or window)](https://www.canva.com/help/article/create-teams) in all requests, via the `brand` property. You can use this ID to add team-specific features to an extension.

## Step 3: Redirect users to the Redirect URL

When a user clicks the **Connect** button, Canva opens a pop-up window.

Inside this window, Canva redirects the user to the app's **Redirect URL**.

The **Redirect URL** must point to a page that lets users authenticate with the third-party platform. For example, this could be a login form with a username and password, or the start of an OAuth 2.0 authorization flow. The exact authentication method is the responsibility of the app. Canva doesn't enforce any specific approach.

When redirecting users to the **Redirect URL** , Canva automatically appends a number of query parameters to the URL. All of these parameters serve a purpose, but the `user` and `state` parameters are of particular importance.

The `user` parameter contains the ID of the user. If the user successfully authenticates, the app needs to persist this ID to a data store. When the user returns to the app, the app can use this ID to check if the user is authenticated or not.

The `state` parameter contains a unique token for the authentication flow. For security reasons, the app must return this token to Canva at the end of the authentication flow. This protects the app against [cross-site request forgery⁠(opens in a new tab or window)](https://owasp.org/www-community/attacks/csrf) (CSRF) attacks.

To see the complete list of query parameters, see [Redirect URL](https://www.canva.dev/docs/extensions/server-api/redirect-url/).

For guidelines on providing a friendly and familiar-looking Redirect URL, see [Provide a user-friendly Redirect URL](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/#provide-a-user-friendly-redirect-url).

## Step 4: Redirect the user back to Canva

At the end of the authentication flow, redirect users to the following URL from within the pop-up window:
    
    
    https://canva.com/apps/configured?success=<true|false>&state=<token>

BASH

Copy

This must be a `302` redirect.

You also need to append the following parameters to the URL:

  * `success`
  * `state`



If the user has successfully authenticated, set the `success` parameter to `true`. This tells Canva to close the pop-up window and reload the extension. When the extension reloads, it can once again check if the user is authenticated.

If the user has not successfully authenticated, set the `success` parameter to `false`. This tells Canva to close the pop-up window without reloading the extension.

Always set the `state` parameter to the value of the token that Canva provided at the start of the authentication flow. If the `state` parameter is missing or invalid, an error occurs and the authentication fails.

Canva's `state` parameter is distinct from OAuth 2.0's `state` parameter.

Once a user has authenticated, don't require them to authenticate with any of the app's other extensions. For example, if an app has a content and a publish extension, only require them to navigate through the authentication flow once. In other words, handle authentication on an app-wide basis, not a per-extension basis. This is because users don't distinguish between apps and extensions. As far as they're concerned, they're simply using an app that supports various features.

## Step 5: Let users disconnect from Canva

After a user authenticates, they have the option of revoking that authentication. Your app must support this option to be eligible for distribution via the [Apps Directory⁠(opens in a new tab or window)](https://www.canva.com/apps).

When a user disconnects an app, Canva sends a `POST` request to the following endpoint:
    
    
    <authentication_base_url>/configuration/delete

BASH

Copy

`<authentication_base_url>` is a placeholder that refers to the app's **Authentication base URL** field, which can be set via the **Authentication** page in the Developer Portal.

Canva automatically appends the `/configuration/delete` path to the URL. Don't include the path in the **Authentication base URL** field.

The body of this request includes a `user` property, which contains the ID of the user. Your app can use this ID to remove the association between the Canva user and the user in the backend of the third-party platform.

When a user disconnects an app, the app must disconnect the user from all of its extensions. This means, if an app has a content and a publish extension, it must disconnect the user from both extensions. (This relates to the earlier point about authentication being app-wide.)

To learn more about this endpoint, see [the API reference](https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/).

## Step 6: Verify request signatures

Before you can submit an app for review, you must implement [signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/) for the following endpoints:

  * Redirect URL
  * `/configuration/delete`
  * `/content/resources/find`



This prevents third-parties from sending requests to these URLs.

The redirection from Canva to the **Redirect URL** is a `GET` request. To learn how to set up signature verification for a `GET` request, see [Verifying `GET` requests](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/).

All other requests from Canva are `POST` requests. To learn how to set up signature verification for a `POST` request, see [Verifying `POST` requests](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/).

## Example

This example uses ESM modules, which means it uses the `import` keyword instead of the `require` keyword. To run the example, add `'type': 'module'` to the `package.json` file.
    
    
    import basicAuth from "express-basic-auth";
    
    import express from "express";
    
    import querystring from "querystring";
    
    import { Low, JSONFile } from "lowdb";
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    // Set up the database
    
    // Docs: https://github.com/typicode/lowdb
    
    const adapter = new JSONFile("db.json");
    
    const db = new Low(adapter);
    
    await db.read();
    
    db.data ||= { loggedInUsers: [] };
    
    
    
    
    // Set up Redirect URL
    
    app.get(
    
      "/login",
    
      basicAuth({
    
        users: { admin: "password123" },
    
        challenge: true,
    
      }),
    
      async (request, response) => {
    
        const { loggedInUsers } = db.data;
    
        const { user } = request.query;
    
    
    
    
        // Add the user to the database
    
        if (!loggedInUsers.includes(user)) {
    
          loggedInUsers.push(user);
    
          await db.write();
    
        }
    
    
    
    
        // Construct query parameters for redirect back to Canva
    
        const params = querystring.stringify({
    
          success: true,
    
          state: request.query.state,
    
        });
    
    
    
    
        // Redirect back to Canva
    
        response.redirect(302, `https://canva.com/apps/configured?${params}`);
    
      }
    
    );
    
    
    
    
    // Handle requests for content
    
    app.post("/content/resources/find", async (request, response) => {
    
      const { loggedInUsers } = db.data;
    
      const { user } = request.body;
    
    
    
    
      // The user is logged-in
    
      if (loggedInUsers.includes(user)) {
    
        response.send({
    
          type: "SUCCESS",
    
          resources: [
    
            {
    
              type: "IMAGE",
    
              id: "123456",
    
              name: "Leaning Tower of Pisa",
    
              thumbnail: {
    
                url: "https://picsum.photos/id/629/600",
    
              },
    
              url: "https://picsum.photos/id/629/2000",
    
              contentType: "image/jpeg",
    
            },
    
          ],
    
        });
    
        return;
    
      }
    
    
    
    
      // The user is not logged-in
    
      response.send({
    
        type: "ERROR",
    
        errorCode: "CONFIGURATION_REQUIRED",
    
      });
    
    });
    
    
    
    
    // Handle disconnection requests
    
    app.post("/configuration/delete", async (request, response) => {
    
      // Remove the current user from the database
    
      db.data.loggedInUsers = db.data.loggedInUsers.filter((user) => {
    
        return user !== request.body.user;
    
      });
    
      await db.write();
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
