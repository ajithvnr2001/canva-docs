---
url: https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/
title: Show the product catalog - Tutorials - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:04.398894+00:00
---

# Show the product catalog - Tutorials - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/

Tutorials

[Getting started](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/)[Set up a web server](https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/)[Initialize the Partnership SDK](https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/)[Show the product catalog](https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/)[Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/)[Create a new design](https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/)[Preview the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/)[Purchase the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/)

# Show the product catalog

Copy page

The product catalog is a ready-made landing page that partners can embed in their website. You can use the product catalog get an integration up and running as quickly as possible.

This part of the tutorial explains how to embed the product catalog in a web page.

An integration doesn't have to use Canva's product catalog—you can create a custom landing page—but this is beyond the scope of this tutorial.

## Step 1: Create a container

The Partnership SDK needs a `HTMLElement` for rendering the product catalog and editor. To provide this element, create a `div` element between the `body` tags of the `index.ejs` file:
    
    
    <div id="container"></div>

HTML

Copy

Then pass this element into the `initialize` method via the `container` property:
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<%= partnerApiKey %>",
    
        container: document.getElementById("container"),
    
      });
    
    })();

JAVASCRIPT

Copy

## Step 2: Call the `showCatalog` method

The `showCatalog` method renders the product catalog in the `container` element:
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<%= partnerApiKey %>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      api.showCatalog({});
    
    })();

JAVASCRIPT

Copy

This method expects an object as its only argument. For the time being, pass through an empty object.

If you refresh the page, the SDK renders the product catalog in an iframe.

## Step 3: Fix the container's height and margins

By default, the iframe that contains the product catalog doesn't extend to the full width and height of the page.

To fix this, add the following styles to the page:
    
    
    <style type="text/css">
    
      body,
    
      html {
    
        margin: 0;
    
      }
    
    
    
    
      #container {
    
        height: 100vh;
    
      }
    
    </style>

HTML

Copy

These styles extend the catalog's iframe to the edges of the viewport.

Some partners also choose to render a header at the top of the page, before the iframe.

## Step 4: Select a product or template

If you select a product or template, nothing happens.

This is because you need to pass a function to the `showCatalog` method that opens the editor. For that to be possible though, you must first [Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/).

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
    
            });
    
    
    
    
            api.showCatalog({});
    
          })();
    
        </script>
    
      </body>
    
    </html>

HTML

Copy
