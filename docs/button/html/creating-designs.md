---
url: https://www.canva.dev/docs/button/html/creating-designs/
title: Creating designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.125833+00:00
---

# Creating designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/html/creating-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/html/getting-started/)[Creating designs](https://www.canva.dev/docs/button/html/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/html/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/html/editing-designs/)[Customization](https://www.canva.dev/docs/button/html/customization/)

# Creating designs

Create a design with the HTML API.

Copy page

If you followed the steps for [creating a Canva Button with the HTML API](https://www.canva.dev/docs/button/html/api-reference/), the generated code provides a Button that, when clicked, creates a new design in the Canva editor:
    
    
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

The presence of the `data-design-type` attribute on the `button` element tells Canva that clicking the Button should create a new design.

The value of the `data-design-type` attribute determines the _design type_ of the created design. The design type determines:

  * the dimensions of the design
  * the templates that Canva shows to the user



For a complete list of the supported design types, refer to [Design types](https://www.canva.dev/docs/button/reference/design-types/).

If the `button` element has a `data-design-type` attribute, it must not have a `data-design-id` attribute. The attributes are mutually exclusive.
