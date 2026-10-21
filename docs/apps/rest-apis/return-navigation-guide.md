---
url: https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/
title: Return users to your platform - Canva for your platform - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:40.222929+00:00
---

# Return users to your platform - Canva for your platform - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/

Canva for your platform

[About Canva's REST APIs](https://www.canva.dev/docs/apps/rest-apis/)

Fundamentals

[API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/)[Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/)[Capabilities](https://www.canva.dev/docs/apps/rest-apis/capabilities/)[API versions](https://www.canva.dev/docs/apps/rest-apis/versions/)

Development guides

[Autofill designs with data](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/)[Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/)

Design guidelines

[User experience guidelines](https://www.canva.dev/docs/apps/rest-apis/experience-guidelines/)[UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/)[Brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/)

# Return users to your platform

Let users move seamlessly between your platform and the Canva editor.

Copy page

You can use the Canva REST APIs to send users from your platform to the Canva editor, and return them to your platform when they've finished editing a design.

## Workflow

This guide demonstrates how you can direct a user from your platform to edit a design in Canva, and when they've finished editing the design, they can click a button in the Canva UI redirecting them back to your platform.

Your workflow needs to do the following:

  1. Authenticate and authorize the user with Canva's OAuth flow.
  2. Query the REST APIs on the user's behalf to get a list of their designs.
  3. Display the designs with an _Edit in Canva_ button that uses the design's edit URL.
  4. Redirect the user to the Canva editor.
  5. Decode Canva's return URL when the user is ready to return to your platform.
  6. Refresh the displayed designs when the user returns to your platform.



![Workflow diagram](https://www.canva.dev/_next/static/media/workflow-diagram.3d0fd844.png)

### Starter kit

To illustrate how your platform might look, this guide uses screenshots from the e-commerce demo app included in the [starter kit for the Canva REST APIs⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-connect-api-starter-kit). We recommend downloading and using this kit as a reference when building your app. The kit requires a working [app](https://www.canva.dev/docs/apps/quickstart/) and includes:

  * A React-based e-commerce web app
  * An Express.js backend with a mock product database
  * A working REST API client
  * A working authentication flow



## Prerequisites

To complete this guide, you need an account on <https://www.canva.com/developers>[⁠(opens in a new tab or window)](https://www.canva.com/developers).

## Configure your app

The following steps walk you through creating an app and authenticating a user with OAuth. Skip to [Build your workflow](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/#build-your-workflow) if you have an app already and are familiar with the authentication flow.

### Step 1. Create an app

  1. Create an app, and enable the REST APIs on it, using the steps described in [Quickstart](https://www.canva.dev/docs/apps/quickstart/).
  2. Your app requires at least one redirect URL, and at least the `design:read` and `design:meta:read` scopes.
  3. In the Developer Portal, open your app and go to **Outside Canva** , then select **Configuration**. Turn on **Return navigation** and fill in the required **Return URL** field.



### Step 2. Authenticate with OAuth

  1. Follow the [Authentication guide](https://www.canva.dev/docs/apps/rest-apis/authentication/) to get an authorization code, then generate an access token for your requests. For this process you need:

     * Your Client ID.
     * Your Client secret.
     * A URL-encoded list of your app's scopes.
     * One of your nominated redirect URLs.
  2. (Optional) If you've already authenticated but your token has expired, you can skip step 1 and [request a new token using your refresh token](https://www.canva.dev/docs/apps/rest-apis/reference/authentication/generate-access-token/).




When you've successfully authenticated and obtained a bearer token, you can build your workflow.

## Build your workflow

The following steps walk you through the process of building your return navigation workflow.

### Step 1. Get designs

  1. Get a list of the user's designs with a call to the [List designs API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/list-designs/).
         
         curl --request GET \
         
           --url https://api.canva.com/rest/v1/designs \
         
           --header 'Authorization: Bearer {TOKEN}'

SHELL

Copy

  2. The endpoint's response includes a list of designs in the `items` array.
         
         {
         
           "continuation": "MjU:Kg:UkVMRVZBTkNF:QU5Z",
         
           "items": [
         
             {
         
               "id": "{DESIGN_ID}",
         
               "title": "Beetroot and Spinach Salad",
         
               "owner": {
         
                 "user_id": "{USER_ID}",
         
                 "team_id": "{TEAM_ID}"
         
               },
         
               "doctype_name": "1920px x 1920px",
         
               "thumbnail": {
         
                 "width": 447,
         
                 "height": 447,
         
                 "url": "{DESIGN_THUMBNAIL_URL}"
         
               },
         
               "urls": {
         
                 "edit_url": "https://www.canva.com/api/design/{token}/edit",
         
                 "view_url": "https://www.canva.com/api/design/{token}/view"
         
               }
         
             }
         
           ]
         
         }

JSON

Copy




Each design item contains a `urls` object with `edit_url` and `view_url` properties. The URLs are temporary URLs which use the structure `https://www.canva.com/api/design/{token}/{edit|view}`. The `{token}` is a unique time-limited token for accessing the design.

The URLs contain everything needed to open the design in the Canva editor.

The `urls` object is also returned in the response of the [Create design API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/create-design/). Instead of directing users to edit an existing design, you could also create a new one then direct them to edit the new design.

### Step 2. Build your UI

  1. Display your designs.

Each design item's object includes all the data required to display it in your platform. For example, the starter kit uses the item's title and thumbnail URL to display the design in the demo e-commerce web app.

![Displayed user designs](https://www.canva.dev/_next/static/media/displayed_designs.5f98ac25.png)

  2. Prepare your edit URL.

For each design, create a unique `correlation_state` string that identifies your product or UI state, and append it to the design's `edit_url` as a query parameter. The `correlation_state` value is returned when the user is redirected from Canva back to your platform.

The `correlation_state` string has the following requirements:

     * Must be 50 characters or less.
     * Must be URL safe.
     * Should include everything you need to redirect your user or update your platform's state.
     * Can contain stringified JSON.
    
    https://www.canva.com/api/design/{token}/edit?correlation_state={YOUR-CORRELATION-STATE-STRING}

Copy

You can optionally add another parameter, `app_id`, to open a particular app inside Canva when the design is opened. App IDs are listed in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).
    
    https://www.canva.com/api/design/{token}/edit?correlation_state={YOUR-CORRELATION-STATE-STRING}&app_id={YOUR-APP-ID}

Copy

If you would like to open an app developed by someone else, or by Canva, app IDs for these apps can be extracted from the app URL:

     1. Navigate to the [Canva Apps Page⁠(opens in a new tab or window)](https://www.canva.com/your-apps).
     2. Find the app you want to open.
     3. Click the app. The modal containing app information opens, and the page URL changes.
     4. Extract the App ID from the URL, which appears after the `/your-apps/` segment. For example, if you click the app _Acquia DAM (Widen)_ , the URL is `https://www.canva.com/your-apps/AAFcE5stzlQ/acquia-dam-(widen)`. The App ID is `AAFcE5stzlQ`.

Because of the 50 character limit, it might not always be practical to directly store all of the required state information in the `correlation_state` string.

In this situation, we recommend that you instead store the state information in a database, and create a unique key (encoded in [base64url⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc4648#section-5)) which identifies the information. You can then pass the key as the `correlation_state` value, and when the user is redirected from Canva back to your platform, use the key in `correlation_state` to retrieve the state information needed to process the return.

  3. Add an _Edit in Canva_ button or link using the design's edit URL created in the previous step. When clicked, the button or link navigates your user to the Canva editor and opens their design.

![Edit in Canva](https://www.canva.dev/_next/static/media/edit-in-canva.c600f358.png)

If you use Canva's logo when creating your button or link, make sure you follow Canva's [brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/).

  4. When the user has finished editing their design, they can return to your platform using the Canva editor's _Return_ button.

![Return to your platform](https://www.canva.dev/_next/static/media/return-to-client.cef36423.png)




### Step 3. Parse the return URL

When the user has finished editing their design, they can return to your platform using the Canva editor's _Return_ button. To power the button, Canva generates a URL that is your app's return URL appended with a unique `correlation_jwt` parameter.

  1. Intercept the return URL, which is structured as follows.
         
         https://{YOUR_RETURN_URL}?correlation_jwt={CORRELATION_JWT}

Copy

  2. Parse the URL and validate the `correlation_jwt` parameter.

The `correlation_jwt` parameter is a URL-safe, Base64-encoded JSON Web Token (JWT). The JWT contains the following claims:

     * `aud`: Your app's Client ID.
     * `exp`: The token expiry. This is 1 day after the design is opened in the Canva editor.
     * `sub`: The User ID of the user who initiated the return navigation workflow.
     * `team_id`: The Team ID of the user who initiated the return navigation workflow.
     * `type`: Set as `rti`.
     * `jti`: The token's unique identifier (JWT ID).
     * `design_id`: The design's ID.
     * `correlation_state`: Your original `correlation_state` string passed to Canva in your prepared edit or view URL.

The JWT is signed using the REST API keys. You should always check the validity of the signature against the public keys provided by the [keys API](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/), and check the JWT payload.

You can use your preferred method or library to decode the JWT and verify the JWT payload. The following JavaScript example shows how to fetch Canva's public JSON Web Key Set (JWKS), validate and decode the JWT using [`jose`⁠(opens in a new tab or window)](https://www.npmjs.com/package/jose), and return the `sub`, `team_id`, and `type` from the payload:
    
    const jose = require('jose');
    
    const correlationJwt = '{CORRELATION_JWT}';
    
    const canvaKeysUrl = 'https://api.canva.com/rest/v1/connect/keys';
    
    
    
    
    async function verifyToken(token) {
    
    const JWKS = jose.createRemoteJWKSet(new URL(canvaKeysUrl));
    
    
    
    
    const { payload, protectedHeader } = await jose.jwtVerify(token, JWKS, {
    
        audience: '{CLIENT_ID}',
    
      });
    
    
    
    
    return !!protectedHeader
    
        && payload.sub === '{USER_ID}'
    
        && payload.team_id === '{TEAM_ID}'
    
        && payload.type === 'rti'
    
    };
    
    
    
    
    const isValid = await verifyToken(correlationJwt);
    
    console.log(isValid);

JAVASCRIPT

Copy

  3. Use the returned `correlation_state` value to update your platform, or redirect the user as needed.



