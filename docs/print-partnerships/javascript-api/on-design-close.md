---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/
title: onDesignClose - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:02.611137+00:00
---

# onDesignClose - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# onDesignClose

Registers a callback that runs when a user closes the Canva editor.

Copy page

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onDesignClose = () => {
    
        // the user has closed the Canva editor
    
        console.log("You closed the Canva editor!");
    
      };
    
    
    
    
      const onProductSelect = (opts) => {
    
        api.createDesign({
    
          ...opts,
    
          onDesignClose,
    
        });
    
      };
    
    
    
    
      api.showCatalog({
    
        onProductSelect,
    
      });
    
    })();

JAVASCRIPT

Copy
