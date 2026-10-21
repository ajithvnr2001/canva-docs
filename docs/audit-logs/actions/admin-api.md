---
url: https://www.canva.dev/docs/audit-logs/actions/admin-api/
title: Admin API - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:49.044665+00:00
---

# Admin API - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/admin-api/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Admin API

Copy page

## Create an Admin API client

An `actor` triggers this event when they attempt to create an API client for the [Admin API](https://www.canva.dev/docs/admin/). The name and scopes are set in a subsequent update, so they are not included in this event. When the `outcome` is `DENIED`, the actor did not have permission to create the client.

`type``string`

**Default value:** `CREATE_ADMIN_API_CLIENT`

**Available values:** The only valid value is `CREATE_ADMIN_API_CLIENT`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_ADMIN_API_CLIENT"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an Admin API client

An `actor` triggers this event when they attempt to update an API client for the [Admin API](https://www.canva.dev/docs/admin/). When the `outcome` is `DENIED`, the actor did not have permission to update the client.

`type``string`

**Default value:** `UPDATE_ADMIN_API_CLIENT`

**Available values:** The only valid value is `UPDATE_ADMIN_API_CLIENT`.

`changed_fields``string[]`

Optional

The fields the `actor` requested changes for in this update.

**Available values:**

  * `NAME`: The name of the API client.
  * `SCOPES`: The scopes granted to the API client.
  * `SECRET`: The client secret was regenerated.



`old_name``string`

Optional

The previous name of the API client.

`new_name``string`

Optional

The new name of the API client.

`old_scopes``string[]`

Optional

The previous scopes granted to the API client.

`new_scopes``string[]`

Optional

The new scopes granted to the API client.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_ADMIN_API_CLIENT",
    
        "changed_fields": [
    
          "NAME",
    
          "SCOPES",
    
          "SECRET"
    
        ],
    
        "old_name": "My Integration",
    
        "new_name": "My Updated Integration",
    
        "old_scopes": [
    
          "admin:team:read"
    
        ],
    
        "new_scopes": [
    
          "admin:team:read"
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete an Admin API client

An `actor` triggers this event when they attempt to delete an API client for the [Admin API](https://www.canva.dev/docs/admin/). When the `outcome` is `DENIED`, the actor did not have permission to delete the client.

`type``string`

**Default value:** `DELETE_ADMIN_API_CLIENT`

**Available values:** The only valid value is `DELETE_ADMIN_API_CLIENT`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_ADMIN_API_CLIENT"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
