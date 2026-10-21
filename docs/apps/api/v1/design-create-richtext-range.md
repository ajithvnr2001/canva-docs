---
url: https://www.canva.dev/docs/apps/api/v1/design-create-richtext-range/
title: createRichtextRange - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:32.627041+00:00
---

# createRichtextRange - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-create-richtext-range/

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

# createRichtextRange

API reference for the createRichtextRange method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Creates a richtext range, which is an object that represents a range of formatted text — anything from a single word to multiple paragraphs — and exposes methods for safely interacting with that text.

To learn more, see [Creating text](https://www.canva.dev/docs/apps/creating-text/).

## Usage
    
    
    import { createRichtextRange } from "@canva/preview/design";
    
    const range = createRichtextRange();

TSX

Copy

## Parameters

This method doesn't have any parameters.

## Returns

An object with the following properties:

`appendText``function`

Required

Appends characters to the end of a richtext range.

**Example**
    
    
     import { createRichtextRange } from "@canva/preview/design";
    
    const range = createRichtextRange();
    
    range.appendText("Hello world");

TSX

Copy

**Parameters**

`characters``string`

Required

The text to append to the range.

`formatting``object`

Optional

The [inline formatting options](https://www.canva.dev/docs/apps/api/v1/design-create-richtext-range/#inline-formatting) for the text.

**Returns**

An object with the following properties:

`bounds``object`

Required

A region of text.

`bounds.start``number`

Required

The index of the character that marks the start of the region.

`bounds.length``number`

Required

The length of the region.

`formatParagraph``function`

Required

Formats all paragraphs that overlap the given bounds. The newline character — `\n` — indicates the end of a paragraph. All paragraphs that overlap the provided bounds will be formatted in their entirety.

**Example**
    
    
     import { createRichtextRange } from "@canva/preview/design";
    
    const range = createRichtextRange();
    
    range.appendText("This is the first paragraph.\nThis is the second paragraph.");
    
    range.formatParagraph({ start: 0, length: 1 }, { fontWeight: "bold" });

TSX

Copy

**Parameters**

`bounds``object`

Required

A region of text.

`bounds.start``number`

Required

The index of the character that marks the start of the region.

`bounds.length``number`

Required

The length of the region.

`formatting``object`

Required

The [paragraph formatting options](https://www.canva.dev/docs/apps/api/v1/design-create-richtext-range/#paragraph-formatting) for the text.

**Returns**

An object with the following properties:

`bounds``object`

Required

The boundaries of the formatted text.

`bounds.start``number`

Required

The index of the character that marks the start of the formatted text.

`bounds.length``number`

Required

The length of the formatted text.

`formatText``function`

Required

Formats the specified region of text with inline formatting.

**Example**
    
    
     import { createRichtextRange } from "@canva/preview/design";
    
    const range = createRichtextRange();
    
    range.appendText("Hello world");
    
    range.formatText({ start: 0, length: 5 }, { fontWeight: "bold" });

TSX

Copy

**Parameters**

`bounds``object`

Required

A region of text.

`bounds.start``number`

Required

The index of the character that marks the start of the region.

`bounds.length``number`

Required

The length of the region.

`formatting``object`

Required

The [inline formatting options](https://www.canva.dev/docs/apps/api/v1/design-create-richtext-range/#inline-formatting) for the text.

**Returns**

An object with the following properties:

`bounds``object`

Required

A region of text.

`bounds.start``number`

Required

The index of the character that marks the start of the region.

`bounds.length``number`

Required

The length of the region.

`readPlaintext``function`

Required

Gets the plaintext representation of a richtext range.

**Example**
    
    
     import { createRichtextRange } from "@canva/preview/design";
    
    const range = createRichtextRange();
    
    range.appendText("Hello world");
    
    const plaintext = range.readPlaintext(); // => "Hello world"

TSX

Copy

**Returns**

A `Promise` that resolves with a string.

`readTextRegions``function`

Required

Gets the current state of the richtext range as an array of text regions.

**Example**
    
    
     import { createRichtextRange } from "@canva/preview/design";
    
    const range = createRichtextRange();
    
    range.appendText("Hello world");
    
    const regions = range.readTextRegions();
    
    console.log(regions); // => [{ text: "Hello world" }]

TSX

Copy

**Returns**

An array of text regions.

Each region is a object with the following properties:

`text``string`

Required

The plaintext content of the region.

`formatting``object`

Required

The formatting information for the region.

`replaceText``function`

Required

Replaces a region of richtext with the specified characters.

**Example**
    
    
     import { createRichtextRange } from "@canva/preview/design";
    
    const range = createRichtextRange();
    
    range.appendText("Hello world");
    
    range.replaceText({ start: 0, index: 5 }, "HELLO");

TSX

Copy

**Parameters**

`bounds``object`

Required

A region of text.

`bounds.start``number`

Required

The index of the character that marks the start of the region.

`bounds.length``number`

Required

The length of the region.

`characters``string`

Required

The replacement text.

`formatting``object`

Optional

The [inline formatting options](https://www.canva.dev/docs/apps/api/v1/design-create-richtext-range/#inline-formatting) for the text.

**Returns**

An object with the following properties:

`bounds``object`

Required

A region of text.

`bounds.start``number`

Required

The index of the character that marks the start of the region.

`bounds.length``number`

Required

The length of the region.

## Formatting options

Richtext can be formatted in a variety of ways.

The formatting options fall into the following categories:

  * Paragraph formatting
  * Inline formatting



The available options depend on how the text is being operated on.

### Paragraph formatting

Apps can only use paragraph formatting when operating on entire paragraphs.

`fontRef``string`

Optional

A unique identifier that references a font in Canva's backend. To learn more, see [Fonts](https://www.canva.dev/docs/apps/fonts/).

`fontSize``number`

Optional

The size of the text, in pixels. This must be an integer between 1 and 1000 (inclusive).

In the user interface, the font size is displayed as points (pts), not pixels. This means the font size defined here will be different from what's shown to the user.

The default value is `16`.

`listLevel``string`

Optional

The indentation level of a list item.

`listMarker``string`

Optional

The appearance of a list item.

The available options include:

  * `"none"`
  * `"disc"`
  * `"circle"`
  * `"square"`
  * `"decimal"`
  * `"lower-alpha"`
  * `"lower-roman"`
  * `"checked"`
  * `"unchecked"`



The default value is `"none"`.

`textAlign``string`

Optional

The alignment of the text.

The available options include:

  * `"start"`
  * `"center"`
  * `"end"`



The default value is `"start"`.

### Inline formatting

Apps can use inline formatting when operating on all text, including paragraphs.

`color``string`

Optional

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol — for example, `"#ff0099"`.

The default value is `"#000000"`.

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

`strikethrough``string`

Optional

The strikethrough styling of the text.

The available options include:

  * `"none"`
  * `"strikethrough"`



The default value is `"none"`.

`link``string`

Optional

The URL of a web page to use as a link for the text.
