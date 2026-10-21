---
url: https://www.canva.dev/blog/engineering/infrastructure-is-distribution/
title: Infrastructure is Distribution - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:14.780830+00:00
---

# Infrastructure is Distribution - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/infrastructure-is-distribution/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Infrastructure

# Infrastructure is Distribution

How we position Infrastructure Engineering as a value-add.

![](https://www.canva.dev/_next/static/media/thumbnail.0b03c2dc.png)

* * *

  * 


[Ryan Armstrong⁠(opens in a new tab or window)](https://www.linkedin.com/in/ryanarmstrongwa/)Mar 14, 2022

* * *

The Infrastructure (Infra) group at Canva is growing fast. The group is composed of around 200 engineers who are responsible for the delivery of engineering workstations, software development tools, production workload scheduling, scalable and durable data-stores, and most importantly, the primitive components that product engineering teams can compose together to [_empower everyone in the world to design anything and publish anywhere_ ⁠(opens in a new tab or window)](https://www.canva.com/about/).

What Infra is _not_ is an engineering group that builds and ships products that Canva users know or care about.

With the rapid growth of Infra comes a perfectly reasonable pause for consideration: **what is a healthy head count?** My answer piqued some curiosity: "_If things go well, I expect Infra should grow to be around 50% of all Engineering_ ".

You'd be forgiven for thinking of Infrastructure as a cost center, but we see it differently.

> Instead, Infra is a value-add and a key differentiator in Canva's business model.

## Infrastructure engineering is distribution

In the pre-dot-com era, it was a foregone conclusion that distribution was the lion's share of the cost of doing business and a key differentiator.

Product development of ground-breaking products, like the Ford Model T, took smarts and an obsession with product-market-fit. But after the product was designed and the prototypes were validated, manufacturing, shipping, warehousing, and delivery became Ford's differentiator. For McDonald's, it wasn't their Tempting Cheeseburger that launched them to global dominance, but their real-estate empire and their ability to reproduce a quality product at scale. I'd confidently wager there were better burgers out there, but no one could scale distribution like McDonald's.

![McDonald's is an example of a company that has mastered scale, particularly
in the distribution of
cheeseburgers.](https://www.canva.dev/_next/static/media/img-1-CR4A72Q_WcPE7TCRw5727w.6856be77.png)

McDonald's scales cheeseburger distribution like no other ([Source⁠(opens in a new tab or window)](https://www.canva.com/photos/MAEAVTHWHJs-burger-with-cheese/))

Ford and McDonald's were able to get their product into the hands of customers and keep them satisfied — more effectively than their competitors.

For modern software as a service (SaaS) companies like Canva, **infrastructure engineering _is_ distribution**. As Canva product teams build products that address market needs, Canva's destiny is co-owned by Infra, who must outpace our competitors' ability to get the products in front of users with low latency, high availability, perfect durability, and uncompromising security and privacy.

## Planet-scale distribution is not a solved problem

Where once companies had to scale a mountain to get their products into the hands of users, the rise of e-commerce detonated a hole right through it.

Businesses like eBay or Yahoo could get their products in front of millions of users without building their own physical distribution networks. The Internet made for a cheap and readily-accessible platform where customers can come to you at any time of the day, from the comfort of their homes.

Then came the rise of Cloud computing.

Many of the difficult parts of distribution on the Internet can now be outsourced to world-class providers whose offerings are far more robust and sophisticated than any small startup company could hope to replicate.

So why do we need Infrastructure engineers working on distribution? The truth is, most small businesses don't. Cloud providers and platform as a service (PaaS) providers have product offerings allowing small businesses to get their products in front of millions of users, employing only commodity skill sets.

What are the options for the outlier companies who want to reach tens or hundreds of millions of users, or who want to serve petabytes or exabytes of data?

Planet-scale distribution is not a solved problem. In my mental model, we can categorize solutions for Internet distribution into three horizons of scale: **Outsourced, Integrated** and **Bespoke**.

![The three horizons of scale: Outsourced, Integrated, Bespoke. Outsourced are for undifferentiated distribution needs, Integrated for distribution needs that outgrow the offerings of any single PaaS provider, and Bespoke for Distribution needs that outgrow integrated public PaaS offerings. Companies move from Outsourced to Integrated and finally to the Bespoke horizon.](https://www.canva.dev/_next/static/media/img-1-eSq8Erm6out400-JcqgqfA.82e1b167.png)

The three horizons of scale: Outsourced, Integrated and Bespoke

The _Outsourced_ horizon is where most companies start. Their distribution needs are undifferentiated, so they can outsource almost everything to Cloud/PaaS providers and focus on developing product/market fit.

The _Integrated_ horizon characterizes companies whose distribution needs out-grow the offerings of any single PaaS provider, so they must integrate solutions from many providers. They'll have large bills on the balance sheet from AWS, Github, BuildKite, Datadog, Sentry.io, Snowflake, Snyk, and so on. The work of curating and integrating these solutions into a single coherent platform for Product teams is the work of the Infrastructure engineer. If they get it right, these investments will have a disproportionately positive return.

The deployment of these integrations comes with inherent risks, including security vulnerabilities, configuration diversity, and artificial constraints on product development. The remit of Infra is to abstract away these concerns with a private PaaS offering that feels like a public PaaS offering, but is a highly-tuned amalgam of third-party products.

The _Bespoke_ horizon is now exclusively the territory of rare unicorns where the distribution needs outpace anything we can support through integrated public PaaS offerings. It's territory where the economies of scale mean it's cheaper to hire world-class talent to build bespoke software than it is to outsource to a PaaS provider. It's cheaper to build and operate your own data-centres than to employ a cloud provider. This is the domain of companies with hundreds of millions or actual billions of monthly active users. This is the land of bespoke programming languages and databases.

## Where we are right now

Canva has grown at break-neck speed from the _Outsourced_ horizon into the _Integrated_ horizon. If we're successful in our ambitions, we'll need to start solving for the _Bespoke_ horizon soon.

In this model, we humbly accept that a home-grown distribution infrastructure is a necessary burden for companies who want to play at a certain level — just like the PaaS bill is for small-scale companies. But there are massive opportunities.

Canva has a platform and distribution network for reaching tens of millions of active monthly users with secure and reliable products that our competitors do not. The infrastructure team is building it. Do we wish we could outsource it all to a single, cheaper line item on the balance sheet? Maybe. That'd be fantastic on the surface, but it would also mean we're playing in a commodity space, not pushing the limits of market reach.

Many people can build a great product. However, only a selection of those can mobilize a collective of human beings and build a distribution network to get that product into the hands of the customers who will love it and pay for it.

Infrastructure engineering unlocks a broader market penetration, beyond the reach of our competitors. Infrastructure engineering provides us with a platform to explore new market opportunities with reliability, security, scalability, and brand trust built-in from day one. Infrastructure engineering improves our time-to-market and the ease with which our incredible product development teams can build and ship groundbreaking new features.

The broader the scale, the fewer the problems we can solve with commodity solutions, and the more leverage we gain with a competency for Infrastructure engineering.

_Canva is growing and looking for new Canvanauts to help empower the world to design. If you want to be a part of it,_ [_we'd love to hear from you_ ⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/)!

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.6933959c.jpg)](https://www.canva.dev/blog/engineering/draw-in-present-mode/)

[Draw toolFrom Intern Project to Production: How I Shipped the Draw Tool for Canva's Present ModeOverview of the technical hurdles I overcame to evolve my intern project into a new feature for users.](https://www.canva.dev/blog/engineering/draw-in-present-mode/)

[Edwina Adisusila⁠(opens in a new tab or window)](https://www.linkedin.com/in/edwina-adisusila/)Aug 6, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.bf282bb2.jpg)](https://www.canva.dev/blog/engineering/scaling-to-count-billions/)

[BackendScaling to Count BillionsHow we built a scalable and reliable content usage counting service.](https://www.canva.dev/blog/engineering/scaling-to-count-billions/)

[Sangzhuoyang Yu⁠(opens in a new tab or window)](https://au.linkedin.com/in/yuszy)Apr 12, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.4c1ba47e.png)](https://www.canva.dev/blog/engineering/standardizing-the-development-environment/)

[ToolingStandardizing the development environmentHow we've built a Standard Development Environment (SDE).](https://www.canva.dev/blog/engineering/standardizing-the-development-environment/)

Josh GrahamApr 21, 2015

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


