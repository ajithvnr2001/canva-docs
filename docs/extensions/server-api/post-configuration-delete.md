---
url: https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/
title: POST /configuration/delete - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:44.776829+00:00
---

# POST /configuration/delete - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/

App Development

[Overview](https://www.canva.dev/docs/extensions/)[Quickstart](https://www.canva.dev/docs/extensions/quickstart/)[Changelog](https://www.canva.dev/docs/extensions/changelog/)

Platform concepts

Apps

Extensions

[Regions](https://www.canva.dev/docs/extensions/platform-concepts/regions/)[Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/)[Deprecation policy](https://www.canva.dev/docs/extensions/platform-concepts/deprecation-policy/)

Extensions

Content extensions

Publish extensions

Backend development

Base URL

[Continuation](https://www.canva.dev/docs/extensions/backend-development/continuation/)

Signature verification

SDKs

Distribution

UX guidelines

[Submission checklist](https://www.canva.dev/docs/extensions/distribution/submission-checklist/)[Creating the App Directory listing](https://www.canva.dev/docs/extensions/distribution/app-directory-listing/)

Server API

[Overview](https://www.canva.dev/docs/extensions/server-api/server-api/)[GET /apps/configured](https://www.canva.dev/docs/extensions/server-api/get-apps-configured/)[POST /configuration](https://www.canva.dev/docs/extensions/server-api/post-configuration/)[POST /configuration/delete](https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/)[POST /content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/)[POST /publish/resources/find](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/)[POST /publish/resources/get](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/)[POST /publish/resources/upload](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/)[Redirect URL](https://www.canva.dev/docs/extensions/server-api/redirect-url/)

Reference

[Languages](https://www.canva.dev/docs/extensions/reference/supported-languages/)

# POST /configuration/delete

API reference for the "/configuration/delete" endpoint.

Copy page

If an app supports authentication, Canva sends a `POST` request to the following endpoint when a user disconnects the app from Canva:
    
    
    <authentication_base_url>/configuration/delete

BASH

Copy

The purpose of this request is to de-authenticate the user, allowing them to either re-authenticate with different credentials or to simply remove the connection between Canva and the app's backend.

When sending this request, Canva replaces `<authentication_base_url>` with the app's **Authentication base URL**. You can configure this URL via the app's **Authentication** page.

For guidelines on creating a delightful authentication flow, see [Optimizing the authentication flow](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/).

## Request

### Endpoint
    
    
    POST <authentication_base_url>/configuration/delete

BASH

Copy

### Headers

Property| Type| Required| Description  
---|---|---|---  
`X-Canva-Signatures`| string| Yes| A comma-separated list of request signatures. The name of this header is sometimes lowercase (e.g. `x-canva-signatures`).  
`X-Canva-Timestamp`| string| Yes| The UNIX timestamp (in seconds) of when Canva sent the request. The name of this header is sometimes lowercase (e.g. `x-canva-timestamp`).  
  
### Body

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`user`| string| Yes| The ID of the user.  
`brand`| string| Yes| The ID of the user's team.  
  
#### Example
    
    
    {
    
      "user": "<user>",
    
      "brand": "<brand>"
    
    }

JSON

Copy

## Responses

### 200 - Success

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"SUCCESS"`| Yes| The type of response.  
  
#### Example
    
    
    {
    
      "type": "SUCCESS"
    
    }

JSON

Copy

### 200 - Error

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"ERROR"`| Yes| The type of response.  
`errorCode`| string| Yes| An error code that describes what went wrong. **Enum:** `"CONFIGURATION_REQUIRED"`, `"FORBIDDEN"`, `"INTERNAL_ERROR"`, `"INVALID_REQUEST"`, `"NOT_FOUND"`, `"TIMEOUT"`  
  
#### Example
    
    
    {
    
      "type": "ERROR",
    
      "errorCode": "<error_code>"
    
    }

JSON

Copy

### 401 - Invalid request signature or timestamp

An extension must [verify the request signature and timestamp](https://www.canva.dev/docs/extensions/backend-development/verify-request/) of all incoming requests. When an extension can't verify either of these values, it must reject the request with a `401` status code.
