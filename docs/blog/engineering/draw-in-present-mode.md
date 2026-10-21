---
url: https://www.canva.dev/blog/engineering/draw-in-present-mode/
title: From Intern Project to Production: How I Shipped the Draw Tool for Canva's Present Mode - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:12.100095+00:00
---

# From Intern Project to Production: How I Shipped the Draw Tool for Canva's Present Mode - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/draw-in-present-mode/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Draw tool

# From Intern Project to Production: How I Shipped the Draw Tool for Canva's Present Mode

Overview of the technical hurdles I overcame to evolve my intern project into a new feature for users.

![](https://www.canva.dev/_next/static/media/thumbnail.6933959c.jpg)

* * *

  * 


[Edwina Adisusila⁠(opens in a new tab or window)](https://www.linkedin.com/in/edwina-adisusila/)Aug 6, 2025

* * *

Canva’s internship offering is a [12-week summer program for penultimate year tertiary students.⁠(opens in a new tab or window)](https://www.lifeatcanva.com/en/early-careers/) Every intern is empowered to own a project over the course of the internship. When I joined as a Frontend Software Engineering Intern in the Summer of 2022/2023, my project was to add the ability to draw in Canva’s present mode - one of the top feature requests for Presentations. By the end of the internship, I built a working proof of concept that enabled users to draw while presenting in real time.

After returning to Canva as a Graduate in 2024, I continued working on the feature as the lead engineer on the project, driving its development and completion. This involved:

  * Breaking down the project into achievable milestones
  * Implementing and testing the code
  * Working through code reviews to make sure it met Canva’s high quality standards
  * Formulating a release plan
  * Monitoring analytics
  * Continuous coordination with various stakeholders



‘Draw in Present Mode’ has been shipped to production, and has seen strong adoption, with an average of 10 million uses over a 2 week period and average of 470 K Monthly Active Users.

In this blog, I’ll share my journey of shipping ‘Draw in Present Mode’ to users. I’ll dive into the feature, technical challenges I faced and the learnings from my experience of taking an internship project to production.

## Listening to Users

User feedback consistently highlighted the desire to draw while presenting, with over 290+ requests it was one of the most highly requested Presentations feature. It had potential to elevate the presenting experience for educators, students and professionals alike.

Being able to visually highlight key points in real time allows presenters to go beyond just speaking, making presentations more interactive and engaging.

![Feedback from our users.](https://www.canva.dev/_next/static/media/user_feedback.966e64f3.png)

Feedback from our users.

## Building the solution

The goal was to enable users to draw in real time while presenting, with access to various draw tools and to only store the drawings for the duration of the presenting session. The draw tool itself already existed in Canva’s editor (check out this [blog post](https://www.canva.dev/blog/engineering/behind-the-draw/) to learn more). However, it was initially built for that single use case, and since Canva’s editor code and presenting code are separate domains, integrating draw into the presenting experience raised several engineering challenges.

  1. First, its code was tightly coupled to the Canva editor making it inaccessible to the presenting package.
  2. Second, in Presenter View - where 2 windows open, one displaying presenter notes and upcoming slides, and another showing the fullscreen view to the audience - drawings appeared incorrectly positioned and scaled between the 2 windows.
  3. Lastly, loading the draw tool upfront caused a 7% increase in presentation load time, impacting performance.



The following sections explore how I overcame these challenges.

## Technical challenges

### Refactoring for reusability

At Canva there's a set of dependency rules to prevent cyclic dependencies across packages. Therefore, an issue I encountered was that the draw tool code was located in a package that couldn't be imported from the presentation package. Secondly, the code architecture was structured in a way that was tightly coupled to the editor and this meant classes couldn't be easily reused.

![Forbidden import](https://www.canva.dev/_next/static/media/forbidden_import.24c49dae.png)

Presentation package unable to import from draw package.

After considering a variety of approaches, the best solution to make the draw tool reusable was to introduce a new package. This package would centralize all core draw logic and be positioned in a location accessible to both the editor and presentation packages. By doing so, this made sure that core classes could be reused across different use cases while keeping domain-specific implementations in their respective packages.

Introducing a new package involved writing a proposal document describing its purpose, components, necessity and dependencies, to make sure it aligned with Canva’s long-term product vision. This needed to be approved by the team responsible for making sure Canva’s architecture remains cohesive and consistent.

![New package structure](https://www.canva.dev/_next/static/media/new_package_structure.140c1a76.png)

New package to store reusable draw code.

Once it was approved, moving the core parts of the system into the new package wasn’t going to be a straightforward task as code was tightly coupled to the editor. To begin, I visualized the components that make up the draw tool to understand their function and how they depend on each other.

![Old draw package architecture.](https://www.canva.dev/_next/static/media/old_draw_package_architecture.a2bd05ef.png)

Class diagram of previous draw package architecture.

I found this problem exciting, as I was able to put concepts I had learnt in university into practice. I applied the Open/Closed Principle by designing abstractions to allow new environments such as present mode, to integrate seamlessly without modifying the core code. Let’s zoom into a simplified section as an example.

![Class abstraction example](https://www.canva.dev/_next/static/media/class_abstraction_example.3011a944.png)

Simplified example of introducing abstractions.

In the previous state, let’s say `Class A` depends on `Class B`. In the desired state, `Class A` can be reused to avoid code duplication and therefore can be moved to the common package. However let’s say `Class B` needs to be implemented differently for the editor package and presentation package. Since `Class A` was previously dependent on `Class B`, for compatibility I introduced an interface as a contract between the shared class and domain specific implementations.

By planning first and visualizing the desired end state of the entire system, it was much clearer how I was going to implement the refactor.

![New draw package structure.](https://www.canva.dev/_next/static/media/new_draw_package_architecture.ce0ac22b.png)

Class diagram of desired draw package architecture.

I was able to successfully move the reusable parts into the new common package I introduced, ready for implementation. Tackling this architectural challenge was an incredible learning experience, reinforcing the importance of modular, maintainable and extensible code in building scalable features.

### Fixing scaling issues

One of Canva’s present modes is ‘Presenter View’, where 2 windows open: the presenter window which displays presenter notes and upcoming slides, and the audience window which shows the fullscreen view to the audience. During implementation, an issue I encountered was that drawings had the incorrect position and size on the window that wasn’t being drawn on. In addition, the drawings didn't resize when the window was resized.

![Scaling issues.](https://www.canva.dev/_next/static/media/scaling_issue.c9dba044.gif)

Example showing issues with scaling in Presenter View.

The solution involved normalizing the drawing points to a generalized coordinate system, regardless of which window the user was drawing on. These normalized points were then converted to the appropriate position and scale based on the size of the target window before rendering the draw strokes.

![Scaling issue high level solution](https://www.canva.dev/_next/static/media/scaling_issue_high_level_solution.43c6d3e9.png)

High level overview of solution. 

Imagine a user draws a dot while presenting on the presenter window. To normalize the point, the `pw_zoom` is calculated and used to translate the point `(pw_x,pw_y)` to the normalized coordinate system `(n_x,n_y)`. This step makes sure that the point’s position is independent of the specific dimensions of the presenter window. Next, to calculate the corresponding position on the audience window `(aw_x,aw_y)`, the normalized point `(n_x,n_y)` is scaled using `aw_zoom`.

![Scaling issue solution example](https://www.canva.dev/_next/static/media/scaling_issue_solution.7316535e.png)

Simple example walking through solution. 

This resulted in consistency across both windows for a seamless experience for users. Addressing the dual-window issue in Presenter View highlighted the importance of identifying and considering edge cases early in the development process.

### Resolving performance regression

After releasing the feature to a small percentage of users, a 7% increase in presentation load time was observed after clicking the ‘Present’ button. I paired with another engineer to investigate the cause, focusing on when the draw tool was being initialized and how long it was taking. We found that the draw tool (a resource-heavy package) was being fully initialized upfront during the initial loading process, causing the performance impact.

To address this, I implemented lazy loading to defer loading parts of the draw tool until they were needed. I employed a code-splitting strategy to divide it into essential components required upfront and the remaining which could be loaded on demand.

![Lazy loading pseudo code](https://www.canva.dev/_next/static/media/lazy_loading_pseudo_code.143a57e5.png)

Pseudo code implemented for lazy loading. 

This pseudo code shows that when a presentation initially loads through `loadPresentation()`, only the button to activate the draw tool is loaded, as it is essential for the initial setup. Once the user clicks this button to activate the draw tool, the remaining code required for live drawing is loaded asynchronously on demand.

By implementing lazy loading for the draw tool in present mode, the presentation load time was reduced from a 7% increase to 0.24% which was within the anticipated and accepted budget, maintaining the high bar of performance and load time. This approach not only fixed the deterioration in load time but also prepares the system to handle future growth and complexity. From this work, I learnt the importance of optimizing for performance to avoid negatively impacting user experience, especially for those with low connectivity.

## Conclusion

In this blog post, we’ve explored the exciting journey of how I took my internship project to production, the technical challenges tackled along the way and the valuable learnings I gained from the experience.

Coming back to Canva as a graduate and being trusted to see through my own intern project through to production was incredibly meaningful to me. While I owned the process end-to-end, I was never alone. Having support from stakeholders genuinely invested in the project's success and engineering domain experts who were willing not just to help, but to actively teach and guide my growth, made this truly a team effort. This experience deepened my appreciation for collaborative engineering and accelerated my growth as an engineer.

For aspiring software engineers, I hope this story highlights the meaningful impact you can make as an intern or new graduate. With the right mindset, determination, and a supportive environment like Canva, challenges become opportunities to grow and innovate.

## Acknowledgements

A huge thank you to everyone who helped bring ‘Draw in Present Mode’ to life.

Thank you [Denis Tokarev⁠(opens in a new tab or window)](https://www.linkedin.com/in/devlato/), [Alex Gemberg⁠(opens in a new tab or window)](https://www.linkedin.com/in/grebmeg/) and [Jason Wong⁠(opens in a new tab or window)](https://www.linkedin.com/in/jtywong) for the incredible technical support, guidance through tough challenges and sharing your engineering expertise in the Draw and Presenting domains.

Thank you [Karo Boaz⁠(opens in a new tab or window)](https://www.linkedin.com/in/karoboaz/), [Muzi Hu⁠(opens in a new tab or window)](https://www.linkedin.com/in/muzihu) and [Andy Peacock⁠(opens in a new tab or window)](https://www.linkedin.com/in/andrewpeacock) for thorough design explorations, [Matt Richmond⁠(opens in a new tab or window)](https://www.linkedin.com/in/mrrichmond/) for leading the product vision, [Owen Darnell⁠(opens in a new tab or window)](https://www.linkedin.com/in/owen-darnell-219367102) and [Aileen Wang⁠(opens in a new tab or window)](https://www.linkedin.com/in/aileen-wang-482b42158/) for support with testing and release and [Ciaran Shaw⁠(opens in a new tab or window)](https://www.linkedin.com/in/ciaran-shaw-87489313a/), [Daniel Pigott⁠(opens in a new tab or window)](https://www.linkedin.com/in/danielpigott/) and [Darcy Cecil-Oakes⁠(opens in a new tab or window)](https://www.linkedin.com/in/darcy-cecil-oakes-74074812b/) for engineering contributions.

Thank you [Nathan Ellis⁠(opens in a new tab or window)](https://www.linkedin.com/in/nathanellis11) for the mentorship and support throughout this project as an intern, and [Darcy Cecil-Oakes⁠(opens in a new tab or window)](https://www.linkedin.com/in/darcy-cecil-oakes-74074812b/) when I returned as a graduate.

It’s been a pleasure collaborating with each of you.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.3b75317b.png)](https://www.canva.dev/blog/engineering/picking-color-via-eyedropper-on-web-app/)

[Web AppPicking Color via Eyedropper on Web AppThe journey of the eyedropper in Canva.](https://www.canva.dev/blog/engineering/picking-color-via-eyedropper-on-web-app/)

[Xidorn Quan⁠(opens in a new tab or window)](https://www.upsuper.org/)Jan 27, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.9d40c487.png)](https://www.canva.dev/blog/engineering/product-analytics-event-collection/)

[BackendHow Canva collects 25 billion events per dayThe architecture of our product analytics event delivery pipeline.](https://www.canva.dev/blog/engineering/product-analytics-event-collection/)

[Long Nguyen⁠(opens in a new tab or window)](https://au.linkedin.com/in/long-hung-nguyen)Jul 10, 2024

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


