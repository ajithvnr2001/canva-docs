---
url: https://www.canva.dev/docs/apps/rest-apis/requests-responses/
title: API requests and responses - Canva for your platform - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:40.028384+00:00
---

# API requests and responses - Canva for your platform - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/requests-responses/

Canva for your platform

[About Canva's REST APIs](https://www.canva.dev/docs/apps/rest-apis/)

Fundamentals

[API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/)[Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/)[Capabilities](https://www.canva.dev/docs/apps/rest-apis/capabilities/)[API versions](https://www.canva.dev/docs/apps/rest-apis/versions/)

Development guides

[Autofill designs with data](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/)[Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/)

Design guidelines

[User experience guidelines](https://www.canva.dev/docs/apps/rest-apis/experience-guidelines/)[UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/)[Brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/)

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

## Asynchronous job endpoints

Some REST APIs are asynchronous. This means that the endpoint doesn't return the response immediately. Instead, it creates a job to process the request and returns a job ID that you can use to check the status of the job.

Asynchronous job APIs are usually those that might require additional server-side processing to complete, such as the [design import](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/) and [autofill](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/) APIs.

### Asynchronous job API workflow

The typical flow for using an asynchronous job API is as follows:

![Flow chart showing the flow of using an asynchronous job API](https://www.canva.dev/_next/static/media/async-api-flow-chart.dc8d5789.png)

  1. Submit a request to the 'Create [API name] job' API.

  2. If the request was valid, the API returns a response that includes a `job` with an `id`, and a `status` of `in_progress`.

For example:
         
         {
         
           "job": {
         
             "id": "450a76e7-f96f-43ae-9c37-0e1ce492ac72",
         
             "status": "in_progress"
         
           }
         
         }

JSON

Copy

  3. Use the job ID to poll the 'Get [API name] job' API until the job status changes from `in_progress` to either `success` or `failed`. For more information on polling, see [Job polling strategies](https://www.canva.dev/docs/apps/rest-apis/requests-responses/#job-polling-strategies).

For successful jobs, the response also includes the result of the job. For example:
         
         {
         
           "job": {
         
             "id": "450a76e7-f96f-43ae-9c37-0e1ce492ac72",
         
             "status": "success",
         
             ...
         
           }
         
         }

JSON

Copy

  4. Use the result of the finished job to do the next steps in your app. For example, if you used the design import API, you can use the returned design ID to show the design thumbnail in your app.




### Job polling strategies

You should poll a 'Get [API name] job' API at an interval that's short enough to provide a good user experience, but not too short to hit rate limits for the particular API.

We recommend that you use an [exponential backoff⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Exponential_backoff) strategy to poll the job status. This means that you should start with a short poll interval, then exponentially increase the time between each poll, up to a maximum interval. For an example implementation, see the [starter kit for the Canva REST APIs⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-connect-api-starter-kit/blob/main/demos/common/utils/poll.ts).

## Trial quotas

Trial quotas are currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview features won't produce a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/).
  * Public apps that use preview features will not pass the review process, and can't be made available to all Canva users.



Trial quotas provide users on free Canva plans with temporary access to certain premium APIs that are normally restricted to paid plans. These trials allow users to evaluate premium functionality before upgrading their subscription.

Trials have specific quotas for each API. For example, for each user, a trial might allow 2 uses in a lifetime, or 2 uses per month.

For APIs that offer trial quotas, the trial quota information is documented in the API's reference documentation. Check individual API endpoints to see if they offer trial quotas and their usage limits.

### Example of trial quotas

For example, a free user might receive a trial quota of 2 resize operations for their lifetime. This allows them to test the [resize API](https://www.canva.dev/docs/apps/rest-apis/reference/resizes/) before deciding whether to upgrade to a paid plan.

The API response for a premium endpoint used during a trial includes trial information:
    
    
    {
    
      "job": {
    
        "id": "37e319c0-2134-493a-9861-1f89befde04d",
    
        "status": "in_progress"
    
      },
    
      "trial_information": {
    
        "uses_remaining": 1,
    
        "upgrade_url": "https://www.canva.com/?tailoringUpsellDialog=GENERIC_C4W&utm_source=canva_connect_api_resize"
    
      }
    
    }

JSON

Copy

### Managing trial quotas

When a user's trial quota is exhausted, subsequent requests to premium endpoints will return an error response:
    
    
    HTTP 403
    
    
    
    
    {
    
      "code": "permission_denied",
    
      "message": "You have reached your limit for this trial. For full access to this feature Upgrade to Pro https://www.canva.com/?tailoringUpsellDialog=GENERIC_C4W&utm_source=canva_connect_api_resize."
    
    }

JSON

Copy
