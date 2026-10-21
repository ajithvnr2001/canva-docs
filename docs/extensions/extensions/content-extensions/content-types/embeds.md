---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/
title: Embeds - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:50.347714+00:00
---

# Embeds - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Embeds

Copy page

When creating a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/), one of the available options for the **Content type** field is **Embeds**. If you select this option, the extension can import embeddable media into Canva, such as YouTube videos or Instagram photos.

![](https://www.canva.dev/_next/static/media/img-6ac5b8ab95.11429a70.jpeg)

If you're looking for the API reference, see [/content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#embed).

## Examples

These are some examples of apps with content extensions that support embeds:

  * [Giphy⁠(opens in a new tab or window)](https://www.canva.com/apps/giphy)
  * [Google Maps⁠(opens in a new tab or window)](https://www.canva.com/apps/google-maps)
  * [YouTube⁠(opens in a new tab or window)](https://www.canva.com/apps/youtube)



To find more examples, see [canva.com/apps⁠(opens in a new tab or window)](https://www.canva.com/apps).

## Supported embed types

Canva uses [Iframely⁠(opens in a new tab or window)](https://iframely.com/) to embed media into designs. This means an extension can import any Iframely supported content into Canva. The media itself is embedded via an iframe.

![](https://www.canva.dev/_next/static/media/img-b691ed293a.157f1ecb.jpg)

To check if a URL is supported by Iframely, see [URLs supported by Iframely⁠(opens in a new tab or window)](https://iframely.com/docs/providers#urls-supported-by-iframely).

For additional requirements that apply to this content type, see [Choose the best content types](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-content-types).

## Additional considerations

For guidelines on choosing the layout that's most appropriate for your content type, see [Choose the best layout](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-layout).

## Limitations

  * Users can't apply effects to embeds. They can only manipulate the size, position, and rotation of the embed.
  * Canva only stores a reference to the embedded media. If the original media is deleted or otherwise becomes unavailable, an error appears in place of the media.



## Example

This example assumes the extension is configured to support embeds.
    
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      response.send({
    
        type: "SUCCESS",
    
        resources: [
    
          {
    
            id: "dQw4w9WgXcQ",
    
            name: "Rick Astley - Never Gonna Give You Up",
    
            type: "EMBED",
    
            thumbnail: {
    
              url: "https://i.imgur.com/Q2Unw.gif",
    
            },
    
            url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    
          },
    
        ],
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
