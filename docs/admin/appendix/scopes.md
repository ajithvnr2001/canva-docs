---
url: https://www.canva.dev/docs/admin/appendix/scopes/
title: Scopes - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:38.550416+00:00
---

# Scopes - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/appendix/scopes/

Getting started

[Overview](https://www.canva.dev/docs/admin/)[Creating clients](https://www.canva.dev/docs/admin/creating-clients/)

Fundamentals

[API requests & responses](https://www.canva.dev/docs/admin/api-requests-responses/)[Authentication](https://www.canva.dev/docs/admin/authentication/)[Canva concepts](https://www.canva.dev/docs/admin/canva-concepts/)

API reference

Authentication

Organizations

Teams

Groups

Users

Audit events

Appendix

[Scopes](https://www.canva.dev/docs/admin/appendix/scopes/)[Error responses](https://www.canva.dev/docs/admin/error-responses/)[Changelog](https://www.canva.dev/docs/admin/changelog/)

# Scopes

Copy page

The `scope` parameter specifies the types of access that your integration needs for a user's account. The list of possible scopes used in the Admin APIs are shown below:

Scope| Description  
---|---  
`admin:auditevent:read`| List audit events for the Canva organization.  
`admin:group:read`| Read information about a Canva group.  
`admin:group:write`| Create or modify a Canva group, and add or remove its users.  
`admin:organization:read`| Read information about the Canva organization.  
`admin:team:read`| Read information about a Canva team and its users.  
`admin:team:write`| Create or modify a Canva team, and add or remove its users.  
`admin:user:read`| Read information about a Canva user.  
`admin:user:write`| Create a managed user in the organization.
