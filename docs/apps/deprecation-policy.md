---
url: https://www.canva.dev/docs/apps/deprecation-policy/
title: Deprecation policy - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:34.130665+00:00
---

# Deprecation policy - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/deprecation-policy/

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

# Deprecation policy

How we deprecate features in the Canva Developers SDK.

Copy page

The Canva Developers SDK is constantly evolving. We try to make changes in backwards compatible ways, but sometimes it's necessary to deprecate existing features in order to improve the platform.

This page describes everything you need to know about how we handle deprecation.

## TL;DR

  * This deprecation policy only applies to the public, stable version of the Developers SDK.
  * When a feature is deprecated, it remains available for at least a further 6 months.
  * Canva communicates deprecations at multiple points in time, via multiple channels.
  * There may be exceptions to this policy, like in the case of security incidents.



## Applicability

This deprecation policy applies to the public, stable version of the Developers SDK.

If an app uses private or unstable APIs, such as those released in beta, breaking changes may occur at any moment and without warning. You should not rely on unstable APIs remaining the same.

## Deprecation period

The deprecation period for the Developers SDK is 6 months.

Once a feature has been deprecated, it will remain available for at least 6 months. When the deprecation period ends, the feature may be removed from the Developers SDK at any point in time.

## Communication

Developers are notified when features are deprecated and when they're made obsolete. This communication happens via a number of channels, including but not limited to:

  * An email sent directly to the developer.
  * An announcement in the [developer community⁠(opens in a new tab or window)](https://community.canva.dev/top?period=quarterly).
  * Alerts in the documentation and [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers).



## Breaking vs. non-breaking changes

There isn't a universal definition of what constitutes a breaking versus non-breaking change. This section explains how Canva defines these terms for apps inside Canva, and for the Canva REST APIs.

### Apps inside Canva

For apps inside Canva, these terms are defined in terms of the SDK's methods and types.

A breaking change is one that's backward incompatible, meaning that it either alters or removes an existing API. Some examples of breaking changes include:

  * Adding required properties to methods.
  * Renaming methods or types.
  * Removing values from enums.



When a breaking change is made, the developer must update their app by the end of the deprecation period.

A non-breaking change is one that's backward compatible. Some examples of non-breaking changes include:

  * Adding methods to the SDK.
  * Adding optional properties to methods.
  * Adding values to enums.



When a non-breaking change is made, the developer is not required to update their app.

### Canva REST APIs

For the Canva REST APIs, these terms are defined in terms of requests and responses. A breaking change requires the release of a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/), whereas a non-breaking change doesn't.

The following are considered breaking changes:

  * Changing the required scopes for an API.
  * Adding a required request parameter.
  * Changing a request parameter from optional to required.
  * Changing the default value of a request parameter.
  * Updating an optional query or search parameter.
  * Removing an enumerated value from a request parameter.
  * Removing a request parameter.
  * Changing a validation rule for request parameters or response properties.
  * Adding an enumerated value to a response property.
  * Changing a response property from required to optional.
  * Changing response property behavior. For example, changing the meaning or structure of a property's value.
  * Removing a response property.
  * Changing a REST API behavior in a way that isn't backwards compatible. For example, changing the way uploads are processed, or how quality settings are applied.
  * Changing the HTTP response status code for an API.



The following are considered non-breaking changes:

  * Adding an optional request parameter.
  * Adding an enumerated value to a request parameter.
  * Changing a request parameter from required to optional.
  * Adding a response property.
  * Changing a response property from optional to required.
  * Removing an enumerated value from a response property.



## Exceptions

Canva is committed to having a stable deprecation policy that developers can rely upon, but there are exceptions that need to be accounted for.

For example, if a security issue is discovered and a breaking change is required to fix it, the deprecation period for that change will not be observed. We will, however:

  * Communicate the change as quickly as possible.
  * Provide resources to help minimize disruption, such as a migration guide.



We do not make exceptions lightly. They're reserved for truly exceptional circumstances.

## Tips & tricks

When a feature is deprecated, here's what we recommend:

  * Upgrade the app as soon as possible. To help make this process painless, we always provide migration guides, support via the developer community, and support via our ticketing system.
  * Don't submit apps that use deprecated APIs. We won't automatically reject apps that do this, but it's easier to upgrade the app as part of the same submission.


