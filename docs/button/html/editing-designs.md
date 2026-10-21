---
url: https://www.canva.dev/docs/button/html/editing-designs/
title: Editing designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.351621+00:00
---

# Editing designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/html/editing-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/html/getting-started/)[Creating designs](https://www.canva.dev/docs/button/html/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/html/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/html/editing-designs/)[Customization](https://www.canva.dev/docs/button/html/customization/)

# Editing designs

Edit an existing design with the HTML API.

Copy page

After a user [creates a design](https://www.canva.dev/docs/button/html/creating-designs/), they may want to edit that design at a later point in time. To enable this, Canva provides your website with the ID of the design. You can use this ID to re-open a design in the Canva editor.

This part of the tutorial series explains how to open an existing design in the Canva editor.

## Step 1: Get the ID of the design

You can get the ID of a design in the following ways:

  * Using an HTML `input` element.
  * Using JavaScript callback functions.



You can use whatever option is most convenient.

### Option 1: Using an HTML `input` element

On the same page as the Canva Button, create an `input` element with a unique `name` attribute:
    
    
    <input name="designId" />

HTML

Copy

Add either (or both) of the following attributes to the Canva Button's `button` element:

  * `data-on-design-open-input-design-id`
  * `data-on-design-publish-input-design-id`



Then set these attributes to the value of the `input` element's `name` attribute:
    
    
    <button
    
      data-design-type="Poster"
    
      data-on-design-open-input-design-id="designId"
    
      data-on-design-publish-input-design-id="designId"
    
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

If the `data-on-design-open-input-design-id` attribute is defined, Canva inserts the ID of the design into the specified field when the user opens a design. This includes when creating a new design or editing an existing design.

If the `data-on-design-publish-input-design-id` attribute is defined, Canva inserts the ID of the design into the specified field when the user publishes their design.

When Canva inserts a value into the `input` element, save the ID for future use.

### Option 2: Using JavaScript callback functions

On the same page as the Canva Button, create two JavaScript functions:
    
    
    function onDesignOpen(opts) {
    
      console.log(opts);
    
    }
    
    
    
    
    function onDesignPublish(opts) {
    
      console.log(opts);
    
    }

JAVASCRIPT

Copy

Each function should accept a single argument. These functions receive the same parameters as the JavaScript API's [`onDesignOpen`](https://www.canva.dev/docs/button/javascript/api-reference/on-design-open/) and [`onDesignPublish`](https://www.canva.dev/docs/button/javascript/api-reference/on-design-publish/) functions.

Add either (or both) of the following attributes to the Canva Button's `button` element:

  * `data-on-design-open`
  * `data-on-design-publish`



Then set these attributes to the names of the JavaScript functions:
    
    
    <button
    
      data-design-type="Poster"
    
      data-on-design-open="onDesignOpen"
    
      data-on-design-publish="onDesignPublish"
    
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

When a user opens a design, Canva calls the function specified in the `data-on-design-open` attribute. This includes when creating a new design or editing an existing design.

When a user publishes a design, Canva calls the function specified in the `data-on-design-publish` attribute.

You can access the ID of the design via the `opts.designId` parameter:
    
    
    function onDesignOpen(opts) {
    
      console.log(opts.designId);
    
    }
    
    
    
    
    function onDesignPublish(opts) {
    
      console.log(opts.designId);
    
    }

JAVASCRIPT

Copy

When Canva calls these functions, save the ID for future use.

You can also use the `data-on-design-publish` attribute to [Download a design](https://www.canva.dev/docs/button/html/downloading-designs/).

## Step 2: Open an existing design in the Canva editor

To open an existing design in the Canva editor, create a Canva Button with a `data-design-id` attribute:
    
    
    <button
    
      data-design-id="DESIGN ID GOES HERE"
    
      data-api-key="API KEY GOES HERE"
    
      class="canva-design-button"
    
      style="display: none;"
    
      >Edit design</button
    
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

The presence of the `data-design-id` attribute on the `button` element tells the Canva Button SDK that clicking this button should open an existing design. The value of the `data-design-id` attribute must be the ID of a design.

If the `button` element has a `data-design-id` attribute, it must not have a `data-design-type` attribute. These attributes are mutually exclusive.
