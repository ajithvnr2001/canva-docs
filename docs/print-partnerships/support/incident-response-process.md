---
url: https://www.canva.dev/docs/print-partnerships/support/incident-response-process/
title: Incident response process - Support - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:04.077729+00:00
---

# Incident response process - Support - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/support/incident-response-process/

Support

[General support](https://www.canva.dev/docs/print-partnerships/support/general-support/)[Incident response process](https://www.canva.dev/docs/print-partnerships/support/incident-response-process/)

# Incident response process

Copy page

At times, partners may experience issues with an integration. Some issues may severely impact a partner's business. Canva refers to such issues as _Incidents_.

Canva has a streamlined process to address incidents. Partners must follow this process and report incidents immediately. This helps Canva resolve issues quickly and reduce the adverse impact on a partner's business.

This document explains Canva's incident response process.

Canva's incident response process is only for Tier 1 partners. Tier 2 and Tier 3 partners must [report bugs](https://www.canva.dev/docs/print-partnerships/support/incident-response-process/#report-bugs) instead.

## Incident vs. Bug

Not all issues are incidents. Some issues may be bugs. Canva differentiates incidents from bugs in the following way:

Issue type| Description| Severity| Attention  
---|---|---|---  
Incident| Severely impacts a partner's business. See [Types](https://www.canva.dev/docs/print-partnerships/support/incident-response-process/#types).| High| Immediate  
Bug| Affects only a few users, designs, or artworks, and not the entire business.| Medium, Low| Can wait  
  
## Types

Canva classifies incidents into the following types:

Incident| < 0.05% Affected users| 0.05% - 1% Affected users| 1% - 10% Affected users| > 10% Affected users  
---|---|---|---|---  
Core feature broken| Minor| Major| Major| Critical  
Non-core feature broken| Minor| Minor| Minor| Major  
Performance severely affected (barely usable)| Minor| Minor| Major| Critical  
Performance slightly affected (degraded, but usable)| Minor| Minor| Minor| Major  
  
## Response team

Canva has a team of engineers on call to respond to incidents and a dedicated team to specifically respond to partnership incidents.

Canva has tooling to monitor the health and performance of its system. Canva sets up these monitors to proactively alert Canva engineers of failures in the system.

Canva engineers get to know of a failure even before a partner gets to know.

## Monitoring dashboard

Canva has a dashboard that shows the system's status in real time. The dashboard is available at <https://www.canvastatus.com/>[⁠(opens in a new tab or window)](https://www.canvastatus.com/).

If partners suspect something's wrong with an integration, they can check the status in the dashboard.

## Subscribe to alerts

Partners can receive alerts when Canva creates, updates, or resolves an incident, or changes a component status.

To subscribe to alerts:

  1. Navigate to Canva's monitoring dashboard at <https://www.canvastatus.com/>[⁠(opens in a new tab or window)](https://www.canvastatus.com/).
  2. Click **SUBSCRIBE TO UPDATES**.
  3. Select the way you want to receive alerts: 
     1. For webhook notifications, specify the endpoint URL.
     2. For email notifications, specify an email address.



To learn about webhook notifications, see the following article: <https://support.atlassian.com/statuspage/docs/enable-webhook-notifications/>[⁠(opens in a new tab or window)](https://support.atlassian.com/statuspage/docs/enable-webhook-notifications/)

## Report incidents

To report an incident:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68).
  2. Select **Incident**.
  3. Select **Report an incident**.
  4. Fill out the required fields.
  5. Attach screenshots and code snippets as needed.
  6. Click **Send**.



Canva engineers will respond via the ticket. The [response time](https://www.canva.dev/docs/print-partnerships/support/incident-response-process/#response-time) varies according to the incident type. Only if they deem necessary, will they contact a partner via other means, such as telephone or video call.

## Report bugs

To report bugs:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68).
  2. Select **Support**.
  3. Select **Report a bug**.
  4. Fill out the required fields.
  5. Attach screenshots and code snippets as needed.
  6. Click **Send**.



Canva engineers will respond via the ticket during their regular business hours.

## Response time

Canva's response time varies according to the incident type:

Response| Critical| Major| Minor  
---|---|---|---  
Acknowledge| Within 15 minutes| Within 15 minutes| Within 8 hours  
Start| Immediately| Immediately| Within 8 hours  
Update| Every hour| Every hour| As per Canva's Bug Fix Policy  
Resolve| Within 8 hours| Within 24 hours| As per Canva's Bug Fix Policy  
Inform| Immediately after resolving| Immediately after resolving| Immediately after resolving  
Close| Within 15 minutes of informing| Within 15 minutes of informing| Within 15 minutes of informing  
  
## Actions

Canva takes the following actions after the incident:

  1. Starts the root cause analysis immediately. If notified outside of business hours, Canva starts the analysis the next business day.
  2. Prepares a Root Cause Analysis report (RCA report). The report has: 
     1. Issue summary.
     2. Incident duration.
     3. Incident start timestamp and end timestamp.
     4. Number of affected customers.
  3. Sends the RCA report to the partner.


