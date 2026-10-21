---
url: https://www.canva.dev/docs/button/javascript/getting-started/
title: Getting started - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:59.448172+00:00
---

# Getting started - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/getting-started/

How-to guides

[Getting started](https://www.canva.dev/docs/button/javascript/getting-started/)[Creating designs](https://www.canva.dev/docs/button/javascript/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/javascript/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/javascript/editing-designs/)[Customization](https://www.canva.dev/docs/button/javascript/customization/)

# Getting started

Add the Canva Button to a website with the JavaScript API.

Copy page

Canva provides a JavaScript API for adding the Canva Button to websites. You can use this API to launch the Canva editor from your website.

If you're wondering whether the JavaScript API is right for you, see [HTML API vs. JavaScript API](https://www.canva.dev/docs/button/platform-concepts/html-api-vs-js-api/).

Here's how it works:

Your website opens the Canva editor in a modal. The user then creates or edits a design. When the user clicks the **Publish** button, your website downloads the user's design as an image file.

Broadly speaking, the main benefit of the JavaScript API is that it's more flexible than the [HTML API](https://www.canva.dev/docs/button/html/api-reference/). This means it's easier to tightly integrate the Canva Button with your website.

This tutorial series explains how to add the Canva Button to a website with the JavaScript API.

## Prerequisites

This tutorial assumes you have an API key to use the Canva Button. If you don't have one, [sign up for an API key](https://www.canva.dev/docs/button/quickstart/#step-1-sign-up-for-an-api-key).

## Step 1: Embed the SDK

Canva distributes an SDK for embedding the SDK in websites. The same SDK is used for the JavaScript and HTML APIs. To embed the SDK, use the HTML or JavaScript syntax. The syntax is different, but the end result is the same.

### HTML
    
    
    <script src="https://sdk.canva.com/designbutton/v2/api.js"></script>

MARKUP

Copy

### JavaScript
    
    
    ((document, url) => {
    
      const script = document.createElement("script");
    
      script.src = url;
    
      script.onload = () => {
    
        // API initialization
    
      };
    
      document.body.appendChild(script);
    
    })(document, "https://sdk.canva.com/designbutton/v2/api.js");

JAVASCRIPT

Copy

If you're using the China version of the SDK, replace `https://sdk.canva.com/designbutton/v2/api.js` with `https://sdk.canva.cn/designbutton/v2/api.js`.

Because of [domain restrictions](https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/), it's not possible to add the Canva Button to an HTML file on your local machine and open that file in a web browser. You need to serve the HTML file via `localhost`. To learn more, refer to [Local development](https://www.canva.dev/docs/button/platform-concepts/local-development/).

## Step 2: Initialize the JavaScript API

To initialize the JavaScript API, call the [`initialize`](https://www.canva.dev/docs/button/javascript/api-reference/initialize/) method:
    
    
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

Replace `API KEY GOES HERE` with your Canva Button API key. This API key is not a sensitive value.

The `initialize` method returns an object with two methods:

  * [`createDesign`](https://www.canva.dev/docs/button/javascript/api-reference/create-design/)
  * [`editDesign`](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/)



You can use these methods to create or open an existing design in the Canva editor.

Don't call the `initialize` method multiple times on the same page.

## Step 3: Render a Canva Button

Unlike the HTML API, Canva doesn't provide pre-made buttons for the JavaScript API. You have complete control over how the button looks and how it integrates with your website.

For advice on how to style the button, refer to [Customization](https://www.canva.dev/docs/button/html/customization/).

## Example

This example demonstrates how to set up a Canva Button that allows users to create a new design in the Canva editor. To learn more about creating designs, refer to [Creating designs](https://www.canva.dev/docs/button/html/creating-designs/).
    
    
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
