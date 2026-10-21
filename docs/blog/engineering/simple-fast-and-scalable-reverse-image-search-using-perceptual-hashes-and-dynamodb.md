---
url: https://www.canva.dev/blog/engineering/simple-fast-and-scalable-reverse-image-search-using-perceptual-hashes-and-dynamodb/
title: Simple, Fast, and Scalable Reverse Image Search Using Perceptual Hashes and DynamoDB - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:16.546924+00:00
---

# Simple, Fast, and Scalable Reverse Image Search Using Perceptual Hashes and DynamoDB - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/simple-fast-and-scalable-reverse-image-search-using-perceptual-hashes-and-dynamodb/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Image Hashing

# Simple, Fast, and Scalable Reverse Image Search Using Perceptual Hashes and DynamoDB

How we built our first iteration of content matching at Canva.

![](https://www.canva.dev/_next/static/media/thumbnail.699fbc58.png)

* * *

  * 


[Christopher Bong⁠(opens in a new tab or window)](https://au.linkedin.com/in/christopherbong)Oct 16, 2022

* * *

Canva hosts a huge collection of ever-growing, user media that needs to be stored and managed properly. The diversity of this media poses challenges around the moderation and reduction of unnecessary duplicate content. To cater to this, one tool we use is perceptual hashing with an internally built reverse image search system.

This blog post describes the design and process we went through to build such a system to the scale of Canva.

## Hashing

Hashing is one simple way of implementing a reverse image search. A hash function is an algorithm that maps data to unique fixed-sized values called hash keys, which are represented as strings. Common hash algorithms include [MD5⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/MD5) and [SHA⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms).

The ability to map any file into unique hash keys is useful for matching duplicate content _but is not very viable in the case of images_.

For instance, you could implement a simple reverse image search in an image library using the image file hash key as a primary key in a database.

In the example below, we have two visually duplicated images (IMAGE_1 and IMAGE_2) whose SHA512 hash keys are the primary keys in a DynamoDB table, and their image IDs are the secondary keys.

![Hash keys using SHA512 for two visually duplicated images IMAGE_1 and IMAGE_2. Note that the hashes are completely different.](https://www.canva.dev/_next/static/media/img-0-zisXnPvVf1hcy_Nw.75c7a9e1.png)

Hash keys using SHA512 for two visually duplicated images IMAGE_1 and IMAGE_2

Even though the images are visually duplicated, it is evident that their hash keys can be totally different, even if there is a single pixel of difference.

In an image library, multiple images are visually similar but can have minor quality or metadata changes. All of these images will have different hash keys. Hence, a reverse image search using simple hashing is only useful in the context of perfectly duplicated images.

## Perceptual hashing

![Two photos of sushi side by side with their MD5 hashes below each. The right photo has been modified with a watermark.](https://www.canva.dev/_next/static/media/img-0-U-WfEw5AmPtE8FS2.45a7c656.png)

_An image with a small watermark applied to it, completely changing its hash_

While cryptographic hashes like SHA512 create hashes of raw bytes, perceptual hashes are created based on the actual pixels of an image. Perceptual hashes change along with the visual change in the images. Hence, a reverse image search using perceptual hashing can be done by calculating the [Hamming distance⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Hamming_distance) between the two hashes.

Perceptual hashing algorithms can use various transformations and some are more effective for matching different image types like photos or vectors. For this blog post, we'll use as an example the [pHash⁠(opens in a new tab or window)](https://www.phash.org/) algorithm since it produces shorter hashes that are easier to use in examples.

![Two photos of sushi side by side with their PDQ hashes below each. The right photo has been modified with a watermark.](https://www.canva.dev/_next/static/media/img-0-05BJpcJf93qDkoS1.20a19750.png)

The original image above is modified with a watermark. Since it's a minimal modification, there is only a small Hamming distance of 2 between them. With more changes, there would be a larger Hamming distance. If there were no modifications, their hashes would have a Hamming distance of 0. Perceptual hashes and Hamming distances can be used to build a system that can find modified images.

## Matching perceptual hashes

A perceptual hash matching system can use a hash and a Hamming distance as input. The system output would be all the stored hashes within that Hamming distance. The previous example cannot be used to create this system as it only supported matching if hashes are equal. Allowing this query type needs a different data structure. In addition, the system should have the right level of precision and recall. The ideal is to have higher precision and avoid false negatives.

To do this we implemented an algorithm called multi-index hashing ([Norouzi, 2012⁠(opens in a new tab or window)](http://www.cs.toronto.edu/~norouzi/research/papers/multi_index_hashing.pdf)) on top of DynamoDB tables. The algorithm involves splitting the query hash and stored hashes into segments (more on this later). This solution was chosen because it is able to guarantee finding hashes for a given Hamming distance at high scale. Here's an example of what the entries in the database could look like for a perceptual hash:

![A table with entries of a DynamoDB table. There are four rows and three column. The first column is partition key of each being one part of the split hash. The second is the hashed image. The third is the row number.](https://www.canva.dev/_next/static/media/img-0-cLMsDLIRCIsuUBgT.97def0a3.png)

The hash is split into 4 parts, with each key prefixed with the index of that part. The same split is done on the image at query time to compare. The image id is the sort key for uniqueness between duplicates.

![A diagram of a query hash being split into 4 DynamoDB queries.](https://www.canva.dev/_next/static/media/img-0-MgYTJd_LJ-WikQ4S.74a7dc6f.png)

With the four hashes, four separate DynamoDB queries are run. Then, a consolidation step is run on the results to remove duplicates and filter out hashes with a Hamming distance higher than the threshold.

## Insights

This solution can find similar hashes with the runtime of a DynamoDB _GetItem_ query. However, its effectiveness depends on the hash split count and the nature of the images. In particular, the hash split count was one of the critical decisions that had to be made and was why the implementation was unusable at rollout.

In the above example, the hash is split into 4 parts. With a 4 split, it is guaranteed that all results with a Hamming distance of 3 or less can be found. This is due to the [pigeonhole principle⁠(opens in a new tab or window)](https://math.hmc.edu/funfacts/pigeonhole-principle/). For example, if there are _n_ slots that the hash is split into, and _n — 1_ character changes to distribute, it is guaranteed that at least one of the slots has no characters changed.

![A diagram of a hash being split into 4 windows and 3 modifications represented as dots. Each dot has an arrow pointing to a separate window.](https://www.canva.dev/_next/static/media/img-0-I-E2TGipD16_41Ph.c336d88e.png)

This is how there is a guarantee of finding all results within a Hamming distance threshold. Naturally, one might pick a high slot count for supporting as large a range as possible. However, increasing this number had two significant implications for the results:

  1. The result set increased, and
  2. The number of matches with high Hamming distances increased.



Immediately after rollout, there were issues that caused the system to be unusable. Queries took minutes to run, used 20x more read capacity than expected, and returned very few results. DynamoDB queries were returning an excessive amount of results that were all filtered out in the consolidation step.

Investigating the queries and their results revealed two interesting insights:

  * For one, it was common for users to upload duplicates of the same image. This meant the uniqueness distribution for images was not as unique as initially expected, leading to more results per search.

![A cropped screenshot of the Canva uploads page where 5 of the images are the same but slightly modified.](https://www.canva.dev/_next/static/media/img-0-sy7rdcr12odEXwNg.001b1e1b.png)

_A sample of what my (and probably many other users) uploads look like in Canva_

  * The other problem involved the hashing algorithm. The perceptual hash being used produces fairly uniform hashes for non-complex images like single-colored shape vectors (i.e., `AAAAAAAA`). This meant that many vectors in our database had the same partition keys. If any query hash matched a slot with these uniform hashes, 100000s of vector hashes would be returned in the result set.

![Colored boxes that inflated our search results to the point of unusability. Three colored boxes are shown with slightly different dimensions and completely different colors. From top clockwise: a green box, a yellow box and a light pink box.](https://www.canva.dev/_next/static/media/img-0-Jf3leeVL8xVCmsfj.11fd7e05.png)

_Colored boxes that inflated our search results to the point of unusability_

To fix these issues, two changes were made:

  * First, the window count was reduced 4x to reduce the number of results that the system filtered. After each reduction, tests were done to ensure that no relevant image matches were lost.
  * Then we chose to skip hashing low-complexity images. These were easy to pick out because the hashes generally consisted of a single character like `AAAAAAAA`.



These changes reduced the number of rows returned from 100000s to 10s for all the previously problematic queries, fixing the issues that occurred on roll-out.

## How well does it run?

Some of the highlights of the system are:

  1. Hashes for over **10 billion images** in DynamoDB.
  2. Average query time of **40ms** , p95 at 60ms.
  3. Our peak workload is in excess of 2000 queries per second, with no performance degradation at that utilization, which maps to ~10k DynamoDB RCU capacity.
  4. Catches watermarking, quality changes, and minor modifications.



## Applications at Canva

We've already been leveraging the system for various use cases at Canva. One use case comes from the sheer amount of media that is stored which is comparable to most large media-based tech companies. This comes with a significant cost in the form of storage, with deduplication of bytes as a means to reduce this.

Since we now have an image hash table, we can analyze the number of unique hashes and determine the deduplication percentage of all our images. This can even be extended to identifying "similar" images as well, finding those instances of light modification.

For content moderation, a system operating on perceptual hashes gives us the ability to quickly act on known illegal, graphic, or dangerous media across our dataset. This means that we can action media takedowns at scale in a matter of seconds with tooling, rather than manual intervention.

## What's next?

Perceptual hashing is only one tool in the toolkit for managing a large media footprint. Its functionality is only just being explored at Canva and we look forward to improving hit rates against other transforms such as images within images.

### Acknowledgements

Huge thanks to everyone in the media platform team for helping to get this project through. Special thanks to:

  * [Jacky⁠(opens in a new tab or window)](https://au.linkedin.com/in/junjie-chen-78b1a796) for coaching and supporting me throughout the project
  * [Oliver⁠(opens in a new tab or window)](https://www.linkedin.com/in/oliver-richards-7ba063150/) for helping with the implementation and for co-owning the service



[Michael⁠(opens in a new tab or window)](https://www.linkedin.com/in/cloudjunky/) and [Raymond⁠(opens in a new tab or window)](https://www.linkedin.com/in/rayschippers) for providing their security perspective and expertise.

_Want to work on scaling media storage and access at Canva?_ [_Join us!_ ⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/)

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.5df784be.png)](https://www.canva.dev/blog/engineering/behind-the-scenes-of-canvas-designdna-campaign/)

[Machine LearningBehind the scenes of Canva's DesignDNA campaignHow we used generative AI to build our year-in-review campaign](https://www.canva.dev/blog/engineering/behind-the-scenes-of-canvas-designdna-campaign/)

[Divya Patel⁠(opens in a new tab or window)](https://www.linkedin.com/in/divyapat1/)Feb 24, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.516cfa0d.png)](https://www.canva.dev/blog/engineering/css-absolutely-positioning-things-relatively/)

[CSSCSS: Absolutely positioning things relativelyUsing CSS grid to render complex webpages responsively.](https://www.canva.dev/blog/engineering/css-absolutely-positioning-things-relatively/)

[Benjamin Morris⁠(opens in a new tab or window)](https://www.linkedin.com/in/benjamin-morris-38bab620/)May 25, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.b4b4f550.jpg)](https://www.canva.dev/blog/engineering/how-we-get-things-done/)

[Engineering PracticesHow we get things doneThis post is our attempt to describe the practices we've found help us work more efficiently as a team.](https://www.canva.dev/blog/engineering/how-we-get-things-done/)

David HearndenAug 25, 2015

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


