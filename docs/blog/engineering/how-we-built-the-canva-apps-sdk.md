---
url: https://www.canva.dev/blog/engineering/how-we-built-the-canva-apps-sdk/
title: How we built the Canva Apps SDK - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:14.718664+00:00
---

# How we built the Canva Apps SDK - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/how-we-built-the-canva-apps-sdk/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Engineering Practices

# How we built the Canva Apps SDK

Our journey to empower developers to build flexible apps with a simple powerful app platform.

![](https://www.canva.dev/_next/static/media/thumbnail.6dcc30b0.png)

* * *

  * 


[Martin Cronjé⁠(opens in a new tab or window)](https://www.linkedin.com/in/mcronje/)Jul 28, 2023

* * *

Reflecting on our journey to build and launch the Canva Apps SDK in June 2022, our Ecosystem team decided to share the insights and lessons learned as we built and evolved the Canva Apps SDK.

## Identifying a need

Inspired by Canva’s mission to _Empower the World to Design_ , we launched our App store in late 2019 with the goal of making app development as simple as possible for each part of the design process.

At the heart of the App Store, we built Extensions, a plugin model that allowed app developers to extend the three essential design activities:

  * Content extensions, where users could import images, videos, or embeds into their design from any source, such as Google Drive, TypeForm, and Giphy (my personal favorite -- let’s face it, who doesn’t love adding awesome gifs to their presentations!).
  * Edit extensions enabled users to edit raster or vector images off-platform, such as the incredibly successful background remover.
  * Publish extensions allowed users to post their designs to any platform, such as Slack or Hubspot.



To build an app, developers only needed a simple web-service endpoint and app configuration. The plugin framework took care of the apps rendering in-product and called the web services at the right time. Developers didn't have to build complex UIs to bring their ideas to life.

![Three blocks representing the user which interacts with Canva that then calls the Extension service! An arrow highlights that Extension is the app](https://www.canva.dev/_next/static/media/img-diagram.4305e9e3.png)

This approach resulted in hundreds of apps being developed, with a few very successful ones. However, we wanted more. Listening to our developers through interviews and our support channels, we realized that the plugin model needed to offer more flexibility. We had the opportunity to push ourselves to unleash the creativity of thousands of developers.

## Canva Apps vision

We needed to build a simple yet powerful platform that gives developers the tools to build rich apps. Success with the SDK would mean that we needed to give developers maximum control over the app's user interface while providing access to interoperable APIs that can be mixed and matched within the app.

This also meant that we needed to expose many key user interactions within the product as APIs, for example, user interactions in the editor.

The main shift in thinking was that we would go from Extensions that could only do one thing (insert, edit, or publish) to Apps that could do anything developers could imagine by giving them a flexible user interface and the ability to use different APIs.

Building a great platform is more than giving people access to product functionality through powerful APIs. We needed to build an integrated app runtime environment that makes it easy for developers to build experiences that feel native to the product. This functionality isn’t always achieved by API endpoints, but also by including capabilities such as our UI Kit, signing secure HTTP requests, hot-module-reloading, and runtime package injection. For simplicity, this article refers to all these capabilities as APIs.

## Refining through continuous feedback

Rebuilding our platform to give our developers more power is an excellent example of one of Canva’s engineering values, _"How does this help our users?"_

Our users and developers are at the heart of every engineering decision. This thinking is not just limited to our product and design team. We expect every Canva engineer, especially in our APIs teams, to consider the user and developer journey to ensure we build delightful APIs.

So to achieve this, we do the following:

  * We start with developer interviews, data insights, and listening to our various market-facing teams, such as sales, partnerships, and support.
  * When we understand the opportunity, we build an initial version of the API and follow up with internal releases. We often support these releases through internal hackathons, where we dogfood the APIs.
  * When we’re happy with the features, we follow up with preview releases where our alpha and beta developers often provide valuable insights.
  * Finally, we have our public launches.



Dogfooding with internal releases and listening to developers in preview releases massively influenced our product direction for the better. So this approach has become the standard model for how we approach API development.

The remainder of this article dives into two areas of the Apps SDK development process. First, we’ll explore how the team iterated as they built the app runtime environment, and then we’ll summarize the API.

## Building the app runtime environment

At the highest level, we have the app built by a developer. This app runs inside the Canva editor, which contains product features used by the apps.

An app is a JavaScript bundle that loads inside a sandboxed IFrame. This sandbox protects our users and the Canva product from potentially unsafe app code, such as leaking sensitive user information or corrupting designs.

Apps then communicate to our various APIs in the App Sandbox. Looking at the inner workings, these APIs communicate to a message bus that marshals calls back and forth between the Canva experience and the app.

We exposed an App controller to the message bus that wraps core product functionality. The App controller is a great place to serve as an adapter to protect our APIs from breaking changes as our product teams evolve their features.

![Visualisation of how an App runs in an Iframe and then communicates with Canva APIs](https://www.canva.dev/_next/static/media/img-architecture.7c6c01d2.png)

### Daunting scope

When we started this project, we realized the daunting work ahead of us:

  * Building a stable and secure sandboxed environment,
  * With a new brand build-and-deploy pipeline,
  * Complete with a new SDK, and
  * A seamless developer experience that minimizes breaking changes!



Delivering everything at once meant it would take a long time before we got anything to app developers.

We decided to dream big and start small and take a year to iterate on the app framework design. This was to ensure we had something to give to our developers early. We knew an iterative approach would require much more development effort, but that was okay because we could learn from our users and developers as we went.

Favoring quick feedback, we started with a simple and pragmatic approach of hosting Apps in simple S3 buckets. This approach required a lot of manual work to make it stable and secure. It also meant that we couldn’t leverage the full power of the internal platform that would give us automated build-time checks, rollback, clarity on who changes what, uniform type checking, and flexible security policies.

While this approach had a price, it also allowed us to rapidly prove the core Apps SDK with our internal hackathons and preview releases.

## Adding more sophistication

When we proved the core product vision, we started adding more sophistication.

Starting with a gateway service that allowed us to serve the apps from within the Canva infrastructure enabled us to begin leveraging our platform, such as infra tooling and flexible security policies. We then introduced automated builds to improve the checks, rollbacks, and audit logs. Finally, we implemented improved type-checking for API messages to simplify supporting backward compatibility and deprecation.

The combination of these facilities makes API development completely pluggable and allows our teams to deploy new API versions without breaking older ones.

The next phase of this journey was to introduce app manifests to make apps more portable and start working on command-line tooling.

## Building individual capabilities

### Planning and prioritization

Coming out of the numerous preview releases, we received excellent signals on the types of apps people build. Combining that with the insights we developed during early product discovery, we identified three app types to focus on:

  * Creation apps to allow users to create new content for designs.
  * Content apps to allow importing images, text, or media elements.
  * Data-driven apps to enable users to bring data from sources outside Canva for visualizations or automation.



We refer to these as App Archetypes and they enabled us to map out the potential capabilities we need to power increasingly more sophisticated versions of the apps they would enable.

For example, if we look at Creation apps, the core capabilities needed include, importing media, dragging and dropping elements onto the design page, and editing elements on the design. With later Creation app iterations, we can combine elements to create compound shapes and connect data to designs, and send media to third-party services for modifications. In future releases, we can continue to evolve these Creation apps to be richer such as providing real-time preview on the design surface, and much more.

App Archetypes were a massive breakthrough because they enabled us to ruthlessly prioritize which APIs we work on, decreasing our time to market. Establishing the core features we needed to expose gave us a minimum viable product to work towards.

It also meant that we deprioritized some APIs already deep into development in favor of being faster. However, it was worth it because we could focus on what mattered.

The outcome of all of this is that our beta developers could build better apps sooner.

### Striving to design great APIs

Outstanding APIs are expensive to design, maintain, and evolve because when APIs are in the wild and used by thousands of developers, they're very challenging to deprecate. Further, poorly designed APIs can make the ongoing evolution of core products difficult and sometimes impossible without deprecating the API.

These immutable truths mean that when designing APIs, we take a conservative approach in our designs and only expose the most powerful, stable, and composable building blocks of Canva. As such, we introduced a set of overarching principles that boil down to four essential qualities:

  * **Simplicity** : Inspired by Canva’s mission to empower the world to design, we make APIs as simple as possible without making them less powerful.
  * **Safety:** We have 135 million users who trust Canva, and our APIs should not compromise their data. These users created 15 billion designs over the years, and all still render in the product, so our APIs should also not corrupt any design data.
  * **Evolvability:** Decisions are expensive and time-consuming to undo, especially considering that poor APIs could couple internal product team development to deprecation cycles. In the same way, we also want to design APIs to add more functionality for developers without breaking changes.
  * **Consistency:** Consistency is critical to ensure our developers are productive and delighted throughout development. It also means that APIs should be predictable so that learnings from one part of the API are transferable to all others.



Underpinning these principles, we realize there's no perfect design, and there will be cases where it’s hard to adhere to all guidelines and qualities.

Also, as a general rule, we would rather postpone a new feature to the next release if we can’t preserve these qualities. When we wrote this principle a year ago, it was a bit scary that it might not work out. However, I’m pleased to see how we consistently made the right decision to defer APIs that aren't ready.

## API development lifecycle

At Canva, we work with small, highly cohesive, loosely-coupled teams empowered to hit their crazy big goals. Although this approach prioritizes speed, it biases focus to team goals, and they risk losing sight of a unified vision.

This is an example of how [Conway’s law⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Conway%27s_law) can manifest in teams. So, to strike a balance between alignment and empowerment, we established an API Design Working group consisting of engineers from each team, who were tasked to ensure APIs align with our principles, guidelines, and overall vision.

> _"Any organization that designs a system (defined broadly) will produce a design whose structure is a copy of the organization’s communication structure."_
> 
> — Melvin E. Conway

We’re careful not to make this a higher authority that approves the designs from an ivory tower. For us, the ultimate goal is to support and empower engineers with generosity, empathy, and humility to build great APIs.

Early on, this working group also introduced an API run sheet, which is a living document engineers use to track essential stages of an API’s lifecycle. For us, the value of this run sheet is that it puts the power in our API product teams’ hands and allows them to self-govern critically essential stages such as:

  * Rapid security risk assessments to identify MUST and SHOULD DO security activities.
  * Designing the engagement model for working with core product teams.
  * Guidance on validating that we’ve built the correct API and that we built it correctly.
  * Developing great templates for design docs, observability, analytics, and public announcements.



Using run sheets and design docs is consistent with Canva’s engineering culture of thinking through problems by writing them down. Design docs are great for determining the primary considerations for sophisticated software designs.

## Conclusion

We hope the value of “How does this help our users?” shines through in the care and thought we’ve put into the Canva Apps SDK, not just in the APIs themselves but also in the tooling and documentation behind them. And we have many Canva Engineers who are eager to live this value to understand our app developers’ (our users) ideas and see how best we can shape our APIs to enable their dreams.

We look forward to seeing how app developers help our diverse 135 million Canva users in ways we haven’t thought of yet. Sign-up to build your first app [here⁠(opens in a new tab or window)](https://www.canva.com/developers/).

## Acknowledgements

Thank you to [Anto Lepejian⁠(opens in a new tab or window)](https://www.linkedin.com/in/anto-lepejian-951b99133/), [Tom Northall-Little⁠(opens in a new tab or window)](https://www.linkedin.com/in/thomas-northall-little-073604111/) and [Dan Scott⁠(opens in a new tab or window)](https://www.linkedin.com/in/dan-scott-b17a7a36/) for making sure the App Runtime story is accurate. Thanks to [Grant Noble⁠(opens in a new tab or window)](https://www.linkedin.com/in/grant-noble-8253994a/) for editing contributions.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.c7e450c5.png)](https://www.canva.dev/blog/engineering/the-science-of-routing-print-orders/)

[BackendThe science of routing print ordersHow Canva uses graph traversal to handle the complexity of getting print orders to our customers.](https://www.canva.dev/blog/engineering/the-science-of-routing-print-orders/)

[Constantinos Kavadias⁠(opens in a new tab or window)](https://www.linkedin.com/in/ckavadias/), [Carmen Wang⁠(opens in a new tab or window)](https://www.linkedin.com/in/carmenwang0/), [Callum Grier⁠(opens in a new tab or window)](https://www.linkedin.com/in/calgrier/)Dec 10, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.7a551639.png)](https://www.canva.dev/blog/engineering/service-aligned-data-platform-architecture/)

[Data PlatformService-aligned Data Platform ArchitectureHow the data analytics platform team scaled data ingestion from various services at Canva.](https://www.canva.dev/blog/engineering/service-aligned-data-platform-architecture/)

[Jaskirat Grover⁠(opens in a new tab or window)](https://www.linkedin.com/in/jaskiratgrover/), [Justin Ty⁠(opens in a new tab or window)](https://www.linkedin.com/in/justinty/)Jun 9, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.059f71b8.png)](https://www.canva.dev/blog/engineering/how-canva-combined-modern-image-processing-with-150-year-old-optics-for-a-new-approach-to-camera/)

[Computer VisionCombining Classic and Modern: A New Approach to Camera SimulationApplying classic principles from physics and optics to build the best possible camera effects at Canva.](https://www.canva.dev/blog/engineering/how-canva-combined-modern-image-processing-with-150-year-old-optics-for-a-new-approach-to-camera/)

[Bhautik Joshi⁠(opens in a new tab or window)](https://bhautik.org)Nov 18, 2021

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


