---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/
title: initialize - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.513794+00:00
---

# initialize - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# initialize

Initializes the Partnership SDK.

Copy page

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
        locale: "fr-CA",
    
      });
    
    })();

JAVASCRIPT

Copy

## Parameters

Parameter| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Options for initializing the SDK.  
`opts.apiKey`| string| Yes| The integration's [Partner API key](https://www.canva.dev/docs/print-partnerships/concepts/credentials/).  
`opts.autoAuthToken`| string| No| The integration's authAuthToken.  
`opts.container`| `HTMLElement`| No| The element where the SDK renders the product catalog and the Canva editor.  
`opts.locale`| string| No| The [language code](https://www.canva.dev/docs/print-partnerships/reference/languages/#supported-languages-for-the-product-catalog) the SDK uses to render the product catalog and the Canva editor. If not set, the SDK determines the locale from the user's browser settings. If set, the SDK ignores the user's browser settings.  
  
## Returns

Parameter| Type| Required| Description  
---|---|---|---  
`api`| object| Yes| API methods for defining the behavior of the integration.  
`api.showCatalog`| function| Yes| Refer to [`showCatalog`](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/).  
`api.createDesign`| function| Yes| Refer to [`createDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/).  
`api.editDesign`| function| Yes| Refer to [`editDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/).
