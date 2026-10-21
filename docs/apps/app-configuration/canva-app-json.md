---
url: https://www.canva.dev/docs/apps/app-configuration/canva-app-json/
title: canva-app.json - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:19.208052+00:00
---

# canva-app.json - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/app-configuration/canva-app-json/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

API reference

[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)

App UI Kit reference

[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

Canva REST API reference

[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)

Webhooks notification reference

[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

Tools

[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)

# canva-app.json

Configuration file for Canva apps.

Copy page

The `canva-app.json` file is the configuration file for Canva apps. It defines the app's permissions, supported devices, API versions, and other runtime settings.

When you create a new app using the [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/), a `canva-app.json` file is automatically created in your project root directory with a default configuration.

The `canva-app.json` schema is expanding. In the Developer Portal, the Canva REST APIs are becoming a capability you enable on an app (see the [community announcement⁠(opens in a new tab or window)](https://community.canva.dev/t/integrations-are-becoming-part-of-apps-in-the-developer-portal-soon/8881)). Apps that use the REST APIs don't use `canva-app.json` today, and this file doesn't yet include REST API configuration for them. Support will follow in a later update, with further changes to this file expected.

## File location

The `canva-app.json` file is located in the root directory of your app project.
    
    
    my-canva-app/
    
    ├── canva-app.json
    
    ├── package.json
    
    └── src/

Copy

## Validation

The `canva-app.json` file is validated against the [JSON Schema⁠(opens in a new tab or window)](https://canva.dev/schemas/app/v1/manifest-schema.json). Most code editors with JSON Schema support provide validation and auto-completion when you include the `$schema` property.

## Properties

### `$schema` (optional)

  * **Type** : `string`
  * **Description** : JSON Schema URL for this manifest ($schema). Used by editors for validation and auto-completion.


    
    
    {
    
      "$schema": "https://www.canva.dev/schemas/app/v1/manifest-schema.json"
    
    }

JSON

Copy

### `manifest_schema_version` (required)

  * **Type** : `integer`
  * **Description** : The version of the manifest schema.


    
    
    {
    
      "manifest_schema_version": 1
    
    }

JSON

Copy

### `runtime` (required)

  * **Type** : `object`
  * **Description** : Application runtime configuration.



#### `runtime.permissions` (optional)

  * **Type** : `array`
  * **Description** : The list of permissions that this app requires to load or may ask for at runtime.



Each permission object must include:

  * `name`: The permission identifier
  * `type`: Must be `"mandatory"`



Available permissions:

  * `canva:design:content:read`: Permission to read design content
  * `canva:design:content:write`: Permission to write design content
  * `canva:asset:private:read`: Permission to read private assets
  * `canva:asset:private:write`: Permission to write private assets
  * `canva:brandkit:read`: Permission to read from the brand kit
  * `canva:brandtemplate:read`: Permission to read from brand templates



See [Configuring permissions](https://www.canva.dev/docs/apps/configuring-permissions/) for more information.
    
    
    {
    
      "runtime": {
    
        "permissions": [
    
          {
    
            "name": "canva:design:content:read",
    
            "type": "mandatory"
    
          },
    
          {
    
            "name": "canva:design:content:write",
    
            "type": "mandatory"
    
          }
    
        ]
    
      }
    
    }

JSON

Copy

### `intent` (optional)

  * **Type** : `object`
  * **Description** : Intent-specific configuration.



For more information about intents, see [Intents](https://www.canva.dev/docs/apps/intents/).

#### `intent.data_connector` (optional)

  * **Type** : `object`
  * **Description** : Configuration for the Data Connector intent.


    
    
    {
    
      "intent": {
    
        "data_connector": {
    
          "enrolled": true
    
        }
    
      }
    
    }

JSON

Copy

#### `intent.design_editor` (optional)

  * **Type** : `object`
  * **Description** : Configuration for the Design Editor intent.


    
    
    {
    
      "intent": {
    
        "design_editor": {
    
          "enrolled": true
    
        }
    
      }
    
    }

JSON

Copy

#### `intent.content_publisher` (optional)

  * **Type** : `object`
  * **Description** : Configuration for the Content Publisher intent.


    
    
    {
    
      "intent": {
    
        "content_publisher": {
    
          "enrolled": true
    
        }
    
      }
    
    }

JSON

Copy

## Example configuration

The following is a complete example of a `canva-app.json` file for a Data Connector app:
    
    
    {
    
      "$schema": "https://www.canva.dev/schemas/app/v1/manifest-schema.json",
    
      "manifest_schema_version": 1,
    
      "runtime": {
    
        "permissions": [
    
          {
    
            "name": "canva:design:content:read",
    
            "type": "mandatory"
    
          },
    
          {
    
            "name": "canva:design:content:write",
    
            "type": "mandatory"
    
          }
    
        ]
    
      },
    
      "intent": {
    
        "data_connector": {
    
          "enrolled": true
    
        }
    
      }
    
    }

JSON

Copy

## Limitations

`canva-app.json` doesn't include every setting available for your app.

  * App name, description, icon, and other listing details aren't part of `canva-app.json`. Manage these in the Developer Portal under **Release > App listing details**.
  * Third-party OAuth, webhooks, and other REST API-based configuration aren't part of `canva-app.json`. Manage this configuration in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).


