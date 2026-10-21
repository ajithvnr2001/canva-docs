---
url: https://www.canva.dev/docs/apps/submitting-apps/
title: Submitting apps - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:42.939586+00:00
---

# Submitting apps - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/submitting-apps/

Prepare for submission

App listing guidelines

[Overview](https://www.canva.dev/docs/apps/app-listing-guidelines/)[Written content](https://www.canva.dev/docs/apps/app-listing-guidelines/written-content/)[App icon](https://www.canva.dev/docs/apps/app-listing-guidelines/app-icon/)[Featured image](https://www.canva.dev/docs/apps/app-listing-guidelines/featured-image/)[Listing behavior](https://www.canva.dev/docs/apps/app-listing-guidelines/behavior/)[App support and links](https://www.canva.dev/docs/apps/app-listing-guidelines/app-urls/)

[Submission checklist](https://www.canva.dev/docs/apps/submission-checklist/)[Developer verification](https://www.canva.dev/docs/apps/developer-verification/)

Submission and release

[Submit your app](https://www.canva.dev/docs/apps/submitting-apps/)[App review process](https://www.canva.dev/docs/apps/app-review-process/)[Releasing apps](https://www.canva.dev/docs/apps/releasing-apps/)

Private apps

[Managing private apps](https://www.canva.dev/docs/apps/managing-team-apps/)

# Submitting apps

An introduction to the app submission process.

Copy page

Before an app can be [released](https://www.canva.dev/docs/apps/releasing-apps/) to the public or a team, it must be submitted for review and pass through an [app review process](https://www.canva.dev/docs/apps/app-review-process/). The submission itself takes place via the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers).

The steps below cover submitting an app that runs inside Canva. The requirements you need to complete before submitting depend on which capabilities your app has enabled.

## How to submit apps for review

The exact steps and outcome of submitting an app depend on whether it's a public app or a private app.

### Public apps

  1. [Upload the app's bundle](https://www.canva.dev/docs/apps/bundling-apps/#how-to-upload-a-bundle) using the Canva CLI or the Developer Portal.

  2. In the Developer Portal, open your app from **Your apps**.

  3. On the **Release > App listing details** pages (**Text** , **Media** , and **Links**), provide written content and visual assets.

  4. On **Release > Testing instructions**, if the app uses credentials to [authenticate users](https://www.canva.dev/docs/apps/authenticating-users/), provide the following information:

     * Login credentials that let app reviewers test the app's functionality, in the **Login details** section.
     * Any additional details that will help the review team test your app, such as an explanation of how the third-party platform works, or how the app integrates with the third-party platform.
  5. On **Release > App status**, under **Submit app for review** :

     1. Agree to the [terms and conditions⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).
     2. Submit the app for review.



The app will be added to Canva's app review queue, and a Jira Service Desk (JSD) ticket will be created to track the progress of the submission. All communication related to the submission should happen via this ticket.

### Private apps

  1. [Upload the app's bundle](https://www.canva.dev/docs/apps/bundling-apps/#how-to-upload-a-bundle) using the Canva CLI or the Developer Portal.
  2. In the Developer Portal, open your app from **Your apps**.
  3. On the **Release > App listing details** pages (**Text** , **Media** , and **Links**), provide written content and visual assets.
  4. On **Release > App status**, under **Submit app for review** : 
     1. Agree to the [terms and conditions⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).
     2. Submit the app for review.



The app will be added to the team's app review queue.

If the owner or an administrator of the team doesn't check the review queue regularly, be sure to notify them of the submission. You can identify the owners or administrators of a team via the **Account settings > People** page.

## How to modify submitted apps

After an app has been submitted for review, it enters a **Submitted** state. In this state, the app can't be modified. If you want to make changes to the submitted app, you need to cancel the submission.

## How to cancel app submissions

  1. In the Developer Portal, open your app from **Your apps**.
  2. On **Release > App status**, select **Cancel submission**.
  3. In the confirmation dialog, select **Cancel submission**.



After a submission has been canceled, the app is removed from the review queue, and it's possible to make changes to the app. When you're ready to resubmit the app, restart the submission process on **Release > App status**.
