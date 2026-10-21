---
url: https://www.canva.dev/docs/apps/api/v1/design-get-current-page-context/
title: getCurrentPageContext - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:28.993687+00:00
---

# getCurrentPageContext - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-get-current-page-context/

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

# getCurrentPageContext

API reference for the getCurrentPageContext method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Gets information about the current page in the user's design.

To see how this method is used, see [Positioning elements](https://www.canva.dev/docs/apps/positioning-elements/).

## Usage
    
    
    import { getCurrentPageContext } from "@canva/design";
    
    
    
    
    const context = await getCurrentPageContext();
    
    console.log(context);

TS

Copy

## Permissions

Before an app that uses this method can be submitted for review, the `canva:design:content:read` permission must be enabled through the Developer Portal. To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Returns

A `Promise` that resolves with the following object:

`result``object`

Required

The successful result of getting the current page context.

`result.dimensions``object`

Optional

The dimensions of the page, in pixels.

Some types of designs, such as [whiteboards⁠(opens in a new tab or window)](https://www.canva.com/online-whiteboard/templates/), don't have page dimensions. In these cases, the `dimensions` property is `undefined`.

`result.dimensions.width``number`

Required

The width of the page, in pixels.

`result.dimensions.height``number`

Required

The height of the page, in pixels.
