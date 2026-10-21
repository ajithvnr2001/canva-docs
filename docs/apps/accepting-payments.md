---
url: https://www.canva.dev/docs/apps/accepting-payments/
title: External payment links - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:39.226925+00:00
---

# External payment links - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/accepting-payments/

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

# External payment links

How to monetize apps by accepting payments from users.

Copy page

Want to offer exclusive features or content outside of Canva? While our SDK doesn't support in-app purchases, you're free to direct users to pay through your own site.

This page covers accepting payments from apps inside Canva.

**Check out the[Monetization status design guidelines](https://www.canva.dev/docs/apps/design-guidelines/monetization-status/)**

Our design guidelines help you create a high-quality app that easily passes app review.

![](https://www.canva.dev/_next/static/media/fundamentals.dda3a961.png)

## How to accept payments

### Step 1: Authenticate the user

For an app to accept payments from a user, it must create a link between the user in Canva and the user in the app's backend. The app can then:

  * Identify if the user is a paying customer.
  * Prompt free users with a call-to-action to become paying customers.
  * Provide paying customers with exclusive content and features.



This is made possible by the Canva Developers SDK authentication mechanisms.

To learn more, see [Authenticating users](https://www.canva.dev/docs/apps/authenticating-users/).

### Step 2: Check if the app can link to a payment flow

Canva, and therefore apps inside Canva, are available on multiple platforms. Some of those platforms, however, only allow payment-related actions that use their own payment mechanisms. This means apps inside Canva are sometimes not allowed to display payment links or similar call-to-actions.

To identify if the app is running on a platform that allows linking to payment flows:

  1. Import the `getPlatformInfo` function from the `@canva/platform` package:
         
         import { getPlatformInfo } from "@canva/platform";

TS

Copy

  2. Call the `getPlatformInfo` function:
         
         const info = getPlatformInfo();

TS

Copy

This function returns an object with a `canAcceptPayments` property:
         
         console.log(info.canAcceptPayments);

TS

Copy

The property is `true` if the app is running on a platform that allows linking to payment flows.

  3. Use a conditional to check the value of the `canAcceptPayments` property:
         
         if (info.canAcceptPayments) {
         
           console.log("The platform allows linking to payment flows!");
         
         } else {
         
           console.log("The platform doesn't allow linking to payment flows.");
         
         }

TS

Copy




### Step 3: Show a call-to-action

Based on the value of `canAcceptPayments`, show the most appropriate call-to-action:

  * If `canAcceptPayments` is `true`, link to a payment flow. You'll need to use the `requestOpenExternalUrl` method in conjunction with the `Button` or `Link` component. To learn more, see [External links](https://www.canva.dev/docs/apps/design-guidelines/external-links/).
  * If `canAcceptPayments` is `false`, ask the user to open the app in their web browser.



The following code sample demonstrates how to implement this behavior:
    
    
    import { Alert, Link } from "@canva/app-ui-kit";
    
    import { getPlatformInfo, requestOpenExternalUrl } from "@canva/platform";
    
    
    
    
    const UPGRADE_URL = "https://www.example.com/upgrade";
    
    
    
    
    export function App() {
    
      return (
    
        <div>
    
          <UpgradeLink />
    
        </div>
    
      );
    
    }
    
    
    
    
    function UpgradeLink() {
    
      const info = getPlatformInfo();
    
    
    
    
      if (info.canAcceptPayments) {
    
        async function handleClick() {
    
          await requestOpenExternalUrl({
    
            url: UPGRADE_URL,
    
          });
    
        }
    
    
    
    
        return (
    
          <Link href={UPGRADE_URL} requestOpenExternalUrl={handleClick}>
    
            Upgrade
    
          </Link>
    
        );
    
      }
    
    
    
    
      return (
    
        <Alert tone="info">
    
          Open this app in a web browser to learn how to upgrade.
    
        </Alert>
    
      );
    
    }

TSX

Copy

## Handle uninstalls

When a user uninstalls your app, we recommend automatically canceling any active subscriptions and notifying the user that their billing has stopped. This prevents ghost subscriptions where users continue to be billed for an app they no longer use.

To detect uninstalls, configure an uninstall webhook in the Developer Portal. For setup instructions, see [Handle disconnections](https://www.canva.dev/docs/apps/authenticating-users/frictionless/#step-4-handle-disconnections).

## API reference

  * [`auth.getCanvaUserToken`](https://www.canva.dev/docs/apps/api/latest/user-auth-get-canva-user-token/)
  * [`auth.requestAuthentication`](https://www.canva.dev/docs/apps/api/v1/user-auth-request-authentication/)
  * [`getPlatformInfo`](https://www.canva.dev/docs/apps/api/latest/platform-get-platform-info/)
  * [`requestOpenExternalUrl`](https://www.canva.dev/docs/apps/api/latest/platform-request-open-external-url/)


