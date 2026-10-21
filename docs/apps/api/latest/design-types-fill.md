---
url: https://www.canva.dev/docs/apps/api/latest/design-types-fill/
title: Fill - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:52.214133+00:00
---

# Fill - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/latest/design-types-fill/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Fill

API reference for the Fill type.

Copy page

Describes how a fill is filled with color or media.

If both `media` and `color` are defined, `media` takes precedence.

## Properties

`mediaContainer``object`Read-only

RequiredView type definition

A media fill, if any.

`set``function`

RequiredView type definition

**Parameters**

`state``MediaFillState | undefined`

RequiredView type definition

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

**Returns**

`void`

`ref``MediaFill | undefined`

RequiredView type definition

ImagesImages

VideosVideos

An image that fills the interior of a media.

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

A video that fills the interior of a media.

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

`colorContainer``object`Read-only

RequiredView type definition

A color fill, if any.

`set``function`

RequiredView type definition

**Parameters**

`state``SolidFillState | undefined`

RequiredView type definition

Properties of **state**

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

**Returns**

`void`

`ref``ColorFill | undefined`

RequiredView type definition

SolidFillSolidFill

UnsupportedUnsupported

A solid color that fills an interior.

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
