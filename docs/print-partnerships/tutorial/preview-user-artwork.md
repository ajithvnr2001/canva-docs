---
url: https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/
title: Preview the users's artwork - Tutorials - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:04.298969+00:00
---

# Preview the users's artwork - Tutorials - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/

Tutorials

[Getting started](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/)[Set up a web server](https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/)[Initialize the Partnership SDK](https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/)[Show the product catalog](https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/)[Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/)[Create a new design](https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/)[Preview the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/)[Purchase the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/)

# Preview the users's artwork

Copy page

When a user finishes their design, they click the **Publish** button to begin the proofing process. This lets the user verify that their design will be printed as expected.

When a user finishes proofing their design, the integration is responsible for defining the next step and sending them there. Typically though, users want to:

  * Look at a preview of their finished artwork.
  * Add the printed version of the artwork to a shopping cart.



This part of the tutorial explains how to access a preview of the user's artwork and set up a (very basic) shopping cart.

## Step 1: Detect when a user has finished proofing their design

After the `initialize` method, create an `onArtworkCreate` function:
    
    
    const onArtworkCreate = (opts) => {
    
      // code goes here
    
    };

JAVASCRIPT

Copy

This function receives an `opts` objects that contains information about the user's artwork, including its ID, title, and a URL for previewing the artwork.

Then pass this function into the `createDesign` method:
    
    
    const onProductSelect = (opts) => {
    
      api.createDesign({
    
        ...opts,
    
        onBackClick,
    
        onArtworkCreate,
    
      });
    
    };

JAVASCRIPT

Copy

## Step 2: Create a shopping cart

When a user has finished proofing their design, partners typically:

  * Add the design to a shopping cart.
  * Show the user a preview of their design.



Then, if the users purchases the design, the partner sends it off for printing.

To create a (very basic) shopping cart, create a `cart.ejs` file in the `src/views` directory:
    
    
    <!DOCTYPE html>
    
    <html lang="en">
    
      <head>
    
        <meta charset="UTF-8" />
    
        <meta
    
          name="viewport"
    
          content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover"
    
        />
    
        <title>Shopping cart</title>
    
      </head>
    
      <body>
    
        <h1>Shopping cart</h1>
    
        <table>
    
          <thead>
    
            <tr>
    
              <td>Artwork ID</td>
    
              <td>Artwork title</td>
    
              <td>Preview</td>
    
            </tr>
    
          </thead>
    
          <tbody>
    
            <tr>
    
              <td><%= artworkId %></td>
    
              <td><%= artworkTitle %></td>
    
              <td><a href="<%= previewImageSrc %>">Click here</a></td>
    
            </tr>
    
          </tbody>
    
        </table>
    
      </body>
    
    </html>

HTML

Copy

Then, in the `server.js` file, set up a route that renders this view:
    
    
    app.get("/cart", async (request, response) => {
    
      response.render("cart");
    
    });

JAVASCRIPT

Copy

But while the page renders, it doesn't have the data it needs—the `artworkId`, `artworkTitle`, or `previewImageSrc`—to render correctly.

## Step 3: Redirect users to the shopping cart

From the `onArtworkCreate` function, redirect users to the shopping cart and append the properties from the `opts` object to the URL as a query string:
    
    
    const onArtworkCreate = (opts) => {
    
      // Create a query string
    
      const params = new URLSearchParams();
    
    
    
    
      // Add opts (artworkId, etc) to query string
    
      Object.keys(opts).forEach((key) => {
    
        params.append(key, opts[key]);
    
      });
    
    
    
    
      // Redirect the user to shopping cart
    
      window.location.href = `/cart?${params.toString()}`;
    
    };

JAVASCRIPT

Copy

Based on this change, you can pass the data from the `opts` object into the "cart" view:
    
    
    app.get("/cart", async (request, response) => {
    
      response.render("cart", {
    
        artworkId: request.query.artworkId,
    
        artworkTitle: request.query.artworkTitle,
    
        previewImageSrc: request.query.previewImageSrc,
    
      });
    
    });

JAVASCRIPT

Copy

If you navigate through the proofing process, you're taken to the shopping cart page and shown a link to preview the artwork.

## Example

### src/views/cart.ejs
    
    
    <!DOCTYPE html>
    
    <html lang="en">
    
      <head>
    
        <meta charset="UTF-8" />
    
        <meta
    
          name="viewport"
    
          content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover"
    
        />
    
        <title>Shopping cart</title>
    
      </head>
    
      <body>
    
        <h1>Shopping cart</h1>
    
        <table>
    
          <thead>
    
            <tr>
    
              <td>Artwork ID</td>
    
              <td>Artwork title</td>
    
              <td>Preview</td>
    
            </tr>
    
          </thead>
    
          <tbody>
    
            <tr>
    
              <td><%= artworkId %></td>
    
              <td><%= artworkTitle %></td>
    
              <td><a href="<%= previewImageSrc %>">Click here</a></td>
    
            </tr>
    
          </tbody>
    
        </table>
    
      </body>
    
    </html>

HTML

Copy

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
    
    
    
    
            const onBackClick = () => {
    
              console.log(
    
                "You clicked the 'Back' button in the Canva editor's header."
    
              );
    
            };
    
    
    
    
            const onArtworkCreate = (opts) => {
    
              // Create a query string
    
              const params = new URLSearchParams();
    
    
    
    
              // Add opts (artworkId, etc) to query string
    
              Object.keys(opts).forEach((key) => {
    
                params.append(key, opts[key]);
    
              });
    
    
    
    
              // Redirect the user to shopping cart
    
              window.location.href = `/cart?${params.toString()}`;
    
            };
    
    
    
    
            const onProductSelect = (opts) => {
    
              api.createDesign({
    
                ...opts,
    
                onBackClick,
    
                onArtworkCreate,
    
              });
    
            };
    
    
    
    
            api.showCatalog({
    
              onProductSelect,
    
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
    
    
    
    
    app.get("/cart", async (request, response) => {
    
      response.render("cart", {
    
        artworkId: request.query.artworkId,
    
        artworkTitle: request.query.artworkTitle,
    
        previewImageSrc: request.query.previewImageSrc,
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
