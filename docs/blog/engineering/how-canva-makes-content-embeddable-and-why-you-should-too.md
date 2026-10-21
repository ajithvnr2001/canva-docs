---
url: https://www.canva.dev/blog/engineering/how-canva-makes-content-embeddable-and-why-you-should-too/
title: How Canva makes content embeddable (and why you should too) - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:13.829684+00:00
---

# How Canva makes content embeddable (and why you should too) - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/how-canva-makes-content-embeddable-and-why-you-should-too/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Embeddable Content

# How Canva makes content embeddable (and why you should too)

In the end, embeds are about making content on the web even more connected and shareable, which is what the web is all about.

![](https://www.canva.dev/_next/static/media/thumbnail.f36d13a8.png)

* * *

  * 


[Paul Knittel⁠(opens in a new tab or window)](http://www.paulknittel.com/)Apr 28, 2017

* * *

 _Originally published by_ [_Paul Knittel_ ⁠(opens in a new tab or window)](http://www.paulknittel.com/) _at product.canva.com on April 28, 2017._

Maybe by the time you're reading this the embedded design above has changed a few times.

A designer didn't like the font and swapped it for me. A colleague didn't like the phrasing and reworked it. All this happened without any emailing of files, uploading or downloading.

I just shared the design with them on Canva, and their edits automatically updated on this blog page. No one had to worry about exporting the image for web or uploading it to our blog, I just copied and pasted the embed code. Maybe one of our colleagues even loved it and shared it on Twitter straight from the blog.

That's the magic of embeds: easy sharing of content and automatic updating across the web. For the user the messy back and forth between their computer file system and the web disappears.

Maybe you're already imagining what kind of embed you could make for your web app, your startup or your company. Embeds are a growing thing — just the other day Apple released their own [Keynote embed feature⁠(opens in a new tab or window)](https://9to5mac.com/2017/03/30/how-to-embed-keynote-presentations-in-blogs-websites-iwork-mac-ios/) (in a hacky kind of way). But making embeds isn't just for big companies like Apple and YouTube — you can make them too!

## Creating your own embeddable content

Although there are lots of subtleties to creating a good embed, getting started is easy and straightforward: to create your own embed you need to offer users some code that they can include on their own website. There's lot of variation on how to do this, but I'll explain the basics first and then break down how the Canva embed code works.

To embed a website within another website HTML provides the iframe tag which is perfect for this use case: _"The HTML Inline Frame Element`<iframe\>` represents a nested browsing context, effectively embedding another HTML page into the current page."_ — [MDN⁠(opens in a new tab or window)](https://developer.mozilla.org/en/docs/Web/HTML/Element/iframe).

This means providing an embed of a user's design could be as simple as putting the [Canva design view⁠(opens in a new tab or window)](https://www.canva.com/design/DACUhj9jKOQ/view) page into an iframe:
    
    
    <iframe
    
      src="https://www.canva.com/design/DACL-CgO2NA/ybPLSlaEaBqein2rb-ohaw/view"
    
    ></iframe>

HTML

Copy

Loading a Canva /view page in an iframe won't actually work as we don't allow most pages to be loaded within an iframe for security reasons.

## Improving the user experience

Although you now have your own embed this doesn't provide the best user experience. Think of a YouTube page with its comments, recommendations, navigation and all the other cruft that comes with the webpage — do you really want to embed all of that in your own website? If you're providing embedable content you want to make sure that your embed focuses on providing valuable content. This can be as radical as only showing a video with a play button, or for a site like Canva we can create a minimal embed that shows just the design and allows for easy sharing and flicking though multiple pages. In many ways it works just like the `/view` page but stripped down to the essentials.

![](https://www.canva.dev/_next/static/media/img-1-mzoNtmNhOX.f36d13a8.png)

A screenshot of an embed

To avoid having to reinvent the wheel Canva embeds use the same slideshow component as used on the /view page — both powered by the same JavaScript code. To achieve different styling a slightly different variation of the HTML template and CSS is used.

## But why is there no iframe in Canva's embed code?

If you carefully look at Canva's embed code you will notice that it doesn't actually contain an iframe. Why is that?
    
    
    <div
    
      class="canva-embed"
    
      data-height-ratio="0.8383"
    
      data-design-id="DACSWFLr08k"
    
      style="padding:83.83% 5px 5px 5px;background:rgba(0,0,0,0.03);border-radius:8px;"
    
    ></div>
    
    <script async src="https://sdk.canva.com/v1/embed.js"></script>
    
    <a
    
      href="https://www.canva.com/design/DACSWFLr08k/view?utm_content=DACSWFLr08k&utm_campaign=designshare&utm_medium=embeds&utm_source=link"
    
      target="_blank"
    
      >Why Canva makes embeds</a
    
    >
    
    by
    
    <a
    
      href="https://www.canva.com/dannykennedy2?utm_campaign=designshare&utm_medium=embeds&utm_source=link"
    
      target="_blank"
    
      >Dan Kennedy</a
    
    >

HTML

Copy

For simplicity this can be stripped down to the essentials (which will still work):
    
    
    <div
    
      class="canva-embed"
    
      data-height-ratio="0.8383"
    
      data-design-id="DACSWFLr08k"
    
    ></div>
    
    <script async src="https://sdk.canva.com/v1/embed.js"></script>

HTML

Copy

The magic in Canva's embed code comes from the `<script>` tag. The script tag runs a script on the embedded website that dynamically inserts the iframe onto the page. This in itself doesn't have any advantage besides keeping the embed code a little shorter, but by having a script on the embed website we can make the iframe responsive to the container the embed is on.

Unlike an image, iframes don't neatly scale to the dimensions of content within them. To make sure that our iframe is the right size we detect the width of the container that the embed is in and then calculate the dimensions of the embed using the ratio of the design. This is how we achieve an edge-to-edge image experience with rounded corners. Every time the container or window is resized we simply recalculate the style, taking advantage of the 'data-height-ratio' defined on the HTML element.
    
    
    /**
    
     * Turn canva elements into iframe
    
     *
    
     * @param {!Element} embedEl
    
     */
    
    function embedify(embedEl) {
    
      // Some more stuff here unrelated to resizing
    
    
    
    
      // Watch window in case size changes - note: would be good to watch for div changes as well
    
      window.addEventListener("resize", () => resize(embedEl, iframe, ratio), true);
    
    }
    
    
    
    
    /**
    
     * Matches the element to the wrapper size with the correct ratio
    
     *
    
     * @param {!Element} wrapper
    
     * @param {!Element} element
    
     * @param {number} ratio
    
     */
    
    function resize(wrapper, element, ratio) {
    
      // Get parent container and match width for embed.
    
      const parentElRect = wrapper.getBoundingClientRect();
    
      const maxWidth = wrapper.getAttribute("data-max-width")
    
        ? wrapper.getAttribute("data-max-width")
    
        : MAX_EMBED_WIDTH_PX;
    
      const embedWidth = Math.min(
    
        Math.max(MIN_EMBED_WIDTH_PX, parentElRect.width),
    
        maxWidth
    
      );
    
      // The same logic is currently defined here: com.canva.cfe.mvc.OembedController.buildResponse
    
      const actionBarHeight = embedWidth < 300 ? 43 : 45;
    
      const embedHeight = embedWidth * ratio + actionBarHeight;
    
      element.style.width = `${embedWidth}px`;
    
      element.style.height = `${embedHeight}px`;
    
      if (wrapper.getAttribute("data-max-width")) {
    
        wrapper.style.width = `${embedWidth}px`;
    
      }
    
    }

JS

Copy

Having a script also allows us to dynamically change things in the future. Although right now we have rounded corners and a slight shadow on our iframe, having a script gives us the flexibility to make changes and update the iframe styling without users having to update their embed code — as can be seen in our `embedify` function below.
    
    
    /**
    
     * Turn canva elements into iframe
    
     *
    
     * @param {!Element} embedEl
    
     */
    
    function embedify(embedEl) {
    
      // Create iFrame use to attach to page
    
      const iframe = document.createElement("iframe");
    
      iframe.src = iframeSrc;
    
      embedEl.classList.add("canva-embed--loaded");
    
      // Add styling to container
    
      embedEl.style.boxShadow = "0 2px 8px 0 rgba(63,69,81,0.16)";
    
      embedEl.style.padding = "0";
    
      embedEl.style.borderRadius = "8px";
    
      embedEl.style.overflow = "hidden";
    
    
    
    
      // more stuff after this :)
    
    }

JS

Copy

It should be noted that there are a few disadvantages to using a `<script>` tag. Most importantly: they limit the supported platforms that will be able to run your embed. For example, some content management systems like WordPress don't by default allow you to include a script tag as part of a blog post or page, for security reasons. Luckily there is a technology called "oEmbeds" that addresses some of the compatibility issues (more on that later). However, if you are just getting started these limitations may or may not be the right decision for your business. I've included a comparison matrix at the end of the blog post so you can see which approach to embeds might be best for you.

## Handling large amounts of traffic

The traffic to a page that contains some of your embedded code can easily be huge — just imagine if your embed was put onto a popular news article seen by millions of people. Every visit to that page is a visit to your site, because the containing page will be fetching your code each time it's loaded. Therefore, it's important to make caching and performance an early consideration if you're going to be serious about providing a reliable embed.

At Canva our backend is powered by Java with Cloudflare sitting in between as the caching layer. For embeds we take advantage of Cloudflare's caching not just for static files. In fact we ensure that for each set of url parameters to a page an identical response is returned each time (kind of like a pure function, for those familiar with functional concepts). This allows us to cache embed page loads aggressively, knowing there is no user state (such as current user information) embedded in the returned content. The URL describes exactly what the output is, which means that the content can be served directly from Cloudflare without having to go through to our backend infrastructure after the first request. To ensure the content updates automatically, the Cloudflare cache has a TTL of 15 minutes, which we think is a good compromise between real time updating and high performance.

Another thing that makes it possible to fully cache embeds is that we don't rely on any API requests to our backend. Normally the document is requested via Ajax, but for embeds we pre-populate the document model into the HTML so that no additional Ajax requests need to be performed after the initial page load. This can be seen if you look at the HTML source of the embed request for a design — you will find the following somewhere in the header:
    
    
    <link
    
      rel="alternate"
    
      type="application/json+oembed"
    
      href="https://www.canva.com/_oembed?url=https%3A%2F%2Fwww.canva.com%2Fdesign%2FDACHZTlgWkU%2Fview"
    
    />
    
    <link
    
      rel="alternate"
    
      type="text/xml+oembed"
    
      href="https://www.canva.com/_oembed?url=https%3A%2F%2Fwww.canva.com%2Fdesign%2FDACHZTlgWkU%2Fview&format=xml"
    
    />

HTML

Copy

Setting up Cloudflare caching is fairly straightforward and can be done by simply setting the HTTP caching headers returned from your backend.

## Unlock the power of oEmbeds

Another simple but powerful technology to consider when making your embed is oEmbeds. This technology provides users the ability to create embeds from content URLs instead of having to copy an embed code manually. There are some websites (for example Medium) that only allow embedding via oEmbeds. Support for oEmbeds has increased recently, to the point where Apple's new Keynote embed feature only works via oEmbeds.

So what exactly is an oEmbed? According to the [official website⁠(opens in a new tab or window)](http://oembed.com/) of the oEmbed spec:

> oEmbed is a format for allowing an embedded representation of a URL on third party sites. The simple API allows a website to display embedded content (such as photos or videos) when a user posts a link to that resource, without having to parse the resource directly.

In other words, oEmbeds are a way to get an embed without the user having to copy and embed code manually. It works by creating a standard API endpoint that returns a HTML embed code or image or video source. Thanks to the additional parameters "width" and "height", oEmbeds can support responsive adjusting to the embedded container.

oEmbed auto discovery works by including some meta tags into the header of a website to let the consumer know that an oEmbed endpoint is available and where it can be accessed. This is what powers the Medium editor auto-embed, as shown in the GIF below:

The process to get the embed code looks like this:

## Whitelisting & oEmbeds

Not all websites use auto-discovery, some rely on lists of URL patterns with matching oEmbed endpoints; otherwise known as whitelisting. It's not as scary as it sounds though and depending on the platform it can be a straightforward process. For example Medium uses [embed.ly⁠(opens in a new tab or window)](http://embed.ly/) for embedding (in fact they acquired embed.ly in 2016), so [applying to become an embed.ly provider⁠(opens in a new tab or window)](http://embed.ly/providers/new) will add support on Medium. They have a list of requirements to become a provider, but the technology that makes it all work behind the scenes is the oEmbed standard.

Becoming whitelisted on WordPress is a little bit more challenging. Although self-hosted WordPress installs support auto discovery, blogs hosted by Automattic on WordPress.com only allow embeds from whitelisted providers. Getting onto the whitelist can be challenging and is best illustrated by reading [this section in the WordPress contributor handbook⁠(opens in a new tab or window)](https://make.wordpress.org/core/handbook/contribute/design-decisions/#whitelisting-oembed-providers). **TL;DR** You need to be a large company with millions of users in order for them to take notice.

## Comparison Matrix

![](https://www.canva.dev/_next/static/media/img-1-3UA5dTDyVCpI124pqfvDZg.2b89bdce.png)

_Shadow DOM provides encapsulation for DOM and CSS in a Web Component. It allows you to create an embed with custom styling that is not affected by the context of the contained website (kind of like an iframe). It's useful for simple embeds that are mostly just text that don't need the overhead of an iframe._

## Conclusion

What I really love about embeds is how easy it is to get started with them. You can build up functionality as you go and as your technology evolves. Just start by allowing users to copy an iframe tag with your website, then build up the user experience and performance as necessary. There's no reason not to start. There are also added benefits for you — spreading your brand on the web and acquiring more users. There can also be analytics and SEO advantages, depending on how you implement your embeds.

Embeds are set to become more important in the future, as they embrace the idea of being completely web-based — not relying on the user's file system but streaming on-demand directly from the source. The web is becoming a collection of specialised service providers such as Dropbox for file sharing, Instagram for photo sharing, Canva for graphic design. Each service does one thing well and by connecting services through embeds we can let everyone do what they do best.

**In the end, embeds are about making content on the web even more connected and shareable, which is what the web is all about. Embeds embody something of the intrinsic value of the Internet — its spirit of openness, collaboration and integration across systems and countries.**

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.44a38b3c.jpg)](https://www.canva.dev/blog/engineering/canva-incident-report-api-gateway-outage/)

[Post incident reviewCanva incident report: API Gateway outageAn incident report for the Canva outage on November 12, 2024.](https://www.canva.dev/blog/engineering/canva-incident-report-api-gateway-outage/)

[Brendan Humphreys⁠(opens in a new tab or window)](https://www.linkedin.com/in/brendanhumphreys/)Dec 20, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.7a551639.png)](https://www.canva.dev/blog/engineering/service-aligned-data-platform-architecture/)

[Data PlatformService-aligned Data Platform ArchitectureHow the data analytics platform team scaled data ingestion from various services at Canva.](https://www.canva.dev/blog/engineering/service-aligned-data-platform-architecture/)

[Jaskirat Grover⁠(opens in a new tab or window)](https://www.linkedin.com/in/jaskiratgrover/), [Justin Ty⁠(opens in a new tab or window)](https://www.linkedin.com/in/justinty/)Jun 9, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.a37b15f6.png)](https://www.canva.dev/blog/engineering/from-zero-to-50-million-uploads-per-day-scaling-media-at-canva/)

[Backend EngineeringFrom Zero to 50 Million Uploads per Day: Scaling Media at CanvaThe evolution of media persistence during hypergrowth at Canva](https://www.canva.dev/blog/engineering/from-zero-to-50-million-uploads-per-day-scaling-media-at-canva/)

[Jacky Chen⁠(opens in a new tab or window)](https://au.linkedin.com/in/junjie-chen-78b1a796), [Robert Sharp⁠(opens in a new tab or window)](https://au.linkedin.com/in/robertnsharp)Nov 29, 2022

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


