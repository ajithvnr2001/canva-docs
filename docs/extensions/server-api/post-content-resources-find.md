---
url: https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/
title: POST /content/resources/find - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:45.473690+00:00
---

# POST /content/resources/find - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/

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

# POST /content/resources/find

API reference for the "/content/resources/find" endpoint.

Copy page

When a user interacts with a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/), Canva sends `POST` requests to the following endpoint:
    
    
    <base_url>/content/resources/find

BASH

Copy

Specifically, Canva sends this request when a user:

  * Opens an extension.
  * Opens a container.
  * Paginates through resources.
  * Searches for content.



The purpose of this request is to retrieve content that Canva can display in the side panel of the editor, such as [images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/), [embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/), or [containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/).

The `types` property in the request body determines the type of resources the extension can provide in the response. For example, when value of the `types` includes `"IMAGE"`, the endpoint can respond with [image resources](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#image).

## Notes

  * Extensions must respond to this request within 8 seconds.
  * When sending this request, Canva replaces `<base_url>` with the extension's **Base URL**. You can configure the **Base URL** via the Developer Portal.
  * To configure the type of resources that Canva expects the extension to provide, change the extension's **Content type** via the Developer Portal.
  * Extensions should meet the [UX guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/).



## Request

### Endpoint
    
    
    POST <base_url>/content/resources/find

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
`limit`| number| Yes| The maximum number of resources to provide in a response.  
`locale`| string| Yes| The user's locale as an [IETF BCP 47 language tag⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/IETF_language_tag).  
`type` (deprecated)| string| Yes| The type of resources the extension must provide in the response. **Enum:** `"CONTAINER"`, `"EMBED"`, `"IMAGE"`, `"VIDEO"`  
`types`| Array<string>| Yes| The types of resources the extension can provide in the response. **Enum:** `"CONTAINER"`, `"EMBED"`, `"IMAGE"`, `"VIDEO"`  
`continuation`| string| No| A token for paginating resources.  
`containerId`| string| No| The ID of the selected container.  
`query`| string| No| A user-provided search query.  
  
#### Example
    
    
    {
    
      "limit": 100,
    
      "user": "<user>",
    
      "brand": "<brand>",
    
      "label": "<label>",
    
      "locale": "<locale>",
    
      "types": "<types>"
    
    }

JSON

Copy

## Responses

### 200 - Success (containers)

The response an extension must provide when the `types` property in the request body includes `"CONTAINER"`.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"SUCCESS"`| Yes| The type of response.  
`resources`| Array<[Container](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#container)>| Yes| The containers to render in the side panel.  
`continuation`| string| No| A token for paginating resources.  
  
#### Example
    
    
    {
    
      "resources": [],
    
      "type": "SUCCESS"
    
    }

JSON

Copy

### 200 - Success (embeds)

The response an extension must provide when the `types` property in the request body includes `"EMBED"`.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"SUCCESS"`| Yes| The type of response.  
`resources`| Array<[Embed](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#embed)>| Yes| The embeds to render in the side panel.  
`continuation`| string| No| A token for paginating resources.  
  
#### Example
    
    
    {
    
      "resources": [],
    
      "type": "SUCCESS"
    
    }

JSON

Copy

### 200 - Success (images)

The response an extension must provide when the `types` property in the request body includes `"IMAGE"`.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"SUCCESS"`| Yes| The type of response.  
`resources`| Array<[Image](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#image)>| Yes| The images to render in the side panel.  
`continuation`| string| No| A token for paginating resources.  
  
#### Example
    
    
    {
    
      "resources": [],
    
      "type": "SUCCESS"
    
    }

JSON

Copy

### 200 - Success (videos)

The response an extension must provide when the `types` property in the request body includes `"VIDEO"`.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`type`| `"SUCCESS"`| Yes| The type of response.  
`resources`| Array<[Video](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#video)>| Yes| The videos to render in the side panel.  
`continuation`| string| No| A token for paginating resources.  
  
#### Example
    
    
    {
    
      "resources": [],
    
      "type": "SUCCESS"
    
    }

JSON

Copy

### 200 - Error

The response an extension provides when it can't provide the requested resources.

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

### Container

Represents a container (folder) that Canva renders in the side panel. When a user selects a container, Canva sends a request for resources that belong to the container.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`thumbnail`| [Thumbnail](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#thumbnail)| No| A thumbnail for the container.  
`id`| string| Yes| A unique ID for the container. The ID must be less than 100 characters.  
`name`| string| Yes| A human readable name for the container. The name must be equal to or less than 200 characters.  
`type`| `"CONTAINER"`| Yes| The type of resource.  
  
#### Example
    
    
    {
    
      "id": "<id>",
    
      "name": "<name>",
    
      "type": "CONTAINER"
    
    }

JSON

Copy

### Embed

Represents embeddable media that Canva renders in the side panel, such as a YouTube video or Instagram photo. When a user selects an embed, Canva adds it to their design.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`id`| string| Yes| A unique ID for the embed. The ID must be less than 100 characters.  
`name`| string| Yes| A human readable name for the embed. The name must be equal to or less than 200 characters.  
`type`| `"EMBED"`| Yes| The type of resource.  
`url`| string| Yes| The URL of the embeddable media. This URL must be HTTPS-enabled, supported by [Iframely⁠(opens in a new tab or window)](https://iframely.com/docs/providers), and less than 2048 characters.  
`thumbnail`| [Thumbnail](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#thumbnail)| Yes| A thumbnail for the embed.  
  
#### Example
    
    
    {
    
      "id": "<id>",
    
      "name": "<name>",
    
      "type": "EMBED",
    
      "url": "<url>",
    
      "thumbnail": {
    
        "url": "<url>"
    
      }
    
    }

JSON

Copy

### Image

Represents an image file that Canva renders in the side panel, such as a PNG or SVG.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`id`| string| Yes| A unique ID for the image. This ID must always refer to the same image file and be less than 100 characters. If the image file is modified, assign it a new ID.  
`name`| string| Yes| A human readable name for the image. The name must be equal to or less than 200 characters.  
`type`| `"IMAGE"`| Yes| The type of resource.  
`url`| string| Yes| The URL of the full-resolution image. This URL must be HTTPS-enabled, not redirect to a different URL, and be less than 2048 characters. The MIME type of the image must match the type specified in the `contentType` property. The image must meet Canva's [file upload requirements⁠(opens in a new tab or window)](https://www.canva.com/help/article/upload-formats-requirements).  
`contentType`| string| Yes| The MIME type of the image. **Enum:** `"image/jpeg"`, `"image/png"`, `"image/svg+xml"`, `"image/heic"`  
`thumbnail`| [Thumbnail](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#thumbnail)| Yes| A thumbnail for the image. This thumbnail must have the same aspect ratio as the full-resolution image.  
  
#### Example
    
    
    {
    
      "id": "<id>",
    
      "name": "<name>",
    
      "type": "IMAGE",
    
      "url": "<url>",
    
      "contentType": "<content_type>",
    
      "thumbnail": {
    
        "url": "<url>"
    
      }
    
    }

JSON

Copy

### Video

Represents a video file that Canva renders in the side panel, such as an MP4 or MOV file.

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`id`| string| Yes| A unique ID for the video. This ID must always refer to the same video file and be less than 100 characters. If the video file is modified, assign it a new ID.  
`name`| string| Yes| A human readable name for the video. The name must be less than 100 characters.  
`type`| `"VIDEO"`| Yes| The type of resource.  
`url`| string| Yes| The URL of the full-resolution video. This URL must be HTTPS-enabled, not redirect to a different URL, and be less than 2048 characters. The MIME type of the video must match the type specified in the `contentType` property. The video must meet Canva's [file upload requirements⁠(opens in a new tab or window)](https://www.canva.com/help/article/upload-formats-requirements).  
`contentType`| string| Yes| The MIME type of the video. **Enum:** `"video/mov"`, `"image/gif"`, `"video/mpeg"`, `"video/x-matroska"`, `"video/webm"`, `"video/mp4"`  
`width`| number| Yes| The width of the full-resolution video, in pixels.  
`height`| number| Yes| The height of the full-resolution video, in pixels.  
`durationMs`| number| Yes| The duration of the video, in milliseconds.  
`thumbnail`| [Thumbnail](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#thumbnail)| Yes| A thumbnail for the video. This thumbnail must have the same aspect ratio as the full-resolution video.  
  
#### Example
    
    
    {
    
      "width": 0,
    
      "height": 0,
    
      "durationMs": 0,
    
      "id": "<id>",
    
      "name": "<name>",
    
      "type": "VIDEO",
    
      "url": "<url>",
    
      "contentType": "<content_type>",
    
      "thumbnail": {
    
        "url": "<url>"
    
      }
    
    }

JSON

Copy

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
