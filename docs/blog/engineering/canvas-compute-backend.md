---
url: https://www.canva.dev/blog/engineering/canvas-compute-backend/
title: Canva's compute backend - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:11.580367+00:00
---

# Canva's compute backend - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/canvas-compute-backend/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Performance

# Canva's compute backend

Developing the Compute Service, aimed at the increasing processing burden of password hashing and the signing of private CDN URLs.

![](https://www.canva.dev/_next/static/media/thumbnail.c165186b.png)

* * *

  * 


[Sam Killin⁠(opens in a new tab or window)](https://au.linkedin.com/in/samuelkillin)Sep 15, 2015

* * *

 _Originally published by_ [_Sam Killin_ ⁠(opens in a new tab or window)](https://au.linkedin.com/in/samuelkillin) _at_ [product.canva.com⁠(opens in a new tab or window)](https://product.canva.com/canvas-compute-backend/) _on September 15, 2015._

A great engineer once told me that it doesn't matter how big your organisation is, you'll always experience growing pains. Canva is far from immune to these pains, and we're constantly reevaluating our infrastructure to ensure that systems designed for Canva of old are still up to scratch for Canva of the present, and will be in good stead to support the Canva of the future.

My first task as the newest, most starry-eyed member of Canva's engineering team was to develop a new backend system, the _Compute Service_ , aimed at tackling one such growing pain: the increasing processing burden of password hashing and the signing of private CDN URLs on our various backend services.

Previously, these CPU intensive hashing and signing functions were tightly coupled to the systems requiring this functionality, giving us no ability to deploy and scale infrastructure focussed on tackling this very particular type of high CPU load separate from the infrastructure requiring it. It was an all or nothing, scale up all our services, or fall behind.

## Wait, so what does it do?

The _Compute Service_ performs two tasks.

Firstly, it hashes passwords with the [BCrypt⁠(opens in a new tab or window)](http://bcrypt.sourceforge.net/) encryption utility. _BCrypt_ wraps _Blowfish_ , an (intentionally) CPU and time intensive hashing function.

Secondly, it signs temporary URLs that reference private media. We heavily leverage CDN services to efficiently distribute media to our users. In the case of private media, (eg. images uploaded into a user's private image library), we craft and sign special URLs that include an expiration time, after which our CDN provider will not serve any content on that URL. We do this as to ensure we don't have references to private media floating around the internet indefinitely. URLs are signed with a _SHA1_ hash, which is an order of magnitude less time and CPU intensive to calculate than as is with _Blowfish_ , however we sign an awful lot of these URLs.

It should be noted that the _Compute Service_ is designed to handle CPU demanding functions that are synchronous, or inlined into a single request. For other computationally demanding tasks, such as the export of Canva designs, we place that work on a queue for asynchronous processing and result retrieval at a point in the future. For tasks such as hashing a password during a new user signup, this sort of asynchronous processing is not available to us.

## So how'd you do it

The _Compute Service_ is comprised of a cluster of new _Amazon EC2_ instances, fronted by an _Amazon Elastic Load Balancer_. These instances serve three main RPCs: one for hashing a password, one for checking a password, and one for computing signed URLs for a batch of private media.

## The end goal

We had three goals for the _Compute Service_ :

  * **Graceful failure** : In the event of the _Compute Service_ becoming unavailable, we wanted the rest of our systems to remain as functional as possible, albeit degraded.
  * **The right tool for the right job** : The _Compute Service_ performs a very particular set of tasks that are CPU intensive, rather than being memory or I/O bound. As this service would run as its own dedicated autoscaling group, separate from the five other autoscaling groups that run the rest of Canva's backend services, we had the opportunity to choose an EC2 instance type specifically tailored for these kinds of tasks.
  * **#cloud** : We wanted to be able to raise and lower the capacity of the _Compute Service_ independently from the needs of the rest of our backend services.



We have also recently released features as part of _Canva for Work_ , such as _Photo Folders_ , that require efficient signing of (potentially large) batches of private media URLs. We wanted to leverage the inherent parallelizability of these batch signing tasks by distributing them across the multiple cores of each instance with the goal of reducing the average latency of these requests.

## Microservices

The design for the _Compute Service_ essentially boils down to that as described by the [Microservice Architecture pattern⁠(opens in a new tab or window)](http://martinfowler.com/articles/microservices.html). _Microservice Architectures_ , as opposed to _Monolithic Architectures_ , are those where functionally distinct software components are also deployed on separate machines or clusters. Communication between these Microservices is generally over a RESTful HTTP API or some form of RPC, allowing for individual components to be written in different languages, and have different deployment cycles, as well as the advantages listed above.

## The right tool for the job

It takes a cursory glance at [www.ec2instances.info⁠(opens in a new tab or window)](http://www.ec2instances.info/) to see that the modern day engineer is blessed with a lot of choices when it comes to _Amazon EC2_ instance types. For the _Compute Service_ , we narrowed down our choices to the _t2.micro_ type and the _c4.8xlarge_ type. The _t2.micro_ is Amazon's most underpowered, but also cheapest instance type. We were curious about how well an army of _t2.micro_ instances might perform, and how cost effective it would be. As a point of comparison, we compared against the performance of a behemoth _c4.8xlarge_ instance, weighing in at 132 ECUs across 36 cores. For reference, ECU refers to _equivalent compute unit_ , Amazon's standardised measure of clock speed across all cores of an instance. The _c4.8xlarge_ comes from Amazon's _"compute"_ category of instances, and is the beefiest therein. Somewhat unsurprisingly, engineering prevails, and we settled on neither of the two, and instead found a compromise with the _c4.large_ type.

We ruled out the _t2.micro_ by examining password hashing performance. As you are unable to distribute a single password hashing task across multiple instances, each password will end up on a single _t2.micro_ core, each of which is around four times slower than each core on Amazon's _"compute"_ type instances. Using _t2.micros_ would have given us finer grain control over machine utilisation, but at the cost of request latency for password related operations. To compare the different instance types, we measured the performance on an _m3.medium_ , and assumed the latency of the password hashing task would scale inversely with the number of ECUs per core on each instance type:

![](https://www.canva.dev/_next/static/media/img-0-bcdNAOybjhyMU3k6.c165186b.png)

We then compared the batch URL signing performance across the _"compute"_ instance types. Again, we estimated the performance on each instance type by assuming that the latency of signing a batch of URLs would scale inversely with the number of ECUs per core and the number of cores:

![](https://www.canva.dev/_next/static/media/img-0-YVnkqY1HjmnuQGln.d2ded2e9.png)

The latency of URL signing is significantly reduced when undertaken by the _"compute"_ type machines, as compared to the _m3.medium_ machines (that handle the vast majority of Canva's general purpose load). This is especially apparent with the larger types which provide a greater number of cores per machine, across which the batch signing tasks are distributed. It should be noted that Amazon's pricing scheme for these instances is linearly proportional to the ECU of each type. This means that deploying eight _c4.large_ instances (at 8 ECU each) delivers approximately the same raw computational power, at approximately the same price, as a single _c4.4xlarge_ at 62 ECU, albeit with a different hierarchy of machines and cores.

Examining existing traffic, we estimated that we only require approximately 6 ECU's of peak compute capacity to handle URL signing and password hashing tasks in Canva's immediate future. As such, we settled on deploying a single _c4.large_ instance, which provides 8 ECU's of capacity. We underestimated this (within an order of magnitude), and currently run between two and four _c4.large_ instances to handle compute tasks. Several assumptions in our modelling contributed to this misestimation. For example, we made the assumption that computational tasks could be perfectly distributed across multiple workers, when in fact there are diminishing returns when increasing the parallelism of any system. Errors were also introduced through the estimation of model inputs such as the benchmark time taken to hash passwords and sign private URLs on _m3.medium_ instances. These errors in estimation and assumption compound, adding to the misestimation in overall required capacity. We also based our calculations on historical average hourly throughput at peak times, which is less volatile than our second-to-second throughput. To ensure that we always have enough capacity to handle any spikes in this instantaneous peak demand (with some capacity to spare) we like to have auto-scaling policies that err on the side of over-deploying rather than under-deploying instances.

As we continue to grow, we look forward to exploring the use of larger compute type instances. The various compute instance types scale up linearly across capacity and price, however the larger types offer more cores per machine. This hints at opportunities to further reduce latency through increased parallelization of each request once we grow into the shoes of those beefier instance types.

## Results

We undertook load testing of our folder service (which delegates a large amount of computational work to the _Compute Service_) with the _Compute Service_ initially disabled and then enabled with a single instance in order to understand the effectiveness of delegating those tasks to separate instances. The following graph demonstrates two bursts of traffic to the folder service, first with the _Compute Service_ disabled, and second with the _Compute Service_ enabled. As can be seen, the request volume is approximately equal over the same approximate time period in both tests.

![](https://www.canva.dev/_next/static/media/img-0-8116cGiWQO8tBUQB.1681e3b3.png)

Examining the folder service latency (the middle graph), we can see that enabling the _Compute Service_ successfully reduces latency on folder requests by approximately half. This correlates with the two-fold parallelisation provided by the _c4.large_ instances (with a little bit of inefficiency a la [Ahmdal's law⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Amdahl%27s_law)), as compared with the single core _m3.medium_.

Before delving into the document service latency (the last graph) I should explain that document service is largely independent of the _Compute Service_. It is, however, served from the same instances that manage the folder service. With that in mind, you may notice the point of interest. With CDN URLs being signed locally, the burst of load on the folder service propagated across multiple services, even if those services are not dependant on those functions delegated to the _Compute Service_. This reduced coupling between services gives us greater overall systematic resiliency across Canva's backend.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.8c4d6cb8.jpg)](https://www.canva.dev/blog/engineering/trust-but-test/)

[SecurityTrust but test: Vendor security testing at CanvaHow we validate vendor security at Canva by going beyond compliance.](https://www.canva.dev/blog/engineering/trust-but-test/)

[Kane Narraway⁠(opens in a new tab or window)](https://www.linkedin.com/in/kane-n/), [CJ Fairhead⁠(opens in a new tab or window)](https://www.linkedin.com/in/chris-fairhead/)Mar 10, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.e14164be.png)](https://www.canva.dev/blog/engineering/how-to-design-in-every-language-at-once/)

[LocalizationHow to design in every language at onceThe technology that powers Continuous Localization at Canva.](https://www.canva.dev/blog/engineering/how-to-design-in-every-language-at-once/)

[Minh Cung⁠(opens in a new tab or window)](https://www.linkedin.com/in/minhcung/), [Simon Hammond⁠(opens in a new tab or window)](https://www.linkedin.com/in/simon-hammond-990250209/)Oct 20, 2021

[![](https://www.canva.dev/_next/static/media/thumbnail.76de1ae1.png)](https://www.canva.dev/blog/engineering/deep-learning-for-infinite-multi-lingual-keywords/)

[Machine LearningDeep Learning for Infinite (Multi-Lingual) KeywordsHow we used a CLIP-inspired model to suggest keywords for template labeling in multiple languages.](https://www.canva.dev/blog/engineering/deep-learning-for-infinite-multi-lingual-keywords/)

[Sachinthaka Abeywardana⁠(opens in a new tab or window)](https://www.linkedin.com/in/sachinabeywardana/)Jan 24, 2023

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


