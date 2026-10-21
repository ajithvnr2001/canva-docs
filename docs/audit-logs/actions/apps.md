---
url: https://www.canva.dev/docs/audit-logs/actions/apps/
title: Apps - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:48.848213+00:00
---

# Apps - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/apps/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Apps

Copy page

## Install an app

An `actor` triggers this event when they use a third-party app for the first time (or following app uninstall). For example, when a user selects "open" on a new app in the editor, or selects **Use in a new design** or **Use in existing design** from the apps [marketplace⁠(opens in a new tab or window)](https://www.canva.com/your-apps/). The installation is for a user in a team.

`type``string`

**Default value:** `INSTALL_APP`

**Available values:** The only valid value is `INSTALL_APP`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

`permissions``string[]`

Optional

A set of permissions.

**Available values:**

  * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `BRANDKIT_READ`: Permission to view [Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).
  * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates⁠(opens in a new tab or window)](https://www.canva.com/help/brand-templates/).



`settings``string[]`

Optional

A set of settings.

**Available values:** The only valid value is `ENABLED_FOR_CANVA_AI`: The app is available for Canva AI to use..

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "INSTALL_APP",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        },
    
        "permissions": [
    
          "DESIGN_CONTENT_READ"
    
        ],
    
        "settings": [
    
          "ENABLED_FOR_CANVA_AI"
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Uninstall an app

An `actor` triggers this event when they remove a third-party app from their list of apps.

`type``string`

**Default value:** `UNINSTALL_APP`

**Available values:** The only valid value is `UNINSTALL_APP`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNINSTALL_APP",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an app's permissions

An `actor` triggers this event when they accept updated permissions for an installed third-party app. The app's developer may have updated the permissions required by the app.

`type``string`

**Default value:** `UPDATE_APP_PERMISSIONS`

**Available values:** The only valid value is `UPDATE_APP_PERMISSIONS`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

`old_permissions``string[]`

Optional

A set of permissions.

**Available values:**

  * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `BRANDKIT_READ`: Permission to view [Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).
  * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates⁠(opens in a new tab or window)](https://www.canva.com/help/brand-templates/).



`new_permissions``string[]`

Optional

A set of permissions.

**Available values:**

  * `DESIGN_CONTENT_READ`: Permission to view [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `DESIGN_CONTENT_WRITE`: Permission to modify [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) content.
  * `ASSET_PRIVATE_READ`: Permission to view private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `ASSET_PRIVATE_WRITE`: Permission to modify private [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets).
  * `BRANDKIT_READ`: Permission to view [Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).
  * `BRAND_TEMPLATE_READ`: Permission to view [Brand Templates⁠(opens in a new tab or window)](https://www.canva.com/help/brand-templates/).



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_APP_PERMISSIONS",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        },
    
        "old_permissions": [
    
          "DESIGN_CONTENT_READ"
    
        ],
    
        "new_permissions": [
    
          "DESIGN_CONTENT_READ"
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a setting for an app

An `actor` triggers this event when they update a setting for an app.

`type``string`

**Default value:** `UPDATE_APP_SETTING`

**Available values:** The only valid value is `UPDATE_APP_SETTING`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

`setting``string`

The setting for an app.

**Available values:** The only valid value is `ENABLED_FOR_CANVA_AI`: The app is available for Canva AI to use..

`old_value``boolean`

`new_value``boolean`

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_APP_SETTING",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        },
    
        "setting": "ENABLED_FOR_CANVA_AI",
    
        "old_value": true,
    
        "new_value": true
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Disconnect from a third-party service through an app

An `actor` triggers this event when they disconnect from a third-party service from within a third-party [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps) installed in Canva. For example, a user disconnects from Google Drive in the [Google Drive App⁠(opens in a new tab or window)](https://www.canva.com/your-apps/googledrive/google-drive).

`type``string`

**Default value:** `DISCONNECT_FROM_THIRD_PARTY_APP`

**Available values:** The only valid value is `DISCONNECT_FROM_THIRD_PARTY_APP`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DISCONNECT_FROM_THIRD_PARTY_APP",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Connect to a third-party service through an app

An `actor` triggers this event when they connect to a third-party service using a third-party [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps) installed in Canva. For example, a user connects to Google Drive using the [Google Drive App⁠(opens in a new tab or window)](https://www.canva.com/your-apps/googledrive/google-drive).

`type``string`

**Default value:** `CONNECT_TO_THIRD_PARTY_APP`

**Available values:** The only valid value is `CONNECT_TO_THIRD_PARTY_APP`.

`app``AuditLogApp`

A Canva [app](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/#canva-apps).

Properties of **app**

`id``string`

The app ID.

`name``string`

Optional

The name of the app.

`version``string`

Optional

The version of the app.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CONNECT_TO_THIRD_PARTY_APP",
    
        "app": {
    
          "id": "AAEJQA10wBV",
    
          "name": "Magic App",
    
          "version": 23
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
