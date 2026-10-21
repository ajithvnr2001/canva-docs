---
url: https://www.canva.dev/docs/button/javascript/creating-designs/
title: Creating designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:58.894525+00:00
---

# Creating designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/creating-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/javascript/getting-started/)[Creating designs](https://www.canva.dev/docs/button/javascript/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/javascript/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/javascript/editing-designs/)[Customization](https://www.canva.dev/docs/button/javascript/customization/)

# Creating designs

Create a new design with the JavaScript API.

Copy page

After [setting up the JavaScript API](https://www.canva.dev/docs/button/html/getting-started/), the next step is to allow users to create a design with the Canva editor.

To do this, call the [`createDesign`](https://www.canva.dev/docs/button/javascript/api-reference/create-design/) method:
    
    
    api.createDesign({
    
      design: {
    
        type: "Poster",
    
      },
    
    });

JAVASCRIPT

Copy

At a minimum, the `createDesign` method expects an `opts.design.type` argument. This argument defines the _design type_ of a newly created design. The design type determines:

  * The dimensions of the user's design.
  * The templates that Canva shows to the user.



For a complete list of design types that Canva supports, refer to [Design types](https://www.canva.dev/docs/button/reference/design-types/).

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
