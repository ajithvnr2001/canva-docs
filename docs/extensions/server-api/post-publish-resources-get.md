---
url: https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/
title: POST /publish/resources/get - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:46.201329+00:00
---

# POST /publish/resources/get - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/

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

# POST /publish/resources/get

API reference for the "/publish/resources/get" endpoint.

Copy page

If a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) uses the [Flat list](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/) or [Nested list](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/) layout, the user can select a container (folder) before publishing their design. If the user selects a container, Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/publish/resources/get

BASH

Copy

Canva sends the request immediately before sending the request to the [`/publish/resources/upload`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/) endpoint.

The purpose of the request is to verify that:

  * The selected container still exists on the destination platform.
  * The user still has access to the selected container.



If the extension can't verify the existence of the container or the permissions of the user, Canva shows an error to the user and doesn't continue the publishing process.

## Notes

  * Extensions must respond to this request within 8 seconds.
  * When sending this request, Canva replaces `<base_url>` with the extension's **Base URL**. You can configure the **Base URL** via the Developer Portal.
  * Extensions should meet the [UX guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/).



## Request

### Endpoint
    
    
    POST <base_url>/publish/resources/get

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
`label`| string| Yes| The type of extension that sent the request.  
`id`| string| Yes| The ID of the selected container.  
`preferredThumbnailHeight`| integer| Yes| The recommended height , in pixels of any thumbnails in the response.  
`preferredThumbnailWidth`| integer| Yes| The recommended width , in pixels of any thumbnails in the response.  
  
#### Example
    
    
    {
    
      "preferredThumbnailHeight": 500,
    
      "preferredThumbnailWidth": 500,
    
      "user": "<user>",
    
      "brand": "<brand>",
    
      "label": "<label>",
    
      "id": "<id>"
    
    }

JSON

Copy

## Responses

### 200 - Success

The response an extension provides when the selected container still exists on the destination platform.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"SUCCESS"`| Yes| The type of response.  
`resource`| object| Yes|   
`resource.id`| string| Yes| A unique ID for the resource.  
`resource.name`| string| Yes| A human readable name for the resource.  
`resource.type`| string| Yes| The type of resource. Canva renders `"CONTAINER"` resources as folders and `"IMAGE"` resources as files. **Enum:** `"CONTAINER"`, `"IMAGE"`  
`resource.thumbnail`| [Thumbnail](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/#thumbnail)| No| A thumbnail image.  
`resource.isOwner`| boolean| Yes| A value of `true` indicates that the user is the owner of the resource.  
`resource.readOnly`| boolean| Yes| A value of `true` indicates that the user has read-only access to the resource.  
  
#### Example
    
    
    {
    
      "resource": {
    
        "isOwner": true,
    
        "readOnly": true,
    
        "id": "<id>",
    
        "name": "<name>",
    
        "type": "<type>"
    
      },
    
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

## Schemas

### Thumbnail

A thumbnail image.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`url`| string| Yes| The URL of the thumbnail. This URL must be HTTPS-enabled and less than 2048 characters.  
`height`| number| No| The height of the thumbnail, in pixels. If you provide a height, you must provide a width.  
`width`| number| No| The width of the thumbnail, in pixels. If you provide a width, you must provide a height.  
  
#### Example
    
    
    {
    
      "url": "<url>"
    
    }

JSON

Copy
