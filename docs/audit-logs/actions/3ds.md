---
url: https://www.canva.dev/docs/audit-logs/actions/3ds/
title: 3Ds - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:48.578516+00:00
---

# 3Ds - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/3ds/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# 3Ds

Copy page

## Create a 3D

An `actor` triggers this event when they create/upload a 3D to their account or team.

`type``string`

**Default value:** `CREATE_3D`

**Available values:** The only valid value is `CREATE_3D`.

`filename``string`

Optional

The name of the uploaded file.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_3D",
    
        "filename": "theme.glb"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete a 3D

An `actor` triggers this event when they permanently delete 3Ds from their account or team.

`type``string`

**Default value:** `DELETE_3D`

**Available values:** The only valid value is `DELETE_3D`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_3D"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Trash a 3D

An `actor` triggers this event when they move a 3D to the trash folder. 3Ds in the trash folder aren't accessible to collaborators and will be deleted after a period of time.

`type``string`

**Default value:** `TRASH_3D`

**Available values:** The only valid value is `TRASH_3D`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "TRASH_3D"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Restore a 3D from Trash

An `actor` triggers this event when they restore a 3D from the trash folder.

`type``string`

**Default value:** `UNTRASH_3D`

**Available values:** The only valid value is `UNTRASH_3D`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNTRASH_3D"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a 3D's access controls

An `actor` triggers this event when they change the rules that control access to a 3D asset. There can be multiple changes in a single update.

`type``string`

**Default value:** `UPDATE_3D_ACCESS_CONTROLS`

**Available values:** The only valid value is `UPDATE_3D_ACCESS_CONTROLS`.

`changes``AccessControlListChange3D[]`

A change to the rules that control the access to the 3D asset.

GRANT_USER_3D_ACCESSGRANT_USER_3D_ACCESS

REVOKE_USER_3D_ACCESSREVOKE_USER_3D_ACCESS

UPDATE_USER_3D_ACCESSUPDATE_USER_3D_ACCESS

GRANT_GROUP_3D_ACCESSGRANT_GROUP_3D_ACCESS

REVOKE_GROUP_3D_ACCESSREVOKE_GROUP_3D_ACCESS

UPDATE_GROUP_3D_ACCESSUPDATE_GROUP_3D_ACCESS

GRANT_TEAM_3D_ACCESSGRANT_TEAM_3D_ACCESS

REVOKE_TEAM_3D_ACCESSREVOKE_TEAM_3D_ACCESS

UPDATE_TEAM_3D_ACCESSUPDATE_TEAM_3D_ACCESS

GRANT_ORGANIZATION_3D_ACCESSGRANT_ORGANIZATION_3D_ACCESS

REVOKE_ORGANIZATION_3D_ACCESSREVOKE_ORGANIZATION_3D_ACCESS

UPDATE_ORGANIZATION_3D_ACCESSUPDATE_ORGANIZATION_3D_ACCESS

UPDATE_3D_OWNERUPDATE_3D_OWNER

A user granted another user access to the 3D.

`type``string`

**Default value:** `GRANT_USER_3D_ACCESS`

**Available values:** The only valid value is `GRANT_USER_3D_ACCESS`.

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

`access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

A user revoked another user's access to the 3D.

`type``string`

**Default value:** `REVOKE_USER_3D_ACCESS`

**Available values:** The only valid value is `REVOKE_USER_3D_ACCESS`.

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

A user changed another user's access to the 3D.

`type``string`

**Default value:** `UPDATE_USER_3D_ACCESS`

**Available values:** The only valid value is `UPDATE_USER_3D_ACCESS`.

`old_access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`new_access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

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

A user granted a [group⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the 3D.

`type``string`

**Default value:** `GRANT_GROUP_3D_ACCESS`

**Available values:** The only valid value is `GRANT_GROUP_3D_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

