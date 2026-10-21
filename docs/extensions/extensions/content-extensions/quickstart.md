---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/
title: Quickstart - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:48.302720+00:00
---

# Quickstart - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# Quickstart

Create a content extension in under 30 minutes.

Copy page

A [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/) imports content, such as photos and illustrations, into Canva. Users can access this content via the side panel and add it to their designs.

![](https://www.canva.dev/_next/static/media/img-8d6a48276d.4ca8c39a.jpeg)

This guide demonstrates how to create a content extension that imports content from [Lorem Picsum⁠(opens in a new tab or window)](https://picsum.photos/), an API for placeholder photos.

## Prerequisites

This guide assumes experience with:

  * JSON APIs
  * Node.js
  * Express.js



You don't have to create content extensions with Node.js or Express.js, but most of the examples in this documentation use these technologies.

## Step 1: Set up a Base URL

At its most basic, a content extension is an API that receives requests from Canva and responds with data in a format that Canva understands. Canva expects this API to have certain paths to handle different requests.

To get an API up and running as quickly as possible, we recommend using [Glitch⁠(opens in a new tab or window)](https://glitch.com), a web-based editor for creating and deploying Node.js apps. Glitch is free and registration is not required.

To set up a project with Glitch:

  1. Click the following button:

[![Remix on Glitch](https://cdn.glitch.com/2703baf2-b643-4da7-ab91-7ee2a2d00b5b%2Fremix-button.svg)⁠(opens in a new tab or window)](https://glitch.com/edit/#!/remix/content-extension-quickstart)

This opens the Glitch editor with the source code of a simple content extension.

  2. Click **Share**.

  3. Copy the URL from the **Live site** field. You need this URL for a later step.




![](https://www.canva.dev/_next/static/media/img-ff3b8ec29a.5d0ac8f5.jpeg)

Don't use Glitch's free service for production apps: it's slow and the servers hibernate after a few minutes of inactivity.

## Step 2: Create an app via the Developer Portal

  1. Log in to the [Developer Portal⁠(opens in a new tab or window)](https://canva.com/developers).
  2. Navigate to **Your integrations**.
  3. Click **Create an app**.
  4. Choose a target audience for the app. (The default option is **Everyone**.)
  5. Click **Next**.
  6. Select **Create content**.
  7. Click **Next**.
  8. Click **Create app**.



## Step 3: Configure the content extension

  1. Paste the **Live site** URL from Glitch into the **Base URL** field.
  2. For the **Layout** option, select **Grid**.
  3. For the **Content type** option, select **Images**.



For guidelines on choosing the layout that's most appropriate for your content type, see [Choose the best layout](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-layout).

To learn about the supported content types, see [Content types](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/). For additional requirements that apply to each content type, see [Choose the best content types](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/#choose-the-best-content-types).

![](https://www.canva.dev/_next/static/media/img-de7cc65558.c653f112.jpeg)

Canva automatically saves changes to apps. You'll see a warning if you try to navigate away from the Developer Portal before your changes are saved.

## Step 4: Preview the extension in the Canva editor

  1. Click **Preview**.
  2. Select the extension from the dropdown list.
  3. Click **Use**.



When the extension loads, Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/content/resources/find

BASH

Copy

This endpoint responds with an array of images, which Canva renders in the side panel.

![](https://www.canva.dev/_next/static/media/img-b7c1ace949.0eda6049.jpeg)

You only have to click the **Use** button when using an app for the first time. On return visits, the app immediately loads.

## Next steps

This guide has only scratched the surface of what's possible with content extensions.

To learn more, refer to the following guides:

  * [Pagination](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)
  * [Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)
  * [Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/)



You can also [create a support ticket⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/2/group/2) if you need additional help.

To provide users the best experience with content extensions, see [UX guidelines for content extensions](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/).

## Example
    
    
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
