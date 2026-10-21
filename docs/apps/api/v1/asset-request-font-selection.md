---
url: https://www.canva.dev/docs/apps/api/v1/asset-request-font-selection/
title: requestFontSelection - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:25.675727+00:00
---

# requestFontSelection - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/asset-request-font-selection/

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

# requestFontSelection

API reference for the requestFontSelection method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Opens a dialog that allows the user to select from a list of fonts.

To learn more, see [Creating text](https://www.canva.dev/docs/apps/creating-text/).

## Usage
    
    
    import { requestFontSelection } from "@canva/asset";
    
    
    
    
    const fontResponse = await requestFontSelection();
    
    console.log(fontResponse.font.name); // => "Arial"

TS

Copy

## Parameters

`request``object`

Optional

The options for requesting the selection of a font.

`request.selectedFontRef``string`

Optional

A unique identifier that references a font asset in Canva's backend. If this is set, the specified font will be selected when the font picker opens. To learn more, see [Creating text](https://www.canva.dev/docs/apps/creating-text/).

## Returns

A `Promise` that resolves with an object.

If the user selects a font, the following object is returned:

`response``object`

Required

The result of selecting a font.

`response.type``string`

Required

The type of result. If the user selects a font, this is always `"COMPLETED"`.

`response.font``object`

Required

The selected font.

`response.font.ref``string`

Required

A unique identifier that references a font in Canva's backend.

You should not rely on the `ref` remaining the same. For example, if you store it in a database and try to use it a few weeks later, an error may be thrown due to the `ref` being outdated.

`response.font.name``string`

Required

The name of the font.

`response.font.weights``array`

Required

An array of font weights that the font is available in.

`response.font.weights[0]``object`

Required

An individual font weight.

`response.font.weights[0].weight``string`

Required

The name of the font weight.

The possible values depend on the font, but may be any combination of the following values:

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



`response.font.weights[0].styles``array`

Required

The styles the font weight is available in.

The possible values depend on the font, but may be any combination of the following values:

  * `"normal"`
  * `"italic"`



`response.font.previewUrl``string`

Optional

The URL of an image that contains a preview of the font.

If the user closes the font picker without selecting a font, the following object is returned:

`response``object`

Required

The result of closing the font picker without selecting a font.

`response.type``string`

Required

The type of result. If the user doesn't select a font, this is always `"ABORTED"`.
