---
url: https://www.canva.dev/docs/audit-logs/audit-events/
title: Audit events - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:56.054743+00:00
---

# Audit events - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/audit-events/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Audit events

Copy page

Audit events are exported as JSON and specify an `actor` that performed an `action` on a `target` at time `timestamp` with a specific `outcome` under a `context`. For example:
    
    
    {
    
      "id": "3849ef51-ca85-4028-bae3-1b8de3ee5738",
    
      "timestamp": 1704070800123,
    
      "actor": {
    
        "type": "USER",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "team": {
    
          "id": "BXeFatjDhdR",
    
          "display_name": "Acme Team"
    
        },
    
        "organization": {
    
          "id": "OXtgecafZvh",
    
          "display_name": "Acme Corporation"
    
        },
    
        "redacted": true
    
      },
    
      "target": {
    
        "target_type": "USER",
    
        "user": {
    
          "id": "UXoqDbwwSbQ",
    
          "display_name": "Jane Doe",
    
          "email": "jane.doe@example.com"
    
        },
    
        "team": {
    
          "id": "BXeFatjDhdR",
    
          "display_name": "Acme Team"
    
        }
    
      },
    
      "action": {
    
        "type": "CREATE",
    
        "create_type": "CREATE_DESIGN"
    
      },
    
      "outcome": {
    
        "result": "PERMITTED",
    
        "details": {
    
          "type": "RESOURCE_CREATED",
    
          "resource_id": "DXWEBartcNg",
    
          "resource_type": "DESIGN"
    
        }
    
      },
    
      "context": {
    
        "ip_address": "192.0.2.123",
    
        "session": "41cfef61",
    
        "request_id": "220d18b47fcb2d23c72a2a954dff09cb",
    
        "device_id": "d2805fafb9b50fe3f3d6ebbe221fc0e0883bf06b6bc285389147f3b259c2c4c1",
    
        "integration_id": "OC-AZEqRSSuRkSM"
    
      }
    
    }

JSON

Copy

The `actor` is the user who initiated the `action`. This can be a logged in user, or an anonymous (logged out) user.

The `action` describes the activity, such as a user viewing a design or deleting another user.

The `target` is the user, team, organization, or resource that the `action` targeted. For example, a delete user `action` includes the ID of the user being deleted.

The `outcome` includes the result of the `action`, such as whether it succeeded and information about affected resources. For example, the `outcome` of a successful create user `action` will contain the user ID of the newly created user.

The `context` contains additional information related to the event, such as the IP address of the `actor`.

## AuditEvent schema

`id``string`

The ID of the audit event.

`timestamp``integer`

The time the event occurred, as a Unix timestamp (in milliseconds since the Unix Epoch).

`actor``Actor`

The person who performed the action.

USERUSER

CANVA_CUSTOMER_SUPPORTCANVA_CUSTOMER_SUPPORT

ANONYMOUSANONYMOUS

SYSTEMSYSTEM

ADMIN_API_CLIENTADMIN_API_CLIENT

A Canva user, including the team and organization context for the action.

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`.

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

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`redacted``boolean`

`true` when we've redacted the details of the user, brand, or organization because they're outside of your organization.

`organization``AuditLogOrganization`

Optional

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

A Canva Staff member providing customer support.

`type``string`

**Default value:** `CANVA_CUSTOMER_SUPPORT`

**Available values:** The only valid value is `CANVA_CUSTOMER_SUPPORT`.

A user that isn't signed in.

`type``string`

**Default value:** `ANONYMOUS`

**Available values:** The only valid value is `ANONYMOUS`.

A system that isn't associated with a single user account. System actors include internal Canva system processes or external systems such as SCIM IdP providers.

`type``string`

**Default value:** `SYSTEM`

**Available values:** The only valid value is `SYSTEM`.

`details``SystemDetails`

Optional

Details about the system actor.

SCIMSCIM

CRMCRM

Details about the SCIM IdP provider.

`type``string`

**Default value:** `SCIM`

**Available values:** The only valid value is `SCIM`.

Details about the Customer Relationship Management system.

`type``string`

**Default value:** `CRM`

**Available values:** The only valid value is `CRM`.

An Admin API client acting on behalf of an organization. Identified by the customer-visible OAuth Client ID.

`type``string`

**Default value:** `ADMIN_API_CLIENT`

**Available values:** The only valid value is `ADMIN_API_CLIENT`.

`client_id``string`

The customer-visible OAuth Client ID shown in the UI.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`client_name``string`

Optional

Human-readable name assigned to the client at creation time.

`target``Target`

The target resource of an action.

USERUSER

TEAMTEAM

ORGANIZATIONORGANIZATION

RESOURCERESOURCE

The user that is the target of the action.

`target_type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`.

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

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

The team that is the target of the action.

`target_type``string`

**Default value:** `TEAM`

**Available values:** The only valid value is `TEAM`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

The organization that is the target of the action.

`target_type``string`

**Default value:** `ORGANIZATION`

**Available values:** The only valid value is `ORGANIZATION`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

The resource that's the target of the action. For example, a design.

`target_type``string`

**Default value:** `RESOURCE`

**Available values:** The only valid value is `RESOURCE`.

`resource_type``string`

The type of resource.

**Available values:**

  * `BRAND_KIT`: A [Brand Kit⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).
  * `DESIGN`: A design.
  * `FILE`: A file.
  * `FOLDER`: A folder.
  * `GROUP`: A [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
  * `MEDIA`: A media.
  * `ADMIN_API_CLIENT`: An OAuth client for the [Admin API](https://www.canva.dev/docs/admin/).
  * `TEMPLATE`: A template.
  * `VIDEO`: A video.
  * `AUDIO`: An audio.
  * `WEBSITE_DOMAIN`: A website domain.
  * `WEBSITE_SSO_CONNECTION`: An SSO connection for Canva Websites.
  * `PROVISIONING_POLICY`: A provisioning policy.
  * `3D`: A 3D.
  * `TEAM_SPACE`: A team space.



`id``string`

The resource ID.

`owner``Owner`

The owner of the resource.

USERUSER

TEAMTEAM

ORGANIZATIONORGANIZATION

An owner who is a user.

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`.

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

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

