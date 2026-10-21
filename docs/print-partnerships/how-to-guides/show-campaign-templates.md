---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/
title: Show campaign templates - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.169815+00:00
---

# Show campaign templates - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Show campaign templates

Copy page

When a user creates a design, by default Canva shows [templates](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/#templates) relevant to a product. Sometimes, a partner may want to show templates specific to a theme, event, or marketing campaign instead. This lets a partner provide a more tailored user experience.

This document explains how to show campaign templates.

If you prefer to set up multiple product catalogs, each with separate products and templates, see [Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/).

## Step 1: Provide Canva with the campaign details and a list of products

Canva maintains the templates to show for each product. This means partners can't directly modify the template settings themselves. Partners must request Canva to make the changes.

To raise a request:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **Homepage Update Request**.
  3. FIll out the required fields.
  4. Provide the following: 
     1. The campaign title, such as "Back to school" or "Mother's day".
     2. A list of products for the campaign.
     3. The campaign launch date.



After receiving the request, Canva:

  * Groups the templates for each product under a specific type, such as “BacktoSchoolPoster”, “MothersDayCard”.
  * Responds with the type the templates are grouped under.



## Step 2: Show the campaign templates

To show the campaign templates for a specific product, pass the partner product ID and the template type to the [createDesign](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/) method.
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
      });
    
    
    
    
      api.createDesign({
    
        partnerProductId: "Poster11x17in",
    
        type: "BacktoSchoolPoster",
    
        designSource: "direct",
    
        onArtworkCreate,
    
        onBackClick,
    
      });
    
    })();

JAVASCRIPT

Copy
