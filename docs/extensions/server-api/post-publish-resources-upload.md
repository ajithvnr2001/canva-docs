---
url: https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/
title: POST /publish/resources/upload - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:46.502960+00:00
---

# POST /publish/resources/upload - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/

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

# POST /publish/resources/upload

API reference for the "/publish/resources/upload" endpoint.

Copy page

When a user publishes their design via a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/), Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/publish/resources/upload

BASH

Copy

The purpose of the request is to upload the user's design to the destination platform.

The body of the request includes an array of [assets](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/#asset). If a user publishes their design as a JPG or PNG, each page of the design is a separate asset. If the user publishes their design as a PDF or PPTX, the entire design is a single asset.

Each asset has a URL, which the extension must use to download the asset and upload it to the destination platform.

## Notes

  * Extensions must respond to this request within 8 seconds.
  * When sending this request, Canva replaces `<base_url>` with the extension's **Base URL**. You can configure the **Base URL** via the Developer Portal.
  * If a user publishes a design that contains embedded media, such as a YouTube video or Instagram photo, Canva temporarily caches that media. If the user re-publishes their design, any changes to the underlying media (for example, a new thumbnail for a YouTube video) may not be reflected in the published design. The cache duration is approximately 24 hours.
  * Extensions should meet the [UX guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/).



## Request

### Endpoint
    
    
    POST <base_url>/publish/resources/upload

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
`message`| string| No| A message the user provides before publishing their design. To use this feature, enable **Requires custom message** via the Developer Portal.  
`parent`| string| No| The ID of the selected container.  
`user`| string| Yes| The ID of the user.  
`brand`| string| Yes| The ID of the user's team.  
`label`| string| Yes| The type of extension that sent the request.  
`assets`| Array<[Asset](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/#asset)>| Yes| The assets to upload to the destination platform.  
`designId`| string| Yes| The ID of the user's design. This ID does not change if the user republishes their design.  
  
#### Example
    
    
    {
    
      "assets": [],
    
      "user": "<user>",
    
      "brand": "<brand>",
    
      "label": "<label>",
    
      "designId": "<design_id>"
    
    }

JSON

Copy

## Responses

### 200 - Success

The response an extension provides when it successfully uploads the published assets to the destination platform.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"SUCCESS"`| Yes| The type of response.  
`url`| string| No| The URL of a web page where the user can see their published assets on the destination platform. This must be fewer than 2000 characters.  
  
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

### Asset

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`name`| string| Yes| The file name of the asset (including the file extension).  
`type`| string| Yes| The file type of the asset. **Enum:** `"JPG"`, `"PNG"`, `"PDF"`, `"PPTX"`  
`url`| string| Yes| The URL of the asset.  
  
#### Example
    
    
    {
    
      "name": "<name>",
    
      "type": "<type>",
    
      "url": "<url>"
    
    }

JSON

Copy
