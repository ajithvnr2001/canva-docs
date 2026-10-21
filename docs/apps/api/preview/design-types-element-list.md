---
url: https://www.canva.dev/docs/apps/api/preview/design-types-element-list/
title: ElementList - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:59.258796+00:00
---

# ElementList - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-types-element-list/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# ElementList

API reference for the ElementList type.

Copy page

A list of elements.

## Methods

`count``function`

RequiredView type definition

Gets the number of items in the list.

**Returns**

The number of items.

`number`

`toArray``function`

RequiredView type definition

Converts the list to an array.

**Returns**

An array containing all items. The items are the same as in the list.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

`forEach``function`

RequiredView type definition

Executes a function for each item in the list.

**Parameters**

`callback``ForEachCallback<AbsoluteElement>`

RequiredView type definition

The function to run for each item.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Parameters**

`item``AbsoluteElement`

RequiredView type definition

The current item in the list.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Returns**

`void`

**Returns**

`void`

`filter``function`

RequiredView type definition

TypeFilterPredicate<AbsoluteElement, C>TypeFilterPredicate<AbsoluteElement, C>

FilterPredicate<AbsoluteElement>FilterPredicate<AbsoluteElement>

Creates a new array with items that match a specific type.

**Parameters**

`filter``TypeFilterPredicate<AbsoluteElement, C>`

RequiredView type definition

A function that checks if an item is of type `C`.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Parameters**

`item``AbsoluteElement`

RequiredView type definition

The item to test.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Returns**

`true` if the item is of type `C`, otherwise `false`.

`item is C`

**Returns**

An array of items that are of type `C`.

readonly `C`[]

Creates a new array with items that pass a test.

**Parameters**

`filter``FilterPredicate<AbsoluteElement>`

RequiredView type definition

A function that tests each item. Returns `true` to keep the item.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Parameters**

`item``AbsoluteElement`

RequiredView type definition

The item to test.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Returns**

`true` if the item should be included, otherwise `false`.

`boolean`

**Returns**

An array of items that passed the test.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

`moveBefore``function`

RequiredView type definition

Moves an existing item to a new position right before another item.

**Parameters**

`ref``AbsoluteElement | undefined`

RequiredView type definition

The existing item to move the item before. If `ref` is `undefined`, the item is moved to the end of the list. If `ref` does not exist in the list, the operation fails.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

`item``AbsoluteElement`

RequiredView type definition

The item to move. The operation fails if the item is not already in the list.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Returns**

`void`

`moveAfter``function`

RequiredView type definition

Moves an existing item to a new position right after another item.

**Parameters**

`ref``AbsoluteElement | undefined`

RequiredView type definition

The existing item to move the item after. If `ref` is `undefined`, the item is moved to the end of the list. If `ref` does not exist in the list, the operation fails.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

`item``AbsoluteElement`

RequiredView type definition

The item to move. The operation fails if the item is not already in the list.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Returns**

`void`

`delete``function`

RequiredView type definition

Removes an item from the list.

**Parameters**

`item``AbsoluteElement`

RequiredView type definition

The item to remove from the list.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

**Returns**

`void`

`insertBefore``function`

RequiredView type definition

Adds a copy of an item to the list and places it right before another item.

**Parameters**

`ref``AbsoluteElement | undefined`

RequiredView type definition

The existing item to place the new item before. If `ref` is `undefined`, the new item is added at the end of the list. If `ref` does not exist in the list, the operation fails.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

`state``InsertableElementState`

RequiredView type definition

An element state that can be inserted into a page.

RectElementStateRectElementState

ShapeElementStateShapeElementState

EmbedElementStateEmbedElementState

TextElementStateTextElementState

A state that creates a rectangle element.

