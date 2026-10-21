---
url: https://www.canva.dev/docs/apps/api/preview/design-get-default-page-dimensions/
title: getDefaultPageDimensions - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:30.428033+00:00
---

# getDefaultPageDimensions - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-get-default-page-dimensions/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# getDefaultPageDimensions

API reference for the getDefaultPageDimensions method.

Copy page

This API is deprecated, and is no longer recommended for use, and should be removed from your app.

Gets the default dimensions that a new page will have when it is added to a design. It is possible for a user to resize a page without resizing the entire design, e.g. by clicking "Expand to Whiteboard". However, there will always be a single set of default dimensions for a design that is applied whenever a new page is created.

Returns `undefined` if the design is unbounded (e.g. Whiteboard or Doc).

## Usage

### Get default page dimensions
    
    
    import { getDefaultPageDimensions } from "@canva/design";
    
    
    
    
    const dimensions = await getDefaultPageDimensions();
    
    
    
    
    if (dimensions) {
    
      // Do something with the dimensions, e.g. `dimensions.width` and `dimensions.height`
    
    } else {
    
      // This design type does not have fixed dimensions, e.g. Whiteboard or Doc
    
    }

TYPESCRIPT

Copy

### Center element using page dimensions
    
    
    import { getDefaultPageDimensions, addElementAtPoint } from "@canva/design";
    
    import type { ImageElementAtPoint } from "@canva/design";
    
    
    
    
    const dimensions = await getDefaultPageDimensions();
    
    
    
    
    if (dimensions) {
    
      const elementWidth = 300;
    
      const elementHeight = 200;
    
    
    
    
      const element: ImageElementAtPoint = {
    
        type: 'image',
    
        dataUrl: 'data:image/png;base64,...',
    
        altText: { text: 'Centered image', decorative: false },
    
        top: (dimensions.height - elementHeight) / 2,
    
        left: (dimensions.width - elementWidth) / 2,
    
        width: elementWidth,
    
        height: elementHeight
    
      };
    
    
    
    
      await addElementAtPoint(element);
    
    }

TYPESCRIPT

Copy

## Returns

A `Promise` that resolves with either `undefined` or the following object:

`width``number`

View type definition

A width, in pixels.

`height``number`

View type definition

A height, in pixels.
