---
url: https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/
title: How We Used Data to Optimize Our Quality Assistance Model - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:15.076780+00:00
---

# How We Used Data to Optimize Our Quality Assistance Model - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Quality Assurance

# How We Used Data to Optimize Our Quality Assistance Model

From firefighting chaos to problem solving zen.

![](https://www.canva.dev/_next/static/media/thumbnail.eeec7a21.png)

* * *

  * 


[Zi Yang Pang⁠(opens in a new tab or window)](https://www.linkedin.com/in/pangzy/)Aug 29, 2022

* * *

At Canva, our quality assistance model aims to drive quality by shifting the process left. Shifting left means that Quality Assistance (QA) engineers assist every team member, from PMs, designers, developers, and data analysts, in thinking about risks and edge cases upfront so we can prevent errors early on instead of finding bugs after development is complete.

Yet we still run into the issue of what we should focus testing on when we have many projects trying to hit the same tight deadlines. This problem affects engineers and QA engineers as they might stretch themselves too thin trying to test everything when there's no prioritization based on usage.

We optimize our quality assistance model by making data-driven decisions whenever possible. Data-driven decisions allow us to focus on the most used features so that even if users encounter an error, it would be in an area that wouldn't be a showstopper for them. Let's face it: there's no software out there with zero bugs. What's important is how often your users encounter them and how critical they are.

## So how did we do it?

### Code coverage

Canva [code exists in a monorepo](https://www.canva.dev/blog/engineering/we-put-half-a-million-files-in-one-git-repository-heres-what-we-learned/) and an owner's file identifies who owns a certain area of the code. Using unit tests, we looked at the code coverage for the code we own as a team. This raised visibility on features with very little code coverage so that we could focus our efforts on areas with few automated tests.

For code coverage, we focus on unit tests because they give the most detailed coverage information compared to integration tests, which are much more difficult to assess.

Here are some of the common first reactions when we first presented this to the development team:

> "Oh, but I've written integration tests for that."

The most common answer you will get, and that's fine. The key here is to raise awareness on how many tests we have for the features we ship. Create a team dashboard to show which integration test covers which user scenarios.

> "Oh yeah, we kinda know about it, but we don't have time or space to work on it."

There's a risk the team is only working on new product features and don't have time to work on technical debt or engineering foundation work. This could lead to the team accruing a lot of technical debt over time and could hinder the engineering team from scaling more in the future. Things that work for one project might not work for other projects.

We then try to pick up at least one technical debt or engineering foundation work ticket from our backlog every sprint so that we don't add too much technical debt moving forward. You want to be paying off your technical debt faster than accruing it.

> "That component or feature is not easily testable."

Components might violate the [Single Responsibility Principle⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Single-responsibility_principle), where they do too many things, and you can't easily break them down because of the number of dependencies.

A common solution is to use dependency injection to decouple code as much as possible. Dependency injection is a technique where instead of instantiating the required resources in a class, the class accepts the required resources as parameters so that you can easily reconfigure and reuse the class. Dependency injection helps in testing different use cases and scenarios.

> "Code coverage itself isn't useful because we don't know what we are looking at."

And that's a fair call because those numbers don't really mean anything without context. So, how do we get around this?

### **Understand how users use our product**

As QAs, we need to be able to analyze how our users are using our products. A quality product doesn't only mean it's free of bugs. It also has to be easy for users to discover and use a new feature well.

When a user faces an annoyance in using a product, their first reaction is not to create a support ticket but to try and get around the issue. It's then important for us to be able to pick up moments like this to help reduce our users' friction points as much as possible.

For example, in Canva, you can invite someone to join your team from the homepage sidebar.

![An image of the sidebar of Canva, with a highlighted button on the bottom left with text "+ Invite members"](https://www.canva.dev/_next/static/media/img-0-O1HQJk53NdGZj307.3e63e970.png)

Alternatively, you can invite someone after you've published your shiny new design.

![An image showing the share dropdown, with the design being shared to "someone@test.canva.com", with message "Hey! Join my team and collaborate on this design"](https://www.canva.dev/_next/static/media/img-0-JjsTuJbZwzgrWrqC.0675b996.png)

By understanding how administrators prefer to invite people into their team, whether on desktop or mobile, from the homepage or after a design has been published, we can group these cohorts and sort them from highest to lowest frequency of use.

We can then use this information to help us focus our testing efforts on areas with the highest traffic area. It also helps us determine the severity and priority of bugs more accurately, which helps reduce alert fatigue when someone reports a bug. We can easily identify the number of users affected instead of treating every bug with the highest priority.

With these analyses, we can start working on writing better tests for areas that have the highest feature usage with the lowest code coverage. This helps us mitigate the risk of the component breaking in the future and affecting many users.

### Measure improvements and celebrate wins

It's easy to get swept up by what we could have done better, but celebrating our small wins is important too because they compound in the long run.

As a team, we agreed on a timeframe to tackle improvements on some key metrics we want to improve such as the number of engineering foundation issues, code coverage, and the number of tests.

We started with a very easy-to-achieve goal and regularly reported on those metric improvements. Then, when the team became more familiar with the process, we started expanding the scope to a bigger area of the code, targeting more features of the product, and so on.

Over time we started to see better test coverage, less code rework, and greater confidence in the team when releasing new features because they can build on a more solid engineering foundation. In the past three months, we saw zero incidents across three teams that I work with (and hope to keep it that way!).

## So what did we achieve and learn?

We were able to shift towards quality.

> "The dashboards created by Pang enabled the team to confidently prioritize our most important flows for the development of the Canva for Teams launch." — Salva, Product Manager

We learned that there's no magic number on the best code coverage you can achieve as a team. 100% unit test code coverage sounds good in an ideal world, but at a certain point, there are diminishing returns in trying to hit that number, and unit test coverage is not perfect. We supplement this with other QA activities, such as QA kickoffs, testing parties, and reviewing designs before engineering work starts.

With more accurate bug prioritization, there's less alert fatigue as a team. We can pragmatically approach a problem we find by first looking at how many users are impacted instead of diving head first into every single problem raised.

As a team, we've developed a better understanding of the current health of our code and now have an objective measure to work towards. Developers could start identifying technical debt that they can work on to improve their team's key metrics. Improvements are now quantifiable and driven by a bottom-up approach.

We've also managed to reduce risk regarding what the developers are shipping. We measure risk as the number of bugs we find in production and incident counts. Developers are less likely to be sidetracked and context switching because they're less likely to be fixing bugs we've shipped. This results in a better user experience because the chances of users being annoyed by a bug are lower.

Teams constantly balance investing time in engineering foundation work and shipping features. Having an objective measure that everyone understands allows the team to align on a goal to ship new features without sacrificing quality.

### Acknowledgements

Kudos to everyone in the Teams and Collaboration Growth for being so onboard with some of the ideas that I've put forward and putting them into practice. Couldn't have done this without them.

Special thanks to

  * [Hansel⁠(opens in a new tab or window)](https://www.linkedin.com/in/hansel-paul-mationg-09580073/), [Mark⁠(opens in a new tab or window)](https://www.linkedin.com/in/markhrynczak/) and [Sid⁠(opens in a new tab or window)](https://www.linkedin.com/in/siddharthsalunke/) for the encouragement to write and reviewing this post, making it better,
  * [Dee⁠(opens in a new tab or window)](https://www.linkedin.com/in/dee-pabst-05769887/) for proposing my ideas to his team and putting them into practice. Turning all those half-baked ideas into long term strategies,
  * [Fiona⁠(opens in a new tab or window)](https://www.linkedin.com/in/fionasmwong/) for reviewing my early data investigation work and [Salva⁠(opens in a new tab or window)](https://www.linkedin.com/in/torressalvador/) embracing the ideas for the Canva for Teams launch, and
  * Jackson and [Grant⁠(opens in a new tab or window)](https://www.linkedin.com/in/grant-noble-8253994a/) for making this blog post much better



_Interested in applying for a QA role?_ [_Apply here!_ ⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/)

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.b928bce2.png)](https://www.canva.dev/blog/engineering/when-url-parsers-disagree-cve-2023-38633/)

[SecurityWhen URL parsers disagree (CVE-2023-38633)Discovery and walkthrough of CVE-2023-38633 in librsvg, when two URL parser implementations (Rust and Glib) disagree on file scheme parsing leading to path traversal.](https://www.canva.dev/blog/engineering/when-url-parsers-disagree-cve-2023-38633/)

[Zac Sims⁠(opens in a new tab or window)](https://au.linkedin.com/in/zacsims)Sep 5, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.fd976c52.jpeg)](https://www.canva.dev/blog/engineering/5-visual-effects-canva-uses-to-thrill-users/)

[Visual Effects5 visual effects Canva uses to thrill usersThis article details five visual effects found in the Canva web application that exist to help achieve these goals of simplicity and fun.](https://www.canva.dev/blog/engineering/5-visual-effects-canva-uses-to-thrill-users/)

Chris DobleMay 16, 2016

[![](https://www.canva.dev/_next/static/media/thumbnail.bc11c251.png)](https://www.canva.dev/blog/engineering/end-to-end-tracing/)

[Distributed TracingEnd-to-end TracingHow Canva implemented end-to-end tracing and are using it to drive operational insights](https://www.canva.dev/blog/engineering/end-to-end-tracing/)

[Ian Slesser⁠(opens in a new tab or window)](https://www.linkedin.com/in/ivslesser/)Jun 14, 2023

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


