---
url: https://www.canva.dev/docs/button/html/customization/
title: Customization - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.414361+00:00
---

# Customization - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/html/customization/

How-to guides

[Getting started](https://www.canva.dev/docs/button/html/getting-started/)[Creating designs](https://www.canva.dev/docs/button/html/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/html/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/html/editing-designs/)[Customization](https://www.canva.dev/docs/button/html/customization/)

# Customization

Customize the Canva Button with the HTML API.

Copy page

You can use HTML attributes to customize the size and theme of the Canva Button. The following image demonstrates the different combinations of sizes and themes:

![](https://www.canva.dev/_next/static/media/canva-button-themes.10ce2804.png)

## Size

To customize the size of the Canva Button, add the `data-button-size` attribute to the Button's `button` element:
    
    
    <button
    
      data-design-type="Poster"
    
      data-api-key="API KEY GOES HERE"
    
      data-button-size="large"
    
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

There are four sizes to choose from:

  * `default`
  * `tiny`
  * `small`
  * `large`



If you don't specify a size, Canva uses the `default` size.

## Theme

To customize the theme of the Canva Button, add the `data-button-theme` attribute to the Button's `button` element:
    
    
    <button
    
      data-design-type="Poster"
    
      data-api-key="API KEY GOES HERE"
    
      data-button-theme="dark"
    
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

There are three themes to choose from:

  * `default`
  * `dark`
  * `light`



If you don't specify a theme, Canva uses the `default` theme.
