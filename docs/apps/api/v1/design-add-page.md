---
url: https://www.canva.dev/docs/apps/api/v1/design-add-page/
title: addPage - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:29.463971+00:00
---

# addPage - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/design-add-page/

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

# addPage

API reference for the addPage method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Adds a new page to the design. The new page is added immediately after the currently selected page.

## Usage

### Basic usage
    
    
    import { Button } from "@canva/app-ui-kit";
    
    import { addPage } from "@canva/design";
    
    
    
    
    export function App() {
    
      async function handleClick() {
    
        await addPage();
    
      }
    
    
    
    
      return <Button onClick={handleClick}>Add page</Button>;
    
    }

TSX

Copy

### Setting a title for the new page
    
    
    import { Button } from "@canva/app-ui-kit";
    
    import { addPage } from "@canva/design";
    
    
    
    
    export function App() {
    
      async function handleClick() {
    
        await addPage({
    
          title: "Hello world",
    
        });
    
      }
    
    
    
    
      return <Button onClick={handleClick}>Add page</Button>;
    
    }

TSX

Copy

### Setting a background for the new page
    
    
    import { Button } from "@canva/app-ui-kit";
    
    import { addPage } from "@canva/design";
    
    
    
    
    export function App() {
    
      async function handleClick() {
    
        await addPage({
    
          background: {
    
            color: "#ff0099",
    
          },
    
        });
    
      }
    
    
    
    
      return <Button onClick={handleClick}>Add page</Button>;
    
    }

TSX

Copy

### Including elements on the new page
    
    
    import { Button } from "@canva/app-ui-kit";
    
    import { addPage } from "@canva/design";
    
    
    
    
    export function App() {
    
      async function handleClick() {
    
        await addPage({
    
          elements: [
    
            {
    
              type: "TEXT",
    
              children: ["Hello world!"],
    
              width: 100,
    
              height: "auto",
    
              top: 0,
    
              left: 0,
    
            },
    
          ],
    
        });
    
      }
    
    
    
    
      return <Button onClick={handleClick}>Add page</Button>;
    
    }

TSX

Copy

## Permissions

Before an app that uses this method can be submitted for review, the `canva:design:content:write` permission must be enabled through the Developer Portal. To learn more, see [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).

## Rate limit

This method has a rate limit of 3 requests every 10 seconds.

## Parameters

`options``object`

Optional

The options for configuring the new page.

`options.background``object`

Optional

The background of the page, such as an image, color, or video. This property accepts the same options that are passed into the [`setCurrentPageBackground`](https://www.canva.dev/docs/apps/api/latest/design-set-current-page-background/) method.

`options.elements``array`

Optional

An array of elements to pre-populate on the new page.

`options.elements[0]``object`

Required

An individual element object to add to a new page.

If this array is provided, it must contain at least one element.

The expected parameters for an element object depend on the type of element being added. For the expected parameters, see the parameters for the [`addNativeElement`](https://www.canva.dev/docs/apps/api/latest/design-add-native-element/#parameters) method.

`options.title``string`

Optional

A human-readable title for the new page. It must not exceed 255 characters.

## Returns

`Promise<void>`
