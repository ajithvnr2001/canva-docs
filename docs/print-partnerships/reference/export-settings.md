---
url: https://www.canva.dev/docs/print-partnerships/reference/export-settings/
title: Export settings - Reference - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:02.447113+00:00
---

# Export settings - Reference - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/reference/export-settings/

Reference

[Export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/)[Glossary](https://www.canva.dev/docs/print-partnerships/reference/glossary/)[Languages](https://www.canva.dev/docs/print-partnerships/reference/languages/)

# Export settings

Settings for PDF, JPG, and PNG export formats of a preview and a print-ready version of a user's artwork.

Copy page

To learn how to customize an integration's export settings, see [Customize export settings](https://www.canva.dev/docs/print-partnerships/how-to-guides/customize-export-settings/).

## Usage
    
    
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

## Properties

The same properties are available for the `publishExportSettings` and `publishExportSettings` objects. The available properties depend on the value of `outputSpecSettings`.

### JPG

Name| Type| Required| Description  
---|---|---|---  
`outputSpecSettings`| string| Yes| The desired format to export all pages of the artwork. Set to `"JPG"`. If not set, the export fails.  
`renderSpecSettings`| object| No| List of properties common to the export format. Contains `bleed`, `bleedMicrons`, and `cropMarks`.  
`renderSpecSettings.bleed`| boolean| No| If `true`, the bleed is added to the artwork. The default value is `false`. When set for `publishExportSettings`, the bleed is added to the design as well.  
`renderSpecSettings.bleedMicrons`| integer| No| The custom bleed size in microns. If set, `bleed` must be `true` and `cropMarks` must be `false`. Can be `null`. The default value is `3000`.  
`renderSpecSettings.cropMarks`| boolean| No| If `true`, crop marks are added to the artwork and `bleedMicrons` must be `null`. The default value is `false`.  
  
### PDF

Name| Type| Required| Description  
---|---|---|---  
`outputSpecSettings`| string| Yes| The desired format to export all pages of the artwork. Set to `"PDF"`. If not set, the export fails.  
`renderSpecSettings`| object| No| List of properties common to the export format. Contains `bleed`, `bleedMicrons`, and `cropMarks`.  
`renderSpecSettings.bleed`| boolean| No| If `true`, the bleed is added to the artwork. The default value is `false`. When set for `publishExportSettings`, the bleed is added to the design as well.  
`renderSpecSettings.bleedMicrons`| integer| No| The custom bleed size in microns. If set, `bleed` must be `true` and `cropMarks` must be `false`. Can be `null`. The default value is `3000`.  
`renderSpecSettings.cropMarks`| boolean| No| If `true`, crop marks are added to the artwork and `bleedMicrons` must be `null`. The default value is `false`.  
`cmyk`| boolean| No| If `true`, the color space is converted from RGB to CMYK. The default value is `true`.  
`canvasIsTransparent`| boolean| No| If `true`, the background is removed for transparent background exports. The default value is `false`.  
`outlineText`| boolean| No| If `true`, the text elements of the PDF are converted to shapes. This ensures compatibility with systems that don't have the necessary fonts installed. The default value is `false`.  
`pdfX`| boolean| No| If `true`, the PDF standard is updated to [PDF/X⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/PDF/X)). The default value is `false`.  
  
### PNG

Name| Type| Required| Description  
---|---|---|---  
`outputSpecSettings`| string| Yes| The desired format to export all pages of the artwork. Set to `"PNG"`. If not set, the export fails.  
`renderSpecSettings`| object| No| List of properties common to the export format. Contains `bleed`, `bleedMicrons`, and `cropMarks`.  
`renderSpecSettings.bleed`| boolean| No| If `true`, the bleed is added to the artwork. The default value is `false`. When set for `publishExportSettings`, the bleed is added to the design as well.  
`renderSpecSettings.bleedMicrons`| integer| No| The custom bleed size in microns. If set, `bleed` must be `true` and `cropMarks` must be `false`. Can be `null`. The default value is `3000`.  
`renderSpecSettings.cropMarks`| boolean| No| If `true`, crop marks are added to the artwork and `bleedMicrons` must be `null`. The default value is `false`.  
`canvasIsTransparent`| boolean| No| If `true`, the background is removed for transparent background exports. The default value is `false`.
