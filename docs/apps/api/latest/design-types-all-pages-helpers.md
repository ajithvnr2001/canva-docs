---
url: https://www.canva.dev/docs/apps/api/latest/design-types-all-pages-helpers/
title: AllPagesHelpers - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:50.905419+00:00
---

# AllPagesHelpers - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/latest/design-types-all-pages-helpers/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# AllPagesHelpers

API reference for the AllPagesHelpers type.

Copy page

Helpers for use when reading all pages of the design.

## Methods

`openPage``function`

RequiredView type definition

AbsolutePageRefAbsolutePageRef

UnsupportedUnsupported

PageRefPageRef

Reads (and optionally updates) a page of the user's design.

**Parameters**

`pageRef``AbsolutePageRef`

RequiredView type definition

Reference to the page to be read.

Properties of **pageRef**

`type``string`Read-only

RequiredView type definition

The type of page.

The only valid value is `"absolute"`.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the page is locked and cannot be modified.

`callback``DesignOpenPageCallback<AbsolutePage>`

RequiredView type definition

A callback for operating on the page of the design.

For more information, see [AbsolutePage](https://www.canva.dev/docs/apps/api/latest/design-types-absolute-page/).

**Parameters**

`response``DesignEditing.OpenPageResult<AbsolutePage>`

RequiredView type definition

Result received by the `openPage` callback.

Properties of **response**

`page``DesignEditing.Page`

RequiredView type definition

The page of the design.

AbsolutePageAbsolutePage

UnsupportedUnsupported

A page with either fixed or unbounded dimensions.

For more information, see [AbsolutePage](https://www.canva.dev/docs/apps/api/latest/design-types-absolute-page/).

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`helpers``PageHelpers`

RequiredView type definition

These are various utilities that allow apps to do more complex operations on the page.

For more information, see [PageHelpers](https://www.canva.dev/docs/apps/api/latest/design-types-page-helpers/).

**Returns**

`Promise<void>`

**Returns**

A response indicating whether the callback was executed. This is a `Promise` that resolves with the following object:

OpenPageCallbackExecutedOpenPageCallbackExecuted

OpenPageCallbackSkippedOpenPageCallbackSkipped

The response from `openPage` if the callback was executed.

`status``string`

View type definition

The only valid value is `"executed"`.

The response from `openPage` if the callback was not executed.

`status``string`

View type definition

The only valid value is `"skipped"`.

`reason``string`

View type definition

Reason that the callback was not executed.

**Parameters**

`pageRef``Unsupported`

RequiredView type definition

Represents design content that the SDK doesn't support.

Properties of **pageRef**

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`callback``DesignOpenPageCallback<Unsupported>`

RequiredView type definition

A callback for operating on a page of the design.

**Parameters**

`response``DesignEditing.OpenPageResult<Unsupported>`

RequiredView type definition

Result received by the `openPage` callback.

Properties of **response**

`page``DesignEditing.Page`

RequiredView type definition

The page of the design.

AbsolutePageAbsolutePage

UnsupportedUnsupported

A page with either fixed or unbounded dimensions.

For more information, see [AbsolutePage](https://www.canva.dev/docs/apps/api/latest/design-types-absolute-page/).

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`helpers``PageHelpers`

RequiredView type definition

These are various utilities that allow apps to do more complex operations on the page.

For more information, see [PageHelpers](https://www.canva.dev/docs/apps/api/latest/design-types-page-helpers/).

**Returns**

`Promise<void>`

**Returns**

The response from `openPage` indicating whether the callback was executed. This is a `Promise` that resolves with the following object:

OpenPageCallbackExecutedOpenPageCallbackExecuted

OpenPageCallbackSkippedOpenPageCallbackSkipped

The response from `openPage` if the callback was executed.

`status``string`

View type definition

The only valid value is `"executed"`.

The response from `openPage` if the callback was not executed.

`status``string`

View type definition

The only valid value is `"skipped"`.

`reason``string`

View type definition

Reason that the callback was not executed.

**Parameters**

`pageRef``PageRef`

RequiredView type definition

A reference to a page.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/latest/design-types-page-ref/).

`callback``DesignOpenPageCallback`

RequiredView type definition

A callback for operating on a page of the design.

**Parameters**

`response``DesignEditing.OpenPageResult<DesignEditing.Page>`

RequiredView type definition

Result received by the `openPage` callback.

Properties of **response**

`page``DesignEditing.Page`

RequiredView type definition

The page of the design.

AbsolutePageAbsolutePage

UnsupportedUnsupported

A page with either fixed or unbounded dimensions.

For more information, see [AbsolutePage](https://www.canva.dev/docs/apps/api/latest/design-types-absolute-page/).

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`helpers``PageHelpers`

RequiredView type definition

These are various utilities that allow apps to do more complex operations on the page.

For more information, see [PageHelpers](https://www.canva.dev/docs/apps/api/latest/design-types-page-helpers/).

**Returns**

`Promise<void>`

**Returns**

The response from `openPage` indicating whether the callback was executed. This is a `Promise` that resolves with the following object:

OpenPageCallbackExecutedOpenPageCallbackExecuted

OpenPageCallbackSkippedOpenPageCallbackSkipped

The response from `openPage` if the callback was executed.

`status``string`

View type definition

The only valid value is `"executed"`.

The response from `openPage` if the callback was not executed.

`status``string`

View type definition

The only valid value is `"skipped"`.

`reason``string`

View type definition

Reason that the callback was not executed.
