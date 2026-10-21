---
url: https://www.canva.dev/docs/button/html/getting-started/
title: Getting started - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.644048+00:00
---

# Getting started - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/html/getting-started/

How-to guides

[Getting started](https://www.canva.dev/docs/button/html/getting-started/)[Creating designs](https://www.canva.dev/docs/button/html/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/html/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/html/editing-designs/)[Customization](https://www.canva.dev/docs/button/html/customization/)

# Getting started

Add the Canva Button to a website with the HTML API.

Copy page

The Canva Button's HTML API is the simplest way to get up and running with the Canva Button.

This tutorial explains how to create a Canva Button with the HTML API and embed it in a web page.

If you're wondering whether the HTML API is right for you, see [HTML API vs. JavaScript API](https://www.canva.dev/docs/button/platform-concepts/html-api-vs-js-api/).

## Prerequisites

This tutorial assumes you have an API key to use the Canva Button. If you don't have one, [sign up for an API key](https://www.canva.dev/docs/button/quickstart/#step-1-sign-up-for-an-api-key).

## Step 1: Generate a Canva Button

Canva provides a tool for generating a Canva Button. You can then use HTML attributes to configure the behavior and appearance of the Button.

To generate a Canva Button:

  1. Navigate to [canva.com/button/build⁠(opens in a new tab or window)](https://www.canva.com/button/build/).
  2. Enter your API key for the Canva Button.
  3. Select a design type. When a user creates a design, the design type determines the dimensions of the design and the templates that Canva shows to the user. For a complete list of the supported design types, refer to [Design types](https://www.canva.dev/docs/button/reference/design-types/).
  4. Select a button size.
  5. Select a button style.
  6. Click **Get my button**.



The generated code looks like this:
    
    
    <button
    
      data-design-type="Poster"
    
      data-api-key="API KEY GOES HERE"
    
      class="canva-design-button"
    
      style="display: none;"
    
      >Design with Canva</button
    
    >
    
    <script>
    
      (function (c, a, n) {
    
        var w = c.createElement(a),
    
          s = c.getElementsByTagName(a)[0];
    
        w.src = n;
    
        s.parentNode.insertBefore(w, s);
    
      })(document, "script", "https://sdk.canva.com/designbutton/v2/api.js");
    
    </script>

JSX

Copy

Copy the code into the part of the web page where you want to display the Canva Button.

If you're using the China version of the SDK, replace `https://sdk.canva.com/designbutton/v2/api.js` with `https://sdk.canva.cn/designbutton/v2/api.js`.

Because of [domain restrictions](https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/), it's not possible to simply add the Canva Button to an HTML file on your local machine and open that file in a web browser. You need to serve the HTML file via `localhost`. To learn more, refer to [Local development](https://www.canva.dev/docs/button/platform-concepts/local-development/).

## Step 2: Customize the Canva Button

The default Canva Button creates a new design in the Canva editor. This is neat, but the Canva Button can do so much more.

To learn about all of the Canva Button's features, refer to the guides in the sidebar.

If you want even more control over the Canva Button, consider using the [JavaScript API](https://www.canva.dev/docs/button/javascript/api-reference/create-design/).

## Example
    
    
    <!DOCTYPE html>
    
    <html lang="en">
    
      <head>
    
        <meta charset="UTF-8" />
    
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    
        <title>Canva Button</title>
    
      </head>
    
      <body>
    
        <button
    
          data-design-type="Poster"
    
          data-api-key="API KEY GOES HERE"
    
          class="canva-design-button"
    
          style="display: none;"
    
          >Design with Canva</button
    
        >
    
        <script>
    
          (function (c, a, n) {
    
            var w = c.createElement(a),
    
              s = c.getElementsByTagName(a)[0];
    
            w.src = n;
    
            s.parentNode.insertBefore(w, s);
    
          })(document, "script", "https://sdk.canva.com/designbutton/v2/api.js");
    
        </script>
    
      </body>
    
    </html>

JSX

Copy
