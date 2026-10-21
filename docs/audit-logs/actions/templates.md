---
url: https://www.canva.dev/docs/audit-logs/actions/templates/
title: Templates - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:54.586652+00:00
---

# Templates - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/templates/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Templates

Copy page

## Publish a template

An `actor` triggers this event when they publish a template

`type``string`

**Default value:** `PUBLISH_TEMPLATE`

**Available values:** The only valid value is `PUBLISH_TEMPLATE`.

`template_type``string`

Optional

The type of a template

**Available values:**

  * `DESIGN`: A design template
  * `ELEMENT`: An element template



`template_domain``string`

Optional

The domain of a template

**Available values:** The only valid value is `BRAND`: Brand domain.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "PUBLISH_TEMPLATE",
    
        "template_type": "DESIGN",
    
        "template_domain": "BRAND"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a template's details

An `actor` triggers this event when they update a template

`type``string`

**Default value:** `UPDATE_TEMPLATE`

**Available values:** The only valid value is `UPDATE_TEMPLATE`.

`template_type``string`

Optional

The type of a template

**Available values:**

  * `DESIGN`: A design template
  * `ELEMENT`: An element template



`template_domain``string`

Optional

The domain of a template

**Available values:** The only valid value is `BRAND`: Brand domain.

`new_title``string`

Optional

The new title of the template

`old_title``string`

Optional

The old title of the template.

`new_description``string`

Optional

The new description of the template

`old_description``string`

Optional

The old description of the template.

`new_keywords``string[]`

Optional

The new keywords of the template

`old_keywords``string[]`

Optional

The old keywords of the template

`changed_fields``string[]`

Optional

Fields requested to be changed in this update.

