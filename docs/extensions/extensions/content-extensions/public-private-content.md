---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/
title: Public vs. private content - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:48.422015+00:00
---

# Public vs. private content - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Public vs. private content

Copy page

When a user imports content into Canva via a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/), Canva may upload the content to the user's account, display it in the **Uploads** tab, and count it against their [upload quota⁠(opens in a new tab or window)](https://www.canva.com/help/article/manage-uploads).

Whether or not this happens depends on if the content is public or private.

## Public content

If a user doesn't need to [authenticate](https://www.canva.dev/docs/extensions/platform-concepts/authentication/) before using a content extension, Canva considers its content to be public.

Public content has the following attributes:

  * It never appears in the user's **Uploads** tab
  * It never counts against the user's upload quota



## Private content

If a user needs to authenticate before using a content extension, Canva considers its content to be private.

Private content has the following attributes:

  * It always appears in the user's **Uploads** tab
  * It always counts against the user's upload quota



## Additional considerations

  * All content must have a unique ID that always refers to the same piece of content. This ensures that, if the content already exists on Canva's servers, users don't have to wait for it to upload.
  * If a piece of content changes, make sure to assign a new ID to that content. If you don't, the old content may appear in the user's design.


