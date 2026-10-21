---
url: https://www.canva.dev/docs/apps/suspension/
title: Suspension - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:44.641243+00:00
---

# Suspension - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/suspension/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Suspension

An introduction to suspension for apps inside Canva.

Copy page

Suspension applies to apps inside Canva.

When a user navigates away from an app, Canva attempts to suspend the app rather than closing it entirely. When the user returns to the app, they can then can continue from where they left off.

This mimics the user experience of Canva's native features.

**Check out the[Suspension design guidelines](https://www.canva.dev/docs/apps/design-guidelines/suspension/)**

Our design guidelines help you create a high-quality app that easily passes app review.

![](https://www.canva.dev/_next/static/media/developing-apps-other.00aad9b5.png)

## How suspension works

When an app is suspended:

  * The app's iframe is hidden from view.
  * The process injected into the iframe remains active but is placed in a `"suspended"` state.



To see this in action:

  1. Open an app.
  2. Interact with the app in some way, such as by entering a value into a text field.
  3. Switch to a different tab in the editor, such as the **Elements** tab.
  4. Switch back to the app.



You should see that the app has remained open and maintained its state.

## Resource limits

While an app is suspended, it continues to consume some resources. Because of this, there are limits to the number of apps that can be running at any point in time. The exact limit depends on the device and may change over time.

The important thing to understand is that suspension is not guaranteed. It's done on a "best effort" basis. If too many resources are consumed, the app's process will be terminated to avoid performance issues.

## Restricted APIs

While an app is suspended, some features of the Canva Developers SDK are not available, including but not limited to:

  * APIs that attempt to access design data.
  * APIs that attempt to access user data.
  * APIs that require user interaction.



In addition, the following restrictions apply to standard web APIs:

  * Audio playback is paused.
  * Video playback is paused.



If an app attempts to call an unavailable API, the SDK throws an `CanvaError` with an error code of `"not_allowed"`:
    
    
    import { addElementAtPoint } from "@canva/design";
    
    import { CanvaError } from "@canva/error";
    
    
    
    
    try {
    
      await addElementAtPoint({
    
        type: "embed",
    
        url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    
      });
    
    } catch (error) {
    
      if (error instanceof CanvaError) {
    
        // If a restricted API is called while the app is
    
        // suspended, the error code is `"not_allowed"`
    
        console.log(error.code);
    
      }
    
    }

TS

Copy

## Gotchas

  * Apps don't remain suspended across page loads. If the user reloads the page, all app processes will be terminated.


