---
url: https://www.canva.dev/docs/apps/api/preview/design-ui-start-drag/
title: ui.startDrag - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:31.707272+00:00
---

# ui.startDrag - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-ui-start-drag/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# ui.startDrag

API reference for the ui.startDrag method.

Copy page

This API is deprecated, and is no longer recommended for use, and should be removed from your app.

The method has been superseded by `startDragToPoint`.

Adds the specified element or content to a design at the end of a drag event.

## Parameters

Expand all

`event``DragStartEvent<E>`

RequiredView type definition

A drag start event.

Properties of **event**

`currentTarget``E`

RequiredView type definition

`dragData``object`

RequiredView type definition

Element or content to be added to the design at the end of the drag event.

AudioAudio

EmbedsEmbeds

TextText

VideosVideos

ImagesImages

Audio track to be added to the design at the end of a drag event.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"audio"`.

`resolveAudioRef``function`

RequiredView type definition

A function that returns a reference (ref) to an audio asset in Canva's backend.

**Returns**

A `Promise` that resolves with the following object:

`ref``AudioRef`

View type definition

A unique identifier that references an audio asset in Canva's backend.

`durationMs``number`

RequiredView type definition

The duration of the audio track, in milliseconds.

`title``string`

RequiredView type definition

A human readable title for the audio track.

Embed element to be added to the design at the end of a drag event.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"embed"`.

`previewSize``Dimensions`

RequiredView type definition

The dimensions of the preview image.

Properties of **previewSize**

`width``number`

RequiredView type definition

A width, in pixels.

`height``number`

RequiredView type definition

A height, in pixels.

`previewUrl``string`

RequiredView type definition

The URL of an image to display under the user's cursor during the drag and drop event.

`embedUrl``string`

RequiredView type definition

The URL of media that can be embedded, such as the URL of a YouTube video.

This URL must be supported by the Iframely API.

Text element or content to be added to the design at the end of a drag event.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"text"`.

`children``string[]`

OptionalView type definition

The text content to drag.

`textAlign``string`

OptionalView type definition

The alignment of the text.

**Default value** : `"start"`

**Available values** :

  * `"start"`
  * `"center"`
  * `"end"`
  * `"justify"`



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



`fontRef``FontRef`

Optional

View type definition

A unique identifier that points to a font asset in Canva's backend.

Video element or content to be added to the design at the end of a drag event.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"video"`.

`resolveVideoRef``function`

RequiredView type definition

A function that returns a reference (ref) to a video asset in Canva's backend.

**Returns**

A `Promise` that resolves with the following object:

`ref``VideoRef`

View type definition

A unique identifier that references a video asset in Canva's backend.

`previewSize``Dimensions`

RequiredView type definition

The dimensions of the preview image.

Properties of **previewSize**

`width``number`

RequiredView type definition

A width, in pixels.

`height``number`

RequiredView type definition

A height, in pixels.

`previewUrl``string`

RequiredView type definition

The URL of an image to display under the user's cursor during the drag and drop event.

`fullSize``Dimensions`

OptionalView type definition

The dimensions of the full-size video.

  * These dimensions are used when adding the video to the design
  * If omitted, the `previewSize` dimensions are used as a fallback.



Properties of **fullSize**

`width``number`

RequiredView type definition

A width, in pixels.

`height``number`

RequiredView type definition

A height, in pixels.

Image element or content to be added to the design at the end of a drag event.

`type``string`

RequiredView type definition

The type of element.

The only valid value is `"image"`.

`previewSize``Dimensions`

RequiredView type definition

The dimensions of the preview image.

Properties of **previewSize**

`width``number`

RequiredView type definition

A width, in pixels.

`height``number`

RequiredView type definition

A height, in pixels.

`resolveImageRef``function`

RequiredView type definition

A function that returns a reference (ref) to an audio asset in Canva's backend.

**Returns**

A `Promise` that resolves with the following object:

`ref``ImageRef`

View type definition

A unique identifier that references an image asset in Canva's backend.

`previewUrl``string`

RequiredView type definition

The URL of an image to display under the user's cursor during the drag and drop event.

`fullSize``Dimensions`

OptionalView type definition

The dimensions of the full-size image.

Properties of **fullSize**

`width``number`

RequiredView type definition

A width, in pixels.

`height``number`

RequiredView type definition

A height, in pixels.

## Returns

`Promise<void>`

## Permissions

To use this method, the `canva:design:content:write` permission must be enabled for the app. To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).
