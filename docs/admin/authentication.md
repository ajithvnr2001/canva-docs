---
url: https://www.canva.dev/docs/admin/authentication/
title: Authentication - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:38.589253+00:00
---

# Authentication - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/authentication/

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

# Authentication

Copy page

The Canva Admin API uses an OAuth 2.0 bearer token to authenticate requests, as part of the OAuth [Client Credentials flow⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4).

## Prerequisites

Before attempting to generate an access token, you must first create and configure an Admin API client in your Canva organization settings, including:

  * Setting a client name and getting a client ID
  * Generating and saving a client secret
  * Selecting scopes



For more information, see [Creating clients](https://www.canva.dev/docs/admin/creating-clients/).

## Authentication and authorization process

The authentication and authorization process works as follows:

  1. Use the [Generate an access token](https://www.canva.dev/docs/admin/api-reference/oauth/generate-access-token/) endpoint to generate an access token. In the request, you must include the client ID, client secret, and scopes.
  2. When making requests to the Admin API resource endpoints, put the access token in the `Authorization` header to authenticate the requests.
  3. When the access token expires, generate a new access token using the [Generate an access token](https://www.canva.dev/docs/admin/api-reference/oauth/generate-access-token/) endpoint.


