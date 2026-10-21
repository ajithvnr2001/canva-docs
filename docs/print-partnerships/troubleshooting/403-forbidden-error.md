---
url: https://www.canva.dev/docs/print-partnerships/troubleshooting/403-forbidden-error/
title: Forbidden (403) - Troubleshooting - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:03.206059+00:00
---

# Forbidden (403) - Troubleshooting - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/troubleshooting/403-forbidden-error/

Troubleshooting

[Forbidden (403)](https://www.canva.dev/docs/print-partnerships/troubleshooting/403-forbidden-error/)

# Forbidden (403)

Copy page

When creating an integration, you may encounter the following **Forbidden (403)** error:

![](https://www.canva.dev/_next/static/media/the-403-forbidden-error.bf0b498f.jpg)

This error can occur for a few different reasons.

## Design permissions

A user can only edit a design that they created. If you call the [`editDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/) method and pass through a `designId` of a design not created by the current user, Canva responds with a `403` error.

## Domain restrictions

By default, an integration's [API keys](https://www.canva.dev/docs/print-partnerships/concepts/credentials/) are locked to the following domains:

  * canva.com
  * localhost



If requests don't originate from these domains, Canva responds to the requests with a `403` error.

To use the API keys from other domains, you need to request Canva to add the domains to the allowlist.

To raise a request:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **Integration support**.
  3. In the **Domains** field, list the other domains.



### Referrer-Policy HTTP header

When an integration loads the product catalog, the request that's sent to Canva must include the `Referer` HTTP header. Canva uses the `Referer` header to identify if the integration's domain is on the allowlist.

Sometimes though, the `Referrer-Policy` header is set to a value that prevents Canva from receiving the `Referer` header:
    
    
    Referrer-Policy: no-referrer
    
    Referrer-Policy: no-referrer-when-downgrade

Copy

As a result, Canva can't confirm if the origin domain is on the allowlist and blocks the request, causing the 403 error.

To fix this problem, we generally recommend setting the `Referrer-Policy` header to the `strict-origin-when-cross-origin` header. This ensures that the origin is sent with cross-origin requests, which allows Canva to verify if the origin domain is on the allowlist.

For more information, refer to [Referrer-Policy⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy).

## Invalid autoAuthToken

When initializing the Partnership SDK, an integration needs to provide an autoAuthToken:
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    })();

JAVASCRIPT

Copy

If this token is invalid, Canva responds with a `403` error.

These are some reasons why an autoAuthToken might be invalid:

### Calculating a token with incorrect values

When calculating a token, double-check the following values

  * The integration's [Partner API key](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-key).
  * The integration's [Partner API secret](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-secret).
  * The ID of the end user (that is, the ID of the partner's customer).
  * The "issued at" time of the token as a UNIX timestamp (in seconds).
  * The "expires at" time of the token as a UNIX timestamp (in seconds).



Are the values accurate? Are they of the correct type?

### Calculating a token with mismatched credentials

Verify that the Partner API key and Partner API secret are for the same environment. You can't, for instance, calculate a token using the "production" API key and the "test" API secret.

Partners are charged for their API usage when using the "production" API keys, so be sure to only use "test" API keys during the development and testing phase. To learn more, refer to [Credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/).

### Calculating a token with an "issued at" time that's in the future

There is some leniency, as it's possible for server clocks to not be perfectly synchronized, but the "issued at" time should be as accurate as reasonably possible.

### Calculating a token with an "expires at" time that's more than 12 hours in the future

The Partnership SDK requires autoAuthTokens to expire in 12 hours or less.

### Calculating more than 5 tokens from the same IP in under an hour

You can't calculate more than 5 autoAuthTokens from the same IP address in under an hour. If end users are returning to an integration more than 5 times per hour, you can avoid reaching this limit by saving the autoAuthToken in a cookie or via local storage.
