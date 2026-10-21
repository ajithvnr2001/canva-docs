---
url: https://www.canva.dev/docs/apps/app-configuration/collaboration/
title: Collaboration - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:19.267867+00:00
---

# Collaboration - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/app-configuration/collaboration/

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

# Collaboration

How to collaborate on apps with your team.

Copy page

App collaboration allows multiple team members to build, test, and manage apps together in the Developer Portal.

## Prerequisites

  * You must have a **Canva Teams** or **Canva Enterprise** plan. See [Canva plans⁠(opens in a new tab or window)](https://www.canva.com/pricing).
  * Users must join your Canva team before you can add them as app collaborators. Team admins or owners can invite users from [Canva team settings⁠(opens in a new tab or window)](https://www.canva.com/settings/people).
  * You must be an app owner or manager to add, remove, and edit collaborators.



## Adding collaborators

  1. Navigate to your app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).
  2. Go to **Manage > Collaborators**.
  3. Select **Add collaborators**.
  4. Choose the team members you want to add. You can only add collaborators from within your Canva team.



When you add a collaborator, they immediately gain access. They will see the app listed in their [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).

## Collaborator roles

There are 3 collaborator roles, listed from lowest to highest privilege:

Role| Permissions  
---|---  
Member| 

  * Can edit **all** app fields (for example, Code upload, App listing details, Your details).
  * Can preview the app.
  * Can submit the app for review, release it, and create a new version.
  * Can view **all** app versions, including previous versions.

  
Manager| 

  * All Member permissions.
  * Can add and remove collaborators.
  * Can change collaborators' roles.

  
Owner| 

  * All Manager permissions.
  * Can delete the app.

  
  
## Managing collaborators

You must be an app owner or manager to change roles or remove collaborators.

### Changing collaborator roles

  1. Navigate to your app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).
  2. Go to **Manage > Collaborators**.
  3. Find the collaborator whose role you want to change.
  4. Select the drop-down next to their current role.
  5. Select the new role.



### Removing collaborators

  1. Navigate to your app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).
  2. Go to **Manage > Collaborators**.
  3. Find the collaborator you want to remove.
  4. Select the drop-down next to their current role.
  5. Select the **Remove collaborator** option.



When a collaborator is removed, they immediately lose access to the app.

### Transferring ownership

You must be the current app owner to transfer ownership.

  1. Navigate to your app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).
  2. Go to **Manage > Collaborators**.
  3. Find the collaborator you want to make the new owner.
  4. Select the drop-down next to their current role.
  5. Select the **Owner** option.



After transferring ownership, your role changes to **Manager**.

## Using the Canva CLI with collaborators

When multiple collaborators manage the same app, review the confirmation diff carefully before confirming a `canva apps config push` or `canva apps config pull`. Both commands perform a full replacement, of the Developer Portal on push, or your local file on pull, so confirming without checking the diff can discard changes you didn't intend to touch: a collaborator's Developer Portal edits on push, or your own local edits on pull. Run `canva apps config status` first if you want to check for changes without applying anything.

Using `--force` or a non-interactive `--strategy` skips the confirmation diff entirely. Without it, a stale local file can overwrite a collaborator's changes on the Developer Portal, including intent enrolments.

For more information, see [App configuration](https://www.canva.dev/docs/apps/app-configuration/).

## Limitations

  * There's a maximum of **49** collaborators per app.
  * Collaborators don't have access to the JSD support ticket created when submitting an app for review.
  * If a team's Canva Teams or Enterprise subscription expires, the app reverts to a single-user app, where only the owner can access it. When the subscription is renewed, all collaborators regain access.


