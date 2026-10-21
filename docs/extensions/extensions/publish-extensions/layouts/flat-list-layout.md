---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/
title: Flat list layout - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:53.239681+00:00
---

# Flat list layout - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Flat list layout

Create a publish extension with the "Flat list" layout.

Copy page

A [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) adds a publish destination to Canva. Users can then publish their design to this destination via Canva's **Publish** menu.

This tutorial explains how to create a publish extension that uses the **Flat list** layout. This layout is intended for platforms that:

  * Require users to organize content into folders.
  * Don't support nested folders.



![](https://www.canva.dev/_next/static/media/img-4ed7354914.9d335fc4.png)

To learn about the other layouts available for publish extensions, see [Layouts](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/).

## Step 1: Set up a Base URL

In the Developer Portal, publish extensions have a **Base URL** field. This indicates that the extension must provide the URL of a server that can receive and respond to HTTP requests from Canva.

To set up a **Base URL** , refer to either of the following guides:

  * [Set up a Base URL (with Glitch)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/)
  * [Set up a Base URL (with ngrok)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/)



You can use any programming language, framework, or architecture to handle requests from Canva, but the examples in this documentation use [Express.js⁠(opens in a new tab or window)](https://expressjs.com).

## Step 2: Set up the required endpoints

A publish extension that uses the **Flat list** layout must support the following endpoints:

  * [`POST /publish/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/)
  * [`POST /publish/resources/get`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/)
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
    
    
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      // code goes here
    
    });
    
    
    
    
    app.post("/publish/resources/get", async (request, response) => {
    
      // code goes here
    
    });
    
    
    
    
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
  3. For the **Layout** option, select **Flat list**.
  4. Enable **Display search field**.
  5. For the **Output file types** option, select the types of files a user can publish to the destination platform. The example in this tutorial requires the file types to be **JPG** and **PNG**.
  6. For the **Max number of pages** field, enter the maximum number of pages that a user can publish of their design. The example in this tutorial requires the number of pages to be **1**.



Any changes to the form save automatically.

## Step 5: Provide a list of folders

When a user opens a publish extension that uses the **Flat list** layout, Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/publish/resources/find

BASH

Copy

This endpoint must respond with an array of `"CONTAINER"` resources. Canva then renders these resources as folders that the user can select.

![](https://www.canva.dev/_next/static/media/img-4ed7354914.9d335fc4.png)

The following snippet demonstrates how to create an array of `"CONTAINER"` resources based on the contents of the `public` directory:
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      const dirPath = path.join(__dirname, "public");
    
    
    
    
      await fs.ensureDir(dirPath);
    
    
    
    
      const files = await fs.readdir(dirPath, {
    
        withFileTypes: true,
    
      });
    
    
    
    
      const resources = files
    
        .filter((dirent) => dirent.isDirectory())
    
        .map((folder) => {
    
          return {
    
            type: "CONTAINER",
    
            id: path.join(dirPath, folder.name),
    
            name: folder.name,
    
            isOwner: true,
    
            readOnly: false,
    
          };
    
        });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources,
    
      });
    
    });

JAVASCRIPT

Copy

In this case, the `id` of the resource is the path of directory.

## Step 6: Verify that the selected folder still exists

When a user is ready to publish their design, they must select a folder.

When the user selects a folder, a **Save** button appears, and when the user clicks this button, Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/publish/resources/get

BASH

Copy

The body of this request includes an `id` property that contains the ID of the selected folder.

The endpoint must verify that:

  * The folder still exists on the destination platform.
  * The user still has access to the folder on the destination platform.



To do this, the endpoint must respond with the details of the selected folder.

The following snippet demonstrates how to verify the existence of a folder in the `public` directory (and how to respond with an error if the folder doesn't exist):
    
    
    app.post("/publish/resources/get", async (request, response) => {
    
      const dirPathExists = await fs.pathExists(request.body.id);
    
    
    
    
      if (!dirPathExists) {
    
        response.send({
    
          type: "ERROR",
    
          errorCode: "NOT_FOUND",
    
        });
    
        return;
    
      }
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resource: {
    
          type: "CONTAINER",
    
          id: request.body.id,
    
          name: path.basename(request.body.id),
    
          isOwner: true,
    
          readOnly: false,
    
        },
    
      });
    
    });

JAVASCRIPT

Copy

In this case, the `id` property in the body of the request is the path of the selected folder.

## Step 7: Upload the user's design

When the extension verifies that the selected folder exists, Canva immediately sends a `POST` request to the following endpoint:
    
    
    <base_url>/publish/resources/upload

BASH

Copy

The body of the request contains:

  * An array of assets. Each asset has a `url` property, which the extension must use to download the asset.
  * A `parent` property, which contains the `id` of the selected folder.



The endpoint must use this information to download the user's design to the destination platform. The following snippet demonstrates how to download assets to the selected folder:
    
    
    app.post("/publish/resources/upload", async (request, response) => {
    
      const [asset] = request.body.assets;
    
      const image = await jimp.read(asset.url);
    
      const filePath = path.join(request.body.parent, asset.name);
    
      await image.writeAsync(filePath);
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        url: url.format({
    
          protocol: request.protocol,
    
          host: request.get("host"),
    
          pathname: path.join(request.body.parent, asset.name),
    
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
    
    const jimp = require("jimp");
    
    const path = require("path");
    
    const url = require("url");
    
    const fs = require("fs-extra");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      const dirPath = path.join(__dirname, "public");
    
    
    
    
      await fs.ensureDir(dirPath);
    
    
    
    
      const files = await fs.readdir(dirPath, {
    
        withFileTypes: true,
    
      });
    
    
    
    
      const resources = files
    
        .filter((dirent) => dirent.isDirectory())
    
        .map((folder) => {
    
          return {
    
            type: "CONTAINER",
    
            id: path.join(dirPath, folder.name),
    
            name: folder.name,
    
            isOwner: true,
    
            readOnly: false,
    
          };
    
        });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources,
    
      });
    
    });
    
    
    
    
    app.post("/publish/resources/get", async (request, response) => {
    
      const dirPathExists = await fs.pathExists(request.body.id);
    
    
    
    
      if (!dirPathExists) {
    
        response.send({
    
          type: "ERROR",
    
          errorCode: "NOT_FOUND",
    
        });
    
        return;
    
      }
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resource: {
    
          type: "CONTAINER",
    
          id: request.body.id,
    
          name: path.basename(request.body.id),
    
          isOwner: true,
    
          readOnly: false,
    
        },
    
      });
    
    });
    
    
    
    
    app.post("/publish/resources/upload", async (request, response) => {
    
      const [asset] = request.body.assets;
    
      const image = await jimp.read(asset.url);
    
      const filePath = path.join(request.body.parent, asset.name);
    
      await image.writeAsync(filePath);
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        url: url.format({
    
          protocol: request.protocol,
    
          host: request.get("host"),
    
          pathname: path.join(request.body.parent, asset.name),
    
        }),
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