An owner that is a team.

`type``string`

**Default value:** `TEAM`

**Available values:** The only valid value is `TEAM`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

An owner that is an organization.

`type``string`

**Default value:** `ORGANIZATION`

**Available values:** The only valid value is `ORGANIZATION`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`name``string`

Optional

The name of the resource.

`action``Action`

This can be one of the following action types:

  * [3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)
  * [Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)
  * [Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)
  * [Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)
  * [Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)
  * [Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)
  * [Content](https://www.canva.dev/docs/audit-logs/actions/content/)
  * [Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)
  * [Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)
  * [Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)
  * [Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)
  * [Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)
  * [Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)
  * [Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)
  * [Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)
  * [Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)
  * [Users](https://www.canva.dev/docs/audit-logs/actions/users/)
  * [Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)
  * [Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)



`outcome``Outcome`

Outcome of the action.

Properties of **outcome**

`result``string`

The outcome result.

**Available values:**

  * `UNKNOWN`: The action failed due to an unknown error.
  * `PERMITTED`: The action was permitted.
  * `DENIED`: The action was denied.
  * `RESOURCE_NOT_FOUND`: The action failed because the resource was not found.
  * `FAILED`: The action failed.



`details``OutcomeDetails`

Optional

Additional details about the outcome.

RESOURCE_CREATEDRESOURCE_CREATED

USER_CREATEDUSER_CREATED

INVESTIGATION_STARTEDINVESTIGATION_STARTED

Outcome details when a new resource is created.

`type``string`

**Default value:** `RESOURCE_CREATED`

**Available values:** The only valid value is `RESOURCE_CREATED`.

`resource_id``string`

The resource ID.

`resource_type``string`

The type of resource.

**Available values:**

  * `BRAND_KIT`: A [Brand Kit⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).
  * `DESIGN`: A design.
  * `FILE`: A file.
  * `FOLDER`: A folder.
  * `GROUP`: A [Canva group](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/).
  * `MEDIA`: A media.
  * `ADMIN_API_CLIENT`: An OAuth client for the [Admin API](https://www.canva.dev/docs/admin/).
  * `TEMPLATE`: A template.
  * `VIDEO`: A video.
  * `AUDIO`: An audio.
  * `WEBSITE_DOMAIN`: A website domain.
  * `WEBSITE_SSO_CONNECTION`: An SSO connection for Canva Websites.
  * `PROVISIONING_POLICY`: A provisioning policy.
  * `3D`: A 3D.
  * `TEAM_SPACE`: A team space.



Outcome details when a new user is created.

`type``string`

**Default value:** `USER_CREATED`

**Available values:** The only valid value is `USER_CREATED`.

`user_id``string`

The ID of the created user.

Outcome details when a new investigation is started.

`type``string`

**Default value:** `INVESTIGATION_STARTED`

**Available values:** The only valid value is `INVESTIGATION_STARTED`.

`investigation_id``string`

The ID for the investigation. This is a UUID that represents the investigation.

`context``Context`

Additional context associated with the audit event.

Properties of **context**

`ip_address``string`

Optional

The IP address of the actor.

`session``string`

Optional

The session ID of the actor.

`request_id``string`

Optional

The ID of the request.

`device_id``string`

Optional

A hashed ID generated and stored on the device when a user logs into Canva from a device without a `device_id` (such as a new or reformatted device, or after a web browser's cache is cleared). This ID can be useful for identifying suspicious logins.

This ID is stored on the user's device, and may be subject to forgery or tampering.

`integration_id``string`

Optional

Identifier for the [Canva Integration](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)
