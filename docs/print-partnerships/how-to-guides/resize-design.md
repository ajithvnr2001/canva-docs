---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/
title: Resize designs - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.980687+00:00
---

# Resize designs - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Resize designs

Copy page

After a user creates a design for a product, they may want to change its dimensions to suit another product. This lets a user print the same design on different products.

This document explains how to resize an existing design for another product.

## How resizing works

When a partner resizes an existing design, the partnership SDK:

  * Duplicates the design.
  * Applies properties of another product.
  * Assigns a separate design ID.



By duplicating a design, users can preserve their original design. Canva enables the feature to duplicate designs only on request.

Some examples of the properties you can apply are height, width, and units. Canva maintains the properties for all products of an integration. Canva identifies each product with a partner product ID. To resize an existing design, a partner must pass a design ID and a partner product ID.

## Step 1: Request Canva to enable the feature

Partners must request Canva to enable the feature to duplicate designs.

To raise a request:

  * Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  * Select **Integration support**.
  * Fill out the required fields.
  * Click **Send**.



## Step 2: Get the design ID

To get the ID of an existing design, use the [`onDesignOpen`](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/) callback when a user creates the design.

The following shows how to store the design ID in a variable:
    
    
    let userDesignId;
    
    
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: '<partner_api_key>',
    
        autoAuthToken: '<auto_auth_token>',
    
        container: document.getElementById('container'),
    
      });
    
    
    
    
      api.showCatalog({
    
        onProductSelect: (opts) => {
    
          api.createDesign({
    
            ...opts,
    
            onDesignOpen: ({ designId }) => userDesignId = designId;
    
          });
    
        },
    
      });
    
    })();

JAVASCRIPT

Copy

Partners can save the design ID locally or in a database. Partners can associate the design ID with the current user.

## Step 3: Resize the design

To resize a design, call the `createDesign` method, and pass the design ID and the partner product ID.
    
    
    api.createDesign({
    
      designId: userDesignId,
    
      partnerProductId: "Poster11x17in",
    
      designSource: "direct",
    
      onBackClick,
    
      onArtworkCreate,
    
    });

JAVASCRIPT

Copy

The Partnership SDK uses the existing design as the starting point of a new design.

## Limitations

  * Users can't resize their design from inside the Canva editor.
  * Users can resize only their designs, not others'.


