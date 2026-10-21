---
url: https://www.canva.dev/docs/audit-logs/actions/groups/
title: Groups - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:52.653300+00:00
---

# Groups - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/groups/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Groups

Copy page

## Create a group

An `actor` triggers this event when they create a new [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). For details on creating Canva groups, see [Canva Help: Creating groups⁠(opens in a new tab or window)](https://www.canva.com/help/groups/).

`type``string`

**Default value:** `CREATE_GROUP`

**Available values:** The only valid value is `CREATE_GROUP`.

`display_name``string`

The display name for the group.

`description``string`

Optional

A description for the group.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_GROUP",
    
        "display_name": "Marketing",
    
        "description": "The Acme Corporation marketing group."
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a group's details

An `actor` triggers this event when they update the details of a [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/), such as the group's display name.

`type``string`

**Default value:** `UPDATE_GROUP`

**Available values:** The only valid value is `UPDATE_GROUP`.

`old_display_name``string`

Optional

The old display name of the group.

`new_display_name``string`

Optional

The new display name for the group.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_GROUP",
    
        "old_display_name": "Marketing",
    
        "new_display_name": "Growth"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete a group

An `actor` triggers this event when they delete a [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).

`type``string`

**Default value:** `DELETE_GROUP`

**Available values:** The only valid value is `DELETE_GROUP`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_GROUP"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Add a user to a group

An `actor` triggers this event when they add a Canva user to a [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). For details on adding users to a Canva group, see [Canva Help: Creating groups — Adding people to a group⁠(opens in a new tab or window)](https://www.canva.com/help/groups/).

`type``string`

**Default value:** `ADD_USER_TO_GROUP`

**Available values:** The only valid value is `ADD_USER_TO_GROUP`.

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

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



`reason``GroupMembershipChangeReason`

Optional

The reason for the change.

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

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "ADD_USER_TO_GROUP",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "role": "MEMBER",
    
        "reason": {
    
          "type": "PROVISIONING_POLICY",
    
          "provisioning_policy": {
    
            "id": "eb4f7245-b082-4774-a3d6-6d64525a8657",
    
            "name": "My Provisioning Policy"
    
          }
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a user in a group

An `actor` triggers this event when they update a Canva user's membership within a [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/), such as changing the user's role from `ADMIN` to `MEMBER`.

`type``string`

**Default value:** `UPDATE_USER_IN_GROUP`

**Available values:** The only valid value is `UPDATE_USER_IN_GROUP`.

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

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



`old_role``string`

Optional

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_USER_IN_GROUP",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "new_role": "ADMIN",
    
        "old_role": "MEMBER"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Remove a user from a group

An `actor` triggers this event when they remove a Canva user from a [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). This includes users removing themselves from a group.

`type``string`

**Default value:** `REMOVE_USER_FROM_GROUP`

**Available values:** The only valid value is `REMOVE_USER_FROM_GROUP`.

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

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



`reason``GroupMembershipChangeReason`

Optional

The reason for the change.

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

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "REMOVE_USER_FROM_GROUP",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "role": "MEMBER",
    
        "reason": {
    
          "type": "PROVISIONING_POLICY",
    
          "provisioning_policy": {
    
            "id": "eb4f7245-b082-4774-a3d6-6d64525a8657",
    
            "name": "My Provisioning Policy"
    
          }
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Send a group invitation

An `actor` triggers this event when they send an invitation to join a [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/). The invitation is addressed to a user, an email address, or shared as a link.

`type``string`

**Default value:** `CREATE_GROUP_INVITATION`

**Available values:** The only valid value is `CREATE_GROUP_INVITATION`.

`invitation_type``GroupInvitationType`

How a user is invited to join a group. The invitation can be addressed to an email address, issued as a short-lived join code, or a shareable link.

EMAILEMAIL

CODECODE

LINKLINK

A group invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email address invited to the group.

A group invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A group invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

`role``string`

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_GROUP_INVITATION",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "role": "MEMBER"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Resend a group invitation

An `actor` triggers this event when they resend a group invitation to an email address.

`type``string`

**Default value:** `RESEND_GROUP_INVITATION`

**Available values:** The only valid value is `RESEND_GROUP_INVITATION`.

`invitation_type``GroupInvitationType`

How a user is invited to join a group. The invitation can be addressed to an email address, issued as a short-lived join code, or a shareable link.

EMAILEMAIL

CODECODE

LINKLINK

A group invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email address invited to the group.

A group invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A group invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

`role``string`

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



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
    
        "type": "RESEND_GROUP_INVITATION",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "inviter": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "role": "MEMBER"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a group invitation

An `actor` triggers this event when they change a pending group invitation, such as updating the invitee's role. The optional `old_role` field is the previous group role when the role was changed.

`type``string`

**Default value:** `UPDATE_GROUP_INVITATION`

**Available values:** The only valid value is `UPDATE_GROUP_INVITATION`.

`invitation_type``GroupInvitationType`

How a user is invited to join a group. The invitation can be addressed to an email address, issued as a short-lived join code, or a shareable link.

EMAILEMAIL

CODECODE

LINKLINK

A group invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email address invited to the group.

A group invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A group invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

`new_role``string`

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



`changed_fields``string[]`

Optional

Fields requested to be changed in this update.

**Available values:** The only valid value is `ROLE`: The group role..

`old_role``string`

Optional

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



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
    
        "type": "UPDATE_GROUP_INVITATION",
    
        "changed_fields": [
    
          "ROLE"
    
        ],
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "new_role": "MEMBER",
    
        "old_role": "MEMBER",
    
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

## Cancel a group invitation

An `actor` triggers this event when they cancel a pending group invitation. The invitation is identified by the invited user, an email address, or the invitation link.

`type``string`

**Default value:** `DELETE_GROUP_INVITATION`

**Available values:** The only valid value is `DELETE_GROUP_INVITATION`.

`role``string`

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



`invitation_type``GroupInvitationType`

Optional

How a user is invited to join a group. The invitation can be addressed to an email address, issued as a short-lived join code, or a shareable link.

EMAILEMAIL

CODECODE

LINKLINK

A group invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email address invited to the group.

A group invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A group invitation issued as a shareable join link.

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
    
        "type": "DELETE_GROUP_INVITATION",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "inviter": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "role": "MEMBER"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Accept a group invitation

An `actor` triggers this event when they accept a pending group invitation.

`type``string`

**Default value:** `ACCEPT_GROUP_INVITATION`

**Available values:** The only valid value is `ACCEPT_GROUP_INVITATION`.

`invitation_type``GroupInvitationType`

How a user is invited to join a group. The invitation can be addressed to an email address, issued as a short-lived join code, or a shareable link.

EMAILEMAIL

CODECODE

LINKLINK

A group invitation addressed to an email address.

`type``string`

**Default value:** `EMAIL`

**Available values:** The only valid value is `EMAIL`: Invite by an email..

`email``string`

The email address invited to the group.

A group invitation issued as a short-lived join code.

`type``string`

**Default value:** `CODE`

**Available values:** The only valid value is `CODE`: Invite by a short-lived code..

A group invitation issued as a shareable join link.

`type``string`

**Default value:** `LINK`

**Available values:** The only valid value is `LINK`: Invite by a link..

`role``string`

Optional

The user's role within a group.

**Available values:**

  * `MEMBER`: Group member.
  * `ADMIN`: Group administrator.



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
    
        "type": "ACCEPT_GROUP_INVITATION",
    
        "invitation_type": {
    
          "type": "EMAIL",
    
          "email": "alex.doe@example.com"
    
        },
    
        "role": "MEMBER",
    
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
