---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/
title: Handle page refreshes - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.123470+00:00
---

# Handle page refreshes - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Handle page refreshes

Copy page

If the user is editing a design and refreshes the page that hosts the integration's iframe, the default behavior forces them to navigate back to their design. This means they can't bookmark and easily return to their design.

This guide explains how to use URL query parameters to re-open the user's design when they refresh the page.

There are other techniques for handling page refreshes, such as using local storage or even backend persistence.

## Step 1: When the user opens a design, create a `designId` query parameter

The following snippet demonstrates how to detect when a user opens a design with the [`onDesignOpen`](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/) method and set the `designId` of the design as a query parameter:
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onDesignOpen = (opts) => {
    
        history.replaceState(
    
          null,
    
          document.title,
    
          window.location.href + "?designId=" + opts.designId
    
        );
    
      };
    
    
    
    
      const onProductSelect = (opts) => {
    
        api.createDesign({
    
          ...opts,
    
          onDesignOpen,
    
        });
    
      };
    
    
    
    
      api.showCatalog({
    
        onProductSelect,
    
      });
    
    })();

JAVASCRIPT

Copy

## Step 2: If the `designId` query parameter exists, open the design with the `editDesign` method

The following snippet checks if the `designId` query parameter exists, and if it does, opens the design with the [`editDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/) method:
    
    
    if (queryString.get("designId")) {
    
      api.editDesign({
    
        designId: queryString.get("designId"),
    
      });
    
      return;
    
    }

JAVASCRIPT

Copy

If the `designId` query parameter does not exist, a new design is created.

## Example
    
    
    <!DOCTYPE html>
    
    <html lang="en">
    
      <head>
    
        <meta charset="UTF-8" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
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
    
              apiKey: "<partner_api_key>",
    
              autoAuthToken: "<auto_auth_token>",
    
              container: document.getElementById("container"),
    
            });
    
    
    
    
            const queryString = new URLSearchParams(location.search);
    
    
    
    
            if (queryString.get("designId")) {
    
              api.editDesign({
    
                designId: queryString.get("designId"),
    
              });
    
              return;
    
            }
    
    
    
    
            const onDesignOpen = (opts) => {
    
              history.replaceState(
    
                null,
    
                document.title,
    
                window.location.href + "?designId=" + opts.designId
    
              );
    
            };
    
    
    
    
            const onProductSelect = (opts) => {
    
              api.createDesign({
    
                ...opts,
    
                onDesignOpen,
    
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
