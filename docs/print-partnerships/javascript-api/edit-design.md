---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/
title: editDesign - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.415359+00:00
---

# editDesign - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# editDesign

Opens an existing design in the editor.

Copy page

When a user edits an existing design, they are editing the live version of the design. Any changes they make are not reflected in an already purchased artwork.

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      // Keep track of a design's ID
    
      let designId;
    
    
    
    
      const onProductSelect = (opts) => {
    
        api.createDesign({
    
          ...opts,
    
          onDesignOpen: (opts) => {
    
            designId = opts.designId;
    
          },
    
        });
    
      };
    
    
    
    
      // The user creates a new design
    
      api.showCatalog({
    
        onProductSelect,
    
      });
    
    
    
    
      // If the user navigates away from the design,
    
      // you can open it again at a later time.
    
      api.editDesign({ designId });
    
    })();

JAVASCRIPT

Copy

## Parameters

Parameter| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Options for configuring the editor.  
`opts.designId`| string| Yes| The ID of an existing design to open in the editor.  
`opts.onArtworkCreate` (deprecated)| function| No| See [onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/). This parameter is superseded by `opts.onMultiArtworkCreate`.  
`opts.onBackClick`| function| No| Refer to [onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/).  
`opts.onDesignOpen`| function| No| Refer to [onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/).  
`opts.onMultiArtworkCreate`| function| No| See [onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/).  
`opts.publishLabel`| string| No| A label for the editor's **Publish** button.  
  
By default, a user can print a minimum of 1 page and a maximum of 2 pages per design. To change these settings, [raise a ticket](https://www.canva.dev/docs/print-partnerships/support/general-support/#create-support-tickets) and request Canva to set them up in the backend. Don't set them via the `opts.minPages` and `opts.maxPages` parameters. The SDK ignores these parameters.
