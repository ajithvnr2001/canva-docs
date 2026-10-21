---
url: https://www.canva.dev/docs/audit-logs/actions/content/
title: Content - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:50.556115+00:00
---

# Content - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/content/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Content

Copy page

## Transfer ownership of user content within a team

An `actor` triggers this event when they change the owner of a user's content (such as [designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)) to another user on their Team. For details transferring content ownership, see [Canva Help: Transfer Designs⁠(opens in a new tab or window)](https://www.canva.com/help/transfer-designs/).

`type``string`

**Default value:** `INITIATE_OWNERSHIP_TRANSFER`

**Available values:** The only valid value is `INITIATE_OWNERSHIP_TRANSFER`.

`new_owner``AuditLogUser`

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
    
        "type": "INITIATE_OWNERSHIP_TRANSFER",
    
        "new_owner": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Copy assets, folders, or designs

An `actor` triggers this event when they make a copy of:

  * One or more [folders](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#folders) either within a team, or to another team.
  * One or more [designs](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs) or [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets) to another team. This event is sent to the `actor`'s team, not the destination team. For details on copying content between teams or accounts, see [Canva Help: Copy designs or files to another team or account⁠(opens in a new tab or window)](https://www.canva.com/help/transfer-designs-to-personal-account/).



`type``string`

**Default value:** `INITIATE_CONTENT_COPY`

**Available values:** The only valid value is `INITIATE_CONTENT_COPY`.

`destination_team``AuditLogTeam`

A Canva team.

Properties of **destination_team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`reason``ContentCopyReason`

Optional

The reason for the content copy operation.

Content copied from one user account to another.

`type``string`

**Default value:** `CROSS_ACCOUNT_COPY`

**Available values:** The only valid value is `CROSS_ACCOUNT_COPY`.

`source_user``AuditLogUser`

Optional

A Canva user.

Properties of **source_user**

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

`destination_user``AuditLogUser`

Optional

A Canva user.

Properties of **destination_user**

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

`content_copy_id``string`

Optional

A unique identifier for a content copy event. This ID matches the `content_copy_id` for the corresponding `RECEIVE_CONTENT_COPY` event.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "INITIATE_CONTENT_COPY",
    
        "destination_team": {
    
          "id": "BXeFatjDhdR",
    
          "display_name": "Acme Team"
    
        },
    
        "reason": {
    
          "type": "CROSS_ACCOUNT_COPY",
    
          "source_user": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          },
    
          "destination_user": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          }
    
        },
    
        "content_copy_id": "00000000-0000-0000-0000-000000000000"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Receive a copy of assets, folders, or designs

A team receives this event when they receive content from another team, or content is copied within the team, as the result of a `INITIATE_CONTENT_COPY` event. This event is sent to the team receiving the content, not the `actor`'s team. For details on copying content between teams or accounts, see [Canva Help: Copy designs or files to another team or account⁠(opens in a new tab or window)](https://www.canva.com/help/transfer-designs-to-personal-account/).

`type``string`

**Default value:** `RECEIVE_CONTENT_COPY`

**Available values:** The only valid value is `RECEIVE_CONTENT_COPY`.

`source_team``AuditLogTeam`

A Canva team.

Properties of **source_team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`reason``ContentCopyReason`

Optional

The reason for the content copy operation.

Content copied from one user account to another.

`type``string`

**Default value:** `CROSS_ACCOUNT_COPY`

**Available values:** The only valid value is `CROSS_ACCOUNT_COPY`.

`source_user``AuditLogUser`

Optional

A Canva user.

Properties of **source_user**

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

`destination_user``AuditLogUser`

Optional

A Canva user.

Properties of **destination_user**

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

`content_copy_id``string`

Optional

A unique identifier for a content copy event. This ID matches the `content_copy_id` for the corresponding `INITIATE_CONTENT_COPY` event. If a user retries a failed copy event, multiple `RECEIVE_CONTENT_COPY` events with the same `content_copy_id` will exist.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "RECEIVE_CONTENT_COPY",
    
        "source_team": {
    
          "id": "BXeFatjDhdR",
    
          "display_name": "Acme Team"
    
        },
    
        "reason": {
    
          "type": "CROSS_ACCOUNT_COPY",
    
          "source_user": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          },
    
          "destination_user": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          }
    
        },
    
        "content_copy_id": "00000000-0000-0000-0000-000000000000"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
