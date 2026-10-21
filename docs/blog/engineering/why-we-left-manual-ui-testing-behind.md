---
url: https://www.canva.dev/blog/engineering/why-we-left-manual-ui-testing-behind/
title: Why we left manual UI testing behind - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:29.982740+00:00
---

# Why we left manual UI testing behind - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/why-we-left-manual-ui-testing-behind/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

UI Testing

# Why we left manual UI testing behind

How we use visual regression testing to instill confidence in every product update.

![](https://www.canva.dev/_next/static/media/thumbnail.e7e2d74e.jpg)

* * *

  * 


[Joscha Feth⁠(opens in a new tab or window)](https://twitter.com/joschafeth)Dec 12, 2018

* * *

 _Originally published by_ [_Joscha Feth_ ⁠(opens in a new tab or window)](https://twitter.com/joschafeth) _at_ [_product.canva.com_ ⁠(opens in a new tab or window)](https://product.canva.com/automated-visual-testing-at-canva/) _on December 12, 2018._

Visual regression testing is vital in a high growth tech startup like Canva to ensure any new code continues to work on our web application, whilst ensuring that visually, it looks just as good as before. In this blog, Canva engineer Joscha Feth shares his approach on visual regression testing to instill confidence in every product update.

Visual Regression Testing (VRT) can be quite a polarizing activity for the developer community — it's one of those things that can either make a developer's eyes sparkle with joy, or darken with rage. Which side of the fence you fall on often depends on how the process of updating the visual baseline and reviewing changes works in your company.

To explain what the baseline update is in simple terms — when, for example, you change the color of a button on a webpage from red to blue, every other developer who works on that page after you has to compare their changes against the blue button. Whilst you are working to change the button from red to blue however, that button on your baseline remains red. Only when you have merged your work back into the mainline does everyone's baseline for the button become blue. The newly generated images (the ones now containing the blue button) are stored centrally and will be the new point of reference for any developer subsequently working on the project.

At most companies that I've worked with previously, these baseline regenerations happen on the developer's machine. Because no two developer machines are the same, when it comes to something very intricate such as generating images for a website, it is very easy to produce a slightly different result every time a new change is introduced. This difference isn't necessarily visible to the human eye, but potentially visibly different to a computer. For example, there may be a few subpixels rounded differently in a new browser version, and thus the whole image is slightly shifted by one pixel — something which a computer would instantly understand as a difference, but would be undetectable in a superficial inspection by human eyes.

Because of this tooling problem, it's often impossible to know when there are real anomalies, as the noise caused by different tooling can be quite severe. The noise might disappear temporarily when you create a new baseline for yourself, but then shortly afterwards a colleague will say that they can see differences, because their machine will create a different image to yours — and the whole frustrating cycle begins again. This unexpected workload can be very aggravating for a developer who is working on multiple amendments to the source code, and has to keep constantly going back to make further changes to a UI that they hadn't even realized they'd adversely impacted — not to mention the additional effort of keeping tooling in sync.

This is why the automation of visual regression testing without using massive local tooling is a godsend for developers, as it eliminates the need for unreliable and time consuming manual testing, as well as having to maintain a possibly unreliable custom stack. There are currently only a few commercially available visual regression testing tools, as the market is still fairly new.

## Commercial solutions for visual regression testing

Of the 3 main commercial service offerings that were available when we looked to implement VRT at Canva, we opted for a tool called Percy.

For a design-centric business such as Canva, Percy is a very valuable tool, which allows us to speed up testing and catch even the small unintended visual changes that are sometimes created as side-effects of code changes.

### The future of commercially available visual regression testing tools

Currently, because the competition is quite small and the market is very big, automated VRT tools are all a bit more on the pricey side in terms of dev tool support — but I suspect that as more vendors come into the space in the near future, the cost will come down. Once this occurs, I firmly believe that it will become a standard tool in all frontend development workflows. Currently though, the cost is too prohibitive to be widely used across small agencies, hobby projects or for Open Source.

Canva has a very strong culture of peer reviewing code changes before they go into the mainline, and whilst it is often possible to reason about how code changes affect the system, it can be a time consuming riddle to reason through everything thoroughly. VRT helps us to speed up code reviews as well, as you can see from a real conversation in a pull request that I came across the other week:

As visual regression testing is yet to be widely adopted, a lot of companies have their own makeshift systems that work for better or for worse. Some companies have been doing it for a few years but the in-house tools they use are commonly very clunky and/or expensive to maintain. When you join a company and they have a visual regression suite, it is usually something that they have written themselves, requires a lot of attention and maintenance, and in the end doesn't work very well after all.

This is because there has been no clearly defined process to update and regenerate baselines. Up until the last couple of years, when commercially available VRT tools have become available as services, visual regression testing involved setting up a myriad of tools on your local machine, running those tools to generate the baseline, and whilst doing so, crossing your fingers and hoping the visual differences generated are only due to the changes made, and not because one of the dependencies to render these images has changed.

It may sound pretty straightforward, but keeping these dependencies stable can be complicated, as screen resolutions, browsers, libraries and machine types change. At Canva, we provide users with templates for a wide range of design projects, from online ads, flyers and logos, to posters, brochures, invitations, business cards, and much more. Whilst we already had visual regression testing for our exported designs, that particular system uses a well-defined rendering engine and is much easier to tame than common frontend and browser-based visual regression testing, so we decided to not reuse it for the web-development workflow. Percy, the service we are now using, comes with an API that will in fact allow us to replace our custom export regression testsuite with a Percy-managed project where we provide the baseline images coming from our export renderer, still retaining full control of the rendering but leveraging Percy's service integration with GitHub, baseline approval, diffing and more, which will greatly improve that part of our testing infrastructure.

Because commercially available visual regression tools are a recent phenomenon, companies have been forced to produce their own out of necessity. Percy is one of the first companies that has developed this technology and made it commercially available and fully supported, removing the headache of the ongoing maintenance of in-house solutions.

## Adopting percy.io

[Percy⁠(opens in a new tab or window)](https://percy.io/) was a service that I had wanted to try for a long time, but in its early days it was tightly coupled to the software development platform GitHub, so I wasn't able to use it, as the company I worked for previously had its own proprietary software development platform that was in direct competition to GitHub and not compatible with Percy.

After joining Canva (which uses GitHub), I knew the time was right. After a few weeks of trialling we knew that with the Percy workflow we could vastly improve testing by preventing unwanted visual regressions, without having to maintain a custom solution. Percy solved the visual baseline update and stability issues, and also provided a number of predefined workflows and integrations with services and tools we use.

There are only a few other commercially available products on the market aside from Percy, and one of these is owned and operated by one person. A company like Canva, which has over a hundred developers, could not seriously consider investing in a product from a company that only has 1 developer — if that company suddenly closed down or that person could no longer provide the support that we need, it would mean we had put a lot of effort into incorporating a product that is not supported any more and we would have to start again from scratch with another provider. With a product like Percy however, which is supported by a bigger team of developers, that risk factor is greatly reduced.

Visual regression testing tools are really not something that companies want to own either, due to the fact that so much effort is required for their ongoing maintenance. Automated VRT tools seem easy enough to create at the outset, but it's the maintenance of these tools that is onerous, not to mention potentially very costly. Commercially available tools such as Percy remove that burden.

Also, once a company develops its own tool, it inherits all the traits that are specific to that particular company and has features that are specific to the types of problems that company is typically trying to solve. This makes them very difficult to migrate away from, whereas something like Percy can be used for a whole range of visual regression testing requirements, and is therefore a lot more versatile and user-friendly.

### How to select the best tool for your company

Firstly, it's critical to draft a checklist of your requirements and benchmark those against each automated VRT vendor so you can determine which one best suits your specific needs. For Canva, selecting a visual regression tool wasn't just a random process. There were a few specific features we wanted that informed our decision to go with Percy:

  * Multiple projects that allow us to separate types of components by organizational structure whilst still sharing them Separate GitHub status checks for each of these projects on pull requests
  * Multi-browser regression testing
  * Stable engine (e.g. no local generation of images that could vary results just by simple changes in the CI container or local development environment)
  * An API, and with that the ability to integrate new toolchains into Percy — our best example for that is Storybook, which we were using to dissect and make our UI components accessible — we knew we wanted to have visual regression on all of them, but not necessarily duplicate the work of writing separate regression tests for each. Working together with the Percy team, we were able to come up with a solution which Percy then adopted as a first-class citizen of the Percy ecosystem
  * Responsive support with an eye to the future. This is particularly important because as frontend development changes so fast, you need a company that embraces this
  * Flexible pricing for a high number of snapshots and users — when we started out we knew that eventually all of Canva frontend engineering would use the new stack we were working on, so we needed to make sure that our solution could grow with us
  * Good support that doesn't shy away from delving into that one regression that you can't easily explain — we had to do that a few times. There is always a good explanation, but sometimes it is hard to find
  * A workflow hub for reviewing, updating the baseline, browsing past diffs (especially helpful when searching for the culprit of a baseline change that was accidentally approved in the past)



## How we set it up…

In the beginning, we set up Percy for our main app page, so on every master build Percy would produce a new baseline reference that the rest of the organisation could compare against in their feature branches.

Percy does have the ability to change the page state, but it means using custom APIs to do so. As we had already decided on a few other technologies to mutate browser state and decouple UI states from each other, we were a bit reluctant to add this complexity on top, hence we started looking at how we could do visual regression testing for our UI library, which is decomposed in a product called Storybook.

We managed to produce a proof-of-concept that worked, but was bound by runtime (we had hundreds of different stories already at that point in time, and we build them both for left-to-right and right-to-left text direction). Together with the Percy team, we were able to improve on that, essentially making it possible to produce hundreds of snapshots in a few seconds and render them immediately.

That's when things really kicked off. Suddenly, all of our frontend developers were able to immediately spot (both wanted and unwanted) visual changes in their pull requests.

Status checks on pull requests help to identify differences that will be made to the baseline. This prevents unwanted changes (tests with diffs show up as failed statuses before they are approved) and highlights intended changes once the diff has been approved. When we set out to create new components, often it's designers, not developers who are approving baseline updates-making sure that the components they drafted in Sketch are actually represented faithfully in the frontend implementation.

Separate components within a website (picture Facebook for example, with shortcuts on the left, the newsfeed in the middle and ads on the right) can be developed in isolation then combined. This separation allows you to ensure that changes made in one component of the site don't affect all of the other components. Each of these components usually has one or more visual "stories" attached, so if, for example, you changed the colour of a button on the page from red to green, then only the button "story" which would change is its color, not the logo story or the header story.

From a developer's point of view, it can sometimes be very difficult to understand the side-effects of your code changes, particularly with user interface changes and complex code. A developer may think that a change they've made is really small and contained, but then when the regression test is run, it can show a knock-on effect on a whole bunch of other components that you didn't expect to be affected. The ability to develop components in isolation gives developers added certainty that their changes are contained to just the parts that they want to effect. I remember one time where some CSS for a lightbox/dialog was introduced that conditionally added a margin to the surrounding element. Whilst this was anticipated in the context where it was introduced, the newly introduced code didn't take all scenarios into account where the dialog was used and also didn't clean up after itself when destroyed. Unfortunately the code was merged into the mainline nonetheless, and for reasons I don't remember not all tests had been run. A few hours later people started seeing the diff clearly visible in hundreds of stories and we were able to track down the offending code before the change was ever shipped to our customers.

For reviewers, it's often much easier to look at changes in an automated visual regression test, rather than the person who made the changes having to verbalise the changes they made or explain them in an email or text message. This can also drastically reduce the review time.

Automated VRT also takes into account the slightly different views generated by different browsers. One of the most difficult aspects of web development, especially when it comes to smaller viewing formats such as mobile browsers, is that some design aspects are very difficult to standardize across different browsers. Most of our developers use Google Chrome, a handful use Firefox and maybe one or two Safari, but none of our developers are currently using Internet Explorer or Microsoft Edge. With VRT, you can run tests in two web browsers simultaneously, so we can pick up any anomalies between the developer's browser and another common browser on the spot.

## …and how widely it has been used

Percy has become part of our standard frontend developer workflow. We currently have around 600 different stories for UI components that we perform visual regression testing on and each app contains between one and ten different screens. All of these are also run in a second text direction and many in additional screen widths based on mobile breakpoints defined by our designers, bringing our snapshot count to well over a thousand. Definitely not something that is still possible to do manually in a reasonable timeframe!

For our apps, we typically use the first screen as a sanity check across browsers (we test visreg on these screens in Firefox and Chrome), then for some language specific pages, we use German to test how text length affects the UI. German is usually a good indicator of capacity, as German sentences are on average around 20% longer than any other language, and secondly, because individual words themselves can be much longer- (Donau­dampf­schiffahrts­elektrizitäten­haupt­betriebs­werk­bau­unter­beamten­gesellschaft is one rather extreme example of the way German chains nouns together, roughly translating to as "Association for Subordinate Officials of the Main Maintenance Building of the Danube Steam Shipping Electrical Services.")

Of course, it is highly unlikely that we would ever use this particular word, but you'd be surprised how many UI components fail on words like these in visual regression testing when unit tests and integration tests still pass.

![](https://www.canva.dev/_next/static/media/img-0--TM39zca0ItwHG_q.79c181f5.png)

Testing the introduction of a new button in German

We use Thai and Burmese to test text height (as they have a lot of characters with ascenders and descenders, so text is easily cut-off if developers use a fixed line-height), and Arabic as a proxy for all right-to-left languages. We also use English in both LTR and RTL as a proxy, because it is easy to reason about for engineers and provides good feedback:

![](https://www.canva.dev/_next/static/media/img-0-hKNpw7e_FU6CYWpu.03128907.png)

Testing right-to-left layouts

VRT tools such as Percy can test in right-to-left text direction as well as left-to-right, so for languages that read right to left, such as Arabic, the testing is carried out automatically. This means we can be confident that the reversed text direction will have the expected effect on component layout and text in an app.

### Making it scale

The following considerations are special additions that we have incorporated to help us scale VRT across Canva.

  * **Stable randomness:** The first thing we observed is that developers love to use randomly generated content for stories (we use a lorem ipsum text generator to emulate changing text lengths, word count, and so on). Keeping the randomness stable is vital, as otherwise developers are confronted with seemingly inexplicable changes. We added random seeding to our code when it is run in visual regression mode. It still generates random text and numbers, but predictably random, so the baseline can be compared safely to changes in a pull request.
  * **Make RTL a priority:** When we started out, we consciously decided that RTL (right to left) testing would be something that we want to actively keep up during normal development cycles, so we could avoid having a mountain of changes in front of us at the end. We even had "RTL Wednesdays" at one stage, where on a Wednesday our developers would put our app and UI components into RTL mode by default (whilst still enabling developers to opt out manually for the odd production blocking bug that needed to be fixed urgently). Whilst we had to discontinue RTL Wednesdays due to infrastructure changes, we kept RTL testing on Percy at all times, so when creating a new component or making changes to an existing component, our developers are immediately asked the question "how does this look for our right-to-left languages?" and they can get a visual representation of that on demand.
  * **Use all the graphs:** When we started approaching 1000 snapshots per build, we had to be smarter in terms of how we used our snapshot allowance, not only because using thousands of snapshots for each pull request build would easily push us over our snapshot limit, but also because reviewing this number of snapshots is such an onerous task. The turnaround time for a completed visual regression set on Percy is dependent on the number of snapshots compared, because all of them have to be rendered. Thankfully, our set-up for the frontend allows us to calculate a complete dependency graph across all resources, including images, fonts and CSS. We had used this during build time on CI to only kick off necessary builds already, so we were able to reuse that code to write a small addition around the Percy API that allows us to only generate snapshots for UI components that are affected by code changes in a pull request. For the vast majority of pull requests this works like a charm, keeping the number of snapshots small and the response time of Percy low.



## Key outcomes

Previously, we may have ended up delivering something to the end user that didn't look exactly as we wanted or intended it to, whereas with automated VRT, we now have the surety and security of not sending anything out that contains a visual error. We're informed by the automated testing any time something is broken and needs to be fixed prior to that going out to the customer, rather than being hostage to human error in testing.

Automated VRT also ensures that developers have a much easier time of identifying and accepting or rejecting changes to the baseline code. Previously we would have to wait until users came back to us and said "this is broken, can you fix it for us?", which is clearly less than ideal. Now we have the tools in place to prevent these incidents occurring in the first place.

![](https://www.canva.dev/_next/static/media/img-0-q9EzMhT3kK5RywAZ.88214c38.png)

_Tweaking the padding on a page_

Because our testing is now automated, it can also scale with our business. As we add more developers to our team, it can perform all the testing we require with little additional effort on our part, which is essential for the future viability of the tool and our organization as a whole.

## Domain-specific benefits of using VRT

A side benefit of using a platform like Percy, where adding additional regression tests has little cost in terms of developer time, is that whole new categories of tests may become feasible. The additional tests we have developed are somewhat domain-specific to Canva, but I assume that each organization has a loosely related set of tests where they could leverage VRT to make things easier.

Let me show you 4 examples:

![](https://www.canva.dev/_next/static/media/img-0-76f-m7GOxa41XrnT.81db2bc6.jpg)

![](https://www.canva.dev/_next/static/media/img-0-n-SBFIEol01uAf-0.5c16d111.png)

![](https://www.canva.dev/_next/static/media/img-0-1wI3QGg-IhMowv0t.1cb2166a.png)

The tests I am talking about are, at their core, mathematical problems (transformations, packing, dynamic alignment) and their conditions can be mathematically expressed. However the result of that math is quite abstract and hard to understand when written down. In Canva's case the solution to these mathematical problems can have an actual visual representation attached, something which can't easily be expressed as part of a unit test whilst at the same time being easily updatable.

Since adopting Percy we've started using VRT to detect regressions on these groups of problems (in the examples you can see a dynamic pie chart generation with labels, image rotation based on EXIF data in the browser, a dynamic endlessly scrolling masonry layout component and image clipping and filtering via paths and all permutations filters and clipping in between). We've noticed that VRT is not only much more manageable in terms of expressing fixtures for these tests and updating them, but also that detecting intended and accidental changes has become a lot easier ever since.

## Final thoughts

Visual regression testing has been a great asset to Canva in the last year and a half or so. It consistently delivers value to our designers and developers, especially our many new starters who may be unsure about how changes they make can affect the system as a whole.

Canva is a very visual product, which probably benefits more from VRT than most other companies, but even just considering our core UI components in Storybook, we're getting great value for money out of Percy. The cost of maintaining the integration with Percy is marginal and Percy's response time to incidents and their support is outstanding. It will definitely help us to scale the company successfully into the future and — as our CEO Melanie Perkins likes to put it — build the rest of the 99% of Canva that is yet to be built. The more surety we have in the end product we deliver to users, the more confident we can be in adding new features and bringing on the new developers that we need to take Canva to the next level.

So if you're standing at the crossroads deciding whether to go down the path of VRT, I would suggest finding answers to the following questions:

  * Do you often roll out new versions where you only find out months later, by accident, that the layout shifted or components are broken?
  * Do you only find out after a customer complains that some infrequently used page has a layout problem?
  * Do you have a lot of legacy code where CSS is deeply nested or mutated directly by Javascript?
  * Do you need confidence that changes look good in multiple screen sizes/ for multiple breakpoints? Are you migrating your stack from legacy to a new one and worried about introducing inconsistencies in your design whilst doing so?
  * Do you have tests that are very visual at their core and hard to express in standard unit tests?
  * Do you want to make sure that designers have a chance to be the gatekeepers of design changes by your engineering organization?
  * Are you currently developing and/or maintaining your custom visual regression tool suite?



If you can answer any of the questions above with a yes and you are not too concerned about throwing a bit of money at the problem to solve it, an automated VRT solution might be for you!

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.c69dca35.png)](https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/)

[Data AnalyticsMeasuring Commercial Impact at Scale at CanvaHow We Built Canva's IMPACT App with Streamlit in Snowflake](https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/)

[Jun Ye⁠(opens in a new tab or window)](https://www.linkedin.com/in/jun-ye-0798/)Jun 20, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.eeec7a21.png)](https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/)

[Quality AssuranceHow We Used Data to Optimize Our Quality Assistance ModelFrom firefighting chaos to problem solving zen.](https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/)

[Zi Yang Pang⁠(opens in a new tab or window)](https://www.linkedin.com/in/pangzy/)Aug 29, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.8b5eeae7.png)](https://www.canva.dev/blog/engineering/snowpipe-streaming/)

[snowflakeThe foundations of Canva’s continuous data platform with Snowpipe StreamingLeveraging Snowpipe Streaming to build a continuous data platform.](https://www.canva.dev/blog/engineering/snowpipe-streaming/)

[Jack Caperon⁠(opens in a new tab or window)](https://www.linkedin.com/in/jdcaperon/)Jan 6, 2025

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


