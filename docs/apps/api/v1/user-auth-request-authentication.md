---
url: https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/
title: auth.requestAuthentication - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:59.316675+00:00
---

# auth.requestAuthentication - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/

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

# auth.requestAuthentication

API reference for the auth.requestAuthentication method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Starts an authentication flow.

To learn more, see [Authenticating users](https://www.canva.dev/docs/apps/authenticating-users/).

## Usage
    
    
    import { auth } from "@canva/user";
    
    
    
    
    const response = await auth.requestAuthentication();
    
    
    
    
    switch (response.status) {
    
      case "COMPLETED":
    
        console.log("The authentication was successful.");
    
        break;
    
      case "ABORTED":
    
        console.log("The user exited the authentication flow.");
    
        break;
    
      case "DENIED":
    
        console.log("The user didn't have the required permissions.");
    
        break;
    
    }

TS

Copy

## Parameters

`options``object`

Optional

The options for customizing the authentication flow.

`options.context``string`

Optional

A string that's appended to the app's **Redirect URL** at the start of an authentication flow.

The value of the `context` parameter must **not** :

  * Exceed 32 characters
  * Contain sensitive information, such as user data, tokens, or secrets
  * Contain anything not strictly relevant to the authentication flow



## Returns

A `Promise` that resolves with the following object:

`result``object`

Required

The result of the authentication flow.

`result.status``string`

Required

A value that identifies if the authentication flow was successful or not.

This property may contain any of the following values:

  * `"COMPLETED"` \- The user successfully authenticated.
  * `"ABORTED"` \- The user exited the authentication flow.
  * `"DENIED"` \- The user didn't have the required permissions.



`result.details``array`

Sometimes required

An array of error codes provided by the app. The app can provide these error codes when redirecting the user back to Canva at the end of an authentication flow.
