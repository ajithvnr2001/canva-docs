---
url: https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/
title: Measuring Commercial Impact at Scale at Canva - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:15.371502+00:00
---

# Measuring Commercial Impact at Scale at Canva - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Data Analytics

# Measuring Commercial Impact at Scale at Canva

How We Built Canva's IMPACT App with Streamlit in Snowflake

![](https://www.canva.dev/_next/static/media/thumbnail.c69dca35.png)

* * *

  * 


[Jun Ye⁠(opens in a new tab or window)](https://www.linkedin.com/in/jun-ye-0798/)Jun 20, 2025

* * *

## Executive Summary

At Canva, experimentation is at the core of how we build and grow. With over thousands of experiments run annually across diverse product surfaces, we needed a scalable, consistent, and trustworthy way to measure what truly drives business outcomes like Monthly Active Users (MAU) and Annual Recurring Revenue (ARR).

To solve this, we developed the IMPACT app — an internal tool built using [Snowflake⁠(opens in a new tab or window)](https://www.snowflake.com/en/product/features/streamlit-in-snowflake/), Streamlit, Snowpark, and Cortex. The app enables fast, self-serve estimation of commercial impact for both pre- and post-experiment analysis, using standardized logic aligned with our central finance model.

Key outcomes include:

  * Reducing time-to-insight from hours to minutes
  * Enabling consistent, auditable impact sizing across Canva
  * Making impact insights accessible to both technical and non-technical users
  * Supporting collaboration through a safe, PR-based development environment



More than a tool, IMPACT represents a shift in how we approach internal data products: scalable, testable, and productized for real-world decision-making.

## Why Measuring Commercial Impact Matters at Scale

At Canva, experimentation is core to how we build and innovate. We’ve already run over 1,800 experiments this year alone and that number keeps growing. These aren’t just A/B tests managed by a single team such as the landing page, they span across user growth, content discovery, design experience, education, international expansion, and of course, AI-powered features.

This scale of experimentation unlocks massive learning potential, but it also introduces significant complexity. With so many teams exploring different ideas and features in parallel, a natural challenge arises: **How do we ensure these experiments are truly meaningful at the company level and that we’re not wasting resources**?

It’s relatively straightforward to measure whether an experiment is statistically significant on its own north-star metrics, such as click-through rate, publishing a design, or collaborating with others. But that’s not enough on its own. What we really care about is whether that uplift flows through the full conversion funnel as shown below, from activation to monetization and ultimately moves the metrics that matter most to the business.

![Canva's business funnel](https://www.canva.dev/_next/static/media/conversion_funnel.208325d6.svg)

Canva's business funnel

As a SaaS company, our model is built on helping people get value from the product and then grow with it over time. Whether that means upgrading from free MAU to trial, trial to paid, reducing churn, retaining customers, or expanding into teams, each of these touch points represents a meaningful signal that the product is working. So we look at whether experiments move key metrics in this funnel and how that, in turn, drives outcomes like **Monthly Active Users** and **Annual Recurring Revenue**. These are foundational metrics for any SaaS business. Not just because they reflect financial performance, but because they indicate whether we’re actually delivering lasting value to our users at scale.

And that’s what we refer to as commercial impact. And our job, as the data team, became clear: **How do we quantify that business impact consistently for every single experiment?**

Most experiments only target specific parts of the product not the entire user base. That means we can’t just apply the observed uplift across all users when calculating company-level impact. For example, users might be segmented by product surface, platform, or geographic region and typically, only a subset of them is actually exposed to a given experiment.

![Product Surface](https://www.canva.dev/_next/static/media/product_exposure.efd1fff8.svg)

Users can interact with any Canva product surface

Imagine the grid (see above) represents our total user base. Now, different colored sections highlight users who are interacting with a specific Canva product surface, like Whiteboards, Presentations, Videos, or the Photo Editor. Assume we run an experiment on just the Presentation product surface. And we observe a 20% uplift in user growth for that group. It might be tempting to apply that 20% uplift to the entire user base and say, “Great, we boosted user growth by 20% overall.”

But that’s not accurate, because the experiment only affected a subset of users. Specifically, the ones who actually use Presentations. If, for example, only 10% of our total user base engages with Presentations, then that 20% uplift should only apply to this 10% slice. So when we scale it against to the full population, we’re looking at a 2% uplift at the company level, not 20%.

![Product Surface Example](https://www.canva.dev/_next/static/media/product_exposure_example.e5da0f1e.svg)

Uplift observed from local change need to be scaled properly.

This kind of scaling is essential when calculating funnel metrics. It ensures we don’t overestimate commercial impact, especially when comparing experiments that target very different parts of the product. That’s why scaling by exposure is a core part of how we estimate impact across the funnel.

## How is Commercial Impact Used at Canva

At Canva, we use commercial impact measurement in three main ways:

  1. Plan prioritization – Teams can stack-rank and compare different initiatives by expected impact. This helps align with broader company goals and ensures resources are allocated effectively.
  2. Post-experiment tracking – Once an experiment is live, we continue updating forecasts and re-evaluating whether we’re still on track to hit targets.
  3. Impact sizing – Understanding the magnitude of impact helps teams see what’s truly working and guides the design of even bigger, bolder product improvements.



In this way, commercial impact isn’t just a number. It’s a tool for strategy, decision-making, and growth at Canva.

## The Old Way Wasn’t Scalable

When you have hundreds of experiments running across the company at any given time and every team is calculating commercial impact slightly differently, things get messy fast.

Here’s what the old process looked like:

  1. It was manual. Even for someone familiar with the process, it could take 6+ hours to complete impact calculations for a single experiment. There were dozens of metrics to assess, and often requiring access to many different data models. It wasn’t realistic to expect data scientists across the business to use these models consistently or correctly.
  2. It relied on inconsistent spreadsheets. Each team had its own templates, naming conventions, and formulas. That made results hard to audit, reproduce, or share and increased the risk of errors or misinterpretation.
  3. Assumptions varied widely. Teams often made different assumptions about definitions, time windows, or metric logic and even small differences could lead to significantly different results. This made it nearly impossible to roll up impact or compare outcomes across teams.



## A Simple But Powerful Vision

Given all these challenges, it became clear that supporting decision-making at Canva’s scale required a consistent, automated, and trustworthy approach.

Our vision was simple but powerful:

**Any product manager, engineer, or data scientist at Canva should be able to view the commercial impact of an initiative tied directly to our central finance model with zero ambiguity.**

Whether it’s:

  * A live experiment running on our internal experimentation platform, or
  * A pre-experiment estimate based on hypothesized uplifts,



We wanted everything to be powered by a single source of truth using the same logic, same assumptions, and same metrics as those used by our finance team to forecast company performance. This vision is what took us from chaos to clarity.

## Introduction of the IMPACT app

How IMPACT app works in action.

The IMPACT app, short for **I** nitiative **M** easurement and **P** ersonalization **A** nalysis **C** omprehensive **T** oolkit was built to bring this vision to life.

With an intuitive UI powered by Streamlit, users can now estimate commercial impact through a low-code or no-code experience. All they need to do is enter or select experiment information, click “run,” and let the app handle the rest.

The app supports both post-experiment analysis and pre-experiment scenario modeling, tightly integrated with our central finance logic. Just as importantly, all results are automatically saved into the app’s own database, giving users a clean, accessible interface to explore, compare, and confidently act on impact insights without spreadsheets or manual calculations.

The IMPACT app has quickly become a core part of Canva’s workflow for measuring commercial impact.

To recap, it has helped us:

  * Standardize ARR and MAU impact estimation across the company
  * Reduce analysis time from hours to under 10 minutes per experiment
  * Automatically store results in the warehouse for easy downstream access and integration



## Under the hood

![High-level Design](https://www.canva.dev/_next/static/media/high_level_design.bc66d17a.svg)

A overview of high-level design.

Here is the high-level overview of the app architecture. We designed it to be modular, maintainable, and fully integrated within the Snowflake ecosystem. The application brings together a few key components:

  * A Streamlit object that handles user interaction, business logic, and impact estimation
  * IMPACT app's own database.
  * Multiple other Snowflake databases where the production, experimentation, and finance data live and the app can access
  * A Snowpark layer that schedules and maintains input tables for MAU and ARR logic.
  * Integrations with LLM models via Cortex for summarising insights via natural language



All of this is powered by the Snowflake Python connector to make sure the entire pipeline stays secure, and consistent with our data governance standards.

### Streamlit object

At the core of the application is the Streamlit object where most of the user interaction and business logic takes place. It's composed of five main components:

  1. **Interface** – Handles all user inputs and displays the results
  2. **Config** – Stores static files, including dependency requirements, configuration settings, branding assets (like logos and CSS), and YAML files used for metric definitions, change logs, FAQs, and more
  3. **Functions** – Run all core workflows, including pre-estimation, post-estimation, and personalization logic
  4. **Modules** – House reusable logic such as the statistical engine, multiple comparison correction, ARR/MAU calculations, and uplift scaling shared across functions
  5. **Query Templates** – Standardize how we retrieve data like experiment metadata, conversion rates, and enrollments from the warehouse, while defining the rules for SQL construction



This structure helps us separate concerns so we can update or scale any part independently, and it keeps the app logic clean and testable. For example, we have dedicated data scientists looking after just the MAU or ARR logic. They don’t need to understand the rest of the app they only need to know what input their module receives, how to process it, and how to pass the result back to the central pipeline.

### The IMPACT app’s own database

We store everything from raw input data to historical results and even session-level analytics in the IMPACT app’s own database. Saving historical results allows users to revisit past analyses without needing to re-run the estimation logic. This is especially helpful during planning cycles or when validating previous decisions.

We also track session analytics to help us, as app owners, understand how the tool is used:

  * Which features are most popular
  * How often teams run impact sizing
  * And where there may be opportunities to improve the user experience



Because the database is part of our broader data warehouse, other teams and applications can also access it whether for meta-analyses, centralized reporting, or integrating impact estimates into planning tools like JIRA. So it’s more than just an internal database it’s a key piece of Canva’s analytics infrastructure.

### Snowpark

Snowpark plays a key role in improving performance and efficiency behind the scenes. In the IMPACT app, we use Snowpark to pre-calculate monthly-updated metrics, things like growth factor, retention, and seasonality, which are key inputs for our MAU forecast. Now, technically we could calculate these directly within the Streamlit app itself, but there are two key problems with that approach:

  1. These logic involves queries that can be heavy and slow to run, which would significantly prolong the running time and impact the user experience.
  2. They don’t need to be recalculated every time when the app is running, these metrics only change once a month, or even quarterly.



That’s why Snowpark is a great option here. We migrated those logic into Snowpark jobs, which run on a scheduled basis and write the results to tables. Then, whenever the app needs them, it can query the precomputed tables instantly, making the entire app experience faster and more responsive for the user. So in this case, Snowpark helps us strike the right balance between data freshness and app performance.

### Cortex

Cortex, Snowflake’s fully managed large language model (LLM) service, gives us instant access to industry-leading models like LLaMA, Mixtral, and Claude, all hosted and managed securely within the Snowflake environment. This is especially important for us, as it ensures our data never leaves our ecosystem, a big win for compliance and governance.

In the IMPACT app, we use Cortex to summarize analysis results in natural language making them more accessible, especially for non-technical stakeholders. After an impact analysis is completed, users can generate a clear, readable summary of the results, making it much easier to share insights without needing to interpret technical tables or statistical outputs.

### Snowflake python connector

Snowflake python connector is the backbone of how the IMPACT app communicates within the Snowflake environment. This connector isn’t just a simple bridge between our app’s logic and the database, it actually plays a huge role in optimizing app performance.

During the initialization stage of the IMPACT app, by design, it runs a large number of backend operations, such as creating temporary tables, fetching experiment metadata, or querying external reference tables etc. Because they are all independent to each other, rather than executing these operations one at a time with the standard `execute()` method, we use `execute_async()` to run them in parallel whenever possible.

Another great example is retrieving metric conversion data during the analysis process, so for each impact analysis, we need run dozens of independent conversion queries. Because they don’t depend on each other, it's a perfect use case of execute_async() that we can process them concurrently using asynchronous execution. This significantly reduces the initial loading time and processing time, which directly translates to a faster user experience.

So while it may seem like a small piece in the diagram, the Python connector is a powerful enabler of speed and scalability for the app.

## Enabling a PR-Based Development Environment

Like many early-stage Streamlit apps, the IMPACT app started with a single developer and a single Python file. This setup made deploying new changes quick and simple changes were tested locally, committed, and then pushed straight to production. And just like that, the updated app was live.

However, as the number of developers have increased, this development method has significantly slowed the progress.

  1. Developers typically develop their changes locally. Once the code is tested, it’s handed over to the app owner for further modifications and integration into the source code. This meant the app owner became a bottleneck and even worse, changes were often made directly into the production codebase, which carried a high risk of breaking the entire app.
  2. As the application’s functionality expands, maintaining all code in a single .py file becomes impractical. This is where modularized design comes into play as I mentioned earlier. But with this modularity comes a new challenge: testing changes directly in production brings another risk of breaking the application. As we may easily ignore certain links between different modules.
  3. On average, the IMPACT app handles approximately 100 unique usage per day. This means any prolonged downtime may disrupt the user experience and further delay the delivery of their analysis reports.
  4. The IMPACT app has its own database for storing user-generated analysis reports. As a result, any changes to these database tables must be thoroughly tested to ensure backward compatibility and prevent issues across dependent applications.



Given all these challenges, it’s clear that the existing development approach is no longer sufficient to meet the growing demands of the application and its users. This where we need a development environment or PR environment. Just like any typical software project. But we need to setup the development environment by ourselves because at the time, Streamlit in Snowflake didn’t support this natively out of the box.

With help from [Kaihao Wang⁠(opens in a new tab or window)](https://www.linkedin.com/in/kaihaowang/), we built a dev environment that allows developers to test their changes end-to-end, using a exact copy of the production setup, but fully isolated from actual users. Each developer, including the app owner, can deploy their own Streamlit instance, which points to a dedicated dev database. This allows them to test new features, improve code logic, or basically anything they want to test without affecting production. Once the code is stable and verified, we then merge it into the production environment, where it powers the prod app and database. So this setup not only minimize the risk of introducing bugs in to production version, but also gives developers faster feedback loops and encourages testing different ideas, and makes it much easier and safer for multiple people to work on the same app at the same time.

![Setup a PR env](https://www.canva.dev/_next/static/media/pr_env.61027632.svg)

Create a new streamlit object and only users with dev__developer can access.

To make this dev environment actually work in practice, we set up a dedicated developer role called `dev__developer`. Users with this role get access to a replicated version of both the codebase and the database so they can work on the app without touching production version. Essentially, we create a new streamlit object and only users with `dev__developer` can access.

All they need to do is:

  1. Create a branch and open a PR
  2. Run a bash script we’ve created



And the bash script basically:

  1. Retrieves the PR number
  2. Creates a Snowflake stage using this PR number
  3. Uploads the code artifacts to that stage
  4. Deploys a fully functional Streamlit app instance linked to that specific PR



This means developers can run, test, and demo their changes in a production-like setting without risking anything in the prod environment.

It’s been a huge step forward for developing the IMPACT app. We now have 5 developers working on different features on IMPACT app and we can all work in parallel.

## Summary

With the toolbox provided by Snowflake, including Streamlit, Snowpark, and Cortex, we were able to build an internal product that gives us performance, flexibility, and simplicity, all in one single ecosystem.

With IMPACT app, we were able to standardizing the commercial impact calculation, scaling decision-making, empowering all teams, and creating a shared source of truth by deeply connected to Canva’s foundational business model.

More importantly, we were also able to take something that used to require 6+ hours of manual analysis, and turn it into something that now takes under 10 minutes. This greatly allows teams to move faster and make decisions with confidence.

To further streamline the app development, we also built a custom development environment that made collaboration safer and more scalable, allowing developers across the data team to test and ship changes without worry of breaking production.

And perhaps the most important shift of all: we began treating our data product like a real product. That means making it scalable, testable, and intuitive to use not just for data scientists, but for all stakeholders.

We hope this post gave you a few useful ideas whether you're just starting to build internal tools or scaling something that's already making an impact.

## Acknowledgements

This project brought together data engineers, data analysts, product manager, and finance analyst across Canva and it’s been a true team effort. I want to thank [Harry Liu⁠(opens in a new tab or window)](https://www.linkedin.com/in/harry-liu17/), [Kaihao Wang⁠(opens in a new tab or window)](https://www.linkedin.com/in/kaihaowang/), [Muhsin Karim⁠(opens in a new tab or window)](https://www.linkedin.com/in/muhsinkarim/), [Eiva Orce⁠(opens in a new tab or window)](https://www.linkedin.com/in/eiva-orce-rodriguez-2792a959/), [James Robinson⁠(opens in a new tab or window)](https://www.linkedin.com/in/james-robinson-a9013589/), [Peter Ayre⁠(opens in a new tab or window)](https://www.linkedin.com/in/peter-ayre-96b0289b/), [Ollie Kirk⁠(opens in a new tab or window)](https://www.linkedin.com/in/ollie-kirk-b6963389/), [Matt D'Cruz⁠(opens in a new tab or window)](https://www.linkedin.com/in/matthewdcruz/), [Amy Morris⁠(opens in a new tab or window)](https://www.linkedin.com/in/amy-morris-400bb452/), [Ariel Lowell⁠(opens in a new tab or window)](https://www.linkedin.com/in/ariel-lowell-7321a4113/), [Jess MacKillop⁠(opens in a new tab or window)](https://www.linkedin.com/in/jessica-mackillop-cfa-433972ba/), [Warren Tat⁠(opens in a new tab or window)](https://www.linkedin.com/in/warren-tat-476a92b7/), [Jake Warner⁠(opens in a new tab or window)](https://www.linkedin.com/in/jake-warner-scientist/), [Fiona Wong⁠(opens in a new tab or window)](https://www.linkedin.com/in/fionasmwong/), [Elvis Leng⁠(opens in a new tab or window)](https://www.linkedin.com/in/elvis-leng/), [Jeremy Sha⁠(opens in a new tab or window)](https://www.linkedin.com/in/jiazhesha/), [Prateeti Tomar⁠(opens in a new tab or window)](https://www.linkedin.com/in/prateeti-tomar/), [Leesa Wockner⁠(opens in a new tab or window)](https://www.linkedin.com/in/leesa-wockner-918b06141/), [Suyan Jin⁠(opens in a new tab or window)](https://www.linkedin.com/in/suyan-j-aaa52522/), [Eugene Chen⁠(opens in a new tab or window)](https://www.linkedin.com/in/eugene-chen-7b0a20140/), and [Sarah Taig⁠(opens in a new tab or window)](https://www.linkedin.com/in/sarahtaig/), who helped shape the IMPACT app from code contributions, model design to user feedback, app promotion, and infrastructure support.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.e7e2d74e.jpg)](https://www.canva.dev/blog/engineering/why-we-left-manual-ui-testing-behind/)

[UI TestingWhy we left manual UI testing behindHow we use visual regression testing to instill confidence in every product update.](https://www.canva.dev/blog/engineering/why-we-left-manual-ui-testing-behind/)

[Joscha Feth⁠(opens in a new tab or window)](https://twitter.com/joschafeth)Dec 12, 2018

[![](https://www.canva.dev/_next/static/media/thumbnail.5451a0a3.png)](https://www.canva.dev/blog/engineering/enabling-real-time-collaboration-with-rsocket/)

[GatewayEnabling real-time collaboration with RSocketThis post describes how we empowered our users at Canva to collaborate by introducing services that support streaming using RSocket.](https://www.canva.dev/blog/engineering/enabling-real-time-collaboration-with-rsocket/)

[Sergey Tselovalnikov⁠(opens in a new tab or window)](https://twitter.com/SerCeMan), [Paul Tune⁠(opens in a new tab or window)](https://medium.com/@anamolous.behaviour), [Michael Belton⁠(opens in a new tab or window)](https://au.linkedin.com/in/michaelbelton)May 27, 2021

[![](https://www.canva.dev/_next/static/media/thumbnail.d96675bf.jpg)](https://www.canva.dev/blog/engineering/why-well-always-be-exploring-new-programming-languages-at-canva/)

[Engineering ProcessesWhy we'll always be exploring new programming languages at CanvaOur choice of programming language has the ability to change the way we view a problem and how we interact with it.](https://www.canva.dev/blog/engineering/why-well-always-be-exploring-new-programming-languages-at-canva/)

[Josh Leeb-du Toit⁠(opens in a new tab or window)](https://joshleeb.com/)Oct 5, 2018

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


