---
url: https://www.canva.dev/docs/apps/authentication-migration-guide/
title: Migration guide for authentication - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:27.747178+00:00
---

# Migration guide for authentication - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/authentication-migration-guide/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Migration guide for authentication

How to migrate to the new authentication flow.

Copy page

In October 2023, we released breaking changes to the authentication flow for apps inside Canva. If you set up authentication for your app before then, you will need to make some changes to the app's backend.

**All apps that use authentication must implement these changes** , including:

  * Public apps and private apps
  * Apps built with the [Canva Developers SDK](https://www.canva.dev/docs/apps/apps-inside-canva/) or the [Extensions API](https://www.canva.dev/docs/extensions/)
  * Apps that are in development, in review, or already released



If your app is available to the public, you'll also need to notify us once the changes have been made so that we can verify that the changes have been implemented correctly.

This guide explains how to implement, test, and then notify us of the changes.

You only need to update the app's backend. You don't need to — and shouldn't — re-submit your app for review via the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers), as doing so will only cause delays.

## What's changed?

We've added some steps to the authentication flow to improve the security of the flow. All of the changes are via the app's backend and do not affect the user experience.

The sequence diagram below shows the updated flow. For the most part, the flow is the same. The steps highlighted with a blue background have been added to the flow.

![](https://www.canva.dev/_next/static/media/sequence-diagram.6ae10404.png)

## Updating your app

This section explains how to update the app's backend. To ensure a smooth migration, **do not make any other changes to your app during the migration process**.

This guide demonstrates how to implement the changes with Express.js. You will need to adapt to the steps to the backend's programming language, framework, and platform.

### Step 1: Create a `/configuration/start` endpoint

In the app's backend, set up the following endpoint to handle `GET` requests:
    
    
    <authentication_base_url>/configuration/start

Copy

For example:
    
    
    import * as express from "express";
    
    
    
    
    const app = express();
    
    
    
    
    app.get("/configuration/start", (req, res) => {
    
      // TODO
    
    });
    
    
    
    
    // Start the server
    
    const port = process.env.PORT || 3000;
    
    
    
    
    app.listen(port, () => {
    
      console.log(`Server is running on port ${port}`);
    
    });

TS

Copy

`<authentication_base_url>` is a placeholder for the app's **Authentication base URL**. This is the URL that you've already configured in the Developer Portal, via the **Add authentication** page.

If your app uses the Developers SDK, do not [verify the HTTP request](https://www.canva.dev/docs/apps/verifying-http-requests/) that's sent to this endpoint. It does not have access to the necessary parameters that make verification possible.

When an app triggers an authentication flow, Canva will:

  1. Open a new browser tab.
  2. Redirect the user to the `/configuration/start` endpoint.
  3. Append a `state` query parameter to the endpoint.



For example, if the **Authentication base URL** is:
    
    
    https://www.example.com

Copy

Then the complete URL would be:
    
    
    https://www.example.com/configuration/start?state=<state>

Copy

This means that that app's **Redirect URL** is no longer the first URL that users are taken to. Instead, users will be taken to the **Redirect URL** in a later step.

### Step 2: Generate a nonce for each request

In the `/configuration/start` endpoint, generate a unique _nonce_ for each request.

A nonce is a random, single-use value that's impossible to guess or enumerate. We recommended using a Version 4 UUID that is cryptographically secure, such as one generated with [`randomUUID`⁠(opens in a new tab or window)](https://nodejs.org/api/crypto.html#cryptorandomuuidoptions):
    
    
    import * as crypto from "crypto";
    
    const nonce = crypto.randomUUID();

TS

Copy

Not all UUIDs are cryptographically secure, such as ones generated with the [`uuid`⁠(opens in a new tab or window)](https://www.npmjs.com/package/uuid) package.

### Step 3: Store the nonce and an expiry time in a cookie

After generating a nonce, set a cookie that contains the nonce and an expiry time.

The cookie should be:

  * [Secure⁠(opens in a new tab or window)](https://owasp.org/www-community/controls/SecureCookieAttribute)
  * [HTTP-only⁠(opens in a new tab or window)](https://owasp.org/www-community/HttpOnly)
  * Signed



It should also have an expiry time **in addition to** the expiry time being included in the cookie itself.

By _signing_ a cookie, the app's backend can verify that the user hasn't modified the cookie. This prevents bad actors from tampering with the cookie in the browser.

The steps for setting and signing cookies depend on the framework. Some frameworks automatically sign cookies, while some don't have built-in support for cookie signing and require custom code.

It's beyond the scope of this documentation to explain all of the possible approaches, but refer to the following links to learn more about cookie signing in some popular frameworks:

  * Go 
    * [Fiber⁠(opens in a new tab or window)](https://docs.gofiber.io/api/middleware/encryptcookie/)
  * Node.js 
    * [Express.js⁠(opens in a new tab or window)](https://expressjs.com/en/resources/middleware/cookie-parser.html)
    * [Remix⁠(opens in a new tab or window)](https://remix.run/docs/en/main/utils/cookies#signing-cookies)
  * PHP 
    * [Laravel⁠(opens in a new tab or window)](https://laravel.com/docs/10.x/requests#cookies)
  * Python 
    * [Django⁠(opens in a new tab or window)](https://docs.djangoproject.com/en/4.2/topics/signing/)
    * [Flask⁠(opens in a new tab or window)](https://flask.palletsprojects.com/en/2.0.x/api/#sessions)
  * Ruby 
    * [Ruby on Rails⁠(opens in a new tab or window)](https://api.rubyonrails.org/v5.1/classes/ActionDispatch/Cookies.html)



The following code sample demonstrates how to set cookies with Express.js and [`cookieParser`⁠(opens in a new tab or window)](https://www.npmjs.com/package/cookie-parser):
    
    
    import * as express from "express";
    
    import * as crypto from "crypto";
    
    import * as cookieParser from "cookie-parser";
    
    
    
    
    const app = express();
    
    
    
    
    // TODO: Load a cryptographically secure secret from an environment variable
    
    app.use(cookieParser("SECRET GOES HERE"));
    
    
    
    
    // The expiry time for the nonce, in milliseconds
    
    const NONCE_EXPIRY_MS = 5 * 60 * 1000; // 5 minutes
    
    
    
    
    app.get("/configuration/start", (req, res) => {
    
      // Generate a nonce
    
      const nonce = crypto.randomUUID();
    
    
    
    
      // Create an expiry time for the nonce
    
      const nonceExpiry = Date.now() + NONCE_EXPIRY_MS;
    
    
    
    
      // Store the nonce and expiry time in a stringified JSON array
    
      const nonceWithExpiry = JSON.stringify([nonce, nonceExpiry]);
    
    
    
    
      // Store the nonce and expiry time in a cookie
    
      res.cookie("nonceWithExpiry", nonceWithExpiry, {
    
        httpOnly: true,
    
        secure: true,
    
        signed: true,
    
        maxAge: NONCE_EXPIRY_MS,
    
      });
    
    });

TS

Copy

It's worth nothing that:

  * To sign a cookie, you need a cryptographically secure secret, such as one generated by the `randomUUID` method. This secret should: 
    * be loaded via an environment variable
    * not change between server restarts
    * not be committed to source control
  * To store the nonce and an expiry time in a cookie, the above code sample stringifies a JSON array that contains both of the values, but there are other ways to accomplish the same outcome.
  * You should be mindful of framework-specific nuances. For example, in Express.js, the `maxAge` property is set in milliseconds, but the [`Max-Age`⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age) attribute value must be set in seconds.



### Step 4: Redirect the user back to Canva

After setting the cookie, redirect the user to the following URL with a `302` redirect:
    
    
    https://www.canva.com/apps/configure/link?state=<state>&nonce=<nonce>

Copy

You'll need to:

  * Replace `<state>` with the `state` query parameter that Canva includes with the request.
  * Replace `<nonce>` with the nonce that was stored in the cookie.



For example:
    
    
    // Extract state from query parameters
    
    const { state } = req.query;
    
    
    
    
    // Create query parameters
    
    const params = new URLSearchParams({
    
      state,
    
      nonce,
    
    });
    
    
    
    
    // Redirect the user
    
    res.redirect(
    
      302,
    
      `https://www.canva.com/apps/configure/link?${params.toString()}`
    
    );

TS

Copy

### Step 5: Validate the nonce

After the previously described redirect, Canva will redirect the user to the app's **Redirect URL** with a `nonce` query parameter appended to the URL (in addition to some other parameters).

Before attempting to authenticate the user, the app's backend must validate that the `nonce` query parameter and the nonce stored in the cookie:

  * are strings
  * are not empty strings
  * are equal to one another



You will also need to:

  * Verify that the current time does not exceed the nonce's expiry time.
  * Clear the cookie as soon as you have a local reference to it.



The end result should be that, if someone who didn't initiate the authentication flow were to visit the **Redirect URL** , the request would fail since they wouldn't have the expected cookie on their machine.

#### Handling invalid nonces

If the nonce validation fails, redirect the user to the following URL with a `302` redirect:
    
    
    https://www.canva.com/apps/configured?success=false&state=<state>&errors=<errors>

Copy

You'll need to:

  * Replace `<state>` with the `state` query parameter that Canva includes with the request.
  * Replace `<errors>` with a comma-separated list of one or more error codes. You can define the error codes yourself. They will be passed as-is to the app's frontend. (This only applies to the Developers SDK. You can omit the `errors` parameter for apps built with the Extensions API.)



For example:
    
    
    // Get the nonce from the query parameter
    
    const nonceQuery = req.query.nonce;
    
    
    
    
    // Get the nonce with expiry time from the cookie
    
    const nonceWithExpiryCookie = req.signedCookies.nonceWithExpiry;
    
    
    
    
    try {
    
      // Parse the JSON that contains the nonce and expiry time
    
      const nonceWithExpiry = JSON.parse(nonceWithExpiryCookie);
    
    
    
    
      // Extract the nonce and expiry time
    
      const [nonceCookie, nonceExpiry] = nonceWithExpiry;
    
    
    
    
      // Clear the cookie
    
      res.clearCookie("nonceWithExpiry");
    
    
    
    
      // If the nonces are invalid, terminate the authentication flow
    
      if (
    
        Date.now() > nonceExpiry || // The nonce has expired
    
        typeof nonceCookie !== "string" || // The nonce in the cookie is not a string
    
        typeof nonceQuery !== "string" || // The nonce in the query parameter is not a string
    
        nonceCookie.length < 1 || // The nonce in the cookie is an empty string
    
        nonceQuery.length < 1 || // The nonce in the query parameter is an empty string
    
        nonceCookie !== nonceQuery // The nonce in the cookie does not match the nonce in the query parameter
    
      ) {
    
        const params = new URLSearchParams({
    
          success: "false",
    
          state: req.query.state,
    
          errors: "invalid_nonce",
    
        });
    
    
    
    
        return res.redirect(
    
          302,
    
          `https://www.canva.com/apps/configured?${params.toString()}`
    
        );
    
      }
    
    } catch (e) {
    
      // An unexpected error has occurred (e.g. JSON parsing error)
    
      const params = new URLSearchParams({
    
        success: "false",
    
        state: req.query.state,
    
        errors: "invalid_nonce",
    
      });
    
    
    
    
      return res.redirect(
    
        302,
    
        `https://www.canva.com/apps/configured?${params.toString()}`
    
      );
    
    }

TS

Copy

We also recommend logging a security alert, as invalid nonces suggest a potential threat.

#### Handling valid nonces

If the nonce validation succeeds, continue the authentication flow as per usual — allow the user to log into their account, link the user with their Canva account, etc. **This part of the flow has not changed**.

### Code sample

The following code sample demonstrates how to follow these steps with Express.js:
    
    
    import * as express from "express";
    
    import * as crypto from "crypto";
    
    import * as cookieParser from "cookie-parser";
    
    
    
    
    const app = express();
    
    
    
    
    // TODO: Load a cryptographically secure secret from an environment variable
    
    app.use(cookieParser("SECRET GOES HERE"));
    
    
    
    
    // The expiry time for the nonce, in milliseconds
    
    const NONCE_EXPIRY_MS = 5 * 60 * 1000; // 5 minutes
    
    
    
    
    app.get("/configuration/start", (req, res) => {
    
      // Generate a nonce
    
      const nonce = crypto.randomUUID();
    
    
    
    
      // Create an expiry time for the nonce
    
      const nonceExpiry = Date.now() + NONCE_EXPIRY_MS;
    
    
    
    
      // Store the nonce and expiry time in a JSON string
    
      const nonceWithExpiry = JSON.stringify([nonce, nonceExpiry]);
    
    
    
    
      // Store the nonce and expiry time in a cookie
    
      res.cookie("nonceWithExpiry", nonceWithExpiry, {
    
        httpOnly: true,
    
        secure: true,
    
        signed: true,
    
        maxAge: NONCE_EXPIRY_MS,
    
      });
    
    
    
    
      // Extract state from query parameters
    
      const { state } = req.query;
    
    
    
    
      // Create query parameters
    
      const params = new URLSearchParams({
    
        state,
    
        nonce,
    
      });
    
    
    
    
      // Redirect the user
    
      res.redirect(
    
        302,
    
        `https://www.canva.com/apps/configure/link?${params.toString()}`
    
      );
    
    });
    
    
    
    
    app.get("/redirect-url", function (req, res) {
    
      // Get the nonce from the query parameter
    
      const nonceQuery = req.query.nonce;
    
    
    
    
      // Get the nonce with expiry time from the cookie
    
      const nonceWithExpiryCookie = req.signedCookies.nonceWithExpiry;
    
    
    
    
      try {
    
        // Parse the JSON that contains the nonce and expiry time
    
        const nonceWithExpiry = JSON.parse(nonceWithExpiryCookie);
    
    
    
    
        // Extract the nonce and expiry time
    
        const [nonceCookie, nonceExpiry] = nonceWithExpiry;
    
    
    
    
        // Clear the cookie
    
        res.clearCookie("nonceWithExpiry");
    
    
    
    
        // If the nonces are invalid, terminate the authentication flow
    
        if (
    
          Date.now() > nonceExpiry || // The nonce has expired
    
          typeof nonceCookie !== "string" || // The nonce in the cookie is not a string
    
          typeof nonceQuery !== "string" || // The nonce in the query parameter is not a string
    
          nonceCookie.length < 1 || // The nonce in the cookie is an empty string
    
          nonceQuery.length < 1 || // The nonce in the query parameter is an empty string
    
          nonceCookie !== nonceQuery // The nonce in the cookie does not match the nonce in the query parameter
    
        ) {
    
          const params = new URLSearchParams({
    
            success: "false",
    
            state: req.query.state,
    
            errors: "invalid_nonce",
    
          });
    
    
    
    
          return res.redirect(
    
            302,
    
            `https://www.canva.com/apps/configured?${params.toString()}`
    
          );
    
        }
    
      } catch (e) {
    
        // An unexpected error has occurred (e.g. JSON parsing error)
    
        const params = new URLSearchParams({
    
          success: "false",
    
          state: req.query.state,
    
          errors: "invalid_nonce",
    
        });
    
    
    
    
        return res.redirect(
    
          302,
    
          `https://www.canva.com/apps/configured?${params.toString()}`
    
        );
    
      }
    
    
    
    
      // This is where you should authenticate the user, etc. You should have
    
      // already written this code and it should not need to be updated.
    
    });
    
    
    
    
    // Start the server
    
    const port = process.env.PORT || 3000;
    
    
    
    
    app.listen(port, () => {
    
      console.log(`Server is running on port ${port}`);
    
    });

JS

Copy

## Testing your changes

### Step 1: Set up a testing or staging environment

To test the changes, Canva needs to be able to send requests to the app's backend. This means the backend must be exposed via the internet. To ensure a smooth migration, we recommend testing the changes via a non-production environment, such as a staging environment.

If you don't have a non-production environment ready to go, we recommend using an SSH tunneling service, such as [ngrok⁠(opens in a new tab or window)](https://ngrok.com/), to expose your local development server to the internet.

There are inherent risks in using tools such as ngrok. Be careful about what you expose to the public internet and shut-down the ngrok tunnel as soon as you're done using it.

### Step 2: Create a new version of the app

Once you release an app, you can't configure its settings via the Developer Portal. This means you can't update the **Redirect URL** or **Authentication base URL** to point to their non-production versions.

To address this, create a new version of the app:

  1. Log in to the Developer Portal.
  2. Navigate to the app via the [Your apps⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) page.
  3. Click **Create a new version**.



The new version of the app will be in the draft state, so any changes will only be visible to you.

Do not submit this new version of the app as part of the migration process. You should only be using this version for testing purposes.

### Step 3: Update the app's authentication settings

  1. In the Developer Portal, navigate to the app's **Add authentication** page.
  2. Update the **Redirect URL** so it points to the non-production version.
  3. Update the **Authentication base URL** so it points to the non-production version.



### Step 4: Test the authentication flow

Start by testing the "happy path" to verify that the core authentication flow works as expected. You should be able to log in, sign up, etc. The user experience should not have changed.

Then test the scenarios described below. Each of the scenarios should terminate the authentication flow by closing the tab and returning an error to the app's frontend.

Be sure to test the scenarios independently from one another — that is, in separate authentication flows — to ensure that you don't conflate the results of each test.

#### Scenario 1: The nonce query parameter doesn't exist

  1. Start an authentication flow.
  2. After the **Redirect URL** loads, remove the `nonce` query parameter from the URL.
  3. Navigate to the updated URL.



#### Scenario 2: The nonce query parameter contains a modified value

  1. Start an authentication flow.
  2. After the **Redirect URL** loads, modify the `nonce` query parameter in the URL — for example, by adding or removing a character.
  3. Navigate to the updated URL.



#### Scenario 3: The cookie doesn't exist

  1. Start an authentication flow.
  2. After the **Redirect URL** loads, delete the cookie that contains the nonce. (See below.)
  3. Reload the page.



##### How to delete cookies in Google Chrome

  1. Open the **JavaScript Console**.
  2. Navigate to the **Application** tab.
  3. Expand the **Storage > Cookies** section.
  4. Select the domain of the **Redirect URL**.
  5. Right-click the relevant cookie.
  6. Click **Delete**.



#### Scenario 4: The cookie doesn't exist and the nonce query parameter doesn't exist

  1. Start an authentication flow.
  2. After the **Redirect URL** loads: 
     1. Delete the cookie that contains the nonce.
     2. Remove the `nonce` query parameter from the URL.
  3. Navigate to the updated URL.



## Notifying Canva of the changes

After making and testing the changes to the app, you need to notify us so that we can verify the changes have been implemented correctly. To notify us, [create a support ticket⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/2/group/2).

In the ticket, **include credentials that we can use to test the authentication flow**.

Once we've been notified of the change, we aim to re-enable apps within 24 hours. To ensure that this process goes smoothly, double-check that the changes have been implemented correctly.

## Additional documentation

### Canva Developers SDK

The complete authentication flow for the Developers SDK is documented in [Authenticating users](https://www.canva.dev/docs/apps/authenticating-users/).

### Extensions API

The complete authentication flow for the Extensions API is documented in the following topics:

  * [Authentication overview](https://www.canva.dev/docs/extensions/platform-concepts/authentication/)
  * [Authentication for content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)
  * [Authentication for publish extensions](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)


