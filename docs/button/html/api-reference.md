---
url: https://www.canva.dev/docs/button/html/api-reference/
title: API reference - API reference - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.180533+00:00
---

# API reference - API reference - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/html/api-reference/

API reference

[API reference](https://www.canva.dev/docs/button/html/api-reference/)

# API reference

List of HTML attributes for the Canva Button.

Copy page

You can use HTML attributes to control the behavior and appearance of the Canva Button. Some of these attributes are always available, while Others are only available when creating a new design or editing an existing design. This page lists the HTML attributes and when they're available.

## General attributes

These attributes are always available.

Name| Type| Required| Description  
---|---|---|---  
`data-api-key`| string| Yes| Your unique API key.  
`data-button-theme`| string| No| The color theme of the button. The accepted values include `default`, `light`, and `dark`. The default value is `default`.  
`data-button-size`| string| No| The size of the button. The accepted values include `default`, `tiny`, `small`, and `large`. The default value is `default`.  
`data-editor-file-type`| string| No| The file type of the exported design. The accepted values include `png`, `pdf`, `jpeg`, and `jpeg`. The ability to export designs as `mp4` and `gif` is an invite-only feature. The default value is `png`.  
`data-editor-publish-label`| string| No| A label for the **Publish** button. The default value is `Publish`.  
`data-on-design-close`| string| No| The name of a JavaScript function. This function runs when the user closes their design. No parameters are passed to this function.  
`data-on-design-open`| string| No| The name of a JavaScript function. This function runs when the user publishes opens a design. This includes when a user creates a new design or edits an existing design. This function receives the same parameters as the JavaScript API's [onDesignOpen](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/) function.  
`data-on-design-open-input-design-id`| string| No| The name of a form input element. When the user opens their design, the ID of the design is inserted into the input.  
`data-on-design-publish`| string| No| The name of a JavaScript function. This function runs when the user publishes their design. This function receives the same parameters as the JavaScript API's [onDesignPublish](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/) function.  
`data-on-design-publish-input-export-url`| string| No| The name of a form input element. When the user publishes their design, the URL of the published design is inserted into the input. The URL is in the form `https://export-download.canva.com/<export_file>`. If you're using the China version of the SDK, the TLD is `.cn` instead of `.com`. You can take the necessary security measures to protect the URL from any malicious attacks.  
`data-on-design-publish-input-design-id`| string| No| The name of a form input element. When the user publishes their design, the ID of the design is inserted into the input.  
`data-on-design-publish-input-title`| string| No| The name of a form input element. When the user publishes their design, the title of the published design is inserted into the input.  
  
## Attributes for creating a new design

These attributes are only available when using the Canva Button to create a new design. You can't use these attributes in conjunction with the attributes for editing an existing design.

Name| Type| Required| Description  
---|---|---|---  
`data-design-type`| string| Yes| The type of design you want your users to create. For the complete list of supported values, see [List of design types](https://www.canva.dev/docs/button/reference/design-types/).  
`data-design-dimensions-height`| number| No| The height of the design. The unit of measurement is determined by the `data-design-dimensions-units` attribute.  
`data-design-dimensions-units`| string| No| The unit of measurement for the `data-design-dimensions-height` and `data-design-dimensions-width` attributes. The accepted values include `cm`, `in`, and `px`. The default value is `px`.  
`data-design-dimensions-width`| number| No| The width of the design. The unit of measurement is determined by the `data-design-dimensions-units` attribute.  
`data-design-title`| string| No| The title of the design. The default title is _Untitled design_. The title is used in the exported design's filename. Users can change the title later in the Canva editor.  
  
For examples of how to use these attributes, see [Create a new design with the HTML API](https://www.canva.dev/docs/button/html/creating-designs/).

## Attributes for editing an existing design

These attributes are only available when using the Canva Button to edit an existing design. You can't use these attributes in conjunction with the attributes for creating a new design.

Name| Type| Required| Description  
---|---|---|---  
`data-design-id`| string| Yes| The ID of an existing design.  
  
For examples of how to use these attributes, see [Edit an existing design with the HTML API](https://www.canva.dev/docs/button/html/editing-designs/).
