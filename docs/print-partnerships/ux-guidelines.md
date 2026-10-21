---
url: https://www.canva.dev/docs/print-partnerships/ux-guidelines/
title: UX guidelines - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:05.137474+00:00
---

# UX guidelines - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/ux-guidelines/

Print partnership

[Overview](https://www.canva.dev/docs/print-partnerships/)[Quickstart](https://www.canva.dev/docs/print-partnerships/quickstart/)

Stay up to date

Information

General information

Guides

Tutorials

How-to guides

Distribution

Support and Troubleshooting

Troubleshooting

Support

References

JavaScript API

REST API

Reference

# UX guidelines

Copy page

Canva is known for it's delightful user experience. This page provides some simple guidelines to ensure that users get the most out of the [product catalog](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/) and editor.

## Give Canva lots of real estate

The iframe that contains the catalog and editor should be given as much screen real estate as possible.

Specifically, we recommend allowing the iframe to:

  * Fill the complete width of the page.
  * Fill most (if not all) of the viewport's height.



## Be mindful that scrolling is disabled

When the Partnership SDK finishes loading the iframe, it disables scrolling on the parent page.

There's two reasons for this:

  * To avoid two sets of scrollbars (one inside the iframe and one on the parent page). This is a potential problem for the catalog and the editor.
  * To prevent users from scrolling as they try to drag and drop content in the Canva editor.



## If you include a header, keep it small

Your website can embed a header before the iframe, but make sure that it doesn't take up too much vertical space. We recommend a header with a maximum height of 50-70px.

If your website displays temporary banners in the header -- cookie disclaimers, etc -- the additional banner shouldn't push the bottom of the iframe beneath the fold.

## Don't include a footer

In general, we recommend _not_ including a footer on the same page as the iframe, as they take up space that could be better used by the iframe. If you must include a footer, keep it small and remain mindful of vertical space.

## Enable support for mobile devices

Canva's product catalog and editor has excellent support for mobile devices, but the support needs to be enabled. To learn how to enable it, refer to [Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/).
