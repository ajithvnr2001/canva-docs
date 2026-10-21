---
url: https://www.canva.dev/docs/apps/deep-linking/
title: Deep linking - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:34.214108+00:00
---

# Deep linking - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/deep-linking/

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

# Deep linking

How to link directly to apps in the Canva editor.

Copy page

After you've [released](https://www.canva.dev/docs/apps/releasing-apps/) an app, you can create URLs that link users directly to the Canva editor with your app open to a design type or template.

  * A design type is a blank design of a set size for a particular purpose, such as an Instagram post or a photo collage.
  * A template is a design that already has elements and styles applied as a starting point.



This page covers deep linking to apps inside Canva.

## Generate a deep link

You can use the following tool to generate a deep link to your app for a design type or template. Be aware that the link will always point to the latest **released** version of the app.

App ID

[(opens in a new tab or window)](https://www.canva.com/developers/app/)

Enter an app ID from the [Your apps](https://www.canva.com/developers/apps) page or a URL from the [Apps Directory](https://www.canva.com/apps).

Deep link type

Design type

Template

Design type

Presentation

Deep link URL

Open in new tab(opens in a new tab or window)

Copy

## When to use deep links to the Canva editor

There are two ways to link to your app: a deep link, which opens your app in the Canva editor with a design, or a link to your app listing in the Canva apps tab.

You might want to use a deep link in the following situations:

  * For linking straight into the editor, so there are fewer steps to get a user interacting with your app.
  * If you know that your app is primarily used with a specific Canva design type, such as presentations or Instagram posts, so you can link to it directly.
  * For linking from ads that explain things in detail, such as a landing page or a blog, where you want to show your app working with a particular design type or template.



See the following sections for how to create deep links and some examples.

You might want to instead link to the app listing in the following situations:

  * To provide more context about what the app does, so users can understand it before trying it.
  * If you want the user to choose the design type or template themselves.
  * For linking from ads that don't explain things in detail, and to allow the user to find out the context.



For example, the [app listing for Canva's Text to Image app⁠(opens in a new tab or window)](https://www.canva.com/your-apps/text-to-image).

## Find your app's unique identifier (ui)

To create a link to your app, you must first find its unique identifier (`ui`).

The `ui` for an app is _not_ the same as the App ID listed on the [Your apps⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) page.

  1. Navigate to the [Your apps⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) page.

  2. From the list of apps, click the app that you want to get the `ui` for.

  3. Click **Preview** to open the app in a new tab.

  4. In the address bar of your browser, the URL ends with something like `/edit?ui=abCDEfg1HiJ_AbcdEFGhIjKlMnOPQRStUVwXYZA1b234C5DeFgHijK5`, where the value after `ui=` is your app's unique identifier.

Copy the `ui` value to use in the next procedures.




## Create a link to your app for a design type

To create a link to your app for a design type, you need your app's unique identifier (`ui`) and the ID of the design type you want to link to.

  1. [Find your app's unique identifier](https://www.canva.dev/docs/apps/deep-linking/#find-your-apps-unique-identifier-ui) (`ui`).

  2. Find the design type's ID.

You can see the design type's ID in the URL of a link to the design type from the Canva homepage. The design type ID is the value of the `type` parameter in the URL.

For example, as shown in the following screenshot, the design type ID for **Instagram Post (square)** is `TABQqs5Kbyc`.

![](https://www.canva.dev/_next/static/media/find-doc-type-id.2f59f72f.png)

  3. Use the following URL and replace `<TYPE-ID>` and `<APP-UI>` with their respective values from the previous steps.
         
         https://www.canva.com/login/?redirect=%2Fdesign%3Fcreate%26type%3D<TYPE-ID>%26ui%3D<APP-UI>

Copy

The preceding URL links to the Canva login page, and has a `redirect` parameter containing URL-encoded values for the design and app values. This is necessary if the user clicking on the link isn't logged in to Canva, so the URL parameters are preserved through the login process.

For example, a URL to use the 'Instagram Post (square)' design type and Canva's [Text to Image app⁠(opens in a new tab or window)](https://www.canva.com/your-apps/text-to-image) is:

<https://www.canva.com/login/?redirect=%2Fdesign%3Fcreate%26type%3DTABQqs5Kbyc%26ui%3DeyJFIjp7IkE_IjoiTiIsIkEiOiJnZW5lcmF0ZV9pbWFnZSJ9fQ>[⁠(opens in a new tab or window)](https://www.canva.com/login/?redirect=%2Fdesign%3Fcreate%26type%3DTABQqs5Kbyc%26ui%3DeyJFIjp7IkE_IjoiTiIsIkEiOiJnZW5lcmF0ZV9pbWFnZSJ9fQ)




## Create a link to your app for a template

To create a link to your app for a template, you need your app's unique identifier (`ui`) and the ID of the template you want to link to.

  1. [Find your app's unique identifier](https://www.canva.dev/docs/apps/deep-linking/#find-your-apps-unique-identifier-ui) (`ui`).

  2. Find the template's ID. When previewing a template, you can find the template ID in either of the following:

     * In the URL for the preview, the template ID is the prefix before the template name.
     * For the **Customize this template** button, you can see the template's ID in the URL that the button links to. The template ID is the value of the `template` parameter in that URL.

For example, as shown in the following screenshot, the preview for the **Clean Work Place LinkedIn Banner** shows that its template ID is `EAENvpM8lg0`.

![](https://www.canva.dev/_next/static/media/find-template-id.4f543183.png)

  3. Use the following URL and replace `<TEMPLATE-ID>` and `<APP-UI>` with their respective values from the previous steps.
         
         https://www.canva.com/login/?redirect=%2Fdesign%3Fcreate%26template%3D<TEMPLATE-ID>%26ui%3D<APP-UI>

Copy

The preceding URL links to the Canva login page, and has a `redirect` parameter containing URL-encoded values for the template and app values. This is necessary if the user clicking on the link isn't logged in to Canva, so the URL parameters are preserved through the login process.

For example, a URL to use the 'Clean Work Place LinkedIn Banner' template and Canva's [Text to Image app⁠(opens in a new tab or window)](https://www.canva.com/your-apps/text-to-image) is:

<https://www.canva.com/login/?redirect=%2Fdesign%3Fcreate%26template%3DEAENvpM8lg0%26ui%3DeyJFIjp7IkE_IjoiTiIsIkEiOiJnZW5lcmF0ZV9pbWFnZSJ9fQ>[⁠(opens in a new tab or window)](https://www.canva.com/login/?redirect=%2Fdesign%3Fcreate%26template%3DEAENvpM8lg0%26ui%3DeyJFIjp7IkE_IjoiTiIsIkEiOiJnZW5lcmF0ZV9pbWFnZSJ9fQ)