The rectangle can be filled with image content, video content, or a solid color.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"rect"`.

`fill``FillState`Read-only

RequiredView type definition

The appearance of the rectangle's interior.

Properties of **fill**

`mediaContainer``MediaFillState | undefined`

RequiredView type definition

The media fill for the path, if any.

ImageFillStateImageFillState

VideoFillStateVideoFillState

A state that creates an image fill.

`type``string`Read-only

RequiredView type definition

The type of media.

The only valid value is `"image"`.

`imageRef``ImageRef`Read-only

RequiredView type definition

A unique identifier that points to an image asset in Canva's backend.

`flipX``boolean`

RequiredView type definition

If `true`, the image is flipped horizontally.

`flipY``boolean`

RequiredView type definition

If `true`, the image is flipped vertically.

A state that creates a video fill.

`type``string`Read-only

RequiredView type definition

The type of media.

The only valid value is `"video"`.

`videoRef``VideoRef`Read-only

RequiredView type definition

A unique identifier that points to a video asset in Canva's backend.

`flipX``boolean`

RequiredView type definition

If `true`, the video is flipped horizontally.

`flipY``boolean`

RequiredView type definition

If `true`, the video is flipped vertically.

`colorContainer``ColorFillState | undefined`

RequiredView type definition

The color fill for the path, if any.

SolidFillStateSolidFillState

UnsupportedUnsupported

A state that creates a solid color fill.

`type``string`Read-only

RequiredView type definition

The type of color.

The only valid value is `"solid"`.

`color``string`

RequiredView type definition

The color of the fill. This must be a valid, six-digit hex code, prefixed with a `#` symbol.

  * Must be six characters long.
  * Must start with a `#`.
  * Must use lowercase letters.



**Example**
    
    
     "#ff0099"

TS

Copy

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`stroke``StrokeState`Read-only

RequiredView type definition

The outline of the rectangle.

Properties of **stroke**

`weight``number`

RequiredView type definition

The weight (thickness) of the stroke.

**Minimum** : `0`

**Maximum** : `100`

`colorContainer``ColorFillState`

RequiredView type definition

The color of the stroke.

SolidFillStateSolidFillState

UnsupportedUnsupported

A state that creates a solid color fill.

`type``string`Read-only

RequiredView type definition

The type of color.

The only valid value is `"solid"`.

`color``string`

RequiredView type definition

The color of the fill. This must be a valid, six-digit hex code, prefixed with a `#` symbol.

  * Must be six characters long.
  * Must start with a `#`.
  * Must use lowercase letters.



**Example**
    
    
     "#ff0099"

TS

Copy

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`Read-only

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`Read-only

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`Read-only

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`Read-only

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

A state that creates a vector shape element.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"shape"`.

`viewBox``AlignedBoxState`Read-only

RequiredView type definition

The scale and cropping of the shape.

Properties of **viewBox**

`top``number`Read-only

RequiredView type definition

The distance of the shape from the top edge of the element, in pixels.

`left``number`Read-only

RequiredView type definition

The distance of the shape from the left edge of the element, in pixels.

`width``number`Read-only

RequiredView type definition

The width of the view box, in pixels.

`height``number`Read-only

RequiredView type definition

The height of the view box, in pixels.

`paths``ListState<PathState>`Read-only

RequiredView type definition

The paths that define the structure of the shape.

  * Must have between 1 and 30 paths.
  * Total size of all paths must not exceed 2kb.
  * Maximum of 6 unique fill colors across all paths.



For more information, see [ListState](https://www.canva.dev/docs/apps/api/preview/design-types-list-state/).

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`Read-only

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`Read-only

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`Read-only

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`Read-only

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

A state that creates an embed element, such as a YouTube video.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"embed"`.

`url``string`Read-only

RequiredView type definition

The URL of the rich media.

This URL must be supported by the Iframely API.

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`Read-only

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`Read-only

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`Read-only

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`Read-only

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

A state that creates a text element.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"text"`.

`text``object`Read-only

RequiredView type definition

The text content.

Properties of **text**

`regions``ListState<TextRegion>`

RequiredView type definition

A list of items that can be read.

For more information, see [ListState](https://www.canva.dev/docs/apps/api/preview/design-types-list-state/).

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`Read-only

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`Read-only

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`Read-only

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`Read-only

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

**Returns**

The added item, or `undefined` if the operation failed.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

`insertAfter``function`

RequiredView type definition

Adds a copy of an item to the list and places it right after another item.

**Parameters**

`ref``AbsoluteElement | undefined`

RequiredView type definition

The existing item to place the new item after. If `ref` is `undefined`, the new item is added at the start of the list. If `ref` does not exist in the list, the operation fails.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).

`state``InsertableElementState`

RequiredView type definition

An element state that can be inserted into a page.

RectElementStateRectElementState

ShapeElementStateShapeElementState

EmbedElementStateEmbedElementState

TextElementStateTextElementState

A state that creates a rectangle element.

The rectangle can be filled with image content, video content, or a solid color.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"rect"`.

`fill``FillState`Read-only

