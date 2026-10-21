---
url: https://www.canva.dev/blog/engineering/worker-backpressure-part-1-how-we-taught-our-queue-workers-to-slow-down/
title: Worker Backpressure (Part 1) - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:29.488147+00:00
---

# Worker Backpressure (Part 1) - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/worker-backpressure-part-1-how-we-taught-our-queue-workers-to-slow-down/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Backend

# Worker Backpressure (Part 1)

How we taught Canva's queue workers to slow down when dependencies fail, then speed back up on their own.

![](https://www.canva.dev/_next/static/media/thumbnail.66ba8451.png)

* * *

  * 


[Mikalai Barysau⁠(opens in a new tab or window)](https://www.linkedin.com/in/mikalai-barysau/)Sep 17, 2026

* * *

Earlier this year, we started rolling out a new reliability mechanism for worker components at Canva called Worker Backpressure. Roughly two weeks in, we had a perfect chance to battle-test it: a major cloud-provider outage sent error spikes across a wide range of Canva services, among them a critical queue worker whose dependencies were suddenly failing.

Normally, this would mean thousands of failed messages piling onto a Dead Letter Queue (DLQ), degraded service for customers across the globe, and a page for on-call engineers.

This time, thanks to the backpressure mechanism, the worker slowed itself down when its dependencies started failing, taking the pressure off them, and then sped back up on its own once they recovered. The DLQ stayed quiet, no one was paged, and the service stayed reliable for customers.

This post covers why we built backpressure and how we designed it to keep our dependencies safe and our services healthy even when parts of the system degrade.

## The problem: greedy workers

A lot of work at Canva happens asynchronously. A request comes in, the service drops a message onto a queue, and a worker picks it up later and does the actual work: resizing an asset, running a classification model, sending an email, or reconciling a subscription. This keeps the request path fast, while the queue absorbs the slow or bursty work. It also keeps the request reliable: if a dependency is briefly down, the user's request still succeeds, and the work waits on the queue.

![Asynchronous request flow](https://www.canva.dev/_next/static/media/request_flow.a99f5eed.svg)

Figure 1: Asynchronous request flow

Workers are built to be greedy, and most of the time that's exactly what you want. As soon as a message lands on the queue and a worker has spare capacity, it grabs and processes it. When everything downstream is healthy, this gives you minimum latency and full use of the infrastructure you're already paying for.

To process a message, a worker almost always calls a dependency: a shared resource, such as a datastore, or another service. The trouble begins when that dependency starts to fail. The greedy worker doesn't notice and keeps pulling messages and firing more requests, which hurts in multiple ways:

  * It pours fuel on the fire, making the dependency take longer to recover.
  * Processing a message that's doomed to fail wastes already-scarce resources.
  * Failed messages get retried until they land on the DLQ, which someone has to drain and reprocess, in many cases by hand.
  * An on-call engineer gets paged and babysits the situation until the dependency recovers.



At Canva's scale, this isn't a rare edge case: we run thousands of queues with diverse business logic and dependencies. Take something routine: a user clicks _Export_ , a message lands on a queue, a worker picks it up, fetches design data from a database, and calls a rendering service. If that database is already slow, perhaps under a background migration, the greedy worker keeps pulling from the queue at full speed. A few slow responses from the database can then snowball into a high-severity incident with exports failing for thousands of users.

Every such incident raises the same questions. Should the worker stop entirely or just slow down? By how much, and for how long? What signals should drive that decision? Finding one answer that works across our diverse fleet is far from trivial.

## What teams were already doing

**Manually scaling the worker fleet.** Scaling up during trouble risks unleashing more load on the exact dependency that's already failing, and any manually chosen number is a guess: too low and the backlog keeps growing, too high and you pay for workers that sit idle.

**Rate limiting inside the processing logic.** A fixed rate limit is only correct for a fixed world. Capacity changes constantly, especially for shared dependencies, so a stale limit either throttles the worker for no reason or sits so far above real capacity that it barely protects anything.

**Circuit breakers.** They count errors, trip open when a threshold is crossed, and stop all traffic until a cooldown expires. There's no gradual ramp between full speed and full stop, and the sudden flood of resumed traffic can knock over a dependency that had only just caught its breath.

**Exponential backoff.** Applied to retries, it smooths out individual retry storms, but it operates per-message and doesn't regulate the overall rate at which a worker leans on a dependency.

**Adaptive backoff.** It wraps calls to a dependency and rejects a fraction of them as errors climb, using the client-side adaptive throttling in the ["Handling Overload" chapter of Google's SRE book⁠(opens in a new tab or window)](https://sre.google/sre-book/handling-overload). Unlike retry backoff, it sheds load at the call site rather than delaying each failed message. One of our teams had already built such a library and ran it in production. It worked well and directly inspired this project, but it lived outside the shared queue library and was fixed to one algorithm.

## The solution: a built-in feedback loop

We needed an adaptive worker backoff solution general enough for our fleet of diverse queues and named it **Worker Backpressure** : a mechanism built into our `queue` library. The worker watches how its own work is going and adjusts its speed accordingly, easing off as errors climb and ramping back up as the dependency recovers, with no human intervention required.

Backpressure is a **feedback loop** around the worker's calls to its dependency. It tracks the outcome of each call as a signal of the dependency's health, and regulates the worker's concurrency: how many messages it may process at once. When the dependency looks healthy, backpressure stays out of the way; when it struggles, it throttles the worker. Backing off early also means fewer doomed attempts wasting scarce resources, and fewer failed messages landing on the DLQ.

Backpressure consists of three pieces:

  1. **Signals.** After each message is processed, the worker records the outcome: success or failure.
  2. **Backpressure Controller.** A pluggable controller (an interface rather than one fixed algorithm) consumes those outcomes and maintains a single number: the **backoff factor** , ranging from `0.0` (full speed) to `1.0` (fully backed off). It works against a configured **set point** : the failure rate the controller treats as acceptable background noise. While the failure rate stays below the set point, the controller does nothing. Once the rate climbs above it, the controller starts backing the worker off.
  3. **Permits.** Before each poll, the worker asks the controller how many messages it may pull and process concurrently (`X` in the diagram below). The controller scales that number down in proportion to the current backoff.

![Worker extended with Backpressure mechanism](https://www.canva.dev/_next/static/media/backpressure.736244dc.svg)

Figure 2: Worker extended with Backpressure mechanism

An important design choice is that all of this happens locally, with no external coordinator and no added network calls. The entire runtime cost is two arithmetic operations: one to move the backoff factor after each outcome and one to scale the requested concurrency at each poll.

A note on the name: backpressure usually refers to a signal traveling upstream to slow the producer, while a worker throttling itself is closer to [Netflix's concurrency-limits⁠(opens in a new tab or window)](https://github.com/Netflix/concurrency-limits). We kept the name because refusing work at the worker leaves that load in the queue, the only upstream we can push back to.

## Seeing it in action

We didn't have to wait long for a real test: backpressure has already protected our dependencies in two production incidents.

On the dashboards below, the orange dashed line marks the set point of 5%, the same value for both workers. Each instance is evaluated against that set point based on its own outcomes, so a single instance can momentarily spike past 5% and get throttled while the fleet-wide failure rate stays low.

### Multi-spike outage

The first is the cloud-provider outage that opened this post: roughly 4 hours of intermittent error spikes, with several of the worker's dependencies failing at once. Two things stood out:

  * Backpressure slowed the worker down and sped it back up, still running the default configuration we'd shipped at rollout.
  * The DLQ grew by just a single message through the entire incident.



In Figure 3 below, the success count shows the worker's normal workload, while the error count spikes at a number of points during the cloud-provider event. The failure-percentage panels show the same errors relative to traffic. Individual worker instances briefly spike as high as 50% and get backed off, so the fleet-wide average peaks at just 1.42%. The backoff factor tracks the error spikes closely, climbing as errors appear and easing back down as they clear. The DLQ depth barely moves: a one-message step rather than the thousands of failed messages an event like this would normally produce.

![Production incident – multi-spike outage](https://www.canva.dev/_next/static/media/multi-spike-outage.32cfb6de.png)

Figure 3: Production incident – multi-spike outage

Metric| Observed  
---|---  
Total success count| 1,610,173  
Total error count| 498  
Failure rate| 0.03% whole-incident average, 1.42% fleet-wide peak  
Incident window| ~4 h of intermittent error spikes  
DLQ growth during incident| 1 message (~0.25 per hour)  
  
### A day and a half of sustained overload

The second incident shows the opposite failure profile: continuous overload instead of short spikes. A worker pushes messages to another queue, which comes with a hard throughput quota. A surge of work drove the fleet's combined send rate over that quota, and the queue kept rejecting pushes for 32.5 hours until a fix landed. The backpressure controller's job here was to contain the failure while the fix was on its way:

  * The controller stayed engaged for 32.5 hours straight. Bursts on individual instances ran as high as ~19% and were throttled back as they crossed the set point, while the fleet-wide failure rate peaked at just 3.7%. The taller ~43% spike is a brief precursor burst on one instance before the sustained overload began.
  * Throughput held up: the fleet kept completing around 2 million messages per hour, above its pre-incident baseline.
  * On this queue, a message moves to the DLQ once it has failed 5 delivery attempts. Out of 1.8 million failed attempts, only 22 messages got that far: roughly one per 82,000 failures (~0.7 per hour). Without backpressure, the closest data point we have is the ~19% failure rate seen on instances the controller hadn't yet slowed down. If anything, that reading is too low: it was taken while backpressure was already slowing the rest of the fleet, easing pressure on the shared quota. An unprotected fleet would also be retrying every failed message at full speed on top of a workload already over the quota. Even assuming failures were independent across a message's 5 attempts, 0.19⁵ of the 65 million messages processed comes to roughly 16,000 DLQ messages (~500 per hour). And that's a lower bound: a message retried within the 32.5-hour incident window would still have hit the breached quota, so one that failed once was likely to fail the rest of its attempts, and the DLQ would have grown faster than 0.19⁵ predicts.



The fleet-average failure-percentage panel shows the rate held in a flat band under the set point for the whole incident. The backoff factor oscillates across its full range the entire time, and the DLQ depth creeps up one message at a time instead of exploding.

![Production incident – a day and a half of sustained overload](https://www.canva.dev/_next/static/media/sustained-overload.aab2eb0e.png)

Figure 4: Production incident – a day and a half of sustained overload

Metric| Observed  
---|---  
Total success count| 63,285,748  
Total failed attempts| 1,795,025  
Failure rate| 2.76% whole-incident average, 3.7% fleet-wide peak  
Time under backpressure| 32.5 h continuous  
DLQ growth during incident| 22 messages (~0.7 per hour)  
  
### What the incidents show

The two incidents had very different failure shapes, and in both, backpressure did the same job. It backed the worker off while errors were present and eased it back to full speed once they stopped. An unprotected worker would have kept hammering struggling dependencies and produced a flood of failed messages and the on-call toil that follows.

The most satisfying part was watching something we'd spent months designing hold up unsupervised in two real incidents. Both times it did exactly what we built it to do, without anyone getting paged in the middle of the night.

## Trade-offs

In this first iteration of the design, we made conscious trade-offs in favor of something small yet effective, intending to deploy, assess, and then iterate.

### A throughput cost

Backpressure cuts the error rate, but it also costs throughput. We consider that a fair price for containing the blast radius of a failure and avoiding the manual toil that follows. In the two incidents above, the workers had enough headroom to absorb the slowdown, and the sustained-overload worker even held its throughput above the pre-incident baseline. However, a worker running at full capacity would feel the cost.

### One simple signal

The controller reacts to one signal, success versus failure outcomes, as a proxy for the health of the dependency. That keeps the mechanism easy to reason about, but a single proxy won't fit every workload, and we don't yet know where it falls short. We expect to find out as the rollout exposes backpressure to a wider variety of workers and failure modes. Starting narrow was a deliberate choice for the first implementation, and the controller is extensible, so more signals, such as latency or messages in flight, can be added later.

## What's next

Our immediate goal is to roll backpressure out to all of Canva's queue workers.

There's also plenty this post glossed over. How exactly does the backoff factor move? If a fully backed-off worker pulls no messages, how does it discover that its dependency has recovered? And how do you pick the two knobs that tune the whole mechanism? In Part 2 (coming soon), we open up the controller, put it through a range of simulated outages, and cover the directions we're exploring beyond that.

## Acknowledgments

Thanks to [Natalie Tridgell⁠(opens in a new tab or window)](https://www.linkedin.com/in/tridgell/), [Ross Black⁠(opens in a new tab or window)](https://www.linkedin.com/in/rossblack/), [Michael Yates⁠(opens in a new tab or window)](https://www.linkedin.com/in/michael-yates-bab837/), and [Elle Dally⁠(opens in a new tab or window)](https://www.linkedin.com/in/elle-dally-b12a66121/) for helping build backpressure. Thanks also to [Tim Deng⁠(opens in a new tab or window)](https://www.linkedin.com/in/jintian-deng/) and [Xushen Ma⁠(opens in a new tab or window)](https://www.linkedin.com/in/xushen-ma-7a273160/), whose early adopter teams helped us study the problem and tune the defaults, and who trusted backpressure in production.

_If you'd like to work on problems like this, take a look at our[current openings⁠(opens in a new tab or window)](https://www.lifeatcanva.com/en/jobs/)._

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.0dd77367.png)](https://www.canva.dev/blog/engineering/a-journey-through-colour-space-with-ffmpeg/)

[Color SpaceA journey through color space with FFmpegFor those who want to understand what color spaces are, find out how to transform videos from one color space into another one, or read about how I almost went crazy trying to find out why videos generated with Canva look slightly off in terms of color.](https://www.canva.dev/blog/engineering/a-journey-through-colour-space-with-ffmpeg/)

[Sven Schindler⁠(opens in a new tab or window)](https://www.linkedin.com/in/sven-schindler-de-au/)Apr 17, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.fd5d2f0c.png)](https://www.canva.dev/blog/engineering/search-pipeline-part-ii/)

[Search and RelevanceSearch Pipeline: Part IIMore on how we are rebuilding Canva's search stack and pipeline.](https://www.canva.dev/blog/engineering/search-pipeline-part-ii/)

[Stuart Cam⁠(opens in a new tab or window)](https://www.linkedin.com/in/codebrain/)Nov 17, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.bf282bb2.jpg)](https://www.canva.dev/blog/engineering/scaling-to-count-billions/)

[BackendScaling to Count BillionsHow we built a scalable and reliable content usage counting service.](https://www.canva.dev/blog/engineering/scaling-to-count-billions/)

[Sangzhuoyang Yu⁠(opens in a new tab or window)](https://au.linkedin.com/in/yuszy)Apr 12, 2024

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


