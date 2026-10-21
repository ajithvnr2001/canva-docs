---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/
title: Search - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:52.084757+00:00
---

# Search - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Search

Add a search field to a publish extension.

Copy page

When a user attempts to publish their design, they may want to publish that design to a specific container. If that container is nested deep in a hierarchy though, it might be difficult to find. To improve the user experience, you can let users search for containers.

This guide explains how to add a search field to a publish extension.

![](https://www.canva.dev/_next/static/media/img-107471c5d0.8630c3ef.jpg)

To support search, a publish extension must use the [Flat list](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/) or [Nested list](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/) layout.

## Step 1: Enable search

By default, publish extensions don't support search. You need to enable the feature.

To enable search for a publish extension:

  1. Navigate to an app via the Developer Portal.
  2. On the **Extensions** page, expand the **Publish** panel.
  3. Enable **Display search field**.



If you preview the extension, a search field is visible in the **Publish** menu.

## Step 2: Receive search requests

When a user performs a search, Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/publish/resources/find

BASH

Copy

This is the same endpoint that Canva sends requests to when a user loads a publish extension or opens a container. The only difference is that the request body includes a `query` parameter:
    
    
    {
    
      "user": "AUQ2RUzug9pEvgpK9lL2qlpRsIbn1Vy5GoEt1MaKRE=",
    
      "brand": "AUQ2RUxiRj966Wsvp7oGrz33BnaFmtq4ftBeLCSHf8=",
    
      "label": "PUBLISH",
    
      "limit": 100,
    
      "type": "IMAGE",
    
      "locale": "en-US",
    
      "query": "funny memes",
    
      "preferredThumbnailHeight": 100,
    
      "preferredThumbnailWidth": 100
    
    }

JSON

Copy

The `query` parameter contains the value of the search field.

## Step 3: Detect when a user performs a search

When a `POST` request is not triggered by a search, the `query` property is `null`. This makes it possible to determine whether or not the user has performed a search:
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      if (request.body.query) {
    
        // The user has performed a search
    
      } else {
    
        // The user hasn't performed a search
    
      }
    
    });

JAVASCRIPT

Copy

The `query` and `containerId` properties are mutually exclusive. This means a user cannot search inside a specific container.

## Step 4: Respond to search requests

When a user performs a search, a publish extension should respond to the request with a `"SUCCESS"` response:
    
    
    {
    
      "type": "SUCCESS",
    
      "resources": []
    
    }

JSON

Copy

This response should include resources relevant to the search query. What "relevancy" means is up to the extension. It could be as simple as returning resources that have the search query in their names or something more sophisticated.

If a publish extension supports search, it should also support [pagination](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/). This lets users paginate through more results than can be included in a single response.

## Example
    
    
    const axios = require("axios");
    
    const express = require("express");
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      // Get fake data for containers
    
      const { data } = await axios.get(
    
        "https://jsonplaceholder.typicode.com/albums"
    
      );
    
    
    
    
      // Create a list of containers
    
      let resources = data.map((resource) => {
    
        return {
    
          id: resource.id,
    
          name: resource.name,
    
          type: "CONTAINER",
    
        };
    
      });
    
    
    
    
      // Handle search requests
    
      if (request.body.query) {
    
        resources = resources.filter((resource) => {
    
          return resource.name.toLowerCase().includes(request.body.query);
    
        });
    
      }
    
    
    
    
      // Respond to the request
    
      response.send({
    
        type: "SUCCESS",
    
        resources: resources,
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
