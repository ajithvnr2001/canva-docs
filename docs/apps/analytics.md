---
url: https://www.canva.dev/docs/apps/analytics/
title: Analytics - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:40.132492+00:00
---

# Analytics - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/analytics/

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

# Analytics

How to track the discovery and usage of an app.

Copy page

After [releasing an app](https://www.canva.dev/docs/apps/releasing-apps/), it's important to understand how the app is performing. To help with this, Canva tracks metrics about an app's performance and makes these metrics available through the Developer Portal.

This page explains the available metrics and how to interpret the data.

This page covers the usage and engagement metrics for apps inside Canva.

## Viewing analytics

You can find the analytics for an app in the Developer Portal on the app's **Grow > Analytics > Usage and engagement** page. The **Grow** section is only available for public apps.

The page is available while your app is still a draft, but it has no data to show. Each metric displays an empty state until the app is released.

## What Canva tracks

The **Usage and engagement** page provides the following metrics:

  * App listing views
  * App installations
  * App usage



This section explains the meaning of each metric.

### App listing views

An _app listing view_ occurs when a user views an app's installation screen in the Canva editor.

When a user views an app's details in the [Apps Marketplace⁠(opens in a new tab or window)](https://www.canva.com/your-apps), it does _not_ count as an app listing view. In this case, a view is only counted if the user clicks the **Use in design** button.

The best way to increase app listing views is to [get featured in the Apps Marketplace](https://www.canva.dev/docs/apps/getting-featured/).

### App installations

An _app installation_ occurs when a user clicks the **Open** button on an app's installation screen.

A user uninstalling an app does not decrease the total number of installations. However, if the same user reinstalls the app within 30 days, the installation is not counted twice.

### App usage

An _app usage_ is a metric that captures how many unique users are using an app. What counts as a usage might change as the Canva Developers SDK evolves, but some examples of usages include:

  * adding an element to a design
  * uploading an asset to the user's media library
  * exporting a design



## Interpreting the data

This is an example of the data available for the **App listing views** metric:

![](https://www.canva.dev/_next/static/media/analytics.2a6aeb77.png)

Here's a breakdown of what this data shows:

  * The total number of app listing views by unique users over the last 30 days.
  * The percentage change between the last two data points.
  * The cumulative growth of the unique app listing views over the last 30 days.



## Limitations

  * Apps can't track analytics with third-party software, such as Google Analytics. This is because Canva's [Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/) prevents third-party scripts from being loaded within the app's iframe.


