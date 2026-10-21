---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/
title: Content extensions - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:23.096336+00:00
---

# Content extensions - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Content extensions

What are content extensions? Why create one?

Copy page

A content extension imports third-party content, such as photos and illustrations, into Canva. Users can access this content via the side panel and add it to their designs.

![](https://www.canva.dev/_next/static/media/img-1994bd01cd.1ca55442.jpeg)

To create a content extension from scratch, check out the [Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/) guide.

## Examples of content extensions

These are some examples of apps with content extensions:

  * [Brandfetch⁠(opens in a new tab or window)](https://www.canva.com/apps/brandfetch) \- Easily add company logos to your design.
  * [Dropbox⁠(opens in a new tab or window)](https://www.canva.com/apps/dropbox) \- Add Dropbox photos to your designs.
  * [Giphy⁠(opens in a new tab or window)](https://www.canva.com/apps/giphy) \- Add GIFs to your designs. Powered by GIPHY.



You can find more examples at [canva.com/apps⁠(opens in a new tab or window)](https://www.canva.com/apps).

## How users experience content extensions

Users can find apps with content extensions via the **More** tab.

![](https://www.canva.dev/_next/static/media/img-c0459178cf.88804146.jpeg)

When a user opens a content extension, the app is pinned to the left side of the screen and the content appears in the side panel. The user can then drag content into their design.

![](https://www.canva.dev/_next/static/media/img-bbab868424.b4316e37.jpeg)

With additional configuration, a content extension can also:

  * [Let users search for content](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/).
  * [Organize images into folders](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/).
  * [Require authentication to access content](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).



## How content extensions work

At its most basic, a content extension is a REST API.

Canva expects this API to have the following endpoint:

  * [`/content/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/)



As a user interacts with a content extension via Canva's UI, Canva sends requests to this endpoint and expects to receive responses in a format that it understands. Based on these responses, Canva knows what content to render in the side panel.

### Supported content types

A content extension can provide users with two types of content:

  * [Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/), such as JPEG, PNG, and SVG files.
  * [Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/), such as animated GIFs, YouTube videos, and Instagram photos.



### Request-response cycle

This is the request-response cycle of a content extension:

![](https://www.canva.dev/_next/static/media/img-e1305bbf91.c1466cd8.png)

Canva sends additional requests if the extension supports [authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).

## Example
    
    
    const axios = require("axios");
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      const { data } = await axios.get("https://picsum.photos/v2/list");
    
    
    
    
      const resources = data.map((resource) => {
    
        return {
    
          type: "IMAGE",
    
          id: resource.id,
    
          name: resource.author || resource.id,
    
          thumbnail: {
    
            url: resource.download_url,
    
          },
    
          url: resource.download_url,
    
          contentType: "image/jpeg",
    
        };
    
      });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources,
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
