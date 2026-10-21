---
url: https://www.canva.dev/docs/admin/canva-concepts/
title: Canva concepts - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:38.630779+00:00
---

# Canva concepts - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/canva-concepts/

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

# Canva concepts

Copy page

The Canva Admin API helps you manage teams, groups, and users within a Canva organization. This article describes the Canva organizational concepts that are relevant to using the Admin API.

## Teams, groups, and users

Canva users are organized into _organizations_ , _teams_ , and _groups_. For [Canva Enterprise⁠(opens in a new tab or window)](https://www.canva.com/enterprise/) customers, an **Organization** is the largest organizational unit, and can contain many teams, groups, and users. For non-enterprise customers, a **Team** is the largest organizational unit.

![Diagram showing that teams can have multiple groups, and users can be members of multiple Groups.](https://www.canva.dev/_next/static/media/Single_team.5710ad37.png)

A team (Acme Corp) can have many users and groups, with some users in one or more groups, and some not in a group at all.

All users are in _at least_ one team; including [Canva Free and Canva Pro users⁠(opens in a new tab or window)](https://www.canva.com/pricing/), who are in their own (individual) teams. Users in a team have access to all content shared with that team and can easily [share content with other team members⁠(opens in a new tab or window)](https://www.canva.com/help/team-sharing/).

Groups belong to _a_ team and can't be shared between two teams. Users don't need to be part of a group, but they can be in one or more groups.

![Diagram showing that a user can be in multiple teams, teams can have multiple groups, and users can be members of multiple groups.](https://www.canva.dev/_next/static/media/Multi_teams.382157a8.png)

Some large organizations have multiple teams, and some users may be in one or more of those teams.
