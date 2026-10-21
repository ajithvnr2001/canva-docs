---
url: https://www.canva.dev/docs/apps/api/v1/design-ui-make-draggable/
title: ui.makeDraggable - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:32.126215+00:00
---

# ui.makeDraggable - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-ui-make-draggable/

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

# ui.makeDraggable

API reference for the ui.makeDraggable method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

The `ui.makeDraggable` method has been deprecated. You should instead handle drag and drop events with the [`ui.startDrag`](https://www.canva.dev/docs/apps/api/latest/design-ui-start-drag/) method.

Makes a DOM node draggable. When the user drags and drops the node into their design, a specified type of element — for example, an image — will be added at the drop coordinates.

To learn more, see [Drag and drop](https://www.canva.dev/docs/apps/supporting-drag-drop/).

## Usage
    
    
    import { ui } from "@canva/design";
    
    
    
    
    const node = document.querySelector("#some-node");
    
    
    
    
    if (!(node instanceof HTMLElement)) {
    
      throw new Error(`DOM node does not exist`);
    
    }
    
    
    
    
    ui.makeDraggable({
    
      node,
    
      dragData: {
    
        type: "TEXT",
    
        children: ["Hello world"],
    
      },
    
      onDragStart: () => {
    
        console.log("The drag event has started");
    
      },
    
      onDragEnd: () => {
    
        console.log("The drag event has ended");
    
      },
    
    });

TS

Copy

## Parameters

The expected parameters depend on what will be added to the user's design at the end of a drag event:

  * Audio tracks

  * Images

  * Text

  * Videos




When adding an audio track to a design, set the following properties:

`options``object`

Required

The options for configuring the drag and drop behavior of a DOM node.

`options.node``HTMLElement`

Required

The DOM node to make draggable.

`options.onDragStart``function`

Required

A callback function that runs at the start of a drag event.

`options.onDragEnd``function`

Required

A callback function that runs at the end of a drag event. This function always runs, regardless of whether or not the user successfully drops something into their design.

`options.dragData``object`

Required

The options for configuring what's added to the user's design at the end of a drag event.

`options.dragData.type``string`

Required

The type of element to add to the design. For audio tracks, this must be `"AUDIO"`.

`options.dragData.title``string`

Required

A human-readable title that appears in the Canva editor.

`options.dragData.durationMs``number`

Required

The duration of the audio file, in milliseconds.

`options.dragData.resolveAudioRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.

When adding an image to a design, set the following properties:

`options``object`

Required

The options for configuring the drag and drop behavior of a DOM node.

`options.node``HTMLElement`

Required

The DOM node to make draggable.

`options.onDragStart``function`

Required

A callback function that runs at the start of a drag event.

`options.onDragEnd``function`

Required

A callback function that runs at the end of a drag event. This function always runs, regardless of whether or not the user successfully drops something into their design.

`options.dragData``object`

Optional

The options for configuring what's added to the user's design at the end of a drag event.

`options.dragData.type``string`

Required

The type of element to add to the design. For images, this must be `"IMAGE"`.

`options.dragData.resolveImageRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.

`options.dragData.previewSize``object`

Required

The dimensions of the drag preview, in pixels. The dimensions should have the same aspect ratio as the full-size image.

`options.dragData.previewSize.width``number`

Required

The width of the drag preview, in pixels.

`options.dragData.previewSize.height``number`

Required

The height of the drag preview, in pixels.

`options.dragData.fullSize``object`

Optional

The dimensions of the full-size image. If omitted, the drag preview dimensions are used.

`options.dragData.fullSize.width``number`

Required

The width of the full-size image, in pixels.

`options.dragData.fullSize.height``number`

Required

The height of the full-size image, in pixels.

`options.dragData.previewSrc``string`

Optional

The URL or data URL of the image to use for the drag preview. This image will appear under the user's cursor during the drag event. If omitted, the full-size image will be used.

When adding text to a design, set the following properties:

`options``object`

Required

The options for configuring the drag and drop behavior of a DOM node.

`options.node``HTMLElement`

Required

The DOM node to make draggable.

`options.onDragStart``function`

Required

A callback function that runs at the start of a drag event.

`options.onDragEnd``function`

Required

A callback function that runs at the end of a drag event. This function always runs, regardless of whether or not the user successfully drops something into their design.

`options.dragData``object`

Required

The options for configuring what's added to the user's design at the end of a drag event.

`options.dragData.type``string`

Required

The type of element to add to the design. For text, this must be `"TEXT"`.

`options.dragData.children``array`

Required

The text to add to the user's design, provided as an array of strings.

For the time being, the array is only allowed to have one item. In the future, each element in the array will be rendered as a separate line of text.

`options.dragData.textAlign``string`

Optional

The horizontal alignment of the text.

The available options include:

  * `"start"`
  * `"center"`
  * `"end"`



The default value is `"start"`.

`options.dragData.fontWeight``string`

Optional

The weight (boldness) of the font.

The available options include:

  * `"normal"`
  * `"bold"`



The default value is `"normal"`.

`options.dragData.fontStyle``string`

Optional

The style of the font.

The available options include:

  * `"normal"`
  * `"italic"`



The default value is `"normal"`.

`options.dragData.decoration``string`

Optional

The decoration to apply to the font.

The available options include:

  * `"normal"`
  * `"underline"`



The default value is `"normal"`.

When adding a video to a design, set the following properties:

`options``object`

Required

The options for configuring the drag and drop behavior of a DOM node.

`options.node``HTMLElement`

Required

The DOM node to make draggable.

`options.onDragStart``function`

Required

A callback function that runs at the start of a drag event.

`options.onDragEnd``function`

Required

A callback function that runs at the end of a drag event. This function always runs, regardless of whether or not the user successfully drops something into their design.

`options.dragData``object`

Required

The options for configuring what's added to the user's design at the end of a drag event.

`options.dragData.type``string`

Required

The type of element to add to the design. For videos, this must be `"VIDEO"`.

`options.dragData.resolveVideoRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.

`options.dragData.previewSize``object`

Required

The dimensions of the drag preview, in pixels. The dimensions should have the same aspect ratio as the full-size video.

`options.dragData.previewSize.width``number`

Required

The width of the drag preview, in pixels.

`options.dragData.previewSize.height``number`

Required

The height of the drag preview, in pixels.

`options.dragData.previewSrc``string`

Required

The URL or data URL of the image to use for the drag preview. This image will appear under the user's cursor during the drag event. If omitted, the full-size image will be used.

`options.dragData.fullSize``object`

Optional

The dimensions of the full-size video, in pixels. If omitted, the drag preview dimensions are used.

`options.dragData.fullSize.width``number`

Sometimes required

The width of the full-size video, in pixels.

`options.dragData.fullSize.height``number`

Sometimes required

The height of the full-size video, in pixels.

## Returns

`Promise<void>`
