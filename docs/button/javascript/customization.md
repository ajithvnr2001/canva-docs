---
url: https://www.canva.dev/docs/button/javascript/customization/
title: Customization - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:58.955526+00:00
---

# Customization - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/javascript/customization/

How-to guides

[Getting started](https://www.canva.dev/docs/button/javascript/getting-started/)[Creating designs](https://www.canva.dev/docs/button/javascript/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/javascript/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/javascript/editing-designs/)[Customization](https://www.canva.dev/docs/button/javascript/customization/)

# Customization

Customize the Canva Button with the JavaScript API.

Copy page

If you're using the JavaScript API, you have a lot of control over how the Canva Button looks and feels. This page provides guidelines for creating a Button from scratch.

## Themes and sizes

You can style the Button to align with the look and feel of your website, but Canva strongly recommends taking inspiration from the HTML API's themes. These themes are suitable for a variety of websites, while retaining the unique and familiar Canva style.

You can view the CSS for these themes on CodePen:

<https://codepen.io/arav-jay/pen/ZEydQaX>[⁠(opens in a new tab or window)](https://codepen.io/arav-jay/pen/ZEydQaX)

For more information, refer to [Customization](https://www.canva.dev/docs/button/html/customization/).

## Font styles

For the Button, Canva recommends using the _Open Sans_ font. If your page doesn't use Open Sans, add it to the page with [Google Fonts⁠(opens in a new tab or window)](https://fonts.google.com/specimen/Open+Sans):
    
    
    <link
    
      href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap"
    
      rel="stylesheet"
    
    />

MARKUP

Copy

The following snippet demonstrates how to apply the font to the button:
    
    
    .canva-design-button {
    
      font-family: "Open Sans", sans-serif;
    
      font-size: 16px;
    
      font-weight: 600;
    
      line-height: 1.6;
    
    }

CSS

Copy

### Notes

  * Include normal (400) and semi-bold (600) font weights.
  * If necessary, include non-Latin characters (for example, Cyrillic).
  * For the `tiny` size variation, use the normal font-weight.
  * For all other size variations, use the semi-bold font weight.



## Button text

If the type of design that users create with the Button is implied by its surroundings, Canva recommends using the default text **Design with Canva**. If not, using a longer call-to-action gives users more context, such as:

  * Design an invitation
  * Create your business card
  * Create a cover photo for your property
  * Design your logo



## Using the Canva logo

The type of Canva logo to be used in the Button depends on the theme you choose for the Button. Please use the logo files provided here in SVG and PNG formats, as they're tailored to the different themes and sizes:

<https://sdk.canva.com/v2/beta/button-logo-resources.zip>[⁠(opens in a new tab or window)](https://sdk.canva.com/v2/beta/button-logo-resources.zip)
