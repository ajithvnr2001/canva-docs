---
url: https://www.canva.dev/docs/apps/api/preview/design-add-native-element/
title: addNativeElement - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:30.115627+00:00
---

# addNativeElement - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-add-native-element/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# addNativeElement

API reference for the addNativeElement method.

Copy page

This API is deprecated, and is no longer recommended for use, and should be removed from your app.

Adds a native element to the user's design.

## Usage: Basic usage
    
    
    import { addNativeElement } from "@canva/design";
    
    import type { NativeElementWithBox } from "@canva/design";
    
    
    
    
    const element: NativeElementWithBox = {
    
      type: 'text',
    
      children: ['Legacy element'],
    
      top: 100,
    
      left: 100,
    
      width: 200
    
    };
    
    
    
    
    await addNativeElement(element);

TYPESCRIPT

Copy

## Parameters

Expand all

`element``object`

RequiredView type definition

The element to add to the user's design.

NativeElement

NativeElement

NativeElementWithBox

NativeElementWithBox

The type has been superseded by `DesignElement`.

An element that's natively supported by the Canva editor.

Images

Images

Videos

Videos

Embeds

Embeds

Text

Text

Shapes

Shapes

Groups

Groups

The type has been superseded by `ImageElement`.

An element that renders image content.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"image"`.

`altText``AltText | undefined`

RequiredView type definition

A description of the image content.

Use `undefined` for content with no description.

Properties of **altText**

`text``string`

RequiredView type definition

The text content.

`decorative``boolean | undefined`

RequiredView type definition

Indicates where the alternative text should be displayed.

  * If `true`, the alternative text will only be displayed in the editor.
  * If `false`, the alternative text will be displayed in the editor and in view-only mode.



`dataUrl``string`

OptionalView type definition

A data URL that contains the image data.

`ref``ImageRef`

OptionalView type definition

A unique identifier that points to an image asset in Canva's backend.

The type has been superseded by `VideoElement`.

An element that renders video content.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"video"`.

`ref``VideoRef`

RequiredView type definition

A unique identifier that points to a video asset in Canva's backend.

`altText``AltText | undefined`

RequiredView type definition

A description of the video content.

Use `undefined` for content with no description.

Properties of **altText**

`text``string`

RequiredView type definition

The text content.

`decorative``boolean | undefined`

RequiredView type definition

Indicates where the alternative text should be displayed.

  * If `true`, the alternative text will only be displayed in the editor.
  * If `false`, the alternative text will be displayed in the editor and in view-only mode.



`imageBox``VideoImageBox`

Optional

View type definition

Options for configuring the cropping of the video.

Properties of **imageBox**

`top``number`

RequiredView type definition

The distance of the image box from the top edge of the video, in pixels.

`left``number`

RequiredView type definition

The distance of the image box from the left edge of the video, in pixels.

`width``number`

RequiredView type definition

The width of the image box, in pixels.

`height``number`

RequiredView type definition

The height of the image box, in pixels.

`trim``VideoTrim`

Optional

View type definition

Options for configuring the start, and end of the video.

Properties of **trim**

`startInSeconds``number`

RequiredView type definition

The start point of the video, in seconds relative to the start of the source video.

`endInSeconds``number`

RequiredView type definition

The end point of the video, in seconds relative to the start of the source video.

The type has been superseded by `EmbedElement`.

An element that renders rich media, such as a YouTube video.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"embed"`.

`url``string`

RequiredView type definition

The URL of the rich media.

This URL must be supported by the Iframely API.

The type has been superseded by `TextElement`.

An element that renders text content.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"text"`.

`children``string[]`

RequiredView type definition

The text content.

Only the first element in this array is used.

`fontSize``number`

OptionalView type definition

The size of the text.

**Minimum** : `1`

**Maximum** : `1000`

**Default value** : `16`

`textAlign``string`

OptionalView type definition

The alignment of the text.

**Default value** : `"start"`

**Available values** :

  * `"start"`
  * `"center"`
  * `"end"`
  * `"justify"`



`color``string`

OptionalView type definition

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`fontRef``FontRef`

