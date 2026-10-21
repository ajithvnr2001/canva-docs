---
url: https://www.canva.dev/docs/apps/platform-concepts-folders/
title: Folders - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:12.051382+00:00
---

# Folders - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/platform-concepts-folders/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Folders

An introduction to folders in the Canva Developers SDK.

Copy page

Users organize their designs, assets, and other items into _folders_.

Folders are a collection of items, such as:

  * Other folders.
  * Assets, such as uploaded images, audio, and videos.
  * Designs, such as Instagram posts, Presentations, and Documents (Canva Docs).
  * Brand Templates.



When identifying folders, we recommend using the folder's `id`, which can't be changed by a user. The top level of the user's content library, [Projects⁠(opens in a new tab or window)](https://www.canva.com/help/find-designs-and-folders/), is represented in APIs as a folder with the ID `root`.

For REST API endpoints that interact with folders, see the [Folders](https://www.canva.dev/docs/apps/rest-apis/reference/folders/) API reference.
