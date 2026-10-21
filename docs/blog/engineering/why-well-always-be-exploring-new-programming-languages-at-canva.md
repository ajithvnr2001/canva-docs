---
url: https://www.canva.dev/blog/engineering/why-well-always-be-exploring-new-programming-languages-at-canva/
title: Why we'll always be exploring new programming languages at Canva - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:29.690863+00:00
---

# Why we'll always be exploring new programming languages at Canva - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/why-well-always-be-exploring-new-programming-languages-at-canva/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Engineering Processes

# Why we'll always be exploring new programming languages at Canva

Our choice of programming language has the ability to change the way we view a problem and how we interact with it.

![](https://www.canva.dev/_next/static/media/thumbnail.d96675bf.jpg)

* * *

  * 


[Josh Leeb-du Toit⁠(opens in a new tab or window)](https://joshleeb.com/)Oct 5, 2018

* * *

 _Originally published by_ [_Josh Leeb-du Toit_ ⁠(opens in a new tab or window)](https://joshleeb.com/) _at_ [_product.canva.com_ ⁠(opens in a new tab or window)](https://product.canva.com/exploring-new-programming-languages/) _on October 05, 2018._

Different languages provide different ways of modelling real-world scenarios, and can have a massive impact on the speed at which a product can iterate and scale. In this blog, Canva engineer Josh Leeb-du Toit explains why he's looking into Rust, and how exploring new languages can benefit you in the long run.

In the earlier days of Canva, our codebase was comprised of Java for the backend, and vanilla Javascript on the frontend. This approach worked well back then, but it would've been impossible to scale to the number of engineers we have now and remain productive if we hadn't adapted.

So, we introduced some changes to our tech stack. We switched out Javascript for Typescript with React, introduced Kotlin and Swift for our mobile apps, and added others for specifically selected purposes, such as Scala for our data science and machine learning team. We haven't been afraid to make these changes and it has allowed us to scale and evolve while remaining productive. We've needed to adapt our tech stack in the past, and we may have to change parts of it again in the future. There will always be isolated problems that our current tech stack can't solve, and blind spots in the conceptual models that our current languages offer.

For all of these reasons, it's important for us to keep exploring new languages, so we have the knowledge that will help us adapt. In this article, I'll talk about developing a culture of exploration around new languages and technologies, and the benefits that this brings.

## Developing a culture of exploration and knowledge sharing

Before anything else, it's important to encourage everyone to adopt a culture of exploration. By exploration, we mean tinkering with ideas and concepts that may, or may not, make an impact to the company's bottom line. By investing the time to explore new options and technologies, we are exercising diversity of thought, which may potentially reap huge rewards down the line.

As well as the languages we use every day at Canva, we're exploring many new languages on the side. There is a strong interest around Canva in many of these nascent languages and we seldom explore them in isolation. Clubs have been forming around these younger languages, like Go and Elixir.

There are Slack channels for those interested in functional programming, and we have groups meeting after work to explore these languages together. [Canva's engineering culture](https://www.canva.dev/blog/engineering/scaling-engineering-at-canva/) values constant learning, and these clubs, regular frontend and backend forums, and hosted tech talks are all part of a culture of exploration and constantly improving engineering.

I've been looking after Canva's Rust club for a while now. It started in the first months of 2018 with only 4 people. Now we're up to 24 on Slack and have been holding weekly sessions after work to talk and do all things Rust.

![](https://www.canva.dev/_next/static/media/img-0-sPNFdFfTefqZaK-Q.304e7ed7.jpg)

Rust Club Weekly Meetup

We've worked on a decentralized chat program, an NES emulator, and now we're looking at embedded projects, fonts, and tooling to 10x our developer efficiency.

![](https://www.canva.dev/_next/static/media/img-0-4R1Ao17pYX6dJhIX.5bccd2ba.png)

NES Emulator Test Output

**How we're fostering a culture of exploration and knowledge sharing**

**Clubs** are a great way to bring like-minded individuals together to deep dive into a particular shared interest — in this case, we chose to launch a Rust club at Canva. With such a diversity of interests at Canva we (almost) have a club for everything. From functional programming, to rock climbing, to baking, each of these clubs are devoted to exploration and knowledge sharing about their respective topics.

**Engineering forums** are another way we regularly discuss and explore new topics even if they aren't related to the core product. Each week we alternate between a forum for backend engineering, and one for frontend engineering. Of course frontend engineers can also attend the backend forum, and vice versa. Our engineers use this opportunity to share what they've been working on and thinking about, and it doesn't have to be directly related to our core product. Often a talk will be about a new technology that could be slowly making its way into our tech stack.

Focusing more on exploration external to Canva, we also regularly host **meetups and talks**. In the past we've hosted SydJS, Rails Girls, talks on functional frontend programming, TypeScript (before it was deployed as part of the Canva editor) and many others.. These events provide all engineers, not just Canva engineers, to explore new languages and tech and gain new ideas and insights.

Along the way, we learned how to foster a culture of exploration and knowledge sharing; here are some the methods we adopted.

  * **Establish from the get-go that all learning is good.** 'We are constantly learning' is one of our engineering values at Canva, and we try to live by that. When everyone comes into the room with the same mindset that "all learning is good", what tends to happen is any participation anxiety is alleviated, providing a safe and welcoming space that encourages curiosity.
  * **Don't make statements — ask questions.** Open-ended questions encourage everyone to come up with unbiased hypothesis and exploration. So instead of a meeting agenda, try replacing each discussion point with questions instead.
  * **Reward boldness.** : It's important to recognize that every idea and potential solution is justified, and more out of the box thinking can be difficult for many people to put out there. Whether it's by recognizing the most creative/random/obscure idea with a certificate or just a shout out — you'd be surprised at how it can encourage people to step out of their comfort zone.



## The Benefits

While there are plenty of languages that we're looking at, I'm not expecting all, if any, to be used everyday for mission critical software. Some haven't been battle tested and others are still young and changing.

But the act of exploring and knowledge sharing has some very immediate benefits, which I'll delve into below.

### 1\. The ability to use the right tool from an expanding toolbox

It can be useful to think of programming languages as tools, like a hammer or a wrench. It's what we use to develop, maintain, and extend software programs.

To continue with this analogy, if you're about to start putting together some furniture it makes sense to have a good idea of the tools available. You don't want to go into it only knowing one or two because when you encounter a screw… I imagine it would be quite a challenge to screw it in with a wrench.

This applies to software development as well. If you need to store some data it's necessary to know what databases are out there. With this in mind, when writing a program it's important to do the same analysis. If your program needs to be built quickly and easily maintained then you may go with one language, and if it needs to scale super well and have an uptime of 99.99999% there might be an alternative, better choice to consider.

#### Case study: Changing technologies at Canva

The switch from vanilla Javascript to Typescript with React has been the biggest change to our tech stack so far. When Canva's editor was first built it was pure Javascript which allowed us to build out the core editor really quickly with a small group of engineers. Over time, we brought on more engineers, and the codebase, features, and modules all grew exponentially. Scaling in all these directions slowed down the development of the editor and what was a benefit of our tech stack became a huge drawback. This prompted us to build Canva 2.0 and the new editor experience. Now built with React in Typescript it allows more developers to be more productive and ship out even more features, fixes, and improvements.

The properties of each language will mean that it will lend itself to solving a specific class of problem. Ask any engineer and they'll tell you that using Bash to write a web frontend is not a great idea. But on the other hand, Javascript definitely has its drawbacks when it comes to composing shell commands.

At Canva, we tend to work with Java and Typescript, but that's not the only code committed to our repos. We are writing everything from Python and PHP, to Scala and Swift. Each language is carefully selected to help us develop solutions for a specific area of the product.

There's no silver bullet. A language will never be the best at everything. There are some more general purpose languages like Java and C++, but you can be certain they have their drawbacks as well. It is important to know your programming toolbox, and by having experience with many languages you are immediately in a better position to select the best language to solve your problem.

### 2\. The ability to change the way you think, for the better

There's another benefit to exploring new languages. The act of learning and thinking in a different way will make you a better problem solver.

Programming languages are how we represent real world problems to computers. To do so we need to break down the problem into smaller pieces and then figure out how best to join them together for the computer to understand.

Depending on the language and the problem, the pieces and the way they look can be very different. Let's use the example of a car and how we could represent that in two different ways.

If we want to represent the car in a language like Java we would likely break it down into its object parts: into its engine, wheels, and pedals. Then each of these would be an object and we could perform actions on them to change their data. For example, if the engine is turned on, we will record that within the engine object.

Now for a language like Haskell, rather than focusing on the objects we focus on the actions. We would have an action for turning on the car, pushing in the accelerator pedal, and stepping on the brakes. Then these actions get given some data to act on and they respond with new data, such as how far the pedals are pushed in.

These are two different ways of solving the same problem. If you only knew the former representation, then everything may appear to be an object. But if you only knew the latter then everything is an action.

![](https://www.canva.dev/_next/static/media/img-0-bo59LqGWax5zA4mP.208f954d.png)

_Diagram of object (Java) representation of a car_

![](https://www.canva.dev/_next/static/media/img-0-Iv1N77lj2TUXpOfX.91106c78.png)

_Diagram of action (Haskell) representation of a car_

These representations go further than telling a computer what something is — they point to completely different paths for arriving at the same solution.

By learning to break down problems and think of solutions in different ways, you expand your problem-solving mind. I often find myself thinking about how I would solve a problem in a completely different language, even though I'm coding in Java. And I'm certain it has made me a better problem solver.

### Final thoughts

There are definitely trade offs when deciding to explore and learn a new language. It doesn't happen overnight — in fact, it can take many weeks to progress beyond beginner level. However, at Canva it is clear the benefits are understood. Constantly exploring new languages and expanding our toolbox allows us to think about problems in new ways, and even adapt our core technology when we need to. So we'll continue looking at new technologies and applying them to big problems and crazy new goals as we grow.

_For more details on our current job openings, visit Canva's careers page_ [here ⁠(opens in a new tab or window)](https://careers.canva.com/).

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.eeec7a21.png)](https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/)

[Quality AssuranceHow We Used Data to Optimize Our Quality Assistance ModelFrom firefighting chaos to problem solving zen.](https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/)

[Zi Yang Pang⁠(opens in a new tab or window)](https://www.linkedin.com/in/pangzy/)Aug 29, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.be3489f2.png)](https://www.canva.dev/blog/engineering/supporting-gpu-accelerated-machine-learning-with-kubernetes-and-nix/)

[Machine Learning InfrastructureSupporting GPU-accelerated Machine Learning with Kubernetes and NixIt ain't what you don't know that gets you into trouble — well, sometimes it is.](https://www.canva.dev/blog/engineering/supporting-gpu-accelerated-machine-learning-with-kubernetes-and-nix/)

[Jonathon Belotti⁠(opens in a new tab or window)](https://github.com/thundergolfer)Jul 5, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.c69dca35.png)](https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/)

[Data AnalyticsMeasuring Commercial Impact at Scale at CanvaHow We Built Canva's IMPACT App with Streamlit in Snowflake](https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/)

[Jun Ye⁠(opens in a new tab or window)](https://www.linkedin.com/in/jun-ye-0798/)Jun 20, 2025

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


