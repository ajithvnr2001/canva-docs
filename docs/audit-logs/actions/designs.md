---
url: https://www.canva.dev/docs/audit-logs/actions/designs/
title: Designs - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:52.092996+00:00
---

# Designs - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/designs/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Designs

Copy page

## Copy a design

An `actor` triggers this event when they make a copy of an existing design.

`type``string`

**Default value:** `COPY_DESIGN`

**Available values:** The only valid value is `COPY_DESIGN`.

`original_design_id``string`

The ID of the original design.

`title``string`

Optional

Title of the new design.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "COPY_DESIGN",
    
        "title": "My awesome design",
    
        "original_design_id": "DAGKs37VOUl"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## View a design

An `actor` triggers this event when they view a design. Actors viewing a publicly shared design without logging in are recorded as `ANONYMOUS`.

`type``string`

**Default value:** `VIEW_DESIGN`

**Available values:** The only valid value is `VIEW_DESIGN`.

`view_type``string`

Optional

The activity type for viewing a design.

**Available values:**

  * `VIEW_IN_EDITOR`: Viewed in the editor.
  * `VIEW_IN_VIEWER`: Viewed in the viewer.



`design_type``string`

Optional

The type of design, such as "Presentation (16:9)", "Document", or "Instagram Post (Square)".

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "VIEW_DESIGN",
    
        "view_type": "VIEW_IN_EDITOR",
    
        "design_type": "Presentation (16:9)"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## View a design from a share link

An `actor` triggers this event when they open a design from a share link, and gain access to that design.

`type``string`

**Default value:** `ACCEPT_DESIGN_SHARE`

**Available values:** The only valid value is `ACCEPT_DESIGN_SHARE`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "ACCEPT_DESIGN_SHARE"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Import a file to create a new design

An `actor` triggers this event when they import a file into Canva to create a new design. This includes uploaded presentations and PDFs, and doesn't include Canva design [assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#assets), such as images and videos.

`type``string`

**Default value:** `IMPORT_DESIGN`

**Available values:** The only valid value is `IMPORT_DESIGN`.

`title``string`

Optional

The title of the imported design.

`file_type``string`

Optional

The file type of the imported file, such as:

  * `PPTX` for a Microsoft PowerPoint presentations.
  * `PDF` for Portable Document Format files.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "IMPORT_DESIGN",
    
        "title": "My awesome design",
    
        "file_type": "PPTX"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Create a design

