---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/search/
title: Search - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:49.665873+00:00
---

# Search - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/search/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Search

Add a search field to a content extension.

Copy page

A content extension can be configured to include a search field. This allows users to find exactly the content they're looking for.

![](https://www.canva.dev/_next/static/media/img-0ae87bd96e.4eb798ba.gif)

This topic explains how to receive and handle search queries.

## Step 1: Enable search

By default, content extensions don't support search. You need to enable the feature.

For guidelines on providing the best search experience, see [Add a search field to the extension](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#add-a-search-field-to-the-extension).

To enable search for a content extension:

  1. Navigate to an app via the Developer Portal
  2. On the **Extensions** page, expand the **Content** panel.
  3. Select the **Display search field** checkbox.



## Step 2: Receive search requests

When a user performs a search, Canva sends a `POST` request to the following URL:
    
    
    <base_url>/content/resources/find

BASH

Copy

This is the same URL that Canva sends requests to when requesting images, embeds, and containers. The only difference is that the body of this request includes a `query` property that contains the user's search query:
    
    
    {
    
      "user": "AUQ2RUzug9pEvgpK9lL2qlpRsIbn1Vy5GoEt1MaKRE=",
    
      "brand": "AUQ2RUxiRj966Wsvp7oGrz33BnaFmtq4ftBeLCSHf8=",
    
      "label": "CONTENT",
    
      "limit": 100,
    
      "type": "IMAGE",
    
      "locale": "en-US",
    
      "query": "funny cats"
    
    }

JSON

Copy

## Step 3: Detect when a user performs a search

When a `POST` request is _not_ triggered by a search, the `query` property is `null`. You can therefore detect when a user has performed a search by checking if the value of the `query` property is `null`:
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      if (request.body.query) {
    
        // the user has performed a search
    
      }
    
    
    
    
      if (!request.body.query) {
    
        // the user has not performed a search
    
      }
    
    });

JAVASCRIPT

Copy

## Step 4: Respond to search requests

When a user performs a search, a content extension should return a `"SUCCESS"` response that includes resources relevant to the user's query:
    
    
    {
    
      "type": "SUCCESS",
    
      "resources": []
    
    }

JSON

Copy

What counts as "relevant" depends on what you're trying to accomplish. Your extension could just return resources that have the user's exact search query in their `name` property. Or after users perform a search, you could keep track of what resources they drag into their designs and then use that data to surface the most relevant resources for future searches. It's your choice.

If a search returns more results than can be included in a single response, use [pagination](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/) to load the additional resources.

## Step 5: Handle containers

If an extension supports [containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/), it's important to know that the `query` and `containerId` properties are mutually exclusive. If the `query` property is not `null`, then the `containerId` will be `null`. This means a user cannot search within a container. You can, however, use a search query to return a filtered list of containers.

## Example

This example allows users to search for photos from [Pixabay⁠(opens in a new tab or window)](https://pixabay.com). You'll need a (free) API key to run it.
    
    
    const axios = require("axios");
    
    const express = require("express");
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      // Configure the request
    
      const options = {
    
        url: "https://pixabay.com/api/",
    
        params: {
    
          key: process.env.PIXABAY_API_KEY,
    
        },
    
      };
    
    
    
    
      // If a user has provided a query, include it in the request
    
      if (request.body.query) {
    
        options["params"]["q"] = request.body.query;
    
      }
    
    
    
    
      // Send a request to Pixabay
    
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
    
          contentType: "image/jpeg",
    
          url: image.webformatURL,
    
        };
    
      });
    
    
    
    
      // Return a "SUCCESS" response
    
      response.send({
    
        type: "SUCCESS",
    
        resources: images,
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
