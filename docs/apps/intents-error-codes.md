---
url: https://www.canva.dev/docs/apps/intents-error-codes/
title: Error codes - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:02.378733+00:00
---

# Error codes - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/intents-error-codes/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

API reference

[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)

App UI Kit reference

[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

Canva REST API reference

[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)

Webhooks notification reference

[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

Tools

[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)

# Error codes

The error codes a Canva Developers SDK method can throw.

Copy page

When a method in the Developers SDK throws an error, there's a limited range of possible error codes. This page lists all of the possible error codes that may appear in a `CanvaError` object.

## `bad_external_service_response`

A response from an external service is invalid or malformed.

**Example:** When redirecting back to Canva at the end of an authentication flow, the URL is malformed.

## `bad_request`

The app has made a request that’s invalid or malformed.

**Example:** The app calls a function without a required parameter.

## `failed_precondition`

The app hasn’t met a precondition.

## `internal_error`

There’s an error in the Developers SDK’s internal implementation.

**Example:** There's an underlying issue in Canva's backend.

## `not_allowed`

The app is not allowed to perform the specified operation.

**Example:** The app tries to call the `navigator.clipboard.write` method, which has been disabled due to it not being cross-browser compatible.

## `not_found`

The app can’t retrieve the specified resource.

**Example:** The app tries to operate on an asset reference that doesn't exist.

## `quota_exceeded`

The app or user has exceeded their allocated quota for a resource or service.

**Example:** The app can't upload a file because the user is out of storage space.

## `permission_denied`

The app doesn’t have sufficient permissions.

**Example:** The app tries to create an element without having sufficient permissions.

## `rate_limited`

The app has made too many requests within a certain time period. The reference page for each API method includes a description of any rate limits. For example, the [rate limit for `requestExport`](https://www.canva.dev/docs/apps/api/v1/design-request-export/#rate-limit).

**Example:** The app tries to create too many elements in a short period of time.

## `timeout`

The operation exceeded the maximum allowed time to complete.

## `unsupported_surface`

An API is called from an incompatible surface. A surface may be incompatible with an API for technical reasons or to avoid a confusing user experience.

**Example:** An app tries to [open a font picker](https://www.canva.dev/docs/apps/creating-text/) from an [image overlay](https://www.canva.dev/docs/apps/creating-image-overlays/).

## `user_offline`

The user is offline.

**Example:** The user tries to authenticate without being connected to the internet.
