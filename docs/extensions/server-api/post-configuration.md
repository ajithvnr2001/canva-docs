---
url: https://www.canva.dev/docs/extensions/server-api/post-configuration/
title: POST /configuration - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:44.580631+00:00
---

# POST /configuration - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/server-api/post-configuration/

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

# POST /configuration

API reference for the "/configuration" endpoint.

Copy page

If an app supports authentication and has a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/), Canva sends a `POST` request to the following endpoint when a user opens the extension:
    
    
    <authentication_base_url>/configuration

BASH

Copy

The purpose of this request is to check if the user is authenticated with the destination platform.

If the user is authenticated, the extension continues to load. If the user is not authenticated, Canva renders a **Connect** button. The user can click this button to start the authentication flow.

To learn more, refer to [Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).

## Notes

  * Extensions must respond to this request within 8 seconds.
  * When sending this request, Canva replaces `<authentication_base_url>` with the app's **Authentication base URL**. You can configure the **Authentication base URL** via the app's **Authentication** page.
  * Extensions should meet the [UX guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/).



## Request

### Endpoint
    
    
    POST <authentication_base_url>/configuration

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

### 200 - Success (user is authenticated)

The response the app provides when the user is authenticated with the destination platform.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"SUCCESS"`| Yes| The type of response.  
`labels`| array| Yes| The extension points the user has authenticated with.  
  
#### Example
    
    
    {
    
      "labels": [],
    
      "type": "SUCCESS"
    
    }

JSON

Copy

### 200 - Error (user not authenticated)

The response the app provides when the user is not authenticated with the destination platform.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"ERROR"`| Yes| The type of response.  
`errorCode`| `"CONFIGURATION_REQUIRED"`| Yes| An error code that describes what went wrong.  
  
#### Example
    
    
    {
    
      "type": "ERROR",
    
      "errorCode": "CONFIGURATION_REQUIRED"
    
    }

JSON

Copy

### 200 - Error (other)

The response the app provides when an error occurs.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"ERROR"`| Yes| The type of response.  
`errorCode`| string| Yes| An error code that describes what went wrong. **Enum:** `"FORBIDDEN"`, `"INTERNAL_ERROR"`, `"INVALID_REQUEST"`, `"NOT_FOUND"`, `"TIMEOUT"`  
  
#### Example
    
    
    {
    
      "type": "ERROR",
    
      "errorCode": "<error_code>"
    
    }

JSON

Copy

### 401 - Invalid request signature or timestamp

An extension must [verify the request signature and timestamp](https://www.canva.dev/docs/extensions/backend-development/verify-request/) of all incoming requests. When an extension can't verify either of these values, it must reject the request with a `401` status code.
