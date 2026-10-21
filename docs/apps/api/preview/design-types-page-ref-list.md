---
url: https://www.canva.dev/docs/apps/api/preview/design-types-page-ref-list/
title: PageRefList - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:35.664292+00:00
---

# PageRefList - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-types-page-ref-list/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# PageRefList

API reference for the PageRefList type.

Copy page

A list containing the references to pages in the design.

## Methods

`count``function`

RequiredView type definition

Gets the number of items in the list.

**Returns**

The number of items.

`number`

`toArray``function`

RequiredView type definition

Converts the list to an array.

**Returns**

An array containing all items. The items are the same as in the list.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/).

`forEach``function`

RequiredView type definition

Executes a function for each item in the list.

**Parameters**

`callback``ForEachCallback<PageRef>`

RequiredView type definition

The function to run for each item.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/).

**Parameters**

`item``PageRef`

RequiredView type definition

The current item in the list.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/).

**Returns**

`void`

**Returns**

`void`

`filter``function`

RequiredView type definition

TypeFilterPredicate<PageRef, C>TypeFilterPredicate<PageRef, C>

FilterPredicate<PageRef>FilterPredicate<PageRef>

Creates a new array with items that match a specific type.

**Parameters**

`filter``TypeFilterPredicate<PageRef, C>`

RequiredView type definition

A function that checks if an item is of type `C`.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/).

**Parameters**

`item``PageRef`

RequiredView type definition

The item to test.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/).

**Returns**

`true` if the item is of type `C`, otherwise `false`.

`item is C`

**Returns**

An array of items that are of type `C`.

readonly `C`[]

Creates a new array with items that pass a test.

**Parameters**

`filter``FilterPredicate<PageRef>`

RequiredView type definition

A function that tests each item. Returns `true` to keep the item.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/).

**Parameters**

`item``PageRef`

RequiredView type definition

The item to test.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/).

**Returns**

`true` if the item should be included, otherwise `false`.

`boolean`

**Returns**

An array of items that passed the test.

For more information, see [PageRef](https://www.canva.dev/docs/apps/api/preview/design-types-page-ref/).