An `actor` triggers this event when they create a new [design in Canva](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/#designs). This includes when a user creates a design from a template, or using a [Canva App or Canva Integration](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/).

`type``string`

**Default value:** `CREATE_DESIGN`

**Available values:** The only valid value is `CREATE_DESIGN`.

`title``string`

Optional

Title of the new design.

`design_type``string`

Optional

The type of design, such as "Presentation (16:9)", "Document", or "Instagram Post (Square)".

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_DESIGN",
    
        "title": "My awesome design",
    
        "design_type": "Presentation (16:9)"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Trash a design

An `actor` triggers this event when they move a design to the trash folder. Designs in the trash folder aren't accessible to collaborators and will be deleted after a period of time. For details, see: [Deleting designs⁠(opens in a new tab or window)](https://www.canva.com/help/delete-designs/).

`type``string`

**Default value:** `TRASH_DESIGN`

**Available values:** The only valid value is `TRASH_DESIGN`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "TRASH_DESIGN"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Restore a design from Trash

An `actor` triggers this event when they restore a design from the trash folder. For details, see: [Restoring or deleting designs or files from your Trash⁠(opens in a new tab or window)](https://www.canva.com/help/deleted-designs/).

`type``string`

**Default value:** `UNTRASH_DESIGN`

**Available values:** The only valid value is `UNTRASH_DESIGN`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNTRASH_DESIGN"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete a design from Trash

An `actor` triggers this event when they permanently delete a design from the trash folder. Deleting a user's account will also delete all the designs in their trash folder.

`type``string`

**Default value:** `DELETE_DESIGN`

**Available values:** The only valid value is `DELETE_DESIGN`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_DESIGN"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Restore a deleted design

An `actor` triggers this event when they restore a recently deleted design. For example, when restoring a deleted user or [team account⁠(opens in a new tab or window)](https://www.canva.com/help/recover-designs-deleted-team/), the designs deleted with the account will also be restored.

`type``string`

**Default value:** `UNDELETE_DESIGN`

**Available values:** The only valid value is `UNDELETE_DESIGN`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNDELETE_DESIGN"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a design's access controls

An `actor` triggers this event when they change the rules that control access to a design. There can be multiple changes in a single update.

`type``string`

**Default value:** `UPDATE_DESIGN_ACCESS_CONTROLS`

**Available values:** The only valid value is `UPDATE_DESIGN_ACCESS_CONTROLS`.

`changes``UpdateDesignAccessControlChange[]`

A change to the rules that control the access to the design.

CREATE_DESIGN_ACCESS_TOKENCREATE_DESIGN_ACCESS_TOKEN

DELETE_DESIGN_ACCESS_TOKENDELETE_DESIGN_ACCESS_TOKEN

CREATE_DESIGN_ACCESS_INVITECREATE_DESIGN_ACCESS_INVITE

REDEEM_DESIGN_ACCESS_INVITEREDEEM_DESIGN_ACCESS_INVITE

DELETE_DESIGN_ACCESS_INVITEDELETE_DESIGN_ACCESS_INVITE

UPDATE_DESIGN_OWNERUPDATE_DESIGN_OWNER

CREATE_DESIGN_ACCESS_RESTRICTIONCREATE_DESIGN_ACCESS_RESTRICTION

DELETE_DESIGN_ACCESS_RESTRICTIONDELETE_DESIGN_ACCESS_RESTRICTION

GRANT_USER_DESIGN_ACCESSGRANT_USER_DESIGN_ACCESS

REVOKE_USER_DESIGN_ACCESSREVOKE_USER_DESIGN_ACCESS

UPDATE_USER_DESIGN_ACCESSUPDATE_USER_DESIGN_ACCESS

GRANT_GROUP_DESIGN_ACCESSGRANT_GROUP_DESIGN_ACCESS

REVOKE_GROUP_DESIGN_ACCESSREVOKE_GROUP_DESIGN_ACCESS

UPDATE_GROUP_DESIGN_ACCESSUPDATE_GROUP_DESIGN_ACCESS

GRANT_TEAM_DESIGN_ACCESSGRANT_TEAM_DESIGN_ACCESS

REVOKE_TEAM_DESIGN_ACCESSREVOKE_TEAM_DESIGN_ACCESS

UPDATE_TEAM_DESIGN_ACCESSUPDATE_TEAM_DESIGN_ACCESS

GRANT_ORGANIZATION_DESIGN_ACCESSGRANT_ORGANIZATION_DESIGN_ACCESS

REVOKE_ORGANIZATION_DESIGN_ACCESSREVOKE_ORGANIZATION_DESIGN_ACCESS

UPDATE_ORGANIZATION_DESIGN_ACCESSUPDATE_ORGANIZATION_DESIGN_ACCESS

GRANT_DESIGN_LINK_ACCESSGRANT_DESIGN_LINK_ACCESS

REVOKE_DESIGN_LINK_ACCESSREVOKE_DESIGN_LINK_ACCESS

UPDATE_DESIGN_LINK_ACCESSUPDATE_DESIGN_LINK_ACCESS

A user created an access token that allows the design to be publicly accessible. Examples include creating:

  * [A Public view link⁠(opens in a new tab or window)](https://www.canva.com/help/sharing-your-design-as-a-public-view-link/).
  * [An embed of a design⁠(opens in a new tab or window)](https://www.canva.com/help/embed-designs/).
  * [A Canva Website⁠(opens in a new tab or window)](https://www.canva.com/help/canva-websites/).



`type``string`

**Default value:** `CREATE_DESIGN_ACCESS_TOKEN`

**Available values:** The only valid value is `CREATE_DESIGN_ACCESS_TOKEN`.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`token_prefix``string`

Optional

The prefix of the access token for the design.

A user removed an access token that allows the design to be publicly accessible, such as deleting a [Public view link⁠(opens in a new tab or window)](https://www.canva.com/en_au/help/sharing-your-design-as-a-public-view-link/).

`type``string`

**Default value:** `DELETE_DESIGN_ACCESS_TOKEN`

**Available values:** The only valid value is `DELETE_DESIGN_ACCESS_TOKEN`.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`token_prefix``string`

Optional

The prefix of the access token for the design.

A user sent an invitation to access the design.

`type``string`

**Default value:** `CREATE_DESIGN_ACCESS_INVITE`

**Available values:** The only valid value is `CREATE_DESIGN_ACCESS_INVITE`.

`recipient``string`

The recipient of the invitation. This property contains the address used to share the design, such as the recipient's email address, Slack ID, or mobile number.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`token_prefix``string`

Optional

The prefix of the single-use invite token for the design.

A user exchanged the invitation to access the design.

`type``string`

**Default value:** `REDEEM_DESIGN_ACCESS_INVITE`

**Available values:** The only valid value is `REDEEM_DESIGN_ACCESS_INVITE`.

`recipient``string`

The recipient of the invitation. This property contains the address used to share the design, such as the recipient's email address, Slack ID, or mobile number.

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

`token_prefix``string`

Optional

The prefix of the single-use invite token for the design.

A user removed the invitation to access the design.

`type``string`

**Default value:** `DELETE_DESIGN_ACCESS_INVITE`

**Available values:** The only valid value is `DELETE_DESIGN_ACCESS_INVITE`.

`recipient``string`

The recipient of the invitation. This property contains the address used to share the design, such as the recipient's email address, Slack ID, or mobile number.

`token_prefix``string`

Optional

The prefix of the single-use invite token for the design.

The owner of the design changed when a user left the team.

`type``string`

**Default value:** `UPDATE_DESIGN_OWNER`

**Available values:** The only valid value is `UPDATE_DESIGN_OWNER`.

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

A user restricted access to the design.

`type``string`

**Default value:** `CREATE_DESIGN_ACCESS_RESTRICTION`

**Available values:** The only valid value is `CREATE_DESIGN_ACCESS_RESTRICTION`.

A user removed an access restriction on the design.

`type``string`

**Default value:** `DELETE_DESIGN_ACCESS_RESTRICTION`

**Available values:** The only valid value is `DELETE_DESIGN_ACCESS_RESTRICTION`.

A user granted another user access to the design.

`type``string`

**Default value:** `GRANT_USER_DESIGN_ACCESS`

**Available values:** The only valid value is `GRANT_USER_DESIGN_ACCESS`.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

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

A user revoked another user's access to the design.

`type``string`

**Default value:** `REVOKE_USER_DESIGN_ACCESS`

**Available values:** The only valid value is `REVOKE_USER_DESIGN_ACCESS`.

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

`access``DesignAccessLevel`

Optional

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

A user changed another user's access to the design.

`type``string`

**Default value:** `UPDATE_USER_DESIGN_ACCESS`

**Available values:** The only valid value is `UPDATE_USER_DESIGN_ACCESS`.

`old_access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`new_access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

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

A user granted a [group⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the design.

`type``string`

**Default value:** `GRANT_GROUP_DESIGN_ACCESS`

**Available values:** The only valid value is `GRANT_GROUP_DESIGN_ACCESS`.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

A user removed a [group's⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the design.

`type``string`

**Default value:** `REVOKE_GROUP_DESIGN_ACCESS`

**Available values:** The only valid value is `REVOKE_GROUP_DESIGN_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`access``DesignAccessLevel`

Optional

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

A user changed a [group's⁠(opens in a new tab or window)](https://www.canva.com/help/groups/) access to the design.

`type``string`

**Default value:** `UPDATE_GROUP_DESIGN_ACCESS`

**Available values:** The only valid value is `UPDATE_GROUP_DESIGN_ACCESS`.

`old_access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`new_access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

A user granted a [team⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the design.

`type``string`

**Default value:** `GRANT_TEAM_DESIGN_ACCESS`

**Available values:** The only valid value is `GRANT_TEAM_DESIGN_ACCESS`.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A user removed a [team's⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the design.

`type``string`

**Default value:** `REVOKE_TEAM_DESIGN_ACCESS`

**Available values:** The only valid value is `REVOKE_TEAM_DESIGN_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`access``DesignAccessLevel`

Optional

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

A user changed a [team's⁠(opens in a new tab or window)](https://www.canva.com/help/create-teams/) access to the design.

`type``string`

**Default value:** `UPDATE_TEAM_DESIGN_ACCESS`

**Available values:** The only valid value is `UPDATE_TEAM_DESIGN_ACCESS`.

`old_access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`new_access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A user granted an organization access to the design.

`type``string`

**Default value:** `GRANT_ORGANIZATION_DESIGN_ACCESS`

**Available values:** The only valid value is `GRANT_ORGANIZATION_DESIGN_ACCESS`.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

A user revoked an organization's access to the design.

`type``string`

**Default value:** `REVOKE_ORGANIZATION_DESIGN_ACCESS`

**Available values:** The only valid value is `REVOKE_ORGANIZATION_DESIGN_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`access``DesignAccessLevel`

Optional

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

A user changed an organization's access to the design.

`type``string`

**Default value:** `UPDATE_ORGANIZATION_DESIGN_ACCESS`

**Available values:** The only valid value is `UPDATE_ORGANIZATION_DESIGN_ACCESS`.

`old_access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **old_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`new_access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **new_access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

A user created a [collaboration link⁠(opens in a new tab or window)](https://www.canva.com/help/share-via-link-or-email/) for the design.

`type``string`

**Default value:** `GRANT_DESIGN_LINK_ACCESS`

**Available values:** The only valid value is `GRANT_DESIGN_LINK_ACCESS`.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`owning_team_only``boolean`

Optional

Only users in the same team as the design's owner can access the design.

If `owning_team_only` is `false`, anyone with the link can access the design.

A user revoked a [collaboration link⁠(opens in a new tab or window)](https://www.canva.com/help/share-via-link-or-email/) for the design.

`type``string`

**Default value:** `REVOKE_DESIGN_LINK_ACCESS`

**Available values:** The only valid value is `REVOKE_DESIGN_LINK_ACCESS`.

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`owning_team_only``boolean`

Optional

Only users in the same team as the design's owner can access the design.

If `owning_team_only` is `false`, anyone with the link can access the design.

A user changed a [collaboration link⁠(opens in a new tab or window)](https://www.canva.com/help/share-via-link-or-email/) for the design.

`type``string`

**Default value:** `UPDATE_DESIGN_LINK_ACCESS`

**Available values:** The only valid value is `UPDATE_DESIGN_LINK_ACCESS`.

`old_link_role``DesignLinkRole`

How the design may be accessed using a [collaboration link⁠(opens in a new tab or window)](https://www.canva.com/help/share-via-link-or-email/).

Properties of **old_link_role**

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`owning_team_only``boolean`

Optional

Only users in the same team as the design's owner can access the design.

If `owning_team_only` is `false`, anyone with the link can access the design.

`new_link_role``DesignLinkRole`

How the design may be accessed using a [collaboration link⁠(opens in a new tab or window)](https://www.canva.com/help/share-via-link-or-email/).

Properties of **new_link_role**

`access``DesignAccessLevel`

Whether the design's content can be viewed or edited.

Properties of **access**

`read``boolean`

Whether read access has been provided (`true`) or denied (`false`).

`write``boolean`

Whether write access has been provided (`true`) or denied (`false`).

`comment``boolean`

Optional

Whether comment access has been provided (`true`) or denied (`false`).

`owning_team_only``boolean`

Optional

Only users in the same team as the design's owner can access the design.

If `owning_team_only` is `false`, anyone with the link can access the design.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_DESIGN_ACCESS_CONTROLS",
    
        "changes": [
    
          {
    
            "type": "CREATE_DESIGN_ACCESS_TOKEN",
    
            "token_prefix": "ZMrbBHL2",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            }
    
          },
    
          {
    
            "type": "DELETE_DESIGN_ACCESS_TOKEN",
    
            "token_prefix": "ZMrbBHL2",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            }
    
          },
    
          {
    
            "type": "CREATE_DESIGN_ACCESS_INVITE",
    
            "token_prefix": "ZMrbBHL2",
    
            "recipient": "ash.doe@example.com",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            }
    
          },
    
          {
    
            "type": "REDEEM_DESIGN_ACCESS_INVITE",
    
            "token_prefix": "ZMrbBHL2",
    
            "recipient": "ash.doe@example.com",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "DELETE_DESIGN_ACCESS_INVITE",
    
            "token_prefix": "ZMrbBHL2",
    
            "recipient": "ash.doe@example.com"
    
          },
    
          {
    
            "type": "UPDATE_DESIGN_OWNER",
    
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
    
            "type": "CREATE_DESIGN_ACCESS_RESTRICTION"
    
          },
    
          {
    
            "type": "DELETE_DESIGN_ACCESS_RESTRICTION"
    
          },
    
          {
    
            "type": "GRANT_USER_DESIGN_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "REVOKE_USER_DESIGN_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_USER_DESIGN_ACCESS",
    
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
    
            "type": "GRANT_GROUP_DESIGN_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            }
    
          },
    
          {
    
            "type": "REVOKE_GROUP_DESIGN_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_GROUP_DESIGN_ACCESS",
    
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
    
            "type": "GRANT_TEAM_DESIGN_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "REVOKE_TEAM_DESIGN_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_TEAM_DESIGN_ACCESS",
    
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
    
            "type": "GRANT_ORGANIZATION_DESIGN_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "REVOKE_ORGANIZATION_DESIGN_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "UPDATE_ORGANIZATION_DESIGN_ACCESS",
    
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
    
          },
    
          {
    
            "type": "GRANT_DESIGN_LINK_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "owning_team_only": true
    
          },
    
          {
    
            "type": "REVOKE_DESIGN_LINK_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "comment": true
    
            },
    
            "owning_team_only": true
    
          },
    
          {
    
            "type": "UPDATE_DESIGN_LINK_ACCESS",
    
            "old_link_role": {
    
              "access": {
    
                "read": true,
    
                "write": false
    
              },
    
              "owning_team_only": true
    
            },
    
            "new_link_role": {
    
              "access": {
    
                "read": true,
    
                "write": true
    
              },
    
              "owning_team_only": false
    
            }
    
          }
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Send a design share notification

An `actor` triggers this event when they share a design. Canva will attempt to send an email and an in-app notification to the user the design is shared with (`recipient`).

`type``string`

**Default value:** `SEND_DESIGN_SHARE_NOTIFICATION`

**Available values:** The only valid value is `SEND_DESIGN_SHARE_NOTIFICATION`.

`recipient``ShareNotificationRecipient`

The recipient of the share notification.

The recipient can be a user, a group, an organization, or an email address.

USER_RECIPIENTUSER_RECIPIENT

GROUP_RECIPIENTGROUP_RECIPIENT

ORGANIZATION_RECIPIENTORGANIZATION_RECIPIENT

EMAIL_RECIPIENTEMAIL_RECIPIENT

`type``string`

**Default value:** `USER_RECIPIENT`

**Available values:** The only valid value is `USER_RECIPIENT`.

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

`type``string`

**Default value:** `GROUP_RECIPIENT`

**Available values:** The only valid value is `GROUP_RECIPIENT`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`type``string`

**Default value:** `ORGANIZATION_RECIPIENT`

**Available values:** The only valid value is `ORGANIZATION_RECIPIENT`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`type``string`

**Default value:** `EMAIL_RECIPIENT`

**Available values:** The only valid value is `EMAIL_RECIPIENT`.

`email``string`

The email address the design invite was sent to.

`message``string`

Optional

An optional message from the `actor` to the `recipient`.

`invite_to_team``boolean`

Optional

Whether the `recipient` was invited to the team containing the shared design.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "SEND_DESIGN_SHARE_NOTIFICATION",
    
        "message": "Check out my design!",
    
        "recipient": {
    
          "type": "USER_RECIPIENT",
    
          "user": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          }
    
        },
    
        "invite_to_team": false
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Request access to a design

An `actor` triggers this event when they request access to a design. This request is sent to the owner of the design.

`type``string`

**Default value:** `REQUEST_DESIGN_ACCESS`

**Available values:** The only valid value is `REQUEST_DESIGN_ACCESS`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "REQUEST_DESIGN_ACCESS"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Grant access to a design

An `actor` (typically the design `owner`) triggers this event when they grant the `requester` access to their design.

`type``string`

**Default value:** `GRANT_DESIGN_ACCESS`

**Available values:** The only valid value is `GRANT_DESIGN_ACCESS`.

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

A user's access level for a design.

**Available values:**

  * `VIEW`: The user can view the design.
  * `COMMENT`: The user can view and comment on the design.
  * `EDIT`: The user can view, comment, edit, and modify access to the design.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "GRANT_DESIGN_ACCESS",
    
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
