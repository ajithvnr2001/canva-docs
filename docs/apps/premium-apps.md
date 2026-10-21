---
url: https://www.canva.dev/docs/apps/premium-apps/
title: Premium Apps Program - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:12.150003+00:00
---

# Premium Apps Program - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/premium-apps/

App lifecycle

[App versioning](https://www.canva.dev/docs/apps/versioning-apps/)[Canva REST API versioning](https://www.canva.dev/docs/apps/rest-apis/manage-versions/)[Disabled apps](https://www.canva.dev/docs/apps/handling-disabled-apps/)[Deep linking](https://www.canva.dev/docs/apps/deep-linking/)

Growth and performance

[Analytics](https://www.canva.dev/docs/apps/analytics/)[Getting featured](https://www.canva.dev/docs/apps/getting-featured/)

Monetization

[Overview](https://www.canva.dev/docs/apps/monetization/)[External payment links](https://www.canva.dev/docs/apps/accepting-payments/)

Premium Apps Program

[Overview](https://www.canva.dev/docs/apps/premium-apps/)[Implementing monetization](https://www.canva.dev/docs/apps/premium-apps/implementing-monetization/)[Set up payout details](https://www.canva.dev/docs/apps/payout-details/)[Design guidelines](https://www.canva.dev/docs/apps/design-guidelines/premium-apps/)[Learn more⁠(opens in a new tab or window)](https://www.canva.com/developers/premium-apps-program/)

Team and access

[App collaborators](https://www.canva.dev/docs/apps/app-configuration/collaboration/)

Upgrades and migrations

[Overview](https://www.canva.dev/docs/apps/upgrades-and-migrations/)[Apps SDK v2 Upgrade guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/v2-migration-guide/)[Apps SDK v2 Upgrade FAQ](https://www.canva.dev/docs/apps/upgrades-and-migrations/v2-migration-faq/)[Design Editor Intent Upgrade guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/design-editor-migration-guide/)[App UI Kit v5 Upgrade guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/app-ui-kit-v5-migration/)[App Scripts Upgrade guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/app-scripts-migration-guide/)

# Premium Apps Program

Monetizing apps with the Premium Apps Program.

Copy page

Do you have a great app or an idea for one, and want to earn some revenue from Canva? The [Premium Apps Program⁠(opens in a new tab or window)](https://www.canva.com/developers/premium-apps-program/) is how you partner with Canva to bring it to our community. For existing apps, you'll earn recurring revenue each month based on how often your app is used. For apps still in development, we offer grants to help cover build costs and get you to launch. Your app — or features within it — will be available to Canva paid users, and free users can upgrade to unlock everything it offers.

Apps can be:

  * **Gated** \- All of your app's features are only available with paid Canva plans, including Education and Non-Profit.
  * **Freemium** \- Your app's core features are available with Canva Free. Premium features come with paid plans including Education and Non-Profit.
  * **Credit-based** \- Your app provides a starter quota of credit. When the starter credit runs out, premium features are unlocked by upgrading to a paid Canva plan.



When you make an application to join the Premium Apps Program, Canva will help determine the access model based on our goals and platform strategy.

Here's how it works:

  1. You specify certain features of your app to be billable actions.
  2. You offer different levels of feature access based on a user’s Canva plan (for example, Free, Pro, or Business).
  3. Canva compensates you for the usage of those features.



To learn more, see [Premium Apps Program⁠(opens in a new tab or window)](https://www.canva.com/developers/premium-apps-program/).

This page covers monetization for apps inside Canva.

**Check out the[Premium apps design guidelines](https://www.canva.dev/docs/apps/design-guidelines/premium-apps/)**

Our design guidelines help you create a high-quality app that easily passes app review.

![](https://www.canva.dev/_next/static/media/developing-apps-other.00aad9b5.png)

## User experience

The following is a high-level overview of how premium apps features work:

  1. The user opens the app.

For gated apps, users on the Canva Free plan are blocked from accessing the app. Canva manages the gating and upgrade flow for this access model.

  2. The app checks if the user has a free or paid Canva plan.

  3. The user sees that certain premium features of the app require a paid Canva plan.

  4. The user attempts to access a premium feature.

  5. If the user has a free Canva plan:

     1. The app opens a dialog for upgrading to a paid plan.
     2. The user upgrades their plan.
     3. The page reloads, thereby reloading the app.
     4. Once again, the app checks if the user has a paid plan.
  6. If the user has a paid Canva plan:

     1. The app sends an HTTP request to its backend.
     2. The app backend confirms that the user has a paid plan.
     3. The app backend performs the requested operation associated with a billable action.
     4. Canva tracks the usage of billable actions, and compensates the app developer for the usage.



We recommend that apps have a backend for performing billable actions. If your app doesn't have a backend, checking that the user is enabled for the billable action is sufficient before performing the requested operation. For more information, see [Implementing monetization](https://www.canva.dev/docs/apps/premium-apps/implementing-monetization/#security-considerations).