A user revoked a [group's⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the 3D.

`type``string`

**Default value:** `REVOKE_GROUP_3D_ACCESS`

**Available values:** The only valid value is `REVOKE_GROUP_3D_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

A user changed a [group's⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the 3D.

`type``string`

**Default value:** `UPDATE_GROUP_3D_ACCESS`

**Available values:** The only valid value is `UPDATE_GROUP_3D_ACCESS`.

`old_access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`new_access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

A user granted a [team⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the 3D.

`type``string`

**Default value:** `GRANT_TEAM_3D_ACCESS`

**Available values:** The only valid value is `GRANT_TEAM_3D_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

A user revoked a [team's⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the 3D.

`type``string`

**Default value:** `REVOKE_TEAM_3D_ACCESS`

**Available values:** The only valid value is `REVOKE_TEAM_3D_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A user changed a [team's⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the 3D.

`type``string`

**Default value:** `UPDATE_TEAM_3D_ACCESS`

**Available values:** The only valid value is `UPDATE_TEAM_3D_ACCESS`.

`old_access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`new_access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A user granted an organization access to the 3D.

`type``string`

**Default value:** `GRANT_ORGANIZATION_3D_ACCESS`

**Available values:** The only valid value is `GRANT_ORGANIZATION_3D_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

A user revoked an organization's access to the 3D.

`type``string`

**Default value:** `REVOKE_ORGANIZATION_3D_ACCESS`

**Available values:** The only valid value is `REVOKE_ORGANIZATION_3D_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

A user changed an organization's access to the 3D.

`type``string`

**Default value:** `UPDATE_ORGANIZATION_3D_ACCESS`

**Available values:** The only valid value is `UPDATE_ORGANIZATION_3D_ACCESS`.

`old_access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`new_access``AccessLevel3D`

Access permissions for a 3D asset.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

The owner of the 3D asset was changed.

`type``string`

**Default value:** `UPDATE_3D_OWNER`

**Available values:** The only valid value is `UPDATE_3D_OWNER`.

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

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_3D_ACCESS_CONTROLS",
    
        "changes": [
    
          {
    
            "type": "GRANT_USER_3D_ACCESS",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "access": {
    
              "read": false,
    
              "write": false
    
            }
    
          },
    
          {
    
            "type": "REVOKE_USER_3D_ACCESS",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_USER_3D_ACCESS",
    
            "old_access": {
    
              "read": false,
    
              "write": false
    
            },
    
            "new_access": {
    
              "read": false,
    
              "write": false
    
            },
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "GRANT_GROUP_3D_ACCESS",
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            },
    
            "access": {
    
              "read": false,
    
              "write": false
    
            }
    
          },
    
          {
    
            "type": "REVOKE_GROUP_3D_ACCESS",
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_GROUP_3D_ACCESS",
    
            "old_access": {
    
              "read": false,
    
              "write": false
    
            },
    
            "new_access": {
    
              "read": false,
    
              "write": false
    
            },
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            }
    
          },
    
          {
    
            "type": "GRANT_TEAM_3D_ACCESS",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            },
    
            "access": {
    
              "read": false,
    
              "write": false
    
            }
    
          },
    
          {
    
            "type": "REVOKE_TEAM_3D_ACCESS",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_TEAM_3D_ACCESS",
    
            "old_access": {
    
              "read": false,
    
              "write": false
    
            },
    
            "new_access": {
    
              "read": false,
    
              "write": false
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "GRANT_ORGANIZATION_3D_ACCESS",
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            },
    
            "access": {
    
              "read": false,
    
              "write": false
    
            }
    
          },
    
          {
    
            "type": "REVOKE_ORGANIZATION_3D_ACCESS",
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_ORGANIZATION_3D_ACCESS",
    
            "old_access": {
    
              "read": false,
    
              "write": false
    
            },
    
            "new_access": {
    
              "read": false,
    
              "write": false
    
            },
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_3D_OWNER",
    
            "old_owner": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "new_owner": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          }
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
