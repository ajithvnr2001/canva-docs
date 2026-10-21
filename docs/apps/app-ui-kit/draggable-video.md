---
url: https://www.canva.dev/docs/apps/app-ui-kit/draggable-video/
title: DraggableVideo - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:22.823305+00:00
---

# DraggableVideo - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/app-ui-kit/draggable-video/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# DraggableVideo

API reference for the DraggableVideo component.

Copy page

The `DraggableVideo` component has been deprecated. Instead, use the [`VideoCard`⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/canva-app-ui-kit-card-videocard--docs) component.

## Usage
    
    
    import React from "react";
    
    import { DraggableVideo } from "components/draggable_video";
    
    import { upload } from "@canva/asset";
    
    
    
    
    export function App() {
    
      return (
    
        <DraggableVideo
    
          mimeType="video/mp4"
    
          durationInSeconds={7}
    
          thumbnailImageSrc="https://www.canva.dev/example-assets/video-import/thumbnail-image.jpg"
    
          thumbnailVideoSrc="https://www.canva.dev/example-assets/video-import/thumbnail-video.mp4"
    
          resolveVideoRef={() => {
    
            return upload({
    
              type: "video",
    
              mimeType: "video/mp4",
    
              url: "https://www.canva.dev/example-assets/video-import/video.mp4",
    
              thumbnailImageUrl:
    
                "https://www.canva.dev/example-assets/video-import/thumbnail-image.jpg",
    
              thumbnailVideoUrl:
    
                "https://www.canva.dev/example-assets/video-import/thumbnail-video.mp4",
    
              aiDisclosure: "none",
    
            });
    
          }}
    
        />
    
      );
    
    }

TSX

Copy

## Props

`mimeType``string`

Required

The MIME type of the full-size video file.

The supported MIME types include:

  * `"video/avi"`
  * `"image/gif"`
  * `"video/x-m4v"`
  * `"video/x-matroska"`
  * `"video/quicktime"`
  * `"video/mp4"`
  * `"video/mpeg"`
  * `"video/webm"`



`resolveVideoRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.

`thumbnailImageSrc``string`

Required

A thumbnail image to display in the object panel of the Canva editor.

`thumbnailVideoSrc``string`

Optional

A low-resolution version of the full video with a maximum duration of 10 seconds. This can be omitted when the `mimeType` is `"video/gif"`.

`duration``number`

Optional

The duration of the full video, in seconds.

`width``number`

Optional

The width of the thumbnail, in pixels.

`height``number`

Optional

The height of the thumbnail, in pixels.

`previewSrc``string`

Optional

The URL or data URL of the image to use for the drag preview. This image will appear under the user's cursor as they during the drag event.

If omitted, `thumbnailImageSrc` will be used as a fallback.

`previewSize``object`

Optional

The dimensions of the drag preview. The dimensions should have the same aspect ratio as the full-size video.

If omitted, the `width` and `height` will be used as a fallback.

`previewSize.width``number`

Required

The width of the drag preview, in pixels.

`previewSize.height``number`

Required

The height of the drag preview, in pixels.

`fullSize``object`

Optional

The dimensions of the full-size video, in pixels.

If omitted, the dimensions of the drag preview will be used.

`fullSize.width``number`

Required

The width of the full-size video, in pixels.

`fullSize.height``number`

Required

The height of the full-size video, in pixels.
