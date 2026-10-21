---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/
title: onDesignSelect - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.800917+00:00
---

# onDesignSelect - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# onDesignSelect

Registers a callback that runs when a user selects a design via the "My Designs" carousel.

Copy page

The "My Designs" carousel only appears if the `onDesignSelect` callback is registered.

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onDesignSelect = (opts) => {
    
        // the user has selected a design via the catalog
    
        console.log(opts);
    
      };
    
    
    
    
      api.showCatalog({
    
        onDesignSelect,
    
      });
    
    })();

JAVASCRIPT

Copy

## Parameters

To understand the meaning of the **Volatile** column, see the definition of [Volatile parameters](https://www.canva.dev/docs/print-partnerships/reference/glossary/#volatile-parameters) in the [Glossary](https://www.canva.dev/docs/print-partnerships/reference/glossary/).

Parameter| Type| Required| Volatile| Description  
---|---|---|---|---  
`opts`| object| Yes| N/A| Information about the selected design.  
`opts.designId`| string| Yes| No| The ID of an existing design.  
`opts.maxPages`| number| Yes| No| The maximum number of pages a user can print for the design's associated product. The default value is 2.  
`opts.partnerProductId`| string| Yes| No| The ID of a product in Canva's back-end. A partner product ID determines the dimensions, the templates, the furniture (if applicable), and the [export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/) to apply for a design. A partner may provide a partner product ID to Canva beforehand. This may match with a product ID in a partner's back-end, such as SKU or internal system identifier. If partner doesn't provide a partner product ID, Canva assigns one for each product.
