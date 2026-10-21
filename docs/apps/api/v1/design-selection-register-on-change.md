---
url: https://www.canva.dev/docs/apps/api/v1/design-selection-register-on-change/
title: selection.registerOnChange - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:30.781367+00:00
---

# selection.registerOnChange - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-selection-register-on-change/

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

# selection.registerOnChange

API reference for the selection.registerOnChange method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Registers a callback that runs when a user selects (or deselects) content within a design.

To learn more, see [Selection API](https://www.canva.dev/docs/apps/selection/).

## Usage
    
    
    import { selection } from "@canva/design";
    
    
    
    
    await selection.registerOnChange({
    
      scope: "plaintext",
    
      onChange: (event) => {
    
        console.log(event);
    
      },
    
    });

TS

Copy

## Permissions

Before an app that uses this method can be [submitted for review](https://www.canva.dev/docs/apps/submitting-apps/), the following permissions must be enabled through the Developer Portal:

  * `canva:design:content:read`, if the app calls the `read` method
  * `canva:design:content:write`, if the app calls the `save` method



To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Parameters

`options``object`

Required

The options for registering a selection callback.

`options.scope``string`

Required

The type of content that should trigger a selection event.

The available options include:

  * `"image"`
  * `"plaintext"`
  * `"richtext"`
  * `"video"`



`options.onChange``function`

Required

The callback that runs when a user selects or deselects the specified type of content.

`options.onChange(event)``object`

Required

The selection event.

`options.onChange(event.scope)``string`

Required

The type of content that's selected. This matches the value passed into the `scope` property.

`options.onChange(event.count)``number`

Required

The number of distinct pieces of content that are selected.

`options.onChange(event.read())``function`

Required

Reads the selected content.

**Returns**

A `Promise` that resolves with the selected content and a `save` method for persisting changes to the content.

`options.onChange(event.read().contents)``array`

Required

The selected content. Each distinct piece of content — for example, the content of two separate text elements — is a separate object. These objects have properties and methods for interacting with the content.

The available properties depend on the value of the `scope` property.

**Images**

If the `scope` is `"image"`, each object has the following properties:

`ref``string`

Required

An identifier that points to an image asset in Canva's backend.

**Plaintext**

If the `scope` is `"plaintext"`, each object has the following properties:

`text``string`

Required

The text content, as plaintext.

**Richtext**

If the `scope` is `"richtext"`, each object is a `RichtextRange`. This is the same object that's returned by the [`createRichtextRange`](https://www.canva.dev/docs/apps/api/latest/design-create-richtext-range/) method.

**Videos**

If the `scope` is `"video"`, each object has the following properties:

`ref``string`

Required

An identifier that points to a video asset in Canva's backend.

`options.onChange(event.read().save())``function`

Required

Saves any changes made to the `contents` array and updates the user's design to reflect those changes.
