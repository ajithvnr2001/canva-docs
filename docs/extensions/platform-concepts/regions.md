---
url: https://www.canva.dev/docs/extensions/platform-concepts/regions/
title: Regions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:42.635794+00:00
---

# Regions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/platform-concepts/regions/

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

# Regions

Copy page

Canva exists in two regions:

  * Global (everywhere except China)
  * China



No data is shared between these regions.

This means there are two, completely independent versions of the Developer Portal:

  * <https://canva.com/developers>[⁠(opens in a new tab or window)](https://canva.com/developers)
  * <https://canva.cn/developers>[⁠(opens in a new tab or window)](https://canva.cn/developers)



This has a few implications that are relevant to developers.

## Terms and conditions

Apps created via `canva.cn` must adhere to the following terms and conditions:

  * [Canva Apps Terms⁠(opens in a new tab or window)](https://about.canva.cn/policies/apps-terms/)
  * [Canva Developer Terms⁠(opens in a new tab or window)](https://about.canva.cn/policies/developer-terms/)



These terms and conditions are unique to the China region.

The key differences include:

  * Your app must adhere to all applicable laws, including: 
    * [Cybersecurity Law of the People's Republic of China⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Cybersecurity_Law_of_the_People%27s_Republic_of_China)
    * [Administration of Internet Information Services Procedures⁠(opens in a new tab or window)](https://wipolex.wipo.int/en/text/475216).
  * Your app's terms of use must not permit users under the age of 14 to use the app.



If you have any specific questions about these terms, send an email to [cnsupport@canva.com⁠(opens in a new tab or window)](mailto:cnsupport@canva.com).

## Personally Identifiable Information (PII)

China's data privacy laws require that personal data of Chinese users must be stored on servers within Chinese territories.

## Multi-region apps

Apps created via `canva.com` are independent of apps created via `canva.cn`. (The reverse is also true.) If you want to release your app in the Global and China regions, you need to create and maintain the apps in both regions.

## Documentation

The documentation always refers to the `canva.com` domain. If you're developing an app for China, it's important to replace references to `canva.com` with `canva.cn`.

## Receiving requests

Throughout the lifecycle of an app, Canva may send HTTP requests to your app. The referring domain of these requests depends on the app's region:

  * Apps created in the Global region receive requests from the `canva.com` domain.
  * Apps created in the China region receive requests from the `canva.cn` domain.



## Sending requests

Throughout the lifecycle of an app, your app may need to send HTTP requests to Canva. The target domain of these requests depends on the app's region:

  * Apps created in the Global region must send requests to the `canva.com` domain.
  * Apps created in the China region must send requests to the `canva.cn` domain.



At the moment, this is only relevant when an app supports [authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/), as apps must redirect users back to Canva at the end of an authentication flow.

## Translations

When Canva releases a public app in the Global region, it translates the app's copy into a variety of different languages.

In the China region, developers can either:

  * Provide copy in English. Canva will translate the copy into Simplified Chinese.
  * Provide copy in Simplified Chinese. Canva won't translate the copy.



The end result is that, in the China region, apps are only available in Simplified Chinese.

## Timeout durations

All HTTP requests that Canva sends to an app have a timeout duration. If the app fails to respond to the request within this duration, the request fails. The exact duration depends on the request.

In the China region, the timeout durations are sometimes longer than the durations in the Global region. This accounts for the slower, less reliable internet speeds in China.
