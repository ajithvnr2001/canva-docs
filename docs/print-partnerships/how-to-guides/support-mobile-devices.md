---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/
title: Support mobile devices - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:01.697778+00:00
---

# Support mobile devices - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Support mobile devices

Copy page

Canva's product catalog and editor has excellent support for mobile devices. To enable this support, add the following `meta` tag to the page that contains the integration's iframe:
    
    
    <meta
    
      name="viewport"
    
      content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover"
    
    />

HTML

Copy

When using the mobile view, we recommend letting the product catalog and editor stretch to the edges of the viewport. This means not using a custom header of footer.
