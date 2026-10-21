---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/
title: onDesignOpen - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.889439+00:00
---

# onDesignOpen - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# onDesignOpen

Registers a callback that runs when a user opens a new or existing design in the editor.

Copy page

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onDesignOpen = (opts) => {
    
        // the user has opened a new or existing design
    
        console.log(opts);
    
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

## Parameters

To understand the meaning of the **Volatile** column, see the definition of [Volatile parameters](https://www.canva.dev/docs/print-partnerships/reference/glossary/#volatile-parameters) in the [Glossary](https://www.canva.dev/docs/print-partnerships/reference/glossary/).

Parameter| Type| Required| Volatile| Description  
---|---|---|---|---  
`opts`| object| Yes| N/A| Information about the opened design.  
`opts.designId`| string| Yes| No| The ID of the user's design.  
`opts.designTitle`| string| Yes| No| The title of the user's design.
