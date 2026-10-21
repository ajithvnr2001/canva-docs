---
url: https://www.canva.dev/blog/developers/simplifying-dx/
title: Simplifying developer experiences at scale - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:09.064402+00:00
---

# Simplifying developer experiences at scale - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/simplifying-dx/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Developer experience

# Simplifying developer experiences at scale

How Canva is bridging the gap between complex developer experience and the simplicity our users love

![](https://www.canva.dev/_next/static/media/thumbnail.7611d581.jpg)

* * *

  * 


[Faria Anzum⁠(opens in a new tab or window)](https://www.linkedin.com/in/farianzum)May 20, 2025

* * *

One big challenge we face when thinking of developer experience is bridging 2 worlds: the **simplicity** that Canva is known for and the **complexity** that often comes with developer experience. Canva’s ethos is to empower everyone to design, and we wanted to carry that into empowering developers to extend Canva. So, the challenge is how to make building on Canva feel as simple and intuitive as using Canva itself, without limiting what developers can do.

## From “one-step plugins” to a full-fledged platform

![the migration of extenstions to Canva apps](https://www.canva.dev/_next/static/media/2.1e951b98.jpg)

When Canva first launched our App Store around 2019, we introduced a lightweight app model that we called Extensions. These made it easy for developers to connect their services to Canva. All they needed to do was provide a simple web endpoint, and Canva took care of everything else, including the UI and user interaction. Developers could enable a single core action like inserting content from a third-party source, applying an edit, or publishing a design to another platform.

This simplicity was a huge win. It meant developers could ship apps quickly, and it helped us grow to hundreds of apps used by millions, from content sources like Google Drive, Pexels, to publish destinations like Slack, Mailchimp.

As our ecosystem matured, we started hearing a recurring theme: **developers wanted more freedom**. They loved the ease of Extensions, but they wanted more; they wanted to create interactive, multi-step experiences, to fetch and manipulate data, or to be able to take multiple actions in one experience like importing content and editing a design, while having a native Canva UI without having to recreate the look and feel from scratch.

That’s what led us to reimagine our platform. In 2022, we launched the [Canva Apps SDK](https://www.canva.dev/docs/apps/), a powerful framework that gives developers access to Canva’s core capabilities through flexible APIs, along with a native UI system. With the SDK, apps can now support much more sophisticated functionality. For example:

  * Fetching external data (e.g. from a CMS or analytics tool)
  * Generating custom visuals dynamically
  * Letting users interact with content directly on the canvas



All within a single app. For example the [Eye Trace⁠(opens in a new tab or window)](https://www.canva.com/your-apps/AAGdYVta-h0/eye-trace?q=Eye+Trace) app. ![screenshot of the eye trace app landing page](https://www.canva.dev/_next/static/media/5.a58180c8.png)

  * The app scans your Canva design and uses AI to analyze visual hierarchy and attention patterns in seconds. This goes beyond static data, it dynamically responds to the specific design you’re working on.
  * Heatmaps and focus maps are overlaid directly within the object panel, which gives users in-context insight into which elements grab attention. This is only possible because of the SDK's canvas access and rendering capabilities.



This wasn’t just about adding more features, it was about giving developers the power to create richer design experiences that feel just as intuitive and delightful as Canva itself.

To support this, we also introduced the [App UI Kit⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-ui-kit/), a library of pre-built, Canva-native components like buttons, dialogs, color pickers, and more, so that if a user opens a third-party app inside Canva, it should feel seamless, like just another part of the product they already love.

## Look and feel like Canva: the app UI kit

![subset of components in the UI kit](https://www.canva.dev/_next/static/media/3.036e0a75.jpg)

One of the more innovative things we’ve done recently is leveraging AI to assist with onboarding and development. We introduced something called the [Canva Devs MCP Server](https://www.canva.dev/blog/developers/canva-dev-mcp-server/), which I’m pretty excited about. The MCP Server connects AI coding assistants (like ChatGPT Claude or other code helpers) with Canva-specific knowledge and tools. Why is that useful? Well, imagine you’re a developer new to Canva’s platform and you’re using an AI helper to speed up coding. Out of the box, that AI might not know anything about Canva’s APIs or how a Canva app is structured. The MCP Server fixes that by providing the AI with real-time context about Canva’s development patterns, components, and even access to our CLI and SDK functions.

In practice, this means a developer can ask something like, “Hey, generate a Canva app that lets users search Pexels and insert a photo,” and the AI (with the MCP Server) can actually scaffold that app using our CLI under the hood. It can suggest code using our APIs, or help debug why an app isn’t passing the design review. It’s like having a Canva expert pair-programmer with you. We’ve even demoed scenarios where the MCP Server-powered assistant will automatically localize your app by integrating our i18n (internationalization) library, or check your app for compliance with Canva’s design guidelines and fix the code.

This is still in beta, but it’s a glimpse of how we’re trying to guide developers in intelligent, context-aware ways that’s truly intuitive. Instead of reading a doc page for an hour, you might get the answer or code snippet you need through an AI assistant in seconds.

## Ready to Build?

If you’ve ever wished you could craft powerful design experiences with the same simplicity that defines Canva, the new [Canva Apps SDK](https://www.canva.dev/docs/apps/) and [MCP Server](https://www.canva.dev/docs/apps/dev-mcp-server/) might just be your perfect match. Jump in, get creative, and let us know what you build next!

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.3a2aa29c.jpg)](https://www.canva.dev/blog/developers/streamlining-real-estate/)

[Real EstateStreamlining Real Estate content creationLearn how to architect your Canva App to supercharge your real estate marketing content creation.](https://www.canva.dev/blog/developers/streamlining-real-estate/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)May 6, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.c59330ae.jpg)](https://www.canva.dev/blog/developers/building-with-content-publisher-part1/)

[Content Publisher IntentMeet the Content Publisher Intent - Part 1Understanding data flow and structure for publishing](https://www.canva.dev/blog/developers/building-with-content-publisher-part1/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Feb 19, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.19bbc178.png)](https://www.canva.dev/blog/developers/enterprise-app-launch/)

[EnterpriseCanva to Enterprises, 3 new apps to boardLaunching 3 new apps to improve your productivity at work](https://www.canva.dev/blog/developers/enterprise-app-launch/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Apr 11, 2024