**Available values:**

  * `TITLE`: The template's title
  * `DESCRIPTION`: The template's description
  * `KEYWORDS`: The template's keywords



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_TEMPLATE",
    
        "template_type": "DESIGN",
    
        "template_domain": "BRAND",
    
        "new_title": "New Instagram Template",
    
        "old_title": "Old Instagram Template",
    
        "new_description": "An new Instagram template",
    
        "old_description": "An old Instagram template",
    
        "new_keywords": [
    
          "festival",
    
          "halloween"
    
        ],
    
        "old_keywords": [
    
          "festival",
    
          "christmas"
    
        ],
    
        "changed_fields": [
    
          "TITLE",
    
          "DESCRIPTION"
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete a template

An `actor` triggers this event when they delete a template.

`type``string`

**Default value:** `DELETE_TEMPLATE`

**Available values:** The only valid value is `DELETE_TEMPLATE`.

`template_type``string`

Optional

The type of a template

**Available values:**

  * `DESIGN`: A design template
  * `ELEMENT`: An element template



`template_domain``string`

Optional

The domain of a template

**Available values:** The only valid value is `BRAND`: Brand domain.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_TEMPLATE",
    
        "template_type": "DESIGN",
    
        "template_domain": "BRAND"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Restore a deleted template

An `actor` triggers this event when they restore a deleted template.

`type``string`

**Default value:** `UNDELETE_TEMPLATE`

**Available values:** The only valid value is `UNDELETE_TEMPLATE`.

`template_type``string`

Optional

The type of a template

**Available values:**

  * `DESIGN`: A design template
  * `ELEMENT`: An element template



`template_domain``string`

Optional

The domain of a template

**Available values:** The only valid value is `BRAND`: Brand domain.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNDELETE_TEMPLATE",
    
        "template_type": "DESIGN",
    
        "template_domain": "BRAND"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a template's access controls

An `actor` triggers this event when they update the access control list of a template.

`type``string`

**Default value:** `UPDATE_TEMPLATE_ACCESS_CONTROLS`

**Available values:** The only valid value is `UPDATE_TEMPLATE_ACCESS_CONTROLS`.

`changes``TemplateAccessControlChange[]`

List of access control changes made to the template

GRANT_USER_TEMPLATE_ACCESSGRANT_USER_TEMPLATE_ACCESS

REVOKE_USER_TEMPLATE_ACCESSREVOKE_USER_TEMPLATE_ACCESS

UPDATE_USER_TEMPLATE_ACCESSUPDATE_USER_TEMPLATE_ACCESS

GRANT_TEAM_TEMPLATE_ACCESSGRANT_TEAM_TEMPLATE_ACCESS

REVOKE_TEAM_TEMPLATE_ACCESSREVOKE_TEAM_TEMPLATE_ACCESS

UPDATE_TEAM_TEMPLATE_ACCESSUPDATE_TEAM_TEMPLATE_ACCESS

GRANT_GROUP_TEMPLATE_ACCESSGRANT_GROUP_TEMPLATE_ACCESS

REVOKE_GROUP_TEMPLATE_ACCESSREVOKE_GROUP_TEMPLATE_ACCESS

UPDATE_GROUP_TEMPLATE_ACCESSUPDATE_GROUP_TEMPLATE_ACCESS

GRANT_ORGANIZATION_TEMPLATE_ACCESSGRANT_ORGANIZATION_TEMPLATE_ACCESS

REVOKE_ORGANIZATION_TEMPLATE_ACCESSREVOKE_ORGANIZATION_TEMPLATE_ACCESS

UPDATE_ORGANIZATION_TEMPLATE_ACCESSUPDATE_ORGANIZATION_TEMPLATE_ACCESS

GRANT_PUBLIC_LINK_TEMPLATE_ACCESSGRANT_PUBLIC_LINK_TEMPLATE_ACCESS

REVOKE_PUBLIC_LINK_TEMPLATE_ACCESSREVOKE_PUBLIC_LINK_TEMPLATE_ACCESS

GRANT_TEAM_LINK_TEMPLATE_ACCESSGRANT_TEAM_LINK_TEMPLATE_ACCESS

REVOKE_TEAM_LINK_TEMPLATE_ACCESSREVOKE_TEAM_LINK_TEMPLATE_ACCESS

Grant template access to a user

`type``string`

**Default value:** `GRANT_USER_TEMPLATE_ACCESS`

**Available values:** The only valid value is `GRANT_USER_TEMPLATE_ACCESS`.

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

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Revoke template access from a user

`type``string`

**Default value:** `REVOKE_USER_TEMPLATE_ACCESS`

**Available values:** The only valid value is `REVOKE_USER_TEMPLATE_ACCESS`.

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

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Update template access from a user

`type``string`

**Default value:** `UPDATE_USER_TEMPLATE_ACCESS`

**Available values:** The only valid value is `UPDATE_USER_TEMPLATE_ACCESS`.

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

`new_access``TemplateAccessLevel`

Template access level

Properties of **new_access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`old_access``TemplateAccessLevel`

Template access level

Properties of **old_access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Grant template access to a team

`type``string`

**Default value:** `GRANT_TEAM_TEMPLATE_ACCESS`

**Available values:** The only valid value is `GRANT_TEAM_TEMPLATE_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`role``string`

Optional

Identity context roles assignable to access control principals

**Available values:**

  * `ORGANIZATION_ADMIN`: The admin of the organization
  * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
  * `TEAM_OWNER`: The owner of the team
  * `TEAM_ADMIN`: The admin of the team
  * `TEAM_DESIGNER`: The designer of the team



Revoke template access from a team

`type``string`

**Default value:** `REVOKE_TEAM_TEMPLATE_ACCESS`

**Available values:** The only valid value is `REVOKE_TEAM_TEMPLATE_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`role``string`

Optional

Identity context roles assignable to access control principals

**Available values:**

  * `ORGANIZATION_ADMIN`: The admin of the organization
  * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
  * `TEAM_OWNER`: The owner of the team
  * `TEAM_ADMIN`: The admin of the team
  * `TEAM_DESIGNER`: The designer of the team



Update template access for a team

`type``string`

**Default value:** `UPDATE_TEAM_TEMPLATE_ACCESS`

**Available values:** The only valid value is `UPDATE_TEAM_TEMPLATE_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`new_access``TemplateAccessLevel`

Template access level

Properties of **new_access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`old_access``TemplateAccessLevel`

Template access level

Properties of **old_access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`role``string`

Optional

Identity context roles assignable to access control principals

**Available values:**

  * `ORGANIZATION_ADMIN`: The admin of the organization
  * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
  * `TEAM_OWNER`: The owner of the team
  * `TEAM_ADMIN`: The admin of the team
  * `TEAM_DESIGNER`: The designer of the team



Grant template access to a group

`type``string`

**Default value:** `GRANT_GROUP_TEMPLATE_ACCESS`

**Available values:** The only valid value is `GRANT_GROUP_TEMPLATE_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Revoke template access from a group

`type``string`

**Default value:** `REVOKE_GROUP_TEMPLATE_ACCESS`

**Available values:** The only valid value is `REVOKE_GROUP_TEMPLATE_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Update template access from a group

`type``string`

**Default value:** `UPDATE_GROUP_TEMPLATE_ACCESS`

**Available values:** The only valid value is `UPDATE_GROUP_TEMPLATE_ACCESS`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`new_access``TemplateAccessLevel`

Template access level

Properties of **new_access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`old_access``TemplateAccessLevel`

Template access level

Properties of **old_access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Grant template access to an organization

`type``string`

**Default value:** `GRANT_ORGANIZATION_TEMPLATE_ACCESS`

**Available values:** The only valid value is `GRANT_ORGANIZATION_TEMPLATE_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`role``string`

Optional

Identity context roles assignable to access control principals

**Available values:**

  * `ORGANIZATION_ADMIN`: The admin of the organization
  * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
  * `TEAM_OWNER`: The owner of the team
  * `TEAM_ADMIN`: The admin of the team
  * `TEAM_DESIGNER`: The designer of the team



Revoke template access from an organization

`type``string`

**Default value:** `REVOKE_ORGANIZATION_TEMPLATE_ACCESS`

**Available values:** The only valid value is `REVOKE_ORGANIZATION_TEMPLATE_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`role``string`

Optional

Identity context roles assignable to access control principals

**Available values:**

  * `ORGANIZATION_ADMIN`: The admin of the organization
  * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
  * `TEAM_OWNER`: The owner of the team
  * `TEAM_ADMIN`: The admin of the team
  * `TEAM_DESIGNER`: The designer of the team



Update template access for an organization

`type``string`

**Default value:** `UPDATE_ORGANIZATION_TEMPLATE_ACCESS`

**Available values:** The only valid value is `UPDATE_ORGANIZATION_TEMPLATE_ACCESS`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`new_access``TemplateAccessLevel`

Template access level

Properties of **new_access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`old_access``TemplateAccessLevel`

Template access level

Properties of **old_access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`role``string`

Optional

Identity context roles assignable to access control principals

**Available values:**

  * `ORGANIZATION_ADMIN`: The admin of the organization
  * `ORGANIZATION_TEAM_MANAGER`: The team manager of the organization
  * `TEAM_OWNER`: The owner of the team
  * `TEAM_ADMIN`: The admin of the team
  * `TEAM_DESIGNER`: The designer of the team



Grant template access to a public share link

`type``string`

**Default value:** `GRANT_PUBLIC_LINK_TEMPLATE_ACCESS`

**Available values:** The only valid value is `GRANT_PUBLIC_LINK_TEMPLATE_ACCESS`.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Revoke template access from a public share link

`type``string`

**Default value:** `REVOKE_PUBLIC_LINK_TEMPLATE_ACCESS`

**Available values:** The only valid value is `REVOKE_PUBLIC_LINK_TEMPLATE_ACCESS`.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Grant template access to a team share link

`type``string`

**Default value:** `GRANT_TEAM_LINK_TEMPLATE_ACCESS`

**Available values:** The only valid value is `GRANT_TEAM_LINK_TEMPLATE_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

Revoke template access from a team share link

`type``string`

**Default value:** `REVOKE_TEAM_LINK_TEMPLATE_ACCESS`

**Available values:** The only valid value is `REVOKE_TEAM_LINK_TEMPLATE_ACCESS`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`access``TemplateAccessLevel`

Template access level

Properties of **access**

`read``boolean`

Whether the user can view the template.

`write``boolean`

Whether the user can edit the template content.

`share_view_access``boolean`

Whether the user can share the template with others to view.

`share_edit_access``boolean`

Whether the user can share the template with others view and edit.

`delete``boolean`

Whether the user can delete the template.

`template_type``string`

Optional

The type of a template

**Available values:**

  * `DESIGN`: A design template
  * `ELEMENT`: An element template



`template_domain``string`

Optional

The domain of a template

**Available values:** The only valid value is `BRAND`: Brand domain.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_TEMPLATE_ACCESS_CONTROLS",
    
        "template_type": "DESIGN",
    
        "template_domain": "BRAND",
    
        "changes": [
    
          {
    
            "type": "GRANT_USER_TEMPLATE_ACCESS",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "REVOKE_USER_TEMPLATE_ACCESS",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "UPDATE_USER_TEMPLATE_ACCESS",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "new_access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            },
    
            "old_access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "GRANT_TEAM_TEMPLATE_ACCESS",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            },
    
            "role": "ORGANIZATION_ADMIN",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "REVOKE_TEAM_TEMPLATE_ACCESS",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            },
    
            "role": "ORGANIZATION_ADMIN",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "UPDATE_TEAM_TEMPLATE_ACCESS",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            },
    
            "role": "ORGANIZATION_ADMIN",
    
            "new_access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            },
    
            "old_access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "GRANT_GROUP_TEMPLATE_ACCESS",
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            },
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "REVOKE_GROUP_TEMPLATE_ACCESS",
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            },
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "UPDATE_GROUP_TEMPLATE_ACCESS",
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            },
    
            "new_access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            },
    
            "old_access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "GRANT_ORGANIZATION_TEMPLATE_ACCESS",
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            },
    
            "role": "ORGANIZATION_ADMIN",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "REVOKE_ORGANIZATION_TEMPLATE_ACCESS",
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            },
    
            "role": "ORGANIZATION_ADMIN",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "UPDATE_ORGANIZATION_TEMPLATE_ACCESS",
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            },
    
            "role": "ORGANIZATION_ADMIN",
    
            "new_access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            },
    
            "old_access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "GRANT_PUBLIC_LINK_TEMPLATE_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "REVOKE_PUBLIC_LINK_TEMPLATE_ACCESS",
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "GRANT_TEAM_LINK_TEMPLATE_ACCESS",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            },
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          },
    
          {
    
            "type": "REVOKE_TEAM_LINK_TEMPLATE_ACCESS",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            },
    
            "access": {
    
              "read": true,
    
              "write": true,
    
              "share_view_access": true,
    
              "share_edit_access": true,
    
              "delete": true
    
            }
    
          }
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
