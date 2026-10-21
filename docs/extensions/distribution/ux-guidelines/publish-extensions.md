---
url: https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/
title: UX guidelines for publish extensions - UX guidelines - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:59:00.229695+00:00
---

# UX guidelines for publish extensions - UX guidelines - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/

UX guidelines

[Overview](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/)[UX guidelines for content extensions](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/)[UX guidelines for publish extensions](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/)[Writing copy for your app](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/copy/)[Optimizing the authentication flow](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/)

# UX guidelines for publish extensions

Copy page

Canva's users love to share their content with the world. This page contains guidelines for creating [publish extensions](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) that seamlessly bridge the gap between Canva and third-party platforms.

## Choose the best layout

The [layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/) of a publish extension has a big impact on the behavior and appearance of the extension. Choosing the most appropriate layout ensures the best user experience.

![](https://www.canva.dev/_next/static/media/img-c4a07f268a.643fe3d8.svg)

### Basic layout

The [basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/#basic-layout) is for destination platforms that don't organize content into folders.

For example, social media platforms with a single feed for each user, such as Twitter or Instagram.

### Flat list layout

The [flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/#flat-list-layout) is for destination platforms that:

  * Organize content into folders.
  * Don't support nested folders.



### Nested list layout

The [nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/#nested-list-layout) is for destination platforms that:

  * Organize content into folders.
  * Support nested folders.



## Upload the user's design to the destination platform

When a user publishes a design, Canva:

  * Exports each page of the design as a separate asset.
  * Provides the extension with a URL to each asset.



An extension must:

  * Upload all the assets to the destination platform.
  * If the app requires a file name, use the asset's [`name`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/#asset) property.
  * If the app requires a title for the asset, use the asset's [`name`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/#asset) property, but remove the file extension.
  * Not simply link to the assets, as the URLs expire within a short time.
  * Organize the assets in such a way that the user can easily find them later on the destination platform.



## Handle large-size files

The destination platform must handle reasonably large-size designs.

Sometimes, a design published from Canva can be up to 50 MB. If required, consider one of these:

  * Processing the design asynchronously.
  * Providing a link to a media library or location where the user can act on the design.



## Correctly set up the output file types

![](https://www.canva.dev/_next/static/media/img-c23d3d0358.af69809e.svg)

When configuring an extension's **Output file types** , only select file types the destination platform supports. Users must be able to publish their designs in any of these configured file types.

If the app has a long processing time for a published design, asynchronously process the design or provide a link to a location, such as the media library, where the user can act on the design.

## Let users search for containers

![](https://www.canva.dev/_next/static/media/img-5dc400b054.7e90bbb5.svg)

If a publish extension uses the **Flat list** or **Nested list** layout, [add a search field to the extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/) to let users search for containers. This is more efficient than requiring users to navigate a list of options.

## Provide a link to the published design

![](https://www.canva.dev/_next/static/media/img-8286309fd7.56797a96.svg)

When a user publishes a design, provide a URL to view or action the design in the context of the destination platform. The URL must be fewer than 2000 characters.

For example, for designs published to Twitter, provide a link to the tweet. For designs published to a website creation platform, take the user to a page where they can insert the published design.

By default, users see the text "Check out your post here", then the complete URL in the next line. You can customize this to show the anchor text "View in `[app-name]`". This keeps the URL simple and short. To enable the anchor text, see [Generate external link](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/#generate-external-link).

If some users (for example, students) aren't allowed to see the published design, inform them with a suitable message.

## Align with the destination platform's requirements

Comply with the destination platform's standards, such as:

  * File name conventions, such as length, whitespace, and special characters restrictions
  * File size limits
  * Security policies
  * Terms and conditions



If required, sanitize or normalize any unknown input. This helps avoid errors, failures, and security issues on the destination platform.

## Tell users what to do next

If the destination platform expects further action, the URL provided by the extension should take the user to where they can complete that action.

For example, a website creation tool that lets users choose where to insert their published design should take the user to a page where the user can make that choice.

## Show the user's message

![](https://www.canva.dev/_next/static/media/img-1308955a7d.69eaa3f1.svg)

If the extension [requires users to provide a message](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/), the destination platform should use that message in a meaningful way. In other words, don't require users to provide a message for no particular reason.

## Ensure the destination platform does what it says

When a user publishes a design, the experience carries over from Canva to the destination platform. This means the destination platform reflects on the app's quality and the user's overall experience.

Ensure the destination platform:

  * Is secure.
  * Works as expected.
  * Shows the published designs.
  * Lets the user complete the user journey. For example, if the platform creates campaigns and surveys, the user must be able to create an email campaign with the published design.


