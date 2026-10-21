---
url: https://www.canva.dev/docs/apps/api/preview/design-types-readable-list/
title: ReadableList - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:36.132307+00:00
---

# ReadableList - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-types-readable-list/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# ReadableList

API reference for the ReadableList type.

Copy page

A list that cannot be changed.

## Type Parameters

• **M**

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

readonly `M`[]

`forEach``function`

RequiredView type definition

Executes a function for each item in the list.

**Parameters**

`callback``ForEachCallback<M>`

RequiredView type definition

The function to run for each item.

**Parameters**

`item``M`

RequiredView type definition

The current item in the list.

**Returns**

`void`

**Returns**

`void`

`filter``function`

RequiredView type definition

TypeFilterPredicate<M, C>TypeFilterPredicate<M, C>

FilterPredicate<M>FilterPredicate<M>

Creates a new array with items that match a specific type.

**Parameters**

`filter``TypeFilterPredicate<M, C>`

RequiredView type definition

A function that checks if an item is of type `C`.

**Parameters**

`item``M`

RequiredView type definition

The item to test.

**Returns**

`true` if the item is of type `C`, otherwise `false`.

`item is C`

**Returns**

An array of items that are of type `C`.

readonly `C`[]

Creates a new array with items that pass a test.

**Parameters**

`filter``FilterPredicate<M>`

RequiredView type definition

A function that tests each item. Returns `true` to keep the item.

**Parameters**

`item``M`

RequiredView type definition

The item to test.

**Returns**

`true` if the item should be included, otherwise `false`.

`boolean`

**Returns**

An array of items that passed the test.

readonly `M`[]
