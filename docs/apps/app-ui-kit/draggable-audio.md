---
url: https://www.canva.dev/docs/apps/app-ui-kit/draggable-audio/
title: DraggableAudio - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:22.586321+00:00
---

# DraggableAudio - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/app-ui-kit/draggable-audio/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# DraggableAudio

API reference for the DraggableAudio component.

Copy page

The `DraggableAudio` component has been deprecated. Instead, use the [`AudioCard`⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-ui-kit/storybook/?path=/docs/canva-app-ui-kit-card-audiocard--docs) component.

## Usage
    
    
    import React from "react";
    
    import { AudioContextProvider } from "components/audio_context";
    
    import { DraggableAudio } from "components/draggable_audio";
    
    import { upload } from "@canva/asset";
    
    
    
    
    export function App() {
    
      return (
    
        <AudioContextProvider>
    
          <DraggableAudio
    
            title="Example audio"
    
            durationMs={86047}
    
            previewUrl="https://www.canva.dev/example-assets/audio-import/audio.mp3"
    
            resolveAudioRef={() => {
    
              return upload({
    
                type: "audio",
    
                title: "Example audio",
    
                mimeType: "audio/mp3",
    
                durationMs: 86047,
    
                url: "https://www.canva.dev/example-assets/audio-import/audio.mp3",
    
                aiDisclosure: "none",
    
              });
    
            }}
    
          />
    
        </AudioContextProvider>
    
      );
    
    }

TSX

Copy

The `AudioContextProvider` component ensures that only one audio file will play at a time.

## Props

`title``string`

Required

A human-readable title that appears in the Canva editor.

`url``string`

Required

The URL of the audio file.

`previewUrl``string`

Required

The URL of the audio file to play when the user clicks the **Play** button.

`durationMs``number`

Required

The duration of the audio file, in milliseconds.

`resolveAudioRef``function`

Required

A function that returns the result of the [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/) method.
