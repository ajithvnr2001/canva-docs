---
url: https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/
title: UX guidelines for content extensions - UX guidelines - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:59.970301+00:00
---

# UX guidelines for content extensions - UX guidelines - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/

UX guidelines

[Overview](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/)[UX guidelines for content extensions](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/)[UX guidelines for publish extensions](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/)[Writing copy for your app](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/copy/)[Optimizing the authentication flow](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/)

# UX guidelines for content extensions

Copy page

Canva's content library is a big part of its charm. This page contains some guidelines for creating a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/) that behaves in a way that's familiar to users.

## Choose the best layout

The layout of a content extension affects the appearance of content within the Canva editor. Your extension should use the layout most appropriate to the type of content it provides.

![](https://www.canva.dev/_next/static/media/img-a8df16d754.7b681898.svg)

### Grid layout

You should use the **Grid** layout if:

  * There is variability in the dimensions of the content.
  * There is a mix of transparent and non-transparent content.
  * The title of the content (and other metadata) is not essential to the user experience.
  * The extension doesn't organize content into containers.
  * Thumbnails exactly match the content that's added to the design.



### List layout

You should use the **List** layout if:

  * There is no variability in the dimensions of the content.
  * Thumbnails must be displayed at full-width for them to be meaningful.
  * The content's metadata helps users differentiate between content (for example, videos displaying their title and publish date).
  * The content's thumbnail is not an exact match for how it appears in the design (for example, videos, maps, forms, etc).



## Choose the best content types

You can configure an extension to support one or more [content types](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/). This determines the type of content the extension can import into Canva. You must only enable the content types that your extension demonstrably supports at submission time.

![](https://www.canva.dev/_next/static/media/img-6c7babda9b.a1037dfe.svg)

There's additional guidelines for each content type.

### Containers

If you enable the [**Containers**](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/) content type, the following requirements apply:

  * The use of containers improves the user's browsing experience.
  * Opening a container loads content that belongs to that container.
  * Users can paginate through containers.
  * The containers are organized the way they're shown on the source platform (structure, hierarchy).
  * The containers are shown in the search results.



### Embeds

If you enable the [**Embeds**](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/) content type, the following requirements apply:

  * The URLs of the embeds are supported by [Iframely⁠(opens in a new tab or window)](https://iframely.com/).
  * Embeds are compatible with Canva's supported browsers.
  * Embeds are added to the design with the correct aspect ratio.
  * Thumbnails allow the user to identify (and distinguish between) embeds.



### Images

If you enable the [**Images**](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/) content type, , the following requirements apply:

  * Images meet Canva's [Upload formats and requirements⁠(opens in a new tab or window)](https://www.canva.com/help/article/upload-formats-requirements).
  * Images are added to the design with the correct aspect ratio.
  * Thumbnails accurately represent the full-sized image.
  * Full-sized images are of sufficient quality for their intended use.



## Show clear thumbnails

Thumbnails in the side panel provide users a glimpse of what the app can offer.

Thumbnails must:

  * Be clear and not pixelated.
  * Match the aspect ratio of the full-resolution media.
  * Accurately represent the content.
  * Be under 200 KB in size.
  * Be sorted in a logical order (newest first, alphabetically, etc).
  * Show a meaningful, human-readable label (no timestamps or special characters).
  * Have [CORS permissions](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/) (otherwise, they won't appear in the side panel).



For API reference information, see [Thumbnail](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#thumbnail).

## Add a search field to the extension

If possible, content extensions should provide a [search field](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/) that allows users to search for content.

![](https://www.canva.dev/_next/static/media/img-356950792f.26044e54.svg)

If an extension has a search field, ensure that:

  * Search results match the user's expectations.
  * Search results are returned in a logical order.
  * Search results are paginated.
  * Users can search for partial words.
  * Thumbnails accurately represent the content.
  * Thumbnails are clear and not pixelated.



You can also (optionally) customize the placeholder text of the search field. As with all text, it should follow the copy guidelines. These are some good examples of placeholder text:

  * Search images
  * Enter a location
  * Enter a website URL
  * Search your folders



## Handle empty states

When a user opens a content extension, they should be shown some initial content, rather than an empty screen. Sometimes though, this isn't possible, such as when an authenticated user doesn't have media uploaded to their account.

If it's not possible to provide initial content, an extension must provide **Empty state text**. Canva displays this text when there is no initial content.

![](https://www.canva.dev/_next/static/media/img-ccd653bb00.73c217d4.svg)

If an extension provides **Empty state text** :

  * Keep the message concise, informative, and actionable.
  * Use 1-2 sentences.
  * Use fewer than 150 characters. This avoids overflow and allows the text to be translated into languages that may require more characters to convey the same meaning.



This is a good example of **Empty state text** :

> Content from your Dropbox account will appear here. Check you have content in your account with Dropbox.

## Review the content

The content the app returns reflects not only on the app's quality but also on Canva's credibility. Review the content and make sure it meets Canva's standards.

  * Show all supported content types ([image types](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/#supported-image-types), [video types](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/#supported-videos-types), [embed types](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/#supported-embed-types)).
  * Show only child-safe content (no explicit, offensive, and violent content).
  * Avoid watermarked content.
  * Follow a logical order (newest to oldest, oldest to newest, etc)
  * Show human-readable labels.
  * Upload the content with a new ID when it's edited.
  * Match the content as shown in the source platform.
  * Enable [CORS permissions](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/) (otherwise, they won't appear when dragged onto a design).


