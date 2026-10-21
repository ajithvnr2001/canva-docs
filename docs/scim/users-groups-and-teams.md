---
url: https://www.canva.dev/docs/scim/users-groups-and-teams/
title: Users, Groups, and Teams - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:08.603012+00:00
---

# Users, Groups, and Teams - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/users-groups-and-teams/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# Users, Groups, and Teams

Copy page

Canva users are organized into _organizations_ , _teams_ , and _groups_. For [Canva Enterprise⁠(opens in a new tab or window)](https://www.canva.com/enterprise/) customers, an **Organization** is the largest organizational unit, and can contain many teams, groups, and users. For non-enterprise customers, a **Team** is the largest organizational unit.

![Diagram showing that teams can have multiple groups, and users can be members of multiple Groups.](https://www.canva.dev/_next/static/media/Single_team.5710ad37.png)

A team (Acme Corp) can have many users and groups, with some users in one or more groups, and some not in a group at all.

All users are in _at least_ one team; including [Canva Free and Canva Pro users⁠(opens in a new tab or window)](https://www.canva.com/pricing/), who are in their own (individual) teams. Users in a team have access to all content shared with that team and can easily [share content with other team members⁠(opens in a new tab or window)](https://www.canva.com/help/team-sharing/).

Groups belong to _a_ team and can't be shared between two teams. Users don't need to be part of a group, but they can be in one or more groups.

![Diagram showing that a user can be in multiple teams, teams can have multiple groups, and users can be members of multiple groups.](https://www.canva.dev/_next/static/media/Multi_teams.382157a8.png)

Some large organizations have multiple teams, and some users may be in one or more of those teams.
