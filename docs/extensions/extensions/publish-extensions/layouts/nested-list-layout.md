---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/
title: Nested list layout - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:54.426943+00:00
---

# Nested list layout - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Nested list layout

Create a publish extension with the "Nested list" layout.

Copy page

A [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) adds a publish destination to Canva. Users can then publish their design to this destination via Canva's **Publish** menu.

This tutorial explains how to create a publish extension that uses the **Nested list** layout. This layout is intended for platforms that:

  * Let users users to organize content into folders.
  * Supported nested folders.



![](https://www.canva.dev/_next/static/media/img-0b77524971.ca7f4dfd.png)

To learn about the other layouts available for publish extensions, see [Layouts](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/).

## Step 1: Set up a Base URL

In the Developer Portal, publish extensions have a **Base URL** field. This indicates that the extension must provide the URL of a server that can receive and respond to HTTP requests from Canva.

To set up a **Base URL** , refer to either of the following guides:

  * [Set up a Base URL (with Glitch)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/)
  * [Set up a Base URL (with ngrok)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/)



You can use any programming language, framework, or architecture to handle requests from Canva, but the examples in this documentation use [Express.js⁠(opens in a new tab or window)](https://expressjs.com).

## Step 2: Set up the required endpoints

A publish extension that uses the **Nested list** layout must support the following endpoints:

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
  3. For the **Layout** option, select **Nested list**.
  4. Enable **Display search field**.
  5. For the **Output file types** option, select the types of files a user can publish to the destination platform. The example in this tutorial requires the file types to be **JPG** and **PNG**.
  6. For the **Max number of pages** field, enter the maximum number of pages that a user can publish of their design. The example in this tutorial requires the number of pages to be **1**.



Any changes to the form save automatically.

## Step 5: Provide a list of files and folders

When a user opens a publish extension that uses the **Nested list** layout, Canva sends a request to the following endpoint:
    
    
    <base_url>/publish/resources/find

BASH

Copy

The endpoint must respond with an array of _resources_.

Each resource must have a `type` property of `"CONTAINER"` or `"IMAGE"`. Canva renders `"CONTAINER"` resources as folders and `"IMAGE"` resources as files. Users can select folders but can't interact with files.

![](https://www.canva.dev/_next/static/media/img-0b77524971.ca7f4dfd.png)

The following snippet demonstrates how to use the contents of the `public` directory create a list of resources:
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      const dirPath = path.join(__dirname, "public");
    
    
    
    
      await fs.ensureDir(dirPath);
    
    
    
    
      const entries = await fs.readdir(dirPath, {
    
        withFileTypes: true,
    
      });
    
    
    
    
      const folders = entries
    
        .filter((dirent) => dirent.isDirectory())
    
        .map((dirent) => {
    
          return {
    
            type: "CONTAINER",
    
            id: path.join(dirPath, dirent.name),
    
            name: dirent.name,
    
            isOwner: true,
    
            readOnly: false,
    
          };
    
        });
    
    
    
    
      const files = entries
    
        .filter((dirent) => !dirent.isDirectory())
    
        .map((dirent) => {
    
          return {
    
            type: "IMAGE",
    
            id: path.join(dirPath, dirent.name),
    
            name: dirent.name,
    
            isOwner: true,
    
            readOnly: false,
    
          };
    
        });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources: [...folders, ...files],
    
      });
    
    });

JAVASCRIPT

Copy

In this case, the `id` of the resource is the path of the file or directory. This lets you access the path of a selected folder from the extension's other endpoints.

