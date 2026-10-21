---
url: https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/
title: CORS - Content extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:49.907288+00:00
---

# CORS - Content extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/

Content extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)[Public vs. private content](https://www.canva.dev/docs/extensions/extensions/content-extensions/public-private-content/)[Continuation](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/content-extensions/search/)[Authentication](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)[CORS](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/)

Content types

[Overview](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/)[Images](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/images/)[Embeds](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/embeds/)[Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/)[Containers](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/containers/)

# CORS

Learn how to fix Cross-Origin Resource Sharing errors.

Copy page

While developing a content extension, you might find that:

  * Thumbnails don't appear in the side panel.
  * Full-sized images disappear after dragging them into the design.



To fix these issues:

  1. Open the JavaScript Console.
  2. Click **View**.
  3. Click **Developer**.
  4. Click **Developer Tools**.



You'll probably see the following error message:
    
    
    No 'Access-Control-Allow-Origin' header is present on the requested resource.

BASH

Copy

This error is caused by Cross-Origin Resource Sharing (CORS).

## What is CORS?

CORS is a security feature of web browsers that blocks client-side HTTP requests between different origins. An origin is a unique combination of a domain, protocol, and port.

These, for instance, are all different origins:

  * `http://abc.com`
  * `https://abc.com`
  * `https://abc.com:3000`
  * `https://abc.com:9090`
  * `https://abc123.com`



When a content extension can't load images, it's because Canva is attempting to fetch the images from a different origin—the server that is serving the images—and that origin is blocking the request.

## Verifying CORS errors

If you're troubleshooting CORS errors, it's useful to check if a URL supports CORS without having to continually reload a content extension.

To check if a URL supports CORS:

  1. Visit [test-cors.org⁠(opens in a new tab or window)](https://test-cors.org).
  2. Enter the URL of the image into the **Remote URL** field.
  3. Click **Send Request**.



Errors will appears in the **Results** tab and JavaScript Console.

## Fixing CORS errors

When Canva fetches an image, the response to that request needs to include an `Access-Control-Allow-Origin` header. This header should have one of the following values:

  * `*`
  * `https://www.canva.com`



The wildcard origin says, "Let any origin access this resource." But a wildcard origin is only valid for unauthenticated requests and, if you're not careful, it can pose a security risk.

The `https://www.canva.com` origin says, "Block requests that don't originate from Canva." The `Access-Control-Allow-Origin` header only allows you to provide a single origin, which can be too restrictive, but there are [workarounds for multiple origins](https://www.canva.dev/docs/extensions/extensions/content-extensions/cross-origin-resource-sharing/#setting-multiple-origins).

There are three primary ways to set the value of the `Access-Control-Allow-Origin` header:

  * At the server-level.
  * At the application-level.
  * With a proxy.



## Setting the origin at the server-level

If you have access to the server that serves the images for a content extension, the `Access-Control-Allow-Origin` header can be set at the server-level.

This example demonstrates how to set the header on Apache servers using the `.htaccess` file:
    
    
    <IfModule mod_headers.c>
    
        Header set Access-Control-Allow-Origin "*"
    
    </IfModule>

APACHECONF

Copy

If you're not running Apache, refer to [w3.org/wiki/CORS_Enabled⁠(opens in a new tab or window)](https://www.w3.org/wiki/CORS_Enabled#At_the_HTTP_Server_level...) for alternate implementations.

## Setting the origin at the application-level

If you have access to the source code for the application that serves the images for a content extension, the `Access-Control-Allow-Origin` header can be set at the application-level.

This example demonstrates how to set the header in Express.js using the `response.header` method:
    
    
    const express = require("express");
    
    const app = express();
    
    
    
    
    app.get("/", async (request, response) => {
    
      response.header("Access-Control-Allow-Origin", "*");
    
      response.send("CORS is enabled for this route.");
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy

If you're not using Express.js, refer to [w3.org/wiki/CORS_Enabled⁠(opens in a new tab or window)](https://www.w3.org/wiki/CORS_Enabled#At_the_Web_Application_level...) for alternate implementations.

## Setting the origin with a proxy

If you don't have access to the server or application that serves the images for a content extension, you can fetch images through a proxy that sets the `Access-Control-Allow-Origin` headers.

### Fetching images through a hosted proxy

If you'd like to get up-and-running as quickly as possible, consider signing up for a [Cloudinary⁠(opens in a new tab or window)](https://cloudinary.com) account and using their [Fetch remote images⁠(opens in a new tab or window)](https://cloudinary.com/documentation/fetch_remote_images) feature.

This feature can take a URL that doesn't support CORS:
    
    
    https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg

Copy

...and turn it into a URL that does support CORS:
    
    
    https://res.cloudinary.com/demo/image/fetch/https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg

Copy

### Fetching images through a self-hosted proxy

If you'd prefer to self-host a proxy, set up an endpoint that:

  * Fetches an image from a URL.
  * Gets the binary data of the image.
  * Sets the `Access-Control-Allow-Origin` header.
  * Responds with the image data.



This is an example of how to set up a proxy with Express.js and [jimp⁠(opens in a new tab or window)](https://www.npmjs.com/package/jimp):
    
    
    const express = require("express");
    
    const jimp = require("jimp");
    
    
    
    
    const app = express();
    
    
    
    
    app.get("/", async (request, response) => {
    
      // Fetch image from URL
    
      const image = await jimp.read(request.query.url);
    
    
    
    
      // Get the image data
    
      const mimeType = await image.getMIME();
    
      const buffer = await image.getBufferAsync(mimeType);
    
      const imageData = buffer.toString("base64");
    
    
    
    
      // Set the `Access-Control-Allow-Origin` header
    
      response.header("Access-Control-Allow-Origin", "*");
    
    
    
    
      // Respond with the image data
    
      response.send(imageData);
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy

To fetch images through this proxy, start the server:
    
    
    node index.js

BASH

Copy

Then append the image URL to the endpoint URL as a query parameter:
    
    
    http://localhost:3000/?url=<image_url>

BASH

Copy

You can view a live demo of this project as [a Glitch project⁠(opens in a new tab or window)](https://glitch.com/edit/#!/express-cors?path=server.js).

## Setting multiple origins

If you need to support multiple origins for the `Access-Control-Allow-Origin` header:

  1. Create a whitelist of supported origins.
  2. When a request is received, check the origin.
  3. If the origin is in the whitelist, set the `Access-Control-Allow-Origin` header to that origin.



This can be done at the server-level:
    
    
    <IfModule mod_headers.c>
    
        SetEnvIf Origin "http(s)?://(www\.)?(canva.com|google.com|example.com)$" AccessControlAllowOrigin=$0
    
        Header add Access-Control-Allow-Origin %{AccessControlAllowOrigin}e env=AccessControlAllowOrigin
    
        Header merge Vary Origin
    
    </IfModule>

APACHECONF

Copy

...or at the application-level:
    
    
    const express = require("express");
    
    const app = express();
    
    
    
    
    const whitelist = ["https://www.canva.com", "https://canva.com"];
    
    
    
    
    app.get("/", async (request, response) => {
    
      const origin = whitelist.find(request.headers["Access-Control-Allow-Origin"]);
    
    
    
    
      if (origin) {
    
        response.header("Access-Control-Allow-Origin", origin);
    
      }
    
    
    
    
      response.send("CORS is enabled for this route.");
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
