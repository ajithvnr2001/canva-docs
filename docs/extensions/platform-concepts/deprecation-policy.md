---
url: https://www.canva.dev/docs/extensions/platform-concepts/deprecation-policy/
title: Deprecation policy - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:42.723447+00:00
---

# Deprecation policy - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/platform-concepts/deprecation-policy/

App Development

[Overview](https://www.canva.dev/docs/extensions/)[Quickstart](https://www.canva.dev/docs/extensions/quickstart/)[Changelog](https://www.canva.dev/docs/extensions/changelog/)

Platform concepts

Apps

Extensions

[Regions](https://www.canva.dev/docs/extensions/platform-concepts/regions/)[Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/)[Deprecation policy](https://www.canva.dev/docs/extensions/platform-concepts/deprecation-policy/)

Extensions

Content extensions

Publish extensions

Backend development

Base URL

[Continuation](https://www.canva.dev/docs/extensions/backend-development/continuation/)

Signature verification

SDKs

Distribution

UX guidelines

[Submission checklist](https://www.canva.dev/docs/extensions/distribution/submission-checklist/)[Creating the App Directory listing](https://www.canva.dev/docs/extensions/distribution/app-directory-listing/)

Server API

[Overview](https://www.canva.dev/docs/extensions/server-api/server-api/)[GET /apps/configured](https://www.canva.dev/docs/extensions/server-api/get-apps-configured/)[POST /configuration](https://www.canva.dev/docs/extensions/server-api/post-configuration/)[POST /configuration/delete](https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/)[POST /content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/)[POST /publish/resources/find](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/)[POST /publish/resources/get](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/)[POST /publish/resources/upload](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/)[Redirect URL](https://www.canva.dev/docs/extensions/server-api/redirect-url/)

Reference

[Languages](https://www.canva.dev/docs/extensions/reference/supported-languages/)

# Deprecation policy

Copy page

Canva's app development platform is constantly evolving. For the most part, these changes are backwards compatible and don't require changes to existing apps. To ensure the growth of the platform though, it's sometimes necessary to deprecate some of the platform's APIs.

This topic describes the deprecation policy for Canva's app development platform and our efforts to minimize the disruption to our developer community.

Canva's app development platform is in open beta and this deprecation policy, along with the rest of our platform, is subject to change.

## TL;DR

  * The deprecation policy only applies to the public, stable version of Canva's APIs.
  * When a feature is deprecated, it remains available for at least a further 6 months.
  * Canva communicates feature deprecations at multiple points in time, via multiple channels.
  * There may be exceptions to this policy, such as security issues.



## Applicability

Canva's deprecation policy only applies to the public, stable version of Canva's APIs. This means APIs that are private or unstable — for example, the beta or alpha version of APIs — are not subject to the policy.

## Deprecation period

The _deprecation period_ defines the minimum amount of time a feature remains active after it has been deprecated.

The deprecation period for Canva's app development APIs is 6 months. This means, if a feature is deprecated, it remains available for at least 6 months. After 6 months, Canva expects apps to use the stable APIs.

Deprecated features are eventually made obsolete and removed from the API.

## Communicating changes

Canva notifies developers about deprecated features via email, including when a feature is deprecated and once a feature has been made obsolete. Canva also shows deprecation alerts via the Developer Portal and throughout the documentation.

## Breaking vs. non-breaking changes

Most changes to Canva's APIs are non-breaking, meaning they're backwards compatible and don't require changes to existing apps. The terms "breaking" and "non-breaking" are somewhat subjective though, so this section describes how Canva defines these terms.

### Breaking changes

A breaking (backwards incompatible) change requires action from a developer to ensure the ongoing functioning of their app.

These are some examples of breaking changes:

  * Adding required methods or endpoints
  * Removing existing methods, endpoints, or properties
  * Renaming existing methods, endpoints, or properties
  * Changing the data type of existing properties
  * Changing the shape of existing methods in a way that isn't backwards compatible
  * Adding required properties to existing responses
  * Removing values from an enum
  * Adding required fields or options to the Developer Portal



### Non-breaking changes

A non-breaking (backwards compatible) change doesn't require action from a developer to ensure the ongoing functioning of their app.

These are some examples of non-breaking changes:

  * Adding properties to existing requests
  * Adding optional methods, endpoints, or properties
  * Adding values to an enum
  * Changing the order of properties
  * Changing the length or format of opaque strings, such as IDs
  * Adding optional fields or options to the Developer Portal



## Handling exceptions

Canva is committed to having a stable deprecation policy that developers can rely on, but any sensible policy must be open to exceptions.

For example, if a security issue is discovered and an immediate, breaking change is required, the deprecation period for that change will not be observed.

This is not a decision that would be made lightly and Canva will make all reasonable efforts to avoid unexpected disruptions to developers and their apps.
