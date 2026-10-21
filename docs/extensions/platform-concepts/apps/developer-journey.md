---
url: https://www.canva.dev/docs/extensions/platform-concepts/apps/developer-journey/
title: Developer journey - Apps - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:59:00.722990+00:00
---

# Developer journey - Apps - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/platform-concepts/apps/developer-journey/

Apps

[Overview](https://www.canva.dev/docs/extensions/platform-concepts/apps/)[Developer journey](https://www.canva.dev/docs/extensions/platform-concepts/apps/developer-journey/)[Change an app's distribution](https://www.canva.dev/docs/extensions/platform-concepts/apps/change-app-distribution/)

Public apps

[Overview](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/)[Create a public app](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/create-public-app/)[Submit a public app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/)[Release a public app](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/release-public-app/)

Team apps

[Overview](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/)[Switch teams](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/switch-teams/)[Create a team app](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/create-team-app/)[Submit a team app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/submit-team-app/)[Review a team app](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/review-team-app/)[Release a team app](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/release-team-app/)[Reject a team app](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/reject-team-app/)

App versions

[Overview](https://www.canva.dev/docs/extensions/platform-concepts/apps/versions/)[Create a new version of an app](https://www.canva.dev/docs/extensions/platform-concepts/apps/versions/create-app-version/)

# Developer journey

Copy page

The _developer's journey_ is the series of steps, decisions, and actions you take to build and release an [app](https://www.canva.dev/docs/extensions/platform-concepts/apps/).

This document explains an app developer's journey.

## Flowchart

This flowchart visualizes the choices you can make as you build and release an app.

![](https://www.canva.dev/_next/static/media/img-577ba4b830.b4bd51fc.png)

## Phases

The developer's journey has the following phases:

  1. Create an app
  2. Add an extension
  3. Develop the extension
  4. Prepare for the app review
  5. Submit the app for review
  6. Wait for Canva to translate the app
  7. Release the app



This section describes each phase.

### Create an app

![](https://www.canva.dev/_next/static/media/img-11425e9ae5.71981645.png)

In this phase, you:

  * Log in to the Developer Portal.
  * Create an app.
  * Choose a way to distribute the app.



You can choose to distribute the app to:

  * All Canva users (a [public app](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/))
  * Only the members of a specific team (a [team app](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/))



You can't change a public app into a team app (or vice-versa). To bypass this limitation, you can create a new app with the metadata of the original app. For more information, see [Change an app's distribution](https://www.canva.dev/docs/extensions/platform-concepts/apps/change-app-distribution/).

### Add an extension

![](https://www.canva.dev/_next/static/media/img-ebdfe06d81.d63f300b.png)

In this phase, you add [extensions](https://www.canva.dev/docs/extensions/platform-concepts/extensions/) to the app. An extension is a feature or capability of an app.

An app can have:

  * [Content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/) that import third-party content, such as photos and illustrations, into Canva.
  * [Publish extensions](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) that add a publish destination to Canva.



An app can support multiple extensions, but only one extension of the same type. Each extension adds a distinct behavior to the app and requires a different sequence of steps to get it up and running.

### Develop the extension

In this phase, you:

  * Write the code for your app's extensions.
  * Follow [Canva's brand guidelines⁠(opens in a new tab or window)](https://public.canva.site/our-brand) to be consistent with Canva's brand.
  * Follow the [UX guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/) to create a delightful user experience.



For content and publish extensions, you also:

  * Follow the [authentication guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/) to create a seamless [authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/) flow for users to connect to the third-party platform (if required).
  * Meet the [signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/) requirements (if authentication is enabled) to verify that requests received by the app are from Canva.



To get started, see:

  * [Quickstart for content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)
  * [Quickstart for publish extensions](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)



For server API reference documentation, see the [Server API](https://www.canva.dev/docs/extensions/server-api/server-api/) section in the sidebar. For client API reference documentation, see the Client API section in the sidebar.

### Prepare for the app review

In this phase, you verify that your app meets the required quality standards before submitting it for review.

This helps you:

  * Deliver an app that's functional, delightful, and appropriate for the audience.
  * Reduce the amount of time spent in the review phase.
  * Create a good reputation for high quality apps.



The review criteria for a public app are outlined in the [Submission checklist](https://www.canva.dev/docs/extensions/distribution/submission-checklist/).

The review criteria for a team app are at the discretion of the team and the reviewer.

### Submit the app for review

In this phase, you submit the app and its user-facing strings (in a JSON file) for review via the Developer Portal.

For public apps, a support ticket is automatically created soon after. All discussions about the app's submission happen via this ticket.

#### Reviewers and criteria

The reviewers and criteria depend on the app type:

  * Canva reviews the public app and its user-facing strings. The review criteria are outlined in the [Submission checklist](https://www.canva.dev/docs/extensions/distribution/submission-checklist/).
  * An owner or administrator of your team reviews the team app. The criteria of this review is at the discretion of the team and the reviewer.



For instructions to submit a public app, see [Submit a public app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/).

For instructions to submit a team app, see [Submit a team app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/submit-team-app/).

#### Review outcomes

There are two possible outcomes of the review process:

  * Approval
  * Rejection



#### Approved apps

If a public app is approved, Canva automatically translates the app. You must [wait for Canva to complete the translation](https://www.canva.dev/docs/extensions/platform-concepts/apps/developer-journey/#wait-for-canva-to-translate-the-app) before [initiating the app's release](https://www.canva.dev/docs/extensions/platform-concepts/apps/developer-journey/#release-the-app).

If a team app is approved, you can [initiate the app's release](https://www.canva.dev/docs/extensions/platform-concepts/apps/developer-journey/#release-the-app).

#### Rejected apps

If a public app is rejected, Canva will explain why and provide some recommendations to improve the app.

If a team app is rejected, you discuss the rejection reasons with your team's app reviewer.

When you've the changes:

  * Create a [new version](https://www.canva.dev/docs/extensions/platform-concepts/apps/versions/) of the app.
  * Implement the suggested changes.
  * Resubmit the app for review.



### Wait for Canva to translate the app

This step only applies to public apps.

In this phase, you wait for Canva to translate the app.

Canva automatically translates the user-facing strings (submitted in a localization file) for 25+ locales. This translation process is free and may take up to approximately three business days.

All discussions about the app's translation happen via the same ticket that's created for the app review.

After the translations are complete, you can [initiate the app's release](https://www.canva.dev/docs/extensions/platform-concepts/apps/developer-journey/#release-the-app).

### Release the app

In this phase, you initiate the app's release via the Developer Portal.

The lead time for a release depends on the app type:

  * For a public app, a member of the Canva Apps team manually adds the app to the Apps directory. This may take up to a week. Until then, your app may be ready, but not available to users.
  * For a team app, Canva sends an email to the creator of the app and immediately makes the app available to members of the team.



All discussions about the app's release happen via the same ticket you raised for the app review.

For instructions to release a public app, see [Release a public app](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/release-public-app/).

For instructions to release a team app, see [Release a team app](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/release-team-app/).
