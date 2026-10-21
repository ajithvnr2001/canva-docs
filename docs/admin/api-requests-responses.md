---
url: https://www.canva.dev/docs/admin/api-requests-responses/
title: API requests and responses - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:38.507990+00:00
---

# API requests and responses - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-requests-responses/

Getting started

[Overview](https://www.canva.dev/docs/admin/)[Creating clients](https://www.canva.dev/docs/admin/creating-clients/)

Fundamentals

[API requests & responses](https://www.canva.dev/docs/admin/api-requests-responses/)[Authentication](https://www.canva.dev/docs/admin/authentication/)[Canva concepts](https://www.canva.dev/docs/admin/canva-concepts/)

API reference

Authentication

Organizations

Teams

Groups

Users

Audit events

Appendix

[Scopes](https://www.canva.dev/docs/admin/appendix/scopes/)[Error responses](https://www.canva.dev/docs/admin/error-responses/)[Changelog](https://www.canva.dev/docs/admin/changelog/)

# API requests and responses

Copy page

API requests (submitted to an API endpoint) tell the endpoint to do something. Once the request is processed, the API endpoint sends a response.

To make API requests, you must know the HTTP method, URL path, and parameters for the endpoint that you want to use.

An API request consists of the combination of the following:

`HTTP method + URL path of the endpoint + request parameters`

This article shows examples using [curl⁠(opens in a new tab or window)](https://curl.se/) requests. Curl is a command line tool, used to send requests using URL syntax. You can use curl _flags_ to execute a specific action in curl.

## HTTP method and URL path

An _HTTP method_ is the operation that you want the endpoint to execute. REST [HTTP methods⁠(opens in a new tab or window)](https://www.restapitutorial.com/introduction/httpmethods) can be:

  * POST (create)
  * GET (read)
  * PUT (update/replace)
  * PATCH (update/modify)
  * DELETE (delete).



The _URL path_ is the HTTP URL where the endpoint can be accessed.

### Example curl request

Use the `--request` flag followed by the HTTP method and the URL path.

For example, the HTTP method for generating an access token is `POST` and the URL path for the endpoint is `https://api.canva.com/rest/v1/oauth/token`. The curl request for generating an access token looks like the following:
    
    
    curl --request POST 'https://api.canva.com/rest/v1/oauth/token'

SH

Copy

## Request parameters

Request parameters are the options that you can pass to the endpoints to influence the response. Parameters help single out the data that you want to receive from the endpoint. Most requests need you to pass parameters and their values.

Parameters can be of the following types:

  * `required` (the request cannot go through without the parameter)
  * `optional` (the parameter value is supplemented with the default value)



We use the following parameters in Canva REST APIs:

### Path parameters

Path parameters are a part of the endpoint itself. They are usually formatted with curly braces and are required.

#### Example of path parameters

For example, the path parameter for getting folder information from the REST API folder endpoint is `{folderID}`.

The curl request is:
    
    
    curl --request GET 'https://api.canva.com/rest/v1/folders/{folderId}' \
    
    --header 'Authorization: Bearer {token}'

SH

Copy

### Query parameters

Query parameters are included in the query string of the endpoint. A query string starts with `?` and lists parameters one after another, separated by `&`.

#### Example of query parameters

For example, the required query parameters for the REST API `/authorize` endpoint are `code_challenge`, `code_challenge_method`, and so on. The URL path becomes:

`https://www.canva.com/api/oauth/authorize?code_challenge=<code challenge string>&code_challenge_method=s256...`

### Header parameters

Header parameters are included in the HTTP request headers. They include information such as the authorization, connection type, proxies, and content type of the request.

#### Example header parameters

When using curl, use the `--header` flag followed by the header in `key:value` format.

For example, the header parameter for the REST API `/token` endpoint is `Content-Type` with the value `application/x-www-form-urlencoded`.

The curl request becomes:
    
    
    curl --request POST 'https://api.canva.com/rest/v1/oauth/token' \
    
    --header 'Content-Type:application/x-www-form-urlencoded'

SH

Copy

### Body parameters

Body parameters are included in the request body, and are used to send data to the API endpoints. These parameters are usually sent as JSON objects in `POST`, `PUT`, or `PATCH` requests.

#### Example body parameters

When using curl, use the `--data-<type>` flag followed by the parameter in the `parameter=value` format.

For example, the body parameters for the REST API `/token` endpoint are `grant_type`, `code_verifier`, `code`, and so on.

The curl request becomes:
    
    
    curl --request POST 'https://api.canva.com/rest/v1/oauth/token' \
    
    --header 'Content-Type: application/x-www-form-urlencoded' \
    
    --data-urlencode 'grant_type=authorization_code' \
    
    --data-urlencode 'code_verifier=<code verifier>' \
    
    ...

SH

Copy

## API responses

API responses indicate whether an API request was successful. A response consists of an HTTP response status code and a response body that includes either a successful response or an error response.

An API response consists of the combination of the following:

`HTTP response status code + response body (success response or error response)`

### HTTP response status code

[HTTP response status codes⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) indicate whether your request was successful. They include the following types:

**Description**| **Status code**  
---|---  
Informational response| 100 - 199  
Successful response| 200 - 299  
Redirection message| 300 - 399  
Client error response| 400 - 499  
Server error response| 500 - 599  
  
### Response body

Many requests return a response body in JSON format. The responses can include the following types:

#### Success response

If your API request has completed successfully, you'll receive a success response that includes the required properties, usually in JSON format.

For example, the success response for the REST API `/token` endpoint is:
    
    
    {
    
      "access_token": "...",
    
      "token_type": "bearer",
    
      "expires_in": "...",
    
      "scope": "...",
    
      "refresh_token": "..."
    
    }

JSON

Copy

#### Error response

If your API request doesn't complete successfully, you'll get an error response that consists of the following:

  * Error HTTP status code
  * Error code (usually includes different information to the status code)
  * Error message



For example, an error response can look like this:
    
    
    HTTP 404
    
    
    
    
    {
    
      "code": "design_not_found",
    
      "message": "Design with id 'ABCD' not found"
    
    }

JSON

Copy
