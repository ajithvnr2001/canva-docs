---
url: https://www.canva.dev/docs/apps/app-ui-kit/draggable-embed/
title: DraggableEmbed - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:22.502689+00:00
---

# DraggableEmbed - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/app-ui-kit/draggable-embed/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# DraggableEmbed

API reference for the DraggableEmbed component.

Copy page

The `DraggableEmbed` component has been deprecated. Instead, use the [`EmbedCard`⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/canva-app-ui-kit-card-embedcard--docs) component.

## Usage
    
    
    import React from "react";
    
    import { DraggableEmbed } from "components/draggable_embed";
    
    
    
    
    export function App() {
    
      return (
    
        <DraggableEmbed
    
          embedUrl="https://www.youtube.com/embed/L3MtFGWRXAA"
    
          previewUrl="https://www.canva.dev/example-assets/images/puppyhood.jpg"
    
          previewSize={{ width: 320, height: 180 }}
    
          title="Heartwarming Chatter: Adorable Conversation with a Puppy"
    
          subtitle="Puppyhood"
    
        />
    
      );
    
    }

TSX

Copy

## Props

`embedUrl``string`

Required

The URL of the embeddable media.

This URL must be supported by Iframely. To learn more, see [What URLs to send to Iframely⁠(opens in a new tab or window)](https://iframely.com/docs/providers).

`previewUrl``string`

Required

The URL of a thumbnail image.

`previewSize``string`

Required

The dimensions of the preview image, in pixels.

`title``string`

Required

A human-readable title for the embed.

`subtitle``string`

Optional

A human-readable subtitle for the embed.
