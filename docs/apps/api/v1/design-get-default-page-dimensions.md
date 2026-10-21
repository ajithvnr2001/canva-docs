---
url: https://www.canva.dev/docs/apps/api/v1/design-get-default-page-dimensions/
title: getDefaultPageDimensions - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:28.719704+00:00
---

# getDefaultPageDimensions - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-get-default-page-dimensions/

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

# getDefaultPageDimensions

API reference for the getDefaultPageDimensions method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Gets the default dimensions that a new page will have when it's added to a design. To learn more about adding pages to a design, see [`addPage`](https://www.canva.dev/docs/apps/api/latest/design-add-page/).

Some types of designs, such as [whiteboards⁠(opens in a new tab or window)](https://www.canva.com/online-whiteboard/templates/), are _unbounded_. An unbounded design is one that doesn't have dimensions. In these cases, this method returns `undefined`.

## Usage
    
    
    import { getDefaultPageDimensions } from "@canva/design";
    
    
    
    
    const defaultPageDimensions = await getDefaultPageDimensions();
    
    
    
    
    // If `undefined`, the design is unbounded
    
    if (!defaultPageDimensions) {
    
      return;
    
    }
    
    
    
    
    const headerElementWidth = defaultPageDimensions.width * 0.5;
    
    const embedElementWidth = defaultPageDimensions.width * 0.4;
    
    
    
    
    await addPage({
    
      elements: [
    
        {
    
          ...headerElement,
    
          width: headerElementWidth,
    
          height: "auto",
    
          // Shift from the top by 10%
    
          top: defaultPageDimensions.height * 0.1,
    
          // Shift it by 50% of the page width, then subtract 50% of the group element width.
    
          left: defaultPageDimensions.width / 2 - headerElementWidth / 2,
    
        },
    
        {
    
          ...embedElement,
    
          width: embedElementWidth,
    
          height: "auto",
    
          // Shift from the top by 40%
    
          top: defaultPageDimensions.height * 0.4,
    
          // Shift it by 50% of the page width, then subtract 50% of the group element width.
    
          left: defaultPageDimensions.width / 2 - embedElementWidth / 2,
    
        },
    
      ],
    
    });

TS

Copy

## Returns

A `Promise` that resolves with the following result:

`result``object`

Optional

The successful result of getting the default page dimensions, or `undefined` if the design is unbounded.

`result.width``number`

Required

The width of the page, in pixels.

`result.height``number`

Required

The height of the page, in pixels.
