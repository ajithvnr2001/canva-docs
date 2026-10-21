---
url: https://www.canva.dev/docs/audit-logs/actions/folders/
title: Folders - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:51.278893+00:00
---

# Folders - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/folders/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Folders

Copy page

## Update a folder's access controls

An `actor` triggers this event when they change the rules that control access to a folder. There can be multiple changes in a single update.

`type``string`

**Default value:** `UPDATE_FOLDER_ACCESS_CONTROLS`

**Available values:** The only valid value is `UPDATE_FOLDER_ACCESS_CONTROLS`.

`access_control_changes``UpdateFolderAccessControlChange[]`

A change to the rules that control the access to the folder.

UPDATE_FOLDER_OWNERUPDATE_FOLDER_OWNER

GRANT_USER_FOLDER_ACCESSGRANT_USER_FOLDER_ACCESS

REVOKE_USER_FOLDER_ACCESSREVOKE_USER_FOLDER_ACCESS

UPDATE_USER_FOLDER_ACCESSUPDATE_USER_FOLDER_ACCESS

GRANT_GROUP_FOLDER_ACCESSGRANT_GROUP_FOLDER_ACCESS

REVOKE_GROUP_FOLDER_ACCESSREVOKE_GROUP_FOLDER_ACCESS

UPDATE_GROUP_FOLDER_ACCESSUPDATE_GROUP_FOLDER_ACCESS

GRANT_TEAM_FOLDER_ACCESSGRANT_TEAM_FOLDER_ACCESS

REVOKE_TEAM_FOLDER_ACCESSREVOKE_TEAM_FOLDER_ACCESS

UPDATE_TEAM_FOLDER_ACCESSUPDATE_TEAM_FOLDER_ACCESS

GRANT_ORGANIZATION_FOLDER_ACCESSGRANT_ORGANIZATION_FOLDER_ACCESS

REVOKE_ORGANIZATION_FOLDER_ACCESSREVOKE_ORGANIZATION_FOLDER_ACCESS

UPDATE_ORGANIZATION_FOLDER_ACCESSUPDATE_ORGANIZATION_FOLDER_ACCESS

The owner of the folder changed. For example, when a user left the team, or when the folder moved into or out of a team space. `old_owner` or `new_owner` might be omitted if the folder doesn't have a user owner. For example, when a folder is owned by a team inside a team space.

`type``string`

**Default value:** `UPDATE_FOLDER_OWNER`

**Available values:** The only valid value is `UPDATE_FOLDER_OWNER`.

`old_owner``AuditLogUser`

Optional

A Canva user.

Properties of **old_owner**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`new_owner``AuditLogUser`

Optional

A Canva user.

Properties of **new_owner**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

A user granted another user access to the folder.

`type``string`

**Default value:** `GRANT_USER_FOLDER_ACCESS`

**Available values:** The only valid value is `GRANT_USER_FOLDER_ACCESS`.

`access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`user``AuditLogUser`

A Canva user.

Properties of **user**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

A user revoked another user's access to the folder.

`type``string`

**Default value:** `REVOKE_USER_FOLDER_ACCESS`

**Available values:** The only valid value is `REVOKE_USER_FOLDER_ACCESS`.

`user``AuditLogUser`

A Canva user.

Properties of **user**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`access``FolderAccessLevel`

Optional

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

A user changed another user's access to the folder.

`type``string`

**Default value:** `UPDATE_USER_FOLDER_ACCESS`

**Available values:** The only valid value is `UPDATE_USER_FOLDER_ACCESS`.

`old_access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`new_access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`user``AuditLogUser`

A Canva user.

Properties of **user**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

A user granted a [group⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the folder.

`type``string`

**Default value:** `GRANT_GROUP_FOLDER_ACCESS`

**Available values:** The only valid value is `GRANT_GROUP_FOLDER_ACCESS`.

`access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

