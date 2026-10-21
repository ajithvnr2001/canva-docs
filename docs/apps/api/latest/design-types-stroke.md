---
url: https://www.canva.dev/docs/apps/api/latest/design-types-stroke/
title: Stroke - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:55.148466+00:00
---

# Stroke - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/latest/design-types-stroke/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Stroke

API reference for the Stroke type.

Copy page

Represents an outline, such as the border of an element.

## Properties

`weight``number`

RequiredView type definition

The weight (thickness) of the stroke.

**Minimum** : `0`

**Maximum** : `100`

`colorContainer``object`Read-only

RequiredView type definition

The color of the stroke.

`ref``ColorFill`

RequiredView type definition

SolidFillSolidFill

UnsupportedUnsupported

A solid color that fills an interior.

`type``string`Read-only

RequiredView type definition

The type of color.

The only valid value is `"solid"`.

`color``string`

RequiredView type definition

The color of the fill. This must be a valid, six-digit hex code, prefixed with a `#` symbol.

  * Must be six characters long.
  * Must start with a `#`.
  * Must use lowercase letters.



**Example**
    
    
     "#ff0099"

TS

Copy

Represents design content that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`set``function`

RequiredView type definition

**Parameters**

`state``SolidFillState`

RequiredView type definition

A state that creates a solid color fill.

Properties of **state**

`type``string`Read-only

RequiredView type definition

The type of color.

The only valid value is `"solid"`.

`color``string`

RequiredView type definition

The color of the fill. This must be a valid, six-digit hex code, prefixed with a `#` symbol.

  * Must be six characters long.
  * Must start with a `#`.
  * Must use lowercase letters.



**Example**
    
    
     "#ff0099"

TS

Copy

**Returns**

`void`
