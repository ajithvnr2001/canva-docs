---
url: https://www.canva.dev/docs/audit-logs/actions/exports/
title: Exports - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:50.657958+00:00
---

# Exports - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/exports/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Exports

Copy page

## Export a design

An `actor` triggers this event when they export a design. Internal Canva systems may export the design for tasks including:

  * Creating template previews.
  * Creating design and template thumbnails.
  * Sending a design for [print⁠(opens in a new tab or window)](https://www.canva.com/print/).



[Canva Apps and Canva Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/) can also trigger the export event.

`type``string`

**Default value:** `EXPORT_DESIGN`

**Available values:** The only valid value is `EXPORT_DESIGN`.

`reason``ExportReason`

Optional

The reason the design was exported. If not specified, a user, a Canva App, or a Canva integration exported the design.

APPAPP

INTERNALINTERNAL

The design was exported by an app.

`type``string`

**Default value:** `APP`

**Available values:** The only valid value is `APP`.

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

Canva internally exported the design for tasks including creating template previews, creating design and template thumbnails, or sending a design for [print⁠(opens in a new tab or window)](https://www.canva.com/print/).

`type``string`

**Default value:** `INTERNAL`

**Available values:** The only valid value is `INTERNAL`.

`output_type``string`

Optional

The type of export.

**Available values:**

  * `PDF`
  * `JPG`
  * `PNG`
  * `PPTX`
  * `MP4`
  * `WEB`
  * `GIF`
  * `SVG`
  * `EMAIL`
  * `HTML`
  * `WEBSITE`
  * `DOCX`
  * `CSV`
  * `XLSX`
  * `WEBP`



`bulk_export_id``string`

Optional

The unique identifier for a bulk export operation. This ID will be shared across all exported resources that are part of the same bulk export operation.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "EXPORT_DESIGN",
    
        "reason": {
    
          "type": "APP",
    
          "app": {
    
            "id": "AAEJQA10wBV",
    
            "name": "Magic App",
    
            "version": 23
    
          }
    
        },
    
        "output_type": "PDF",
    
        "bulk_export_id": 6611763471969146000
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Export a user's data and content in bulk

This isn't a Data Subject Access Request (DSAR).

An `actor` triggers this event when they export personal data, uploads, and designs from the **Login & Security** settings page. A [team owner⁠(opens in a new tab or window)](https://www.canva.com/help/roles-and-permissions/) can also download their team's content. For details, see [Canva Help: Downloading your personal data, uploads, and designs in bulk⁠(opens in a new tab or window)](https://www.canva.com/help/bulk-download-data-uploads-designs/).

`type``string`

**Default value:** `EXPORT_BULK_DOWNLOAD`

**Available values:** The only valid value is `EXPORT_BULK_DOWNLOAD`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "EXPORT_BULK_DOWNLOAD"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Download a user's data and content in bulk

An `actor` triggers this event when they visit the page showing the download URL for their bulk download request. This event doesn't record whether the user downloaded the content.

These download URLs are valid for 14 days after the user made the request.

`type``string`

**Default value:** `VIEW_BULK_DOWNLOAD_LINKS`

**Available values:** The only valid value is `VIEW_BULK_DOWNLOAD_LINKS`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "VIEW_BULK_DOWNLOAD_LINKS"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
