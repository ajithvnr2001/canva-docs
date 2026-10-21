---
url: https://www.canva.dev/docs/apps/api/v1/design-request-export/
title: requestExport - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:23.031180+00:00
---

# requestExport - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-request-export/

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

# requestExport

API reference for the requestExport method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Exports the user's design as one or more static files.

To learn more, see [Exporting designs](https://www.canva.dev/docs/apps/exporting-designs/).

## Usage
    
    
    import { requestExport } from "@canva/design";
    
    
    
    
    const response = await requestExport({
    
      acceptedFileTypes: ["PNG", "JPG"],
    
    });
    
    
    
    
    if (response.status === "COMPLETED") {
    
      console.log(response); // => { status: "COMPLETED", title: "My design", exportBlobs: [{ url: "https://example.com/image.png" }] }
    
    } else {
    
      console.log("The user exited the export flow.");
    
      console.log(response); // => { status: "ABORTED" }
    
    }

TS

Copy

## Rate limit

This method has a rate limit of 10 requests every 10 seconds.

## Parameters

`options``object`

Required

The options for configuring the export of a design.

`options.acceptedFileTypes``array`

Required

The types of files the user can export their design as.

You must provide at least one file type.

The supported file types include:

  * `"GIF"`
  * `"JPG"`
  * `"PDF_STANDARD"`
  * `"PNG"`
  * `"PPTX"`
  * `"SVG"`
  * `"VIDEO"`



## Returns

A `Promise` that resolves with the following object:

`result``object`

Required

The result of the successful export of a design.

`result.status``string`

Required

A value that identifies if the export was successful or not.

This property may contain any of the following values:

  * `"COMPLETED"` \- The user successfully exported their design.
  * `"ABORTED"` \- The user closed the export dialog without exporting their design.



`result.title``string`

Optional

The title of the design, if it had been set by the user.

`result.exportBlobs``array`

Required

The exported files.

If there are multiple files, they'll be provided in a ZIP file and the array will contain one item. In the future, there'll be an option for each file to be a separate item in the array.

`result.exportBlobs[0].url``string`

Required

The URL of the exported file, such as a ZIP or PNG file.

If the user's design contains multiple pages but is exported in a format that doesn't support multiple pages, the URL will point to a ZIP file that contains each page as a separate file.

The following file types support multiple pages:

  * `"GIF"`
  * `"PDF_STANDARD"`
  * `"PPTX"`
  * `"VIDEO"`



The following file types do not support multiple pages:

  * `"JPG"`
  * `"PNG"`
  * `"SVG"`



If a user selects the `"VIDEO"` option, they have the choice of exporting each page as a separate file. In this case, the URL will point to a ZIP file that contains a separate video for each page.
