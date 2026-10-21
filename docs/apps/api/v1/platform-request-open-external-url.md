---
url: https://www.canva.dev/docs/apps/api/v1/platform-request-open-external-url/
title: requestOpenExternalUrl - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:34.864478+00:00
---

# requestOpenExternalUrl - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/platform-request-open-external-url/

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

# requestOpenExternalUrl

API reference for the requestOpenExternalUrl method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Opens a dialog that asks the user if they want to navigate to the provided URL. If they agree, the URL is opened in a new browser tab on desktop devices or in a browser sheet on mobile devices.

The user may need to enable pop-up permissions before URLs can be opened.

## Usage
    
    
    import { Link } from "@canva/app-ui-kit";
    
    import { requestOpenExternalUrl } from "@canva/platform";
    
    
    
    
    const EXTERNAL_URL = "https://www.example.com";
    
    
    
    
    export function App() {
    
      async function handleClick() {
    
        const response = await requestOpenExternalUrl({
    
          url: EXTERNAL_URL,
    
        });
    
    
    
    
        console.log(response); // => { status: "COMPLETED" }
    
      }
    
    
    
    
      return (
    
        <div>
    
          <Link
    
            href={EXTERNAL_URL}
    
            requestOpenExternalUrl={handleClick}
    
            ariaLabel="Navigate to example.com"
    
          >
    
            Click me
    
          </Link>
    
        </div>
    
      );
    
    }

TSX

Copy

## Parameters

`options``object`

Required

The options for opening an external URL.

`options.url``string`

Required

The URL of a web page.

## Returns

A `Promise` that resolves with the following object:

`response``object`

Required

The response of the app requesting to open an external URL.

`response.status``string`

Required

A value that identifies if the user navigated away from Canva.

This property may contain one of the following values:

  * `"COMPLETED"` \- The value when a user navigated away from Canva.
  * `"ABORTED"` \- The value when a user did not navigate away from Canva.


