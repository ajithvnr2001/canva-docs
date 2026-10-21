---
url: https://www.canva.dev/blog/engineering/how-to-design-in-every-language-at-once/
title: How to design in every language at once - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:14.611424+00:00
---

# How to design in every language at once - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/how-to-design-in-every-language-at-once/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Localization

# How to design in every language at once

The technology that powers Continuous Localization at Canva.

![](https://www.canva.dev/_next/static/media/thumbnail.e14164be.png)

* * *

  *   * 


[Minh Cung⁠(opens in a new tab or window)](https://www.linkedin.com/in/minhcung/), [Simon Hammond⁠(opens in a new tab or window)](https://www.linkedin.com/in/simon-hammond-990250209/)Oct 20, 2021

* * *

At Canva, part of our commitment to inclusivity is building a global design product that's accessible to everyone in the world. Our vision is to empower the world to design, so one of our crazy big goals is to be available in every language. With over 7,000 languages in the world, that's a work in progress, but at the time of this post, Canva is available in [104 languages across the globe⁠(opens in a new tab or window)](https://slator.com/canvas-localization-leaders-on-translating-into-100-languages/).

![](https://www.canva.dev/_next/static/media/img-0-_7I7I87hJVtpBO42.48f1a87a.png)

Localization matters to us, not just because it helps fulfil our mission to be truly accessible to everyone in the world, but also because it fuels our growth. The majority of our users today work in a language other than English, and as we continue to grow, a larger and larger proportion of our users will be working in non-English languages!

Canva also changes fast: since we release new features every day, we like all of them to be translated and ready to go for as many of our international users as possible. Our engineers and designers need to be aware of the needs of our users around the world, without being slowed down by manual checks and wait times.

In this blog post, we'll show you how we built a localization system that scales to as many languages as we like, without having to wait weeks for the features to roll out. We'll look at the tooling our engineers interact with to get their features translated and merged without sacrificing quality or user experience (UX) for our users.

![](https://www.canva.dev/_next/static/media/img-0-i5utnsb8rb7lAxjf.e14164be.png)

## Why is localization so hard?

Localization isn't just a matter of taking the English language content from each page and passing it through machine translation. Localization requires that we maintain a sensitivity to the culture of each of our users' locales, adapting everything from the linguistic content to local currencies, date formats, and user measures. We even need to make sure images and visuals work for each locale (a topic for another blog post).

Our translators also need to have clear context for each message. What will it look like on the page? What is the intended user experience here?

![](https://www.canva.dev/_next/static/media/img-0-KcSur8MihFaqAqy-.bd8f4d51.png)

For instance, in the screenshot above, the French phrase "Créez et publiez" means "Design and publish", but "Créer un design" on the top right corner means "Create a design". The English word "design" translates differently depending on whether it's a noun or a verb.

Translated content often looks very different from the English source we design in. Sometimes translations are a lot shorter than English (for example, [Korean translation contracts by 10—15%⁠(opens in a new tab or window)](https://www.unitedlanguagegroup.com/blog/translation/korean-translation-facts)), and others are consistently longer ([Vietnamese translation is estimated to be 30—37% longer than the original English⁠(opens in a new tab or window)](https://gtelocalize.com/insightful-tips-for-vietnamese-localization/)). Also, [Thai characters normally have taller glyphs⁠(opens in a new tab or window)](https://www.w3.org/International/articles/article-text-size), and therefore increase line height. We need to make sure that our designs don't cut these translations off.

But it's not practical to test every feature development in every language every day. Even with 104 locales, and certainly not as we scale up to 7,000.

## What did we do?

We here at Canva's Internationalization Engineering team have helped put together a translation pipeline and development framework that ensures:

  * Engineers and designers are able to see how much space their elements need to allow, without having to hand-check every language as they go.
  * Translations are done by human professionals, within two days for any language representing more than 0.03% of our active user base.
  * New features roll out only when enough of the translation has been done that it will cover 99.8% of our user base.
  * Messages are formatted such that translations adjust automatically for variable content such as dates and numbers (plural forms, counting terms, and grammatical agreement).
  * Every source message comes with an explanatory comment given by the engineer introducing the language string and a visual snapshot of the page for the translator's reference to provide more context.
  * Translation quality is checked by experts without blocking feature releases, and international UX is subject to continuous feedback even after the feature is live.



## A step by step overview

We've implemented processes to help with localization at several stages through our development cycle. If it's not well handled, localization can often seem like a chore for engineers, so it's important that we integrate it organically into their workflow. We'll walk you through each part now.

## Development Stage

Thinking about translation quality begins as soon as engineers are running the site locally and looking at their changes.

### Pseudo Localization

We use a special locale code `en-psaccent` implementing pseudolocalization, which is the process of using mock translations to aid in the testing of UI adaption and responsiveness to localized text. For instance, our `en-psaccent` might help us identify issues like this with our "Present" Button:

![](https://www.canva.dev/_next/static/media/img-0-ypFE3n3AH6ouMRkP.f136cdd0.png)

Sure enough, we find the translated text becomes truncated in languages like Vietnamese:

![](https://www.canva.dev/_next/static/media/img-0-GKN4RkANICRTwUht.25c3e062.png)

Some other examples of our pseudolocalized text:

  * `Hello` into `[~~~Hėęllôõ~~~]`
  * `You will receive an SMS shortly.` into `[~Yőòűù~ ~wïĩll~ ~rëēcėęíîvéê~ ~âãn~ ~SMS~ ~~shöōrtlÿ.~~]`
  * `Your security code is: {0}` into `[~Ýòóùúr~ ~seècùúrįitý~ ~cōŏdėę~ ~įis:~ {0}]`



We use three techniques to pseudolocalize text:

  * Accents (for example, "Lōrêm ípsüm"): Applies accents and diacritics to some characters. Not only does this help engineers clearly identify when text is pseudolocalized, it can also help identify issues with non-latin characters, character height and vertical space, and unsupported characters.
  * Encapsulation (for example, "[Lorem ipsum]"): Clearly identifies the start and end of text. This helps detect cases where text is being concatenated, truncated, or where text has been hard-coded.
  * Expansion (for example, "Loongeeer iiiipsuuum"): Simulates the expansion of text as it might appear in a translation. Shorter strings can expand by as much as 300%, with longer strings generally sitting somewhere between 150% and 250%. For more information, see the [IBM/W3 guidelines⁠(opens in a new tab or window)](https://www.w3.org/International/articles/article-text-size/#predict).



**Engineer accessibility** : In some development contexts, using pseudolocalization might introduce accessibility concerns for dyslexic engineers, making it very difficult to determine the original meaning of the message string. At Canva, we do have some engineers with dyslexia, and the i18n team has worked with our Accessibility team to ensure this process doesn't cause undue stress.

In Canva's workflow, copywriting is typically the domain of non-engineer designers, who aren't working with page layouts containing pseudolocalized texts. We only use pseudolocalization further down the production chain, where engineering concerns are around screen real estate, positioning, and flow, as opposed to content and comprehension. In cases where engineers with dyslexia need to understand the text, there's a built-in option to remove pseudolocalization and switch to their desired language.

### Code Structure

We structure our codebase so that translated content lives near its source, which enables our engineers to move/copy code and its associated translations, as well as keeping the scope and ownership of each set of translations clear.

English source strings used in our frontend code live in Typescript files (`*.messages.ts`). Source strings used in our backend code live in Java files (`*Message.java`). Our internationalization (i18n) pipeline converts this into a series of [XLIFF⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/XLIFF) files (ending in `.xlf`), with one file for each locale. All these files live in the repository, but the translated `.xlf` files should never be modified by hand since they are updated automatically when strings get translated.

The directory structure of a feature or a component looks something like:
    
    
    ├── BUILD
    
    ├── example_feature.css
    
    ├── example_feature.messages.ts
    
    ├── example_feature.tsx
    
    ├── translations
    
    │   ├── example_feature_af-ZA.xlf
    
    │   ├── example_feature_ar-EG.xlf
    
    │   ├── [ ... Truncated for brevity ... ]
    
    │   ├── example_feature_zh-TW.xlf
    
    │   └── example_feature_zu-ZA.xlf

TXT

Copy

### Messages Files

A big challenge of localization is formatting messages so that they can be translated flexibly. In many languages (including English) word forms need to change based on dynamic content, such as numbers.

User-facing text at Canva is stored in [ICU Format⁠(opens in a new tab or window)](https://unicode-org.github.io/icu/userguide/) (International Components for Unicode). It's a widely used message format in many translation software systems and i18n libraries, such as _react-intl_. It provides a clear framework for data formatting in the source messages.

Here's an example:
    
    
    You have {numPhotos, plural,
    
          =0 {no photos.}
    
          =1 {one photo.}
    
          other {# photos.}
    
    }

JSX

Copy

The result would be _"You have 1,000 photos."_ when we pass numPhotos = 1000 into the message string, and _"You have one photo."_ when we pass in `numPhotos = 1`.

Here's what an example of a messages file for Frontend called `onboarding.messages.ts` might contain:
    
    
    export const OnboardingMessages = {
    
      /**
    
       * A generic welcome message.
    
       */
    
      welcomeGeneric: (): string => "Welcome!",
    
      /**
    
       * A heading welcoming a user by their name.
    
       *
    
       * @param name The user's preferred name.
    
       */
    
      welcomeByName: (name: string): string => "Welcome to the world of i18n, {0}!",
    
    };

JSX

Copy

For Backend Java Strings, it's fairly similar:
    
    
    // A general greeting to the world.
    
    public String someGeneralGreeting() {
    
      return "Hello, world!";
    
    }
    
    
    
    
    /**
    
     * A nice warm greeting to a user.
    
     *
    
     * @param name The user's name
    
     */
    
    public String someNiceWarmGreeting(String name) {
    
      return "Hey, {0}! It's great to see you.";
    
    }

JAVA

Copy

This file contains a mapping between message names, and closures which might take any number of arguments. These closures should return our source string, which is in English (US).

It's not just the ICU syntax that the translators need in order to do their best work. They also need clear explanations of the purpose of each string. Comments in JavaDoc and JSDoc are processed and displayed in a human-friendly format in Smartling so that the translators can get the context of the source messages. For example:​

![](https://www.canva.dev/_next/static/media/img-0-PV12141zDcewZDrw.55d51fbf.png)

### Translation Pipeline

We've designed our localization process to run in parallel with code review after feature development is complete.

When the engineers create or update a Pull Request (PR) in Github, a bot maintained by the i18n team checks whether any messages need to be translated. If so, a comment similar to the following is added.

![](https://www.canva.dev/_next/static/media/img-0-lOvro6eQInzRkdeT.fdf9f53e.png)

After code review on the messages file is complete, the engineer triggers the translation cycle via an automation triggered via a comment on Github and messages are uploaded to an external third-party translation management system (Smartling). Periodically, the i18n bot checks the progress of translations in Smartling, downloads incremental translation updates and commits them to the PR. A defined subset of the locales must be translated before PRs can be merged. These are called blocking locales. As of October 2021, the blocking locales cover 99.8% of our active user base.

From uploading strings to merging the translations, the process usually takes around 48 hours for new message strings. If the messages match with previously-translated text, the process may be faster. PRs with untranslated strings from the blocking locales fail the `i18n-check-pr-translated` test and merging is blocked. The master branch is therefore always translated into all blocking locales.

The remaining locales are sent for translation once a month, and are not linked to engineer-created PRs. The i18n bot checks on the progress of these languages and pushes updates to master every day.

![](https://www.canva.dev/_next/static/media/img-0-pDMjfJTVOpqD1LLQ.4b5948fb.png)

### Visual Context

Smartling has a [Visual Context⁠(opens in a new tab or window)](https://www.smartling.com/resources/101/visual-context-a-translator-tool-that-helps-the-whole-team/) feature, which allows us to show translators images of the page where the translated messages would show up.

This visual feedback confirms intended meanings, formatting requirements, and many other linguistic nuances at the heart of an accurate translation. As a result, translators spend less time awaiting clarification from colleagues and more time processing new strings.

Quality is not sacrificed in the name of speed. Allowing translators to answer their own questions increases the likelihood of correctly translating strings on the first try. Even if incorrect translations are forwarded to proofreaders, the visual context provides them with the best possible perspective for detecting errors prior to publication.

## Testing Stage

After translations are complete, we run further tests to ensure quality as the PR is merged and we wait for deployment.

### ICU Syntax Validation

Human translators produce much better results than machine translation, but humans sometimes make typos, particularly around syntax markers like `{0}`. For this reason, we've added an ICU Syntax validation as an integration test in our CI to identify any invalid messages and flag it with our translators. Under the hood, this validator uses the [ICU MessageFormat Parser⁠(opens in a new tab or window)](https://formatjs.io/docs/icu-messageformat-parser).

### Linguistic Quality Assurance (LQA)

Each week, a sample of the previous week's translations are marked for review in Smartling. These strings are then double-checked by our expert Language Managers, who make corrections as they go and note patterns of feedback they can offer to the translation teams.

The rate of corrections is measured over time so that we can be alert to any changes or unusual patterns. Common improvements from review include items being added to a reference glossary, or style guides being updated for preserving Canva's voice and technical terms.

#### Visual Regression Tests

As mentioned in [one of our previous blog posts](https://www.canva.dev/blog/engineering/why-we-left-manual-ui-testing-behind/#and-how-widely-it-has-been-used), we currently use Percy for Canva's UI testing at scale. We generate page screens in Burmese to test text height, in German to test text expansion and non-breaking long words, and in RTL mode (with `en-psaccent`) to test right-to-left text rendering.

![](https://www.canva.dev/_next/static/media/img-0-lwQ9Vwa33ethReEr.03128907.png)

## Production Stage

Our commitment to quality and to measuring international user experience doesn't end after the changes go live. Canva has community representatives using our product every day and offering feedback as they work. To enable manual testing at scale, we've created a Chrome extension for third party LQA testers on production to quickly grab string IDs for any text on the page. These string IDs are generated from various properties such as the content and the context where it appears. This is incredibly useful because third party testers can use them to find and edit the translated strings in Smartling without accessing our source code.

![](https://www.canva.dev/_next/static/media/img-1-8_U7OajIgEzDP5h3ItR8Ag.65900916.png)

## Next Steps

Even with all of this tech in place, we know we're only 1% of the way there. The systems we've outlined here allow us to add languages without adding to development time, so we're looking forward to bringing Canva to even more locales soon!

Our next technical goal is to develop a tool to catalogue every possible unique screen and allow anyone to view a specific set of screens that they are interested in, using a variety of filters such as devices and locales.

Occasionally, we need screenshots to check the quality of translation or understand the context of a localised A/B test. This tool will allow Canva engineers and in-house localization specialists to quickly search for strings, evaluate a translation's quality and its appearance on all screens.

## Acknowledgements

Kudos to the other members of the i18n team — [Ben Lloyd⁠(opens in a new tab or window)](https://www.linkedin.com/in/bjl501/) and [Reece Como⁠(opens in a new tab or window)](https://www.linkedin.com/in/reececomo/) — who work on localization technologies at Canva. Special thanks to [Michael Foley⁠(opens in a new tab or window)](https://github.com/michaelfoley1), [Toby Rahilly⁠(opens in a new tab or window)](https://github.com/wearymonkey), and [Sam Killin⁠(opens in a new tab or window)](https://github.com/samkillin) for setting up the technical foundation for localization.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.b928bce2.png)](https://www.canva.dev/blog/engineering/when-url-parsers-disagree-cve-2023-38633/)

[SecurityWhen URL parsers disagree (CVE-2023-38633)Discovery and walkthrough of CVE-2023-38633 in librsvg, when two URL parser implementations (Rust and Glib) disagree on file scheme parsing leading to path traversal.](https://www.canva.dev/blog/engineering/when-url-parsers-disagree-cve-2023-38633/)

[Zac Sims⁠(opens in a new tab or window)](https://au.linkedin.com/in/zacsims)Sep 5, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.5e886671.jpeg)](https://www.canva.dev/blog/engineering/going-deeper-with-depth-maps/)

[Computer VisionGoing Deeper with Depth MapsHow we use machine learning to estimate depth and salience maps for photos in Canva.](https://www.canva.dev/blog/engineering/going-deeper-with-depth-maps/)

[Kerry Halupka⁠(opens in a new tab or window)](https://medium.com/@kerry.halupka)Dec 15, 2021

[![](https://www.canva.dev/_next/static/media/thumbnail.f929c2eb.jpg)](https://www.canva.dev/blog/engineering/adding-responsiveness-to-canvas-design-system/)

[Design SystemsAdding responsiveness to Canva’s Design SystemHow we use the CSS cascade to enable building responsive layouts](https://www.canva.dev/blog/engineering/adding-responsiveness-to-canvas-design-system/)

[Jordan Cohn⁠(opens in a new tab or window)](https://www.linkedin.com/in/jordan-cohn/)Aug 22, 2024

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


