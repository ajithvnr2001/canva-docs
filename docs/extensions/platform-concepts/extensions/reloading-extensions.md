---
url: https://www.canva.dev/docs/extensions/platform-concepts/extensions/reloading-extensions/
title: Reloading extensions - Extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:59:00.346986+00:00
---

# Reloading extensions - Extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/platform-concepts/extensions/reloading-extensions/

Extensions

[Overview](https://www.canva.dev/docs/extensions/platform-concepts/extensions/)[Reloading extensions](https://www.canva.dev/docs/extensions/platform-concepts/extensions/reloading-extensions/)

# Reloading extensions

How to reload extensions within the Canva editor.

Copy page

When an app is in the **Draft** state, Canva displays buttons in the editor for reloading the app's extensions. You can click these buttons to preview changes to extensions without reloading the entire page. For example, reloading a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/) sends a request to the [`/content/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/) endpoint.

The reload button appears in a different location for each extension point.

## Content extensions

The **Reload resources** button for content extensions appears in the side panel.

![](https://www.canva.dev/_next/static/media/img-f3d71074e0.bdd6d32a.jpg)

Reloading a content extension only reloads the content, not the extension's configuration. For example, if you change the **Layout** of a content extension, you need to reload the editor to preview the change.

## Publish extensions

The **Reload extension configuration** button for publish extensions appears in the **Publish** menu.

![](https://www.canva.dev/_next/static/media/img-de5c85af96.31877761.jpg)
