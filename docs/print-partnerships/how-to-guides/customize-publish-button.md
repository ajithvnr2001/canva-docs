---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/
title: Customize the \"Publish\" button - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.687214+00:00
---

# Customize the "Publish" button - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Customize the "Publish" button

Copy page

When a user is ready to print their design, they can click the **Publish** button to start the [proofing process](https://www.canva.dev/docs/print-partnerships/concepts/proofing/). If you'd like to use different terminology for this button though, you can change the label.

To customize the label of the "Publish" button, provide a value for the `publishLabel` property when using the following methods:

  * [`createDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/)
  * [`editDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/)



The following snippet demonstrates this customization in the `createDesign` method:
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onProductSelect = (opts) => {
    
        api.createDesign({ ...opts, publishLabel: "Do something!" });
    
      };
    
    
    
    
      api.showCatalog({
    
        onProductSelect,
    
      });
    
    })();

JAVASCRIPT

Copy

While viewing the editor on a mobile device, the **Publish** button uses an icon instead of a label. You can't customize this icon.
