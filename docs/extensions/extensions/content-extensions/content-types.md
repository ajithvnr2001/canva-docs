---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/
title: Content types - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:49.229261+00:00
---

# Content types - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Content types

Copy page

In the Developer Portal, [content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/) have a **Content type** field.

![](https://www.canva.dev/_next/static/media/img-52b21ac0e8.158520f4.jpeg)

This field determines:

  * The type of content the extension can import into Canva
  * The work required to create the extension



This topic describes the types of content that Canva supports and the implications of supporting them.

If you're looking for the API reference, see [/content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#embed).

## Supported content types

You can configure a content extension to support the following types of content:

  * [Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)
  * [Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)
  * [Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)
  * [Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)



To learn more about each specific content type, see the linked documentation.

For guidelines on choosing the layout that's most appropriate for your content type, see [Choose the best layout](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-layout).

For additional requirements that apply to each content type, see [Choose the best content types](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-content-types).

## Request-response cycle

As a user interacts with a content extension, Canva sends `POST` requests to the following endpoint:
    
    
    <base_url>/content/resources/find

BASH

Copy

`<base_url>` is a placeholder that's replaced with the extension's [Base URL](https://www.canva.dev/docs/extensions/backend-development/base-url/).

This is an example of a request:
    
    
    {
    
      "user": "AQ_7dBCCJN5yCxQiBX-QjJLT8ZnLwn-0kISpwpHqh68=",
    
      "brand": "AQ_7dBC9ihGVL06M4KkBKreDsSoZcZZAwbrdzwgDkjs=",
    
      "label": "CONTENT",
    
      "limit": 8,
    
      "locale": "en",
    
      "type": "IMAGE",
    
      "types": ["IMAGE"]
    
    }

JSON

Copy

The body of this request contains a `types` array. Each value in this array is an uppercase string that corresponds to one of the supported content types:

  * `"CONTAINER"`
  * `"EMBED"`
  * `"IMAGE"`
  * `"VIDEO"`



In response to this request, the extension must provide an array of _resources_. (The term _resource_ is how Canva's API generally refers to an individual piece of content.)

In the request body, the `types` property has superseded the now-deprecated `type` property. Canva only sends the `type` property for backwards compatibility reasons.

This is an example of a response that doesn't have any resources:
    
    
    {
    
      "type": "SUCCESS",
    
      "resources": []
    
    }

JSON

Copy

The type of content an extension can include in a response depends on the value of the `types` array. For example, if the `types` array contains `"IMAGE"` and `"EMBED"`, the extension can respond with images, embeds, or a combination of the two.

You can represent each resource as an object with a `type` property and metadata that describes the resource. For example, this is an `"IMAGE"` resource:
    
    
    {
    
      "type": "IMAGE",
    
      "id": "1025",
    
      "name": "Matthew Wiebe",
    
      "thumbnail": { "url": "https://picsum.photos/id/1025/4951/3301" },
    
      "url": "https://picsum.photos/id/1025/4951/3301",
    
      "contentType": "image/jpeg"
    
    }

JSON

Copy

Some properties are required for all content types, such as `id` and `name`, but other properties are only required for certain types of content. The details are described in [the API reference](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/).

After receiving a response from the extension, Canva renders the resources in the side panel. This is an example of an extension that renders a container, image, and embed:

![](https://www.canva.dev/_next/static/media/img-ff3d21c77f.eb75e53b.jpeg)

For guidelines on keeping the users informed when you can't show the initial content, see [Handle empty states](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#handle-empty-states).

## Limitations

  * You can't [submit an app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/) if it has a content extension that only has the **Container** option selected for its **Content type**. This is because an extension that only provides users with containers isn't useful.



## Example

To see a complete preview of this extension, configure it to support images, embeds, containers, and videos.
    
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      const resources = [];
    
    
    
    
      if (request.body.types.includes("CONTAINER")) {
    
        resources.push({
    
          type: "CONTAINER",
    
          id: "things",
    
          name: "Things",
    
        });
    
      }
    
    
    
    
      if (request.body.types.includes("IMAGE")) {
    
        resources.push({
    
          type: "IMAGE",
    
          id: "1025",
    
          name: "Matthew Wiebe",
    
          thumbnail: { url: "https://picsum.photos/id/1025/4951/3301" },
    
          url: "https://picsum.photos/id/1025/4951/3301",
    
          contentType: "image/jpeg",
    
        });
    
      }
    
    
    
    
      if (request.body.types.includes("EMBED")) {
    
        resources.push({
    
          id: "dQw4w9WgXcQ",
    
          name: "Rick Astley - Never Gonna Give You Up",
    
          type: "EMBED",
    
          thumbnail: {
    
            url: "https://i.imgur.com/Q2Unw.gif",
    
          },
    
          url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    
        });
    
      }
    
    
    
    
      if (request.body.types.includes("VIDEO")) {
    
        resources.push({
    
          id: "125",
    
          name: "Yellow flowers",
    
          type: "VIDEO",
    
          thumbnail: {
    
            url: "https://i.vimeocdn.com/video/529927645_640x360.jpg",
    
          },
    
          url: "https://player.vimeo.com/external/135736646.hd.mp4?s=ed02d71c92dd0df7d1110045e6eb65a6&profile_id=174",
    
        });
    
      }
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources,
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
