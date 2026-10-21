---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/
title: Publish extensions - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:47.358084+00:00
---

# Publish extensions - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Publish extensions

What are publish extensions? Why create one?

Copy page

A publish extension adds a publish destination to Canva. This destination appears in the **Publish** menu. Users can then publish their designs to the destination platform.

![](https://www.canva.dev/_next/static/media/img-3d6ae7b361.a7931833.jpg)

To create a publish extension from scratch, check out the [Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/) guide.

## Examples of publish extensions

These are some examples of apps with publish extensions:

  * [Pinterest⁠(opens in a new tab or window)](https://www.canva.com/apps/pinterest) \- Post designs to your boards on Pinterest.
  * [Slack⁠(opens in a new tab or window)](https://www.canva.com/apps/slack) \- Share designs to your channels on Slack.
  * [Twitter⁠(opens in a new tab or window)](https://www.canva.com/apps/twitter) \- Post designs on Twitter.



You can find more examples at [canva.com/apps⁠(opens in a new tab or window)](https://www.canva.com/apps).

## Supported publish formats

A publish extension can publish the user's design in any of the following formats:

  * JPG
  * PNG
  * PDF
  * PPTX



You can configure the supported formats via the Developer Portal.

Designs published as a PNG don't have transparent backgrounds.

## How users experience publish extensions

Users can find publish extensions via the **Publish** menu.

![](https://www.canva.dev/_next/static/media/img-2773052e33.b4ff6189.jpeg)

When a user opens a publish extension, the user experience depends on the [layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/) of the extension, which you can configure via the Developer Portal. This is an example of the user experience of an extension that uses the **Basic** layout:

![](https://www.canva.dev/_next/static/media/img-3d6ae7b361.a7931833.jpg)

When a user clicks the **Save** button, Canva sends a request to the destination platform to upload the user's design. The extension then responds with a URL where the user can view their design on the destination platform.

![](https://www.canva.dev/_next/static/media/img-b9ee05c626.6306d85e.jpeg)

With additional configuration, a publish extension can also:

  * [Let users search for a folder](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)
  * [Require users to provide a message before publishing their design](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)
  * [Require users to authenticate with the destination platform](https://www.canva.dev/docs/extensions/platform-concepts/authentication/)



## How publish extensions work

At its most basic, a publish extension is a REST API.

Canva expects this API to have the following endpoints:

  * [`/publish/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/)
  * [`/publish/resources/get`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/)
  * [`/publish/resources/upload`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/)



As a user interacts with a publish extension via Canva's UI, Canva sends requests to these endpoints and expects to receive responses in a format that it understands.

The `/publish/resources/find` and `/publish/resources/get` endpoints are only required for extensions that use the **Flat list** or **Nested list** layout.

### Request-response cycle

The request-response cycle of a publish extension depends on the extension's layout. This is the request-response cycle of a publish extension that uses the **Basic** layout:

![](https://www.canva.dev/_next/static/media/img-fa28193c4b.0c86706e.png)

Canva sends additional requests if the extension supports [authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).

## Limitations

  * Publish extensions can't publish designs as videos, GIFs, or HTML. Some apps, like the Twitter app, can publish videos because they're created by Canva.
  * You're not allowed to create publish extensions that let users print their designs on physical products.



## Example
    
    
    const express = require("express");
    
    const jimp = require("jimp");
    
    const path = require("path");
    
    const url = require("url");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/publish/resources/upload", async (request, response) => {
    
      // Download the image
    
      const [asset] = request.body.assets;
    
      const image = await jimp.read(asset.url);
    
    
    
    
      // Write the file to disk
    
      const filePath = path.join(__dirname, "public", asset.name);
    
      await image.writeAsync(filePath);
    
    
    
    
      // Respond to the request
    
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
