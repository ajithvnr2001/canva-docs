---
url: https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/
title: onMultiArtworkCreate - JavaScript API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:02.007510+00:00
---

# onMultiArtworkCreate - JavaScript API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/

JavaScript API

[createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)[editDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)[initialize](https://www.canva.dev/docs/print-partnerships/javascript-api/initialize/)[onArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-artwork-create/)[onBackClick](https://www.canva.dev/docs/print-partnerships/javascript-api/on-back-click/)[onDesignClose](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/)[onDesignSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/)[onMultiArtworkCreate](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/)[onProductSelect](https://www.canva.dev/docs/print-partnerships/javascript-api/on-product-select/)[showCatalog](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/)

# onMultiArtworkCreate

Registers a callback that runs when a user finishes proofing their design.

Copy page

The Partnership SDK refers to a proofed design as an _artwork_.

## Usage
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onMultiArtworkCreate = (opts) => {
    
        opts.artworks.forEach((artwork) => {
    
          console.log(artwork);
    
        });
    
      };
    
    
    
    
      const onProductSelect = (opts) => {
    
        api.createDesign({
    
          ...opts,
    
          onMultiArtworkCreate,
    
        });
    
      };
    
    
    
    
      api.showCatalog({
    
        onProductSelect,
    
      });
    
    })();

JS

Copy

## Parameters

Name| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Information about a user's proofed design.  
`opts.artworks`| Array<[Artwork](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/#artwork)>| Yes| List of artworks representing a user's proofed designs.  
  
## Types

### Artwork

Represents an individual artwork.

#### Properties

To understand the meaning of the **Volatile** column, see the definition of [Volatile parameters](https://www.canva.dev/docs/print-partnerships/reference/glossary/#volatile-parameters) in the [Glossary](https://www.canva.dev/docs/print-partnerships/reference/glossary/).

Name| Type| Required| Volatile| Description  
---|---|---|---|---  
`previewImages`| Array<string>| Yes| Yes| A list of URLs for previewing a low-resolution version of the artwork. For JPG and PNG file formats, there's a separate URL for each page. For PDF file formats, there's one URL for the entire preview. The URL is in the form `https://partnership-artwork.canva.com/<export_file>`. If you're using the China version of the SDK, the TLD is `.cn` instead of `.com`. You can take the necessary security measures to protect the URL from any malicious attacks.  
`previewImageSrc` (deprecated)| string| Yes| Yes| The URL of a low-resolution preview of the artwork. This parameter is superseded by `previewImages`.  
`artworkId`| string| Yes| No| The ID of the user's artwork.  
`artworkTitle`| string| Yes| No| The title of the user's artwork.  
`designId`| string| Yes| No| The design ID of the user's artwork.  
`pageCount`| number| Yes| No| The number of the pages in the artwork.  
`partnerProductId`| string| Yes| No| The ID of a product in Canva's back-end. A partner product ID determines the dimensions, the templates, the furniture (if applicable), and the [export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/) to apply for a design. A partner may provide a partner product ID to Canva beforehand. This may match with a product ID in a partner's back-end, such as SKU or internal system identifier. If partner doesn't provide a partner product ID, Canva assigns one for each product.
