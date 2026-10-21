---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/
title: Anonymous editing - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.352611+00:00
---

# Anonymous editing - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Anonymous editing

Copy page

Some partners don't require users to login before creating designs via their website. In these cases, a partner can [calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/) with a random string instead of a user's ID:
    
    
    const jwt = require("jwt-simple");
    
    
    
    
    const now = Math.floor(new Date().getTime() / 1000);
    
    
    
    
    const payload = {
    
      iss: process.env.PARTNER_API_KEY,
    
      sub: "<random_string>",
    
      iat: now,
    
      exp: now + 60 * 30,
    
    };
    
    
    
    
    const autoAuthToken = jwt.encode(payload, process.env.PARTNER_API_SECRET);
    
    
    
    
    console.log(autoAuthToken);

JAVASCRIPT

Copy

This still creates an account in Canva's backend, but the account isn't associated with a user in the partner's backend. As a result, the user is effectively anonymous.

## Limitations

  * If your integration uses anonymous editing, users can't view their previously created designs or uploaded media.


