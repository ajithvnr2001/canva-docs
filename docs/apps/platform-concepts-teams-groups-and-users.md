---
url: https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/
title: Teams, groups, and users - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:12.096718+00:00
---

# Teams, groups, and users - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Teams, groups, and users

An introduction to how Canva organizes teams, groups, and users.

Copy page

How Canva organizes its users affects which content each user can access.

Canva users are organized into _organizations_ , _teams_ , and _groups_. For [Canva Enterprise⁠(opens in a new tab or window)](https://www.canva.com/enterprise/) customers, an **Organization** is the largest organizational unit, and can contain many teams, groups, and users. For non-enterprise customers, a **Team** is the largest organizational unit.

![Diagram showing that teams can have multiple groups, and users can be members of multiple Groups.](https://www.canva.dev/_next/static/media/Single_team.5710ad37.png)

A team (Acme Corp) can have many users and groups, with some users in one or more groups, and some not in a group at all.

All users are in _at least_ one team; including [Canva Free and Canva Pro users⁠(opens in a new tab or window)](https://www.canva.com/pricing/), who are in their own (individual) teams. Users in a team have access to all content shared with that team and can easily [share content with other team members⁠(opens in a new tab or window)](https://www.canva.com/help/team-sharing/).

Groups belong to _a_ team and can't be shared between two teams. Users don't need to be part of a group, but they can be in one or more groups.

![Diagram showing that a user can be in multiple teams, teams can have multiple groups, and users can be members of multiple groups.](https://www.canva.dev/_next/static/media/Multi_teams.382157a8.png)

Some large organizations have multiple teams, and some users may be in one or more of those teams.

For REST API endpoints that interact with users, see the [Users](https://www.canva.dev/docs/apps/rest-apis/reference/users/) API reference.
