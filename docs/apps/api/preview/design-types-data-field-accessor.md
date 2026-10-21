---
url: https://www.canva.dev/docs/apps/api/preview/design-types-data-field-accessor/
title: DataFieldAccessor - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:13.402883+00:00
---

# DataFieldAccessor - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-types-data-field-accessor/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# DataFieldAccessor

API reference for the DataFieldAccessor type.

Copy page

**This API is a preview**. Preview APIs are unstable and may change without warning. You can't release public apps using this API until it's stable.

Reads and updates the data-field mapping of a single target — obtained from [DesignEditing.PageHelpers.getDataFieldFor](https://www.canva.dev/docs/apps/api/preview/design-types-page-helpers/).

Updates the data-field mapping and the dataset definition. Supported targets are text (connected to a field of type `text`) and fills (connected to a field of type `fill`).

When `label` is present:

  * If a field with the same label already exists in the dataset definition and its type is compatible with the target type, the target is connected to that existing field.
  * If a field with the same label exists but has a different type, `set` resolves to `{ status: "incompatible_data_field_type" }`.
  * If no compatible field exists and the dataset definition has reached the field limit, `set` resolves to `{ status: "data_field_limit_exceeded" }`.
  * Otherwise a new field is added to the dataset definition with a randomly generated id. The field type is inferred from the target type, and the target is connected to it.



When `label` is Unset:

  * The data-field mapping is removed from the target.
  * The dataset definition is not cleaned up; unused fields are left in place. Unused fields continue to count toward the document's data-field limit and may be reused by later calls to `set`.



Developer mistakes, such as unsupported targets or invalid fill/parent combinations, throw `CanvaError({ code: "bad_request" })`.

`getDesignMetadata()` only returns committed data fields. Fields staged during the current `openDesign` transaction are not visible through `getDesignMetadata()` until `sync()` commits the changes.

## Methods

`get``function`

RequiredView type definition

Returns the label of the data field the target is currently connected to, or `undefined` if the target is not connected to any data field.

**Returns**

`string | undefined`

`set``function`

RequiredView type definition

Stages a change to the target's data-field mapping. The change is committed when the app calls `session.sync()`.

**Parameters**

`opts``DataFieldSetOptions`

Required

View type definition

Options for [DataFieldAccessor.set](https://www.canva.dev/docs/apps/api/preview/design-types-data-field-accessor/).

Properties of **opts**

`label``object`

RequiredView type definition

The label of the data field to connect the target to, or Unset to remove the target's mapping.

When a string, the target is connected to a field with this label, creating the field if it does not exist. The field type is inferred from the target: text targets use `text` fields and fill targets use `fill` fields.

DataFieldLabel

DataFieldLabel

objectobject

The human-readable label of a data field, for example `"Product name"`. Canva uses the label as the field's identifier within the document's dataset definition.

_typeof_

**Returns**

The result of [DataFieldAccessor.set](https://www.canva.dev/docs/apps/api/preview/design-types-data-field-accessor/). This is a `Promise` that resolves with the following object:

DataFieldAccessorSetResultCompleted

DataFieldAccessorSetResultCompleted

DataFieldAccessorSetResultError

DataFieldAccessorSetResultError

Returned by [DataFieldAccessor.set](https://www.canva.dev/docs/apps/api/preview/design-types-data-field-accessor/) when the change was staged successfully.

`status``string`

View type definition

The only valid value is `"completed"`.

Returned by [DataFieldAccessor.set](https://www.canva.dev/docs/apps/api/preview/design-types-data-field-accessor/) when the change could not be staged.

  * **`data_field_limit_exceeded`** — staging a new field would exceed the dataset field limit.
  * **`incompatible_data_field_type`** — a field with the same label already exists in the dataset definition with a type that is incompatible with the target.



`status``string`

View type definition

**Available values** :

  * `"data_field_limit_exceeded"`
  * `"incompatible_data_field_type"`


