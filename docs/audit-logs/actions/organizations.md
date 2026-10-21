---
url: https://www.canva.dev/docs/audit-logs/actions/organizations/
title: Organizations - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:52.797884+00:00
---

# Organizations - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/organizations/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Organizations

Copy page

## Update an organization's details

An `actor` triggers this event when they update the details of a [Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/), such as the organization's display name.

`type``string`

**Default value:** `UPDATE_ORGANIZATION`

**Available values:** The only valid value is `UPDATE_ORGANIZATION`.

`changed_fields``string[]`

Optional

Fields requested to be changed in this update.

**Available values:**

  * `ORGANIZATION_NAME`: The name of the organization.
  * `DEFAULT_TEAM`: The team to provision users into by default.
  * `DEFAULT_TEAM_POLICY`: The policy for determining if a user can be provisioned into a default team.



`old_name``string`

Optional

The previous name of the organization.

`new_name``string`

Optional

The new name of the organization.

`default_team``AuditLogTeam`

Optional

A Canva team.

Properties of **default_team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`default_team_policy``string`

Optional

The policy for determining if a user can be provisioned into a default team.

**Available values:**

  * `ADMIN_AND_UP`: Users with the `ADMIN` organization role or higher are added to the team.
  * `DESIGNER_AND_UP`: Users with the `DESIGNER` organization role or higher are added to the team.
  * `MEMBER_AND_UP`: Users with the `MEMBER` organization role or higher are added to the team.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_ORGANIZATION",
    
        "changed_fields": [
    
          "ORGANIZATION_NAME",
    
          "DEFAULT_TEAM",
    
          "DEFAULT_TEAM_POLICY"
    
        ],
    
        "old_name": "Untitled Corporation",
    
        "new_name": "Acme Corporation",
    
        "default_team": {
    
          "id": "BXeFatjDhdR",
    
          "display_name": "Acme Team"
    
        },
    
        "default_team_policy": "ADMIN_AND_UP"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a user in an organization

An `actor` triggers this event when they update a Canva user's membership within a [Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). This includes promoting a `MEMBER` to `BRAND_DESIGNER` or `ADMIN`, changing roles between `BRAND_DESIGNER` and `ADMIN`, or removing a user's `ADMIN` or `BRAND_DESIGNER` role.

`type``string`

**Default value:** `UPDATE_USER_IN_ORGANIZATION`

**Available values:** The only valid value is `UPDATE_USER_IN_ORGANIZATION`.

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

`old_role``string`

Optional

The user's role in the organization.

**Available values:**

  * `ADMIN`: Organization admin.
  * `BRAND_DESIGNER`: Organization brand designer.
  * `MEMBER`: Organization member.



`new_role``string`

Optional

The user's role in the organization.

**Available values:**

  * `ADMIN`: Organization admin.
  * `BRAND_DESIGNER`: Organization brand designer.
  * `MEMBER`: Organization member.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_USER_IN_ORGANIZATION",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "old_role": "BRAND_DESIGNER",
    
        "new_role": "ADMIN"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Add a team to the organization

An `actor` triggers this event when they add a Canva Team to their [Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).

`type``string`

**Default value:** `ADD_TEAM_TO_ORGANIZATION`

**Available values:** The only valid value is `ADD_TEAM_TO_ORGANIZATION`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "ADD_TEAM_TO_ORGANIZATION",
    
        "team": {
    
          "id": "BXeFatjDhdR",
    
          "display_name": "Acme Team"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Remove a team from the organization

An `actor` triggers this event when they remove a Canva Team from their [Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).

`type``string`

**Default value:** `REMOVE_TEAM_FROM_ORGANIZATION`

**Available values:** The only valid value is `REMOVE_TEAM_FROM_ORGANIZATION`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "REMOVE_TEAM_FROM_ORGANIZATION",
    
        "team": {
    
          "id": "BXeFatjDhdR",
    
          "display_name": "Acme Team"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
