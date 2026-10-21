---
url: https://www.canva.dev/blog/engineering/testing-search-engine-optimization-scalably-without-breaking-a-sweat/
title: Testing Search Engine Optimization Scalably without Breaking a Sweat - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:28.598660+00:00
---

# Testing Search Engine Optimization Scalably without Breaking a Sweat - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/testing-search-engine-optimization-scalably-without-breaking-a-sweat/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Search Engine Optimization

# Testing Search Engine Optimization Scalably without Breaking a Sweat

Scaling pre-development, rollout, and post-production SEO testing at Canva.

![](https://www.canva.dev/_next/static/media/thumbnail.7caec38f.png)

* * *

  * 


[Siddharth Salunke⁠(opens in a new tab or window)](https://www.linkedin.com/in/siddharthsalunke/)Jun 20, 2022

* * *

Search Engine Optimization (SEO) helps a website rank better in search results on search engines.

SEO can also be considered as _a_ _set of best practices to ensure your web pages are positioned or ranked higher in organic search results_. Search is the best possible way for users to discover your web pages and it's completely free of charge. So having an excellent SEO strategy and ensuring there are no SEO regressions is quite critical.

SEO serves a very important function to Canva: getting Canva discovered and used for design by users around the globe. The magic of SEO is usually planned upfront and is done by a majority of people in an engineering team including content researchers, content writers, software developers, software testers, product managers, and many others. Each role is equally important.

In this post, we'll focus on the testing side of things when it comes to SEO, and how we approach SEO testing at Canva.

First, let us take a look at what _organic search_ is.

## What is organic search?

When you're interested in something and you search for it on the Internet, it's usually through a search engine such as Google, Bing, Baidu, Yahoo, and a few others. The returned search results can be categorized into 2 parts:

  * Ads
  * Organic



Ads can be useful in helping users navigate to your website and in generating more traffic. However, you need to pay for these Ads and the costs can grow significantly.

On the other hand, organic search results are completely free so you don't have to pay for them. These search results are based on the algorithms and ranking factors determined by the search engine. To satisfy the needs of the search engines and to ensure your web pages rank higher and are always consistently at the top, a LOT of effort needs to be put in, so there is a cost in terms of time and effort.

This is different to Paid marketing or Ads which belong to the SEM (Search Engine Marketing) territory.

A combination of ads and organic search is necessary for any web page to generate decent traffic as a lot of people do click on ads on mobile devices due to a lack of real estate but organic search results win in the longer run, as organic traffic increases and becomes more important.

## Why is SEO important to Canva?

Canva's overarching mission is to empower the world to design — where every person with access to the Internet is using Canva regularly to unlock their creativity and meet their design needs. We need to be at the top of our SEO game and help users satisfy their intent by showcasing solutions at Canva.

For example, if a user wants to design a business card (_intent_), the first option they see is our [business cards product page⁠(opens in a new tab or window)](https://www.canva.com/business-cards/) which will help them design their very own customized business card (_solution_) and eventually also help them print it (_additional solution_). The user being able to see our business cards product page as the first organic result is all the hard work of our SEO and Engineering teams and it helps Canva tremendously.

Organic results drive a lot of traffic to Canva and are the second-highest source of traffic. The main focus is usually on Google but can differ depending on the locale (e.g. Baidu in China).

## How we test for SEO at Canva

There are different methods to test for SEO at Canva but they can broadly be classified into 2 groups: **manual** and **automated**. Both methods help us in identifying SEO issues and preventing them in the future.

Since SEO's benefits can only be reaped in the long term, any SEO issues found can negatively impact rankings and have a greater negative impact on Canva's vision. The impact of SEO issues will not immediately be noticeable until it's too late.

## Manual SEO testing

SEO testing is as important as [functional testing⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Functional_testing). There isn't much of a visual aspect to it but it's very important for pages that want to be ranked higher for search results. Manual SEO testing is done at different stages in Canva.

### Quality Assurance (QA) Kickoffs

QA kickoffs are usually led by the QA engineers in collaboration with developers and sometimes product managers. As part of our QA kickoffs, we iron out scenarios that might affect SEO negatively. If the feature that's being developed changes the URL of our pages, we think about how we can prevent potential issues such as pages not being indexed or canonical URLs not being self-referenced. If the feature that's being developed introduces new assets on the page, we think about how we can prevent regressions to our CVW (Core Web Vital) metrics such as LCP (Largest Contentful Paint), FID (First Input Delay), CLS (Cumulative Layout Shift).

Thinking about these issues even before development begins gives us the edge when it comes to SEO testing. We can plan and prevent SEO blockers from the start.

### Developer testing

Developers are more confident testing their code in terms of functionality as well as SEO by using the testing notes from QA kickoffs. Manual SEO testing is done by the developers themselves when functionally testing a feature at Canva. Any issues that arise when testing locally are fixed immediately.

### Exploratory testing

QAs regularly do exploratory testing at Canva to ensure we have a quality product in the market. SEO testing is something that's considered by QAs while doing exploratory testing (usually if the pages that they are testing are optimized).

As a user, you can access Canva logged in (authenticated) or out (anonymous). Some teams work on features that are only accessible to logged-in users and hence SEO testing is out of scope for such teams. However, SEO testing is a top priority for teams that manage logged-out pages which are usually optimized.

Things that we test when doing exploratory SEO testing are

#### Disabling JavaScript (JS)

  * It is important to check how a page renders without JS as this is what search engine crawlers would see
  * Ensuring all the content on the page is still visible with JS disabled is one of the checks performed during exploratory SEO testing
  * Nowadays, modern crawlers can render the page with JS, however the downside of that is that it consumes more crawl budget and is not ideal



#### Canonicals

  * Canonicals play an important role in SEO as they help search engines determine the primary page to rank if multiple versions of a page exist
  * When performing exploratory SEO testing, it is important to ensure that canonicals are _present_ and _self-referencing_.
  * For dynamic URLs (user-generated pages with URL parameters e.g. `?query=` for search generated pages), these are usually canonicalized or have canonical tags pointing to their primary page

![](https://www.canva.dev/_next/static/media/img-0-soauZ4a3ldYW5b9n.46552716.png)

Canonical tag for one of our top performing SEO pages [https://www.canva.com/templates](https://www.canva.com/templates)

#### robots.txt

  * `robots.txt` is perhaps the most important file when it comes to SEO testing as it directs search engine crawlers to accessible pages (pages that should be crawled) of your website and tells crawlers which pages are not accessible (pages that should not be crawled)
  * During exploratory testing, we usually ensure that the right pages are allowed or disallowed for bot crawling in the `robots.txt` file



#### hreflang

  * As Canva is available in 100+ languages, testing for localisation and `hreflang` rules is very important. `hreflang`attributes help search engines determine the relationship between web pages in alternate languages.
  * As part of our testing, we ensure that `hreflang` attributes:
  * are present
  * are pointing to all supported locales for that page
  * for the main page always have `hreflang="x-default"`

![](https://www.canva.dev/_next/static/media/img-0-elwzPeNcb4umXKYM.104a5325.png)

`hreflang` attributes for one of our top performing SEO pages — [https://www.canva.com/templates](https://www.canva.com/templates)

#### Lighthouse

  * [Lighthouse⁠(opens in a new tab or window)](https://github.com/GoogleChrome/lighthouse) is an open-source tool from Google that helps you quickly uncover performance and SEO issues
  * We use Lighthouse to quickly determine if basic SEO checks pass, and usually expect the score to be 100. Admittedly a perfect score is hard to achieve and not always necessary as there could be diminishing returns once Core Web Vitals and performance scores go high enough.

![Example lighthouse report for one of our top performing SEO pages. An example issue is mentioned. A number 100 appears in the center of the image, showing a perfect score.](https://www.canva.dev/_next/static/media/img-0-NOVDQ04hSqt2Wi7J.ead99f4a.png)

Example lighthouse report for one of our top performing SEO pages — [https://www.canva.com/templates](https://www.canva.com/templates)

### Test Parties

At Canva, we usually have test parties before making a feature available to end users. Test parties are a great way for the team to come together and test a feature thoroughly in an effective time-based manner. Manual SEO testing is also considered when running test parties. The different types of exploratory testing mentioned in the section above are also usually conducted during the test party

![Example Test Party agenda before launching a localized product page. Some heading includes Localised content, Navigation, SEO manual tests, Language selector, Exploratory tests and All pages return a 200](https://www.canva.dev/_next/static/media/img-0-hF5klJWDopfHcWoy.0fecb36e.png)

_Example Test Party agenda before launching a localized product page_

### Post launch

We have monitoring in place to help us determine if the feature we've launched has had negative implications for SEO. Dashboards alert us if there's a drop in traffic or if unrelated pages are being ranked on Google.

The SEO dashboards also help us determine who's crawling our web pages including Google and other crawlers.

![Example dashboard to visualize Google crawlers by device](https://www.canva.dev/_next/static/media/img-0-D59J7NrIPTeY0LvT.9bfc0105.png)

_Example dashboard to visualize Google crawlers by device_

![Example dashboard to visualize top 10 crawlers except for Google](https://www.canva.dev/_next/static/media/img-0-War4tnLthGWcZDKg.dbdda1cc.png)

_Example dashboard to visualize top 10 crawlers except for Google_

## Automated SEO testing

Apart from Manual SEO testing, we have automated tests for SEO. We use different tools such as [Deepcrawl⁠(opens in a new tab or window)](https://www.deepcrawl.com/) and [Datadog⁠(opens in a new tab or window)](https://www.datadoghq.com/) to help us test for SEO in an automated fashion and alert us if something goes wrong. We review tooling to remain consistent. We are proactive with the changing requirements of our SEO strategies and testing roadmaps. Note that we're not affiliated with any of the tools mentioned below — they're just good software that helps us get the job done in an efficient way.

## Deepcrawl

We've been using Deepcrawl for the past 2 years. Not only does it allow us to run automated SEO tests but they also provide technical expertise every month as well as run frequent webinars. We generally use 2 tools from Deepcrawl:

### Automation Hub (formerly known as Automator)

Automation Hub is Deepcrawl's tool that can be integrated into CI pipelines. Using this tool, you can set up a test suite and configure it to run heaps of tests with different thresholds to catch SEO issues on your web pages. During the configuration of a test suite, you can decide the starting URL, the type of crawl (list or web), crawl settings, tests, alerts, and CI connection settings.

![Example URL settings for one of our test suites](https://www.canva.dev/_next/static/media/img-0-DLg60an80Q2SO9YU.652d0bdf.png)

_Example URL settings for one of our test suites_

![](https://www.canva.dev/_next/static/media/img-0-mCAlSR1HdQFp2XXh.5ff8ac53.png)

_Example tests for one of our test suites with multiple tests and their thresholds_

We've configured multiple test suites to cater to different parts of the product and their test thresholds differ based on the requirements. These test suites are triggered throughout the day based on our release cycle as well as our daily schedule.

We've adopted an approach at Canva that allows us to run daily smoke and regressions SEO tests. After every release, we trigger a set of smoke test suites that run SEO tests against a small set of SEO-optimized pages. If a test fails, we instantly get notified on Slack and the issue is then investigated and triaged by the development team.

Aside from the post-release smoke tests, we also have a set of daily regression tests that are executed regularly. These tests are full-blown and test almost every SEO-optimized page at Canva. The alerting mechanism is the same as above for these tests.

These tests help us identify SEO issues such as

  * 3xx
  * 4xx
  * 5xx
  * Canonicals not present
  * Canonicals pointing to non-200s
  * Canonicals are not self-referencing
  * Broken links
  * Broken redirects
  * Duplicate pages
  * Empty pages
  * Missing titles
  * Unsupported `hreflang`links



Our teams work hard to fix these issues instantly if they are critical. Some are fixed over time and the test thresholds are updated accordingly.

![](https://www.canva.dev/_next/static/media/img-0-Wp37DpVj_6fo4wgH.683fb9e3.png)

_A whiteboard representation of our Automation Hub process_

### Analytics Hub (formerly known as Deepcrawl Core)

Analytics Hub is Deepcrawl's main product which is a comprehensive cloud-based crawler as well as a monitoring and reporting tool. We use it to run ad-hoc full-blown crawls, analyze reports and observe the trends and patterns of issues occurring over time.

![](https://www.canva.dev/_next/static/media/img-0-bJJgUscXr_rnGQ7o.6b514e46.png)

_An example dashboard of Analytics Hub that shows us everything about a crawl at a glance_

From the dashboard above, we can dive deeper into the Non-200 Pages report and identify exactly what's causing 49 URLs to return a non-200 status code. The reports are quite powerful and provide loads of sorting and filtering functionalities.

![](https://www.canva.dev/_next/static/media/img-0-WCyX1spg9-954T3c.a7ca0c2b.png)

From the report above, we can see that all 49 URLs returned a 500 status code. This usually happens when we are not able to serve the page to crawlers. End users usually aren't affected by this.

![](https://www.canva.dev/_next/static/media/img-0-Tq183IyXE_3Df47H.f23714cc.png)

Each failing URL can be analyzed further to investigate what the issue is by checking the response headers and other useful information.

Using the combination of Automation and Analytics Hub from Deepcrawl helps us sleep peacefully at night knowing that no SEO issues get past us.

### Datadog Synthetics

We also use [Datadog Synthetic⁠(opens in a new tab or window)](https://docs.datadoghq.com/synthetics/) tests or in order words Synthetic Monitoring from Datadog for automated SEO testing. This allows us to ensure our top-performing SEO pages are always up in all parts of the world.

![](https://www.canva.dev/_next/static/media/img-0-Gxe7mXvjAa9tLlNa.5f30349c.png)

_An example batch of tests from 7 different locations every 5 minutes_

These synthetic tests help us quickly identify if any of our top performing pages go down so that we can get them fixed as soon as possible, and back online.

### In-house tools and tests

Apart from the above-mentioned tools, we also have a few in-house test frameworks and tools that help us test for SEO changes directly or indirectly. There are some test frameworks and tools that help check the performance of our pages in relation to Google's CWV metrics while some other test frameworks that help validate if a page is SSRed ([server side rendered⁠(opens in a new tab or window)](https://www.gatsbyjs.com/docs/glossary/server-side-rendering)) properly.

## Conclusion

SEO is a long-term game and its effects aren't always immediately apparent. It's best to keep on top of any issues you find to prevent them in the future. An issue happening today may hamper your SEO journey tomorrow.

With the right balance of manual and automated SEO testing, we strive to set a high bar of quality for SEO at Canva.

SEO testing is an innovative space, and there's a lot of potential for more improvements. As our founders often say, we've only achieved 1% of what we know is possible!

### Acknowledgements

Kudos to all the people in the Marketplace and SEO groups for always encouraging me to try different things to solve challenging problems. Special thanks to

  * [Jake⁠(opens in a new tab or window)](https://www.linkedin.com/in/jakeyjunkie/) and [Kollins⁠(opens in a new tab or window)](https://www.linkedin.com/in/kollins-guerzon-003aab9a/): for always staying on top of all the SEO issues caught by our frameworks,
  * [Nikola⁠(opens in a new tab or window)](https://www.linkedin.com/in/n-yurukov/), [Sasha⁠(opens in a new tab or window)](https://www.linkedin.com/in/sashagusain/), [Belen⁠(opens in a new tab or window)](https://www.linkedin.com/in/belenfernandez/), and [Linda⁠(opens in a new tab or window)](https://www.linkedin.com/in/lindazhangsyd/): for sharing their experiences, insights, and feedback when it comes to SEO, and
  * [Mark⁠(opens in a new tab or window)](https://www.linkedin.com/in/markhrynczak/) and [Hansel⁠(opens in a new tab or window)](https://www.linkedin.com/in/hansel-paul-mationg-09580073/): for constantly providing guidance and constructive feedback



Massive shoutout to [Chris Hew⁠(opens in a new tab or window)](https://www.linkedin.com/in/christopherhew1/) and [Paul Tune⁠(opens in a new tab or window)](https://www.linkedin.com/in/paul-tune-0ba18116/) for suggestions in improving this post.

_Interested in applying for a QA role?_ [_Apply here!_ ⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/)

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.bc11c251.png)](https://www.canva.dev/blog/engineering/end-to-end-tracing/)

[Distributed TracingEnd-to-end TracingHow Canva implemented end-to-end tracing and are using it to drive operational insights](https://www.canva.dev/blog/engineering/end-to-end-tracing/)

[Ian Slesser⁠(opens in a new tab or window)](https://www.linkedin.com/in/ivslesser/)Jun 14, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.c7e450c5.png)](https://www.canva.dev/blog/engineering/the-science-of-routing-print-orders/)

[BackendThe science of routing print ordersHow Canva uses graph traversal to handle the complexity of getting print orders to our customers.](https://www.canva.dev/blog/engineering/the-science-of-routing-print-orders/)

[Constantinos Kavadias⁠(opens in a new tab or window)](https://www.linkedin.com/in/ckavadias/), [Carmen Wang⁠(opens in a new tab or window)](https://www.linkedin.com/in/carmenwang0/), [Callum Grier⁠(opens in a new tab or window)](https://www.linkedin.com/in/calgrier/)Dec 10, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.e14164be.png)](https://www.canva.dev/blog/engineering/how-to-design-in-every-language-at-once/)

[LocalizationHow to design in every language at onceThe technology that powers Continuous Localization at Canva.](https://www.canva.dev/blog/engineering/how-to-design-in-every-language-at-once/)

[Minh Cung⁠(opens in a new tab or window)](https://www.linkedin.com/in/minhcung/), [Simon Hammond⁠(opens in a new tab or window)](https://www.linkedin.com/in/simon-hammond-990250209/)Oct 20, 2021

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


