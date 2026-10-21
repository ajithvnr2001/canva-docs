---
url: https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/
title: Purchase the user's artwork - Tutorials - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:05.064794+00:00
---

# Purchase the user's artwork - Tutorials - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/

Tutorials

[Getting started](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/)[Set up a web server](https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/)[Initialize the Partnership SDK](https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/)[Show the product catalog](https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/)[Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/)[Create a new design](https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/)[Preview the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/)[Purchase the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/)

# Purchase the user's artwork

Copy page

When a user purchases a print of their artwork, a partner must purchase the print-quality version of the artwork from Canva. The partner can then print the artwork and send it to the customer.

## Step 1: Get the required order details

When a user purchases a print of their artwork, a partner must provide Canva with details about the order, such as the price of each item in the order. Canva uses this data to verify the revenue a partner owes. You can find the list of required properties in the [API reference](https://www.canva.dev/docs/print-partnerships/rest-api/purchase-artwork/).

For this tutorial, pass placeholder amounts into the "cart" view:
    
    
    app.get("/cart", async (request, response) => {
    
      response.render("cart", {
    
        artworkId: request.query.artworkId,
    
        artworkTitle: request.query.artworkTitle,
    
        previewImageSrc: request.query.previewImageSrc,
    
        order: "OR_12345672",
    
        item: "IT_12345672-003",
    
        sku: "PS034509",
    
        quantity: 5,
    
        currency: "USD",
    
        grossAmount: 65.5,
    
        discountAmount: 6.55,
    
        netAmount: 58.95,
    
      });
    
    });

JAVASCRIPT

Copy

Then render these values in the view:
    
    
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
    
        <h2>Order #<%= order %></h2>
    
        <table>
    
          <thead>
    
            <tr>
    
              <td>Item ID</td>
    
              <td>Product SKU</td>
    
              <td>Artwork ID</td>
    
              <td>Artwork title</td>
    
              <td>Preview</td>
    
              <td>Quantity</td>
    
              <td>Price (per item)</td>
    
            </tr>
    
          </thead>
    
          <tbody>
    
            <tr>
    
              <td><%= item %></td>
    
              <td><%= sku %></td>
    
              <td><%= artworkId %></td>
    
              <td><%= artworkTitle %></td>
    
              <td><a href="<%= previewImageSrc %>">Click here</a></td>
    
              <td><%= quantity %></td>
    
              <td>$<%= grossAmount %> <%= currency %></td>
    
            </tr>
    
          </tbody>
    
        </table>
    
        <p>Price (with discounts): $<%= netAmount * quantity %> <%= currency %></p>
    
      </body>
    
    </html>

HTML

Copy

## Step 2: Create an order form

To simulate the ordering of a print, add a form to the `cart.ejs` file:
    
    
    <form method="POST" action="/process-order">
    
      <input type="hidden" name="artworkId" value="<%= artworkId %>" />
    
      <input type="hidden" name="currency" value="<%= currency %>" />
    
      <input type="hidden" name="discountAmount" value="<%= discountAmount %>" />
    
      <input type="hidden" name="grossAmount" value="<%= grossAmount %>" />
    
      <input type="hidden" name="item" value="<%= item %>" />
    
      <input type="hidden" name="netAmount" value="<%= netAmount %>" />
    
      <input type="hidden" name="order" value="<%= order %>" />
    
      <input type="hidden" name="quantity" value="<%= quantity %>" />
    
      <input type="hidden" name="sku" value="<%= sku %>" />
    
      <button>Confirm order</button>
    
    </form>

HTML

Copy

When a user submits this form, it sends a `POST` request to `/process-order`, which is an endpoint that doesn't exist (yet). The hidden fields contain the data that Canva requires for processing orders.

## Step 3: Purchase the artwork from Canva

In the `server.js` file, create a route that receives `POST` requests:
    
    
    app.post("/process-order", async (request, response) => {
    
      // code goes here
    
    });

JAVASCRIPT

Copy

In this route, send a `POST` request to the following endpoint:
    
    
    https://api.canva.com/_tpi/partnership/<partner_id>/artworks/<artwork_id>

BASH

Copy

In this request:

  * Replace `<partner_id>` with the [Partner ID](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-id).
  * Replace `<artwork_id>` with the ID of the user's artwork.
  * Set the `Authorization` header to the [Artwork API secret](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#artwork-api-secret).
  * Include a `purchaseConfirmation` object in the body. The object must contain the data that Canva requires to process the order, the SKU of each product.



An integration must send a separate request for each unique item in an order. This means a single order may require multiple requests.

For security reasons, you _must_ send this request from a backend server. If you send this request via a browser, Canva rejects the request.

This example destructures the required data from the request body and uses the [axios⁠(opens in a new tab or window)](https://www.npmjs.com/package/axios) library to send a request:
    
    
    app.post("/process-order", async (request, response) => {
    
      // Get the required data from the incoming request body
    
      const {
    
        artworkId,
    
        currency,
    
        discountAmount,
    
        grossAmount,
    
        item,
    
        netAmount,
    
        order,
    
        quantity,
    
        sku,
    
      } = request.body;
    
    
    
    
      // Send a request to Canva
    
      const { data } = await axios.request({
    
        baseURL: "https://api.canva.com",
    
        url: `/_tpi/partnership/${process.env.PARTNER_ID}/artworks/${artworkId}`,
    
        method: "post",
    
        headers: {
    
          Authorization: process.env.ARTWORK_API_SECRET,
    
        },
    
        data: {
    
          purchaseConfirmation: {
    
            currency,
    
            discountAmount: parseFloat(discountAmount),
    
            grossAmount: parseFloat(grossAmount),
    
            item,
    
            netAmount: parseFloat(netAmount),
    
            order,
    
            quantity: parseInt(quantity),
    
            sku,
    
          },
    
        },
    
      });
    
    
    
    
      // Log the results
    
      console.log(data);
    
    });

JAVASCRIPT

Copy

The response body contains a `productionFile` property that contains the URL of the print-quality artwork.

Canva charges partners for each purchase made in a production environment. To avoid being charged while testing an integration, use the test credentials.

For the complete API reference, refer to [Purchase an artwork](https://www.canva.dev/docs/print-partnerships/rest-api/purchase-artwork/).

## Step 4: Print the user's artwork

A real integration should download the print-quality version of the user's artwork and send it off for printing. For this tutorial, simply redirect users to the print-quality artwork:
    
    
    // Redirect users to the print-quality artwork
    
    response.redirect(data.productionFile);

JAVASCRIPT

Copy

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
    
        <h2>Order #<%= order %></h2>
    
        <table>
    
          <thead>
    
            <tr>
    
              <td>Item ID</td>
    
              <td>Product SKU</td>
    
              <td>Artwork ID</td>
    
              <td>Artwork title</td>
    
              <td>Preview</td>
    
              <td>Quantity</td>
    
              <td>Price (per item)</td>
    
            </tr>
    
          </thead>
    
          <tbody>
    
            <tr>
    
              <td><%= item %></td>
    
              <td><%= sku %></td>
    
              <td><%= artworkId %></td>
    
              <td><%= artworkTitle %></td>
    
              <td><a href="<%= previewImageSrc %>">Click here</a></td>
    
              <td><%= quantity %></td>
    
              <td>$<%= grossAmount %> <%= currency %></td>
    
            </tr>
    
          </tbody>
    
        </table>
    
    
    
    
        <p>Price (with discounts): $<%= netAmount * quantity %> <%= currency %></p>
    
    
    
    
        <form method="POST" action="/process-order">
    
          <input type="hidden" name="artworkId" value="<%= artworkId %>" />
    
          <input type="hidden" name="currency" value="<%= currency %>" />
    
          <input
    
            type="hidden"
    
            name="discountAmount"
    
            value="<%= discountAmount %>"
    
          />
    
          <input type="hidden" name="grossAmount" value="<%= grossAmount %>" />
    
          <input type="hidden" name="item" value="<%= item %>" />
    
          <input type="hidden" name="netAmount" value="<%= netAmount %>" />
    
          <input type="hidden" name="order" value="<%= order %>" />
    
          <input type="hidden" name="quantity" value="<%= quantity %>" />
    
          <input type="hidden" name="sku" value="<%= sku %>" />
    
          <button>Confirm order</button>
    
        </form>
    
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
    
    const axios = require("axios");
    
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
    
        order: "OR_12345672",
    
        item: "IT_12345672-003",
    
        sku: "PS034509",
    
        quantity: 5,
    
        currency: "USD",
    
        grossAmount: 65.5,
    
        discountAmount: 6.55,
    
        netAmount: 58.95,
    
      });
    
    });
    
    
    
    
    app.post("/process-order", async (request, response) => {
    
      // Get the required data from the incoming request body
    
      const {
    
        artworkId,
    
        currency,
    
        discountAmount,
    
        grossAmount,
    
        item,
    
        netAmount,
    
        order,
    
        quantity,
    
        sku,
    
      } = request.body;
    
    
    
    
      // Send a request to Canva
    
      const { data } = await axios.request({
    
        baseURL: "https://api.canva.com",
    
        url: `/_tpi/partnership/${process.env.PARTNER_ID}/artworks/${artworkId}`,
    
        method: "post",
    
        headers: {
    
          Authorization: process.env.ARTWORK_API_SECRET,
    
        },
    
        data: {
    
          purchaseConfirmation: {
    
            currency,
    
            discountAmount: parseFloat(discountAmount),
    
            grossAmount: parseFloat(grossAmount),
    
            item,
    
            netAmount: parseFloat(netAmount),
    
            order,
    
            quantity: parseInt(quantity),
    
            sku,
    
          },
    
        },
    
      });
    
    
    
    
      // Redirect users to the print-quality artwork
    
      response.redirect(data.productionFile);
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
