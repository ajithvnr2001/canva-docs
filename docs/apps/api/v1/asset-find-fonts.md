---
url: https://www.canva.dev/docs/apps/api/v1/asset-find-fonts/
title: findFonts - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:25.369291+00:00
---

# findFonts - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/asset-find-fonts/

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

# findFonts

API reference for the findFonts method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Returns a list of recommended fonts. The recommendations are based on a number of factors, such as the user's locale. To learn more, see [Creating text](https://www.canva.dev/docs/apps/creating-text/).

## Usage

### Basic usage
    
    
    import { findFonts } from "@canva/asset";
    
    const { fonts } = await findFonts();
    
    console.log(fonts); // => [ { name: "Arial", ... }]

TS

Copy

### Filtering
    
    
    import { findFonts } from "@canva/asset";
    
    const { fonts } = await findFonts({ fontRefs: ["FONT_REF_GOES_HERE"] });
    
    console.log(fonts); // => [ { name: "Arial", ... }]

TS

Copy

## Parameters

`options``object`

Optional

Options for filtering the returned fonts.

`options.fontRefs``array`

Optional

An array of font references. If defined, only the fonts with the specified references will be returned.

## Returns

A `Promise` that resolves with the following object:

`response``object`

Required

The result of requesting a list of available fonts.

`response.fonts``array`

Required

An array of fonts.

`response.fonts[0]``object`

Required

An individual font.

`response.fonts[0].ref``string`

Required

A unique identifier that references a font in Canva's backend.

You should not rely on the `ref` remaining the same. For example, if you store it in a database and try to use it a few weeks later, an error may be thrown due to the `ref` being outdated.

`response.fonts[0].name``string`

Required

The name of the font.

`response.fonts[0].weights``array`

Required

An array of font weights that the font is available in.

`response.fonts[0].weights[0]``object`

Required

An individual font weight.

`response.fonts[0].weights[0].weight``object`

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



`response.fonts[0].weights[0].styles``array`

Required

The styles the font weight is available in.

The possible values depend on the font, but may be any combination of the following values:

  * `"normal"`
  * `"italic"`



`response.fonts[0].previewUrl``string`

Optional

The URL of an image that contains a preview of the font.
