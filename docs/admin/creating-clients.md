---
url: https://www.canva.dev/docs/admin/creating-clients/
title: Creating clients - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:39.031345+00:00
---

# Creating clients - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/creating-clients/

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

# Creating clients

How to create and configure an Admin API client.

Copy page

To get started with the Canva Admin API, you must first create and configure an API client in your organization settings.

## Prerequisites

To create an Admin API client, your Canva account must meet the following prerequisites:

  * You must be a member of a Canva organization, and your account role must be an organization admin. For more information on Canva roles, see [Canva Teams and Canva Enterprise roles and access⁠(opens in a new tab or window)](https://www.canva.com/help/roles-and-permissions/) in the Canva Help Center.
  * Your account must either be set up using Single Sign-On (SSO) or have [Multi-factor Authentication (MFA)⁠(opens in a new tab or window)](https://www.canva.com/help/login-verification/) enabled.



## Creating a client

  1. On Canva, click your profile icon and select **Settings** to open your [Account settings⁠(opens in a new tab or window)](https://www.canva.com/settings/your-account).

  2. In the left sidebar, under **Organization settings** , click **Admin API**.

  3. Click **Create an API client**.

  4. For **Client name** , enter a name for your client. This name is used to identify the client in the Admin API.

  5. Under **Scopes** , select the scopes that you want to grant to the client. Only select the scopes that are required for your client.

For more information on each scope, see [Scopes](https://www.canva.dev/docs/admin/appendix/scopes/).

  6. Click **Continue**.

  7. Save your client ID and secret. You won't be able to view the secret again after you proceed.

  8. Select **I have saved my client secret** , and click **Done**.




Your new client is added to the list of clients in the Admin API settings. From here you can edit the client, view its details, or delete it if it's no longer needed.

## Next steps

See [Authentication](https://www.canva.dev/docs/admin/authentication/) to learn about the Admin API authentication and authorization process for generating access tokens.
