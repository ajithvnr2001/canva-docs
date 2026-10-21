---
url: https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/
title: Optimizing the authentication flow - UX guidelines - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:47.475213+00:00
---

# Optimizing the authentication flow - UX guidelines - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/

UX guidelines

[Overview](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/)[UX guidelines for content extensions](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/content-extensions/)[UX guidelines for publish extensions](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/)[Writing copy for your app](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/copy/)[Optimizing the authentication flow](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/)

# Optimizing the authentication flow

Guidelines for creating a great authentication experience.

Copy page

Apps can require users to [authenticate](https://www.canva.dev/docs/extensions/platform-concepts/authentication/) with a third-party platform before gaining access to the app's features. This page contains some guidelines for creating a delightful authentication flow.

## Let users sign up (or log into) an account

![](https://www.canva.dev/_next/static/media/img-e04323547a.0d06e13b.svg)

When a user starts the authentication flow, provide an option to sign up for or log into an account with the third-party platform. Don't assume that the user already has (or doesn't have) an account. Also provide an option to reset or retrieve the password.

Consider offering a trial for signups, as it increases the usage. If signup isn't supported via the app, inform the users or provide a link where they can learn more about the platform and register.

Username and password are preferred to API keys and other forms of credentials. All successful signups and logins must lead to the app.

## Support authentication on non-desktop devices

![](https://www.canva.dev/_next/static/media/img-c302b13886.8c1474ae.svg)

A lot of people exclusively use Canva on non-desktop devices, such as smartphones. Knowing this, the authentication flow should be as delightful as possible on various hardware and screen resolutions. Consider using a responsive design that adjusts itself automatically to various screen sizes.

## Keep it simple and fit for purpose

![](https://www.canva.dev/_next/static/media/img-b6fe4959d6.6a9930e2.svg)

Everything you do in the authentication flow must be relevant to authentication (signups, logins, password resets, terms and conditions, etc) and must lead the users to the app. Don't include anything that'll disrupt or unnecessarily let users escape the authentication flow.

If sign-up isn't supported, you can include a link where users can learn more about the third-party platform. This helps when users discover the app via Canva instead of the third-party platform.

If you must add more links, keep the list short. Open all links in a separate window so that users can return to the authentication flow anytime.

## Title the authentication window

![](https://www.canva.dev/_next/static/media/img-dfeded428d.066f2d8b.svg)

Although the intent of the authentication flow is obvious, we recommend adding a title to the authentication window. This ensures consistency with the other screens. This also helps users switch back to the authentication flow if they open any links (pricing, privacy policy, etc) in a different window.

The window title must:

  * Be short and meaningful.
  * Not include any special characters.
  * Not have "Untitled", "Canva Login", and similar titles that mislead the user.



## Rely on explicit connection

![](https://www.canva.dev/_next/static/media/img-237a604318.2abe4105.svg)

Users must log in to the app explicitly via the authentication flow. If there's an existing active session with the third-party platform, don't use it to automatically connect to the app. Instead, inform the users a connection exists, show the permissions Canva has on the account, and provide options to continue, exit, or change the account.

## Provide clear, actionable error messages

![](https://www.canva.dev/_next/static/media/img-0f747f5649.df5302dd.svg)

A lot of things can go wrong during an authentication flow, such as entering an incorrect password or trying to log in with a username that doesn't exist. To minimize frustration, provide clear error messages that explain what went wrong and how the user can fix it.

## Avoid dead-ends and endless loops

![](https://www.canva.dev/_next/static/media/img-470b5f0503.b42fa7a7.svg)

Don't leave users stranded in an endless rabbit hole or stranded in an unfixable error state. Thoroughly test the authentication flow for edge-cases and make it easy for the user to eject from (or restart) the flow if something does go wrong.

## Keep the connection to the app intact

![](https://www.canva.dev/_next/static/media/img-668b31e40f.2818a3b2.svg)

If a user is already authenticated and logged in to an app:

  * Proceed to the app directly without prompting them to sign up or log in.
  * Retain the connection even if the app is reloaded or the browser is refreshed. This ensures the authentication status endpoints are properly implemented.
  * Use the same connection for all extension types of the app (content, publish). Authenticating with one must hold good for the other.



## Let users revoke their permissions

![](https://www.canva.dev/_next/static/media/img-7806d16b0c.058823a7.svg)

When a user authenticates, they must be able to revoke that authentication at any point in time. They must also have the option to re-authenticate with the same (or a different) account at a later point in time.

To learn about the endpoint for de-authenticating users, see [POST /configuration/delete](https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/).

## Provide a user-friendly Redirect URL

![](https://www.canva.dev/_next/static/media/img-33c0d048fc.a4ffe908.svg)

If a user starts an authentication flow on an iOS device, iOS shows them the domain name of the **Redirect URL**. If the **Redirect URL** is a strange-looking URL, like that of an AWS bucket, users may be hesitant to continue authenticating. For this reason, we require apps to have a **Redirect URL** that looks friendly and familiar.

For more details, see [redirecting content extension users](https://www.canva.dev/docs/extensions/extensions/content-extensions/authentication/#step-3-redirect-users-to-the-redirect-url) and [redirecting publish extension users](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/#step-3-redirect-users-to-the-redirect-url).

## Don't auto-subscribe users to marketing communication

![](https://www.canva.dev/_next/static/media/img-de2460bb65.85eec995.svg)

During an authentication flow, apps must not opt users into marketing communications by default. At most, apps can allow users to opt into communications. Users must also be able to unsubscribe from communications at any time.