OptionalView type definition

A unique identifier that points to a font asset in Canva's backend.

`fontWeight``FontWeight`

OptionalView type definition

The weight (thickness) of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



`fontStyle``string`

OptionalView type definition

The style of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"italic"`



`decoration``string`

OptionalView type definition

The decoration of the font.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"underline"`



The type has been superseded by `ShapeElement`.

An element that renders a vector shape.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"shape"`.

`viewBox``ShapeViewBox`

RequiredView type definition

Options for configuring the scale and cropping of the shape.

Properties of **viewBox**

`top``number`

RequiredView type definition

The distance of the shape from the top edge of the element, in pixels.

`left``number`

RequiredView type definition

The distance of the shape from the left edge of the element, in pixels.

`width``number`

RequiredView type definition

The width of the view box, in pixels.

`height``number`

RequiredView type definition

The height of the view box, in pixels.

`paths``ShapePath[]`

RequiredView type definition

The paths that define the structure of the shape.

  * There must be between 1 and 30 paths (inclusive).
  * The maximum combined size of all paths must not exceed 2kb.
  * The maximum number of unique fill colors across all paths is 6.



Properties of **paths**

`d``string`

RequiredView type definition

The shape of the path.

This is similar to the `d` attribute of an SVG's `path` element, with some limitations:

  * The path must start with an M command.
  * The path must not have more than one M command.
  * The path must not use the Q command.
  * The path must be closed, either by: 
    * Using a Z command at the end of the path
    * Having the last coordinate match the first coordinate



`fill``Fill`

RequiredView type definition

The appearance of the path's interior.

Properties of **fill**

`dropTarget``boolean`

OptionalView type definition

If `true`, users can replace a fill by dropping an image or video onto it.

`color``string`

OptionalView type definition

The color of the fill as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`asset``object`

OptionalView type definition

An image or video to use as the fill.

ImagesImages

VideosVideos

An image asset that fills a path's interior.

`type``string`

RequiredView type definition

The type of fill.

The only valid value is `"image"`.

`ref``ImageRef`

RequiredView type definition

A unique identifier that points to an image asset in Canva's backend.

`altText``AltText`

OptionalView type definition

A description of the image content.

Use `undefined` for content with no description.

Properties of **altText**

`text``string`

RequiredView type definition

The text content.

`decorative``boolean | undefined`

RequiredView type definition

Indicates where the alternative text should be displayed.

  * If `true`, the alternative text will only be displayed in the editor.
  * If `false`, the alternative text will be displayed in the editor and in view-only mode.



A video asset that fills a path's interior.

`type``string`

RequiredView type definition

The type of fill.

The only valid value is `"video"`.

`ref``VideoRef`

RequiredView type definition

A unique identifier that points to a video asset in Canva's backend.

`altText``AltText`

OptionalView type definition

A description of the image content.

Use `undefined` for content with no description.

Properties of **altText**

`text``string`

RequiredView type definition

The text content.

`decorative``boolean | undefined`

RequiredView type definition

Indicates where the alternative text should be displayed.

  * If `true`, the alternative text will only be displayed in the editor.
  * If `false`, the alternative text will be displayed in the editor and in view-only mode.



`stroke``PathStroke`

OptionalView type definition

The outline of the path.

Properties of **stroke**

`weight``number`

RequiredView type definition

The weight (thickness) of the stroke.

**Minimum** : `0`

**Maximum** : `100`

`color``string`

RequiredView type definition

The color of the stroke as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`strokeAlign``string`

RequiredView type definition

The alignment of the stroke.

The only valid value is `"inset"`.

The type has been superseded by `GroupElement`.

An element that contains two or more elements.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"group"`.

`children``GroupContentAtPoint[]`

RequiredView type definition

The elements to render within the group.

  * Each element within a group must have dimensions and a position.
  * The dimensions and positions are relative to the dimensions and positions of the group.



The type has been superseded by `ElementAtPoint`.

An element that's natively supported by the Canva editor and has positional properties.

Images

Images

Videos

Videos

Embeds

Embeds

Text

Text

Shapes

Shapes

