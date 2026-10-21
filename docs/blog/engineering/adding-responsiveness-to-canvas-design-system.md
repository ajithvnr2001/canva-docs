---
url: https://www.canva.dev/blog/engineering/adding-responsiveness-to-canvas-design-system/
title: Adding responsiveness to Canva\u2019s Design System - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:11.060272+00:00
---

# Adding responsiveness to Canva’s Design System - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/adding-responsiveness-to-canvas-design-system/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Design Systems

# Adding responsiveness to Canva’s Design System

How we use the CSS cascade to enable building responsive layouts

![](https://www.canva.dev/_next/static/media/thumbnail.f929c2eb.jpg)

* * *

  * 


[Jordan Cohn⁠(opens in a new tab or window)](https://www.linkedin.com/in/jordan-cohn/)Aug 22, 2024

* * *

At Canva, our Design System (which we lovingly call Easel) serves a few purposes:

  * **Consistency** : Our components behave consistently across the product, bringing consistency to Canva.
  * **Composability** : Our components have defined responsibilities so that we can compose them in ways that serve the needs of the product.
  * **Efficiency** : 
    * Building a component once discourages engineers from building their own, decreases the bundle size of the Canva application, and reduces the time it take for pages to load.
    * Product designers and engineers have a shared basis from which to start their conversations.



## Our layout system

Some of our core principles for creating consistent layouts include:

  * A set spacing scale (using 8px grid units)
  * Defined breakpoints (small: 600px, medium: 900px, large: 1200px. For more information, see [The 100% correct way to do CSS breakpoints⁠(opens in a new tab or window)](https://www.freecodecamp.org/news/the-100-correct-way-to-do-css-breakpoints-88d6a5ba1862/)).



From these principles, we provide layout components that leave our engineers to focus on more important things. For example, we have a `Rows` component that places components vertically (in rows).
    
    
    <Rows spacing="2u">
    
      <Component1/>
    
      <Component2/>
    
      <Component3/>
    
    </Rows>

TSX

Copy

![A visual demonstration of components in the Rows component](https://www.canva.dev/_next/static/media/rows.559fb41b.png)

As well as making it easier to construct layouts with a high degree of consistency, the components also provide a simple and consistent language between designers and developers.

Diving into a simplified version of how this looked, we applied a default class to set `display: grid` and `width: 100%` and another class conditionally setting the `row-gap` property.
    
    
    function Rows({ children, spacing }) {
    
      return (
    
        <div
    
          className={classNames(
    
            'rows',
    
            `spacing${spacing}`,
    
          )}
    
        >
    
          {children}
    
        </div>
    
      );
    
    };

TSX

Copy
    
    
    .rows {
    
        display: grid;
    
        width: 100%;
    
    }
    
    
    
    
    .spacing0 {
    
        row-gap: 0px;
    
    }
    
    
    
    
    .spacing1u {
    
        row-gap: 8px;
    
    }
    
    
    
    
    .spacing2u {
    
        row-gap: 16px;
    
    }
    
    
    
    
    .spacing3u {
    
        row-gap: 24px;
    
    }
    
    
    
    
    .spacing4u {
    
        row-gap: 32px;
    
    }

CSS

Copy

Therefore, `<Rows spacing="2u">` renders as follows.
    
    
    <div class="rows spacing2u"/>

HTML

Copy

Although this solution worked well to address layouts, we also had to address responsive design. If components are going to be spaced further apart on larger screens, our components should be able to provide that flexibility.

## Designing a solution

The next step was deciding what a good solution should look like. We had 2 hard requirements: an understandable API and for it to be SSR friendly, which meant using CSS media queries.

Designing the API was simple enough. Taking inspiration from [Braid⁠(opens in a new tab or window)](https://seek-oss.github.io/braid-design-system/foundations/layout)’s “responsive props”, we could use the existing `spacing` prop and give it an object, with properties representing breakpoints.
    
    
    spacing={{ default: '2u', smallUp: '4u' }}

TSX

Copy

Mapping that onto our existing styling posed a different challenge. Where previously we had 1 class per space value, adding classes for each breakpoint would have meant _a lot_ of classes.
    
    
    .spacing0 {
    
        row-gap: 0px;
    
    }
    
    
    
    
    .spacing1u {
    
        row-gap: 8px;
    
    }
    
    
    
    
    ...
    
    
    
    
    @media (min-width: 600px) {
    
        .smallUpSpacing0 {
    
            row-gap: 0px;
    
        }
    
        
    
        .smallUpSpacing1u {
    
            row-gap: 8px;
    
        }
    
    
    
    
        ...
    
    }
    
    
    
    
    @media (min-width: 900px) {
    
        .mediumUpSpacing0 {
    
            row-gap: 0px;
    
        }
    
        
    
        .mediumUpSpacing1u {
    
            row-gap: 8px;
    
        }
    
    
    
    
        ...
    
    }
    
    
    
    
    @media (min-width: 1200px) {
    
        .largeUpSpacing0 {
    
            row-gap: 0px;
    
        }
    
        
    
        .largeUpSpacing1u {
    
            row-gap: 8px;
    
        }
    
    
    
    
        ...
    
    }

CSS

Copy

This solution meant that every time we add a feature to our layout system, we’d have to write classes for each option, for each breakpoint. How would we maintain it all? We recognised it wouldn’t scale well, so we needed something better.

### An aside: increasing the size of our design system is a trade-off

With over 190M active users, many with slow devices and slow connections, we want to ensure every user has the best experience possible. Increasing the Canva bundle size results in longer loading times, impacting the user experience.

We take care with every new feature we add to Canva, and our design system is no different. Every new line of CSS added to our design system increases the bundle size on every page. But there is a trade-off! Adding to what our design system can handle also means reducing the custom code we need to write, reducing the _potential_ bundle size.

### C is for Cascade

So, we needed a solution that would not only address every option at every breakpoint, but one that would allow us flexibility and the ability to introduce more options in the future. Inspired by [Lea Verou’s blog post on the topic⁠(opens in a new tab or window)](https://lea.verou.me/blog/2021/10/custom-properties-with-defaults/), we used custom properties and the cascade to our advantage.

The following is our solution.
    
    
    function Rows({ children, spacing }) {
    
      return (
    
        <div
    
          className="rows"
    
          style={{
    
            '--spacing-default': toPx(spacing.default),
    
            '--spacing-small-up': toPx(spacing.smallUp),
    
            '--spacing-medium-up': toPx(spacing.mediumUp),
    
            '--spacing-large-up': toPx(spacing.largeUp),
    
          }}
    
        >
    
          {children}
    
        </div>
    
      );
    
    };

TSX

Copy
    
    
    .rows {
    
        display: grid;
    
        width: 100%;
    
    
    
    
        --spacing-default: 0;
    
        --spacing-internal: var(--spacing-default);
    
        row-gap: var(--spacing-internal);
    
    }
    
    
    
    
    @media (min-width: 600px) {
    
        .rows {
    
            --spacing-small-up: var(--spacing-default);
    
            --spacing-internal: var(--spacing-small-up);
    
        }
    
    }
    
    
    
    
    @media (min-width: 900px) {
    
        .rows {
    
            --spacing-medium-up: var(--spacing-small-up);
    
            --spacing-internal: var(--spacing-medium-up);
    
        }
    
    }
    
    
    
    
    @media (min-width: 1200px) {
    
        .rows {
    
            --spacing-large-up: var(--spacing-medium-up);
    
            --spacing-internal: var(--spacing-large-up);
    
        }
    
    }

CSS

Copy
    
    
    <div class="rows" style="--spacing-default: 16px; --spacing-small-up: 32px"/>

HTML

Copy

![A visual demonstration of components in the Rows component with responsive spacing](https://www.canva.dev/_next/static/media/responsive.5b82a3de.gif)

Instead of one class selector _per space value_ (we have 10 by the way), we now have one class selector _per breakpoint_. We have a custom property for each breakpoint (`--spacing-default`, `--spacing-small-up`, and so on), and set these directly in the `style` tag. There is also one more property, which we’ve called `--spacing-internal`. This is what Lea calls a “pseudo-private custom property”, which prevents long fallback chains. Otherwise, the large breakpoint would look something like `row-gap: var(--spacing-large-up, var(--spacing-medium-up, var(--spacing-small-up, var(--spacing-default))))`.

This works by leveraging the CSS specificity of inline styles:

  1. We set `--spacing-internal` to the variable for the current breakpoint.
  2. If the value for that breakpoint is passed in through the `style` attribute, we use that.
  3. Otherwise, the value for the breakpoint inherits from the previous breakpoint, and we repeat step 2 for the previous breakpoint.
  4. If there are no values set, we fall back to the value for `--spacing-default` defined in the stylesheet (in this case, `--spacing-default: 0;`)



To support more options (for example, with `Rows` we also support alignment, and other components can have many different values to configure) it’s as simple as adding one property for each breakpoint.

## Laying out the future

Adding responsiveness to our layout system was an exciting journey. We’re very proud of our solution, and we hope you’ve enjoyed the ride. There’s so much more to come for the future of our design system, and we’re keen to share more in the future.

I’d like to give a special shout-out to [Cameron Moon⁠(opens in a new tab or window)](https://www.linkedin.com/in/cmrn/) and [Phoebe Hong⁠(opens in a new tab or window)](https://www.linkedin.com/in/phoebehong/) who designed and implemented the foundations of our layout system.

_Interested in solving challenging frontend engineering problems?_ [Join Us!⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/)

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.f0047f36.png)](https://www.canva.dev/blog/engineering/recommender-systems-when-they-fail-who-are-you-gonna-call/)

[Recommender SystemsRecommender systems: When they fail, who are you gonna call?How we deal with potential problems when running Canva's recommendation system.](https://www.canva.dev/blog/engineering/recommender-systems-when-they-fail-who-are-you-gonna-call/)

[Mayur Panchal⁠(opens in a new tab or window)](https://www.linkedin.com/in/panchalm), [Thien Bui⁠(opens in a new tab or window)](https://www.linkedin.com/in/ducthienbui/)Nov 4, 2021

[![](https://www.canva.dev/_next/static/media/thumbnail.b3659c51.png)](https://www.canva.dev/blog/engineering/realtime-mouse-pointers/)

[Real-time CollaborationReal-time mouse pointersOur journey to implement and support real-time mouse pointers.](https://www.canva.dev/blog/engineering/realtime-mouse-pointers/)

[Anton Egorov⁠(opens in a new tab or window)](https://au.linkedin.com/in/anton-egorov), [Mark Gurevich⁠(opens in a new tab or window)](https://www.linkedin.com/in/yodairish/)Aug 15, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.5df784be.png)](https://www.canva.dev/blog/engineering/behind-the-scenes-of-canvas-designdna-campaign/)

[Machine LearningBehind the scenes of Canva's DesignDNA campaignHow we used generative AI to build our year-in-review campaign](https://www.canva.dev/blog/engineering/behind-the-scenes-of-canvas-designdna-campaign/)

[Divya Patel⁠(opens in a new tab or window)](https://www.linkedin.com/in/divyapat1/)Feb 24, 2025

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


