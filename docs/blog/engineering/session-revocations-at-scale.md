---
url: https://www.canva.dev/blog/engineering/session-revocations-at-scale/
title: Session revocations at scale - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:17.130429+00:00
---

# Session revocations at scale - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/session-revocations-at-scale/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Backend

# Session revocations at scale

How Canva keeps hundreds of millions of user sessions fast and secure

![](https://www.canva.dev/_next/static/media/thumbnail.b9cff2fd.png)

* * *

  * 


[Llew Vallis⁠(opens in a new tab or window)](https://www.linkedin.com/in/llew-vallis-153b50246)Jul 22, 2026

* * *

Managing sessions for hundreds of millions of users is a tricky problem because every backend request needs to know which logged-in user made it. At Canva’s scale, this means answering this question hundreds of thousands of times every second. We keep session revocations directly in memory for the best possible performance and reliability, but as we grew, loading this cache during deploys became a bottleneck.

Canva uses browser cookies to store everything we need to know about a user’s session, from their user ID to their permissions and roles. By encrypting these cookies, our gateways can trust these details without talking to a networked datastore on every request. However, if a user is logged out or their permissions change, we need to be able to revoke or update their cookies in near real time.

To enable this, each gateway needs a record of any revoked sessions. We use in-memory lookups because they’re faster and more reliable than checking a networked datastore. Since our session cookies refresh periodically, we store 12 hours of revocations in memory and rely on slower MySQL lookups during these refreshes. Tokens that need refreshing will always be checked against the database, so they don’t have to rely on the in-memory cache.

Although reading the in-memory cache is cheap, seeding it was becoming an issue. With hundreds of gateway pods each potentially pulling over a million revocations from MySQL on startup, our deployments became a coordinated stampede on our database. Although we could temporarily mitigate this by adding a large number of read replicas, we needed a better solution, and ideally one that would reduce the in-memory size of the cache too.

The diagram below shows this pre-existing system end-to-end.

![](https://www.canva.dev/_next/static/media/pre-existing-architecture.69df2790.png)

Our pre-existing session revocation architecture

## Optimizing our in-memory cache

We didn’t want to address this by slowing down our deployments, so we fundamentally needed to deal with many gateway instances downloading the whole cache of over a million revocations at once. The challenge was to maintain the fast and reliable per-request in-memory session revocation checks at the gateway level, but avoid overloading our MySQL database when the cache needed to be loaded on deploy.

A standard solution to scaling reads is to introduce a cache between the database and the reader, but the choice of caching technology isn’t so obvious. Redis is a popular caching technology, so we evaluated it as an intermediary cache. On startup, each gateway instance would ask Redis (over a network call) for the full in-memory dataset, and then periodically poll for new revocations to stay up to date. The main problem is that Redis isn’t typically deployed in a fully durable configuration, and we would still need to manage the Redis cluster itself. We would just be moving our problems from one datastore to another, while adding significant complexity to keep the cache consistent.

We needed something that provides strong durability guarantees and that supports efficient reads of large amounts of data. This led us to S3, which is designed to serve downloads of large, durably stored files at a low cost. This is exactly what we needed for our use case, but it also presented a major challenge since we’re caching a moving window of records, not a blob of static binary data.

If we wanted to use S3 to cache our data, we needed to convert our sliding window of revocation records into a format suitable for object storage. We decided to partition our sliding window into 30-minute segments, each corresponding to one object in S3. We don’t need to worry about individually removing old revocations from S3, since each gateway instance can fetch only the most recent chunks. This also lets us perform smaller updates, since each 30-minute block contains less data than the full multi-hour window. However, even with 30-minute chunks, adding a single revocation into S3 requires downloading and re-uploading potentially hundreds of thousands of records. We’ll go into more detail on that later.

![](https://www.canva.dev/_next/static/media/binary-format.9eb65c60.png)

Binary data format of a single revocation

Each revocation contains two critical pieces of information: who it applies to (called the “principal”), and the login timestamp up to which it applies (typically, you would revoke all sessions started before a specific timestamp). With some bit twiddling we’re able to pack this into 16 bytes, with our revocation chunks just being a flat array of these 16-byte elements. By sorting this array, we can efficiently binary search each chunk to find revocations that apply to a specific principal. This makes the cache loading incredibly fast, since the only cost paid is the download from our S3 bucket. Our gateway service never even needs to transform these chunks into a different representation, and can instead operate directly on the downloaded bytes. By keeping only the dense binary representation in memory, we also reduced the size of our in-memory cache by a factor of 8 compared to our previous implementation which tracked each revocation using multiple Java objects. Although the cache’s memory footprint wasn’t our biggest challenge, this was still an important improvement given that millions of revocations can fall within the cache’s 12-hour window.

In practice, it turns out to be a bit more complicated, since we need to support multiple types of revocations. For example, we might want to invalidate some information cached in a user’s cookies without logging them out, or we might want to target an entire brand rather than a single user. To handle this, we needed to reserve a few bits for flags, but as long as we still sort by each revocation’s principal, we can store many types of revocations in the same flat array.

![](https://www.canva.dev/_next/static/media/bucket-format.f5087069.png)

Structure of data in our revocations S3 bucket

## Keeping the chunks up to date

A major challenge of this approach is keeping the chunks up to date. Rewriting a chunk in S3 every time a revocation is created would be incredibly expensive. Instead, we delegated this task to an asynchronous worker process. The worker continually scans our database and fetches large batches of revocations which haven’t yet been uploaded to S3. The worker then fetches the latest chunk (or creates a new one if sufficient time has passed), inserts the new revocations into the sorted array, and then re-uploads the chunk.

To ensure high availability and to aid with deployments, we run multiple copies of this worker process at any given time. In a naive implementation, this would give rise to data races against S3, such as lost updates where revocations are silently dropped. To mitigate this, we use conditional PUT requests to implement optimistic concurrency control. This includes adding a precondition on all chunk updates to assert that the chunk hasn’t changed since it was first read, and newly created chunks use similar checks to ensure another process hasn’t already created the same chunk. The PUT conditions guarantee that each read-modify-write operation only ever appends to the set of revocations in S3, ensuring interleaving executions never lose data.

We also use a ZooKeeper leader election as an optimization to prevent continuous conflicts from adding load to our system. Although the leader election means worker tasks rarely race each other, we can’t depend on this for correctness. For example, a node could pause for an arbitrary period of time just before performing a write operation. By the time it resumes, another node might have become the new leader and written its own changes, which the original node would overwrite once it wakes up if it weren’t for our PUT conditions.

![](https://www.canva.dev/_next/static/media/worker-sequence.53723b51.png)

How a worker task copies revocations from our database into S3

At first glance, this approach might not seem like it scales. Building a chunk of `N` revocations requires on the order of `O(N^2)` time, since we need to process the entire chunk for each fixed-size batch of revocations we add. Worse yet, we can’t easily scale this process horizontally without running into the aforementioned lost update problem. In practice, though, by processing many hundreds of revocations in each batch, even an unoptimized implementation can achieve a write throughput above 2000 revocations per second. This is more throughput than we expect to need for the foreseeable future.

## Downloading the chunks

Each chunk in our bucket contains all revocations that were created within a particular 30-minute window. Since we only need revocations that were created in the past 12 hours (all tokens are guaranteed to refresh in this time window), we can download only a subset of the most recent chunks when a gateway pod starts up. Each chunk encodes the timestamp of the start of its 30-minute window directly in its name, so we can efficiently find all applicable chunks by searching for keys in sorted order after a cutoff timestamp.

We also need to keep our in-memory caches continuously up to date with new revocations as they are created; otherwise, they would only be picked up during deployments. To achieve this, we used S3 conditional GET requests to redownload the latest chunks only when they have actually changed. Even if we had 1 million revocations in a 30-minute window, this would only be 16 megabytes a few times per minute, which is just a drop in the ocean compared to the amount of request and response data our gateways proxy. Once the end of a chunk’s window becomes older than 12 hours, we can simply drop it from the cache.

Each gateway pod still needs to pull the same number of invalidations on startup, but streaming a compact binary version of this data from S3 is significantly faster and more scalable than asking MySQL to serve over a billion rows. For each gateway, this is only tens of megabytes of data, but that becomes tens of gigabytes when considered across the full fleet.

![](https://www.canva.dev/_next/static/media/download-process.01ef20b6.png)

How revocations flow through our new system

## Outcome and learnings

Since migrating to the new session revocation system, we were able to improve deployment speed and reduce the number of read replicas on our session revocation database, keeping only two for redundancy. Our new binary format also reduced the in-memory footprint of our cache by 87.5%, since we were no longer paying the overhead of storing multiple objects on the Java heap for each revocation. Previously, our database load depended on the number of previous writes in a multi-hour time span, and on the number of gateway instances attempting to download the cache at any given time. With the new solution, the load predictably scales with our write throughput and overall site traffic.

The biggest takeaway from this project is the difference between scaling in theory and in practice. At first glance, having a single worker constantly sorting hundreds of thousands of records might sound inefficient, but empirical testing proved that the worker’s throughput exceeded our practical requirements. Constant factors matter enormously – modern systems are so good at processing dense arrays that our worker implementation is actually bottlenecked on network latency, even when dealing with hundreds of thousands of revocations in a single array.

In the age of AI coding agents, it is incredibly easy to play with mock implementations of distributed system designs on your cloud platform of choice. In our case, we implemented multiple different solutions to our problem and tested them at our expected scale on real infrastructure. This gave us the confidence to pick the approach that worked best for us since we had proven that it met our scalability requirements. After developing a proof of concept, we used our extensive suite of end-to-end tests and careful human review to ensure the production-ready version was safe for our users.

## Acknowledgments

Thanks to [Joeby Neil⁠(opens in a new tab or window)](https://www.linkedin.com/in/joeby-neil) for collaborating with me on building this solution and to [Martin Doms⁠(opens in a new tab or window)](https://www.linkedin.com/in/martin-doms/) for their support. Thanks also to [Dennis Kao⁠(opens in a new tab or window)](https://www.linkedin.com/in/dennis-kao/), [Michael Yates⁠(opens in a new tab or window)](https://www.linkedin.com/in/michael-yates-bab837/), [Zac Sims⁠(opens in a new tab or window)](https://www.linkedin.com/in/zacsims/), [Stu Liston⁠(opens in a new tab or window)](https://www.linkedin.com/in/stu-liston/), [Min Coombes⁠(opens in a new tab or window)](https://www.linkedin.com/in/melindacoombes/), and [Simon Newton⁠(opens in a new tab or window)](https://www.linkedin.com/in/nomis52/) for taking the time to provide feedback for this article.

If you want to work on interesting technical challenges too, then come [join us⁠(opens in a new tab or window)](https://www.lifeatcanva.com/en/jobs/)!

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.3ac4421d.png)](https://www.canva.dev/blog/engineering/faster-ci-builds-at-canva/)

[InfrastructureFaster continuous integration builds at CanvaHow we improved our continuous integration build times from hours to less than 30 minutes.](https://www.canva.dev/blog/engineering/faster-ci-builds-at-canva/)

[Marco Lacava⁠(opens in a new tab or window)](https://www.linkedin.com/in/marco-lacava/), [Arpit Sharma⁠(opens in a new tab or window)](https://www.linkedin.com/in/notarpit/)Jul 30, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.0dd77367.png)](https://www.canva.dev/blog/engineering/a-journey-through-colour-space-with-ffmpeg/)

[Color SpaceA journey through color space with FFmpegFor those who want to understand what color spaces are, find out how to transform videos from one color space into another one, or read about how I almost went crazy trying to find out why videos generated with Canva look slightly off in terms of color.](https://www.canva.dev/blog/engineering/a-journey-through-colour-space-with-ffmpeg/)

[Sven Schindler⁠(opens in a new tab or window)](https://www.linkedin.com/in/sven-schindler-de-au/)Apr 17, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.f27ae3db.png)](https://www.canva.dev/blog/engineering/subscription-analytics-at-scale/)

[Data ScienceSubscription analytics at scaleEvolving Canva's subscription data architecture to enable data-driven decision making.](https://www.canva.dev/blog/engineering/subscription-analytics-at-scale/)

[Chuxin Huang⁠(opens in a new tab or window)](https://twitter.com/chuxin_h), [Paul Tune⁠(opens in a new tab or window)](https://medium.com/@anamolous.behaviour), [Grant Noble⁠(opens in a new tab or window)](https://www.linkedin.com/in/grant-noble-8253994a/)Jul 15, 2021

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


