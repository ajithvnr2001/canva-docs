---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/
title: Continuation - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:51.852358+00:00
---

# Continuation - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Continuation

Add pagination to a publish extension.

Copy page

In a publish extension, there's a limit to how many resources—images or containers—can be returned in a single response. This limit ensures that resources are loaded quickly.

To provide users with more resources than this limit allows, they need to be loaded across multiple requests. In some APIs, this is known as _pagination_. In the publish extension API, it's known as _continuation_. The terms, however, can be used interchangeably.

The best way to understand pagination is with a practical example, so this topic explains how to allow users to paginate through an arbitrary list of resources.

![](https://www.canva.dev/_next/static/media/img-e7bd40c2c7.a91e63bd.gif)

For a publish extension to support pagination, it must use the [Flat list](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/) or [Nested list](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/) layout.

## Prerequisites

This tutorial assumes experience with:

  * REST APIs
  * Node.js
  * Express.js



You should have also completed the [quickstart for publish extensions](https://www.canva.dev/docs/extensions/quickstart/).

## Set up

Before continuing:

  1. Create an app via the Developer Portal.

  2. Add a publish extension to the app.

  3. Set up a REST API with [Glitch⁠(opens in a new tab or window)](https://glitch.com) and Express.js:
         
         const express = require("express");
         
         const app = express();
         
         
         
         
         app.use(express.json());
         
         app.use(express.static("public"));
         
         
         
         
         // Routes go here
         
         
         
         
         app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy




## Loading the initial page of resources

When a user opens a publish extension, Canva sends a `POST` request to `/publish/resources/find`:
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      console.log(request.body);
    
    });

JAVASCRIPT

Copy

The purpose of this request is to retrieve that resources that will appear in the **Publish** menu.

For this tutorial, use the `fill` and `map` methods to generate an array of `"CONTAINER"` resources:
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      const containers = new Array(20).fill(0).map((item, index) => {
    
        return {
    
          type: "CONTAINER",
    
          id: `${index}`,
    
          name: `Container #${index}`,
    
          isOwner: true,
    
          readOnly: false,
    
        };
    
      });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources: containers,
    
      });
    
    });

JAVASCRIPT

Copy

You cannot return more than 100 resources in a single response.

## Providing the next page number in the response

Before a user reaches the end of the resource list, we want to trigger an additional request to `/publish/resources/find`. This will allow us to seamlessly load additional resources, creating the effect of infinite scrolling.

To accomplish this, add a `continuation` property to the response:
    
    
    response.send({
    
      type: "SUCCESS",
    
      resources: images,
    
      continuation: "2",
    
    });

JAVASCRIPT

Copy

The presence of this property tells Canva that it should send another `POST` request to `/publish/resources/find` before the user reaches the end of the resource list. The value of this property will also be included in the body of that request.

In this example, the value of the `continuation` property is `"2"`. This is because we've loaded the first page of results and we would like to load the second page. But this value does not _have_ to be a page number. The only requirement is that this value is a string.

After making this change, scroll through the resources in the side panel.

The same resources will be repeatedly loaded. This isn't exactly what we want, but it's a step in the right direction.

## Getting the current page number from the request body

When a `continuation` property is included in a response, that same `continuation` property will be made available in the body of the next `POST` request that's sent to `/publish/resources/find`.

To see an example of this, log the value of `request.body.continuation`:
    
    
    console.log(request.body.continuation);

JAVASCRIPT

Copy

When the first page of resources is loaded, the `continuation` property is `null`. This is because there isn't a previous response. But if you trigger another request by scrolling through the resources, the value of `"2"` will be logged. You can use this behavior to load unique resources for each request.

At the top of the route, before the `options` object, create a `currentPage` variable that contains the value of the request body's `continuation` property:
    
    
    const currentPage = request.body.continuation;

JAVASCRIPT

Copy

But since the `continuation` property will be `null` on the initial request, provide a fall-back value of `"1"`:
    
    
    const currentPage = request.body.continuation || "1";

JAVASCRIPT

Copy

This code will include the page number in the name of the resources:
    
    
    const resources = new Array(20).fill(0).map((item, index) => {
    
      return {
    
        type: "CONTAINER",
    
        id: `${currentPage}-${index}`,
    
        name: `Page #${currentPage}, Container #${index}`,
    
        isOwner: true,
    
        readOnly: false,
    
      };
    
    });

JAVASCRIPT

Copy

Based on these changes, we'll be able to load the first and second pages into the side panel.

If we keep scrolling through the resources though, it's now the second page of images that will be repeatedly loaded. This is because we've hard-coded the value of the `continuation` property in all responses as `"2"`.

Even so, this is another step in the right direction.

## Incrementing the page number

To load unique resources for every request, we need to increment the value of the `continuation` property.

Before the `response.send` method, create a variable that parses the number from the `currentPage` variable, increments it by one, and converts the result back into a string:
    
    
    const nextPage = (parseInt(currentPage, 10) + 1).toString();

JAVASCRIPT

Copy

Then provide this variable in the response:
    
    
    response.send({
    
      type: "SUCCESS",
    
      resources: images,
    
      continuation: nextPage,
    
    });

JAVASCRIPT

Copy

Based on this change, a unique set of resources will be loaded for each request.

## Loading the final page of resources

When the final page of resources is reached, don't provide a `continuation` property in the response:
    
    
    response.send({
    
      type: "SUCCESS",
    
      resources: images,
    
    });

JAVASCRIPT

Copy

...or set the `continuation` property to `null`:
    
    
    response.send({
    
      type: "SUCCESS",
    
      resources: images,
    
      continuation: null,
    
    });

JAVASCRIPT

Copy

This signifies that there's no more pages to load.

## Example
    
    
    const express = require("express");
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    app.post("/publish/resources/find", async (request, response) => {
    
      const currentPage = request.body.continuation || "1";
    
      const nextPage = (parseInt(currentPage, 10) + 1).toString();
    
      const maxPages = 5;
    
    
    
    
      const resources = new Array(20).fill(0).map((item, index) => {
    
        return {
    
          type: "CONTAINER",
    
          id: `${currentPage}-${index}`,
    
          name: `Page #${currentPage}, Container #${index}`,
    
          isOwner: true,
    
          readOnly: false,
    
        };
    
      });
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources,
    
        continuation: currentPage < maxPages ? nextPage : null,
    
      });
    
    });
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
