---
url: https://www.canva.dev/docs/apps/api/preview/design-types-absolute-page/
title: AbsolutePage - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T14:42:16.335768+00:00
---

# AbsolutePage - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-types-absolute-page/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# AbsolutePage

API reference for the AbsolutePage type.

Copy page

A page with either fixed or unbounded dimensions.

## Properties

`type``string`Read-only

RequiredView type definition

The type of page.

`id``PageId`Read-only

RequiredView type definition

Stable identifier for this page within the design.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the page is locked and cannot be modified.

`dimensions``Dimensions | undefined`Read-only

RequiredView type definition

The dimensions of the page. `dimensions` is undefined for whiteboard pages.

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`background``Fill | undefined`Read-only

RequiredView type definition

The background of the page. `background` is undefined for whiteboard pages.

For more information, see [Fill](https://www.canva.dev/docs/apps/api/preview/design-types-fill/).

`elements``ElementList`Read-only

RequiredView type definition

The elements on the page.

For more information, see [ElementList](https://www.canva.dev/docs/apps/api/preview/design-types-element-list/).
