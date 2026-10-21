---
url: https://www.canva.dev/docs/button/javascript/api-reference/initialize/
title: initialize - API reference - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:59.042252+00:00
---

# initialize - API reference - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/api-reference/initialize/

API reference

[createDesign](https://www.canva.dev/docs/button/javascript/api-reference/create-design/)[editDesign](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/)[initialize](https://www.canva.dev/docs/button/javascript/api-reference/initialize/)[onDesignClose](https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/)[onDesignPublish](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/)

# initialize

API reference for the JavaScript API's initialize method.

Copy page

Initializes the JavaScript API for the Canva Button. You must embed the Canva Button SDK before calling this function.

## Usage
    
    
    (async () => {
    
      if (!window.Canva || !window.Canva.DesignButton) {
    
        return;
    
      }
    
    
    
    
      const api = await window.Canva.DesignButton.initialize({
    
        apiKey: "API KEY GOES HERE",
    
      });
    
    })();

JAVASCRIPT

Copy

## Parameters

Name| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Options for configuring the Canva Button API.  
`opts.apiKey`| string| Yes| Your API key for the Canva Button.  
  
## Returns

Name| Type| Required| Description  
---|---|---|---  
`api`| object| Yes| An object that contains functions for interacting with Canva.  
`api.createDesign`| function| Yes| A function that creates a new design in the Canva editor. For more information, see [createDesign](https://www.canva.dev/docs/button/javascript/api-reference/create-design/).  
`api.editDesign`| function| Yes| A function that opens an existing design in the Canva editor. For more information, see [editDesign](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/).
