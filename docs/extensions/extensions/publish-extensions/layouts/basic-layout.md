---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/
title: Basic layout - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:53.579227+00:00
---

# Basic layout - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Basic layout

Create a publish extension with the "Basic" layout.

Copy page

A [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) adds a publish destination to Canva. Users can then publish their design to this destination via Canva's **Publish** menu.

This tutorial explains how to create a publish extension that uses the **Basic** layout. This layout is intended for platforms that don't organize content into folders, such as social media platforms with a single feed for each user (for example, Twitter or Instagram).

![](https://www.canva.dev/_next/static/media/img-8fb29990cc.6ee96c1b.png)

To learn about the other layouts available for publish extensions, see [Layouts](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/).

## Step 1: Set up a Base URL

In the Developer Portal, publish extensions have a **Base URL** field. This indicates that the extension must provide the URL of a server that can receive and respond to HTTP requests from Canva.

To set up a **Base URL** , refer to either of the following guides:

  * [Set up a Base URL (with Glitch)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/)
  * [Set up a Base URL (with ngrok)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/)



You can use any programming language, framework, or architecture to handle requests from Canva, but the examples in this documentation use [Express.js⁠(opens in a new tab or window)](https://expressjs.com).

## Step 2: Set up the required endpoints

A publish extension that uses the **Basic** layout must support the following endpoint:

  * [`POST /publish/resources/upload`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/)



The following snippet demonstrates how to set up these endpoints with Express.js:
    
    
    const express = require("express");
    
    const fs = require("fs-extra");
    
    const jimp = require("jimp");
    
    const path = require("path");
    
    const url = require("url");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/publish/resources/upload", async (request, response) => {
    
      // code goes here
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy

This snippet also assumes the following Node.js dependencies are installed:

  * [`express`⁠(opens in a new tab or window)](https://www.npmjs.com/package/express)
  * [`fs-extra`⁠(opens in a new tab or window)](https://www.npmjs.com/package/fs-extra)
  * [`jimp`⁠(opens in a new tab or window)](https://www.npmjs.com/package/jimp)



## Step 3: Create an app via the Developer Portal

  1. Log in to the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers).
  2. Navigate to the **Your integrations** page.
  3. Click **Create an app**.
  4. In the **App name** field, enter a name for the app.
  5. Agree to the [Canva Developer Terms⁠(opens in a new tab or window)](https://about.canva.com/policies/developer-terms/).
  6. Click **Create app**.



## Step 4: Add a publish extension to the app

  1. Select **Publish**.
  2. In the **Base URL** field, enter the URL of the server.
  3. For the **Layout** option, select **Basic**.
  4. For the **Output file types** option, select the types of files a user can publish to the destination platform. The example in this tutorial requires the file types to be **JPG** and **PNG**.
  5. For the **Max number of pages** field, enter the maximum number of pages that a user can publish of their design. The example in this tutorial requires the number of pages to be **1**.



Any changes to the form save automatically.

## Step 5: Upload the user's design

When a user opens a publish extension, Canva displays a handful of options and a **Save** button. The available options depend on how the extension is configured.

![](https://www.canva.dev/_next/static/media/img-8fb29990cc.6ee96c1b.png)

When the user clicks the **Save** button, Canva sends a request to the extension. The request body includes an array of assets. Each asset has a `url`, which the extension must use to download the assets to the destination platform.

The following snippet demonstrates how to download an asset to the `public` directory and create a URL that lets the user view the published asset:
    
    
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

JAVASCRIPT

Copy

If the user publishes their design as an image, Canva provides each page of the design as a separate asset. Otherwise, Canva provides the entire design as a single asset.

For guidelines on uploading the assets, see [Upload the user's design to the destination platform](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/#upload-the-users-design-to-the-destination-platform).

If you'd like to release your app to Canva's users, the `url` property must point to a page that lets users view and action the published design in context on the destination platform. For guidelines on providing a publish link, see Provide a link to the published design.

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