A user revoked a [group's⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the folder.

`type``string`

**Default value:** `REVOKE_GROUP_FOLDER_ACCESS`

**Available values:** The only valid value is `REVOKE_GROUP_FOLDER_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`access``FolderAccessLevel`

Optional

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

A user changed a [group's⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the folder.

`type``string`

**Default value:** `UPDATE_GROUP_FOLDER_ACCESS`

**Available values:** The only valid value is `UPDATE_GROUP_FOLDER_ACCESS`.

`old_access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`new_access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

A user granted a [team⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the folder.

`type``string`

**Default value:** `GRANT_TEAM_FOLDER_ACCESS`

**Available values:** The only valid value is `GRANT_TEAM_FOLDER_ACCESS`.

`access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A user revoked a [team's⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the folder.

`type``string`

**Default value:** `REVOKE_TEAM_FOLDER_ACCESS`

**Available values:** The only valid value is `REVOKE_TEAM_FOLDER_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`access``FolderAccessLevel`

Optional

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

A user changed a [team's⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the folder.

`type``string`

**Default value:** `UPDATE_TEAM_FOLDER_ACCESS`

**Available values:** The only valid value is `UPDATE_TEAM_FOLDER_ACCESS`.

`old_access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`new_access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A user granted an organization access to the folder.

`type``string`

**Default value:** `GRANT_ORGANIZATION_FOLDER_ACCESS`

**Available values:** The only valid value is `GRANT_ORGANIZATION_FOLDER_ACCESS`.

`access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

A user revoked an organization's access to the folder.

`type``string`

**Default value:** `REVOKE_ORGANIZATION_FOLDER_ACCESS`

**Available values:** The only valid value is `REVOKE_ORGANIZATION_FOLDER_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`access``FolderAccessLevel`

Optional

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

A user changed an organization's access to the folder.

`type``string`

**Default value:** `UPDATE_ORGANIZATION_FOLDER_ACCESS`

**Available values:** The only valid value is `UPDATE_ORGANIZATION_FOLDER_ACCESS`.

`old_access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`new_access``FolderAccessLevel`

Whether the folder's content can be viewed, edited, organized or managed.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`). For a folder in a team space, this only includes adding and editing content. Removing and moving content requires `organize`.

`organize``boolean`

Optional

Whether access to organize content in the folder has been provided (`true`) or denied (`false`). Only applies to folders in a team space.

`manage``boolean`

Optional

Whether access to administer the folder has been provided (`true`) or denied (`false`). Can only be granted via a team space.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_FOLDER_ACCESS_CONTROLS",
    
        "access_control_changes": [
    
          {
    
            "type": "UPDATE_FOLDER_OWNER",
    
            "old_owner": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "new_owner": {
    
              "id": "UXqwwoQDSbb",
    
              "display_name": "Ash Doe",
    
              "email": "ash.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "GRANT_USER_FOLDER_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "organize": true,
    
              "manage": true
    
            },
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "REVOKE_USER_FOLDER_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "organize": true,
    
              "manage": true
    
            },
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_USER_FOLDER_ACCESS",
    
            "old_access": {
    
              "read": true,
    
              "write": false
    
            },
    
            "new_access": {
    
              "read": true,
    
              "write": true
    
            },
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "GRANT_GROUP_FOLDER_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "organize": true,
    
              "manage": true
    
            },
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            }
    
          },
    
          {
    
            "type": "REVOKE_GROUP_FOLDER_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "organize": true,
    
              "manage": true
    
            },
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_GROUP_FOLDER_ACCESS",
    
            "old_access": {
    
              "read": true,
    
              "write": false
    
            },
    
            "new_access": {
    
              "read": true,
    
              "write": true
    
            },
    
            "group": "GADkBZ48E04"
    
          },
    
          {
    
            "type": "GRANT_TEAM_FOLDER_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "organize": true,
    
              "manage": true
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "REVOKE_TEAM_FOLDER_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "organize": true,
    
              "manage": true
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_TEAM_FOLDER_ACCESS",
    
            "old_access": {
    
              "read": true,
    
              "write": false
    
            },
    
            "new_access": {
    
              "read": true,
    
              "write": true
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "GRANT_ORGANIZATION_FOLDER_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "organize": true,
    
              "manage": true
    
            },
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "REVOKE_ORGANIZATION_FOLDER_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "organize": true,
    
              "manage": true
    
            },
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_ORGANIZATION_FOLDER_ACCESS",
    
            "old_access": {
    
              "read": true,
    
              "write": false
    
            },
    
            "new_access": {
    
              "read": true,
    
              "write": true
    
            },
    
            "organization": {
    
              "id": "OXtgecafZvh"
    
            }
    
          }
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Add an item to a folder

