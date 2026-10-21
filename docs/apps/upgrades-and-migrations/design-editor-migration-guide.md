---
url: https://www.canva.dev/docs/apps/upgrades-and-migrations/design-editor-migration-guide/
title: Design Editor intent upgrade guide - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:45.926930+00:00
---

# Design Editor intent upgrade guide - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/upgrades-and-migrations/design-editor-migration-guide/

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

# Design Editor intent upgrade guide

How to upgrade to the Design Editor intent pattern.

Copy page

This guide explains all of the code changes required to upgrade from the legacy direct render pattern to the new Design Editor intent pattern. The Design Editor intent provides a standardized way to render apps within the Canva editor and ensures better compatibility with future Canva features.

## Automated migration tool

You can use the [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/) automated migration tool to handle most of the required changes. The CLI automatically updates:

  * Package installation for `@canva/intents`
  * Import statements to include `prepareDesignEditor`
  * Render function to use `async`/`await`
  * Code change to wrap render logic in an object to implement the `DesignEditorIntent` type.
  * Code structure changes to match the recommended practices for [intents](https://www.canva.dev/docs/apps/intents/) by creating `src/intents/design_editor/index.tsx`.
  * Code change to call `prepareDesignEditor()` in the `src/index.tsx` file which imports the implementation of the `DesignEditorIntent` type.
  * App manifest configuration in Developer Portal



For detailed CLI usage, see the [Canva CLI documentation](https://www.canva.dev/docs/apps/canva-cli/#migrate).

### Run the migration tool

  1. If you haven't already, install the Canva CLI:
         
         npm install -g @canva/cli@latest

SHELL

Copy

  2. In your app directory, run the migration command:
         
         canva apps migrate design-editor-intent

SHELL

Copy




After running the automated migration, review the changes and complete any manual steps outlined in the following sections.

## Manual migration steps

The following sections explain the specific code changes if you prefer to upgrade manually or need to handle cases not covered by the automated tool.

### Install the @canva/intents package

The Design Editor intent requires the `@canva/intents` package. Install it by running:
    
    
    npm install @canva/intents@latest

SHELL

Copy

### Update your app's index file

The main code change involves updating how your app initializes and renders its UI. We recommend this happens in a new `src/intents/design_editor/index.tsx` file, which is imported from `src/index.tsx`.

#### Before: Direct render pattern

In the legacy pattern, apps directly called the render function:
    
    
    import { createRoot } from "react-dom/client";
    
    import { App } from "./app";
    
    
    
    
    const root = createRoot(document.getElementById("root"));
    
    
    
    
    function render() {
    
      root.render(<App />);
    
    }
    
    
    
    
    render(); // Direct function call

TSX

Copy

#### After: Design Editor intent pattern

With the Design Editor intent, you implement the intent contract in `src/intents/design_editor/index.tsx` and call `prepareDesignEditor()` in `src/index.tsx`:
    
    
    import type { DesignEditorIntent } from "@canva/intents/design";
    
    import { createRoot } from "react-dom/client";
    
    import { App } from "./app";
    
    import { prepareDesignEditor } from "@canva/intents/design";
    
    
    
    
    const root = createRoot(document.getElementById("root"));
    
    
    
    
    async function render() {
    
      root.render(<App />);
    
    }
    
    
    
    
    const designEditor: DesignEditorIntent = { render };
    
    export default designEditor; // default export the intent contract

TSX

Copy

This new file should be imported from `src/index.tsx`:
    
    
    import { prepareDesignEditor } from "@canva/intents/design";
    
    
    
    
    import designEditor from "./intents/design_editor";
    
    
    
    
    prepareDesignEditor(designEditor);

TSX

Copy

The key changes are:

  1. **Import`prepareDesignEditor`** from `@canva/intents/design` in `src/index.tsx`
  2. **Export the designEditor** implementation object from `src/intents/design_editor/index.tsx`
  3. **Make render function async** by adding the `async` keyword
  4. **Replace direct render call** with `prepareDesignEditor(designEditor)`



### Enable the Design Editor intent

After updating your code, you need to enable the Design Editor intent in your app's configuration.

You can configure intents for your app with either the Developer Portal or the Canva CLI:

Developer PortalDeveloper Portal

Canva CLICanva CLI

To enable the Design Editor intent:

  1. Navigate to an app via the [Your apps⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) page.
  2. Go to **Inside Canva**. If the app already has an intent, select **Intents** beneath it.
  3. Under **Available intents** , find the "Design Editor" intent and click **Set up**.
  4. In the **Set up Design Editor** dialog, click **Add Design Editor**. This guide walks you through implementing the intent in your code.



  1. Set up your app to use the Canva CLI to manage settings using the [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/#manage-configuration-using-the-canva-cli) file.

  2. Set the `intent.design_editor` property to be enrolled. For more information, see [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/#intent-optional).
         
         {
         
           "intent": {
         
             "design_editor": {
         
               "enrolled": true
         
             }
         
           }
         
         }

JSON

Copy

  3. Push the configuration to the Developer Portal:
         
         canva apps push

SHELL

Copy




### Advanced: Custom render implementation

If your app has a more complex rendering setup, you may need to adapt the pattern accordingly. The `render` function in the `DesignEditorIntent` can contain any initialization logic your app needs:
    
    
    import type { DesignEditorIntent } from "@canva/intents/design";
    
    import { createRoot } from "react-dom/client";
    
    import { AppUiProvider } from "@canva/app-ui-kit";
    
    import { App } from "./app";
    
    import "@canva/app-ui-kit/styles.css";
    
    
    
    
    async function render() {
    
      // Find the root element
    
      const rootElement = document.getElementById("root");
    
      if (!rootElement) {
    
        throw new Error("Unable to find element with id of 'root'");
    
      }
    
    
    
    
      // Create React root
    
      const root = createRoot(rootElement);
    
    
    
    
      // Render your app with any providers
    
      root.render(
    
        <AppUiProvider>
    
          <App />
    
        </AppUiProvider>
    
      );
    
    };
    
    
    
    
    const designEditor: DesignEditorIntent = { render };
    
    export default designEditor; // default export the intent contract

TSX

Copy

### Update tests

If your app has tests that verify the rendering behavior, you'll need to update them to account for the new pattern:

**Before:**
    
    
    import { render } from "./index";
    
    render(); // Called directly in tests

TSX

Copy

**After:**
    
    
    import { prepareDesignEditor } from "@canva/intents/design";
    
    // Tests should mock prepareDesignEditor or test the render function passed to it

Copy

## Verify the migration

After completing the migration:

  1. **Build your app** to check for TypeScript errors:
         
         canva apps build

SHELL

Copy

  2. **Preview your app** in the Canva editor:
         
         canva apps preview

SHELL

Copy

  3. **Test functionality** by opening your app in Canva and verifying it loads correctly.



