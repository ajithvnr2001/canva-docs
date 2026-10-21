---
url: https://www.canva.dev/docs/admin/api-reference/oauth/generate-access-token/
title: Generate an access token - Authentication - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:33.042102+00:00
---

# Generate an access token - Authentication - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/oauth/generate-access-token/

Authentication

[Generate access token](https://www.canva.dev/docs/admin/api-reference/oauth/generate-access-token/)

# Generate an access token

Copy page

This endpoint implements the OAuth 2.0 `token` endpoint, as part of the [Client Credentials flow⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4). It lets you generate an access token that's used to authenticate requests to resource endpoints in the Canva Admin API.

Requests to this endpoint require authentication with your Admin API client ID and client secret.

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

`scope``string`

Optional

Optional scope value. Separate multiple [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) with a single space between each scope.

The requested scope can't include any scopes that aren't selected in the client settings. Providing a subset of the client's scopes lets you limit the permissions for a token.

If this parameter is omitted, the token that is generated includes **all** the scopes that are selected in the client settings.

We strongly recommend that you always specify the scope that you want to include in the token.

## Example request

Examples for using the `/v1/oauth/token` endpoint:
    
    
    curl --request POST 'https://api.canva.com/auth/v1/oauth/token' \
    
    --header 'Authorization: Basic {credentials}' \
    
    --header 'Content-Type: application/x-www-form-urlencoded' \
    
    --data-urlencode 'grant_type=client_credentials' \
    
    --data-urlencode 'scope=admin:user:read admin:organization:read'

SH

Copy

## Success response

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`access_token``string`

The bearer access token to use to authenticate to Admin API endpoints.

`token_type``string`

The token type returned. This is always `Bearer`.

`expires_in``integer`

The expiry time (in seconds) for the token.

### Example response
    
    
    {
    
      "access_token" : "eyJraWQiOiI2OWMwYzgwNS1lNGQwLTQyNDgtOWQzZi0yODEyZTI2OGYwM2UiL",
    
      "token_type" : "Bearer",
    
      "expires_in" : 14400
    
    }

JSON

Copy
