---
url: https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/
title: Generate an access token - Requests to Canva - Canva Print API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:31.995337+00:00
---

# Generate an access token - Requests to Canva - Canva Print API Documentation

> Source: https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/

Requests to Canva

[Overview](https://www.canva.dev/docs/print/api-reference/requests-to-canva/)[Generate access token](https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/)[Create order production event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-production-event/)[Create order shipment event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-shipment-event/)[Create order cost summary event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-cost-summary-event/)[Create order error event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-error-event/)[Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/)

# Generate an access token

Copy page

This endpoint implements the OAuth 2.0 `token` endpoint, as part of the [Client Credentials flow⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4). It lets you generate an access token that is used to authenticate requests to other endpoints in the Canva Print API.

Requests to this endpoint require authentication with your OAuth client ID and client secret, which were provided to you during the print partner onboarding process.

You must use [basic access authentication⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Basic_access_authentication), where the `{credentials}` string must be a Base64 encoded value of `{client id}:{client secret}`.

## HTTP method and URL path

POST` https://api.canva.com/auth/v1/oauth/token`

## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of [basic access authentication⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Basic_access_authentication). The `{credentials}` string must be a Base64 encoded value of `{client id}:{client secret}`.

For example: `Authorization: Basic {credentials}`

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/x-www-form-urlencoded`.

For example: `Content-Type: application/x-www-form-urlencoded`

## Body parameters

`grant_type``string`

Required

Must be set to `client_credentials`.

## Example request

Examples for using the `/v1/oauth/token` endpoint:
    
    
    curl --request POST 'https://api.canva.com/auth/v1/oauth/token' \
    
    --header 'Authorization: Basic {credentials}' \
    
    --header 'Content-Type: application/x-www-form-urlencoded' \
    
    --data-urlencode 'grant_type=client_credentials'

SH

Copy

## Success response

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`access_token``string`

The bearer access token to use to authenticate to Canva Print API endpoints.

`token_type``string`

The token type returned. This is always `Bearer`.

`expires_in``integer`

The expiry time (in seconds) for the token.

### Example response
    
    
    {
    
      "access_token" : "JagALLazU0i2ld9WW4zTO4kaG0lkvP8Y5sSO206Z",
    
      "token_type" : "Bearer",
    
      "expires_in" : 14400
    
    }

JSON

Copy

## Error responses

### 400 Invalid request. For example, missing parameters.

### 401 Invalid or unauthorized client ID or secret.