RequiredView type definition

The appearance of the rectangle's interior.

Properties of **fill**

`mediaContainer``MediaFillState | undefined`

RequiredView type definition

The media fill for the path, if any.

ImageFillStateImageFillState

VideoFillStateVideoFillState

A state that creates an image fill.

`type``string`Read-only

RequiredView type definition

The type of media.

The only valid value is `"image"`.

`imageRef``ImageRef`Read-only

RequiredView type definition

A unique identifier that points to an image asset in Canva's backend.

`flipX``boolean`

RequiredView type definition

If `true`, the image is flipped horizontally.

`flipY``boolean`

RequiredView type definition

If `true`, the image is flipped vertically.

A state that creates a video fill.

`type``string`Read-only

RequiredView type definition

The type of media.

The only valid value is `"video"`.

`videoRef``VideoRef`Read-only

RequiredView type definition

A unique identifier that points to a video asset in Canva's backend.

`flipX``boolean`

RequiredView type definition

If `true`, the video is flipped horizontally.

`flipY``boolean`

RequiredView type definition

If `true`, the video is flipped vertically.

`colorContainer``ColorFillState | undefined`

RequiredView type definition

The color fill for the path, if any.

SolidFillStateSolidFillState

UnsupportedUnsupported

A state that creates a solid color fill.

`type``string`Read-only

RequiredView type definition

The type of color.

The only valid value is `"solid"`.

`color``string`

RequiredView type definition

The color of the fill. This must be a valid, six-digit hex code, prefixed with a `#` symbol.

  * Must be six characters long.
  * Must start with a `#`.
  * Must use lowercase letters.



**Example**
    
    
     "#ff0099"

TS

Copy

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`stroke``StrokeState`Read-only

RequiredView type definition

The outline of the rectangle.

Properties of **stroke**

`weight``number`

RequiredView type definition

The weight (thickness) of the stroke.

**Minimum** : `0`

**Maximum** : `100`

`colorContainer``ColorFillState`

RequiredView type definition

The color of the stroke.

SolidFillStateSolidFillState

UnsupportedUnsupported

A state that creates a solid color fill.

`type``string`Read-only

RequiredView type definition

The type of color.

The only valid value is `"solid"`.

`color``string`

RequiredView type definition

The color of the fill. This must be a valid, six-digit hex code, prefixed with a `#` symbol.

  * Must be six characters long.
  * Must start with a `#`.
  * Must use lowercase letters.



**Example**
    
    
     "#ff0099"

TS

Copy

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`Read-only

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`Read-only

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`Read-only

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`Read-only

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

A state that creates a vector shape element.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"shape"`.

`viewBox``AlignedBoxState`Read-only

RequiredView type definition

The scale and cropping of the shape.

Properties of **viewBox**

`top``number`Read-only

RequiredView type definition

The distance of the shape from the top edge of the element, in pixels.

`left``number`Read-only

RequiredView type definition

The distance of the shape from the left edge of the element, in pixels.

`width``number`Read-only

RequiredView type definition

The width of the view box, in pixels.

`height``number`Read-only

RequiredView type definition

The height of the view box, in pixels.

`paths``ListState<PathState>`Read-only

RequiredView type definition

The paths that define the structure of the shape.

  * Must have between 1 and 30 paths.
  * Total size of all paths must not exceed 2kb.
  * Maximum of 6 unique fill colors across all paths.



For more information, see [ListState](https://www.canva.dev/docs/apps/api/preview/design-types-list-state/).

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`Read-only

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`Read-only

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`Read-only

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`Read-only

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

A state that creates an embed element, such as a YouTube video.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"embed"`.

`url``string`Read-only

RequiredView type definition

The URL of the rich media.

This URL must be supported by the Iframely API.

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`Read-only

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`Read-only

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`Read-only

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`Read-only

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

A state that creates a text element.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"text"`.

`text``object`Read-only

RequiredView type definition

The text content.

Properties of **text**

`regions``ListState<TextRegion>`

RequiredView type definition

A list of items that can be read.

For more information, see [ListState](https://www.canva.dev/docs/apps/api/preview/design-types-list-state/).

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`Read-only

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`Read-only

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`Read-only

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`Read-only

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

**Returns**

The added item, or `undefined` if the operation failed.

For more information, see [AbsoluteElement](https://www.canva.dev/docs/apps/api/preview/design-types-absolute-element/).
