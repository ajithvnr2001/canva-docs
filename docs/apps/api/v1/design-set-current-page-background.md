---
url: https://www.canva.dev/docs/apps/api/v1/design-set-current-page-background/
title: setCurrentPageBackground - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:31.046921+00:00
---

# setCurrentPageBackground - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-set-current-page-background/

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

# setCurrentPageBackground

API reference for the setCurrentPageBackground method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Sets the background of the current page, which is either the page the user has explicitly selected or the page that occupies the majority of the viewport.

## Usage

### Setting a background color
    
    
    import { setCurrentPageBackground } from "@canva/design";
    
    
    
    
    setCurrentPageBackground({
    
      color: "#ff0099",
    
    });

TS

Copy

### Setting a background image
    
    
    import { setCurrentPageBackground } from "@canva/design";
    
    import { upload } from "@canva/asset";
    
    
    
    
    const image = await upload({
    
      type: "IMAGE",
    
      mimeType: "image/jpeg",
    
      url: "https://www.canva.dev/example-assets/image-import/image.jpg",
    
      thumbnailUrl:
    
        "https://www.canva.dev/example-assets/image-import/thumbnail.jpg",
    
    });
    
    
    
    
    setCurrentPageBackground({
    
      asset: {
    
        type: "IMAGE",
    
        ref: image.ref,
    
      },
    
    });

TS

Copy

### Setting a background video
    
    
    import { setCurrentPageBackground } from "@canva/design";
    
    import { upload } from "@canva/asset";
    
    
    
    
    const video = await upload({
    
      type: "VIDEO",
    
      mimeType: "video/mp4",
    
      url: "https://www.canva.dev/example-assets/video-import/video.mp4",
    
      thumbnailImageUrl:
    
        "https://www.canva.dev/example-assets/video-import/thumbnail-image.jpg",
    
      thumbnailVideoUrl:
    
        "https://www.canva.dev/example-assets/video-import/thumbnail-video.mp4",
    
    });
    
    
    
    
    setCurrentPageBackground({
    
      asset: {
    
        type: "VIDEO",
    
        ref: video.ref,
    
      },
    
    });

TS

Copy

## Parameters

The expected parameters depend on the type of background:

  * Asset

  * Color




To set an [asset](https://www.canva.dev/docs/apps/uploading-assets/) as the current page background, such as an image or video, set the following parameters:

`options``object`

Required

The options for setting the current page background.

`options.asset``object`

Required

The asset to set as the current page background.

`options.asset.type``string`

Required

The type of asset.

The available options include:

  * `"IMAGE"`
  * `"VIDEO"`



`options.asset.ref``string`

Required

A unique identifier that points to an asset, such as an image or video, in Canva's backend.

To set a color as the current page background, set the following parameters:

`options``object`

Required

The options for setting the current page background.

`options.color``string`

Required

The color to set as the current page background, as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol (e.g., `#ff0099`).

## Returns

`Promise<void>`
