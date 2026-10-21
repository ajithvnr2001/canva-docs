---
url: https://www.canva.dev/docs/scim/authentication/
title: Authentication - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:05.176152+00:00
---

# Authentication - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/authentication/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# Authentication

Copy page

To authenticate to the Canva SCIM API, your client requests must provide a `Bearer` token in the `Authorization` header.

## Generate an access token

Generate the access token from your team's settings in your Canva account. Only team administrators and owners of Canva for Teams or Canva for Education have access to generate a SCIM access token.

  1. Log in to your Canva account.

  2. Click the gear icon to go to your [Account settings⁠(opens in a new tab or window)](https://www.canva.com/settings/your-account).

  3. In the side menu, under your team's settings, click **SSO & provisioning**.

  4. Under **SCIM** , select **Enable SCIM user provisioning**.

Each time the slider is toggled, the current access token is revoked and a new token is created.

  5. Copy the access token.




The SCIM access token is unique to your Canva team, and there's only a single access token active at any one time. It is a long-lived token, so make sure it's stored securely.
