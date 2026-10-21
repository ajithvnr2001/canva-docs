---
url: https://www.canva.dev/docs/extensions/distribution/submission-checklist/
title: Submission checklist - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:43.048576+00:00
---

# Submission checklist - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/distribution/submission-checklist/

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

# Submission checklist

What to do before submitting your app for review.

Copy page

Once you've developed an app, the next step is to [submit it for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/). After you submit it, a reviewer from the Canva Apps team will verify that it's suitable for distribution via the [Apps Directory⁠(opens in a new tab or window)](https://www.canva.com/apps). This page contains a checklist to prepare your app for submission.

## Read Canva's terms and conditions

Canva's terms and conditions contain essential information about the basic expectations that Canva has for developers and their apps.

At a minimum, read the following pages:

  * [Terms of Use⁠(opens in a new tab or window)](https://www.canva.com/policies/terms-of-use/)
  * [Canva Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/)
  * [Canva App Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-apps-terms/)



You're asked to agree to these terms when submitting an app.

## Use a suitable hosting platform

Choose a hosting platform that's reliable, secure, and capable of handling the expected traffic.

The tutorials in the documentation use Glitch's free service to demonstrate an extension's capabilities. For production apps, don't use Glitch's free service. The servers are slow and go to sleep after a few minutes of inactivity, which causes timeout errors when opening an app.

## Follow Canva's brand guidelines

If your app integrates with a third-party platform, such as a [publish destination](https://www.canva.dev/docs/extensions/extensions/publish-extensions/), any references to Canva must adhere to [Canva's brand guidelines⁠(opens in a new tab or window)](https://public.canva.site/our-brand).

## Follow the UX guidelines

Canva's [UX guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/) are packed with advice to create delightful apps. If you want to reduce the amount of time your app spends in the review pipeline, double (and triple) check that it follows the guidelines.

## Test signature verification

If your app has extensions that receive HTTP requests and has [signature verification check](https://www.canva.dev/docs/extensions/backend-development/verify-request/) enabled, you must verify that any requests it receives are actually arriving from Canva (and not from some nefarious third-party). This requirement is enforced by the [signature verification test](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/) in the Developer Portal.

If signature verification checks are disabled, [there are additional requirements](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/) that you must meet before submitting your app.

For more information, refer to [Signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/).

## Secure your app

Use reasonable security measures to protect your app and its users.

At a minimum:

  * Implement encryption and a strong password policy.
  * Sanitize names received from Canva and avoid security issues such as XSS, CSRF attacks, or path traversal. Handle maximum length and unsupported characters suitably.
  * Avoid [OWASP Top 10⁠(opens in a new tab or window)](https://owasp.org/Top10/) risks.



## Test the app

Run through the app to ensure it's complete and everything works as expected. This avoids a lot of friction in the review phase and reduces the chances of rejection.

At a minimum, test the:

  * Core functionality (ability to show, edit, and publish all supported file types)
  * Authentication flow (with and without an active session, with an existing user, with a newly signed up user)
  * Endpoints
  * Links
  * Buttons



Canva will monitor the app's health regularly, and may disable the app if there's a high error rate.

## Create the App Directory listing

Your app's listing in the [Apps Directory⁠(opens in a new tab or window)](https://www.canva.com/apps) is an excellent way to drive attention and engagement to your app. Before submitting your app, create copy and graphics that clearly communicate your app's benefits.

For a complete list of guidelines, refer to [Creating the App Directory listing](https://www.canva.dev/docs/extensions/distribution/app-directory-listing/).

## Review the copy

The copy reflects your app's quality and reputation. Keep the language simple, and free from typos and formatting errors. Proofread the copy, run a spellcheck, and review the grammar and punctuation.

For a complete list of copywriting guidelines, see [Writing copy for your app](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/copy/).

## Provide authentication details

If your app supports [authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/), the app's reviewer needs to test the authentication flow and any integration points the app has with a third-party platform.

To avoid any delays, prepare the following details before submitting the app:

  * Login details for an account that allows the reviewer to test the integration.
  * Documentation that introduces the platform: 
    * How the platform works.
    * Where's the content sourced from.
    * What are the available tiers (Free, Paid, Pro, etc) and how they'll affect the app users.
    * Where and how can a user access their published designs.
  * Documentation that explains where we can find integration points (if any) in the platform.


