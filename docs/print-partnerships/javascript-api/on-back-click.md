---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/
title: onBackClick - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.657408+00:00
---

# onBackClick - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# onBackClick

Registers a callback that runs when a user clicks the Back button in the editor's header.

Copy page

This function does _not_ run when then the user uses the native "back" feature in their browser.

If you don't register the `onBackClick` callback, the "Back" button still appears in the Canva editor, but nothing happens when the user clicks it.

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onBackClick = () => {
    
        // the user has clicked the "Back" button in the editor's header
    
        console.log("You clicked the 'Back' button!");
    
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

JAVASCRIPT

Copy
