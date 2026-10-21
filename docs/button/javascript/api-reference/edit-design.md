---
url: https://www.canva.dev/docs/button/javascript/api-reference/edit-design/
title: editDesign - API reference - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:58.180123+00:00
---

# editDesign - API reference - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/api-reference/edit-design/

API reference

[createDesign](https://www.canva.dev/docs/button/javascript/api-reference/create-design/)[editDesign](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/)[initialize](https://www.canva.dev/docs/button/javascript/api-reference/initialize/)[onDesignClose](https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/)[onDesignPublish](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/)

# editDesign

API reference for the JavaScript API's editDesign method.

Copy page

Opens an existing design in the Canva editor.

## Usage
    
    
    api.editDesign({
    
      design: {
    
        id: "DESIGN ID GOES HERE",
    
      },
    
    });

JAVASCRIPT

Copy

You must [initialize the SDK](https://www.canva.dev/docs/button/javascript/api-reference/initialize/) before calling the `editDesign` function.

## Parameters

Name| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Options for opening an existing design in the Canva editor.  
`opts.design`| object| Yes| Options for the user's design.  
`opts.design.id`| object| Yes| The ID of the user's design.  
`opts.editor`| object| No| Options for the Canva editor.  
`opts.editor.publishLabel`| string| No| A label for the **Publish** button. The default value is `Publish`.  
`opts.editor.fileType`| string| No| A file type for the exported design. The accepted values include `png`, `pdf`, `jpeg`, and `jpeg`. The ability to export designs as `mp4` and `gif` is an invite-only feature. The default value is `png`. If this argument is null, the editor uses whatever value is defined for the `createDesign` method.  
`opts.onDesignOpen`| function| No| A function that runs when a user opens their design. For more information, see [onDesignOpen](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/).  
`opts.onDesignPublish`| function| No| A function that runs when the user publishes their design. For more information, see [onDesignPublish](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/).  
`opts.onDesignClose`| function| No| A function that runs when the user closes their design. For more information, see [onDesignClose](https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/).  
  
## Returns

`void`
