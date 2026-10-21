---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/
title: createDesign - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.294051+00:00
---

# createDesign - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# createDesign

Creates a design in the editor.

Copy page

The `createDesign` method accepts different parameters depending on whether or not a design is created via a product catalog.

## Create a design via the catalog-to-editor path

The [catalog-to-editor](https://www.canva.dev/docs/print-partnerships/concepts/user-journey/#select) path lets an integration create a design via a product catalog.

### Usage
    
    
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
    
    
    
    
      const onArtworkCreate = (opts) => {
    
        // the user has finished proofing their design
    
        console.log(opts);
    
      };
    
    
    
    
      const onProductSelect = (opts) => {
    
        api.createDesign({
    
          ...opts,
    
          onBackClick,
    
          onArtworkCreate,
    
        });
    
      };
    
    
    
    
      api.showCatalog({
    
        onProductSelect,
    
      });
    
    })();

JAVASCRIPT

Copy

### Parameters

Parameter| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Options for creating a new design in the Canva editor.  
`opts.onArtworkCreate` (deprecated)| function| Yes| See [onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/). This parameter is superseded by `opts.onMultiArtworkCreate`.  
`opts.onBackClick`| function| Yes| See [onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/).  
`opts.onMultiArtworkCreate`| function| Yes| See [onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/).  
`opts.designId`| string| No| The ID of an existing design. If present, a new design is created as a copy of the existing design.  
`opts.designSource`| string| No| Whether a design is created via a product catalog or [by directly launching the Canva editor](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/#create-a-design-via-the-direct-to-editor-path). Set to `"catalog"`.  
`opts.onDesignClose`| function| No| See [onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/).  
`opts.onDesignOpen`| function| No| See [onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/).  
`opts.publishLabel`| string| No| A label for the editor's **Publish** button.  
`opts.title`| string| No| The title of the design. The default title is `Untitled design`. The title is used in the exported design's filename. Users can change the title later in the Canva editor.  
  
By default, a user can print a minimum of 1 page and a maximum of 2 pages per design. To change these settings, [raise a ticket](https://www.canva.dev/docs/print-partnerships/support/general-support/#create-support-tickets) and request Canva to set them up in the backend. Don't set them via the `opts.minPages` and `opts.maxPages` parameters. The SDK ignores these parameters.

## Create a design via the direct-to-editor path

The [direct-to-editor](https://www.canva.dev/docs/print-partnerships/concepts/user-journey/#direct-to-editor) path lets an integration create a design by directly launching the Canva editor.

### Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
      });
    
    
    
    
      const onBackClick = () => {
    
        // the user has clicked the "Back" button in the editor's header
    
        console.log("You clicked the 'Back' button!");
    
      };
    
    
    
    
      const onArtworkCreate = (opts) => {
    
        console.log(opts);
    
      };
    
    
    
    
      api.createDesign({
    
        partnerProductId: "Poster11x17",
    
        designSource: "direct",
    
        onBackClick,
    
        onArtworkCreate,
    
      });
    
    })();

JAVASCRIPT

Copy

### Parameters

Parameter| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Options for creating a new design in the Canva editor.  
`opts.designSource`| string| Yes| Whether a design is created [via a product catalog](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/#create-a-design-via-the-catalog-to-editor-path) or by directly launching the Canva editor. Set to `"direct"`.  
`opts.onArtworkCreate` (deprecated)| function| Yes| See [onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/). This parameter is superseded by `opts.onMultiArtworkCreate`.  
`opts.onBackClick`| function| Yes| See [onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/).  
`opts.onMultiArtworkCreate`| function| Yes| See [onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/).  
`opts.partnerProductId`| string| Yes| The ID of a partner's product. Some examples are `"Poster11x17in"` and `"Banner96x24in"`. A partner product ID determines the dimensions, the templates, the furniture (if applicable), and the [export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/) to apply for a design. A partner may provide a partner product ID to Canva beforehand. This may match with a product ID in a partner's back-end, such as SKU or internal system identifier. If partner doesn't provide a partner product ID, Canva assigns one for each product.  
`opts.designId`| string| No| The ID of an existing design. If present, a new design is created as a copy of the existing design.  
`opts.onDesignClose`| function| No| See [onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/).  
`opts.onDesignOpen`| function| No| See [onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/).  
`opts.publishLabel`| string| No| A label for the editor's **Publish** button.  
`opts.title`| string| No| The title of the design. The default title is `Untitled design`. The title is used in the exported design's filename. Users can change the title later in the Canva editor.  
  
By default, a user can print a minimum of 1 page and a maximum of 2 pages per design. To change these settings, [raise a ticket](https://www.canva.dev/docs/print-partnerships/support/general-support/#create-support-tickets) and request Canva to set them up in the backend. Don't set them via the `opts.minPages` and `opts.maxPages` parameters. The SDK ignores these parameters.
