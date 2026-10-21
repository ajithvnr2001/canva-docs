---
url: https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/
title: Calculate an autoAuthToken - Tutorials - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:03.601365+00:00
---

# Calculate an autoAuthToken - Tutorials - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/

Tutorials

[Getting started](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/)[Set up a web server](https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/)[Initialize the Partnership SDK](https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/)[Show the product catalog](https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/)[Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/)[Create a new design](https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/)[Preview the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/)[Purchase the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/)

# Calculate an autoAuthToken

Copy page

When a user opens the Canva editor via a partner's website, Canva attempts to automatically (and invisibly) create an account for that user. This ensures that:

  * Users don't have to create a Canva account.
  * Users can access their designs and uploaded media on return visits.



To accomplish this, an integration must calculate a JSON Web Token (JWT) for each user. Canva refers to the calculated token as an _autoAuthToken_.

This part of the tutorial explains how to calculate an autoAuthToken.

## Step 1: Install jwt-simple

There are many libraries for calculating JWTs. For Node.js, [jwt-simple⁠(opens in a new tab or window)](https://www.npmjs.com/package/jwt-simple) is one of the easier ones to use.

To install jwt-simple, run the following command:
    
    
    npm install jwt-simple --save

BASH

Copy

Then include the library at the top of the `server.js` file:
    
    
    const jwt = require("jwt-simple");

JAVASCRIPT

Copy

## Step 2: Create a payload

A payload is an object with the following properties:

  * `iss` \- The integration's [Partner API key](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-key).
  * `sub` \- The ID of the end-user (that is, the ID of the partner's customer).
  * `iat` \- The creation time of the token as a UNIX timestamp (in seconds).
  * `exp` \- The expiry time of the token as a UNIX timestamp (in seconds).



The SDK's `initialize` method needs access to the autoAuthToken, so create the payload in the home page route:
    
    
    app.get("/", async (request, response) => {
    
      // Get the current time
    
      const now = Math.floor(new Date().getTime() / 1000);
    
    
    
    
      // Create a payload
    
      const payload = {
    
        iss: process.env.PARTNER_API_KEY,
    
        sub: "12345",
    
        iat: now,
    
        exp: now + 60 * 30,
    
      };
    
    
    
    
      response.render("index", { partnerApiKey: process.env.PARTNER_API_KEY });
    
    });

JAVASCRIPT

Copy

The expiry time in the payload must be less than 12 hours after the creation time.

## Step 3: Calculate the autoAuthToken

To calculate the autoAuthToken, use the `jwt.encode` function:
    
    
    const autoAuthToken = jwt.encode(payload, process.env.PARTNER_API_SECRET);

JAVASCRIPT

Copy

This function accepts two arguments: the payload and the integration's [Partner API secret](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-secret).

## Step 4: Initialize the SDK with the autoAuthToken

Pass the autoAuthToken into the `index.ejs` file via the `render` method:
    
    
    response.render("index", {
    
      autoAuthToken,
    
      partnerApiKey: process.env.PARTNER_API_KEY,
    
    });

JAVASCRIPT

Copy

Then, in the `index.ejs` file, pass the autoAuthToken into the `initialize` method:
    
    
    const api = await Canva.Partnership.initialize({
    
      apiKey: "<%= partnerApiKey %>",
    
      container: document.getElementById("container"),
    
      autoAuthToken: "<%= autoAuthToken %>",
    
    });

JAVASCRIPT

Copy

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
    
        <style type="text/css">
    
          body,
    
          html {
    
            margin: 0;
    
          }
    
    
    
    
          #container {
    
            height: 100vh;
    
          }
    
        </style>
    
      </head>
    
      <body>
    
        <div id="container"></div>
    
        <script type="text/javascript">
    
          (async () => {
    
            const api = await Canva.Partnership.initialize({
    
              apiKey: "<%= partnerApiKey %>",
    
              container: document.getElementById("container"),
    
              autoAuthToken: "<%= autoAuthToken %>",
    
            });
    
    
    
    
            api.showCatalog({});
    
          })();
    
        </script>
    
      </body>
    
    </html>

HTML

Copy

### src/server.js
    
    
    require("dotenv").config();
    
    const express = require("express");
    
    const jwt = require("jwt-simple");
    
    
    
    
    const app = express();
    
    
    
    
    app.set("views", "./src/views");
    
    app.set("view engine", "ejs");
    
    
    
    
    app.use(express.json());
    
    app.use(express.urlencoded({ extended: true }));
    
    
    
    
    app.get("/", async (request, response) => {
    
      // Get the current time
    
      const now = Math.floor(new Date().getTime() / 1000);
    
    
    
    
      // Create a payload
    
      const payload = {
    
        iss: process.env.PARTNER_API_KEY,
    
        sub: "12345",
    
        iat: now,
    
        exp: now + 60 * 30,
    
      };
    
    
    
    
      // Calculate the autoAuthToken
    
      const autoAuthToken = jwt.encode(payload, process.env.PARTNER_API_SECRET);
    
    
    
    
      response.render("index", {
    
        autoAuthToken,
    
        partnerApiKey: process.env.PARTNER_API_KEY,
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
