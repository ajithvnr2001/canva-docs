---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/
title: Messages - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:52.602927+00:00
---

# Messages - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Messages

Require users to provide a message before publishing their design.

Copy page

When a user publishes a design via a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/), the extension can require them to provide a message. Canva then includes this message in the [upload request](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/).

![](https://www.canva.dev/_next/static/media/img-ebe6dd5e6c.871433ad.jpg)

This tutorial explains how to require users to provide a message when publishing a design.

## Step 1: Enable the message field

By default, Canva doesn't prompt users to provide a message. You must enable the feature.

Enable the feature only if the destination platform can use the message in a purposeful way. Requiring a message for no particular reason will only deteriorate the user experience.

To enable the message field:

  1. Navigate to an app via the Developer Portal.
  2. From the **Extensions** page, expand the **Publish** panel.
  3. Enable **Require a message**.
  4. (Optional) Customize the maximum length of the message via the **Max message length** field.



## Step 2: Handle requests with messages

When a user publishes a design, Canva sends a `POST` request to the following endpoint:
    
    
    <base_url>/publish/resources/upload

BASH

Copy

You can access the user's message in the body of the request, via the `message` property:
    
    
    app.post("/publish/resources/upload", async (request, response) => {
    
      console.log(request.body.message);
    
    });

JAVASCRIPT

Copy

## Limitations

  * You can't customize the placeholder text of the message field.
  * If the message field is enabled, it must be required. It can't be enabled and optional.



## Example
    
    
    const express = require("express");
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/publish/resources/upload", async (request, response) => {
    
      // Do something with the message
    
      console.log(request.body.message);
    
    
    
    
      // Respond to the request
    
      response.send({
    
        type: "SUCCESS",
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
