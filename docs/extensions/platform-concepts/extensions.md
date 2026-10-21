---
url: https://www.canva.dev/docs/extensions/platform-concepts/extensions/
title: Extensions - Extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:46.756742+00:00
---

# Extensions - Extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/platform-concepts/extensions/

Extensions

[Overview](https://www.canva.dev/docs/extensions/platform-concepts/extensions/)[Reloading extensions](https://www.canva.dev/docs/extensions/platform-concepts/extensions/reloading-extensions/)

# Extensions

What are extensions? What can they do?

Copy page

For an app to do something, it must have one or more _extensions_. An extension is what allows an app to hook into and extend the behavior of the Canva editor. For example, a publish extension adds a publish destination to the **Publish** menu.

You can think of an extension as a feature or a capability of your app.

## Types of extensions

You can add the following types of extensions to an app:

  * [Content](https://www.canva.dev/docs/extensions/extensions/content-extensions/)
  * [Publish](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)



Each type of extension — or _extension points_ , as they're also known — adds distinct behavior to your app and requires a different sequence of steps to get it up and running.

To learn more about each extension point, see the linked documentation.

## Creating extensions

You can add extensions to an app via the Developer Portal.

Developing the extension requires a combination of configuration, which is handled via the Developer Portal, and server-side development.

## Supporting multiple extensions

Apps can have more than one extension. Typically, this feature is used to let users consume and publish content from a single app. For example, the Dropbox app has a content and a publish extension, which means the user can connect and authenticate with one app to get their content in or out of Canva.

Apps can't have more than one extension of the same type. For example, an app can't have multiple content extensions. This is because each extension is surfaced in a certain part of the Canva editor and one app surfacing multiple extensions in the same place would be a confusing user experience.
