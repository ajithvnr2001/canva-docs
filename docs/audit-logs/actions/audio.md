---
url: https://www.canva.dev/docs/audit-logs/actions/audio/
title: Audio - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:49.418704+00:00
---

# Audio - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/audio/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Audio

Copy page

## Create an audio

An `actor` triggers this event when they create/upload an audio to their account or team.

`type``string`

**Default value:** `CREATE_AUDIO`

**Available values:** The only valid value is `CREATE_AUDIO`.

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
    
        "type": "CREATE_AUDIO",
    
        "filename": "theme.mp3"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an audio's details

An `actor` triggers this event when they update audios in their account or team.

`type``string`

**Default value:** `UPDATE_AUDIO`

**Available values:** The only valid value is `UPDATE_AUDIO`.

`old_title``string`

Optional

The old title of the audio.

`new_title``string`

Optional

The new title of the audio.

`old_tags``string[]`

Optional

Original list of tags associated with the audio.

`new_tags``string[]`

Optional

New list of tags associated with the audio.

`changed_fields``string[]`

Optional

Fields requested to be changed in this update.

**Available values:**

  * `TITLE`: The audio's title.
  * `TAGS`: The audio's tags.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_AUDIO",
    
        "old_title": "Original theme",
    
        "new_title": "New theme",
    
        "old_tags": [
    
          "theme"
    
        ],
    
        "new_tags": [
    
          "theme",
    
          "branding"
    
        ],
    
        "changed_fields": [
    
          "TITLE",
    
          "TAGS"
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete an audio

An `actor` triggers this event when they permanently delete audios from their account or team.

`type``string`

**Default value:** `DELETE_AUDIO`

**Available values:** The only valid value is `DELETE_AUDIO`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_AUDIO"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Trash an audio

An `actor` triggers this event when they move audios to the trash folder. Audios in the trash folder aren't accessible to collaborators and will be deleted after a period of time.

`type``string`

**Default value:** `TRASH_AUDIO`

**Available values:** The only valid value is `TRASH_AUDIO`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "TRASH_AUDIO"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Restore an audio from Trash

An `actor` triggers this event when they restore audios from the trash folder.

`type``string`

**Default value:** `UNDELETE_AUDIO`

**Available values:** The only valid value is `UNDELETE_AUDIO`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNDELETE_AUDIO"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Copy an audio

An `actor` triggers this event when they copy an audio.

`type``string`

**Default value:** `COPY_AUDIO`

**Available values:** The only valid value is `COPY_AUDIO`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "COPY_AUDIO"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an audio's access controls

An `actor` triggers this event when they change the rules that control access to an audio asset. There can be multiple changes in a single update.

`type``string`

**Default value:** `UPDATE_AUDIO_ACCESS_CONTROLS`

**Available values:** The only valid value is `UPDATE_AUDIO_ACCESS_CONTROLS`.

`changes``AudioAccessControlListChange[]`

A change to the rules that control the access to the audio asset.

GRANT_USER_AUDIO_ACCESSGRANT_USER_AUDIO_ACCESS

REVOKE_USER_AUDIO_ACCESSREVOKE_USER_AUDIO_ACCESS

UPDATE_USER_AUDIO_ACCESSUPDATE_USER_AUDIO_ACCESS

GRANT_GROUP_AUDIO_ACCESSGRANT_GROUP_AUDIO_ACCESS

REVOKE_GROUP_AUDIO_ACCESSREVOKE_GROUP_AUDIO_ACCESS

UPDATE_GROUP_AUDIO_ACCESSUPDATE_GROUP_AUDIO_ACCESS

GRANT_TEAM_AUDIO_ACCESSGRANT_TEAM_AUDIO_ACCESS

REVOKE_TEAM_AUDIO_ACCESSREVOKE_TEAM_AUDIO_ACCESS

UPDATE_TEAM_AUDIO_ACCESSUPDATE_TEAM_AUDIO_ACCESS

GRANT_ORGANIZATION_AUDIO_ACCESSGRANT_ORGANIZATION_AUDIO_ACCESS

REVOKE_ORGANIZATION_AUDIO_ACCESSREVOKE_ORGANIZATION_AUDIO_ACCESS

UPDATE_ORGANIZATION_AUDIO_ACCESSUPDATE_ORGANIZATION_AUDIO_ACCESS

UPDATE_AUDIO_OWNERUPDATE_AUDIO_OWNER

A user granted another user access to the audio.

`type``string`

**Default value:** `GRANT_USER_AUDIO_ACCESS`

**Available values:** The only valid value is `GRANT_USER_AUDIO_ACCESS`.

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

`access``AudioAccessLevel`

Access permissions for an audio asset.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

A user revoked another user's access to the audio.

`type``string`

**Default value:** `REVOKE_USER_AUDIO_ACCESS`

**Available values:** The only valid value is `REVOKE_USER_AUDIO_ACCESS`.

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

A user changed another user's access to the audio.

`type``string`

**Default value:** `UPDATE_USER_AUDIO_ACCESS`

**Available values:** The only valid value is `UPDATE_USER_AUDIO_ACCESS`.

`old_access``AudioAccessLevel`

Access permissions for an audio asset.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`new_access``AudioAccessLevel`

Access permissions for an audio asset.

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

A user granted a [group⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the audio.

`type``string`

**Default value:** `GRANT_GROUP_AUDIO_ACCESS`

**Available values:** The only valid value is `GRANT_GROUP_AUDIO_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`access``AudioAccessLevel`

Access permissions for an audio asset.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

A user revoked a [group's⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the audio.

`type``string`

**Default value:** `REVOKE_GROUP_AUDIO_ACCESS`

**Available values:** The only valid value is `REVOKE_GROUP_AUDIO_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

A user changed a [group's⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the audio.

`type``string`

**Default value:** `UPDATE_GROUP_AUDIO_ACCESS`

**Available values:** The only valid value is `UPDATE_GROUP_AUDIO_ACCESS`.

`old_access``AudioAccessLevel`

Access permissions for an audio asset.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`new_access``AudioAccessLevel`

Access permissions for an audio asset.

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

A user granted a [team⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the audio.

`type``string`

**Default value:** `GRANT_TEAM_AUDIO_ACCESS`

**Available values:** The only valid value is `GRANT_TEAM_AUDIO_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`access``AudioAccessLevel`

Access permissions for an audio asset.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

A user revoked a [team's⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the audio.

`type``string`

**Default value:** `REVOKE_TEAM_AUDIO_ACCESS`

**Available values:** The only valid value is `REVOKE_TEAM_AUDIO_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A user changed a [team's⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the audio.

`type``string`

**Default value:** `UPDATE_TEAM_AUDIO_ACCESS`

**Available values:** The only valid value is `UPDATE_TEAM_AUDIO_ACCESS`.

`old_access``AudioAccessLevel`

Access permissions for an audio asset.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`new_access``AudioAccessLevel`

Access permissions for an audio asset.

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

A user granted an organization access to the audio.

`type``string`

**Default value:** `GRANT_ORGANIZATION_AUDIO_ACCESS`

**Available values:** The only valid value is `GRANT_ORGANIZATION_AUDIO_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`access``AudioAccessLevel`

Access permissions for an audio asset.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

A user revoked an organization's access to the audio.

`type``string`

**Default value:** `REVOKE_ORGANIZATION_AUDIO_ACCESS`

**Available values:** The only valid value is `REVOKE_ORGANIZATION_AUDIO_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

A user changed an organization's access to the audio.

`type``string`

**Default value:** `UPDATE_ORGANIZATION_AUDIO_ACCESS`

**Available values:** The only valid value is `UPDATE_ORGANIZATION_AUDIO_ACCESS`.

`old_access``AudioAccessLevel`

Access permissions for an audio asset.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

**Default value:** `false`

`new_access``AudioAccessLevel`

Access permissions for an audio asset.

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

The owner of the audio asset was changed.

`type``string`

**Default value:** `UPDATE_AUDIO_OWNER`

**Available values:** The only valid value is `UPDATE_AUDIO_OWNER`.

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
    
        "type": "UPDATE_AUDIO_ACCESS_CONTROLS",
    
        "changes": [
    
          {
    
            "type": "GRANT_USER_AUDIO_ACCESS",
    
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
    
            "type": "REVOKE_USER_AUDIO_ACCESS",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_USER_AUDIO_ACCESS",
    
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
    
            "type": "GRANT_GROUP_AUDIO_ACCESS",
    
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
    
            "type": "REVOKE_GROUP_AUDIO_ACCESS",
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_GROUP_AUDIO_ACCESS",
    
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
    
            "type": "GRANT_TEAM_AUDIO_ACCESS",
    
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
    
            "type": "REVOKE_TEAM_AUDIO_ACCESS",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_TEAM_AUDIO_ACCESS",
    
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
    
            "type": "GRANT_ORGANIZATION_AUDIO_ACCESS",
    
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
    
            "type": "REVOKE_ORGANIZATION_AUDIO_ACCESS",
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_ORGANIZATION_AUDIO_ACCESS",
    
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
    
            "type": "UPDATE_AUDIO_OWNER",
    
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
