---
url: https://www.canva.dev/docs/apps/designs/
title: Designs - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:39.561119+00:00
---

# Designs - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/designs/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Designs

An introduction to designs in the Canva Developers SDK.

Copy page

In Canva, users can create _designs_. These designs are made out of pages, and those pages contain various ingredients, such as [image](https://www.canva.dev/docs/apps/creating-images/) elements and [text](https://www.canva.dev/docs/apps/creating-text/) content.

A design is anything you create in Canva, including:

  * [Documents⁠(opens in a new tab or window)](https://www.canva.com/docs/)
  * [Presentations⁠(opens in a new tab or window)](https://www.canva.com/presentations/)
  * [Print products⁠(opens in a new tab or window)](https://www.canva.com/print/), such as T-shirts, mugs, and business cards
  * [Social media content⁠(opens in a new tab or window)](https://www.canva.com/social-media/), such as Instagram posts
  * [Videos⁠(opens in a new tab or window)](https://www.canva.com/video-editor/)
  * [Websites⁠(opens in a new tab or window)](https://www.canva.com/website-builder/)
  * [Whiteboards⁠(opens in a new tab or window)](https://www.canva.com/whiteboards/)



This doesn't include elements within a design, such as:

  * Images and videos uploaded by a user.
  * Built-in elements, such as shapes and stock images.



Most Canva designs are between 40 × 40 pixels and 8,000 × 8,000 pixels and can have multiple pages, with exceptions for some design types, such as Documents (unlimited length) and Whiteboards (unlimited width and height).

## Design types

Canva supports a range of _design types_ , each of which is intended for specific use-cases. For example, there's a design type for Instagram posts and a design type for postcards.

The design types themselves fall into the following categories, which determine how an app adds content to a design:

  * _Fixed design types_ , which use a coordinate-based positioning system, where an app adds an element at a specific point on a page. This is the most common category of design type, and includes presentations, posters, and social media posts.
  * _Responsive design types_ , which use a text-based flow, where an app slots an element into a stream of content. Canva docs are the only responsive design type.



These categories describe how content is positioned, not how large a design can be. Some design types are unbounded, meaning their pages have no set width and height, so methods such as [getCurrentPageContext](https://www.canva.dev/docs/apps/api/latest/design-get-current-page-context/) return no dimensions for them.

Apps inside Canva are compatible with all design types, but some methods are only available for certain categories. We recommend designing your app to support both categories, so it works across the full range of Canva formats, such as presentations, whiteboards, docs, and emails.

Where possible, apps should determine the context in which an app is running and either call the compatible method or make it obvious when a certain feature isn't available. To learn more, see [Feature support](https://www.canva.dev/docs/apps/feature-support/).

## Design IDs

All designs have a unique ID. Apps can access this ID and use it to store information that's associated with the design — for example, to save the user's settings on a per-design basis. To learn more, see [Using design IDs](https://www.canva.dev/docs/apps/using-design-ids/).

## Interacting with designs

Apps inside Canva can interact with designs in a variety of ways, such as by:

  * [Adding elements to designs](https://www.canva.dev/docs/apps/elements/)
  * [Adding pages to a design](https://www.canva.dev/docs/apps/api/latest/design-add-page/)
  * [Querying content in designs](https://www.canva.dev/docs/apps/querying/)
  * [Listening for content selection](https://www.canva.dev/docs/apps/selection/)
  * [Traversing elements in designs](https://www.canva.dev/docs/apps/design-editing/)



Many REST API endpoints interact with designs. For more information, see the [Designs](https://www.canva.dev/docs/apps/rest-apis/reference/designs/), [Design import](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/), and [Design types](https://www.canva.dev/docs/apps/rest-apis/reference/design-types/) API references.
