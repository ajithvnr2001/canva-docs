---
url: https://www.canva.dev/docs/audit-logs/
title: Canva Audit Logs - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:48.176097+00:00
---

# Canva Audit Logs - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Canva Audit Logs

Use audit logs to track changes made by your team in Canva.

Copy page

Canva provides audit logs that contain records of user activities in Canva, such as installing a [Canva App⁠(opens in a new tab or window)](https://www.canva.com/your-apps/), [exporting a design⁠(opens in a new tab or window)](https://www.canva.com/help/download-or-purchase/) for download, or a user changing their [account settings⁠(opens in a new tab or window)](https://www.canva.com/help/account-settings/). These logs can be useful for compliance audits, monitoring for unauthorized activity, and other matters that require details about the creation, access, and deletion of data in Canva.

Audit logs are available for organizations that use [Canva Enterprise⁠(opens in a new tab or window)](https://www.canva.com/enterprise/).

Canva starts generating audit logs when an organization upgrades their account to Canva Enterprise and will start logging events for a brand once it joins the Canva Enterprise account.

Canva stores audit log data in an [Amazon S3 bucket⁠(opens in a new tab or window)](https://aws.amazon.com/s3/) that your organization owns and manages. We add events to your S3 bucket every minute as a gzipped archive containing [JSONL⁠(opens in a new tab or window)](https://jsonlines.org/) content.

We record each activity as an [audit event](https://www.canva.dev/docs/audit-logs/audit-events/), with details about the activity under the `action` property. For information on the different actions, review the audit logs **Actions reference**.
