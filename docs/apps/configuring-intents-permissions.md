---
url: https://www.canva.dev/docs/apps/configuring-intents-permissions/
title: Permissions - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:29.059480+00:00
---

# Permissions - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/configuring-intents-permissions/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

API reference

[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)

App UI Kit reference

[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

Canva REST API reference

[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)

Webhooks notification reference

[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

Tools

[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)

# Permissions

How to manage an app's permissions.

Copy page

At Canva, the privacy of our users is a top priority, but there are many valid reasons for apps to have access to their data. To balance these concerns, the Canva Developers SDK has a permissions system that lets developers access user data while ensuring that users remain informed and in control of what data is accessed.

## How permissions work

In the Developers SDK, some methods have an associated _permission_. If an app uses one of these methods, the permission must be enabled with either the Developer Portal or the Canva CLI. If the permission isn't enabled, the app can't be approved for release.

By requiring apps to enable permissions, Canva can inform users of what data the app will have access to — and what the app can do with that data — before the user installs it.

## The user experience

Before a user installs an app, they're shown a screen that explains what the app is and what permissions are required to install it. If an app doesn't require any permissions, no requirements are listed.

![](https://www.canva.dev/_next/static/media/app-install.43f31c2a.png)

If the user doesn't accept the app's permissions, the app can't be installed.

If a user uninstalls an app, all permissions are revoked.

## What permissions are required?

The permissions required by an app depend on the methods called by the app. For the complete list of permissions, along with the methods associated with those permissions, see [List of permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/#list-of-permissions).

## How to configure permissions

You can configure permissions for your app with either the Developer Portal or the Canva CLI:

Developer PortalDeveloper Portal

Canva CLICanva CLI

  1. Navigate to an app via the [Your apps⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) page.

  2. Go to **Inside Canva > Permissions**, and enable the required permissions.

Each permission is prefixed with `canva:`. Don't confuse them with the **Scopes** section on **Outside Canva > Configuration**, which holds the unprefixed scopes for the Canva REST APIs.

**Permissions** appears under **Inside Canva** once the app has at least one intent.




  1. Set up your app to use the Canva CLI to manage settings via the [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/#manage-configuration-using-the-canva-cli) file.

  2. Add the required permissions to the `runtime.permissions` property. For more information, see [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/#runtime-required).

For example, the following adds the **Design read** and **Design write** permissions.
         
         {
         
           "runtime": {
         
             "permissions": [
         
               {
         
                 "name": "canva:design:content:read",
         
                 "type": "mandatory"
         
               },
         
               {
         
                 "name": "canva:design:content:write",
         
                 "type": "mandatory"
         
               }
         
             ]
         
           }
         
         }

JSON

Copy




## List of permissions

This section lists the permissions that can be enabled for an app, including the methods that require the permission to be enabled. The required permissions are also listed on the API reference pages for each method.

### `canva:design:content:read`

The app may read the content of the user's design.

The following methods require this permission to be enabled:

  * [`editContent`](https://www.canva.dev/docs/apps/api/latest/design-edit-content/)
  * [`getCurrentPageContext`](https://www.canva.dev/docs/apps/api/latest/design-get-current-page-context/)
  * [`getCurrentPageMetadata`](https://www.canva.dev/docs/apps/api/latest/design-get-current-page-metadata/)
  * [`getDesignColors`](https://www.canva.dev/docs/apps/api/latest/design-get-design-colors/)
  * [`getDesignMetadata`](https://www.canva.dev/docs/apps/api/latest/design-get-design-metadata/)
  * [`initAppElement`](https://www.canva.dev/docs/apps/api/latest/design-init-app-element/), if the app calls the `registerOnElementChange` method
  * [`openColorSelector`](https://www.canva.dev/docs/apps/api/latest/asset-open-color-selector/)
  * [`openDesign`](https://www.canva.dev/docs/apps/api/latest/design-open-design/)
  * [`requestExport`](https://www.canva.dev/docs/apps/api/latest/design-request-export/)
  * [`selection.registerOnChange`](https://www.canva.dev/docs/apps/api/latest/design-selection-register-on-change/), if the app calls the `read` method



### `canva:design:content:write`

The app may modify the content of the user's design.

The following methods require this permission to be enabled:

  * [`addAudioTrack`](https://www.canva.dev/docs/apps/api/latest/design-add-audio-track/)
  * [`addElementAtCursor`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-cursor/)
  * [`addElementAtPoint`](https://www.canva.dev/docs/apps/api/latest/design-add-element-at-point/)
  * [`addNativeElement`](https://www.canva.dev/docs/apps/api/latest/design-add-native-element/)
  * [`addPage`](https://www.canva.dev/docs/apps/api/latest/design-add-page/)
  * [`editContent`](https://www.canva.dev/docs/apps/api/latest/design-edit-content/), if the app calls the `sync` method
  * [`initAppElement`](https://www.canva.dev/docs/apps/api/latest/design-init-app-element/), if the app calls the `addElement`, `addOrUpdateElement`, or `update` methods
  * [`openDesign`](https://www.canva.dev/docs/apps/api/latest/design-open-design/), if the app calls the `sync` method
  * [`selection.registerOnChange`](https://www.canva.dev/docs/apps/api/latest/design-selection-register-on-change/), if the app calls the `save` method
  * [`setCurrentPageBackground`](https://www.canva.dev/docs/apps/api/latest/design-set-current-page-background/)
  * [`ui.startDrag`](https://www.canva.dev/docs/apps/api/latest/design-ui-start-drag/)
  * [`ui.startDragToCursor`](https://www.canva.dev/docs/apps/api/latest/design-ui-start-drag-to-cursor/)
  * [`ui.startDragToPoint`](https://www.canva.dev/docs/apps/api/latest/design-ui-start-drag-to-point/)



### `canva:asset:private:read`

The app may download assets from the user's media library.

The following methods require this permission to be enabled:

  * [`getTemporaryUrl`](https://www.canva.dev/docs/apps/api/latest/asset-get-temporary-url/)



### `canva:asset:private:write`

The app may upload assets to the user's media library.

The following methods require this permission to be enabled:

  * [`upload`](https://www.canva.dev/docs/apps/api/latest/asset-upload/)



### `canva:brandkit:read`

The app may read data from brand kits that the user can access.

The following methods require this permission to be enabled:

  * [`getBrandKitColors`](https://www.canva.dev/docs/apps/api/latest/design-get-brand-kit-colors/)
  * [`openColorSelector`](https://www.canva.dev/docs/apps/api/latest/asset-open-color-selector/)



### `canva:brandtemplate:read`

The app may read metadata and contents from brand templates that the user can access.

The following methods require this permission to be enabled:

  * [`getDesignTemplateMetadata`](https://www.canva.dev/docs/apps/api/latest/design-get-design-template-metadata/)


