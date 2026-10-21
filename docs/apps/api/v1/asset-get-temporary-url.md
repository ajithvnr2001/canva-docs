---
url: https://www.canva.dev/docs/apps/api/v1/asset-get-temporary-url/
title: getTemporaryUrl - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:25.172183+00:00
---

# getTemporaryUrl - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/asset-get-temporary-url/

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

# getTemporaryUrl

API reference for the getTemporaryUrl method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Gets the URL of an asset, such as an image or video file, from Canva's backend.

To see how this method is used, see [Selection API](https://www.canva.dev/docs/apps/selection/).

## Usage
    
    
    import { getTemporaryUrl } from "@canva/asset";
    
    
    
    
    const result = await getTemporaryUrl({
    
      type: "IMAGE",
    
      ref: "<REFERENCE_GOES_HERE>",
    
    });
    
    
    
    
    console.log(result.url);

TS

Copy

## Permissions

Before an app that uses this method can be submitted for review, the `canva:asset:private:read` permission must be enabled through the Developer Portal. To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Rate limit

This method has a rate limit of 20 requests every 10 seconds.

## Parameters

`options``object`

Required

The options for getting the URL of an asset.

`options.type``string`

Required

The type of asset.

The available options include:

  * `"IMAGE"`
  * `"VIDEO"`



`options.ref``string`

Required

A unique identifier that points to an asset in Canva's backend.

## Returns

A `Promise` that resolves with the following object:

`result``object`

Required

The successful result of getting a temporary URL.

`result.type``string`

Required

The type of asset.

The possible values include:

  * `"IMAGE"`
  * `"VIDEO"`



`result.ref``string`

Required

A unique identifier that points to an asset in Canva's backend.

`result.url``string`

Required

The URL of the asset.

The URL is temporary and expires after a short duration. Your app should download the asset immediately rather than assuming the URL will continue to exist.
