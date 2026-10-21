---
url: https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/
title: Create a new design - Tutorials - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:03.711530+00:00
---

# Create a new design - Tutorials - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/

Tutorials

[Getting started](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/)[Set up a web server](https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/)[Initialize the Partnership SDK](https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/)[Show the product catalog](https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/)[Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/)[Create a new design](https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/)[Preview the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/)[Purchase the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/)

# Create a new design

Copy page

By default, nothing happens when a user selects a product or template via the product catalog. This is because an integration needs to explicitly define the behavior.

This part of the tutorial explains how to:

  * Detect when a user selects a product or template.
  * Create and open a new design in the Canva editor.



## Step 1: Detect when a user selects a product or template

After the `initialize` method, create a function named `onProductSelect`:
    
    
    const onProductSelect = (opts) => {
    
      console.log("Product selected.");
    
    };

JAVASCRIPT

Copy

Then pass this function into the `showCatalog` method:
    
    
    api.showCatalog({
    
      onProductSelect,
    
    });

JAVASCRIPT

Copy

This function runs when a user selects a product. It receives an `opts` object that contains information about the selected product, such as its dimensions and category.

## Step 2: Create a new design in the Canva editor

In the `onProductSelect` function, call the `createDesign` method.
    
    
    const onProductSelect = (opts) => {
    
      api.createDesign({
    
        ...opts,
    
      });
    
    };

JAVASCRIPT

Copy

The `...opts` is an [object spread operator⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) that merges the `opts` object with any other properties. This enables the `opts` object from the `onProductSelect` function to be passed into the `createDesign` method. This ensures that the `createDesign` method can still access the relevant product and template data.

The `createDesign` method also requires an `onBackClick` callback function. This function runs when a user clicks the back button in the Canva editor's header. You should use this function to return the user to the previous screen.

For this tutorial, use the `onBackClick` function to log a message to the JavaScript Console:
    
    
    const onBackClick = () => {
    
      console.log("You clicked the 'Back' button in the Canva editor's header.");
    
    };
    
    
    
    
    const onProductSelect = (opts) => {
    
      api.createDesign({
    
        ...opts,
    
        onBackClick,
    
      });
    
    };

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
    
    
    
    
            const onBackClick = () => {
    
              console.log(
    
                "You clicked the 'Back' button in the Canva editor's header."
    
              );
    
            };
    
    
    
    
            const onProductSelect = (opts) => {
    
              api.createDesign({
    
                ...opts,
    
                onBackClick,
    
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
