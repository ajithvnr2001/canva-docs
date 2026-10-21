---
url: https://www.canva.dev/docs/apps/api/latest/design-types-list-state/
title: ListState - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:53.984572+00:00
---

# ListState - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/latest/design-types-list-state/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# ListState

API reference for the ListState type.

Copy page

A list of items that can be read.

## Type Parameters

• **T**

## Indexable
    
    
    [n: number]: T

TS

Copy

## Properties

`length``number`Read-only

RequiredView type definition

## Methods

`join``function`

RequiredView type definition

**Parameters**

`separator``string`

OptionalView type definition

**Returns**

`string`

`slice``function`

RequiredView type definition

**Parameters**

`start``number`

OptionalView type definition

`end``number`

OptionalView type definition

**Returns**

A list of items that can be read and updated.

`length``number`

View type definition

`pop``function`

View type definition

**Returns**

`T | undefined`

`push``function`

View type definition

**Parameters**

`items``T[]`

RequiredView type definition

**Returns**

`number`

`shift``function`

View type definition

**Returns**

`T | undefined`

`splice``function`

View type definition

splice(start, deleteCount)splice(start, deleteCount)

splice(start, deleteCount, items)splice(start, deleteCount, items)

**Parameters**

`start``number`

RequiredView type definition

`deleteCount``number`

OptionalView type definition

**Returns**

A list of items that can be read and updated.

`EditableListState<T>`

**Parameters**

`start``number`

RequiredView type definition

`deleteCount``number`

RequiredView type definition

`items``T[]`

RequiredView type definition

**Returns**

A list of items that can be read and updated.

`EditableListState<T>`

`unshift``function`

View type definition

**Parameters**

`items``T[]`

RequiredView type definition

**Returns**

`number`

For more information, see [ListState](https://www.canva.dev/docs/apps/api/latest/design-types-list-state/).

`indexOf``function`

RequiredView type definition

**Parameters**

`searchElement``T`

RequiredView type definition

`fromIndex``number`

OptionalView type definition

**Returns**

`number`

`lastIndexOf``function`

RequiredView type definition

**Parameters**

`searchElement``T`

RequiredView type definition

`fromIndex``number`

OptionalView type definition

**Returns**

`number`

`every``function`

RequiredView type definition

every(predicate) 1every(predicate) 1

every(predicate) 2every(predicate) 2

**Parameters**

`predicate``function`

RequiredView type definition

**Parameters**

`value``T`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`value is S`

**Returns**

`this is ListState<S>`

**Parameters**

`predicate``function`

RequiredView type definition

**Parameters**

`value``T`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`unknown`

**Returns**

`boolean`

`some``function`

RequiredView type definition

**Parameters**

`predicate``function`

RequiredView type definition

**Parameters**

`value``T`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`unknown`

**Returns**

`boolean`

`forEach``function`

RequiredView type definition

**Parameters**

`callbackFn``function`

RequiredView type definition

**Parameters**

`value``T`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`void`

**Returns**

`void`

`map``function`

RequiredView type definition

**Parameters**

`callbackFn``function`

RequiredView type definition

**Parameters**

`value``T`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`U`

**Returns**

A list of items that can be read and updated.

`length``number`

View type definition

`pop``function`

View type definition

**Returns**

`T | undefined`

`push``function`

View type definition

**Parameters**

`items``T[]`

RequiredView type definition

**Returns**

`number`

`shift``function`

View type definition

**Returns**

`T | undefined`

`splice``function`

View type definition

splice(start, deleteCount)splice(start, deleteCount)

splice(start, deleteCount, items)splice(start, deleteCount, items)

**Parameters**

`start``number`

RequiredView type definition

`deleteCount``number`

OptionalView type definition

**Returns**

A list of items that can be read and updated.

`EditableListState<T>`

**Parameters**

`start``number`

RequiredView type definition

`deleteCount``number`

RequiredView type definition

`items``T[]`

RequiredView type definition

**Returns**

A list of items that can be read and updated.

`EditableListState<T>`

`unshift``function`

View type definition

**Parameters**

`items``T[]`

RequiredView type definition

**Returns**

`number`

For more information, see [ListState](https://www.canva.dev/docs/apps/api/latest/design-types-list-state/).

`filter``function`

RequiredView type definition

filter(predicate) 1filter(predicate) 1

filter(predicate) 2filter(predicate) 2

**Parameters**

`predicate``function`

RequiredView type definition

**Parameters**

`value``T`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`value is S`

**Returns**

`S`[]

**Parameters**

`predicate``function`

RequiredView type definition

**Parameters**

`value``T`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`unknown`

**Returns**

`T`[]

`reduce``function`

RequiredView type definition

reduce(callbackFn, initialValue) 1reduce(callbackFn, initialValue) 1

reduce(callbackFn, initialValue) 2reduce(callbackFn, initialValue) 2

**Parameters**

`callbackFn``function`

RequiredView type definition

**Parameters**

`previousValue``T`

RequiredView type definition

`currentValue``T`

RequiredView type definition

`currentIndex``number`

RequiredView type definition

**Returns**

`T`

`initialValue``T`

OptionalView type definition

**Returns**

`T`

**Parameters**

`callbackFn``function`

RequiredView type definition

**Parameters**

`previousValue``U`

RequiredView type definition

`currentValue``T`

RequiredView type definition

`currentIndex``number`

RequiredView type definition

**Returns**

`U`

`initialValue``U`

RequiredView type definition

**Returns**

`U`

`reduceRight``function`

RequiredView type definition

reduceRight(callbackFn, initialValue) 1reduceRight(callbackFn, initialValue) 1

reduceRight(callbackFn, initialValue) 2reduceRight(callbackFn, initialValue) 2

**Parameters**

`callbackFn``function`

RequiredView type definition

**Parameters**

`previousValue``T`

RequiredView type definition

`currentValue``T`

RequiredView type definition

`currentIndex``number`

RequiredView type definition

**Returns**

`T`

`initialValue``T`

OptionalView type definition

**Returns**

`T`

**Parameters**

`callbackFn``function`

RequiredView type definition

**Parameters**

`previousValue``U`

RequiredView type definition

`currentValue``T`

RequiredView type definition

`currentIndex``number`

RequiredView type definition

**Returns**

`U`

`initialValue``U`

RequiredView type definition

**Returns**

`U`

`find``function`

RequiredView type definition

find(predicate) 1find(predicate) 1

find(predicate) 2find(predicate) 2

**Parameters**

`predicate``function`

RequiredView type definition

**Parameters**

`value``T | undefined`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`value is S`

**Returns**

`S | undefined`

**Parameters**

`predicate``function`

RequiredView type definition

**Parameters**

`value``T | undefined`

RequiredView type definition

`index``number`

RequiredView type definition

**Returns**

`unknown`

**Returns**

`T | undefined`

`flatMap``function`

RequiredView type definition

**Parameters**

`callback``function`

RequiredView type definition

**Parameters**

`value``T`

RequiredView type definition

`index``number`

RequiredView type definition

`array``T[]`

RequiredView type definition

**Returns**

UU

U[]U[]

**Returns**

`U`[]

`at``function`

RequiredView type definition

**Parameters**

`index``number`

RequiredView type definition

**Returns**

`T | undefined`
