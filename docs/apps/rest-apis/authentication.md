---
url: https://www.canva.dev/docs/apps/rest-apis/authentication/
title: Authentication - Canva for your platform - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:14.413793+00:00
---

# Authentication - Canva for your platform - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/authentication/

Canva for your platform

[About Canva's REST APIs](https://www.canva.dev/docs/apps/rest-apis/)

Fundamentals

[API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/)[Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/)[Capabilities](https://www.canva.dev/docs/apps/rest-apis/capabilities/)[API versions](https://www.canva.dev/docs/apps/rest-apis/versions/)

Development guides

[Autofill designs with data](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/)[Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/)

Design guidelines

[User experience guidelines](https://www.canva.dev/docs/apps/rest-apis/experience-guidelines/)[UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/)[Brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/)

# Authentication

Copy page

To start using the Canva REST APIs, you need to authorize your users using [OAuth 2.0⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc6749).

OAuth lets your app authenticate the user, get their authorization to access the REST API endpoints, and then perform actions on their behalf. Specifically, the REST APIs use OAuth 2.0 with the [Authorization Code flow with Proof Key for Code Exchange (PKCE)⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7636) using SHA-256.

The authorization and authentication process involves the following steps:

  1. Obtain authorization from the Canva user for the scopes that your app requires. After the user authorizes your app, you'll receive an authorization code at your specified redirect URL.
  2. Use the authorization code to generate access tokens, which lets your app access REST API resources. This lets your app act on the user's behalf.



There are libraries in various languages that provide support for handling the OAuth process. For more information, see the [OAuth Community Site⁠(opens in a new tab or window)](https://oauth.net/code/).

You can also use the [starter kit for the Canva REST APIs⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-connect-api-starter-kit) as a starting point for an authorization and authentication implementation.

## Prerequisites

Before authenticating to the REST APIs, you must first create and configure your app in the Developer Portal, including:

  * Setting an app name
  * Generating and saving a client secret
  * Selecting scopes
  * Setting at least one authentication redirect URL



For more information, see [Quickstart](https://www.canva.dev/docs/apps/quickstart/).

## Obtain user authorization

To obtain user authorization, you must direct your users to Canva's authorization URL. This lets a user review and approve access for your app.

### Create the authorization URL

The authorization URL that you direct users to is in the following format:
    
    
    https://www.canva.com/api/oauth/authorize?code_challenge=<code challenge string>&code_challenge_method=s256&scope=<list of scopes>&response_type=code&client_id=<client ID>&state=<optional state>&redirect_uri=<redirect uri for your app>

Copy

In the Developer Portal, open your app from [**Your apps** ⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) and go to **Outside Canva** , then select **Redirect URLs**. That page has an **Authorization URL generator** tool that pre-fills most of the parameters for an authorization URL. If you use this tool, you must still provide your own `code_challenge` and `state` values, as well as verify the values for the other query parameters.

Create the URL, starting with `https://www.canva.com/api/oauth/authorize?` and add the following query parameters:

  1. **`code_challenge`**

The `code_challenge` string you provide is derived from another string, a `code_verifier`. You must first create a `code_verifier` value, and then transform the `code_verifier` into the `code_challenge` string. For more information, see the [PKCE specification⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7636#section-4.1).

     1. Create the `code_verifier` string. It must be a high-entropy cryptographically random string that is between 43 and 128 characters long. Only ASCII letters, numbers, and `-`, `.`, `_`, or `~` characters are allowed.

You must securely store the `code_verifier` string in your client, because you'll use it later to generate an access token.

The `code_verifier` value must not be accessible by the user or their browser.

     2. Generate the `code_challenge` string by SHA-256 hashing the `code_verifier` value and then encoding that result into a URL-safe base64 string.

You can use the [sample code shown below](https://www.canva.dev/docs/apps/rest-apis/authentication/#example-code-for-codeverifier-and-codechallenge-strings) to generate the `code_verifier` and `code_challenge` strings.

The `code_verifier` and `code_challenge` values should be unique for each request.

  2. **`code_challenge_method`**

This must be set to `S256` (SHA-256).

  3. **`scope`**

This is a space-separated list of [scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/) requested by your app.

The scopes you request must already be set in your app's settings in the Developer Portal. You can't request any scopes you haven't set in your app's settings.

You must be explicit when listing scopes.

For example, specifying `asset:write` doesn't grant `asset:read` permissions. You must specify _both_ in the scope string, for example: `asset:read asset:write`.

  4. **`response_type`**

This must be set to `code`.

  5. **`client_id`**

This value is the unique ID that identifies your client. You can get this value from the **Credentials** section of your app's **Outside Canva > Configuration** page in the Developer Portal.

  6. **`state`** (Optional)

The `state` parameter serves two primary purposes:

     * It acts as a countermeasure against [Cross-Site Request Forgery (CSRF)⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Cross-site_request_forgery) attacks by maintaining a unique session state between your app and the Canva API. For more information, see the [OWASP Cross-Site Request Forgery Prevention Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).
     * It helps preserve your platform's state through the OAuth flow.

Although this parameter is optional to include in the authorization URL, it's highly recommended. It makes sure that the response your app receives corresponds to the request initiated by the user, thereby preventing bad actors from forging requests.

When creating the `state` value, it must be a high-entropy random string and it should be unique for each request. You can use the [sample code shown below](https://www.canva.dev/docs/apps/rest-apis/authentication/#example-code-for-state-string) to generate the `state` string.

You must securely store the `state` string in your client, so you can use it later to verify the response.

The `state` parameter must not be used to store the `code_verifier` value.

  7. **`redirect_uri`** (Optional)

This is the URL to redirect the user to after they authorize your app.

Although this parameter is optional to include in the authorization URL, you must have at least one redirect URL set in your app's settings in the Developer Portal. The URL set in this query parameter must be one that you have already set in your app's settings.

If you have _only one_ redirect URL set in your app's settings, you don't need to provide this parameter.

If you have multiple redirect URLs set in your app's settings and this query parameter isn't supplied in the authorization URL, then the first redirect URL that's set in your app's settings is used by default.




After adding the preceding query parameters, an example authorization URL might look similar to the following:

`https://www.canva.com/api/oauth/authorize?code_challenge=eeeAbcdefgh123456789Vz96F9UIv8EHwnmibz3Djx3EE&code_challenge_method=s256&scope=asset:read%20asset:write%20design:meta:read%20folder:read%20comment:write&response_type=code&client_id=OCABC12-DeF`

#### Example code for `code_verifier` & `code_challenge` strings

You can use the following sample code to generate the `code_verifier` and `code_challenge` strings.
    
    
    import crypto from "crypto";
    
    const codeVerifier = crypto.randomBytes(96).toString("base64url");
    
    const codeChallenge = crypto
    
      .createHash("sha256")
    
      .update(codeVerifier)
    
      .digest("base64url");

JS

Copy

#### Example code for `state` string
    
    
    import crypto from "crypto";
    
    const state = crypto.randomBytes(96).toString("base64url");

JS

Copy

### Send the user to the authorization URL

You must direct your users to the authorization URL that you created to get their approval for your app and the requested scopes.

They will see a prompt similar to the following:

![User authorization prompt](https://www.canva.dev/_next/static/media/authentication_approval.c416eae2.png)

After they authorize your app, they are redirected to your redirect URL with the following query parameters:

`code```

Required

The authorization code you can use to [generate an access token](https://www.canva.dev/docs/apps/rest-apis/authentication/#generate-access-tokens).

`state```

Optional

The value of the `state` parameter, if it was provided with the initial request.

To prevent forgery of cross-site requests, you must verify that the received `state` value matches the one in the authorization URL you sent to the user. If they don't match, you must stop the authorization flow and return an error to the user.

## Generate access tokens

After you've obtained user authorization and received an authorization code, you can exchange the code for an access token (that lets you act on the user's behalf) and a refresh token (that you can use to get new access tokens).

Because access tokens are only valid for a short period time, you can handle requesting new access tokens using a refresh token instead of having to re-authorize the user to get a new authorization code.

An overview of the token request process is shown in the diagram below:

![Diagram showing the token request flow, adapted from OAuth 2.0 specification](https://www.canva.dev/_next/static/media/connect_token_flow_1600x976.6d4762db.png)

Token request flow (Adapted from the OAuth 2.0 specification).

Requests that require authenticating with your client ID and client secret can't be made from a web-browser client. They must come from your backend, otherwise they'll be blocked by Canva's [Cross-Origin Resource Sharing (CORS)⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) policy.

### Use an authorization code

To exchange an authorization code for an access token, use the [Generate an access token endpoint](https://www.canva.dev/docs/apps/rest-apis/reference/authentication/generate-access-token/).

Some points to note when using the endpoint with an authorization code:

  * Requests to the endpoint must be authenticated, and we recommend using the [basic access authentication⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Basic_access_authentication) method. For basic access authentication, the `{credentials}` string must be a Base64 encoded value of `{client id}:{client secret}`.
  * When exchanging an authorization code for an access token, you must set `grant_type` to `authorization_code` .
  * You must provide the `code_verifier` value that you generated when [creating the user authorization URL](https://www.canva.dev/docs/apps/rest-apis/authentication/#create-the-authorization-url).
  * You must provide the authorization code you received after the [user authorized your app](https://www.canva.dev/docs/apps/rest-apis/authentication/#send-the-user-to-the-authorization-url).



The endpoint reference includes [example request code](https://www.canva.dev/docs/apps/rest-apis/reference/authentication/generate-access-token/#example-request) in various languages.

A successful response from the endpoint includes the access token, the expiry time for the token, and a refresh token.

### Use a refresh token

When an access token expires or becomes invalid, you can use a refresh token from a previous access token request to get a new access token.

Refresh tokens can't be used to access resources on protected APIs. They are only used for generating new access tokens.

To exchange a refresh token for an access token, you again use the [Generate an access token endpoint](https://www.canva.dev/docs/apps/rest-apis/reference/authentication/generate-access-token/).

Some points to note when using the endpoint with a refresh token:

  * Requests to the endpoint must be authenticated, and we recommend using the [basic access authentication⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Basic_access_authentication) method. For basic access authentication, the `{credentials}` string must be a Base64 encoded value of `{client id}:{client secret}`.
  * When exchanging a refresh token for a new access token, you must set `grant_type` to `refresh_token`.
  * You must provide a refresh token from a previous token request.
  * Each refresh token can only be used once.



A successful response from the endpoint includes a new access token, the expiry time for the new token, and another refresh token.

## Introspect an access token

You can use the [Introspect an access token](https://www.canva.dev/docs/apps/rest-apis/reference/authentication/introspect-access-token/) endpoint to see whether an access token or refresh token is valid and active. You can also verify some token properties, such as its claims, scopes, and validity times.

## Revoke a token

If necessary, you can use the [Revoke a token](https://www.canva.dev/docs/apps/rest-apis/reference/authentication/revoke-token/) endpoint to revoke an access token or refresh token.
