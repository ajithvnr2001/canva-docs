---
url: https://www.canva.dev/docs/apps/setting-up-starter-kit/
title: Starter kit - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:42.995074+00:00
---

# Starter kit - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/setting-up-starter-kit/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Starter kit

The starter kits for building with the Canva Developers SDK.

Copy page

A starter kit is a GitHub repository that contains the boilerplate of a working app, along with the tooling that Canva recommends for building one. Cloning a starter kit is the quickest route to a running app, and the documentation assumes that you're using the kit for the surface you're building for.

There is one starter kit per surface. To clone, configure, and run either of them, see [Quickstart](https://www.canva.dev/docs/apps/quickstart/) and choose your surface.

The starter kits for apps inside Canva (previously known as the Apps SDK) and the Canva REST APIs (previously known as the Connect APIs) are being combined in a future update. The steps here continue to work until that happens, and will be updated in the future.

## Apps inside Canva

The [starter kit for apps inside Canva⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-apps-sdk-starter-kit) includes:

  * An app's boilerplate, with `src/app.tsx` as its entry point.
  * The [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/), so that your app matches the look and feel of Canva.
  * [TypeScript⁠(opens in a new tab or window)](https://www.typescriptlang.org/), [React⁠(opens in a new tab or window)](https://react.dev/), and [`@canva/app-scripts`](https://www.canva.dev/docs/apps/canva-app-scripts/).
  * An `examples` directory of usage examples for the APIs.
  * [An example backend⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/tree/main/utils/backend), built with Express.js, that some of the examples rely on.



The kit also simplifies [generating the JavaScript bundle](https://www.canva.dev/docs/apps/bundling-apps/) that you upload to Canva.

## Canva for your platform

The [starter kit for the Canva REST APIs⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-connect-api-starter-kit) includes:

  * A React-based e-commerce web app.
  * An Express.js backend with a mock product database.
  * A working REST API client.
  * A working authentication flow.



The [reference apps](https://www.canva.dev/docs/apps/reference-apps/) are built from this kit's demos.
