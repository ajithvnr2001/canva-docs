---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/
title: onArtworkCreate - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.573237+00:00
---

# onArtworkCreate - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# onArtworkCreate

Registers a callback that runs when a user finishes proofing their design.

Copy page

`onArtworkCreate` is [deprecated](https://www.canva.dev/docs/print-partnerships/stay-up-to-date/deprecated-obsolete-features/). It's superseded by [`onMultiArtworkCreate`](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/).

The Partnership SDK refers to a proofed design as an _artwork_.

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onArtworkCreate = (opts) => {
    
        // the user has finished proofing their design
    
        console.log(opts);
    
      };
    
    
    
    
      const onProductSelect = (opts) => {
    
        api.createDesign({
    
          ...opts,
    
          onArtworkCreate,
    
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

Name| Type| Required| Volatile| Description  
---|---|---|---|---  
`opts`| object| Yes| N/A| Information about the user's proofed design.  
`opts.previewImages`| Array<string>| Yes| Yes| A list of URLs for previewing a low-resolution version of the artwork. For JPG and PNG file formats, there's a separate URL for each page. For PDF file formats, there's one URL for the entire preview. The URL is in the form `https://partnership-artwork.canva.com/<export_file>`. If you're using the China version of the SDK, the TLD is `.cn` instead of `.com`. You can take the necessary security measures to protect the URL from any malicious attacks.  
`opts.previewImageSrc` (deprecated)| string| Yes| Yes| The URL of a low-resolution preview of the artwork. This parameter is superseded by `opts.previewImages`.  
`opts.artworkId`| string| Yes| No| The ID of the user's artwork.  
`opts.artworkTitle`| string| Yes| No| The title of the user's artwork.  
`opts.pageCount`| number| Yes| No| The number of the pages in the artwork.  
`opts.partnerProductId`| string| Yes| No| The ID of a product in Canva's back-end. A partner product ID determines the dimensions, the templates, the furniture (if applicable), and the [export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/) to apply for a design. A partner may provide a partner product ID to Canva beforehand. This may match with a product ID in a partner's back-end, such as SKU or internal system identifier. If partner doesn't provide a partner product ID, Canva assigns one for each product.
