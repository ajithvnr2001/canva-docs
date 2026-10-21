---
url: https://www.canva.dev/docs/apps/app-ui-kit/draggable-text/
title: DraggableText - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:22.709125+00:00
---

# DraggableText - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/app-ui-kit/draggable-text/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# DraggableText

API reference for the DraggableText component.

Copy page

The `DraggableText` component has been deprecated. Instead, use the [`TypographyCard`⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/canva-app-ui-kit-card-typographycard--docs) component.

## Usage

### Basic usage
    
    
    import React from "react";
    
    import { DraggableText } from "components/draggable_text";
    
    
    
    
    export function App() {
    
      return <DraggableText>Drag me into the design</DraggableText>;
    
    }

TSX

Copy

### Styling the text

You can use the `style` prop to style the text in the app's iframe. Where possible, Canva will use these styles to determine the style of the text that's dropped into the design.
    
    
    import React from "react";
    
    import { DraggableText } from "components/draggable_text";
    
    
    
    
    export function App() {
    
      return (
    
        <DraggableText
    
          style={{
    
            fontStyle: "italic",
    
            fontWeight: "bold",
    
            textAlign: "center",
    
            textDecoration: "underline",
    
          }}
    
        >
    
          Drag me into the design
    
        </DraggableText>
    
      );
    
    }

TSX

Copy

### Customizing the drag data

If you want the text that's dropped into the design to look different from the text that's in the app's iframe, set props that are distinct from the `style` prop.
    
    
    import React from "react";
    
    import { DraggableText } from "components/draggable_text";
    
    
    
    
    export function App() {
    
      return (
    
        <DraggableText
    
          style={{
    
            fontStyle: "italic",
    
            fontWeight: "bold",
    
            textAlign: "center",
    
            textDecoration: "underline",
    
          }}
    
          decoration="none"
    
          fontStyle="normal"
    
          fontWeight="normal"
    
          textAlign="end"
    
        >
    
          Drag me into the design
    
        </DraggableText>
    
      );
    
    }

TSX

Copy

## Props

`children``string`

Required

The text to make draggable.

`decoration``string`

Optional

The decoration of the text.

The available values include:

  * `"none"`
  * `"underline"`



The default value is `"none"`.

`fontStyle``string`

Optional

The style of the text.

The available values include:

  * `"normal"`
  * `"italic"`



The default value is `"normal"`.

`fontWeight``string`

Optional

The weight of the text.

The available values include:

  * `"normal"`
  * `"bold"`



The default value is `"normal"`.

`style``string`

Optional

The style of the text.

The available values include:

  * `"none"`
  * `"italic"`



The default value is `"none"`.

`textAlign``string`

Optional

The alignment of the text.

The available values include:

  * `"start"`
  * `"center"`
  * `"end"`



The default value is `"start"`.
