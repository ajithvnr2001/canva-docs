---
url: https://www.canva.dev/docs/extensions/platform-concepts/authentication/
title: Authentication - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:21.966500+00:00
---

# Authentication - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/platform-concepts/authentication/

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

# Authentication

Learn how authentication works in Canva Apps.

Copy page

You can configure an app to support _authentication_. If an app supports authentication, users must authenticate with a third-party platform before accessing the app's [extensions](https://www.canva.dev/docs/extensions/platform-concepts/extensions/).

For example, apps with a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) may support authentication to ensure that only users who are registered with the publish destination can publish their designs.

This topic explains what authentication is and how it works.

If you have enabled authentication for an app, you must also implement and pass [signature verification checks](https://www.canva.dev/docs/extensions/backend-development/verify-request/) before submitting your app.

## Examples of authentication

These are some examples of apps that support authentication:

  * [Bitmoji⁠(opens in a new tab or window)](https://www.canva.com/apps/AADxCLHNr_o-bitmoji)
  * [Brandfetch⁠(opens in a new tab or window)](https://www.canva.com/apps/AAD2V_3Se-E-brandfetch)
  * [Pixton⁠(opens in a new tab or window)](https://www.canva.com/apps/AAD6Bz83ydE-pixton)



For more examples, see [canva.com/apps⁠(opens in a new tab or window)](https://www.canva.com/apps).

## How users experience authentication

When a user opens an extension in an authentication-enabled app, they see a **Connect** button.

![](https://www.canva.dev/_next/static/media/img-737d32f18b.e6b0a12d.jpeg)

If the user clicks this button, a pop-up window appears and loads an authentication screen for a third-party platform.

![](https://www.canva.dev/_next/static/media/img-ae0b4af912.3bcf84fd.png)

The user can log in to or sign up for an account with the platform. (The exact authentication method is entirely dependent on the platform.)

Once the user authenticates:

  * The pop-up window closes.
  * The extension reloads.
  * The user gains access to the extension's content or options.



After authenticating, the user can choose to [revoke authentication](https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/).

If you click the **Connect** button, minimize the pop-up window, and click the **Connect** button again, the pop-up window is blank. This is a bug that's in our backlog.

## How authentication works

When Canva sends an HTTP request to an extension, the body of the request includes the ID of the current user. An extension uses this ID to check if it's associated with a user in a third-party platform's backend.

If the ID **is** associated with a user, it can load the extension with content or options specific to that user. For example, a content extension may only retrieve content belonging to that user.

If the ID **is not** associated with a user, the extension can render a **Connect** button, which, once the user clicks, begins the authentication flow. How an extension handles the authentication flow depends on the extension point. To learn more, see the extension-specific guides:

  * [Authentication for content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/)
  * [Authentication for publish extensions](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)



The authentication flow is:

  1. A user clicks on the **Connect** button.
  2. Canva opens a pop-up window and redirects them to the app's **Redirect URL**. You can configure this URL via the Developer Portal.
  3. The **Redirect URL** takes the user to a page that's hosted on the third-party platform. This page must let users sign up for or log in to an account with the platform.
  4. The user logs in at the redirect URL location.
  5. Canva appends a `user` parameter to the **Redirect URL**. This parameter contains the ID of the current Canva user. Canva uses this parameter to associate the user in Canva's backend with the user in the platform's backend.
  6. The extension redirects the user back to Canva from within the pop-up window. This closes the pop-up window and reloads the extension.
  7. Once again, the extension receives a request that contains the ID of the user. Since this user is now associated with a user in the platform's backend, it can load with content or options specific to that user.



Canva's platform is designed to support all methods of authentication, so it doesn't matter how users sign up or log in via the pop-up window, but some common methods include:

  * Username and password
  * OAuth 2.0
  * QR codes



For guidelines on providing a friendly and familiar-looking **Redirect URL** , see [Provide a user-friendly Redirect URL](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/#provide-a-user-friendly-redirect-url).

## Team-scoped authentication

All Canva users can be a member of one or more [teams⁠(opens in a new tab or window)](https://www.canva.com/help/article/create-teams). Canva includes the ID of the user's current team in all requests it sends to an extension. This lets the extension offer team-specific features.

Canva's APIs refers to the user's team as their _brand_.

## Limitations

  * You can only enable authentication for an entire app, not an individual extension.



## Additional considerations

  * The ID of the user is obfuscated and unique to each app. If the same user authenticates with a different app, their ID is different.
  * The ID of the user is unique to each team. If a user switches to a different team and uses the same app, their ID is different.
  * The authentication flow of [public apps](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/) must adhere to the [UX guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/). When you [submit an app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/), Canva checks that the app is following these guidelines.
  * When a user starts an authentication flow, Canva redirects them to the app's **Redirect URL**. The app must [verify the request signature](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/) of this request.


