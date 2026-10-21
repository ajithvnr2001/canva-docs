---
url: https://www.canva.dev/docs/apps/versioning-apps/
title: App versioning - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:48.113061+00:00
---

# App versioning - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/versioning-apps/

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

# App versioning

How to create a new version of an app.

Copy page

Once an app is [released](https://www.canva.dev/docs/apps/releasing-apps/), or if it's rejected during the review process, you can't make changes to the app. However, you can create a new version of it.

When you create a new version of a _released_ app, both versions of the app appear in the Developer Portal until you release another new version. When the new version is released, the previous version is no longer available.

If you create a new version of a _rejected_ app, the new version of the app is displayed instead of the previous version, and the previous version is no longer available.

An app can have, at most, two versions: the current version and the previous version.

An app's version is separate from the [REST API version](https://www.canva.dev/docs/apps/rest-apis/versions/) that the app calls. Creating a new version of an app doesn't change which REST API version it uses.

## Create a new version of an app

  1. Log in to the Developer Portal.
  2. Navigate to the **Your apps** page.
  3. Click **Create a new version**.



Creating a new version of an app creates a complete copy of the existing app, including its metadata. Nothing is lost between versions.

You can only create new versions of apps that are in the **Rejected** or **Released** state. If the **Create a new version** button isn't available, verify that it's in a supported state.
