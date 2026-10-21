---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/
title: Images - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:50.060421+00:00
---

# Images - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Images

Copy page

When creating a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/), one of the available options for the **Content type** field is **Images**. If you select this option, the extension can import image files, such as photos or illustrations, into Canva.

![](https://www.canva.dev/_next/static/media/img-8d6a48276d.4ca8c39a.jpeg)

If you're looking for the API reference, see [/content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#image).

## Examples

These are some examples of apps with content extensions that support images:

  * [Brandfetch⁠(opens in a new tab or window)](https://www.canva.com/apps/AAD2V_3Se-E-brandfetch)
  * [Bynder⁠(opens in a new tab or window)](https://www.canva.com/apps/AAEQj2I8aCM-bynder)
  * [Pixton⁠(opens in a new tab or window)](https://www.canva.com/apps/AAD6Bz83ydE-pixton)



To find more examples, see [canva.com/apps⁠(opens in a new tab or window)](https://www.canva.com/apps).

## Supported image types

This section describes the types of images a content extension can import into Canva.

### GIF

You can't import GIFs into Canva as images. You can only import them as [embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/) or [videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/).

### JPG / JPEG

  * Under 25 MB in size
  * Not more than 100 million total pixels (width × height)



### PNG

  * Under 25 MB in size
  * Not more than 100 million total pixels (width × height)



### HEIC

  * Under 25 MB in size
  * Not more than 100 million total pixels (width × height)



### SVG

  * Under 10 MB in size
  * Saved with an SVG Profile of "SVG 1.1"



The following elements are stripped from SVG images:

  * `script`
  * `metadata`
  * `style`



You must wrap SVG attribute values in double quotes, not single quotes. For example, `version="1.0"` is valid, while `version='1.0'` is not.

For additional requirements that apply to this content type, see [Choose the best content types](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-content-types).

## Additional considerations

  * Cross-Origin Resource Sharing (CORS) can interfere with the importing of images. To learn more, see [CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/).
  * For guidelines on choosing the layout that's most appropriate for your content type, see [Choose the best layout](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-layout).



## Example

This example assumes the extension is configured to support images.
    
    
    const axios = require("axios");
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      // Get a list of images
    
      const { data } = await axios.get("https://picsum.photos/v2/list");
    
    
    
    
      // Create an array of resources
    
      const resources = data.map((resource) => {
    
        return {
    
          type: "IMAGE",
    
          id: resource.id, // This ID should always refer to the same piece of media
    
          name: resource.author || resource.id,
    
          thumbnail: {
    
            url: resource.download_url,
    
          },
    
          url: resource.download_url,
    
          contentType: "image/jpeg",
    
        };
    
      });
    
    
    
    
      // Respond with the resources
    
      response.send({
    
        type: "SUCCESS",
    
        resources,
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
