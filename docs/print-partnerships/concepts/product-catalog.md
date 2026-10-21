---
url: https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/
title: Product Catalog - General information - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:59.830549+00:00
---

# Product Catalog - General information - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/

General information

[Evaluating Canva](https://www.canva.dev/docs/print-partnerships/concepts/evaluating-canva/)[Authentication](https://www.canva.dev/docs/print-partnerships/concepts/authentication/)[Credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/)[Request credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/)[Product catalog](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/)[Proofing](https://www.canva.dev/docs/print-partnerships/concepts/proofing/)[Security](https://www.canva.dev/docs/print-partnerships/concepts/security/)[User journey](https://www.canva.dev/docs/print-partnerships/concepts/user-journey/)

# Product Catalog

Copy page

The product catalog is a ready-made landing page that partners can embed in their website.

![](https://www.canva.dev/_next/static/media/product-catalog.91c44155.jpg)

If you want more control over the user experience, [create a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/). If you want to have multiple product catalogs, see [Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/).

## Features

The product catalog lets users:

  * Create a design based on a product configuration or a template.
  * Open their existing designs.
  * Search for products and templates.



By using the product catalog, you can get a Print Partnership integration up and running as quickly as possible.

## Live demo

For a live demo of the product catalog, check out the following page:

<https://sdk.canva.com/partnership-internal-demo.html>[⁠(opens in a new tab or window)](https://sdk.canva.com/partnership-internal-demo.html)

To learn how to set up a product catalog from scratch, follow the [step-by-step tutorial](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/).

## Interface tour

### Search

Help users find the product they're looking for.

![](https://www.canva.dev/_next/static/media/search.91df55d9.jpg)

The search bar is enabled by default. To disable the search bar, raise a support request and ask Canva to disable it.

If your integration has multiple product catalogs, only one of those product catalogs can have a search bar. The search bar searches all products and templates even if a product catalog shows only a subset of products and templates.

To raise a request:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **Homepage Update Request**.
  3. In the **Description** field, ask Canva to disable the search bar.



### Products

Let users create a design based on a product, such as a T-shirt, poster, or business card. This determines the initial dimensions of the design.

![](https://www.canva.dev/_next/static/media/products.dd32809b.jpg)

### Designs

Once a user creates at least one design, their designs appear in the catalog, in a carousel. This lets the user easily open their previously created designs.

![](https://www.canva.dev/_next/static/media/my-designs.83527296.jpg)

To display the "My Designs" carousel, register the [`onDesignSelect`](https://www.canva.dev/docs/print-partnerships/javascript-api/on-design-select/) callback via the [`showCatalog`](https://www.canva.dev/docs/print-partnerships/javascript-api/show-catalog/) method.

### Templates

As the user scrolls down the page, they see carousels of templates. These templates give users a starting point for their designs. Each template is associated with a specific type of product.

![](https://www.canva.dev/_next/static/media/templates.257cf3ba.jpg)

### Pricing

Display pricing information alongside products and templates.

![](https://www.canva.dev/_next/static/media/pricing.5ba73530.jpg)

Pricing information is disabled by default. To enable pricing information, raise a support request with Canva and ask to enable it.

To raise a request:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **Homepage Update Request**.
  3. In the **Description** field, ask Canva to enable the pricing information.



## Limitations

  * You can't control the ranking of templates. Canva automatically ranks the templates based on relevance and popularity.


