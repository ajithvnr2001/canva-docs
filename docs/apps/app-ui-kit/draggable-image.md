---
url: https://www.canva.dev/docs/apps/app-ui-kit/draggable-image/
title: DraggableImage - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:23.194951+00:00
---

# DraggableImage - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/app-ui-kit/draggable-image/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# DraggableImage

API reference for the DraggableImage component.

Copy page

The `DraggableImage` component has been deprecated. Instead, use the [`ImageCard`⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/canva-app-ui-kit-card-imagecard--docs) component.

## Usage
    
    
    import React from "react";
    
    import { DraggableImage } from "components/draggable_image";
    
    import { upload } from "@canva/asset";
    
    
    
    
    export function App() {
    
      return (
    
        <DraggableImage
    
          src="https://www.canva.dev/example-assets/image-import/thumbnail.jpg"
    
          resolveImageRef={() => {
    
            return upload({
    
              type: "image",
    
              mimeType: "image/jpeg",
    
              url: "https://www.canva.dev/example-assets/image-import/image.jpg",
    
              thumbnailUrl:
    
                "https://www.canva.dev/example-assets/image-import/thumbnail.jpg",
    
              aiDisclosure: "none",
    
            });
    
          }}
    
        />
    
      );
    
    }

TSX

Copy

## Props

`src``string`

Required

The URL or data URL of the image to embed in the app's user interface.

This image must have a MIME type of `"image/jpeg"` or `"image/png"`.

`resolveImageRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.

`fullSize``object`

Optional

The dimensions of the full-size image, in pixels.

`fullSize.width``number`

Sometimes required

The width of the full-size image, in pixels.

`fullSize.height``number`

Sometimes required

The height of the full-size image, in pixels.

`previewSrc``string`

Optional

The data URL of the image used in the _drag preview_. This is the image that appears under the user's cursor during the drag event. If omitted, the image from the `src` prop is used.

This image must have a MIME type of `"image/jpeg"` or `"image/png"`.

`previewSize``object`

Optional

The dimensions of the drag preview, in pixels.

`previewSize.width``number`

Sometimes required

The width of the drag preview, in pixels.

`previewSize.height``number`

Sometimes required

The height of the drag preview, in pixels.
