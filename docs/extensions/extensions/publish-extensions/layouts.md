---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/
title: Layouts - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:52.779264+00:00
---

# Layouts - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Layouts

Choose a layout for a publish extension.

Copy page

When creating a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/), the first decision you need to make is what _layout_ you want to use for the extension.

The layout of a publish extension determines:

  * The user experience of the extension.
  * The features the extension can support.
  * The time and effort required to develop the extension.



This guide provides an overview of the different layouts and when to use them. Refer to the linked tutorials to learn about the work required to support each layout.

## Basic layout

When a user opens a publish extension that uses the **Basic** layout, they see a handful of options and a **Save** button. The available options depend on how the extension is configured and aren't dependent on the layout.

![](https://www.canva.dev/_next/static/media/img-26a647ee9c.4d776e0e.png)

When the user clicks the **Save** button, Canva uploads their design to the destination platform.

The **Basic** layout is ideal for platforms that don't organize content into folders, such as social media platforms with a single feed for each user (for example, Twitter or Instagram).

To learn how to create a publish extension that uses the **Basic** layout, refer to [Create a publish extension with the "Basic" layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/).

## Flat list layout

When a user opens a publish extension that uses the **Flat list** layout, they see a list of folders. The user must select a folder to proceed.

![](https://www.canva.dev/_next/static/media/img-4ed7354914.9d335fc4.png)

After selecting a folder, the user sees a handful of options and a **Save** button. The available options depend on how the extension is configured and aren't dependent on the layout.

When the user clicks the **Save** button, Canva uploads their design to the destination platform. Canva includes the ID of the selected folder in the upload request, which the platform can use to ensure the design is uploaded to the relevant location.

The **Flat list** layout is ideal for platforms that:

  * Require users to put content into folders.
  * Don't support nested folders.



To learn how to create a publish extension that uses the **Flat list** layout, refer to [Create a publish extension with the "Flat list" layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/).

## Nested list layout

When a user opens a publish extension that uses the **Nested list** layout, they see a list of files and folders.

![](https://www.canva.dev/_next/static/media/img-0b77524971.ca7f4dfd.png)

The user can select a folder to open it, revealing more files and folders.

![](https://www.canva.dev/_next/static/media/img-cc58de86f2.119df742.png)

At any level in the hierarchy, the user can click the **Choose** button. This indicates that they want to publish their design to the current folder.

After the user chooses a folder, they see a handful of options and a **Save** button. The available options depend on how the extension is configured and aren't dependent on the layout.

When the user clicks the **Save** button, Canva uploads their design to the destination platform. Canva includes the ID of the selected folder in the upload request, which the platform can use to ensure the design is uploaded to the relevant location.

If the user opens a folder that doesn't contain any additional folders, they're immediately taken to the screen with the **Save** button.

The **Nested list** layout is ideal for platforms that:

  * Let users organize content into folders.
  * Support nested folders.



To learn how to create a publish extension that uses the **Nested list** layout, refer to [Create a publish extension with the "Nested list" layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/).
