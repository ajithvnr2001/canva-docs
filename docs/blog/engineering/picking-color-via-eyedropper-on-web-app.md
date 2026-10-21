---
url: https://www.canva.dev/blog/engineering/picking-color-via-eyedropper-on-web-app/
title: Picking Color via Eyedropper on Web App - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:15.853056+00:00
---

# Picking Color via Eyedropper on Web App - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/picking-color-via-eyedropper-on-web-app/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Web App

# Picking Color via Eyedropper on Web App

The journey of the eyedropper in Canva.

![](https://www.canva.dev/_next/static/media/thumbnail.3b75317b.png)

* * *

  * 


[Xidorn Quan⁠(opens in a new tab or window)](https://www.upsuper.org/)Jan 27, 2022

* * *

Using an eyedropper to pick a color from the screen is ubiquitous for design software, yet Canva has lacked such a functionality on the web app until very recently. With the release of browsers based on Chromium 95, including Microsoft Edge 95 and Google Chrome 95, web users can now enjoy the eyedropper inside Canva.

## Creating an eyedropper in the browser is challenging

While an eyedropper looks like a simple and innocent feature, it's hard to implement with existing web APIs. To pick a color from the screen, the web app needs the ability to read the color of an arbitrary pixel, which could then be used to generate a full image on the screen; even if the user only wants to give one pixel of color. Granting such access to websites would implicitly be a disaster for privacy. An adversarial website might be able to know what applications you're using, what tabs are opened in your browser, what files are on your desktop, etc.

The [Screen Capture API⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Capture_API) already exists to capture the screen content, but it requires user authorization on both the browser and sometimes the operating system. This authorization would look confusing and scary for users especially because it is rarely used. They wouldn't expect the website to record their screen when they are just asking for a tool to pick a color. Another problem with this API is that it is designed for screen sharing, so the content it captures is in the form of a video stream. A video stream might not be a pixel-perfect match to the color on the screen, and for color picking, we want the color to be as precise as possible.

![](https://www.canva.dev/_next/static/media/img-0-9eW3X-vrlK7R0bxt.e5f3e388.png)

Example screen capture

While showing an eyedropper to pick an arbitrary color on the screen is impossible without user permission, it's not impossible to offer one for content inside the boundary of a specific web page. In many cases, our users probably just want to pick a color from within their design.

However, this is still not easy for us to implement.

In Canva, designs are rendered mostly with native CSS, HTML, and SVG. These technologies enable us to utilize browser functionalities without having to reinvent some significant parts of the rendering stack from scratch, especially for features around text and video but there are always trade-offs. Using native CSS and HTML means it's hard to rasterize page content within the browser, again for security and privacy reasons.

Historically, websites are allowed to load resources they don't own, including pages in iframes, images, stylesheets, and scripts, and those resources are loaded with user cookies attached by default. If a website has access to the pixel data of the page, it might gain access to cross-origin information that it shouldn't know by loading those resources, such as your avatar on Facebook.

Worse, the infamous CSS selector, `:visited`, allows websites to style an element with different colors based on whether a link was visited before. For example, on Google or DuckDuckGo, you can see the link to a page you visited before being purple, while unvisited pages are blue. This is very useful for users to know what pages they've visited, but if the website can read the colors, it could be able to partially extract the browsing history from it by putting a lot of links on a page and rasterizing them.

![](https://www.canva.dev/_next/static/media/img-1-Vq5FhdzbmtSd-4T1-gU5bA.f8f69799.png)

It is possible to rasterize an arbitrary DOM tree through SVG `<foreignObject>`, which allows embedding HTML within an SVG image. There are also JavaScript libraries that enable capturing page content, either via the aforementioned SVG approach or by having their own, independent CSS rendering implementation.

We have also developed a Rust implementation of the design renderer, which can be compiled to WebAssembly to provide rasterization of Canva designs. However, none of these methods are suitable for an eyedropper. Some are just too slow or resource consuming to use, and others don't have enough fidelity that users would expect from an eyedropper.

## Previous workarounds

While an eyedropper integrated into the web app is difficult, one workaround we've been suggesting to users is to use browser extensions, such as [ColorZilla⁠(opens in a new tab or window)](https://www.colorzilla.com/), to pick colors from the page.

When we were releasing our [Canva desktop app⁠(opens in a new tab or window)](https://www.canva.com/download/), one of the known shortcomings was that users no longer had access to browser extensions they could use for color picking. However, an independent desktop app has a different security model than a generic web app because it requires explicit installation, and its web view doesn't have access to private data in browsers by default. A desktop app can capture page content without a problem. Therefore we implemented the eyedropper feature for the desktop app first and later integrated it into our mobile apps.

Another workaround we provided is to have the color panel show existing colors in the design and prominent colors from images added. This satisfies a large number of use cases, because most people just want to align their color schemes across pages or to their image content.

However, we always know that it would be better to have an eyedropper directly.

## EyeDropper API

To fill this gap between web apps and native apps, the Microsoft Edge team proposed and implemented the new EyeDropper API. It is a very simple web API, as can be seen from its [explainer⁠(opens in a new tab or window)](https://github.com/WICG/eyedropper-api/blob/main/README.md) and [specification draft⁠(opens in a new tab or window)](https://wicg.github.io/eyedropper-api/).

A sample usage of the API is as follows.
    
    
    const eyeDropper = new EyeDropper();
    
    
    
    
    eyeDropper.open().then(
    
      // log the color in the form of #RRGGBB
    
      (result) => console.log(result.sRGBHex),
    
    
    
    
      (reason) => {
    
        if (reason.name === "AbortError") {
    
          // handle user cancellation
    
        } else {
    
          throw reason;
    
        }
    
      }
    
    );

JS

Copy

Note that for security reasons, the open method must be invoked from a user activation such as inside a click event handler. While picking color through the eyedropper, users can cancel using the escape key, similar to other APIs that can trap users in a controlled state, such as Fullscreen and PointerLock.

Because its browser support is still at an early stage, and while Mozilla has [expressed⁠(opens in a new tab or window)](https://github.com/mozilla/standards-positions/issues/557#issuecomment-925727706) some initial interest, it's currently only supported on the latest versions of Chromium-based browsers, and not at all on mobile devices. Until support for the EyeDropper API is universal, it's necessary to use feature detection so that we don't create a broken user interface on browsers that don't currently support it. Because this is an object on the top level, feature detection is easily done by checking its availability.
    
    
    const hasEyedropper = "EyeDropper" in window;

JS

Copy

You might have noticed that the name for the color result `sRGBHex` is a bit unusual. This is because there is some [ongoing work⁠(opens in a new tab or window)](https://wicg.github.io/color-api/) to provide a better Color API for the web. It will likely introduce a new `Color` object, making it easier to handle colors across different color spaces and with wide color gamuts taken into account. However, this work is also in the early design stage and it's unlikely to stabilize and become available on the web platform in the short term, so a more specific name describing the format being returned was chosen to avoid any conflict with future evolutions of the API.

It is worth noting that while this API is being shipped on Chromium-based browsers, there is still some [discussion⁠(opens in a new tab or window)](https://github.com/WICG/eyedropper-api/issues/13) around its security and privacy concerns. More specifically, whether this API could be used to trick users into unknowingly handing out their browsing history or information from other origins. One such theoretical attack is to trick users into doing a double click, but open the eyedropper at the first click and swap a cross-origin pixel (for example, an image showing your Facebook login status) under the cursor so that it can gain access to such information from the color being picked. There hasn't been enough consensus on whether existing mitigations or any mitigation other than requiring [cross-origin isolation⁠(opens in a new tab or window)](https://web.dev/cross-origin-isolation-guide/) would be able to prevent leaking user information.

## How we got here

The Microsoft Edge team reached out to Canva back in April 2020 to confirm with us that the EyeDropper API would indeed be a useful addition to the web platform and to clarify requirements. In July 2021, the Edge team reached out to us again, saying the feature was ready to test. We quickly integrated the feature into our web app, confirming that it does work very well, and provided some initial feedback. We enabled it for all our users when the feature shipped on Chromium-based browsers in the week of 21 Oct 2021.

## Conclusion

Eyedropper is ubiquitous for design softwares, but creating one for a web app like Canva was challenging. The lack of a web API due to security and privacy concern was a large obstacle. The new web API overcame these issues.

Try it now on Canva!

## Acknowledgements

Big kudos to the Microsoft Edge platform team for proposing and implementing this amazing new web API. Special thanks to [Greg Whitworth⁠(opens in a new tab or window)](https://www.linkedin.com/in/gregwhitworth/), [Clay Martin⁠(opens in a new tab or window)](https://www.linkedin.com/in/instylevii/), [Ionel Popescu⁠(opens in a new tab or window)](https://www.linkedin.com/in/ionelpopescu/) for reaching out to us about this API.

Huge thanks to [Ellie Shin⁠(opens in a new tab or window)](https://www.linkedin.com/in/elizabethveprik/) and [Kurt Lash⁠(opens in a new tab or window)](https://www.linkedin.com/in/kurtlash/) for clarifying product requirements with the Edge team, [Sean Lee⁠(opens in a new tab or window)](https://www.linkedin.com/in/sean-lee-075b3b65/) and [Vadim Brodsky⁠(opens in a new tab or window)](https://www.linkedin.com/in/vadimbro/) for reviewing the changes to integrate this new API into Canva, [Joscha Feth⁠(opens in a new tab or window)](https://www.linkedin.com/in/joschafeth/), [Toby Rahilly⁠(opens in a new tab or window)](https://www.linkedin.com/in/tobyrahilly/), and [Grant Noble⁠(opens in a new tab or window)](https://www.linkedin.com/in/grant-noble-8253994a/) for suggestions in improving this post.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.9d40c487.png)](https://www.canva.dev/blog/engineering/product-analytics-event-collection/)

[BackendHow Canva collects 25 billion events per dayThe architecture of our product analytics event delivery pipeline.](https://www.canva.dev/blog/engineering/product-analytics-event-collection/)

[Long Nguyen⁠(opens in a new tab or window)](https://au.linkedin.com/in/long-hung-nguyen)Jul 10, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.b9cff2fd.png)](https://www.canva.dev/blog/engineering/session-revocations-at-scale/)

[BackendSession revocations at scaleHow Canva keeps hundreds of millions of user sessions fast and secure](https://www.canva.dev/blog/engineering/session-revocations-at-scale/)

[Llew Vallis⁠(opens in a new tab or window)](https://www.linkedin.com/in/llew-vallis-153b50246)Jul 22, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.eeec7a21.png)](https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/)

[Quality AssuranceHow We Used Data to Optimize Our Quality Assistance ModelFrom firefighting chaos to problem solving zen.](https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/)

[Zi Yang Pang⁠(opens in a new tab or window)](https://www.linkedin.com/in/pangzy/)Aug 29, 2022

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


