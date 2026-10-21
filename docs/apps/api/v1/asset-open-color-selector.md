---
url: https://www.canva.dev/docs/apps/api/v1/asset-open-color-selector/
title: openColorSelector - v1 API reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:25.537749+00:00
---

# openColorSelector - v1 API reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/v1/asset-open-color-selector/

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

# openColorSelector

API reference for the openColorSelector method.

Copy page

**This version of the API is deprecated.** This version will soon be unsupported. You should use a stable version of the API in your app.

Opens a color selector flyout.

To learn more, see [Using color selectors](https://www.canva.dev/docs/apps/using-color-selectors/).

## Usage
    
    
    import { Rows, Swatch } from "@canva/app-ui-kit";
    
    import { openColorSelector } from "@canva/asset";
    
    import * as React from "react";
    
    import * as styles from "styles/components.css";
    
    
    
    
    export function App() {
    
      const [color, setColor] = React.useState<string>("#ff0099");
    
    
    
    
      return (
    
        <div className={styles.scrollContainer}>
    
          <Rows spacing="1u">
    
            <Swatch
    
              fill={color}
    
              onClick={async (event) => {
    
                const anchor = event.currentTarget.getBoundingClientRect();
    
                await openColorSelector(anchor, {
    
                  scopes: ["solid"],
    
                  onColorSelect: (event) => {
    
                    if (event.selection.type === "solid") {
    
                      setColor(event.selection.hexString);
    
                    }
    
                  },
    
                });
    
              }}
    
            />
    
          </Rows>
    
        </div>
    
      );
    
    }

TSX

Copy

## Parameters

`anchor``object`

Required

The dimensions and coordinates of an element on which to pin the color selector flyout.

`anchor.top``number`

Required

The top position from which to pin the color selector flyout, in pixels.

`anchor.left``number`

Required

The left position from which to pin the color selector flyout, in pixels.

`anchor.width``number`

Required

The width of the element from which to pin the color selector flyout, in pixels.

`anchor.height``number`

Required

The height of the element from which to pin the color selector flyout, in pixels.

`options``object`

Required

The options for configuring the behavior of the color selector.

`options.scopes``array`

Required

The scopes that the color selector should support. This affects the user experience.

The available scopes include:

  * `"solid"`



`selectedColor``object`

Optional

The color to display as selected when the color selector is opened.

This is only required if there are multiple selectable colors rendered within the user interface, such as multiple `Swatch` components. If this value isn't defined, the most recently selected color will be displayed as selected.

This property only affects **Document colors** and **Default colors**.

`selectedColor.type``string`

Required

The type of color. For the time being, the only valid value is `"solid"`.

`selectedColor.hexString``string`

Required

The selected color, as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol — for example, `"#ff0099"`.

`options.onColorSelect``function`

Required

A callback function that runs when a color is selected.

`options.onColorSelect(event)``object`

Required

An object that contains information about the color selection event.

`options.onColorSelect(event.selection)``object`

Required

An object that contains information about the selected color.

`options.onColorSelect(event.selection.type)``string`

Required

The type of color. For the time being, the only valid value is `"solid"`.

`options.onColorSelect(event.selection.hexString)``string`

Required

The selected color, as a hex code.

The hex code always includes all six characters and is prefixed with a `#` symbol — for example, `"#ff0099"`.

## Returns

A `Promise` that, once resolved, returns a function. When called, this function closes the color selector flyout. This function is not usually necessary, and it's better to let users close the flyout themselves.
