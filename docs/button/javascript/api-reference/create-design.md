---
url: https://www.canva.dev/docs/button/javascript/api-reference/create-design/
title: createDesign - API reference - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:58.361391+00:00
---

# createDesign - API reference - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/api-reference/create-design/

API reference

[createDesign](https://www.canva.dev/docs/button/javascript/api-reference/create-design/)[editDesign](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/)[initialize](https://www.canva.dev/docs/button/javascript/api-reference/initialize/)[onDesignClose](https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/)[onDesignPublish](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/)

# createDesign

API reference for the JavaScript API's createDesign method.

Copy page

Creates a new design in the Canva editor.

## Usage
    
    
    api.createDesign({
    
      design: {
    
        type: "Poster",
    
      },
    
    });

JAVASCRIPT

Copy

You must [initialize the SDK](https://www.canva.dev/docs/button/javascript/api-reference/initialize/) before calling the `createDesign` function.

## Parameters

Name| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Options for creating a new design in the Canva editor.  
`opts.design`| object| Yes| Options for the user's design.  
`opts.design.type`| object| Yes| The type of design to create.  
`opts.design.dimensions.units`| string| No| The unit of measurement for the `height` and `width` properties.  
`opts.design.dimensions.height`| number| No| The height of the design. The unit of measurement is determined by the `units` property.  
`opts.design.dimensions.width`| number| No| The width of the design. The unit of measurement is determined by the `units` property.  
`opts.design.title`| string| No| The title of the design. The default title is _Untitled design_. The title is used in the exported design's filename. Users can change the title later in the Canva editor.  
`opts.editor`| object| No| Options for the Canva editor.  
`opts.editor.publishLabel`| string| No| A label for the **Publish** button. This overrides the default value of `"Publish"`.  
`opts.editor.fileType`| string| No| A file type for the exported design. The accepted values include `png`, `pdf`, `jpeg`, and `jpeg`. The ability to export designs as `mp4` and `gif` is an invite-only feature. The default value is `png`.  
`opts.onDesignOpen`| function| No| A function that runs when a user opens their design. For more information, see [onDesignOpen](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/).  
`opts.onDesignPublish`| function| No| A function that runs when the user publishes their design. For more information, see [onDesignPublish](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/).  
`opts.onDesignClose`| function| No| A function that runs when the user closes their design. For more information, see [onDesignClose](https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/).  
  
## Returns

`void`

## Example
    
    
    <!DOCTYPE html>
    
    <html lang="en">
    
      <head>
    
        <meta charset="UTF-8" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
        <title>Canva Button</title>
    
        <script src="https://sdk.canva.com/designbutton/v2/api.js"></script>
    
      </head>
    
      <body>
    
        <button>Create a new design</button>
    
        <script type="text/javascript">
    
          (async () => {
    
            if (!window.Canva || !window.Canva.DesignButton) {
    
              return;
    
            }
    
    
    
    
            const api = await window.Canva.DesignButton.initialize({
    
              apiKey: "API KEY GOES HERE",
    
            });
    
    
    
    
            const button = document.querySelector("button");
    
    
    
    
            button.onclick = () => {
    
              api.createDesign({
    
                design: {
    
                  type: "Poster",
    
                },
    
              });
    
            };
    
          })();
    
        </script>
    
      </body>
    
    </html>

MARKUP

Copy
