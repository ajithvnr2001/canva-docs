---
url: https://www.canva.dev/docs/audit-logs/actions/audit-logs/
title: Audit Logs - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:49.542570+00:00
---

# Audit Logs - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/audit-logs/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Audit Logs

Copy page

## Export audit logs

An `actor` triggers this event when they click the **Export** button on the **Audit logs** settings page, then click **Download** , as described in [Canva Help: About Canva audit logs⁠(opens in a new tab or window)](https://www.canva.com/help/view-audit-logs/).

`type``string`

**Default value:** `EXPORT_AUDIT_LOGS`

**Available values:** The only valid value is `EXPORT_AUDIT_LOGS`.

`start_timestamp``integer`

Optional

The start of the time period queried by the `actor`, as a Unix timestamp (in milliseconds since the Unix Epoch).

`end_timestamp``integer`

Optional

The end of the time period queried by the `actor`, as a Unix timestamp (in milliseconds since the Unix Epoch).

`team``AuditLogTeam`

Optional

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
    
        "type": "EXPORT_AUDIT_LOGS",
    
        "start_timestamp": 1720292247000,
    
        "end_timestamp": 1720292247000,
    
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

## View audit logs

An `actor` triggers this event when they view the audit logs, as described in [Canva Help: About Canva audit logs⁠(opens in a new tab or window)](https://www.canva.com/help/view-audit-logs/).

`type``string`

**Default value:** `VIEW_AUDIT_LOGS`

**Available values:** The only valid value is `VIEW_AUDIT_LOGS`.

`start_timestamp``integer`

Optional

The start of the time period viewed by the `actor`, as a Unix timestamp (in milliseconds since the Unix Epoch).

`end_timestamp``integer`

Optional

The end of the time period viewed by the `actor`, as a Unix timestamp (in milliseconds since the Unix Epoch).

`team``AuditLogTeam`

Optional

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
    
        "type": "VIEW_AUDIT_LOGS",
    
        "start_timestamp": 1720292247000,
    
        "end_timestamp": 1720292247000,
    
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

## Update audit log settings

An `actor` triggers this event when they update the audit log settings. If the change updated the S3 Bucket name, this event will appear in the new S3 bucket (the configured S3 Bucket after the change).

`type``string`

**Default value:** `UPDATE_AUDIT_LOGS_SETTINGS`

**Available values:** The only valid value is `UPDATE_AUDIT_LOGS_SETTINGS`.

`changed_fields``string[]`

Optional

The configuration settings the `actor` requested changes for.

**Available values:**

  * `REGION`: The region of the AWS S3 bucket.
  * `S3_BUCKET_NAME`: The name of your Canva audit logs S3 bucket.
  * `S3_KEY_PREFIX`: An optional S3 key prefix.
  * `ROLE_ARN`: The Amazon Resource Name (ARN) of the AWS Role that Canva uses to access the S3 bucket.



`old_region``string`

Optional

The old region of the AWS S3 bucket.

`new_region``string`

Optional

The new region of the AWS S3 bucket.

`old_s3_bucket_name``string`

Optional

The old name of your Canva audit logs S3 bucket.

`new_s3_bucket_name``string`

Optional

The new name of your Canva audit logs S3 bucket.

`old_s3_key_prefix``string`

Optional

The old S3 key prefix.

`new_s3_key_prefix``string`

Optional

The new S3 key prefix.

`old_role_arn``string`

Optional

The old Amazon Resource Name (ARN) of the AWS Role that Canva uses to access the S3 bucket.

`new_role_arn``string`

Optional

The new Amazon Resource Name (ARN) of the AWS Role that Canva uses to access the S3 bucket.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_AUDIT_LOGS_SETTINGS",
    
        "changed_fields": [
    
          "REGION",
    
          "S3_BUCKET_NAME",
    
          "S3_KEY_PREFIX",
    
          "ROLE_ARN"
    
        ],
    
        "old_region": "us-east-1",
    
        "new_region": "us-east-1",
    
        "old_s3_bucket_name": "my-old-canva-audit-logs-bucket",
    
        "new_s3_bucket_name": "my-new-canva-audit-logs-bucket",
    
        "old_s3_key_prefix": "old_bucket/canva/auditlogs",
    
        "new_s3_key_prefix": "new_bucket/canva/auditlogs",
    
        "old_role_arn": "arn:aws:iam::123456789012:role/OldS3Access",
    
        "new_role_arn": "arn:aws:iam::123456789012:role/NewS3Access"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
