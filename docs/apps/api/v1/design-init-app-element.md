---
url: https://www.canva.dev/docs/apps/api/v1/design-init-app-element/
title: initAppElement - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:30.277198+00:00
---

# initAppElement - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-init-app-element/

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

# initAppElement

API reference for the initAppElement method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Initializes an element that the app can edit once it exists in the user's design.

To learn more, see [Creating app elements](https://www.canva.dev/docs/apps/creating-app-elements/).

## Usage
    
    
    import { initAppElement } from "@canva/design";
    
    
    
    
    // The data structure to attach to the app element
    
    type AppElementData = {
    
      text: string;
    
    };
    
    
    
    
    // Initialize the app element
    
    const appElement = initAppElement<AppElementData>({
    
      render: (data) => {
    
        return [
    
          {
    
            type: "TEXT",
    
            children: [data.text],
    
            top: 0,
    
            left: 0,
    
          },
    
        ];
    
      },
    
    });
    
    
    
    
    // Set the app element data
    
    appElement.addOrUpdateElement({
    
      text: "Hello world",
    
    });
    
    
    
    
    // Keep track of element changes
    
    appElement.registerOnElementChange((element) => {
    
      console.log("The app element has changed:", element?.data);
    
    });

TS

Copy

## Permissions

Before an app that uses this method can be submitted for review, the following permissions must be enabled through the Developer Portal:

  * `canva:design:content:read`, if the app calls the `registerOnElementChange` method
  * `canva:design:content:write`, if the app calls the `addOrUpdateElement` method



To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Parameters

`options``object`

Required

The options for initializing an app element.

`options.render``function`

Required

Renders an app element based on the current state of the app element data.

This function must return an array of one or more elements, such as images or shapes, and all of the elements must have the following positional properties:

  * `top`
  * `left`
  * `width`
  * `height`



`options.render(data)``function`

Required

The current state of the app element data.

## Returns

A `Promise` that resolves with the following object:

`result``object`

Required

The result of the successful initialization of an app element.

`result.addOrUpdateElement``function`

Required

If an app element is not selected, sets the initial data of the element and adds it to the user's design. If an app element is selected, overwrites the data and re-renders the element.

`result.addOrUpdateElement(data)``object`

Required

The data to attach to the app element.

`result.addOrUpdateElement(data, placement)``object`

Optional

The position of the app element on the page.

`result.addOrUpdateElement(data, placement.top)``number`

Required

The distance from the top edge of the page, in pixels.

`result.addOrUpdateElement(data, placement.left)``number`

Required

The distance from the left edge of the page, in pixels.

`result.addOrUpdateElement(data, placement.width)``number`

Required

The width of the element, in pixels.

If `height` is a number, this can be set to `"auto"`.

`result.addOrUpdateElement(data, placement.height)``number`

Required

The height of the element, in pixels.

If `width` is a number, this can be set to `"auto"`.

`result.addOrUpdateElement(data, placement.rotation)``number`

Optional

The rotation of the element, in degrees. This must be a number between `-180` and `180`.

`result.registerOnElementChange``function`

Required

Registers a callback that runs when the app element data or selection changes.

`result.registerOnElementChange(callback)``function`

Required

The callback that runs when the app element data or selection changes.

`result.registerOnElementChange(callback(element))``object`

Optional

The selected element. If an element is not selected, this is `undefined`.

`result.registerOnElementChange(callback(element.data))``object`

Required

The current state of the app element data.

`result.registerOnElementChange(callback(element.version))``string`

Required

The version number of the app.
