---
url: https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/
title: Initialize the Partnership SDK - Tutorials - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:04.005945+00:00
---

# Initialize the Partnership SDK - Tutorials - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/

Tutorials

[Getting started](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/)[Set up a web server](https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/)[Initialize the Partnership SDK](https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/)[Show the product catalog](https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/)[Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/)[Create a new design](https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/)[Preview the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/)[Purchase the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/)

# Initialize the Partnership SDK

Copy page

The Partnership SDK is a JavaScript library for developing the frontend of a Print Partnership integration.

You can use the Partnership SDK to:

  * Embed Canva's product catalog in a web page.
  * Embed the Canva editor in a web page.
  * Control what happens when a user interacts with the catalog or editor.



This part of the tutorial explains how to initialize the Partnership SDK.

## Step 1: Render a home page

In the `src/views` directory, create an `index.ejs` file:
    
    
    <!DOCTYPE html>
    
    <html lang="en">
    
      <head>
    
        <meta charset="UTF-8" />
    
        <meta
    
          name="viewport"
    
          content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover"
    
        />
    
        <title>Print Partnership Example</title>
    
        <script src="https://sdk.canva.com/partnership.js"></script>
    
      </head>
    
      <body></body>
    
    </html>

HTML

Copy

This file is the integration's home page.

If you're using the China version of the SDK, replace `https://sdk.canva.com/partnership.js` with `https://sdk.canva.cn/partnership.js`.

Next, create a route in the `server.js` file:
    
    
    app.get("/", async (request, response) => {
    
      response.render("index", { partnerApiKey: process.env.PARTNER_API_KEY });
    
    });

JAVASCRIPT

Copy

This route should:

  * Render the "index" template when users visit the root path.
  * Pass the [Partner API key](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-key) into the template.



With this code in place, <http://localhost:3000>[⁠(opens in a new tab or window)](http://localhost:3000) renders an empty page.

The Partner API key is _not_ a sensitive value. Even so, load it via an environment variable to make it easier to switch between test and production credentials.

## Step 2: Embed the Partnership SDK

In the `index.ejs` file, copy the following code before the closing `body` tag:
    
    
    <script src="https://sdk.canva.com/partnership.js"></script>

HTML

Copy

To verify that the SDK is loading, log the `Canva.Partnership` object to the JavaScript Console:
    
    
    console.log(Canva.Partnership);

JAVASCRIPT

Copy

Then refresh the page.

## Step 3: Initialize the SDK

To initialize the SDK, call the `initialize` method:
    
    
    <script type="text/javascript">
    
      (async () => {
    
        const api = await Canva.Partnership.initialize();
    
      })();
    
    </script>

HTML

Copy

This method expects an object with an `apiKey` property. This property must contain the integration's Partner API key:
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<%= partnerApiKey %>",
    
      });
    
    })();

JAVASCRIPT

Copy

`<%= partnerApiKey %>` is the EJS syntax for outputting a value. In this case, it outputs the value of the `partnerApiKey` variable that's passed it from the route.

After making this change, refresh the browser and open the JavaScript Console. If there's no errors, the SDK is initialized.

The examples in this documentation use the async/await syntax for asynchronous functions, which isn't supported in all browsers. In a production environment, we recommend using [Babel⁠(opens in a new tab or window)](https://babeljs.io/) or [TypeScript⁠(opens in a new tab or window)](https://www.typescriptlang.org/) to ensure maximum compatibility.

## Example

### src/views/index.ejs
    
    
    <!DOCTYPE html>
    
    <html lang="en">
    
      <head>
    
        <meta charset="UTF-8" />
    
        <meta
    
          name="viewport"
    
          content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover"
    
        />
    
        <title>Print Partnership Example</title>
    
        <script src="https://sdk.canva.com/partnership.js"></script>
    
      </head>
    
      <body>
    
        <script type="text/javascript">
    
          (async () => {
    
            const api = await Canva.Partnership.initialize({
    
              apiKey: "<%= partnerApiKey %>",
    
            });
    
          })();
    
        </script>
    
      </body>
    
    </html>

HTML

Copy

### src/server.js
    
    
    require("dotenv").config();
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.set("views", "./src/views");
    
    app.set("view engine", "ejs");
    
    
    
    
    app.use(express.json());
    
    app.use(express.urlencoded({ extended: true }));
    
    
    
    
    app.get("/", async (request, response) => {
    
      response.render("index", { partnerApiKey: process.env.PARTNER_API_KEY });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
