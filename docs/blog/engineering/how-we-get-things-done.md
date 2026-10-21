---
url: https://www.canva.dev/blog/engineering/how-we-get-things-done/
title: How we get things done - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:14.090035+00:00
---

# How we get things done - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/how-we-get-things-done/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Engineering Practices

# How we get things done

This post is our attempt to describe the practices we've found help us work more efficiently as a team.

![](https://www.canva.dev/_next/static/media/thumbnail.b4b4f550.jpg)

* * *

  * 


David HearndenAug 25, 2015

* * *

 _Originally published by David Hearnden at_ [product.canva.com⁠(opens in a new tab or window)](https://product.canva.com/how-we-get-things-done/) _on August 25, 2015._

As the Canva engineering team [continues to grow⁠(opens in a new tab or window)](https://about.canva.com/careers/), we've started to codify some of the "tribal knowledge" that previously went unspoken. This post is our attempt to describe the practices we've found help us work more efficiently as a team. It's been really useful so far as a survival guide for new engineers, so we thought we'd share it. This isn't meant to be a prescription for every team; it's just what works for us.

The important parts break down nicely into three categories:

  * _Practices_ — how we get things done
  * _People_ — how we get things done with others
  * _Principles_ — how we approach problems



## Practices — how we get things done

### Monday planning

Every Monday, each feature team lays out the rough trajectory of work for the week in a JIRA sprint. Each of our deployable components has a baseline weekly release cycle synchronized with these sprints (some components release more regularly on top of that baseline). These sprint planning meetings are the primary means for communicating the latest priorities. We try not to get too hung up on the specifics of formal agile processes, but it's a familiar practice to anyone who's experienced agile before.

Related trivia: We name our releases alphabetically, and we're currently in the midst of CHEESES OF THE WORLD. Previous release themes include "Sh*t Gen-Y Says," "Muppets Characters," and "Crayola Colours."

### Design Docs

Design docs clarify domain models and implementation strategies for non-trivial things, allowing them to be communicated effectively between several people over time, and in order to put subsequent coding in context. We keep design docs in a shared Engineering folder on Google Drive, where everyone on the team can find and edit them.

To publicise these documents better, one of the Canva devs developed a Hipchat integration that publishes all "public to Canva" documents to a dedicated "Google Drive" room. It's a great way to see what your colleagues are working on.

### Code Reviews

Before code gets pushed to a master branch, it gets reviewed. Code-review culture makes or breaks an engineering team, so we follow a few principles that keep things running smoothly:

  * For non-obvious changes, authors discuss their approach with their intended reviewer before starting to code. For large initiatives, this usually occurs through a design-doc process, so that reviewers always have context before they see any code.
  * Core reviews are divided into cohesive, bite-sized pieces (100~300LOC max). This sometimes requires deft git-fu to manage a dependent sequence of changes, but (perhaps counter-intuitively to some) a series of bite-sized reviews always goes faster than one big review.
  * As reviewers, we respond to review requests in a timely manner, or assign the review to someone else. Timely usually means within an hour or so, but no more than 1 day.
  * We keep the feedback cycles minimal; on the rare occasion when an issue is going in circles, we resolve it in person at a time of mutual convenience rather than engaging in long discussion threads.



### Style Guides

Each language we use has an internal style guide, and each guide is a living document that evolves through consensus from those on the team who use that language. We keep those guides in a GitHub repo, and propose changes, through pull requests.

### Interviews

Given our pace of recruiting, at some point everyone will be involved in reviewing submissions from potential hires or interviewing candidates. During hiring periods, we expect this to take 4~5 hours a week of an engineer's time.

### Releasing

Key points about our release cycle are:

  * we run a baseline weekly release cycle for all of our deployable components (some components release much more frequently), in addition to occasional feature-driven releases;
  * all backend and frontend engineers participate in a release cop roster, so everyone gets hands-on exposure to how things run in production.



## Communicating

### Email

Email is our primary tool for reliable communication. To get someone's input on something, it's best to send them an email. In particular, we strongly suggest **not using chat software for reliable messaging**. We recommend everyone brushes up on how to use an email client effectively (e.g., keyboard navigation in Gmail) and checks their inbox regularly, at least hourly during work hours. For example, our CI system delivers notifications primarily over email. In order to push code, engineers need to be contactable by the system in the event of a break.

In many chat tools, notification state is not preserved across network reconnection or signout/signin. If you send someone a message, you have no way of knowing if they're ever going to notice it.

### HipChat

We use HipChat for transient, short-lived group discussion. We've found it to be an invaluable tool for having several vibrant discussions occurring concurrently, and allowing people who weren't present at that time to peruse the discourse at a later time. No one's obliged to use it, but pretty much everyone does. There are more serious rooms for asking questions, and sillier rooms for posting the latest cat GIFs and memes. If everyone in the room suddenly starts laughing, it's probably because of something on HipChat.

## People — how we get things done with others

Everyone's got their own preferred way of working. Contrary to the stereotype, not every engineer is an introvert. Some people get their best ideas from bouncing off others, and some work better when they can isolate themselves and fully immerse themselves in a problem. Some prefer to solve problems by doing and iterating, some prefer to solve problems by analyzing and understanding. One person might use different styles in different contexts. Rather than try to coerce people into one style or another, we just recommend common sense and politeness to enable everyone to work together constructively.

We all try to be mindful of our different styles in all aspects of how we interact day to day, but two interactions are of particular importance at Canva:

### Checking in

We enjoy a great amount of freedom in managing time and priorities on our own. We have flexible hours, and nobody micro-manages our day-to-day schedules. But to paraphrase Uncle Ben, with great freedom comes great responsibility… to keep the rest of the team informed about what you're working on.

Checking in with the team keeps priorities and scope in mind as we build things, and offers a way for everyone to contribute via offering suggestions, lending a hand, or challenging preconceptions. We've found from experience that when someone has been working on a project in isolation for a few days, there's a good chance that a discussion with a peer would have saved a lot of time.

We keep each other up-to-date through things like small standups, daily conversation, HipChat, code reviews, and JIRA. Sometime's it's as simple as leaving a message in the team's HipChat room every few days.

### Managing interruptions

All day, every day, most of us are busy doing something. Our open plan office is great for camaraderie and vibe, but it can sometimes make it difficult to focus, especially if you're working on a task that requires deep concentration. Some people hold a lot of context in their working memory at any one time, others don't. Some people welcome interruption, others don't. To work together effectively, we ensure that everyone is aware of the almost-universal-but-usually-unspoken ways that engineers work day to day.

### Concentration indicators

  * Wearing headphones
  * Working away from normal desk



If someone's displaying the above behavior, we try not to interrupt them verbally unless it's urgent; IM is preferred (which means there's a responsibility on everyone to check IM periodically, even when they're the one trying to concentrate).

For extended conversations, it's best to politely ask in advance ("can we chat about X in 10mins?"), so the person has enough time to context-switch out of their current task. For anything longer than that, we suggest putting a timeframe on what you want to talk about ("can we chat for ~30mins about X when you're free?").

Interruptions still happen, of course. When one does, we suggest letting the person know upfront that you're concentrating on something, and asking them if it's urgent. And if you're the person doing the interrupting, try not to get offended when you get asked if your needs are urgent.

### Noise

Concrete floors are great for skateboarding; less great for acoustics. Extended conversations around the desks can break the concentration of everyone nearby. We often take discussions into small meeting rooms instead, or having them in HipChat so others can benefit from what was concluded afterwards.

## Principles — how we approach problems

These are not the Canva Commandments of "How to be a Good Engineer," but rather just a list of principles that we have been applying consistently, and help to paint a picture of our engineering philosophy. We find this helps new people understand how decisions have been in the past (and how they continue to be made), and context for expectations when collaborating and code reviewing.

### Understand the problem

It's best to always have a clear understanding of the precise problem you're trying to solve, particularly in terms of a user story, and keep referring back to that precise problem. Try to avoid phrasing problems in ways that presuppose a solution. If you start a conversation with someone at Canva with "how do I make X do Y?", they'll usually reply with "what problem are you trying to solve?".

Of course, you may have already thought long and hard about how to solve the problem and you're asking advice on a specific part of the implementation. Nonetheless, it's better to provide the context and rationale, giving yourself an opportunity to consider a different approach from your colleague.

### Work smarter, not harder

Things move very quickly here. We try to aim for the smallest, simplest change that meets requirements, while keeping in mind what the bigger, better way would be if it becomes a priority. Our priorities change weekly, if not daily, so any task that takes more than a few days runs the risk of being wasted work.

### What does everyone else do?

It's never good to reinvent the wheel. Our default strategy for solving any problem, somewhat tongue-in-cheek, is to look for someone smart who's already solved it before and copy what they did. In particular, if there's already an overwhelming convention to solve a problem in a particular way, we err towards that convention. There are few problems that can't be solved quickly by judicious browsing of Stack Overflow. By having a solid understanding of the real problem you're trying to solve, you can use your judgement for whether there's reason to break the trend. When a trend does need to be broken, we say go for it.

### Choose the right thing to build

Before thinking about how we're going to build something, we try to be sure we're building the right thing. We don't hesitate to change what we're building in order to significantly simplify how it can be built, so long as it still solves the essential problem.

Sometimes, the initial conception of a feature can be pretty vague or internally inconsistent, and the details aren't set in stone. We like to think we thrive on this ambiguity. Each engineer uses their understanding of the underlying business problem and customer need to massage each feature into something consistent, something that can be built quickly and simply, but something that is still faithful to the original vision.

## Looking to the future

We've found that these practices and principles have been working well for our team at its current scale (16 engineers across our web client, ios client, and backends), but according to the rule of 3 and 10, we're expecting them to evolve significantly as we grow. We'll share an update with how we're going once we reach a team of 30!

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.3b75317b.png)](https://www.canva.dev/blog/engineering/picking-color-via-eyedropper-on-web-app/)

[Web AppPicking Color via Eyedropper on Web AppThe journey of the eyedropper in Canva.](https://www.canva.dev/blog/engineering/picking-color-via-eyedropper-on-web-app/)

[Xidorn Quan⁠(opens in a new tab or window)](https://www.upsuper.org/)Jan 27, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.ef686439.png)](https://www.canva.dev/blog/engineering/machine-learning-hyperparameter-optimization-with-argo/)

[Machine LearningMachine learning hyperparameter optimization with ArgoHow the hyperparameters of our machine learning models are tuned at Canva.](https://www.canva.dev/blog/engineering/machine-learning-hyperparameter-optimization-with-argo/)

[Ryan Lin⁠(opens in a new tab or window)](https://www.linkedin.com/in/ryanlyn/), [Yiran Jing⁠(opens in a new tab or window)](https://www.linkedin.com/in/yiranjing/), [Paul Tune⁠(opens in a new tab or window)](https://medium.com/@anamolous.behaviour)Sep 16, 2021

[![](https://www.canva.dev/_next/static/media/thumbnail.1397c3e4.png)](https://www.canva.dev/blog/engineering/dms-aws-rds-migration/)

[BackendRelational Database Migration with AWS Database Migration Service (DMS)How we reliably migrated hundreds of GBs of relational DB data for our service split project](https://www.canva.dev/blog/engineering/dms-aws-rds-migration/)

[Dafu Ai⁠(opens in a new tab or window)](https://www.linkedin.com/in/dafu-a-409417103/)Jun 19, 2023

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


