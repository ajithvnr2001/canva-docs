---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/
title: Custom landing page - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.467526+00:00
---

# Custom landing page - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Custom landing page

Copy page

Canva provides a product catalog to help partners get an integration up and running as quickly as possible. However, not all partners want to use the pre-made catalog. Some prefer to use a custom landing page that better integrates with their existing user experience.

This guide explains how to open the Canva editor via a custom landing page, which eliminates the integration's dependency on the product catalog.

Custom landing pages don't support templates. You can open the Canva editor with a selected product, but not with a template.

## Step 1: Provide Canva with the ID of each product

When you use the product catalog, the [`showCatalog`](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/) method provides all of the required data for creating new designs.

When you don't use the product catalog, you need to provide Canva with the ID (such as a SKU) of each product that you'd like to make available to users. For example, a poster product may have the ID `"Poster11x17in"`.

You can't define these IDs via the Partnership SDK. You need to request Canva to set them up in the backend.

To raise a request:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **Integration support**.
  3. In the **Description** field, provide the ID of each product.



If you inspect the SDK's `opts` objects, you might find the`productId` or `productSizeOptionId` properties. These are internal, volatile properties that are different from the `partnerProductId`.

## Step 2: Call the `createDesign` method

When the product IDs are defined in Canva's backend, call the [`createDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/) method and pass the product ID via the `partnerProductId` property.
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
      });
    
    
    
    
      api.createDesign({
    
        partnerProductId: "Poster11x17in",
    
        maxPages: 2,
    
        title: "Untitled Design - Poster",
    
        designSource: "direct",
    
        onBackClick,
    
        onArtworkCreate,
    
      });
    
    })();

JAVASCRIPT

Copy

This code doesn't depend on the `showCatalog` function, which means the product catalog is optional.
