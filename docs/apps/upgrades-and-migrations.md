---
url: https://www.canva.dev/docs/apps/upgrades-and-migrations/
title: Upgrades and migrations - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:44.949312+00:00
---

# Upgrades and migrations - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/upgrades-and-migrations/

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

# Upgrades and migrations

Keep your app up to date with the latest Canva features and best practices.

Copy page

As the Canva Developers SDK evolves, we release new versions of the SDK, App UI Kit, and introduce new patterns to improve app performance, compatibility, and developer experience. This section provides guides to help you upgrade your apps to use the latest features and APIs.

## Available migrations

The following migration guides are available to help you upgrade your app:

  * **[Apps SDK v2](https://www.canva.dev/docs/apps/upgrades-and-migrations/v2-migration-guide/)** : Migrate your app from Apps SDK v1 to v2, which includes breaking changes and new APIs.
  * **[Design Editor intent](https://www.canva.dev/docs/apps/upgrades-and-migrations/design-editor-migration-guide/)** : Migrate your app from the legacy direct render pattern to the standardized Design Editor intent pattern.
  * **[App UI Kit v5](https://www.canva.dev/docs/apps/upgrades-and-migrations/app-ui-kit-v5-migration/)** : Migrate your app from App UI Kit v4 to v5, which includes a new design token system and component updates.
  * **[@canva/app-scripts](https://www.canva.dev/docs/apps/upgrades-and-migrations/app-scripts-migration-guide/)** : Migrate your app from a legacy webpack setup to `@canva/app-scripts`, the package that powers `canva apps start` and `canva apps build`.



## Automated migrations with the Canva CLI

The [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/#migrate) includes an automated migration tool that can handle most of the code changes required for these upgrades. The `canva apps migrate` command analyzes your app's code and automatically updates:

  * Package imports and versions
  * API method signatures
  * Component properties and design tokens
  * App configuration files



### Using the migrate command

To use the automated migration tool:

  1. Install the Canva CLI if you haven't already:
         
         npm install -g @canva/cli@latest

SHELL

Copy

  2. In your app directory, run the migrate command with the migration name:
         
         canva apps migrate <migrationName>

SHELL

Copy




### Example

To migrate your app to Apps SDK v2:
    
    
    canva apps migrate apps-sdk-v1-v2

SHELL

Copy

The tool will analyze your code, make the necessary changes, and provide a summary of what was updated. After running the migration, review the changes and test your app to ensure everything works as expected.

While the automated migration tool handles most changes, some migrations may require additional manual steps. Always refer to the specific migration guide for complete instructions.

## Next steps

  * Review the specific migration guide for your upgrade.
  * Learn more about the [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/).
  * Check the [API reference](https://www.canva.dev/docs/apps/api/latest/) for the latest API documentation.


