---
url: https://www.canva.dev/docs/apps/handling-disabled-apps/
title: Disabled apps - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:01.807998+00:00
---

# Disabled apps - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/handling-disabled-apps/

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

# Disabled apps

What to do if your app is disabled.

Copy page

After an app has been [released](https://www.canva.dev/docs/apps/releasing-apps/), it may need to be disabled in response to some sort of issue, such as a security incident. When this happens, the app will be hidden from both new and existing users.

The details of how apps are disabled (and re-enabled) depend on whether it's a public app or a private app.

This page covers disabling and re-enabling apps inside Canva.

## Public apps

### Who disables public apps?

Public apps can be disabled by members of Canva's app review team.

### Why are public apps disabled?

There are many reasons why an app may be disabled, and it's not practical to describe every possible reason, but these are some examples of possible reasons:

  * The app has a security issue.
  * The app relies on a backend that is not responding to requests.
  * The app has a significant bug.



### What happens when a public app is disabled?

  1. The app is hidden from new and existing users.
  2. The owner of the app receives an email that explains why the app was disabled.
  3. A ticket is created in Jira Service Desk (JSD) for communication between Canva and the owner of the app.



### How to re-enable public apps

The steps for re-enabling a public app depend on the type of change that needs to be made to the app.

#### Scenario #1

If a change to the app's frontend source code or Developer Portal configuration is required:

  1. [Create a new version of the app](https://www.canva.dev/docs/apps/versioning-apps/).
  2. Make the required change by uploading a new bundle and/or updating the app's configuration.
  3. Submit the new version of the app for review.



If Canva approves the new version, it will replace the disabled version.

#### Scenario #2

Sometimes, a change to the app's frontend source code or Developer Portal configuration is not required. For example, it might be that only the app's backend needs to be updated.

In this scenario:

  1. Make the required change without creating a new version of the app.
  2. Use the JSD ticket to inform Canva that the change has been made.



After Canva has confirmed that the change has been made, the app will be enabled.

## Private apps

### Who disables private apps?

Private apps can be disabled by the owner or an administrator of a team.

### Why are private apps disabled?

The reasons a private app may be disabled depend entirely on the team. Canva is not involved in the disabling or enabling of private apps, so any standards will be set within the team itself.

### What happens when a private app is disabled?

  1. The app is hidden from new and existing users.
  2. The owner of the app receives an email that explains why the app was disabled.



### How to re-enable private apps

The steps for re-enabling a private app depend on the type of change that needs to be made to the app.

#### Scenario #1

If a change to the app's frontend source code or Developer Portal configuration is required:

  1. [Create a new version of the app](https://www.canva.dev/docs/apps/versioning-apps/).
  2. Make the required change by uploading a new bundle and/or updating the app's configuration.
  3. Submit the new version of the app for review.



If the owner or an administrator of the team approves the new version, it will replace the disabled version.

#### Scenario #2

Sometimes, a change to the app's frontend source code or Developer Portal configuration is not required. For example, it might be that only the app's backend needs to be updated.

In this scenario:

  1. Make the required change without creating a new version of the app.
  2. Use the JSD ticket to inform Canva that the change has been made.



After the owner or an administrator of the team has confirmed that the change has been made, they can re-enable the app via the **Account settings > Team apps** page.