An `actor` triggers this event when they add an item to a folder.

`type``string`

**Default value:** `ADD_ITEM_TO_FOLDER`

**Available values:** The only valid value is `ADD_ITEM_TO_FOLDER`.

`item``FolderItem`

An item in a folder, such as a [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs). `owner` is omitted when the item is owned by a team space, as team spaces have no user owner.

Properties of **item**

`item_type``string`

The type of item.

**Available values:**

  * `FOLDER`: A folder.
  * `DESIGN`: A design.
  * `IMAGE`: An image.
  * `VIDEO`: A video.
  * `AUDIO`: An audio.
  * `TEMPLATE`: A template.
  * `FILE`: A file.



`id``string`

The item ID.

`team``AuditLogTeam`

Optional

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`owner``AuditLogUser`

Optional

A Canva user.

Properties of **owner**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`display_name``string`

Optional

The display name of the item. Rarely, it may be omitted for technical reasons.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "ADD_ITEM_TO_FOLDER",
    
        "item": {
    
          "item_type": "DESIGN",
    
          "id": "DXWEBartcNg",
    
          "team": {
    
            "id": "BXeFatjDhdR",
    
            "display_name": "Acme Team"
    
          },
    
          "owner": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          },
    
          "display_name": "My awesome design"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Remove an item from a folder

An `actor` triggers this event when they remove an item from a folder.

`type``string`

**Default value:** `REMOVE_ITEM_FROM_FOLDER`

**Available values:** The only valid value is `REMOVE_ITEM_FROM_FOLDER`.

`item``FolderItem`

An item in a folder, such as a [design](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs). `owner` is omitted when the item is owned by a team space, as team spaces have no user owner.

Properties of **item**

`item_type``string`

The type of item.

**Available values:**

  * `FOLDER`: A folder.
  * `DESIGN`: A design.
  * `IMAGE`: An image.
  * `VIDEO`: A video.
  * `AUDIO`: An audio.
  * `TEMPLATE`: A template.
  * `FILE`: A file.



`id``string`

The item ID.

`team``AuditLogTeam`

Optional

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`owner``AuditLogUser`

Optional

A Canva user.

Properties of **owner**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`display_name``string`

Optional

The display name of the item. Rarely, it may be omitted for technical reasons.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "REMOVE_ITEM_FROM_FOLDER",
    
        "item": {
    
          "item_type": "DESIGN",
    
          "id": "DXWEBartcNg",
    
          "team": {
    
            "id": "BXeFatjDhdR",
    
            "display_name": "Acme Team"
    
          },
    
          "owner": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          },
    
          "display_name": "My awesome design"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Request access to a folder

An `actor` triggers this event when they request access to a folder. This request is sent to the owner of the folder.

`type``string`

**Default value:** `REQUEST_FOLDER_ACCESS`

**Available values:** The only valid value is `REQUEST_FOLDER_ACCESS`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "REQUEST_FOLDER_ACCESS"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Grant access to a folder

An `actor` (typically the folder `owner`) triggers this event when they grant the `requester` access to their folder.

`type``string`

**Default value:** `GRANT_FOLDER_ACCESS`

**Available values:** The only valid value is `GRANT_FOLDER_ACCESS`.

`requester``AuditLogUser`

A Canva user.

Properties of **requester**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`access``string`

Optional

A user's access level for a folder.

**Available values:**

  * `VIEW`: The user can view the folder and its contents.
  * `EDIT`: The user can view and edit the folder and its contents.
  * `ADMIN`: The user can view, edit, and modify access to the folder and its contents.
  * `ORGANIZE`: The user can view, edit, and organize the folder and its contents. This access level applies only to folders in a Team Space.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "GRANT_FOLDER_ACCESS",
    
        "requester": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "access": "VIEW"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
