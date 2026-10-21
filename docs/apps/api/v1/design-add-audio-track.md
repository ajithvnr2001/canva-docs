---
url: https://www.canva.dev/docs/apps/api/v1/design-add-audio-track/
title: addAudioTrack - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:27.529537+00:00
---

# addAudioTrack - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-add-audio-track/

API reference

v1 (Deprecated)

Asset

[getTemporaryUrl](https://www.canva.dev/docs/apps/api/v1/asset-get-temporary-url/)[findFonts](https://www.canva.dev/docs/apps/api/v1/asset-find-fonts/)[openColorSelector](https://www.canva.dev/docs/apps/api/v1/asset-open-color-selector/)[requestFontSelection](https://www.canva.dev/docs/apps/api/v1/asset-request-font-selection/)[upload](https://www.canva.dev/docs/apps/api/v1/asset-upload/)

Design

[addAudioTrack](https://www.canva.dev/docs/apps/api/v1/design-add-audio-track/)[addNativeElement](https://www.canva.dev/docs/apps/api/v1/design-add-native-element/)[addPage](https://www.canva.dev/docs/apps/api/v1/design-add-page/)[getCurrentPageContext](https://www.canva.dev/docs/apps/api/v1/design-get-current-page-context/)[getDefaultPageDimensions](https://www.canva.dev/docs/apps/api/v1/design-get-default-page-dimensions/)[getDesignToken](https://www.canva.dev/docs/apps/api/v1/design-get-design-token/)[initAppElement](https://www.canva.dev/docs/apps/api/v1/design-init-app-element/)[overlay.registerOnCanOpen](https://www.canva.dev/docs/apps/api/v1/design-overlay-register-on-can-open/)[requestExport](https://www.canva.dev/docs/apps/api/v1/design-request-export/)[selection.registerOnChange](https://www.canva.dev/docs/apps/api/v1/design-selection-register-on-change/)[setCurrentPageBackground](https://www.canva.dev/docs/apps/api/v1/design-set-current-page-background/)[ui.makeDraggable](https://www.canva.dev/docs/apps/api/v1/design-ui-make-draggable/)[ui.startDrag](https://www.canva.dev/docs/apps/api/v1/design-ui-start-drag/)

Platform

[appProcess](https://www.canva.dev/docs/apps/api/v1/platform-app-process/)[appProcess.broadcastMessage](https://www.canva.dev/docs/apps/api/v1/platform-app-process-broadcast-message/)[appProcess.current](https://www.canva.dev/docs/apps/api/v1/platform-app-process-current/)[appProcess.current.getInfo](https://www.canva.dev/docs/apps/api/v1/platform-app-process-current-get-info/)[appProcess.current.requestClose](https://www.canva.dev/docs/apps/api/v1/platform-app-process-current-request-close/)[appProcess.current.setOnDispose](https://www.canva.dev/docs/apps/api/v1/platform-app-process-current-set-on-dispose/)[appProcess.requestClose](https://www.canva.dev/docs/apps/api/v1/platform-app-process-request-close/)[appProcess.registerOnMessage](https://www.canva.dev/docs/apps/api/v1/platform-app-process-register-on-message/)[appProcess.registerOnStateChange](https://www.canva.dev/docs/apps/api/v1/platform-app-process-register-on-state-change/)[getPlatformInfo](https://www.canva.dev/docs/apps/api/v1/platform-get-platform-info/)[requestOpenExternalUrl](https://www.canva.dev/docs/apps/api/v1/platform-request-open-external-url/)

User

[auth.getCanvaUserToken](https://www.canva.dev/docs/apps/api/v1/user-auth-get-canva-user-token/)[auth.requestAuthentication](https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/)

# addAudioTrack

API reference for the addAudioTrack method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Adds an audio track to the user's design.

To learn more, see [Creating audio tracks](https://www.canva.dev/docs/apps/creating-audio-tracks/).

## Usage
    
    
    import { addAudioTrack } from "@canva/design";
    
    import { upload } from "@canva/asset";
    
    
    
    
    // Upload an audio asset
    
    const audio = await upload({
    
      type: "AUDIO",
    
      title: "Example audio",
    
      mimeType: "audio/mp3",
    
      durationMs: 86047,
    
      url: "https://www.canva.dev/example-assets/audio-import/audio.mp3",
    
    });
    
    
    
    
    // Add the audio track to the user's design
    
    await addAudioTrack({
    
      ref: audio.ref,
    
    });

TS

Copy

## Permissions

Before an app that uses this method can be submitted for review, the `canva:design:content:write` permission must be enabled through the Developer Portal. To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Parameters

`options``object`

Required

The options for adding an audio track to the user's design.

`options.ref``string`

Required

A unique identifier that points to an audio asset in Canva's backend.

## Returns

`Promise<void>`
