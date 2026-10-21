---
url: https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/
title: onDesignClose - API reference - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:58.666071+00:00
---

# onDesignClose - API reference - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/

API reference

[createDesign](https://www.canva.dev/docs/button/javascript/api-reference/create-design/)[editDesign](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/)[initialize](https://www.canva.dev/docs/button/javascript/api-reference/initialize/)[onDesignClose](https://www.canva.dev/docs/button/javascript/api-reference/on-design-close/)[onDesignOpen](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/)[onDesignPublish](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/)

# onDesignClose

API reference for the JavaScript API's onDesignClose method.

Copy page

A function that runs when a user closes a design.

## Usage
    
    
    api.createDesign({
    
      design: {
    
        type: "Poster",
    
      },
    
      onDesignClose: () => {
    
        // code goes here
    
      },
    
    });

JAVASCRIPT

Copy

You can pass the `onDesignClose` function into the [`createDesign`](https://www.canva.dev/docs/button/javascript/api-reference/create-design/) and [`editDesign`](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/) functions.

## Parameters

This function doesn't receive any parameters.

## Returns

`void`
