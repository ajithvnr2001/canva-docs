---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/
title: onProductSelect - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:02.066553+00:00
---

# onProductSelect - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# onProductSelect

Registers a callback that runs when a user selects a product via the product catalog.

Copy page

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onProductSelect = (opts) => {
    
        // the user has selected a product via the catalog
    
        console.log(opts);
    
      };
    
    
    
    
      api.showCatalog({
    
        onProductSelect,
    
      });
    
    })();

JAVASCRIPT

Copy

You don't need to directly access the properties in the `opts` object. You only need to pass them straight into the [`createDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/) method.

## Parameters

To understand the meaning of the **Volatile** column, see the definition of [Volatile parameters](https://www.canva.dev/docs/print-partnerships/reference/glossary/#volatile-parameters) in the [Glossary](https://www.canva.dev/docs/print-partnerships/reference/glossary/).

Parameter| Type| Required| Volatile| Description  
---|---|---|---|---  
`opts`| object| Yes| N/A| Options for configuring the editor.  
`opts.analyticsCorrelationId`| string| Yes| Yes| The ID to track user interactions with a design.  
`opts.designSource`| string| Yes| Yes| Whether a design is created [via a product catalog](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/#create-a-design-via-the-catalog-to-editor-path) or [by directly launching the Canva editor](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/#create-a-design-via-the-direct-to-editor-path).  
`opts.partnerProductId`| string| Yes| No| The ID of a partner's product. Some examples are `"Poster11x17in"` and `"Banner96x24in"`. A partner product ID determines the dimensions, the templates, the furniture (if applicable), and the [export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/) to apply for a design. A partner may provide a partner product ID to Canva beforehand. This may match with a product ID in a partner's back-end, such as SKU or internal system identifier. If partner doesn't provide a partner product ID, Canva assigns one for each product.  
`opts.productId`| string| Yes| Yes| The ID of a type of partner's product. Some examples are `"posters"` and `"cards"`.  
`opts.productSizeOptionId`| string| Yes| Yes| The ID of the partner's product size option.  
`opts.maxPages`| number| Yes| No| The maximum number of pages a user can print. The default value is 2.  
`opts.minPages`| number| Yes| No| The minimum number of pages a user can print. The default value is 1.  
`opts.template`| string| No| Yes| The ID of a template.
