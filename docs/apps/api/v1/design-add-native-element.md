---
url: https://www.canva.dev/docs/apps/api/v1/design-add-native-element/
title: addNativeElement - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:28.087094+00:00
---

# addNativeElement - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-add-native-element/

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

# addNativeElement

API reference for the addNativeElement method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Adds a native element to a user's design.

To learn more, see:

  * [Creating images](https://www.canva.dev/docs/apps/creating-images/)
  * [Creating shapes](https://www.canva.dev/docs/apps/creating-shapes/)
  * [Creating tables](https://www.canva.dev/docs/apps/creating-tables/)
  * [Creating text](https://www.canva.dev/docs/apps/creating-text/)
  * [Creating videos](https://www.canva.dev/docs/apps/creating-videos/)
  * [Embedding rich media](https://www.canva.dev/docs/apps/embedding-rich-media/)
  * [Grouping elements](https://www.canva.dev/docs/apps/grouping-elements/)



## Usage
    
    
    import { addNativeElement } from "@canva/design";
    
    
    
    
    await addNativeElement({
    
      type: "TEXT",
    
      children: ["Hello world"],
    
    });

TS

Copy

## Permissions

Before an app that uses this method can be submitted for review, the `canva:design:content:write` permission must be enabled through the Developer Portal. To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Rate limit

This method has a rate limit of 20 requests every 10 seconds.

## Parameters

The expected parameters depend on the type of element being added to the design:

  * Embeds

  * Groups

  * Images

  * Plaintext

  * Richtext

  * Shapes

  * Tables

  * Videos




To add an embed element to the user's design, set the following parameters:

`type``string`

Required

The type of element. For embed elements, this must be `"EMBED"`.

`url``string`

Required

The URL of the embeddable media.

This URL must be supported by Iframely. To learn more, see [What URLs to send to Iframely⁠(opens in a new tab or window)](https://iframely.com/docs/providers).

`width``number`

Sometimes required

The width of the element, in pixels.

If `height` is a number, this can be set to `"auto"`.

`height``number`

Sometimes required

The height of the element, in pixels.

If `width` is a number, this can be set to `"auto"`.

`top``number`

Sometimes required

The distance from the top edge of the container, in pixels.

The container could be a page, a group, or an app element.

`left``number`

Sometimes required

The distance from the left edge of the container, in pixels.

The container could be a page, a group, or an app element.

`rotation``number`

Optional

The rotation of the element, in degrees. This must be a number between `-180` and `180`.

This property doesn't have an effect unless you also set position properties for the element. To set a position, you must provide the `width`, `height`, `top`, and `left` properties.

To add a group element to the user's design, set the following parameters:

`type``string`

Required

The type of element. For group elements, this must be `"GROUP"`.

`children``array`

Required

The elements to include in the group.

Each element must have the following properties:

  * `width`
  * `height`
  * `top`
  * `left`



Group elements can't contain group elements.

`width``number`

Sometimes required

The width of the element, in pixels.

If `height` is a number, this can be set to `"auto"`.

`height``number`

Sometimes required

The height of the element, in pixels.

If `width` is a number, this can be set to `"auto"`.

`top``number`

Sometimes required

The distance from the top edge of the page, in pixels.

`left``number`

Sometimes required

The distance from the left edge of the page, in pixels.

`rotation``number`

Optional

The rotation of the element, in degrees. This must be a number between `-180` and `180`.

This property doesn't have an effect unless you also set position properties for the element. To set a position, you must provide the `width`, `height`, `top`, and `left` properties.

To add an image element to the user's design, set the following parameters:

`type``string`

Required

The type of element. For image elements, this must be `"IMAGE"`.

`ref``string`

Required

A unique identifier that points to an image in Canva's backend.

`width``number`

Sometimes required

The width of the element, in pixels.

If `height` is a number, this can be set to `"auto"`.

`height``number`

Sometimes required

The height of the element, in pixels.

If `width` is a number, this can be set to `"auto"`.

`top``number`

Sometimes required

The distance from the top edge of the container, in pixels.

The container could be a page, a group, or an app element.

`left``number`

Sometimes required

The distance from the left edge of the container, in pixels.

The container could be a page, a group, or an app element.

`rotation``number`

Optional

The rotation of the element, in degrees. This must be a number between `-180` and `180`.

This property doesn't have an effect unless you also set position properties for the element. To set a position, you must provide the `width`, `height`, `top`, and `left` properties.

To add a plaintext element to the user's design, set the following parameters:

`type``string`

Required

The type of element. For plaintext elements, this must be `"TEXT"`.

`children``array`

Required

The text to add to the user's design, provided as an array of strings.

For the time being, the array is only allowed to have one item. In the future, each element in the array will be rendered as a separate line of text.

`fontSize``string`

Optional

The size of the text, in pixels. This must be an integer between 1 and 1000 (inclusive). The default value is `16`.

In the user interface, the font size is displayed as points (pts), not pixels. This means the font size defined here will be different from what's shown to the user.

This property doesn't have an effect unless you also set position properties for the element. To set a position, you must provide the `top`, `left`, and `width` properties.

`textAlign``string`

Optional

The alignment of the text.

The available options include:

  * `"start"`
  * `"center"`
  * `"end"`



The default value is `"start"`.

`color``string`

Optional

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol — for example, `"#ff0099"`.

The default value is `"#000000"`.

`fontRef``string`

Optional

A unique identifier that references a font in Canva's backend. To learn more, see [Creating text](https://www.canva.dev/docs/apps/creating-text/).

`fontWeight``string`

Optional

The weight of the font.

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

`fontStyle``string`

Optional

The style of the font.

The available options include:

  * `"normal"`
  * `"italic"`



The default value is `"normal"`.

`decoration``string`

Optional

The decoration of the font.

The available options include:

  * `"none"`
  * `"underline"`



The default value is `"none"`.

`width``number`

Sometimes required

The width of the element, in pixels.

`top``number`

Sometimes required

The distance from the top edge of the container, in pixels.

The container could be a page, a group, or an app element.

`left``number`

Sometimes required

The distance from the left edge of the container, in pixels.

The container could be a page, a group, or an app element.

`rotation``number`

Optional

The rotation of the element, in degrees. This must be a number between `-180` and `180`.

This property doesn't have an effect unless you also set position properties for the element. To set a position, you must provide the `top`, `left`, and `width` properties.

To add a richtext element to the user's design, set the following parameters:

`type``string`

Required

The type of element. For richtext elements, this must be `"RICHTEXT"`.

`range``object`

Required

A range of formatted text created with the [`createRichtextRange`](https://www.canva.dev/docs/apps/api/latest/design-create-richtext-range/) method.

`width``number`

Sometimes required

The width of the element, in pixels.

`top``number`

Sometimes required

The distance from the top edge of the container, in pixels.

The container could be a page, a group, or an app element.

`left``number`

Sometimes required

The distance from the left edge of the container, in pixels.

The container could be a page, a group, or an app element.

`rotation``number`

Optional

The rotation of the element, in degrees. This must be a number between `-180` and `180`.

This property doesn't have an effect unless you also set position properties for the element. To set a position, you must provide the `top`, `left`, and `width` properties.

To add a shape element to the user's design, set the following parameters:

`type``string`

Required

The type of element. For shape elements, this must be `"SHAPE"`.

`paths``array`

Required

The paths that define the shape of the element.

There must be between 1 and 30 paths. The maximum combined size of all paths must not exceed 2kb. The maximum number of unique fill colors across all paths is 6.

`paths[0].d``string`

Required

The shape of the path.

This accepts the same value as the `d` attribute of the SVG `<path>` element, with some limitations:

  * The path must start with an `M` command
  * The path must not have more than one `M` command
  * The path must not use the `Q` command
  * The path must be closed, either with a `Z` command at the end or by having the last coordinate match the first coordinate



`paths[0].fill``object`

Required

The appearance of the path's interior.

Only one type of fill — color, image, or video — can be set.

`paths[0].fill.dropTarget``boolean`

Optional

If `true`, users can drop images or videos onto the path to use them as a fill.

Although the `dropTarget` property is optional, we encourage you to set it to prevent breaking in potential future API changes. For image fills `dropTarget` can be `false`, but for video fills it must be `true`.

`paths[0].fill.color``string`

Optional

The color of the fill as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol — for example, `"#ff0099"`.

`paths[0].fill.asset``object`

Optional

If set, a user can fill a shape with an asset.

`paths[0].fill.asset.type``string`

Required

The type of asset to fill the shape.

Valid values include:

  * `IMAGE`
  * `VIDEO`



`paths[0].fill.asset.ref``string`

Required

The unique identifier of the `paths[0].fill.asset.type` asset to fill the shape.

`paths[0].stroke``object`

Required

The outline of the path.

`paths[0].stroke.weight``number`

Required

The weight of the stroke. This must be an integer between 0 and 100.

`paths[0].stroke.color``string`

Required

The color of the stroke as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol — for example, `"#ff0099"`.

`paths[0].stroke.strokeAlign``string`

Required

The alignment of the stroke. The only supported value is `"inset"`.

`viewBox``object`

Required

The scale and cropping of a shape. This is similar to the `viewBox` attribute of a `HTMLSVGElement`.

`viewBox.width``number`

Required

The width of the view box, in pixels.

`viewBox.height``number`

Required

The height of the view box, in pixels.

`viewBox.top``number`

Required

The distance of the shape from the top edge of the element, in pixels.

`viewBox.left``number`

Required

The distance of the shape from the left edge of the element, in pixels.

`width``number`

Sometimes required

The width of the element, in pixels.

If `height` is a number, this can be set to `"auto"`.

`height``number`

Sometimes required

The height of the element, in pixels.

If `width` is a number, this can be set to `"auto"`.

`top``number`

Sometimes required

The distance from the top edge of the container, in pixels.

The container could be a page, a group, or an app element.

`left``number`

Sometimes required

The distance from the left edge of the container, in pixels.

The container could be a page, a group, or an app element.

`rotation``number`

Optional

The rotation of the element, in degrees. This must be a number between `-180` and `180`.

This property doesn't have an effect unless you also set position properties for the element. To set a position, you must provide the `width`, `height`, `top`, and `left` properties.

This API is in preview mode and may experience breaking changes. Apps that use this API will not pass the review process and can't be made available on the Apps Marketplace.

To add a table element to the user's design, set the following parameters:

`type``string`

Required

The type of element. For table elements, this must be `"TABLE"`.

`rows``array`

Required

The rows that make up a table. A table must have at least one row, one column, and no more than 225 cells.

`rows[0]``object`

Required

An individual row within a table.

`rows[0].cells``array`

Required

The cells that make up a row.

`rows[0].cells[0]``object`

Required

An individual cell within a row.

`rows[0].cells[0].text``object`

Optional

A text element to set as the contents of the cell.

`rows[0].cells[0].text.type``string`

Required

The type of element. For text elements, this must be `"TEXT"`.

`rows[0].cells[0].text.children``array`

Required

The text to add to the user's design, provided as an array of strings.

For the time being, the array is only allowed to have one item. In the future, each element in the array will be rendered as a separate line of text.

`rows[0].cells[0].fill``object`

Optional

The background of the cell.

`rows[0].cells[0].fill.color``string`

Optional

The background color of the cell as a hex code. The hex code must include all six characters and be prefixed with a `#` symbol — for example, `"#ff0099"`.

`rows[0].cells[0].colSpan``number`

Optional

The number of columns that the cell occupies.

`rows[0].cells[0].rowSpan``number`

Optional

The number of rows that the cell occupies.

To add a video element to the user's design, set the following parameters:

`type``string`

Required

The type of element. For video elements, this must be `"VIDEO"`.

`ref``string`

Required

A unique identifier that points to a video in Canva's backend.

`width``number`

Sometimes required

The width of the element, in pixels.

If `height` is a number, this can be set to `"auto"`.

`height``number`

Sometimes required

The height of the element, in pixels.

If `width` is a number, this can be set to `"auto"`.

`top``number`

Sometimes required

The distance from the top edge of the page, in pixels.

The container could be a page or a group.

`left``number`

Sometimes required

The distance from the left edge of the container, in pixels.

The container could be a page or a group.

`rotation``number`

Optional

The rotation of the element, in degrees. This must be a number between `-180` and `180`.

This property doesn't have an effect unless you also set position properties for the element. To set a position, you must provide the `width`, `height`, `top`, and `left` properties.

## Returns

`Promise<void>`
