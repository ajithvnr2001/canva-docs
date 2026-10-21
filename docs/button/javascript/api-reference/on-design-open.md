---
url: https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/
title: onDesignOpen - API reference - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:58.731523+00:00
---

# onDesignOpen - API reference - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/

API reference

[createDesign](https://www.canva.dev/docs/button/javascript/api-reference/create-design/)[editDesign](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/)[initialize](https://www.canva.dev/docs/button/javascript/api-reference/initialize/)[onDesignClose](https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/)[onDesignPublish](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/)

# onDesignOpen

API reference for the JavaScript API's onDesignOpen method.

Copy page

A function that runs when a user opens a design. This includes when a user creates a new design or edits an existing design.

## Usage
    
    
    api.createDesign({
    
      design: {
    
        type: "Poster",
    
      },
    
      onDesignOpen: (opts) => {
    
        console.log(opts);
    
      },
    
    });

JAVASCRIPT

Copy

You can pass the `onDesignOpen` function into the [`createDesign`](https://www.canva.dev/docs/button/javascript/api-reference/create-design/) and [`editDesign`](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/) functions.

## Parameters

Name| Type| Required| Description  
---|---|---|---  
`opts`| object| Yes| Parameters that Canva passes into the function.  
`opts.designId`| string| Yes| The ID of the user's design.  
`opts.designTitle`| string| Yes| The title of the user's design.  
  
## Returns

`void`
