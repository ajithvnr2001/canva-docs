---
url: https://www.canva.dev/blog/engineering/scaling-engineering-at-canva/
title: Scaling engineering at Canva - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:16.135516+00:00
---

# Scaling engineering at Canva - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/scaling-engineering-at-canva/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Engineering Practices

# Scaling engineering at Canva

Canva's first Head of Engineering shares lessons learned from Google and Lyft to scale our engineering culture at Canva.

![](https://www.canva.dev/_next/static/media/thumbnail.75b1df18.jpg)

* * *

  * 


Joel HynoskiJun 20, 2018

* * *

 _Originally published by Joel Hynoski_ _at_ [_product.canva.com_ ⁠(opens in a new tab or window)](https://product.canva.com/scaling-engineering-at-canva/) _on June 20, 2018._

_"It's not just about scaling from 50 to 100 engineers. It's not even about scaling to 200. I'm thinking about how we can scale to 1000 people and beyond."_

This was the mission Cliff Obrecht (Canva co-founder and COO) set for me when I first sat down with him. It seemed like a crazy idea. At the time, we had just over 40 engineers, and were three and a half years into the Canva journey. I was being recruited as the first ever head of engineering.

This might be one of those magical situations where everything falls into place, I thought. The right product at the right time, with the right people to build it. There's no reason why we couldn't reach a thousand engineers. But how would we preserve the magic as we split into different teams, disperse across office floors, buildings — and even countries?

At the start of the journey, a small and dedicated fellowship ventures out on the quest. They know what they stand for, and they'll do whatever it takes to get the job done. Every day is a learning experience. As more and more people join the mission though, how do you know what everyone stands for? How can one person feel empowered to set a new direction, and how do you realize the potential of every person?

While I don't claim to have all the answers, I've been in a lucky position to witness the growth of a few notable companies-Google from 2006—2013, and Lyft from 2015—2017, for example-and I've got a few ideas. From the 47 engineers we had at Canva when I joined in March 2017, we're now at over 120, and I think we're doing OK. This is very much a journey in progress. In this article, I'll share a few of the things we're doing at Canva to scale our engineering culture and processes.

## Our engineering values

The core of an awesome, united team is a small set of shared understandings. This doesn't mean a team powered by groupthink. What you want is a motley crew with a small set of common beliefs, which everyone is proud to hold-and perhaps stick onto their laptops.

![](https://www.canva.dev/_next/static/media/img-0-rp_2isWYITlQA6uB.b95aa910.jpg)

An engineering team planning session

With 5 or 10 people, you can develop common understandings just by sitting around a table all day together. But when it comes to 40 or 50 engineers, the point at which I arrived at Canva, it's definitely a different story-one worth committing to in some form of writing. Without a common set of values for how we approach engineering, I could see we would end up with big disparities between teams. Some would be following more effective practices, others less so. Some would be fostering one culture, others something different. People wouldn't know what it meant to be an engineer at Canva.

When I joined, we had some nascent ideas about ['how engineering is done here'](https://www.canva.dev/blog/engineering/how-we-get-things-done/), but they were fairly amorphous. Everyone knew we were aiming for 'excellence in engineering', but not everyone was aligned in what this meant, or had different interpretations of that idea. So while we already had a lot of good processes and teamwork in place-our code review culture was already very strong, for example- we needed to make sure the foundation was solid and included only practices that we wanted to maintain. So about a month after I joined, I started to scope out a set of engineering values for the team.

How do you go about setting up and establishing team values? In my first engineering-wide email on the subject, I introduced it like this:

> _Rather than impose a set of values on you all, I wanted to chat about some of the proposed ones that we could embrace, and get suggestions on how to word them, or add more, or subtract them-whatever we decide._

It would have been easy enough for me to meet with a few of Canva's earliest engineers, and pull together a list of values based on our observations. Instead, I committed to work out our values collaboratively, together with the team-however long that took.

Why did I decide to do it this way?

**Ownership.** It goes almost without saying that if the team creates a set of core values for themselves, they're more likely to truly own them.

**Common knowledge.** While this idea is a little trickier to grasp, among [logicians⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Common_knowledge_\(logic\)) this is actually a technical term. Common knowledge is what everyone knows that everyone else knows. It's a kind of infinite recursion. You know something, you know that I know something, you know that I know that you know it, and so on. Anything less than this is simply referred to as 'shared knowledge'-the knowledge is generally diffused throughout the group, but no-one is perfectly sure of who knows what.

Research using [game-theory models⁠(opens in a new tab or window)](https://news.harvard.edu/gazette/story/2015/03/understanding-common-knowledge/) shows us that common knowledge makes a big difference when groups collaborate. Having a bedrock of understandings that can be assumed and rallied around without extra communication overhead makes groups much more efficient. In the case of common values, it's no different. People have a common vocabulary-so today if people refer to being 'pragmatic' during a code review, everyone knows what that means in terms of our value 'Aim for pragmatic excellence'. No one has to justify why they're taking time to teach a newbie, because of our value 'Take the time to teach each other'. If people want to change teams, they know they won't need to learn a new set of working principles.

But common knowledge is much harder to achieve than you'd think. Because it requires that everyone know what others know, it requires confirmation and clarification in a group setting, ideally a face-to-face setting. Unfortunately, you can't just tell people what the team values are over Slack. So that's where it helps to generate common values collaboratively. That way, you can be sure they really are commonly held.

![](https://www.canva.dev/_next/static/media/img-0-Vwo75W5YouWDMhhq.ebd591ca.jpg)

Editor team meeting

Here's how we did it at Canva:

**Brainstorm.** Ideas are hard to generate in a vacuum, people need other ideas to bounce off. We all got together and spent some time generating post-its and discussing what engineering stood for at Canva. This gave us a shortlist of about 35 draft values.

**Collate.** If people have similar ideas, that's a good sign. We had a lot around learning, for example 'keep getting better at your craft' or 'we're always learning'. I worked with a couple of people to consolidate our draft values into 22 different themes.

**Workshop.** In cohorts of 15—20, we voted on the values (the values were written on a whiteboard, and everyone had tally marks to allocate to their favorites). We then split into groups of 3—4, made Canva presentations around the most popular choices and presented them back to the cohort. This brought us down to 12 draft values. _Note: In written form, a value is just a few words-so it's important to generate some interpretation around them like this and capture the intent._

![](https://www.canva.dev/_next/static/media/img-0-Cemp0JpOi51MTD_z.628300f4.jpg)

**Vote.** The basic acceptance criteria for a value is whether it resonates with the team. So there's no harm in eliminating a few 'correct' but less popular options. We chose our final set of values using a simple Google form, with the header "Don't decide which presentation is the best, but instead which values resonate the most with you."

And just like that, we had a set of values. No further convincing or buy-ins were necessary, because we'd taken the time to involve everyone in the process. Canva's engineering values:

***A warning about the democratic process**** : Some values might sound great to the majority of your team, but still alienate others. It's important to remind people throughout the process that values should be inclusive, as well as inspirational.*

  * We are constantly learning
  * Focus on the user
  * Aim for pragmatic excellence-ship early, ship often
  * Take the time to teach each other
  * Validate the problem, embrace rethinking
  * Evaluate ideas based on merit-trust in people's best intentions
  * Keep testing your ideas
  * Constantly improve engineering



Of course, the ownership and common knowledge of these values might diminish over time as more engineers come on board. And values that served us in the past might start to hamper our growth today. But who said values need to be set in stone? I plan to revisit the values periodically with the team, following a similarly collaborative process to the one I mentioned above. I doubt we'll change them wholesale, but I'm open to that if necessary.

## Distributing responsibility

![](https://www.canva.dev/_next/static/media/img-0-qJcGRCxG3ouBhhjc.ad175b90.jpg)

We want to preserve the awesome minimum viable structure and culture of responsibility that we have at Canva. However, that's not an easy thing to do as we grow close to 50 teams. To keep the structure of our engineering group as flat as possible, we want to empower every team and minimize their dependence on formal leadership.

![](https://www.canva.dev/_next/static/media/img-0-8g_HYrE4_O0RgsbX.1974eece.jpg)

To do this, we've defined the things that each team needs to be doing, and collected them into a set of functions. These are roles that need to be fulfilled on each team, but the people that fill them during each 'Season' (three month period) can change. To keep with the metaphor of each team as a small, independent fellowship setting out on a journey with each a new goal, we envisage these roles as 'backpacks'.

![](https://www.canva.dev/_next/static/media/img-0-NZc9Wulbgur8SqqZ.2ce6e6f3.jpg)

Breaking it down, the first backpack is Coaching. The capacity of our engineering leadership to provide 1:1 time and support is quite limited. So it's important that we hand out lots of these backpacks to people with appropriate experience.

![](https://www.canva.dev/_next/static/media/img-0-_U0wqcivdoLuiwRt.2be6fbbe.jpg)

Next is Facilitating. It's important that every every team stays goal-oriented and everyone has the right work assigned. This is the role of the facilitator.

Finally, there's the Navigators. They're like the wise guide of the group-mentoring new people in the ways of the team, setting the technical directions, and making sure the code is up to scratch.

Each 'backpack' has its own set of tools that it carries. 'Facilitating', for example, has things like project planning, using Jira, running retrospectives and reporting. While 'Navigating' has mentoring and giving feedback. Although there are a number of premade 'backpacks', we constantly encourage everyone to put whichever tools they may need or feel comfortable with in their own pack.

"Wait, are these backpacks just hierarchy by another name?" you ask. "Is a 'tech navigator' just a tech lead after all?" In a way, that's the role they fulfill. But the emphasis here is very important. Naming them this way helps people understand that they are responsibilities, not fixed roles. Responsibilities can be shared, and when a backpack gets heavy, someone else can shoulder the load. In some cases the contents of two packs can be combined, and someone can take on multiple responsibilities. In other cases they can be separated, and two people can do a job. Canva is growing so quickly that there will be responsibilities and possibilities for anyone who wants them. It's about keeping the engineering culture of a startup-so anyone can reach out and take on tasks. With green fields of opportunity and growth all around us, we need everyone to have that sense of urgency.

## Scaling our culture of learning

With so many new people coming on board, getting new team members up to speed is one of the most important things we do at Canva. However, there's a few problems we have to contend with: Canva's codebase is large, and so far we've prioritized shipping over documentation. A lot of responsibility has been placed on mentors, who've been doing a great job-but as a complete solution it's not scalable.

At Canva, we definitely have a culture of learning. Some of the core values chosen by the team include 'Making sure we are constantly learning', 'Take the time to teach each other', and 'Constantly improving engineering'. I see people striving to learn new things every day. There's no problem with creating a culture of learning; the key thing is ensuring we scale that culture.

![](https://www.canva.dev/_next/static/media/img-0-TY4yhzbUJrPTWoiQ.3d6e2fad.png)

Here are some of the things we've been working on with regard to scaling a culture of learning:

## Skills journeys

The image above sums up what we're hoping to achieve with learning and development at Canva. We don't want a ladder with a few rungs, so that our people skill up and then do the same thing forever. We don't want a rung-less ladder, where the support for learning just isn't there. We want our people to be able to continuously learn-the company is always growing, and as such we want our people to able to grow with it.

But rather than just hoping that limitless learning will happen, we've been formalizing what we call 'skills journeys' for every specialty within Canva.

A kind of framework, the engineering skills journey is based around five characteristics:

  * Code contributions
  * Effectiveness
  * Technical design
  * Communication
  * Culture



Just having a framework for learning like this is very important. People often used to come to me wanting to improve their skills, but not knowing where to start. By having these journeys set up, people are now able to see for themselves "this is where I am on the journey now, and to get to the next level I need to be doing these things".

Learning is supported by four internal partners:

  * A specialty lead
  * Canva University (see below)
  * Team Happiness (Canva's HR)
  * Our new internal coach



## Canva University

![](https://www.canva.dev/_next/static/media/img-0--lqBW1S96fbf6VYs.b4b4f550.jpg)

The idea for 'Canva Engineering University' is to provide a curriculum and peer-to-peer education to Canva engineers. A part of a wider 'Canva University' strategy we're rolling out in the coming months; this allows us to successfully [onboard newbies⁠(opens in a new tab or window)](https://product.canva.com/onboarding-new-hires/), develop their skills, and learn new skills. Having an internal 'University' means we are all able to work more effectively, and empower others to do their work.

Engineers will be able to find both in-person and online courses with the recorded content they need, when they need it. Courses will include things like 'An introduction to internal tooling', 'PR best practices', and 'Design React Components'. We've recently hired Dianah Ward, our Learning and Development Specialist who is working on rolling out the program, so watch this space!

## Final thoughts

It's early days yet, but we've seen a lot of positive results from introducing our engineering values, distributing responsibility, and building out our skills journeys. Every day I see that our values are being taken to heart and helping people to think about their daily work in new ways.

Take our value 'Validate the problem'-which is all about making sure you're solving the right problem, not just making sure you're solving the problem right. When engineers get a request from a PM or a designer, instead of just going away and crunching out code for it, I hear them asking what it's for and really trying to understand and validate the product thinking behind the feature. Likewise among engineers, our value 'Aim for pragmatic excellence' is really being taken into the culture. Pragmatic excellence is about building a minimal feature set and getting products shipped, while still balancing that with long term needs and scalability. Nowadays during code reviews it's more common to hear people say "Are we over-engineering this? Could we build less now and do more later?".

Another important value has been 'Evaluate ideas based on merit'. At a startup it can be easy to idolise the ideas of the early engineers-they've built the core code of the product, and they have a large personal stake in the company. It's easy to fall into thinking that their opinion means more than yours, if you've only been around for two months. But I see this value freeing people up-everyone knows that regardless of their tenure at Canva, people will respect their ideas and evaluate them objectively. That's helped a lot with onboarding, because new engineers know that their ideas will be taken seriously, and feel free to question the status quo-which is what we need to do, in order to continue growing engineering.

There's less tangible benefits from the values as well, like the cohesion of the engineering team. Even though we're now split over three floors and many different projects, the way we work together is very consistent. There's room for individuality among teams, but there is also alignment with a general vision and working style.

Our Canva University is still in progress, but I see our skills journey framework being used often. People use it as a way to benchmark their own progress, and say "This is where I am today, this is where I want to be, and this is how I'm tracking". It's very empowering to be able to measure and steer that process of growth. In the end that's what it's about-from choosing the values, to distributing responsibility, to setting up the skills framework-it's about empowering people and giving them control over their own journey at Canva. I'm confident that we're keeping the core of Canva's great engineering culture as we grow. Things will change, and there will be new challenges on the way, but our culture will scale to meet it.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.be3489f2.png)](https://www.canva.dev/blog/engineering/supporting-gpu-accelerated-machine-learning-with-kubernetes-and-nix/)

[Machine Learning InfrastructureSupporting GPU-accelerated Machine Learning with Kubernetes and NixIt ain't what you don't know that gets you into trouble — well, sometimes it is.](https://www.canva.dev/blog/engineering/supporting-gpu-accelerated-machine-learning-with-kubernetes-and-nix/)

[Jonathon Belotti⁠(opens in a new tab or window)](https://github.com/thundergolfer)Jul 5, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.7caec38f.png)](https://www.canva.dev/blog/engineering/testing-search-engine-optimization-scalably-without-breaking-a-sweat/)

[Search Engine OptimizationTesting Search Engine Optimization Scalably without Breaking a SweatScaling pre-development, rollout, and post-production SEO testing at Canva.](https://www.canva.dev/blog/engineering/testing-search-engine-optimization-scalably-without-breaking-a-sweat/)

[Siddharth Salunke⁠(opens in a new tab or window)](https://www.linkedin.com/in/siddharthsalunke/)Jun 20, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.5e4abe46.png)](https://www.canva.dev/blog/engineering/understanding-a-diverse-user-base-with-frequency-segmentation-at-scale/)

[Data-Driven SegmentationUnderstanding a Diverse User Base with Frequency Segmentation at ScaleHow we developed a bespoke frequency-recency segmentation to understand our users' diverse usage patterns.](https://www.canva.dev/blog/engineering/understanding-a-diverse-user-base-with-frequency-segmentation-at-scale/)

[Cuong Duong⁠(opens in a new tab or window)](https://www.linkedin.com/in/cuong-duong-351b5ab4/), [Naomi Stuart⁠(opens in a new tab or window)](https://www.linkedin.com/in/naomistuart/)Mar 16, 2023

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


