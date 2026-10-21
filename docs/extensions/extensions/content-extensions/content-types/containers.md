---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/
title: Containers - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:50.838793+00:00
---

# Containers - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Containers

Copy page

When creating a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/), one of the available options for the **Content type** field is **Containers**. If you select this option, the extension can organize content into containers (folders).

![](https://www.canva.dev/_next/static/media/img-7e145abdc8.6de9d3b8.jpeg)

If you're looking for the API reference, see [/content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#container).

## Request-response cycle

For the most part, containers work the same way as the other [content types](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/). There are, however, a couple of details that affect the request-response cycle:

Canva always requests containers in separate HTTP requests from the other types of content. For example, if you configure a content extension to support [images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/), [embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/), and containers, Canva will send one request for the images and embeds, and a different request for the containers.

When a user selects a container, Canva includes a `containerId` property in both requests. The extension can use this ID to respond with content and sub-containers that belong to the selected container. This is demonstrated in [the example](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/#example).

## Notes

  * You can assign [thumbnails](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#thumbnail) to containers. This thumbnail should represent or provide an example of the container's contents.
  * For additional requirements that apply to this content type, see [Choose the best content types](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-content-types).



## Limitations

  * You can't [submit an app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/) if it has a content extension that only supports containers. This is because an extension that only supports containers isn't useful.
  * If a content extension supports [search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/), containers appear in search results, but users can't search for content inside specific containers.



## Example

This example assumes the extension is configured to support images and containers.
    
    
    const axios = require("axios");
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    if (!process.env.PIXABAY_API_KEY) {
    
      throw new Error("The PIXABAY_API_KEY environment variable is not set");
    
    }
    
    
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      // Handle "CONTAINER" requests
    
      if (request.body.types.includes("CONTAINER")) {
    
        // The user has opened a container
    
        if (request.body.containerId) {
    
          response.send({
    
            type: "SUCCESS",
    
            resources: [],
    
          });
    
        }
    
    
    
    
        // The user has not opened a container
    
        if (!request.body.containerId) {
    
          response.send({
    
            type: "SUCCESS",
    
            resources: [
    
              {
    
                type: "CONTAINER",
    
                id: "animals",
    
                name: "Animals",
    
              },
    
              {
    
                type: "CONTAINER",
    
                id: "food",
    
                name: "Food",
    
              },
    
              {
    
                type: "CONTAINER",
    
                id: "people",
    
                name: "People",
    
              },
    
            ],
    
          });
    
        }
    
      }
    
    
    
    
      // Handle "IMAGE" requests
    
      if (request.body.types.includes("IMAGE")) {
    
        // Configure the request
    
        const options = {
    
          url: "https://pixabay.com/api/",
    
          params: {
    
            key: process.env.PIXABAY_API_KEY,
    
          },
    
        };
    
    
    
    
        // The user has opened a container
    
        if (request.body.containerId) {
    
          options.params.category = request.body.containerId;
    
        }
    
    
    
    
        // Send the request
    
        const pixabay = await axios.request(options);
    
    
    
    
        // Transform the array of images into an array of "IMAGE" resources
    
        const images = pixabay.data.hits.map((image) => {
    
          return {
    
            type: "IMAGE",
    
            id: image.id,
    
            name: `Photo by ${image.user}`,
    
            thumbnail: {
    
              url: image.webformatURL,
    
              height: image.webformatHeight,
    
              width: image.webformatWidth,
    
            },
    
            url: image.webformatURL,
    
            contentType: "image/jpeg",
    
          };
    
        });
    
    
    
    
        // Provide a success response
    
        response.send({
    
          type: "SUCCESS",
    
          resources: images,
    
        });
    
      }
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
