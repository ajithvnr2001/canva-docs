---
url: https://www.canva.dev/docs/extensions/quickstart/
title: Quickstart - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:38.303152+00:00
---

# Quickstart - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/quickstart/

App Development

[Overview](https://www.canva.dev/docs/extensions/)[Quickstart](https://www.canva.dev/docs/extensions/quickstart/)[Changelog](https://www.canva.dev/docs/extensions/changelog/)

Platform concepts

Apps

Extensions

[Regions](https://www.canva.dev/docs/extensions/platform-concepts/regions/)[Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/)[Deprecation policy](https://www.canva.dev/docs/extensions/platform-concepts/deprecation-policy/)

Extensions

Content extensions

Publish extensions

Backend development

Base URL

[Continuation](https://www.canva.dev/docs/extensions/backend-development/continuation/)

Signature verification

SDKs

Distribution

UX guidelines

[Submission checklist](https://www.canva.dev/docs/extensions/distribution/submission-checklist/)[Creating the App Directory listing](https://www.canva.dev/docs/extensions/distribution/app-directory-listing/)

Server API

[Overview](https://www.canva.dev/docs/extensions/server-api/server-api/)[GET /apps/configured](https://www.canva.dev/docs/extensions/server-api/get-apps-configured/)[POST /configuration](https://www.canva.dev/docs/extensions/server-api/post-configuration/)[POST /configuration/delete](https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/)[POST /content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/)[POST /publish/resources/find](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/)[POST /publish/resources/get](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/)[POST /publish/resources/upload](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/)[Redirect URL](https://www.canva.dev/docs/extensions/server-api/redirect-url/)

Reference

[Languages](https://www.canva.dev/docs/extensions/reference/supported-languages/)

# Quickstart

Get up and running with Canva's app development platform.

Copy page

Canva's app development platform allows anyone to create [apps](https://www.canva.dev/docs/extensions/platform-concepts/apps/) that add features to Canva. This guide explains how to get started with app development as quickly as possible.

## Step 1: Create an app via the Developer Portal

The [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers) is where you can create, manage, and preview apps.

![](https://www.canva.dev/_next/static/media/img-7ada6bdd71.c9fd7eae.jpeg)

To create an app via the Developer Portal:

  1. Log in to the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers). If you already have a Canva account, you can use the same credentials.

  2. Navigate to the **Your integrations** page.

  3. Click **Create an app**.

  4. Choose a target audience for the app from the **Who is this app for?** page.

![](https://www.canva.dev/_next/static/media/img-5258d2dfbc.d502aa1c.jpeg)

Selecting **Everyone** creates a [public app](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/) for everyone. Selecting **Your team** creates a [team app](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/) for members of your [team⁠(opens in a new tab or window)](https://www.canva.com/teams).

  5. Click **Next**.

  6. Select what your app will do in the **What will your app do?** page.

![](https://www.canva.dev/_next/static/media/img-d3ef1cb67b.38de3d59.jpg)

You can configure your app to **Create content** , **Edit images** , or **Publish designs**. Selecting one or more of these options determines what extensions appear in the next step.

  7. Click **Next**.

  8. Add extensions to the app from the **Select one or more extensions** page.

![](https://www.canva.dev/_next/static/media/img-92277aa4fe.9bbfdd9a.jpg)

An extension is what hooks into the Canva editor and makes the app a seamless part of the user experience. The available extensions depend on what was selected in the previous step. You can also add or remove extensions after the app is created.

You can add any combination of the following types of extensions to an app:

     * [Content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/) \- Add third-party content to Canva.
     * [Publish extensions](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) \- Add publish destinations to Canva.

You can't add multiple extensions of the same type to an app.

  9. Click **Create app**.




Once your app is created, you're taken to the app's **Extensions** page where you can configure the enabled extensions. To configure the app's settings, navigate to the **Details** page.

![](https://www.canva.dev/_next/static/media/img-b75509e098.caacdd88.jpeg)

## Step 2: Start developing an extension

Each extension has its own quickstart guide:

  * [Quickstart for content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/quickstart/)
  * [Quickstart for publish extensions](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)



These guides demonstrate how to create simple yet illustrative examples of extensions. They're short, practical, and lay the foundation for more advanced development. Once you read them, you can confidently dive into the rest of the documentation.

## Questions?

If you have questions about our platform, need help creating your app, or have something else to share, [create a support ticket via Jira Service Desk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/2/group/2).
