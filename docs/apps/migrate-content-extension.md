---
url: https://www.canva.dev/docs/apps/migrate-content-extension/
title: Migrate a content extension - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:11.960253+00:00
---

# Migrate a content extension - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/migrate-content-extension/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Migrate a content extension

How to migrate your content extension to use the Canva Developers SDK.

Copy page

[Content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/) are being deprecated in favor of the [Canva Developers SDK](https://www.canva.dev/docs/apps/apps-inside-canva/). To help you migrate to the Developers SDK, Canva has created [a template⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/tree/main/examples/assets_and_media/digital_asset_management) that demonstrates how to build a digital asset management (DAM) app.

As part of the migration process, you’ll need to configure CORS, remove signature verification, and add support for user authentication, among other steps.

To see how you can customize the app's UI, see the [SearchableListView⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-templates/storybook/?path=/docs/app-components-searchable-list-view-searchablelistview--docs) component.

## Step 1: Create a new app

Create a new app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps). You'll use this app ID to configure your settings in the next steps. For more information, see [Quickstart](https://www.canva.dev/docs/apps/quickstart/).

## Step 2: Clone the repo and install dependencies

This step explains how to clone the example repository and install the npm dependencies.

The starter kits for apps inside Canva (previously known as the Apps SDK) and the Canva REST APIs (previously known as the Connect APIs) are being combined in a future update. The steps here continue to work until that happens, and will be updated in the future.

  1. Clone the [canva-sdks/canva-apps-sdk-starter-kit⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-apps-sdk-starter-kit) repo.
         
         git clone git@github.com:canva-sdks/canva-apps-sdk-starter-kit.git

BASH

Copy

  2. Install the npm dependencies.
         
         npm install

BASH

Copy




## Step 3: Configure the environment

Open the `.env` file and add your backend server’s details. For more information, see [Previewing apps](https://www.canva.dev/docs/apps/previewing-apps/#automatic).
    
    
    CANVA_FRONTEND_PORT=8080
    
    CANVA_BACKEND_PORT=3001
    
    CANVA_BACKEND_HOST=https://my-backend/
    
    CANVA_APP_ID=<your App ID>
    
    CANVA_HMR_ENABLED=FALSE

Copy

  * `CANVA_BACKEND_HOST`: The URL of your backend server.
  * `CANVA_APP_ID`: To find this value, open [Your apps⁠(opens in a new tab or window)](https://www.canva.com/developers/apps), find the app you created in step 1, and copy the ID from the **App ID** column.
  * `CANVA_HMR_ENABLED`: You can optionally enable Hot Module Replacement (HMR). For more information, see [Previewing apps](https://www.canva.dev/docs/apps/previewing-apps/)



## Step 4: Preview your app

Run the app locally to preview your changes. For more information, see [Previewing apps](https://www.canva.dev/docs/apps/previewing-apps/). If you haven’t already created an app, see [Quickstart](https://www.canva.dev/docs/apps/quickstart/) to create one.

  1. Start the local preview:
         
         npm start:example digital_asset_management

BASH

Copy




Then preview the app from the Developer Portal, which opens the Canva editor in a new tab with a preview of your app in the sidebar. In [Your apps⁠(opens in a new tab or window)](https://www.canva.com/developers/apps), select your app, then:

  1. On the app's **Inside Canva** page, set **Code upload > App source > Development URL** to the address of your local development server.

The URL must point directly to a standalone JavaScript file. This field exists only for development: you can't submit an app for review while it holds a value.

  2. Click **Preview**.

The app opens in a new tab. Apps use the [Design Editor](https://www.canva.dev/docs/apps/intents/design-editor/) intent by default; if your app implements another intent, or more than one, choose which to preview under **Preview options > Choose an intent**, beside **Preview**.

  3. The first time you open an app you have to connect it. Click **Open** , and the app loads in the iframe.




You only need to connect the app once.

To preview your app with Safari, see [Using HTTPS](https://www.canva.dev/docs/apps/previewing-apps/#using-https).

## Step 5: Configure CORS

Configure your CORS header by applying the configuration at [Cross-Origin Resource Sharing](https://www.canva.dev/docs/apps/cross-origin-resource-sharing/).

## Step 6: Add user authentication

Update your app to add [user authentication](https://www.canva.dev/docs/apps/authenticating-users/). Frictionless authentication is not available for this type of app, so you’ll need to use [manual authentication](https://www.canva.dev/docs/apps/authenticating-users/manual/) with a third-party platform.

## Step 7: Remove signature verification

Update your legacy extension to remove the signature verification code. You can do this by removing the `isValidPostRequest` and `isValidGetRequest` steps. For more information, see [Signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/).
    
    
    app.post("/content/resources/find", async (request, response) => {
    
    -  if (!isValidPostRequest(process.env.CLIENT_SECRET, request)) {
    
    -    response.sendStatus(401);
    
    -    return;
    
    -  }
    
      response.send({
    
        type: "SUCCESS",
    
        resources: [],
    
      });
    
    });

DIFF

Copy

## Step 8: Update config.ts

Edit your [config.ts⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/blob/main/examples/digital_asset_management/config.ts) to remove any configuration settings that you don't need. For more information, see the `config` settings in [SearchableListView⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-templates/storybook/?path=/docs/app-components-searchable-list-view-searchablelistview--docs).

## Next steps

  * To organize your content for a Digital Asset Management (DAM) app, see the [example app](https://www.canva.dev/docs/apps/app-templates/digital-asset-management/#step-3-customize-the-dam-app). 
    * The DAM app template uses the [SearchableListView](https://www.canva.dev/docs/apps/app-components/searchable-list-view/) component in the background to let users navigate your content using filters and search. You might want to use this component in your app directly.
    * To learn about the capabilities, see the [SearchableListView⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-templates/storybook/?path=/story/app-components-searchable-list-view-searchablelistview--searchable-list-view) storybook.
  * When your app is ready, submit it on the Developer Portal. For more information, see [Submitting apps](https://www.canva.dev/docs/apps/submitting-apps/).


