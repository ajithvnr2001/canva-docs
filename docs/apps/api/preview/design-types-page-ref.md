---
url: https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/
title: PageRef - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:57.725804+00:00
---

# PageRef - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# PageRef

API reference for the PageRef type.

Copy page

A reference to a page.

## Type declaration

AbsolutePageRefAbsolutePageRef

UnsupportedUnsupported

A reference to an `absolute` type page.

`type``string`Read-only

RequiredView type definition

The type of page.

The only valid value is `"absolute"`.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the page is locked and cannot be modified.

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.
