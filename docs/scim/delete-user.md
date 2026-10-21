---
url: https://www.canva.dev/docs/scim/delete-user/
title: Delete a user - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:05.987067+00:00
---

# Delete a user - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/delete-user/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# Delete a user

Copy page

The Canva SCIM API doesn't implement a REST `DELETE` operation for a SCIM user.

To deprovision a SCIM user, you can use the `PATCH` operation to set the user's `active` attribute to `false`. For more information, see [Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/).