Groups

Groups

The type has been superseded by `ImageElementAtPoint`.

An element that renders image content and has positional properties.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"image"`.

`altText``AltText | undefined`

RequiredView type definition

A description of the image content.

Use `undefined` for content with no description.

Properties of **altText**

`text``string`

RequiredView type definition

The text content.

`decorative``boolean | undefined`

RequiredView type definition

Indicates where the alternative text should be displayed.

  * If `true`, the alternative text will only be displayed in the editor.
  * If `false`, the alternative text will be displayed in the editor and in view-only mode.



`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`width``number`

RequiredView type definition

A width, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`height``number`

RequiredView type definition

A height, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`rotation``number`

OptionalView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`dataUrl``string`

OptionalView type definition

A data URL that contains the image data.

`ref``ImageRef`

OptionalView type definition

A unique identifier that points to an image asset in Canva's backend.

The type has been superseded by `VideoElementAtPoint`.

An element that renders video content and has positional properties.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"video"`.

`ref``VideoRef`

RequiredView type definition

A unique identifier that points to a video asset in Canva's backend.

`altText``AltText | undefined`

RequiredView type definition

A description of the video content.

Use `undefined` for content with no description.

Properties of **altText**

`text``string`

RequiredView type definition

The text content.

`decorative``boolean | undefined`

RequiredView type definition

Indicates where the alternative text should be displayed.

  * If `true`, the alternative text will only be displayed in the editor.
  * If `false`, the alternative text will be displayed in the editor and in view-only mode.



`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`width``number`

RequiredView type definition

A width, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`height``number`

RequiredView type definition

A height, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`imageBox``VideoImageBox`

Optional

View type definition

Options for configuring the cropping of the video.

Properties of **imageBox**

`top``number`

RequiredView type definition

The distance of the image box from the top edge of the video, in pixels.

`left``number`

RequiredView type definition

The distance of the image box from the left edge of the video, in pixels.

`width``number`

RequiredView type definition

The width of the image box, in pixels.

`height``number`

RequiredView type definition

The height of the image box, in pixels.

`trim``VideoTrim`

Optional

View type definition

Options for configuring the start, and end of the video.

Properties of **trim**

`startInSeconds``number`

RequiredView type definition

The start point of the video, in seconds relative to the start of the source video.

`endInSeconds``number`

RequiredView type definition

The end point of the video, in seconds relative to the start of the source video.

`rotation``number`

OptionalView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

The type has been superseded by `EmbedElementAtPoint`.

An element that renders rich media, such as a YouTube video, and has positional properties.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"embed"`.

`url``string`

RequiredView type definition

The URL of the rich media.

This URL must be supported by the Iframely API.

`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`width``number`

RequiredView type definition

A width, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`height``number`

RequiredView type definition

A height, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`rotation``number`

OptionalView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

The type has been superseded by `TextElementAtPoint`.

An element that renders text content and has positional properties.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"text"`.

`children``string[]`

RequiredView type definition

The text content.

Only the first element in this array is used.

`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`fontSize``number`

OptionalView type definition

The size of the text.

**Minimum** : `1`

**Maximum** : `1000`

**Default value** : `16`

`textAlign``string`

OptionalView type definition

The alignment of the text.

**Default value** : `"start"`

**Available values** :

  * `"start"`
  * `"center"`
  * `"end"`
  * `"justify"`



`color``string`

OptionalView type definition

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`fontRef``FontRef`

OptionalView type definition

A unique identifier that points to a font asset in Canva's backend.

`fontWeight``FontWeight`

OptionalView type definition

The weight (thickness) of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



`fontStyle``string`

OptionalView type definition

The style of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"italic"`



`decoration``string`

OptionalView type definition

The decoration of the font.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"underline"`



`rotation``number`

OptionalView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`width``number`

OptionalView type definition

The width of the element, in pixels.

**Minimum** : `0`

**Maximum** : `32767`

The type has been superseded by `ShapeElementAtPoint`.

