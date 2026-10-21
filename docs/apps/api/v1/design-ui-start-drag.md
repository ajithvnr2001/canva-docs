---
url: https://www.canva.dev/docs/apps/api/v1/design-ui-start-drag/
title: ui.startDrag - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:33.086422+00:00
---

# ui.startDrag - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-ui-start-drag/

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

# ui.startDrag

API reference for the ui.startDrag method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Handles a drag event. At the end of the drag event, the specified type of element — for example, an image — will be added at the drop coordinates.

## Usage
    
    
    import React from "react";
    
    import { Text, TypographyCard } from "@canva/app-ui-kit";
    
    import { addNativeElement, ui } from "@canva/design";
    
    
    
    
    export function App() {
    
      return (
    
        <TypographyCard
    
          ariaLabel="Add text to design"
    
          onClick={() => {
    
            addNativeElement({
    
              type: "TEXT",
    
              children: ["Add text into a design"],
    
            });
    
          }}
    
          onDragStart={(event: React.DragEvent<HTMLElement>) => {
    
            ui.startDrag(event, {
    
              type: "TEXT",
    
              children: ["Add text into a design"],
    
            });
    
          }}
    
        >
    
          <Text>Add text into a design</Text>
    
        </TypographyCard>
    
      );
    
    }

TSX

Copy

## Parameters

The expected parameters depend on what will be added to the user's design at the end of a drag event:

  * Embeds

  * Audio tracks

  * Images

  * Text

  * Videos




`event``object`

Required

The event that's fired when the user starts dragging an element.

`dragData``object`

Required

The options for configuring what's added to the user's design at the end of a drag event.

`dragData.type``string`

Required

The type of element to add to the design. For embeds, this must be `"EMBED"`.

`dragData.embedUrl``string`

Required

The URL of the embeddable media.

`dragData.previewUrl``string`

Required

The URL or data URL of the image to use for the drag preview. This image will appear under the user's cursor during the drag event.

`dragData.previewSize``object`

Required

The dimensions of the drag preview, in pixels.

`dragData.previewSize.width``number`

Required

The width of the drag preview, in pixels.

`dragData.previewSize.height``number`

Required

The height of the drag preview, in pixels.

When adding an audio track to a design, set the following parameters:

`event``object`

Required

The event that's fired when the user starts dragging an element.

`dragData``object`

Required

The options for configuring what's added to the user's design at the end of a drag event.

`dragData.type``string`

Required

The type of element to add to the design. For audio tracks, this must be `"AUDIO"`.

`dragData.title``string`

Required

A human-readable title that appears in the Canva editor.

`dragData.durationMs``number`

Required

The duration of the audio file, in milliseconds.

`dragData.resolveAudioRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.

For image elements, the expected parameters depend on the format of the image data:

`event``object`

Required

The event that's fired when the user starts dragging an element.

`dragData``object`

Required

The options for configuring what's added to the user's design at the end of a drag event.

`dragData.type``string`

Required

The type of element to add to the design. For images, this must be `"IMAGE"`.

`dragData.resolveImageRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.

`dragData.previewSize``object`

Required

The dimensions of the drag preview, in pixels. The dimensions should have the same aspect ratio as the full-size image.

`dragData.previewSize.width``number`

Required

The width of the drag preview, in pixels.

`dragData.previewSize.height``number`

Required

The height of the drag preview, in pixels.

`dragData.fullSize``object`

Optional

The dimensions of the full-size image. If omitted, the drag preview dimensions are used.

`dragData.fullSize.width``number`

Required

The width of the full-size image, in pixels.

`dragData.fullSize.height``number`

Required

The height of the full-size image, in pixels.

`dragData.previewUrl``string`

Optional

The URL or data URL of the image to use for the drag preview. This image will appear under the user's cursor during the drag event. If omitted, the full-size image will be used.

When adding text to a design, set the following parameters:

`event``object`

Required

The event that's fired when the user starts dragging an element.

`dragData``object`

Required

The options for configuring what's added to the user's design at the end of a drag event.

`dragData.type``string`

Required

The type of element to add to the design. For text, this must be `"TEXT"`.

`dragData.children``array`

Required

The text to add to the user's design, provided as an array of strings.

For the time being, the array is only allowed to have one item. In the future, each element in the array will be rendered as a separate line of text.

`dragData.textAlign``string`

Optional

The horizontal alignment of the text.

The available options include:

  * `"start"`
  * `"center"`
  * `"end"`



The default value is `"start"`.

`dragData.fontWeight``string`

Optional

The weight (boldness) of the font.

The available options include:

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



The default value is `"normal"`.

`dragData.fontStyle``string`

Optional

The style of the font.

The available options include:

  * `"normal"`
  * `"italic"`



The default value is `"normal"`.

`dragData.decoration``string`

Optional

The decoration to apply to the font.

The available options include:

  * `"normal"`
  * `"underline"`



The default value is `"normal"`.

`dragData.fontRef``string`

Optional

A unique identifier that references a font asset in Canva's backend. To learn more, see [Creating text](https://www.canva.dev/docs/apps/creating-text/).

When adding a video to a design, set the following parameters:

`event``object`

Required

The event that's fired when the user starts dragging an element.

`dragData``object`

Required

The options for configuring what's added to the user's design at the end of a drag event.

`dragData.type``string`

Required

The type of element to add to the design. For videos, this must be `"VIDEO"`.

`dragData.resolveVideoRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.

`dragData.previewSize``object`

Required

The dimensions of the drag preview, in pixels. The dimensions should have the same aspect ratio as the full-size video.

`dragData.previewSize.width``number`

Required

The width of the drag preview, in pixels.

`dragData.previewSize.height``number`

Required

The height of the drag preview, in pixels.

`dragData.previewUrl``string`

Required

The URL or data URL of the image to use for the drag preview. This image will appear under the user's cursor during the drag event. If omitted, the full-size image will be used.

`dragData.fullSize``object`

Optional

The dimensions of the full-size video, in pixels. If omitted, the drag preview dimensions are used.

`dragData.fullSize.width``number`

Sometimes required

The width of the full-size video, in pixels.

`dragData.fullSize.height``number`

Sometimes required

The height of the full-size video, in pixels.

## Returns

`Promise<void>`
