---
url: https://www.canva.dev/docs/print-partnerships/concepts/authentication/
title: Authentication - General information - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.021451+00:00
---

# Authentication - General information - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/concepts/authentication/

General information

[Evaluating Canva](https://www.canva.dev/docs/print-partnerships/concepts/evaluating-canva/)[Authentication](https://www.canva.dev/docs/print-partnerships/concepts/authentication/)[Credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/)[Request credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/)[Product catalog](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/)[Proofing](https://www.canva.dev/docs/print-partnerships/concepts/proofing/)[Security](https://www.canva.dev/docs/print-partnerships/concepts/security/)[User journey](https://www.canva.dev/docs/print-partnerships/concepts/user-journey/)

# Authentication

Copy page

When an end user arrives at a Print Partnership integration, the user experience should be seamless.

To accomplish this, Canva doesn't require that end users:

  * Sign up for (or log into) a Canva account.
  * Sign up for (or log into) a separate account via the partner's website.



Instead, the end user's existing account on the partner's website is used to automatically (and invisibly) create a "ghost" account on Canva.

These accounts let users:

  * Create designs via the Canva editor.
  * View and edit previously created designs.
  * Upload private media to Canva.



But without the friction of a manual authentication flow.

Canva never requests access to your user's contact details.

If your integration doesn't require authentication, you can enable [anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/).

## How authentication works

When a user arrives at an integration, the partner calculates a [JSON Web Token⁠(opens in a new tab or window)](https://jwt.io/introduction/) (JWT) for the user and passes it into the Partnership SDK's [`initialize`](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/) method:
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        container: document.getElementById("container"),
    
        autoAuthToken: "<auto_auth_token>",
    
      });
    
    })();

JAVASCRIPT

Copy

The SDK refers to this token as an _autoAuthToken_.

When calculating an autoAuthToken, the partner provides an ID for the current user. This ID is a value that maps to a user in the partner's backend system, such as a primary key in a database row.

If the user's ID is _not_ already associated with an account, Canva creates an account for the user and logs them into it. If the user's ID _is_ already associated with an account, Canva logs them into the account.

If an autoAuthToken is invalid, Canva returns a [Forbidden (403)](https://www.canva.dev/docs/print-partnerships/troubleshooting/403-forbidden-error/) error.

## Calculating an autoAuthToken

You need to two ingredients to calculate an autoAuthToken: a _payload_ and a _secret_.

### Payload

The payload is an object with the following properties:

#### `iss`

The integration's [Partner API key](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-key).

#### `sub`

A unique ID for the current user. This ID is a value that maps to a user in the partner's backend system, such as an email address.

#### `iat`

The UNIX timestamp of when the token was issued (in seconds).

#### `exp`

An expiration time for the token as a UNIX timestamp (in seconds). This time must be less than 12 hours after the token's "iat" time.

This is an example of a payload:
    
    
    {
    
      "iss": "<issuer>",
    
      "sub": "<subject>",
    
      "iat": "<issued_at>",
    
      "exp": "<expires_at>"
    
    }

JSON

Copy

### Secret

The secret is the integration's [Partner API secret](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-secret).

A secret is a sensitive value. You should never share it or commit it to source control. If someone gains access to this secret, they can access your user's private designs.

## Example

The following snippet demonstrates how to calculate an autoAuthToken:
    
    
    const jwt = require("jwt-simple");
    
    
    
    
    function generateAutoAuthToken(opts) {
    
      const expiryInMinutes = opts.expiryInMinutes || 30;
    
      const now = Math.floor(new Date().getTime() / 1000);
    
    
    
    
      // Create a payload
    
      const payload = {
    
        iss: opts.partnerApiKey,
    
        sub: opts.userId,
    
        iat: opts.currentTime || now,
    
        exp: opts.expiryTime || now + 60 * expiryInMinutes,
    
      };
    
    
    
    
      // Calculate a JWT
    
      return jwt.encode(payload, opts.partnerApiSecret);
    
    }
    
    
    
    
    const autoAuthToken = generateAutoAuthToken({
    
      partnerApiKey: "<partner_api_key>",
    
      partnerApiSecret: "<partner_api_secret>",
    
      userId: "<user_id>",
    
    });
    
    
    
    
    console.log(autoAuthToken);

JAVASCRIPT

Copy
