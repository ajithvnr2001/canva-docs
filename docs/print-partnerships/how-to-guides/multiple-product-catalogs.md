---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/
title: Set up multiple product catalogs - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.913883+00:00
---

# Set up multiple product catalogs - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Set up multiple product catalogs

Copy page

This feature is in a closed, invite-only beta.

By default, Canva provides a single [product catalog](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/) for each integration. Sometimes though, partners find it useful to have multiple product catalogs, each with separate products and templates.

Partners generally opt for multiple product catalogs when they want to promote products and templates for a specific marketing campaign, event, or industry vertical.

This guide explains how to set up multiple product catalogs.

## Step 1: Request multiple product catalogs

Partners must request Canva to set up multiple product catalogs.

To raise a request:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **Multiple Catalogs Request**.
  3. In the **Summary** field, specify `Requesting multiple product catalogs`.
  4. In the **Description** field, provide: 
     1. The number of product catalogs you want.
     2. A title or theme for each product catalog, such as "Back to school" or "Mother's day."
     3. A list of products and templates for each product catalog.
     4. Banner text for each product catalog. This is shown in the banner, above the [search bar](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/#search).
     5. (Optional) A banner image. If you don't provide one, Canva uses a default banner image.



After receiving the request, Canva:

  * Creates the product catalogs.
  * Responds with a tag for each product catalog.



Canva uses the tags to identify specific product catalogs.

## Step 2: Show a specific product catalog

To show a specific product catalog, pass a tag into the `showCatalog` method via the `tag` parameter.
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      api.showCatalog({
    
        tag: "back-to-school",
    
      });
    
    })();

JAVASCRIPT

Copy

## Notes

  * The `tag` parameter is optional. Use it only when you want to set up multiple product catalogs.
  * If you don't pass the `tag` parameter, an integration renders a default product catalog. A default product catalog shows the default banner image, banner text, and all products, templates, and saved designs.
  * The tags are case-sensitive.
  * If you pass an empty string or a tag that Canva doesn't recognize, the SDK shows an error in the JavaScript Console.


