---
url: https://www.canva.dev/docs/apps/api/v1/asset-upload/
title: upload - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:27.364255+00:00
---

# upload - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/asset-upload/

API reference

v1 (Deprecated)

Asset

[getTemporaryUrl](https://www.canva.dev/docs/apps/api/v1/asset-get-temporary-url/)[findFonts](https://www.canva.dev/docs/apps/api/v1/asset-find-fonts/)[openColorSelector](https://www.canva.dev/docs/apps/api/v1/asset-open-color-selector/)[requestFontSelection](https://www.canva.dev/docs/apps/api/v1/asset-request-font-selection/)[upload](https://www.canva.dev/docs/apps/api/v1/asset-upload/)

Design

[addAudioTrack](https://www.canva.dev/docs/apps/api/v1/design-add-audio-track/)[addNativeElement](https://www.canva.dev/docs/apps/api/v1/design-add-native-element/)[addPage](https://www.canva.dev/docs/apps/api/v1/design-add-page/)[getCurrentPageContext](https://www.canva.dev/docs/apps/api/v1/design-get-current-page-context/)[getDefaultPageDimensions](https://www.canva.dev/docs/apps/api/v1/design-get-default-page-dimensions/)[getDesignToken](https://www.canva.dev/docs/apps/api/v1/design-get-design-token/)[initAppElement](https://www.canva.dev/docs/apps/api/v1/design-init-app-element/)[overlay.registerOnCanOpen](https://www.canva.dev/docs/apps/api/v1/design-overlay-register-on-can-open/)[requestExport](https://www.canva.dev/docs/apps/api/v1/design-request-export/)[selection.registerOnChange](https://www.canva.dev/docs/apps/api/v1/design-selection-register-on-change/)[setCurrentPageBackground](https://www.canva.dev/docs/apps/api/v1/design-set-current-page-background/)[ui.makeDraggable](https://www.canva.dev/docs/apps/api/v1/design-ui-make-draggable/)[ui.startDrag](https://www.canva.dev/docs/apps/api/v1/design-ui-start-drag/)

Platform

[appProcess](https://www.canva.dev/docs/apps/api/v1/platform-app-process/)[appProcess.broadcastMessage](https://www.canva.dev/docs/apps/api/v1/platform-app-process-broadcast-message/)[appProcess.current](https://www.canva.dev/docs/apps/api/v1/platform-app-process-current/)[appProcess.current.getInfo](https://www.canva.dev/docs/apps/api/v1/platform-app-process-current-get-info/)[appProcess.current.requestClose](https://www.canva.dev/docs/apps/api/v1/platform-app-process-current-request-close/)[appProcess.current.setOnDispose](https://www.canva.dev/docs/apps/api/v1/platform-app-process-current-set-on-dispose/)[appProcess.requestClose](https://www.canva.dev/docs/apps/api/v1/platform-app-process-request-close/)[appProcess.registerOnMessage](https://www.canva.dev/docs/apps/api/v1/platform-app-process-register-on-message/)[appProcess.registerOnStateChange](https://www.canva.dev/docs/apps/api/v1/platform-app-process-register-on-state-change/)[getPlatformInfo](https://www.canva.dev/docs/apps/api/v1/platform-get-platform-info/)[requestOpenExternalUrl](https://www.canva.dev/docs/apps/api/v1/platform-request-open-external-url/)

User

[auth.getCanvaUserToken](https://www.canva.dev/docs/apps/api/v1/user-auth-get-canva-user-token/)[auth.requestAuthentication](https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/)

# upload

API reference for the upload method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Uploads an asset, such as an image or video file, to Canva's backend.

To learn more, see [Assets](https://www.canva.dev/docs/apps/uploading-assets/).

## Usage

### Uploading audio
    
    
    import { upload } from "@canva/asset";
    
    
    
    
    // Start uploading the file
    
    const audio = await upload({
    
      type: "AUDIO",
    
      title: "Example audio",
    
      mimeType: "audio/mp3",
    
      durationMs: 86047,
    
      url: "https://www.canva.dev/example-assets/audio-import/audio.mp3",
    
    });
    
    
    
    
    // Get a reference to the asset in Canva's backend
    
    console.log("The asset reference is", audio.ref);
    
    
    
    
    // Wait for the upload to complete
    
    await audio.whenUploaded();
    
    console.log("The upload is complete.");

TS

Copy

### Uploading images
    
    
    import { upload } from "@canva/asset";
    
    
    
    
    // Start uploading the file
    
    const image = await upload({
    
      type: "IMAGE",
    
      mimeType: "image/jpeg",
    
      url: "https://www.canva.dev/example-assets/image-import/image.jpg",
    
      thumbnailUrl:
    
        "https://www.canva.dev/example-assets/image-import/thumbnail.jpg",
    
    });
    
    
    
    
    // Get a reference to the asset in Canva's backend
    
    console.log("The asset reference is", image.ref);
    
    
    
    
    // Wait for the upload to complete
    
    await image.whenUploaded();
    
    console.log("The upload is complete.");

TS

Copy

### Uploading videos
    
    
    import { upload } from "@canva/asset";
    
    
    
    
    // Start uploading the file
    
    const video = await upload({
    
      type: "VIDEO",
    
      mimeType: "video/mp4",
    
      url: "https://www.canva.dev/example-assets/video-import/video.mp4",
    
      thumbnailImageUrl:
    
        "https://www.canva.dev/example-assets/video-import/thumbnail-image.jpg",
    
      thumbnailVideoUrl:
    
        "https://www.canva.dev/example-assets/video-import/thumbnail-video.mp4",
    
    });
    
    
    
    
    // Get a reference to the asset in Canva's backend
    
    console.log("The asset reference is", video.ref);
    
    
    
    
    // Wait for the upload to complete
    
    await video.whenUploaded();
    
    console.log("The upload is complete.");

TS

Copy

## Permissions

Before an app that uses this method can be submitted for review, the `canva:asset:private:write` permission must be enabled through the Developer Portal. To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Parameters

The expected parameters depend on the type of asset being uploaded:

  * Audio

  * Images

  * Videos




To upload audio, set the following parameters:

`options``object`

Required

The options for configuring the audio to be uploaded.

`options.type``string`

Required

The type of asset to upload. For audio, this must be `"AUDIO"`.

`options.title``string`

Required

A human-readable title that appears in the Canva editor.

`options.mimeType``string`

Required

The MIME type of the audio file. Inexact MIME types are allowed for assets that belong to the same format. For example, you can use `audio/mpeg` for an `audio/mp3` file, but `audio/wav` will not work.

The supported MIME types include:

  * `"audio/mp3"`
  * `"audio/mp4"`
  * `"audio/mpeg"`
  * `"audio/ogg"`
  * `"audio/wav"`
  * `"audio/webm"`
  * `"audio/x-m4a"`
  * `"audio/x-wav"`



`options.durationMs``number`

Required

The duration of the audio, in milliseconds.

`options.url``string`

Required

The URL of the audio file.

The URL must:

  * Use HTTPS
  * Return a `200` status code
  * Point to an image with the same MIME type that's specified in the `mimeType` property
  * Have a `Content-Type` that matches the MIME type of the audio, such as `audio/mp4`
  * Be accessible to Canva's backend — that is, exposed to the internet



The URL must **not** :

  * Redirect to a different URL
  * Contain an IP address
  * Exceed 4096 characters
  * Contain whitespace
  * Contain the following characters: `>`, `<`, `{`, `}`, `^`, or backticks



The maximum file size of an audio file is 50MB.

To upload an image, set the following parameters:

`options``object`

Required

The options for configuring the image to be uploaded.

`options.type``string`

Required

The type of asset to upload. For images, this must be `"IMAGE"`.

`options.mimeType``string`

Required

The MIME type of the full-size image. The MIME type must match the format of the uploaded asset.

The supported MIME types include:

  * `"image/heic"`: HEIC files are not supported for thumbnail images.
  * `"image/jpeg"`
  * `"image/png"`
  * `"image/svg+xml"`: Limitations apply for SVG files. See [Assets](https://www.canva.dev/docs/apps/uploading-assets/).
  * `"image/tiff"`: TIFF files are not supported for thumbnail images.
  * `"image/webp"`



`options.url``string`

Required

The external URL or data URL of the full-size image file.

If the value is an external URL, it must:

  * Use HTTPS
  * Return a `200` status code
  * Point to an image with the same MIME type that's specified in the `mimeType` property
  * Have a `Content-Type` that matches the MIME type of the image, such as `image/jpeg`
  * Be accessible to Canva's backend — that is, exposed to the internet



If the value is an external URL, it must **not** :

  * Redirect to a different URL
  * Contain an IP address
  * Exceed 4096 characters
  * Contain whitespace
  * Contain the following characters: `>`, `<`, `{`, `}`, `^`, or backticks



If the value is a data URL, it must:

  * Point to an image with the same MIME type that's specified in the `mimeType` property
  * Include `;base64` if the data is Base64 encoded



If the value is a data URL, it must **not** :

  * Exceed 10MB (10 × 1024 × 1024) characters



The maximum file size of an image is 50MB.

By default, the `Content-Type` of HEIC images is `application/octet-stream`, which is _not_ a valid value.

`options.thumbnailUrl``string`

Required

The external URL or data URL of a thumbnail image.

An external URL must:

  * Use HTTPS
  * Point to a lower-resolution version of the full-size image file
  * Point to an image file that has the same aspect ratio as the full-size image
  * Point to a PNG, JPEG, or SVG file — HEIC and TIFF thumbnails are not supported
  * Support [Cross-Origin Resource Sharing⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
  * Not exceed 4096 characters



A data URL must:

  * Point to an image file that has the same aspect ratio as the full-size image
  * Ideally, point to a lower-resolution version of the full-size image file, but you can use the full-size image as the thumbnail
  * Include `;base64` if the data is Base64 encoded
  * Point to a PNG, JPEG, or SVG file — HEIC and TIFF thumbnails are not supported
  * Not exceed 10MB (10 × 1024 × 1024) characters



`options.width``number`

Sometimes required

The width of the thumbnail, in pixels.

If a width isn't provided, Canva infers the width from the width of the thumbnail. This requires a `GET` or `HEAD` request, which is slower than manually providing a width.

If the `width` is set, the `height` must also be set, and vice versa.

`options.height``number`

Sometimes required

The height of the thumbnail, in pixels.

If a height isn't provided, Canva infers the height from the height of the thumbnail. This requires a `GET` or `HEAD` request, which is slower than manually providing a height.

If the `height` is set, the `width` must also be set, and vice versa.

`parentRef``string`

Optional

A unique identifier that points to an image in Canva's backend, indicating that the image being uploaded was derived from the specified image.

To upload a video, set the following parameters:

`options``object`

Required

The options for configuring the video to be uploaded.

`options.type``string`

Required

The type of asset to upload. For videos, this must be `"VIDEO"`.

`options.mimeType``string`

Required

The MIME type of the full-size video file. The MIME type must match the format of the uploaded asset.

The supported MIME types include:

  * `"video/avi"`
  * `"image/gif"`
  * `"video/x-m4v"`
  * `"video/x-matroska"`
  * `"video/quicktime"`
  * `"video/mp4"`
  * `"video/mpeg"`
  * `"video/webm"`
  * `"application/json"`



`"application/json"` applies _only_ to [Lottie⁠(opens in a new tab or window)](https://airbnb.io/lottie/#/) files. The import will fail if the `.json` is not a valid Lottie file.

`options.url``string`

Required

The URL of the full-size video file.

The URL must:

  * Use HTTPS
  * Return a `200` status code
  * Point to a video with the same MIME type that's specified in the `mimeType` property
  * Have a `Content-Type` that matches the MIME type of the video, such as `video/mp4`
  * Be accessible to Canva's backend — that is, exposed to the internet



The URL must **not** :

  * Redirect to a different URL
  * Contain an IP address
  * Exceed 4096 characters
  * Contain whitespace
  * Contain the following characters: `>`, `<`, `{`, `}`, `^`, or backticks



The maximum file size of a video file is 100MB.

`options.thumbnailImageUrl``string`

Required

The URL of a thumbnail image. This image is shown while the user drags the video into their design if a thumbnail video can't be used or if a thumbnail video isn't defined.

The URL must:

  * Use HTTPS
  * Point to a thumbnail that is an accurate representation of the video
  * Point to an image file that has the same aspect ratio as the full-size video
  * Point to a PNG, JPEG, or SVG file — HEIC thumbnails are not supported
  * Support [Cross-Origin Resource Sharing⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
  * Not exceed 4096 characters



`options.thumbnailVideoUrl``string`

Optional

The URL of a low-resolution video file. If supplied, this is used while the full-size video is still being uploaded. If not supplied, the image from the `thumbnailImageUrl` is used instead.

The URL must:

  * Use HTTPS
  * Point to a lower-resolution version of the full-size video file
  * Point to a video file that has the same aspect ratio as the full-size video
  * Point to a file with a MIME type of `"video/webm"` or `"video/mpeg"`
  * Support [Cross-Origin Resource Sharing⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
  * Not exceed 4096 characters



`options.width``number`

Sometimes required

The width of the thumbnail, in pixels.

If a width isn't provided, Canva infers the width from the width of the thumbnail. This requires a `GET` or `HEAD` request, which is slower than manually providing a width.

If the `width` is set, the `height` must also be set, and vice versa.

`options.height``number`

Sometimes required

The height of the thumbnail, in pixels.

If a height isn't provided, Canva infers the height from the height of the thumbnail. This requires a `GET` or `HEAD` request, which is slower than manually providing a height.

If the `height` is set, the `width` must also be set, and vice versa.

`parentRef``string`

Optional

A unique identifier that points to a video in Canva's backend, indicating that the video being uploaded was derived from the specified video.

## Returns

A `Promise` that resolves with the following object:

`result``object`

Required

The successful result of an upload.

`result.ref``string`

Required

A unique identifier that points to an asset in Canva's backend.

`result.whenUploaded``function`

Required

An asynchronous method that returns a `Promise`. This `Promise` resolves when the upload is complete. You can use this method to check when the asset has finished uploading. Ensure `whenUploaded` is called _after_ adding the element to the page (such as using `addNativeElement`) in your app's code.
