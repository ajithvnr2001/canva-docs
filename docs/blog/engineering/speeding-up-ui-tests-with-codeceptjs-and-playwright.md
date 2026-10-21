---
url: https://www.canva.dev/blog/engineering/speeding-up-ui-tests-with-codeceptjs-and-playwright/
title: Speeding up UI tests with CodeceptJS and Playwright - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:17.260790+00:00
---

# Speeding up UI tests with CodeceptJS and Playwright - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/speeding-up-ui-tests-with-codeceptjs-and-playwright/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

UI Testing

# Speeding up UI tests with CodeceptJS and Playwright

Lessons learned from migrating 1000+ browser-functional tests from Chimp, WebdriverIO, and Saucelabs to CodeceptJS and Playwright.

![](https://www.canva.dev/_next/static/media/thumbnail.68c525c0.png)

* * *

  *   * 


[Benjamin Sejas⁠(opens in a new tab or window)](https://www.linkedin.com/in/benjamin-sejas-49586632/), [Srini Ramasamy⁠(opens in a new tab or window)](https://www.linkedin.com/in/srini-ramasamy/)Mar 3, 2022

* * *

At Canva, we empower the world to design by providing a powerful and intuitive user interface that anyone can use. However, with 75 million people using Canva each month and more than 350 frontend engineers making 160+ changes per day, we must keep our frontend working as expected.

One way we ensure stability is by writing browser-functional tests that mimic how a user interacts with Canva. These functional tests are run for every change and must pass in our continuous integration (CI) pipelines before the changes are accepted into the Canva codebase.

In this blog post, we'll recount our Test Platform team's experience migrating browser-functional tests from Chimp, WebdriverIO, and Saucelabs to CodeceptJS and Playwright. We'll share our journey, the challenges we encountered, how we resolved them, and the lessons we learned.

## Problems with our original framework

In 2017, we began rebuilding Canva's frontend architecture so that development could scale to handle 1000s of engineers working together. We decided to use a testing framework called [Chimp 1.0⁠(opens in a new tab or window)](https://github.com/TheBrainFamily/chimpy) to write frontend functional tests using Cucumber, Webdriverio, and Typescript. Chimp 1.0 had some features that our team liked, such as watch mode, which enabled tests to run automatically when we made a local change.

![](https://www.canva.dev/_next/static/media/img-0-YT-tCeXM2Fw-zfgi.02fa956e.png)

Example of functional tests written in Cucumber

While Chimp worked for us for several years, Chimp fell behind on updates and fixes for Cucumber and Webdriverio. The old Cucumber version had performance issues and processed all support files, even if you only wanted to run one test. As the number of tests grew from 100 to 1000, the test start-up time went from seconds to several minutes. We explored upgrading to the latest Cucumber and Webdriverio versions. However, we couldn't make the newer Webdriverio version scale in our extensive Typescript codebase because of the [retranspilation speed⁠(opens in a new tab or window)](https://github.com/webdriverio/webdriverio/issues/4949) (this has since been [fixed⁠(opens in a new tab or window)](https://github.com/webdriverio/webdriverio/pull/6548)). We were also on a fork of the project because of fixes needed for Chimp's Saucelabs support.

Our existing framework setup quickly gained negative sentiment amongst engineers. It reduced productivity and lowered quality because engineers were deferring writing tests because of its slowness. It was time to address this problem.

## What did we do?

Because upgrading the internal components didn't work out, we switched to a whole new framework.

The new framework needed to:

  * Support Typescript so that it was consistent with our frontend codebase.
  * Have active development accepting external contributions so that it's less likely to become outdated.
  * Support our existing test setup (Cucumber) while we migrated to the new framework.
  * Support using drivers and libraries such as Playwright for web tests and Appium for web and mobile tests.
  * Support testing on multiple browsers and devices, including using cloud-based browser testing services such as Saucelabs, Browerstack, or LambdaTest.
  * Support headless browsers such as those provided by Playwright.



[CodeceptJS⁠(opens in a new tab or window)](https://github.com/codeceptjs/CodeceptJS) fulfilled all our requirements and has good documentation and a great community.

## A detailed look at our journey

We started our journey a year ago by planning out what the migration journey would look like. We had to customize our new framework so that it worked seamlessly with existing tests and to abstract away most of the complexities so that it supported running tests on both frameworks. We spent a good amount of time tailoring the framework set up and then updating the tests to work with the new framework.

## How we set up our new framework

### Chimp-like API (with pseudo-locators)

One of the guiding principles of the migration was keeping code changes to a minimum. We first decided to create a wrapper around the CodeceptJS API that resembled the Chimp API to support both test frameworks. This would allow us to inject the correct framework during runtime, depending on which framework we wanted to run.

Trying to get CodeceptJS to behave like Chimp proved harder than anticipated. There were fundamental differences in some APIs, and often there wasn't a matching API available in CodeceptJS. One example was how CodeceptJS used selectors.

WebdriverIO allowed the use of multiple selector strategies which involved chaining find element commands such as `browser.$('.editor').$('.canvas').$('.element')`. However, CodeceptJS only supported [one level of chaining⁠(opens in a new tab or window)](https://codecept.io/playwright/#within), which didn't satisfy our needs. To work around this, we introduced a pseudo-element object when using the find element command that internally kept track of the selectors. When actions were triggered, we would join the underlying selectors in the pseudo-element into one selector, such as `browser.$('.editor .canvas .element')`.

### Supporting sync and async APIs with codemods

The largest issue we faced was that the Chimp API was synchronous while the CodeceptJS API was asynchronous. Chimp used [Fibers⁠(opens in a new tab or window)](https://github.com/laverdet/node-fibers) to make asynchronous actions synchronous but Fibers' authors [announced⁠(opens in a new tab or window)](https://github.com/laverdet/node-fibers/commit/e2a0ed9c6d985f94c2b1947eaf72d5797e8a3278) they would no longer maintain this feature. All the other major test frameworks used asynchronous APIs too. So regardless of which framework we chose, we needed to change our tests to use asynchronous interactions.

![](https://www.canva.dev/_next/static/media/img-1-CGwdMRJpExjaEkOpok9hXg.5729e1b5.png)

Chimp API was synchronous while the CodeceptJS API was asynchronous

Supporting both frameworks meant making our existing framework continue working while we started adding `async`s and `await`s to the codebase. Unfortunately, adding `async`s and `await`s caused the Cucumber steps in the old Cucumber version to run out of order, and there was no fix for it.

We then explored the possibility of using codemods at compile time to add `async`s and `await`s. Using codemods was our preferred option because it meant we didn't have to update our test code, but it proved too difficult to apply the correct transformation for all scenarios to work. Array functions, such as `forEach` or `filter`, are examples that require complex transformations. These functions don't work with `async`s and `await`s, and changing them from a function into a for-loop is not a straightforward transformation in most cases.

Instead, we did the opposite and wrote a codemod to remove `async`s and `await`s to work for our existing framework. These codemods worked well but had some minor downsides, such as slightly skewed stack traces and slightly slower execution times, but were manageable.

This still meant we needed to add `async`s and `await`s to all our tests. We'll talk about this challenge later in this post.

### Watch mode

CodeceptJS doesn't provide watch mode out-of-the-box but this was a necessity for us. Almost all our engineers rely on watch mode to develop frontend tests as it provides a faster and seamless developer experience. So we used [ts-node-dev⁠(opens in a new tab or window)](https://github.com/wclr/ts-node-dev) to watch for any code changes and programmatically invoke our tests if any changes are made.

### Supporting co-existing type declarations for both frameworks

Supporting two frameworks also caused clashes in Typescript typings. In our tests, we used a `browser` object to access the Chimp API and the CodeceptJS API, but only one of these APIs was available at a time. So we created a script to switch between the typing declarations whenever an engineer needed it. Enabling typing was important because it allowed engineers to access autocomplete that helped migrate missing API implementations and tests. In addition, this would help engineers become familiar with the new framework.

### Improving Safari test runs

Playwright allows Webkit testing without the need for cloud-based cross-browser testing services. Using Playwright in our CI pipelines halved our CI Webkit test run times and increased our test coverage by 30%. We encountered many unique challenges configuring our CI agents to work with Playwright that we'll cover separately in a future blog post.

## How we migrated our existing tests

### Running both frameworks in CI

During the initial months of the migration, we ran all tests using the old and new test frameworks in parallel in CI to compare the test runs and catch any unforeseen problems. After we migrated enough tests and we had confidence with the builds, we started running migrated tests only in the new framework.

### Migrating the actual test code

As mentioned previously, we needed to add `async`s and `await`s to all the tests. Making a function asynchronous also meant any calling functions needed to become asynchronous. In the example below, adding an await to `this.element.isExisting()` in `Button.getLabel()` meant we also needed to add async and await in the step definition function that was calling it. We had many occurrences in our codebase ranging between two and five levels deep, and they all had to be updated.
    
    
    // Chimp
    
    
    
    
    getLabel() {
    
     const hasLabel = this.element.isExisting(styles.label);
    
     …
    
    }
    
    
    
    
    // CodeceptJS
    
    
    
    
    async getLabel() {
    
     const hasLabel = await this.element.isExisting(styles.label);
    
     …
    
    }
    
    
    
    
    // Chimp
    
    
    
    
    Then(/^the button label is "([^"]*)"$/, function(this: Scope, label: string) {
    
     expect(this.button.getLabel()).toBe(label);
    
    });
    
    
    
    
    // CodeceptJS
    
    
    
    
    Then(/^the button label is "([^"]*)"$/, async function(this: Scope, label: string) {
    
     expect(await this.button.getLabel()).toBe(label);
    
    });

JS

Copy

While the change was straightforward, changing thousands of lines would be time-consuming.

### Automating the code transformation

We took inspiration from our initial attempts using codemods to add `async`s and `await`s during compile-time and created two scripts: one to add awaits and another to circle back and add `async`s.

To add `await`s, we customized the eslint [no-floating-promise⁠(opens in a new tab or window)](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/eslint-plugin/docs/rules/no-floating-promises.md) rule to find asynchronous functions that were not awaited and wrote a fix function specific to our scenarios that would safely add awaits.

To add `async`s, we used [ts-morph⁠(opens in a new tab or window)](https://github.com/dsherret/ts-morph), a Typescript AST, to transform function expressions and arrow functions to asynchronous functions if they contained the keyword `await`.

We ran the scripts alternatively until all the `async`s and `await`s were added. It wasn't the most elegant solution and needed some manual tweaking, but it saved a lot of time.

### We finally made it!

Even though we aimed to automate the migration as much as possible, we knew we couldn't migrate all the tests within the Test Platform team. So we reached out to other teams through alignment requests and worked with each team's QA representative to keep teams accountable. Reaching out to other teams worked well, but the nature of alignment requests meant migration took months longer than expected because teams needed to plan the migration into their roadmap. The last test was migrated in mid-August, eight months after the migration started.

![](https://www.canva.dev/_next/static/media/img-0-8uDQEMIilZ4mxlPW.aec2da35.png)

Last 4 months of migrating test to CodeceptJS

### And we went further by reducing start-up times

When working with Cucumber, you must provide a configuration file detailing where to find feature files and their respective step definitions files. The default values `**/*.feature` and `**/steps.ts` would work quickly for most cases, but we had accumulated over 400 feature files and 600 step definitions files. For a developer running one scenario, it would take at minimum 90 seconds in Chimp and 45 seconds in CodeceptJS to start a test run on top-end Mac laptops. It was a painful experience waiting between changes.

To reduce the start-up wait times, we programmatically generated the Cucumber configuration file to contain only the feature files and steps definition files required for the test. First, we used the [Gherkin AST⁠(opens in a new tab or window)](https://github.com/cucumber/gherkin) to read the feature file steps that we wanted to run. Second, we used [ts-morph⁠(opens in a new tab or window)](https://github.com/dsherret/ts-morph) to extract all step regexes from step definitions files and matched the regexes with the feature file steps mentioned previously. Using this method reduced the start-up time to between 6 and 10 seconds. This was a significant reduction in wait times for local execution, but we also saw faster executions in CI builds.

![](https://www.canva.dev/_next/static/media/img-0-Qo203QnaNqgSlFlW.bbc45781.png)

Login test runs were reduced by 50% in CI

Additionally, we introduced a cache mechanism that would search the step definitions used from the previous run before searching all the step definitions. Using this cache meant searching only about 20 step definition files instead of 600. In most cases, a developer would want to run the same test multiple times, which worked great and reduced the start-up time to between 2 and 4 seconds.

## Lessons learned

### Keep your tooling updated

Setting aside time and resources to keep your tooling updated prevents large and complex updates in the future. While some brave engineers attempted to solve the problem as a side project, it ultimately needed more hands and dedicated time. _Special shout out to_ [_Gustavo Henke_ ⁠(opens in a new tab or window)](https://www.linkedin.com/in/gustavohenke/)_ ,_ [_George Crabtree_ ⁠(opens in a new tab or window)](https://www.linkedin.com/in/supercrabtree/) _and_ [_Joscha Feth_ ⁠(opens in a new tab or window)](https://www.linkedin.com/in/joschafeth/)_._

### Align with teams early and have a dedicated point of contact

When introducing outside work to teams, be mindful that each team handles new work differently, and this means allowing teams generous time to complete work. In our situation, we saw some teams migrating all their tests at once over several days while others slowly migrated their tests over several weeks. It's important to have a dedicated team contact who understands their team's context, can communicate any changes, and keep their team accountable.

### Visualizing progress

During the migration we collected data on the number of tests remaining to be migrated and we created dashboards to visualise our progress. The dashboards were incredibly helpful when communicating with teams and understanding when teams needed assistance. We found that many teams were motivated by seeing their progress and would celebrate when they finished migrating their tests.

## Acknowledgements

Kudos to the members of the Test Platform team — [Srini Ramasamy⁠(opens in a new tab or window)](https://www.linkedin.com/in/srini-ramasamy/), [Benjamin Sejas⁠(opens in a new tab or window)](https://www.linkedin.com/in/benjamin-sejas-49586632/), [Ray Ru⁠(opens in a new tab or window)](https://www.linkedin.com/in/ray-r-090303146/), [Henry Pan⁠(opens in a new tab or window)](https://www.linkedin.com/in/henrypan1231/), [Klym Malakhov⁠(opens in a new tab or window)](https://www.linkedin.com/in/klyment-malakhov/) and [Niko Georgievskiy⁠(opens in a new tab or window)](https://www.linkedin.com/in/ngeorgievskiy/) — who worked on building the infrastructure to migrate to CodeceptJS. Special thanks to [Joscha Feth⁠(opens in a new tab or window)](https://www.linkedin.com/in/joschafeth/), [Gustavo Henke⁠(opens in a new tab or window)](https://www.linkedin.com/in/gustavohenke/) and [George Crabtree⁠(opens in a new tab or window)](https://www.linkedin.com/in/supercrabtree/) for their early efforts in migrating our test framework. Thank you to all the QAs for working with your teams to finish off the migration.

_Interested in UI testing infrastructure?_ [Join Us!⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/)

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.7349e802.png)](https://www.canva.dev/blog/engineering/search-pipeline-part-i/)

[Search and RelevanceSearch Pipeline: Part IHow we are rebuilding Canva's search stack and pipeline.](https://www.canva.dev/blog/engineering/search-pipeline-part-i/)

[Stuart Cam⁠(opens in a new tab or window)](https://www.linkedin.com/in/codebrain/)Nov 2, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.bf282bb2.jpg)](https://www.canva.dev/blog/engineering/scaling-to-count-billions/)

[BackendScaling to Count BillionsHow we built a scalable and reliable content usage counting service.](https://www.canva.dev/blog/engineering/scaling-to-count-billions/)

[Sangzhuoyang Yu⁠(opens in a new tab or window)](https://au.linkedin.com/in/yuszy)Apr 12, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.c165186b.png)](https://www.canva.dev/blog/engineering/canvas-compute-backend/)

[PerformanceCanva's compute backendDeveloping the Compute Service, aimed at the increasing processing burden of password hashing and the signing of private CDN URLs.](https://www.canva.dev/blog/engineering/canvas-compute-backend/)

[Sam Killin⁠(opens in a new tab or window)](https://au.linkedin.com/in/samuelkillin)Sep 15, 2015

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


