---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/
title: Quickstart - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:51.400099+00:00
---

# Quickstart - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Quickstart

Create a publish extension in under 30 minutes.

Copy page

A [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) adds a publish destination to Canva. This destination appears in the **Publish** menu. Users can then publish their designs to the destination platform.

![](https://www.canva.dev/_next/static/media/img-a26f96abe6.8feb8092.jpeg)

This guide demonstrates how to create a publish extension that uploads the user's design to a directory on a web server.

## Prerequisites

This guide assumes experience with:

  * JSON APIs
  * Node.js
  * Express.js



You don't have to create publish extensions with Node.js or Express.js, but most of the examples in this documentation use these technologies.

## Step 1: Set up a Base URL

At its most basic, a publish extension is an API that receives requests from Canva and responds with data in a format that Canva understands. Canva expects this API to have certain paths to handle different requests.

To get an API up and running as quickly as possible, we recommend using [Glitch⁠(opens in a new tab or window)](https://glitch.com), a web-based editor for creating and deploying Node.js apps. Glitch is free and registration is not required.

To set up a project with Glitch:

  1. Click the following button:

[![Remix on Glitch](https://cdn.glitch.com/2703baf2-b643-4da7-ab91-7ee2a2d00b5b%2Fremix-button.svg)⁠(opens in a new tab or window)](https://glitch.com/edit/#!/remix/publish-extension-quick-start)

This opens the Glitch editor with the source code of a simple publish extension.

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
  6. Select **Publish designs**.
  7. Click **Next**.
  8. Click **Create app**.



## Step 3: Configure the publish extension

  1. Paste the **Live site** URL from Glitch into the **Base URL** field.
  2. For the **Layout** option, select **Basic**.
  3. For the **Output file types** option, select **JPG** and **PNG**.
  4. For the **Max number of pages** field, enter a value of **1**.



To learn about the available layouts, see [Layouts](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/). For guidelines on choosing the layout that's most appropriate for the destination platform, see [Choose the best layout](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/#choose-the-best-layout).

![](https://www.canva.dev/_next/static/media/img-905af61172.8d4a7691.jpeg)

Canva automatically saves changes to apps. You'll see a warning if you try to navigate away from the Developer Portal before your changes are saved.

## Step 4: Preview the extension in the Canva editor

  1. Click **Preview**.
  2. Select the extension from the dropdown list.
  3. Click **Use**.



When a user publishes their design by clicking the extension's **Save** button, Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/publish/resources/upload

BASH

Copy

This endpoint uploads the user's design to the web server and responds with a URL that lets users view the published design.

![](https://www.canva.dev/_next/static/media/img-6114152789.aded1c8d.jpeg)

You only have to click the **Use** button when using an app for the first time. On return visits, the app immediately loads.

## Next steps

This guide has only scratched the surface of what's possible with publish extensions.

To learn more, refer to the following guides:

  * [Pagination](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)
  * [Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)
  * [Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/)



You can also [create a support ticket⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/2/group/2) if you need additional help.

## Example
    
    
    const express = require("express");
    
    const fs = require("fs-extra");
    
    const jimp = require("jimp");
    
    const path = require("path");
    
    const url = require("url");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/publish/resources/upload", async (request, response) => {
    
      // Ensure the "public" directory exists
    
      await fs.ensureDir(path.join(__dirname, "public"));
    
    
    
    
      // Get the first asset from the "assets" array
    
      const [asset] = request.body.assets;
    
    
    
    
      // Download the asset
    
      const image = await jimp.read(asset.url);
    
      const filePath = path.join(__dirname, "public", asset.name);
    
      await image.writeAsync(filePath);
    
    
    
    
      // Respond with the URL of the published design
    
      response.send({
    
        type: "SUCCESS",
    
        url: url.format({
    
          protocol: request.protocol,
    
          host: request.get("host"),
    
          pathname: asset.name,
    
        }),
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
