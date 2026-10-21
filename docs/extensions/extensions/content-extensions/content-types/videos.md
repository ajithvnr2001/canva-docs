---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/
title: Videos - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:50.659368+00:00
---

# Videos - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Videos

Copy page

When creating a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/), one of the available options for the **Content type** field is **Videos**. If you select this option, the extension can import video files into Canva.

![](https://www.canva.dev/_next/static/media/img-08efa1850b.ebb9e987.jpg)

If you're looking for the API reference, see [/content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#video).

## Supported videos types

A content extension can import the following types of video files into Canva:

  * MOV
  * GIF
  * MP4
  * MPEG
  * MKV
  * WEBM



Canva does _not_ support videos encoded in the following formats:

  * Apple Intermediate
  * ProRes 4444 (ProRes 422 Supported)
  * HDV 720p60
  * Go2Meeting3 (G2M3)
  * Go2Meeting4 (G2M4)



The maximum supported file size is 100 MB. (This applies to all media imported via a content extension, not just video files.)

If you want to import embeddable videos into Canva, such as YouTube videos, see [Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/).

## Handling video requests

When a content extension supports videos, Canva retrieves the videos from the extension by sending a `POST` request to the following endpoint:
    
    
    <base_url>/content/resources/find

BASH

Copy

`<base_url>` is a placeholder that's replaced with the extension's [Base URL](https://www.canva.dev/docs/extensions/backend-development/base-url/).

The body of the request includes a `types` property that contains `"VIDEO"` as one of its values:
    
    
    {
    
      "user": "AUQ2RUzug9pEvgpK9lL2qlpRsIbn1Vy5GoEt1MaKRE=",
    
      "brand": "AUQ2RUxiRj966Wsvp7oGrz33BnaFmtq4ftBeLCSHf8=",
    
      "label": "CONTENT",
    
      "limit": 100,
    
      "type": "VIDEO",
    
      "types": ["VIDEO"],
    
      "locale": "en-US"
    
    }

JSON

Copy

This indicates that the extension can include video resources in the response:
    
    
    {
    
      "type": "VIDEO",
    
      "id": "37088",
    
      "name": "Video by Sakura_Studio",
    
      "thumbnail": {
    
        "url": "https://i.vimeocdn.com/video/885893632_1280x720.jpg",
    
        "width": 1280,
    
        "height": 720
    
      },
    
      "url": "https://player.vimeo.com/external/413229662.hd.mp4?s=26815ea7e1ba43aa54042b394780fbde2ad33d02&profile_id=170",
    
      "contentType": "video/mp4",
    
      "durationMs": 2000,
    
      "width": 2560,
    
      "height": 1440
    
    }

JSON

Copy

You can find the schema for video resources in [the API reference](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/#video).

## Additional considerations

  * Cross-Origin Resource Sharing (CORS) can interfere with the importing of videos. To learn more, see [CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/).
  * For guidelines on choosing the layout that's most appropriate for your content type, see [Choose the best layout](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-layout).



## Example

This example assumes the extension is configured to support videos.
    
    
    const axios = require("axios");
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    if (!process.env.PIXABAY_API_KEY) {
    
      throw new Error("The PIXABAY_API_KEY environment variable is not set");
    
    }
    
    
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      const options = {
    
        url: "https://pixabay.com/api/videos/",
    
        params: {
    
          key: process.env.PIXABAY_API_KEY,
    
        },
    
      };
    
    
    
    
      const { data } = await axios.request(options);
    
    
    
    
      const resources = data.hits.map((item) => {
    
        return {
    
          type: "VIDEO",
    
          id: item.id.toString(),
    
          name: `Video by ${item.user}`,
    
          thumbnail: createThumbnail(item),
    
          url: item.videos.medium.url,
    
          contentType: "video/mp4",
    
          durationMs: item.duration * 1000,
    
          width: item.videos.medium.width,
    
          height: item.videos.medium.height,
    
        };
    
      });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources,
    
      });
    
    });
    
    
    
    
    function createThumbnail({
    
      picture_id,
    
      videos: {
    
        tiny: { width, height },
    
      },
    
    }) {
    
      return {
    
        url: `https://i.vimeocdn.com/video/${picture_id}_${width}x${height}.jpg`,
    
        width,
    
        height,
    
      };
    
    }
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