An element that renders a vector shape and has positional properties.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"shape"`.

`viewBox``ShapeViewBox`

RequiredView type definition

Options for configuring the scale and cropping of the shape.

Properties of **viewBox**

`top``number`

RequiredView type definition

The distance of the shape from the top edge of the element, in pixels.

`left``number`

RequiredView type definition

The distance of the shape from the left edge of the element, in pixels.

`width``number`

RequiredView type definition

The width of the view box, in pixels.

`height``number`

RequiredView type definition

The height of the view box, in pixels.

`paths``ShapePath[]`

RequiredView type definition

The paths that define the structure of the shape.

  * There must be between 1 and 30 paths (inclusive).
  * The maximum combined size of all paths must not exceed 2kb.
  * The maximum number of unique fill colors across all paths is 6.



Properties of **paths**

`d``string`

RequiredView type definition

The shape of the path.

This is similar to the `d` attribute of an SVG's `path` element, with some limitations:

  * The path must start with an M command.
  * The path must not have more than one M command.
  * The path must not use the Q command.
  * The path must be closed, either by: 
    * Using a Z command at the end of the path
    * Having the last coordinate match the first coordinate



`fill``Fill`

RequiredView type definition

The appearance of the path's interior.

Properties of **fill**

`dropTarget``boolean`

OptionalView type definition

If `true`, users can replace a fill by dropping an image or video onto it.

`color``string`

OptionalView type definition

The color of the fill as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`asset``object`

OptionalView type definition

An image or video to use as the fill.

ImagesImages

VideosVideos

An image asset that fills a path's interior.

`type``string`

RequiredView type definition

The type of fill.

The only valid value is `"image"`.

`ref``ImageRef`

RequiredView type definition

A unique identifier that points to an image asset in Canva's backend.

`altText``AltText`

OptionalView type definition

A description of the image content.

Use `undefined` for content with no description.

Properties of **altText**

`text``string`

RequiredView type definition

The text content.

`decorative``boolean | undefined`

RequiredView type definition

Indicates where the alternative text should be displayed.

  * If `true`, the alternative text will only be displayed in the editor.
  * If `false`, the alternative text will be displayed in the editor and in view-only mode.



A video asset that fills a path's interior.

`type``string`

RequiredView type definition

The type of fill.

The only valid value is `"video"`.

`ref``VideoRef`

RequiredView type definition

A unique identifier that points to a video asset in Canva's backend.

`altText``AltText`

OptionalView type definition

A description of the image content.

Use `undefined` for content with no description.

Properties of **altText**

`text``string`

RequiredView type definition

The text content.

`decorative``boolean | undefined`

RequiredView type definition

Indicates where the alternative text should be displayed.

  * If `true`, the alternative text will only be displayed in the editor.
  * If `false`, the alternative text will be displayed in the editor and in view-only mode.



`stroke``PathStroke`

OptionalView type definition

The outline of the path.

Properties of **stroke**

`weight``number`

RequiredView type definition

The weight (thickness) of the stroke.

**Minimum** : `0`

**Maximum** : `100`

`color``string`

RequiredView type definition

The color of the stroke as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`strokeAlign``string`

RequiredView type definition

The alignment of the stroke.

The only valid value is `"inset"`.

`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`width``number`

RequiredView type definition

A width, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`height``number`

RequiredView type definition

A height, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`rotation``number`

OptionalView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

The type has been superseded by `GroupElementAtPoint`.

An element that contains two or more elements and has positional properties.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"group"`.

`children``GroupContentAtPoint[]`

RequiredView type definition

The elements to render within the group.

  * Each element within a group must have dimensions and a position.
  * The dimensions and positions are relative to the dimensions and positions of the group.



`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`width``number`

RequiredView type definition

A width, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`height``number`

RequiredView type definition

A height, in pixels.

  * The pixels are relative to their container.



**Minimum** : `0`

**Maximum** : `32767`

`rotation``number`

OptionalView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

## Returns

`Promise<void>`

## Permissions

To use this method, the `canva:design:content:write` permission must be enabled for the app. To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Rate limit

This method has a rate limit of 30 requests every 10 seconds. This limit is shared with the `addElementAtPoint` and `addElementAtCursor` methods.
