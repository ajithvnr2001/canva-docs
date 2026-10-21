---
url: https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/
title: Customize the export settings - How-to guides - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.426084+00:00
---

# Customize the export settings - How-to guides - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/

How-to guides

[Anonymous editing](https://www.canva.dev/docs/print-partnerships/how-to-guides/anonymous-editing/)[Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/)[Customize the "Publish" button](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-publish-button/)[Edit designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/edit-designs/)[Handle page refreshes](https://www.canva.dev/docs/print-partnerships/how-to-guides/refresh-editor/)[Request for translation](https://www.canva.dev/docs/print-partnerships/how-to-guides/request-for-translation/)[Resize designs](https://www.canva.dev/docs/print-partnerships/how-to-guides/resize-design/)[Set up multiple product catalogs](https://www.canva.dev/docs/print-partnerships/how-to-guides/multiple-product-catalogs/)[Show campaign templates](https://www.canva.dev/docs/print-partnerships/how-to-guides/show-campaign-templates/)[Support mobile devices](https://www.canva.dev/docs/print-partnerships/how-to-guides/support-mobile-devices/)[Use a custom landing page](https://www.canva.dev/docs/print-partnerships/how-to-guides/custom-landing-page/)

# Customize the export settings

Copy page

Partners can define _export settings_ for an integration. These settings control the way Canva:

  * Generates a preview of the user's proofed design.
  * Generates a print-ready version of the user's design.



Some of the available settings include the image format, bleed microns, color space, and transparency level. For a complete list of the available settings, refer to [Export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/).

This page explains how export settings work and how to customize them.

## Export types

Canva maintains an integration's export settings in a JSON file.
    
    
    {
    
      "exports": {
    
        "publishExportSettings": {
    
          "outputSpecSettings": "PDF",
    
          "renderSpecSettings": {
    
            "bleed": true,
    
            "bleedMicrons": null,
    
            "cropMarks": true
    
          },
    
          "cmyk": false,
    
          "canvasIsTransparent": false,
    
          "outlineText": true,
    
          "pdfX": false
    
        },
    
        "previewExportSettings": {
    
          "outputSpecSettings": "JPG",
    
          "renderSpecSettings": {
    
            "bleed": true,
    
            "bleedMicrons": null,
    
            "cropMarks": false
    
          }
    
        }
    
      }
    
    }

JSON

Copy

The JSON file contains an `exports` object that has the following properties:

  * `previewExportSettings`
  * `publishExportSettings`



These properties contain separate export settings that Canva uses in different contexts.

When a user is ready to see a proof of a design, Canva uses the settings from the `previewExportSettings` object to generate the preview of the user's design.

When a user has purchased a print of their design, Canva uses the settings from the `publishExportSettings` object to generate the print-ready version of the user's design.

If an integration doesn't provide settings for the `previewExportSettings` object, Canva uses the settings defined in the `publishExportSettings` object.

The settings for `previewExportType` and `publishExportType` objects differ based on the export format. The supported export formats are PDF, JPG, and PNG. To learn about the settings for each export format, see [Export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/).

Export settings don't affect the quality (DPI, resolution, etc) of the user's exported design.

## Levels of customization

You can define export settings at a product level or a partner level.

The export settings defined at a product level affect an integration's individual products. This enables you to define different export settings for different products.

The export settings defined at a partner level affect all of an integration's products.

When Canva retrieves the export settings for a design, Canva first looks for the export settings defined at a product level. If none are defined, Canva looks for the export settings defined at a partner level. If none are defined, Canva falls back to the default settings as described in [Export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/).

## Requesting changes

Canva maintains the export settings for each integration. This means partners can't directly modify the settings themselves. Partners need to request Canva to make the changes.

To request changes to your integration's export settings:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **Integration support**.
  3. Fill out the required fields.


