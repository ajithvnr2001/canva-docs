---
url: https://www.canva.dev/docs/button/javascript/editing-designs/
title: Editing designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:59.332899+00:00
---

# Editing designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/editing-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/javascript/getting-started/)[Creating designs](https://www.canva.dev/docs/button/javascript/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/javascript/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/javascript/editing-designs/)[Customization](https://www.canva.dev/docs/button/javascript/customization/)

# Editing designs

Edit an existing design with the JavaScript API.

Copy page

After a user [creates a design](https://www.canva.dev/docs/button/html/creating-designs/), they may want to edit that design at a later point in time. To enable this, Canva provides your website with the ID of the user's design. You can use this ID to re-open a design in the Canva editor.

This part of the tutorial series explains how to open an existing design in the Canva editor.

## Step 1: Get the ID of the user's design

To get the ID of the user's design, register callbacks with the [`onDesignOpen`](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/) and [`onDesignPublish`](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/) methods:
    
    
    api.createDesign({
    
      design: {
    
        type: "Poster",
    
      },
    
      onDesignOpen: (opts) => {
    
        console.log(opts.designId);
    
      },
    
      onDesignPublish: (opts) => {
    
        console.log(opts.designId);
    
      },
    
    });

JAVASCRIPT

Copy

The `onDesignOpen` callback runs when the user opens a design via the Canva Button. The `onDesignPublish` callback runs when the user publishes a design via the Canva editor. Both of these callbacks receive an `opts.designId` argument that contains the ID of the user's design.

When your website receives the ID of a user's design, it can save the ID for later use, but it doesn't particularly matter _how_ the website saves the ID. Some common patterns are persisting the ID to a database or storing it locally via [`localStorage`⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

## Step 2: Open an existing design in the Canva editor

To open an existing design in the Canva editor, call the [`editDesign`](https://www.canva.dev/docs/button/javascript/api-reference/edit-design/) method:
    
    
    api.editDesign({
    
      design: {
    
        id: "DESIGN ID GOES HERE",
    
      },
    
    });

JAVASCRIPT

Copy

At a minimum, the `editDesign` method expects an `opts.design.id` argument. This argument must contain the ID of a design that Canva can open in the editor.

The `editDesign` method accepts many of the same arguments as the [`createDesign`](https://www.canva.dev/docs/button/javascript/api-reference/create-design/) method, but the arguments are not identical. The main difference is that the `editDesign` method doesn't accept the `opts.design.type` argument. This is because the [design type](https://www.canva.dev/docs/button/reference/design-types/) of an existing design can't be changed.

You can pass the `onDesignOpen` and `onDesignPublish` methods into the `createDesign` _and_ `editDesign` methods.

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
    
        <button id="create-design">Create design</button>
    
        <button id="edit-design" disabled="true">Edit design</button>
    
        <button id="download-design" disabled="true">Download design</button>
    
    
    
    
        <script type="text/javascript">
    
          (async () => {
    
            if (!window.Canva || !window.Canva.DesignButton) {
    
              return;
    
            }
    
    
    
    
            const api = await window.Canva.DesignButton.initialize({
    
              apiKey: "API KEY GOES HERE",
    
            });
    
    
    
    
            let previousDesignId;
    
    
    
    
            const createDesignButton = document.querySelector("#create-design");
    
            const editDesignButton = document.querySelector("#edit-design");
    
            const downloadDesignButton = document.querySelector("#download-design");
    
    
    
    
            const handleDesignOpen = (opts) => {
    
              previousDesignId = opts.designId;
    
              editDesignButton.disabled = false;
    
            };
    
    
    
    
            const handleDesignPublish = (opts) => {
    
              previousDesignId = opts.designId;
    
              downloadDesignButton.disabled = false;
    
              downloadDesignButton.onclick = () => {
    
                window.location.href = opts.exportUrl;
    
              };
    
            };
    
    
    
    
            createDesignButton.onclick = () => {
    
              api.createDesign({
    
                design: {
    
                  type: "Poster",
    
                },
    
                onDesignOpen: handleDesignOpen,
    
                onDesignPublish: handleDesignPublish,
    
              });
    
            };
    
    
    
    
            editDesignButton.onclick = () => {
    
              api.editDesign({
    
                design: {
    
                  id: previousDesignId,
    
                },
    
                onDesignOpen: handleDesignOpen,
    
                onDesignPublish: handleDesignPublish,
    
              });
    
            };
    
          })();
    
        </script>
    
      </body>
    
    </html>

MARKUP

Copy
