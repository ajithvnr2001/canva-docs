---
url: https://www.canva.dev/docs/audit-logs/actions/investigations/
title: Investigations - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:52.905953+00:00
---

# Investigations - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/investigations/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Investigations

Copy page

## Start an investigation

An `actor` triggers this event when they start an investigation.

`type``string`

**Default value:** `START_INVESTIGATION`

**Available values:** The only valid value is `START_INVESTIGATION`.

`owners``AuditLogUser[]`

The list of owners that are being audited in the investigation.

Properties of **owners**

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

`investigation_reason``string`

Optional

**Available values:**

  * `SECURITY_INVESTIGATION`: Security investigation.
  * `COMPLIANCE_INVESTIGATION`: Compliance investigation.
  * `OTHER`: Other.



`context``string`

Optional

The context provided as a rationale for starting the investigation.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "START_INVESTIGATION",
    
        "owners": [
    
          {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          }
    
        ],
    
        "investigation_reason": "SECURITY_INVESTIGATION",
    
        "context": "Reviewing designs created by the marketing team for brand compliance."
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Investigate a design

An `actor` triggers this event when they view a specific design during an investigation.

`type``string`

**Default value:** `INVESTIGATE_DESIGN`

**Available values:** The only valid value is `INVESTIGATE_DESIGN`.

`investigation_id``string`

Optional

The ID for the investigation. This is a UUID that represents the investigation.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "INVESTIGATE_DESIGN",
    
        "investigation_id": "550e8400-e29b-41d4-a716-446655440000"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
