---
url: https://www.canva.dev/docs/audit-logs/actions/teams/
title: Teams - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:53.928858+00:00
---

# Teams - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/teams/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Teams

Copy page

## Update a team's details

An `actor` triggers this event when they update the details of a [Canva Team⁠(opens in a new tab or window)](https://www.canva.com/help/manage-teams/), such as the team's display name.

We only log the team properties that the actor requested changes for. The changed fields are listed in the `changed_fields` array.

`type``string`

**Default value:** `UPDATE_TEAM`

**Available values:** The only valid value is `UPDATE_TEAM`.

`changed_fields``string[]`

Optional

Fields requested to be changed in this update.

**Available values:**

  * `TEAM_NAME`: The team name.
  * `DISPLAY_NAME`: The team's display name as shown in the Canva UI.
  * `THIRD_PARTY`: Whether this team represents a third party integration.
  * `BILLING_INFO`: Billing information for the team.
  * `WEBSITE_URL`: The website URL for the team.
  * `ADDRESS`: The team's address.
  * `EXTERNAL_LINKS`: Links to teams or other entities within external identity providers.
  * `BRAND_COLORS_ONLY`: Whether the team is restricted to brand colors.
  * `BRAND_FONTS_ONLY`: Whether the team is restricted to brand fonts.



`team_name``string`

Optional

The team name.

`display_name``string`

Optional

The team's display name. This is used to represent the team with text in a UI.

`third_party_integrated``boolean`

Optional

Whether this team represents a third-party integrated application.

`billing_info``object`

Optional

Billing information for the team.

Properties of **billing_info**

`company_name``string`

Optional

`company_address``string`

Optional

`billing_contacts``string[]`

Optional

`team_address``object`

Optional

Address for the team.

Properties of **team_address**

`street1``string`

Optional

`street2``string`

Optional

`city``string`

Optional

`subdivision``string`

Optional

`country_code``string`

Optional

`postcode``string`

Optional

`external_links``TeamExternalLink[]`

Optional

Represents a link to teams or other entities within external identity providers.

Properties of **external_links**

`source``string`

Optional

The source of the external link.

**Available values:**

  * `ONE_ROSTER`: A OneRoster system.
  * `MANUAL`: Manual imports, such as Canva customer support performing the import.



`managing_team``object`

Optional

Represents the managing team with the associated external configuration. When `source` is `MANUAL`, users managed by the managing team are provisioned into this team as a fallback.

Properties of **managing_team**

`id``string`

The managing team ID.

`external_id``string`

Optional

Included when `source` is not `MANUAL`. Otherwise, this is the SSO identity provider or OneRoster external ID associated with the team.

`website_url``string`

Optional

The website URL for the team.

`brand_fonts_only``boolean`

Optional

Whether the team is restricted to brand fonts.

`brand_colors_only``boolean`

Optional

Whether the team is restricted to brand colors.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_TEAM",
    
        "changed_fields": "ADDRESS",
    
        "team_address": {
    
          "street1": "110 Kippax street",
    
          "city": "Surry Hills",
    
          "subdivision": "AU-NSW",
    
          "country_code": "AU",
    
          "postcode": 2010
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete a team

An `actor` triggers this event when they delete a [Canva Team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). For details on deleting a Canva team, see [Canva Help: Managing and deleting teams — Deleting a team⁠(opens in a new tab or window)](https://www.canva.com/help/manage-teams/).

`type``string`

**Default value:** `DELETE_TEAM`

**Available values:** The only valid value is `DELETE_TEAM`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_TEAM"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Cancel the deletion of a team

An `actor` triggers this event when they cancel or undo the deletion of a [Canva Team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). For details on deleting a Canva team, see [Canva Help: Managing and deleting teams — Canceling or undoing team deletion⁠(opens in a new tab or window)](https://www.canva.com/help/manage-teams/).

`type``string`

**Default value:** `UNDELETE_TEAM`

**Available values:** The only valid value is `UNDELETE_TEAM`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNDELETE_TEAM"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Add a user to a team

An `actor` triggers this event when they add a Canva user to a [Canva team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). For details on adding users to a Canva team, see [Canva Help: Adding or removing people in a team or class — Inviting users to join your team⁠(opens in a new tab or window)](https://www.canva.com/help/manage-members/).

The `reason` field contains the reason the user was added to the team. For example, they accepted a team invitation or they were provisioned by a SCIM provider.

`type``string`

**Default value:** `ADD_USER_TO_TEAM`

**Available values:** The only valid value is `ADD_USER_TO_TEAM`.

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

`role``string`

Optional

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`reason``TeamMembershipChangeReason`

Optional

The reason for the change.

INVITATION_ACCEPTEDINVITATION_ACCEPTED

JOIN_POLICY_ALLOWEDJOIN_POLICY_ALLOWED

REQUEST_TO_JOIN_APPROVEDREQUEST_TO_JOIN_APPROVED

SCIMSCIM

SAML_JIT_PROVISIONINGSAML_JIT_PROVISIONING

PROVISIONING_POLICYPROVISIONING_POLICY

ADMIN_APIADMIN_API

An invitation to join team was accepted

`type``string`

**Default value:** `INVITATION_ACCEPTED`

**Available values:** The only valid value is `INVITATION_ACCEPTED`.

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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

The change was permitted by your [Team discovery and settings⁠(opens in a new tab or window)](https://www.canva.com/help/team-discovery/).

`type``string`

**Default value:** `JOIN_POLICY_ALLOWED`

**Available values:** The only valid value is `JOIN_POLICY_ALLOWED`.

A user request to join your team was approved.

`type``string`

**Default value:** `REQUEST_TO_JOIN_APPROVED`

**Available values:** The only valid value is `REQUEST_TO_JOIN_APPROVED`.

The change was made through your team's configured [SCIM Identity Provider⁠(opens in a new tab or window)](https://www.canva.com/help/scim-provisioning-and-deprovisioning/).

`type``string`

**Default value:** `SCIM`

**Available values:** The only valid value is `SCIM`.

SAML Just-In-Time provisioning. This event can be triggered by events like a user [linking their Canva account with your SSO provider⁠(opens in a new tab or window)](https://www.canva.com/help/sso-linking/) or when you [set up Single Sign-On (SSO)⁠(opens in a new tab or window)](https://www.canva.com/help/set-up-sso/) for your team.

`type``string`

**Default value:** `SAML_JIT_PROVISIONING`

**Available values:** The only valid value is `SAML_JIT_PROVISIONING`.

This change was triggered by an provisioning policy.

`type``string`

**Default value:** `PROVISIONING_POLICY`

**Available values:** The only valid value is `PROVISIONING_POLICY`.

`provisioning_policy``AuditLogProvisioningPolicy`

Optional

A Canva provisioning policy.

Properties of **provisioning_policy**

`id``string`

The provisioning policy ID.

`name``string`

Optional

The provisioning policy name.

The change was made through the Admin API.

`type``string`

**Default value:** `ADMIN_API`

**Available values:** The only valid value is `ADMIN_API`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "ADD_USER_TO_TEAM",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Ash Doe",
    
          "email": "ash.doe@example.com"
    
        },
    
        "role": "MEMBER",
    
        "reason": {
    
          "type": "INVITATION_ACCEPTED",
    
          "inviter": {
    
            "id": "USwwQbbxoqD",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          }
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a user in a team

An `actor` triggers this event when they update a Canva user's membership within a [Canva team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/), such as changing the user's role from `ADMIN` to `MEMBER`. For details on the different team roles, see [Canva Help: Team roles and permissions⁠(opens in a new tab or window)](https://www.canva.com/help/roles-and-permissions/).

The `reason` field contains the reason the user was updated in the team. For example, their details were updated by a SCIM provider.

`type``string`

**Default value:** `UPDATE_USER_IN_TEAM`

**Available values:** The only valid value is `UPDATE_USER_IN_TEAM`.

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

`new_role``string`

Optional

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`old_role``string`

Optional

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`reason``TeamMembershipChangeReason`

Optional

The reason for the change.

INVITATION_ACCEPTEDINVITATION_ACCEPTED

JOIN_POLICY_ALLOWEDJOIN_POLICY_ALLOWED

REQUEST_TO_JOIN_APPROVEDREQUEST_TO_JOIN_APPROVED

SCIMSCIM

SAML_JIT_PROVISIONINGSAML_JIT_PROVISIONING

PROVISIONING_POLICYPROVISIONING_POLICY

ADMIN_APIADMIN_API

An invitation to join team was accepted

`type``string`

**Default value:** `INVITATION_ACCEPTED`

**Available values:** The only valid value is `INVITATION_ACCEPTED`.

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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

The change was permitted by your [Team discovery and settings⁠(opens in a new tab or window)](https://www.canva.com/help/team-discovery/).

`type``string`

**Default value:** `JOIN_POLICY_ALLOWED`

**Available values:** The only valid value is `JOIN_POLICY_ALLOWED`.

A user request to join your team was approved.

`type``string`

**Default value:** `REQUEST_TO_JOIN_APPROVED`

**Available values:** The only valid value is `REQUEST_TO_JOIN_APPROVED`.

The change was made through your team's configured [SCIM Identity Provider⁠(opens in a new tab or window)](https://www.canva.com/help/scim-provisioning-and-deprovisioning/).

`type``string`

**Default value:** `SCIM`

**Available values:** The only valid value is `SCIM`.

SAML Just-In-Time provisioning. This event can be triggered by events like a user [linking their Canva account with your SSO provider⁠(opens in a new tab or window)](https://www.canva.com/help/sso-linking/) or when you [set up Single Sign-On (SSO)⁠(opens in a new tab or window)](https://www.canva.com/help/set-up-sso/) for your team.

`type``string`

**Default value:** `SAML_JIT_PROVISIONING`

**Available values:** The only valid value is `SAML_JIT_PROVISIONING`.

This change was triggered by an provisioning policy.

`type``string`

**Default value:** `PROVISIONING_POLICY`

**Available values:** The only valid value is `PROVISIONING_POLICY`.

`provisioning_policy``AuditLogProvisioningPolicy`

Optional

A Canva provisioning policy.

Properties of **provisioning_policy**

`id``string`

The provisioning policy ID.

`name``string`

Optional

The provisioning policy name.

The change was made through the Admin API.

`type``string`

**Default value:** `ADMIN_API`

**Available values:** The only valid value is `ADMIN_API`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_USER_IN_TEAM",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "new_role": "DESIGNER",
    
        "old_role": "MEMBER",
    
        "reason": {
    
          "type": "SCIM"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Remove a user from a team

An `actor` triggers this event when they remove a Canva user from a [Canva team](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). This includes users [removing themselves from a team⁠(opens in a new tab or window)](https://www.canva.com/help/leave-teams/).

The `reason` field contains the reason the user was removed from the team. For example, they were removed by a SCIM provider.

`type``string`

**Default value:** `REMOVE_USER_FROM_TEAM`

**Available values:** The only valid value is `REMOVE_USER_FROM_TEAM`.

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

`role``string`

Optional

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`reason``TeamMembershipChangeReason`

Optional

The reason for the change.

INVITATION_ACCEPTEDINVITATION_ACCEPTED

JOIN_POLICY_ALLOWEDJOIN_POLICY_ALLOWED

REQUEST_TO_JOIN_APPROVEDREQUEST_TO_JOIN_APPROVED

SCIMSCIM

SAML_JIT_PROVISIONINGSAML_JIT_PROVISIONING

PROVISIONING_POLICYPROVISIONING_POLICY

ADMIN_APIADMIN_API

An invitation to join team was accepted

`type``string`

**Default value:** `INVITATION_ACCEPTED`

**Available values:** The only valid value is `INVITATION_ACCEPTED`.

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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

The change was permitted by your [Team discovery and settings⁠(opens in a new tab or window)](https://www.canva.com/help/team-discovery/).

`type``string`

**Default value:** `JOIN_POLICY_ALLOWED`

**Available values:** The only valid value is `JOIN_POLICY_ALLOWED`.

A user request to join your team was approved.

`type``string`

**Default value:** `REQUEST_TO_JOIN_APPROVED`

**Available values:** The only valid value is `REQUEST_TO_JOIN_APPROVED`.

The change was made through your team's configured [SCIM Identity Provider⁠(opens in a new tab or window)](https://www.canva.com/help/scim-provisioning-and-deprovisioning/).

`type``string`

**Default value:** `SCIM`

**Available values:** The only valid value is `SCIM`.

SAML Just-In-Time provisioning. This event can be triggered by events like a user [linking their Canva account with your SSO provider⁠(opens in a new tab or window)](https://www.canva.com/help/sso-linking/) or when you [set up Single Sign-On (SSO)⁠(opens in a new tab or window)](https://www.canva.com/help/set-up-sso/) for your team.

`type``string`

**Default value:** `SAML_JIT_PROVISIONING`

**Available values:** The only valid value is `SAML_JIT_PROVISIONING`.

This change was triggered by an provisioning policy.

`type``string`

**Default value:** `PROVISIONING_POLICY`

**Available values:** The only valid value is `PROVISIONING_POLICY`.

`provisioning_policy``AuditLogProvisioningPolicy`

Optional

A Canva provisioning policy.

Properties of **provisioning_policy**

`id``string`

The provisioning policy ID.

`name``string`

Optional

The provisioning policy name.

The change was made through the Admin API.

`type``string`

**Default value:** `ADMIN_API`

**Available values:** The only valid value is `ADMIN_API`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "REMOVE_USER_FROM_TEAM",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Alex Doe",
    
          "email": "alex.doe@example.com"
    
        },
    
        "role": "MEMBER",
    
        "reason": {
    
          "type": "SAML_JIT_PROVISIONING"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Request to join a team

An `actor` triggers this event when they request to join a team and the team's settings require an administrator to approve before they can join. For information on users joining teams, see [Canva Help: Joining teams⁠(opens in a new tab or window)](https://www.canva.com/help/join-teams/).

`type``string`

**Default value:** `CREATE_TEAM_JOIN_REQUEST`

**Available values:** The only valid value is `CREATE_TEAM_JOIN_REQUEST`.

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

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_TEAM_JOIN_REQUEST",
    
        "user": {
    
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

## Update a user's request to join a team

An `actor` triggers this event when they update a user's request to join a team. For example, an administrator approved another user's request to join a team.

`type``string`

**Default value:** `UPDATE_TEAM_JOIN_REQUEST`

**Available values:** The only valid value is `UPDATE_TEAM_JOIN_REQUEST`.

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

`approval_status``string`

The status of a request or invite to join a team.

**Available values:**

  * `PENDING`: The request is pending.
  * `APPROVED`: An administrator approved the request.
  * `REJECTED`: An administrator rejected the request.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_TEAM_JOIN_REQUEST",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "approval_status": "PENDING"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Request to invite a user into a team

A non-administrator `actor` triggers this event when they create a request to invite user to join a team.

`type``string`

**Default value:** `CREATE_TEAM_INVITATION_REQUEST`

**Available values:** The only valid value is `CREATE_TEAM_INVITATION_REQUEST`.

`emails``string[]`

A list of emails invited to join the team. These emails might not be linked to existing Canva accounts.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_TEAM_INVITATION_REQUEST",
    
        "emails": [
    
          "ash.doe@example.com",
    
          "alex.doe@example.com"
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a request to invite a user into a team

An `actor` triggers this event when they update a non-administrator's request to invite a user to join a team. For example, an administrator approved a user's request to invite another user to join a team.

`type``string`

**Default value:** `UPDATE_TEAM_INVITATION_REQUEST`

**Available values:** The only valid value is `UPDATE_TEAM_INVITATION_REQUEST`.

`email``string`

The email invited to join the team.

`approval_status``string`

The status of a request or invite to join a team.

**Available values:**

  * `PENDING`: The request is pending.
  * `APPROVED`: An administrator approved the request.
  * `REJECTED`: An administrator rejected the request.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_TEAM_INVITATION_REQUEST",
    
        "email": "alex.doe@example.com",
    
        "approval_status": "PENDING"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Export a team report

An `actor` triggers this event when they export a team report. For details on these reports, see [Canva Help: Checking team analytics and reports⁠(opens in a new tab or window)](https://www.canva.com/help/team-reports/).

`type``string`

**Default value:** `EXPORT_TEAM_REPORT`

**Available values:** The only valid value is `EXPORT_TEAM_REPORT`.

`report_type``string`

Optional

The type of team activity report.

**Available values:**

  * `TEAM_MEMBER_ACTIVITY`: Team member activity. This includes the team member role, when they were last active, and the number of designs that they have created, published, shared, and viewed.
  * `BRAND_TEMPLATE_ACTIVITY`: Brand template activity. This includes the number of times a brand template was used, published, or shared.
  * `BRAND_KIT_ACTIVITY`: Brand Kit activity. This includes the number of times a Brand Kit was applied.
  * `BRAND_KIT_DESIGN_ACTIVITY`: Brand Kit design activity. This includes either the designs using a specific Brand Kit, or designs not using any Brand Kits.



`start_timestamp``integer`

Optional

The start of the report's time window, as a Unix timestamp (in milliseconds since the Unix Epoch).

`end_timestamp``integer`

Optional

The end of the report's time window, as a Unix timestamp (in milliseconds since the Unix Epoch).

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "EXPORT_TEAM_REPORT",
    
        "report_type": "TEAM_MEMBER_ACTIVITY",
    
        "start_timestamp": 1709751447000,
    
        "end_timestamp": 1720292247000
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Export a design approval activity report

An `actor` triggers this event when they export a design approval activity report from the design approvals page. The report contains the team's design approval activity for up to the past 12 months. For details on design approvals, see [Canva Help: Setting up design approval⁠(opens in a new tab or window)](https://www.canva.com/help/setting-up-design-approval/).

`type``string`

**Default value:** `EXPORT_DESIGN_APPROVAL_ACTIVITY_REPORT`

**Available values:** The only valid value is `EXPORT_DESIGN_APPROVAL_ACTIVITY_REPORT`.

`start_timestamp``integer`

Optional

The start of the report's time window, as a Unix timestamp (in milliseconds since the Unix Epoch).

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "EXPORT_DESIGN_APPROVAL_ACTIVITY_REPORT",
    
        "start_timestamp": 1709751447000
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Send a team invitation

An `actor` triggers this event when they send a request to invite a user to join a team. The invitation is addressed by email, an invited user, a single-use code, or a shareable link. For information on users joining teams, see [Canva Help: Joining teams⁠(opens in a new tab or window)](https://www.canva.com/help/join-teams/?query=invitation).

`type``string`

**Default value:** `CREATE_TEAM_INVITATION`

**Available values:** The only valid value is `CREATE_TEAM_INVITATION`.

`role``string`

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`invitation_type``TeamInvitationType`

Optional

How a user is invited to join a team. The invitation can be addressed to a specific email, an existing Canva user, a short-lived join code, or a shareable link.

EMAILEMAIL

USERUSER

CODECODE

LINKLINK

A team invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email invited to join the team.

A team invitation addressed to a specific Canva user.

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`: Invite by a user..

`invitee``AuditLogUser`

A Canva user.

Properties of **invitee**

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

A team invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A team invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_TEAM_INVITATION",
    
        "role": "MEMBER",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a team invitation

An `actor` triggers this event when they change the role or other details of an existing team invitation.

`type``string`

**Default value:** `UPDATE_TEAM_INVITATION`

**Available values:** The only valid value is `UPDATE_TEAM_INVITATION`.

`invitation_type``TeamInvitationType`

How a user is invited to join a team. The invitation can be addressed to a specific email, an existing Canva user, a short-lived join code, or a shareable link.

EMAILEMAIL

USERUSER

CODECODE

LINKLINK

A team invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email invited to join the team.

A team invitation addressed to a specific Canva user.

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`: Invite by a user..

`invitee``AuditLogUser`

A Canva user.

Properties of **invitee**

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

A team invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A team invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

`changed_fields``string[]`

Optional

Fields requested to be changed in this update.

**Available values:** The only valid value is `ROLE`: The team role..

`new_role``string`

Optional

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`old_role``string`

Optional

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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
    
        "type": "UPDATE_TEAM_INVITATION",
    
        "changed_fields": [
    
          "ROLE"
    
        ],
    
        "new_role": "MEMBER",
    
        "old_role": "MEMBER",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "inviter": {
    
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

## Resend a team invitation

An `actor` triggers this event when they resend a team invitation to an invitee.

`type``string`

**Default value:** `RESEND_TEAM_INVITATION`

**Available values:** The only valid value is `RESEND_TEAM_INVITATION`.

`role``string`

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`invitation_type``TeamInvitationType`

How a user is invited to join a team. The invitation can be addressed to a specific email, an existing Canva user, a short-lived join code, or a shareable link.

EMAILEMAIL

USERUSER

CODECODE

LINKLINK

A team invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email invited to join the team.

A team invitation addressed to a specific Canva user.

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`: Invite by a user..

`invitee``AuditLogUser`

A Canva user.

Properties of **invitee**

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

A team invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A team invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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
    
        "type": "RESEND_TEAM_INVITATION",
    
        "role": "MEMBER",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "inviter": {
    
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

## Cancel a team invitation

An `actor` triggers this event when they cancel a pending team invitation. The invitation is identified by the invited email, invitee user, or a multi-use code.

`type``string`

**Default value:** `DELETE_TEAM_INVITATION`

**Available values:** The only valid value is `DELETE_TEAM_INVITATION`.

`role``string`

Optional

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`invitation_type``TeamInvitationType`

Optional

How a user is invited to join a team. The invitation can be addressed to a specific email, an existing Canva user, a short-lived join code, or a shareable link.

EMAILEMAIL

USERUSER

CODECODE

LINKLINK

A team invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email invited to join the team.

A team invitation addressed to a specific Canva user.

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`: Invite by a user..

`invitee``AuditLogUser`

A Canva user.

Properties of **invitee**

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

A team invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A team invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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
    
        "type": "DELETE_TEAM_INVITATION",
    
        "role": "MEMBER",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "inviter": {
    
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

## Accept a team invitation

An `actor` triggers this event when they accept a pending team invitation.

`type``string`

**Default value:** `ACCEPT_TEAM_INVITATION`

**Available values:** The only valid value is `ACCEPT_TEAM_INVITATION`.

`role``string`

The user's role within a team.

**Available values:**

  * `MEMBER`: Team member.
  * `DESIGNER`: Team designer.
  * `ADMIN`: Team administrator.
  * `OWNER`: Team owner.



`invitation_type``TeamInvitationType`

How a user is invited to join a team. The invitation can be addressed to a specific email, an existing Canva user, a short-lived join code, or a shareable link.

EMAILEMAIL

USERUSER

CODECODE

LINKLINK

A team invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email invited to join the team.

A team invitation addressed to a specific Canva user.

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`: Invite by a user..

`invitee``AuditLogUser`

A Canva user.

Properties of **invitee**

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

A team invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A team invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

`invitee``AuditLogUser`

Optional

A Canva user.

Properties of **invitee**

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

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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
    
        "type": "ACCEPT_TEAM_INVITATION",
    
        "role": "MEMBER",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "invitee": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "inviter": {
    
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

## Send a team ownership invitation

An `actor` triggers this event when they invite another user to become the owner of a team.

`type``string`

**Default value:** `CREATE_TEAM_OWNERSHIP_INVITATION`

**Available values:** The only valid value is `CREATE_TEAM_OWNERSHIP_INVITATION`.

`invitee``AuditLogUser`

A Canva user.

Properties of **invitee**

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
    
        "type": "CREATE_TEAM_OWNERSHIP_INVITATION",
    
        "invitee": {
    
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

## Accept a team ownership invitation

An `actor` triggers this event when they accept an invitation to become the owner of a team. The `invitee` field may be omitted when unavailable or redacted.

`type``string`

**Default value:** `ACCEPT_TEAM_OWNERSHIP_INVITATION`

**Available values:** The only valid value is `ACCEPT_TEAM_OWNERSHIP_INVITATION`.

`invitee``AuditLogUser`

Optional

A Canva user.

Properties of **invitee**

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

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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
    
        "type": "ACCEPT_TEAM_OWNERSHIP_INVITATION",
    
        "invitee": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "inviter": {
    
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

## Reject a team ownership invitation

An `actor` triggers this event when they decline an invitation to become the owner of a team. The `invitee` field may be omitted when unavailable or redacted.

`type``string`

**Default value:** `REJECT_TEAM_OWNERSHIP_INVITATION`

**Available values:** The only valid value is `REJECT_TEAM_OWNERSHIP_INVITATION`.

`invitee``AuditLogUser`

Optional

A Canva user.

Properties of **invitee**

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

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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
    
        "type": "REJECT_TEAM_OWNERSHIP_INVITATION",
    
        "invitee": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "inviter": {
    
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

## Cancel a team ownership invitation

An `actor` triggers this event when they withdraw a pending invitation for another user to become the owner of a team. The `invitee` field may be omitted when unavailable or redacted.

`type``string`

**Default value:** `DELETE_TEAM_OWNERSHIP_INVITATION`

**Available values:** The only valid value is `DELETE_TEAM_OWNERSHIP_INVITATION`.

`invitee``AuditLogUser`

Optional

A Canva user.

Properties of **invitee**

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

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

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
    
        "type": "DELETE_TEAM_OWNERSHIP_INVITATION",
    
        "invitee": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "inviter": {
    
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
