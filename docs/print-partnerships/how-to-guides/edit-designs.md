---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/
title: Edit designs - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.804804+00:00
---

# Edit designs - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Edit designs

Copy page

After a user creates a design, they may want to edit the design later. To enable this, Canva provides a [My Designs](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/#designs) carousel in the product catalog and an ID for each design.

Partners can enable the My Designs carousel to show and reopen a design from the product catalog. Partners can use the design ID to reopen a design by directly launching the Canva editor.

This page explains how to reopen and edit a design.

## Edit a design via the catalog-to-editor path

The [catalog-to-editor](https://www.canva.dev/docs/print-partnerships/concepts/user-journey/#catalog-to-editor) path lets you show and reopen a design from the My Designs carousel of the product catalog.

### Step 1: Show the My Designs carousel

A product catalog doesn't show the My Designs carousel by default. You must enable the carousel.

To enable the carousel, use the [`onDesignSelect`](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/) callback in the [`showCatalog`](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/) method.
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
        container: document.getElementById("container"),
    
      });
    
    
    
    
      const onDesignSelect = (opts) => {
    
        console.log(opts);
    
      };
    
    
    
    
      api.showCatalog({
    
        onDesignSelect,
    
      });
    
    })();

JS

Copy

The `onDesignSelect` callback passes information about the design a user selects, including the design ID.

At this point, users can see their designs in the My Designs carousel, but can't reopen a design in the Canva editor yet.

### Step 2: Reopen a design

When a user selects a design in the My Designs carousel, you must reopen the design in the Canva editor. This lets a user edit their design.

To reopen a design, in the `onDesignSelect` callback, call the [`editDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/) method and pass the design ID.
    
    
    const onDesignSelect = (opts) => {
    
      api.editDesign({
    
        ...opts,
    
        designId: opts.designId,
    
      });
    
    };

JS

Copy

## Edit a design via the direct-to-editor path

The [direct-to-editor](https://www.canva.dev/docs/print-partnerships/concepts/user-journey/#direct-to-editor) path lets you reopen a design by directly launching the Canva editor.

### Step 1: Get the design ID

Canva provides the design ID when:

  * A user creates a new design.
  * Canva generates the artworks for a design.



You can save the design ID locally or to a datastore. You can later use the design ID to reopen a design.

#### Option 1: When a user creates a design

To get the design ID when a user creates a design, use the [`onDesignOpen`](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-open/) callback in the [`createDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/create-design/) method.
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
      });
    
    
    
    
      const onDesignOpen = (opts) => {
    
        console.log(opts);
    
      };
    
    
    
    
      api.createDesign({
    
        partnerProductId: "Poster11x17in",
    
        designSource: "direct",
    
        onDesignOpen,
    
      });
    
    })();

JS

Copy

#### Option 2: When Canva generates the artworks

To get the design ID when Canva generates the artworks for a design, use the [`onMultiArtworkCreate`](https://www.canva.dev/docs/print-partnerships/javascript-api/on-multi-artwork-create/) method in the `createDesign` method.
    
    
    (async () => {
    
      const api = await Canva.Partnership.initialize({
    
        apiKey: "<partner_api_key>",
    
        autoAuthToken: "<auto_auth_token>",
    
      });
    
    
    
    
      const onMultiArtworkCreate = (opts) => {
    
        opts.artworks.forEach((artwork) => {
    
          console.log(artwork);
    
        });
    
      };
    
    
    
    
      api.createDesign({
    
        partnerProductId: "Poster11x17in",
    
        designSource: "direct",
    
        onMultiArtworkCreate,
    
      });
    
    })();

JS

Copy

### Step 2: Reopen a design

To reopen a design, call the [`editDesign`](https://www.canva.dev/docs/print-partnerships/javascript-api/edit-design/) method and pass the design ID.
    
    
    api.editDesign({
    
      designId: "DESIGN ID GOES HERE",
    
    });

JS

Copy
