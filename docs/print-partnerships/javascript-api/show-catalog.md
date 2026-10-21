---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/
title: showCatalog - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:02.708903+00:00
---

# showCatalog - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# showCatalog

Renders an iframe that contains the product catalog.

Copy page

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auth_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      api.showCatalog({
    
        // options go here
    
      });
    
    })();

JAVASCRIPT

Copy

## Parameters

Parameter| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Options for configuring the product catalog.  
`opts.onProductSelect`| function| No| Refer to [onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/).  
`opts.onDesignSelect`| function| No| Refer to [onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/).  
`opts.tag`| string| No| The _tag_ of a product catalog. This is only relevant when you've [set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/).  
  
The "My Designs" carousel only appears if the `onDesignSelect` callback is registered.
