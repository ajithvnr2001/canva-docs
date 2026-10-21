---
url: https://www.canva.dev/docs/apps/submission-checklist/
title: Submission checklist - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:43.805879+00:00
---

# Submission checklist - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/submission-checklist/

Prepare for submission

App listing guidelines

[Overview](https://www.canva.dev/docs/apps/app-listing-guidelines/)[Written content](https://www.canva.dev/docs/apps/app-listing-guidelines/written-content/)[App icon](https://www.canva.dev/docs/apps/app-listing-guidelines/app-icon/)[Featured image](https://www.canva.dev/docs/apps/app-listing-guidelines/featured-image/)[Listing behavior](https://www.canva.dev/docs/apps/app-listing-guidelines/behavior/)[App support and links](https://www.canva.dev/docs/apps/app-listing-guidelines/app-urls/)

[Submission checklist](https://www.canva.dev/docs/apps/submission-checklist/)[Developer verification](https://www.canva.dev/docs/apps/developer-verification/)

Submission and release

[Submit your app](https://www.canva.dev/docs/apps/submitting-apps/)[App review process](https://www.canva.dev/docs/apps/app-review-process/)[Releasing apps](https://www.canva.dev/docs/apps/releasing-apps/)

Private apps

[Managing private apps](https://www.canva.dev/docs/apps/managing-team-apps/)

# Submission checklist

What to do before submitting an app for review.

Copy page

Before your app can be [released](https://www.canva.dev/docs/apps/releasing-apps/) to the public, it must go through and pass Canva's review process.

This page outlines Canva's review criteria for developer apps, as well as some best practices to consider during development. This will help you understand the review process so you can develop and easily release your app.

After you submit a public app, a Canva reviewer verifies whether your app is suitable. For apps inside Canva, this means whether it's suitable for distribution on the [Apps Marketplace⁠(opens in a new tab or window)](https://www.canva.com/apps). For apps built for Canva for your platform, it means whether it's suitable for all Canva users.

Private apps are reviewed by an owner or administrator of your team rather than by Canva. To learn more about both review flows, see [App review process](https://www.canva.dev/docs/apps/app-review-process/).

To prevent spam, an app can only be submitted for review up to 5 times in a single day.

## Before submission

Use the following sections as a checklist to ensure that your app is ready for submission.

Which items apply depends on the surfaces your app is built for and the capabilities it enables. The Developer Portal lists the required actions for your app on **Release > App status**.

### Check email

When submitting your app, make sure that the email address you use to log in to Canva is integrated with your external platform. This helps to associate your app with that platform.

### Read Canva's terms and conditions

Canva's terms and conditions contain essential information about our basic expectations for developers and their apps.

At a minimum, read the following pages:

  * [Terms of Use⁠(opens in a new tab or window)](https://www.canva.com/policies/terms-of-use/)
  * [Canva Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/)



You're asked to agree to these terms when submitting an app.

### Make sure your app idea is unique

The Canva App ecosystem thrives on creativity, diversity, and solving real user needs in new ways. We encourage developers to focus on what makes their app unique. What problem are you solving? What experience are you creating that doesn’t already exist?

Submitting copycat apps isn't allowed. Copycat apps replicate the name, layout, or functionality of existing Canva apps or native Canva features, with only minor changes.

Copycat apps dilute the ecosystem, make discovery harder, and reduce opportunities for genuine innovation. Canva supports original thinking, and we expect all apps in the ecosystem to reflect that standard.

All public apps can be found in the [Apps Marketplace⁠(opens in a new tab or window)](https://www.canva.com/your-apps). Check the Apps Marketplace to make sure your app is unique.

### Use a suitable hosting platform

If your app sends HTTP requests to a third-party server or to your own platform, use a hosting platform that's reliable, secure, and capable of handling the expected traffic from your Canva users.

For production apps, don't use free services, such as [Glitch⁠(opens in a new tab or window)](https://glitch.com/). Free servers can be slow and sleep after a few minutes of inactivity, which causes timeout errors when opening an app.

### Follow Canva's brand guidelines

If your app integrates with a third-party platform, or brings Canva into your own product, any references to Canva on that platform must adhere to [Canva's brand guidelines⁠(opens in a new tab or window)](https://public.canva.site/our-brand).

Apps built for Canva for your platform have additional [brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/) to follow.

### Follow the design guidelines

Canva's [Design guidelines](https://www.canva.dev/docs/apps/design-guidelines/) outline how to create delightful apps inside Canva, and the [UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/) do the same for apps built for Canva for your platform. To reduce the amount of time your app spends in review, double-check that it follows the guidelines that apply to it.

The [recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/) also explain how to make a meaningful app.

### Secure your app

At Canva, the security of our platform and our user data is paramount, and we expect app developers to maintain similar standards. To learn how to keep your app (and its users) secure, see the [security guidelines](https://www.canva.dev/docs/apps/security-guidelines/) for apps inside Canva, or the [security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/) for apps built for Canva for your platform.

### Upload UI strings for translation

For apps inside Canva, you need to upload your app's UI strings for translation to support people who use Canva in languages other than English, in line with our [localization documentation](https://www.canva.dev/docs/apps/localization/).

We’ll then translate your app to all [supported locales](https://www.canva.dev/docs/apps/localization/#supported-locales) for free.

### Test the app

Run through the app to ensure it's complete and everything works as expected. This avoids friction in the review phase and reduces the chances of rejection.

At a minimum, test the following:

  * Core functionality
  * Authentication flow: 
    * With and without an active session
    * With an existing user
    * With a newly signed-up user



For apps inside Canva, also test the following:

  * Endpoints
  * Links
  * Buttons
  * Permissions: 
    * Check your app's functionality to make sure that any required permissions are configured. See [Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/).
  * Themes: 
    * Test your app in both light and dark themes, using the Dev Toolkit. ![Dev Toolkit showing theme selection options](https://www.canva.dev/_next/static/media/dev-toolkit-themes.db4c4911.png)
    * For compatibility, make sure your theme uses the [App UI Kit](https://www.canva.dev/docs/apps/app-ui-kit/).
  * Feature support: 
    * Check for any unsupported APIs in your app. See [feature support guidelines](https://www.canva.dev/docs/apps/design-guidelines/feature-support/).
    * If there are unsupported APIs, make sure to test your app in the relevant Canva design types (both fixed and responsive).



Canva regularly monitors your app's health and might disable the app if there's a high error rate, such as a high error rate when making API requests.

### Make sure your app's configuration is ready for review

For apps built for Canva for your platform, make sure that:

  * Your app's name is suitable for the public.
  * You have at least one valid authentication redirect URL.
  * You don't have any local URLs set as an authentication redirect URL.
  * If you enabled the `collaboration:event` scope to receive webhook notifications, you provided a valid webhook URL.
  * If you enabled **Return navigation** , you provided a valid return URL.



### Create the Apps Marketplace listing

Your app's listing in the [Apps Marketplace⁠(opens in a new tab or window)](https://www.canva.com/apps) drives attention and engagement to your app once released. Before submitting your app, create written content and graphics that clearly communicate your app's benefits.

For a complete list of guidelines, see [Create your app listing](https://www.canva.dev/docs/apps/designing-apps/create-app-listing/).

### Review written content

Your app's written content reflects its quality. Keep the language simple and free from typos and formatting errors. Proofread the written content, run a spellcheck, and review the grammar and punctuation. Remove any external links.

### Provide the required details

We need the following details before proceeding with the app review:

  * Login details for a test account that allow the reviewer to test the app's full functionality (required only if the app uses authentication).
  * Documentation that explains how the platform works.
  * Documentation that lets the reviewer know where to find content if your app provides it.



Depending on the complexity of the app, the above steps might be able to be skipped.

### Recommendation

Creating an app on Canva means you can get your product or idea in front of 135M+ users. To leverage the most use of your app possible, we recommend making your app free to use, which leads to more users trying the app and discovering your platform, likely leading to more sign-ups.

## After submission

After developing your app and submitting it for review, the Canva Ecosystem team checks if it meets Canva's guidelines.

### Duration

The duration of the app review process depends on the complexity of the app and the amount of feedback required. We have a dedicated team that reviews submissions as quickly as they can and will provide progress updates via a support ticket.

### Updates

Updates and messages from the team are added to your ticket, which is automatically generated once you submit your app via the Developer Portal.

You also receive feedback via the Developer Portal when we approve or reject your app.