When a resource's `isOwner` property is `false` or `readOnly` property is `true`, the resource is greyed out and the user can't interact with it (even if it's a folder).

When a response contains files and folders, the folders must appear before the files.

## Step 6: Detect when a user opens a folder

If a user selects a folder, Canva sends another request to the following endpoint:
    
    
    <base_url>/publish/resources/find

BASH

Copy

The body of this request includes a `containerId` property that contains the `id` of the folder. The extension must respond with resources that belong to the folder.

In this case, the value of the `containerId` property is a directory path, so the only change you need to make is to set the `dirPath` variable to the value of the `containerId`:
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      const dirPath = request.body.containerId || path.join(__dirname, "public");
    
    
    
    
      await fs.ensureDir(dirPath);
    
    
    
    
      const entries = await fs.readdir(dirPath, {
    
        withFileTypes: true,
    
      });
    
    
    
    
      const folders = entries
    
        .filter((dirent) => dirent.isDirectory())
    
        .map((dirent) => {
    
          return {
    
            type: "CONTAINER",
    
            id: path.join(dirPath, dirent.name),
    
            name: dirent.name,
    
            isOwner: true,
    
            readOnly: false,
    
          };
    
        });
    
    
    
    
      const files = entries
    
        .filter((dirent) => !dirent.isDirectory())
    
        .map((dirent) => {
    
          return {
    
            type: "IMAGE",
    
            id: path.join(dirPath, dirent.name),
    
            name: dirent.name,
    
            isOwner: true,
    
            readOnly: false,
    
          };
    
        });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources: [...folders, ...files],
    
      });
    
    });

JAVASCRIPT

Copy

But the `containerId` property isn't defined in the initial request, so it's important to provide the `public` directory as a fallback.

Based on these changes, opening the extension via the **Publish** menu displays the contents of the `public` directory.

## Step 7: Verify that the selected folder still exists

When a user is ready to publish their design, they can click the **Choose** button.

After clicking the **Choose** button, a **Save** button appears. When the user clicks this button, Canva sends a request to the the following endpoint:
    
    
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

In this case, the `id` property in the request body is the path of the selected folder.

If the user doesn't select a folder before clicking the **Choose** button, Canva doesn't send this request.

## Step 8: Upload the user's design

When the extension verifies that the selected folder exists, Canva sends a request to the following endpoint:
    
    
    <base_url>/publish/resources/upload

BASH

Copy

The request body contains an array of assets. Each asset has a `url`, which the extension must use to download the assets to the destination platform.

If the user selects a folder before publishing their design, the request body also includes a `parent` property that contains the `id` of the selected folder. The extension must use the `parent` property to publish the design to the correct location.

The following snippet demonstrates how to download assets to the requested folder:
    
    
    app.post("/publish/resources/upload", async (request, response) => {
    
      // Get the first asset from the "assets" array
    
      const [asset] = request.body.assets;
    
    
    
    
      // Download the asset
    
      const image = await jimp.read(asset.url);
    
      const filePath = path.join(request.body.parent, asset.name);
    
      await image.writeAsync(filePath);
    
    
    
    
      // Respond with the URL of the published design
    
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

**Note:**If you'd like to release your app to Canva's users, the `url` property must point to a page that lets users view and action the published design in context on the destination platform. For guidelines on providing a publish link, see Provide a link to the published design.

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
    
      const dirPath = request.body.containerId || path.join(__dirname, "public");
    
    
    
    
      await fs.ensureDir(dirPath);
    
    
    
    
      const entries = await fs.readdir(dirPath, {
    
        withFileTypes: true,
    
      });
    
    
    
    
      const folders = entries
    
        .filter((dirent) => dirent.isDirectory())
    
        .map((dirent) => {
    
          return {
    
            type: "CONTAINER",
    
            id: path.join(dirPath, dirent.name),
    
            name: dirent.name,
    
            isOwner: true,
    
            readOnly: false,
    
          };
    
        });
    
    
    
    
      const files = entries
    
        .filter((dirent) => !dirent.isDirectory())
    
        .map((dirent) => {
    
          return {
    
            type: "IMAGE",
    
            id: path.join(dirPath, dirent.name),
    
            name: dirent.name,
    
            isOwner: true,
    
            readOnly: false,
    
          };
    
        });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources: [...folders, ...files],
    
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
