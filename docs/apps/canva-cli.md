---
url: https://www.canva.dev/docs/apps/canva-cli/
title: Canva CLI - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:28.723804+00:00
---

# Canva CLI - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/canva-cli/

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

# Canva CLI

CLI for creating and managing Canva Apps, and working with Canva.

Copy page

## Introduction

`@canva/cli` is a command line tool designed for creating and managing Canva Apps. Use `@canva/cli` to get started creating and testing your app. The Canva CLI allows you to create apps from the command line, to use Canva's recommended development tools and templates, and to work with Canva from your machine.

To learn more about app development, visit [the official documentation](https://www.canva.dev/docs/apps/).

## Requirements

Before using the CLI, make sure that you have the following:

  * Node.js `v24`

  * npm `v11`

  * A [Canva account⁠(opens in a new tab or window)](https://www.canva.com/developers).

If you are using a version manager such as nvm, run the `nvm install 24` command to make sure you have the correct Node.js version.




## Quickstart

The following commands create a new Canva app using the Canva CLI.
    
    
    npm install -g @canva/cli@latest
    
    canva login
    
    canva apps create "My New App" --template="hello_world" --distribution="public" --git --installDependencies
    
    cd my-new-app
    
    canva apps start

SHELL

Copy

## Use the Canva CLI

### Step 1: Install and log in

Installing the Canva CLI allows you to create new apps from the command line.

To get started:

  1. Install the Canva CLI globally.
         
         npm install -g @canva/cli@latest

SHELL

Copy

  2. Log in to the Canva CLI. The Canva CLI then opens an access request page in your browser.
         
         canva login

SHELL

Copy

  3. In your browser, click **Allow** to grant the Canva CLI access to manage apps and work with your designs on your behalf. When you grant access, the Canva CLI generates an auth token and stores it locally. For more information on the auth token, read the following section on [auth token storage and removal](https://www.canva.dev/docs/apps/canva-cli/#log-out-auth-token-storage-and-removal).

  4. Copy the confirmation code shown in your browser, and paste it into the Canva CLI input.




### Step 2: Create your app

After you log in to the Canva CLI and authorize it, you can create your app.

To create a new app:

  1. Run the `canva apps create` command. The flags in the following code snippet are optional, and you can instead configure these settings during the apps creation process. See the [CLI Reference](https://www.canva.dev/docs/apps/canva-cli/#cli-reference) for more information on each flag.
         
         canva apps create "My New App" --template="hello_world" --distribution="public" --git --installDependencies

SHELL

Copy

You can't change the distribution type after creating an app.




### Step 3: Preview your app

When your new app is ready, the Canva CLI automatically opens the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) to your new app's configuration page in your browser. You can then continue to preview and manage your new app.

To preview your app:

  1. Change into your new app's folder.
         
         cd my-new-app

SHELL

Copy

  2. Run the following command to start your app.
         
         canva apps start

SHELL

Copy

  3. The preview URL will be generated and opened automatically in your browser.

  4. If this is the first time previewing your app, click **Open** to preview your new app.




### Step 4: Run a health check on your app

After creating your app, you can diagnose potential issues using:
    
    
    canva apps doctor

SHELL

Copy

This checks for missing dependencies, outdated packages, and other issues.

## Log out, auth token storage, and removal

When you log in to the Canva CLI using the `canva login` command, and then grant the Canva CLI access to manage apps in your Canva account, an auth token is encrypted and stored locally on your machine. The token provides authentication for future requests so you don't need to grant the Canva CLI access each time it sends a request.

When you log out of the Canva CLI with the `canva logout` command, the auth token is revoked, and deleted.

### Token Location

The auth token is located in your home directory under the `.canva-cli` folder.

If you use more than one [profile](https://www.canva.dev/docs/apps/canva-cli/#profile), each one has its own token file: the `default` profile is stored in `credentials`, and every other profile in `profiles/<name>.json`. Logging out of one profile leaves the others in place, unless you pass `--all` to remove every one of them.

### Removing the Token

To delete the token, there are two options. However, only the `canva logout` command revokes and deletes the token. If there's a copy of the token, it's possible to reconnect the Canva CLI to your account's apps using the token.

#### Log out

  1. Use the `canva logout` command to revoke access and delete the stored token.
         
         canva logout

SHELL

Copy




#### Delete the file manually

  1. Locate the `credentials` file, which is stored in the following locations:

     * **macOS and Linux** : The token is stored in `~/.canva-cli/credentials`.
     * **Windows** : The token is stored in `%USERPROFILE%\.canva-cli\credentials`.

Tokens for named profiles sit alongside it in the `profiles` folder, one JSON file per profile.

  2. Delete the file. To remove every stored login, delete the whole `.canva-cli` folder.




## CLI Reference

After installation, you can use the Canva CLI by running:
    
    
    canva <command-name>

SHELL

Copy

### Flags

Top-level flags applicable to commands:

  * `--help`: Show help information about commands and flags.
  * `--lite`: Enable a simplified CLI interface for enhanced accessibility.
  * `--profile`: Run the command as a named stored login. See [profile](https://www.canva.dev/docs/apps/canva-cli/#profile).
  * `--version`: Show the CLI version number.



### Commands

#### welcome

Show the welcome page and general information.
    
    
    canva welcome

SHELL

Copy

#### tip

Print a random development tip for working with the Apps SDK.
    
    
    canva tip

SHELL

Copy

  * **Aliases** : 
    * `tips`: Also prints a random development tip.



#### bug

Raise an issue with the Canva CLI on GitHub.
    
    
    canva bug

SHELL

Copy

#### login

Log in to the Canva CLI.
    
    
    canva login

SHELL

Copy

  * **Flags** : 
    * `--china`, `--cn`: Login to canva.cn, this will use canva.cn for all subsequent commands until you log out.

    * `--mode`: The authentication mode or flow to use when logging in.

Available modes:

      * `"auto"`: Uses `manual` when running remotely, such as over SSH or in a container, and `callback` otherwise (default).
      * `"callback"`: Runs a local server to receive the auth code.
      * `"manual"`: Prompts you to copy and paste the auth code manually.
    * `--profile`: Store this login under a named profile instead of the current one, leaving your other logins in place. Commands keep using your current profile until you run [`canva profile switch`](https://www.canva.dev/docs/apps/canva-cli/#switch). See [profile](https://www.canva.dev/docs/apps/canva-cli/#profile).




#### logout

Log out of the Canva CLI, and delete the saved auth token:
    
    
    canva logout

SHELL

Copy

Only the profile you are currently using is affected. To log out of a different one, name it:
    
    
    canva logout --profile work

SHELL

Copy

To log out of every [profile](https://www.canva.dev/docs/apps/canva-cli/#profile) at once, pass `--all`. It reports each profile separately, forgets the profile chosen with [`canva profile switch`](https://www.canva.dev/docs/apps/canva-cli/#switch), and succeeds only if every profile was fully logged out, so a partial failure is still a failure:
    
    
    canva logout --all

SHELL

Copy

`--all` and `--profile` cannot be combined, since one covers every profile and the other names a single one.

The stored token is always deleted from your machine. The CLI also asks Canva to revoke it, but that part needs a working connection: if the request fails, the command reports the deletion, warns that the token stays valid until it expires, and fails, since you are not fully logged out. The deletion still stands, so running `canva logout` again reports that you are not logged in.

  * **Flags** : 
    * `--all`: Log out of every stored profile, not just the current one.
    * `--profile`: Log out of the named profile instead of the current one.



#### profile

Manage the stored logins the CLI can run as. Each profile holds its own auth token and its own Canva environment, so you can keep a login for your real account and a login for a test account side by side and switch between them without logging in again.
    
    
    canva profile <subcommand>

SHELL

Copy

To remove a profile, log out of it with `canva logout --profile <name>`, or remove them all with [`canva logout --all`](https://www.canva.dev/docs/apps/canva-cli/#logout).

To create a profile, log in with it:
    
    
    canva login --profile work
    
    canva profile switch work

SHELL

Copy

Any command accepts `--profile <name>` to run against one profile just once, without changing which profile is selected:
    
    
    canva apps list --profile work

SHELL

Copy

Setting `CANVA_CLI_PROFILE` picks a profile for a whole shell session, which is useful for scripts and agents:
    
    
    CANVA_CLI_PROFILE=work canva apps list

SHELL

Copy

When more than one is set, `--profile` wins, then `CANVA_CLI_PROFILE`, then the profile chosen with `canva profile switch`, and finally the `default` profile.

Profile names may contain letters, numbers, hyphens and underscores, must start with a letter or number, and may be up to 64 characters long.

##### list

Show every stored login, and mark the one in use.
    
    
    canva profile list

SHELL

Copy

##### switch

Make `<name>` the profile later commands run as. The choice persists until you switch again.
    
    
    canva profile switch work

SHELL

Copy

Leave `<name>` out to pick from your stored logins instead:
    
    
    canva profile switch

SHELL

Copy

The interactive list places a visual marker on the profile the command is currently running as. Note that `--profile` and `CANVA_CLI_PROFILE` both override that profile. If using either of those options, selecting the marked profile makes the override permanent.

The interactive switcher does not work when running headlessly.

#### mcp

Start the canva [MCP⁠(opens in a new tab or window)](https://modelcontextprotocol.io) server. This is usually called by your MCP client, such as Claude Desktop, Cursor, or other compatible tools. For more information on how to configure your MCP client to use the Canva Dev MCP server, please see [Dev MCP server](https://www.canva.dev/docs/apps/dev-mcp-server/) in the developer documentation.

#### api

Call the [Canva REST APIs](https://www.canva.dev/docs/connect/) using your Canva CLI login. Commands are grouped by the resource they act on, such as `canva api designs create`, and `--help` works at every level to show the available groups, commands, and flags. For more information on making REST API requests from the CLI, please see [Making Canva REST API requests from the CLI](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/) in the developer documentation.

Each call writes one JSON object to stdout and nothing else, so the output can be piped straight into `jq` or read by an agent. Missing arguments and unknown flags print a usage error to stderr instead of that object.
    
    
    canva api designs get DAF123abc
    
    canva api designs get --design-id DAF123abc
    
    canva api designs create --design-type preset --design-type-name presentation --title "Q3 Review"
    
    canva api designs get DAF123abc --dry-run
    
    canva api designs list | jq '.data.items[].id'

SHELL

Copy

Path parameters can be passed as positional arguments or as flags, such as `--design-id`. Every query parameter and request body field is a flag too; run `canva api <group> <command> --help` to see them.

You can pass input with operation flags (recommended) or with `--body` (advanced) when flags cannot express a nested payload:
    
    
    canva api designs create --body @payload.json

SHELL

Copy

`--body` also accepts inline JSON, or `-` to read stdin. It is only available on operations that send a JSON request body. Operations that upload a file, such as `canva api assets create-upload`, take `--file` instead.

  * **Flags** : 
    * `--dry-run`: Validate the arguments and print the response object without sending the request.
    * `--body`: Request body as `@path/to/file.json`, inline JSON, or `-` for stdin. Use this when operation flags cannot express the payload.
    * `--file`: Request body from a file's bytes, or `-` for stdin. Only on operations that upload a file.



Example success output:
    
    
    {
    
      "ok": true,
    
      "data": {
    
        "design": {
    
          "id": "DAF123abc"
    
        }
    
      },
    
      "next": [],
    
      "meta": {
    
        "status": 200,
    
        "durationMs": 12
    
      }
    
    }

JSON

Copy

When a call fails, `error` takes the place of `data` and carries a `code` and `message`, `meta.status` is the HTTP status (or `0` when no request was sent), and `next` suggests the command to run, such as `canva login` when the stored token is missing a scope.

If you logged in with a CLI version older than the `api` command, run `canva login` again so your stored token carries the REST API scopes.

##### describe

Show the contract for one REST API command as JSON: its method and path, the scopes and capabilities it needs, every flag with its summary, the rate limit, a link to the reference documentation, and the commands that usually follow it.
    
    
    canva api describe designs get
    
    canva api describe exports create

SHELL

Copy

##### request

Send a raw request to a REST path. Use this for an endpoint `canva api` has no generated command for. One command exists per HTTP method: `get`, `post`, `put`, `patch`, and `delete`.
    
    
    canva api get /v1/users/me
    
    canva api get "/v1/designs?query=Q3"
    
    canva api post /v1/designs --body @body.json
    
    canva api post /v1/asset-uploads --file ./photo.jpg --header "Asset-Upload-Metadata: {\"name_base64\": \"cGhvdG8=\"}"

SHELL

Copy

  * **Flags** : 
    * `--body`: Request body as `@path/to/file.json`, inline JSON, or `-` for stdin. Only on `post`, `put`, and `patch`.
    * `--file`: Request body from a file's bytes, or `-` for stdin. Only on `post`, `put`, and `patch`, and cannot be combined with `--body`.
    * `--header`: An extra request header as `'<name>: <value>'`. Repeat the flag for more than one.



#### apps

Manage your Canva apps.
    
    
    canva apps

SHELL

Copy

##### create

Create a new Canva app.
    
    
    canva apps create "My New App" --template="hello_world" --distribution="public" --git --installDependencies

SHELL

Copy

  * **Arguments** : 
    * `--name`: Sets the app's name. Provide the name you want for the app.
  * **Flags** : 
    * `--template`: Specifies the starting template for the app. Templates are pre-built starter projects that demonstrate common use cases and best practices. For a complete list of available templates, see [App templates](https://www.canva.dev/docs/apps/app-templates/).

    * `--distribution`: Sets the app's distribution type.

Available types:

      * `"public"`: Available to all Canva users, subject to Canva review.

      * `"private"`: Only available to your team on an [Enterprise plan⁠(opens in a new tab or window)](https://www.canva.com/enterprise/), and requires team admin approval.

You can't change the distribution setting after creating a new app with the `canva apps create` command.

    * `--git`: Initializes a Git repository in the project directory.

    * `--installDependencies`: Automatically installs necessary npm dependencies during the app creation process.

    * `--strict`: Uses the strict Canva app linting configuration in the generated project.

    * `--optionalConfig`: Optional configuration files to be created in the project directory.

Available options:

      * `"vscode"`: Adds a `.vscode` folder to the project directory.
      * `"cursor"`: Adds a `.cursor` folder to the project directory.
      * `"agents.md"`: Adds a `AGENTS.md` file to the project directory.
      * `"claude"`: Adds a `CLAUDE.md` file to the project directory.
    * `--offline`: Scaffold the app locally without also creating an app in the Developer Portal.

    * `--yes`: Automatically accept the default option for any prompts and run non-interactively.




##### list

List all Canva apps.
    
    
    canva apps list

SHELL

Copy

  * **Flags** : 
    * `--app-id`: Specifies an App ID to select.
    * `--all`, `-a`: Lists all apps at once without pagination.
    * `--print`, `-p`: Prints the list of apps to the console without interactivity.



##### preview

Preview your app.
    
    
    canva apps preview

SHELL

Copy

  * **Flags** : 
    * `--intent`: App intent to preview when the app has multiple intents enrolled.
    * `--target`: Canva target to preview in (`editor` or `canva_ai`), for intents that run in more than one location.
    * `--source`: Load the app from its development URL (`url`) or uploaded bundle (`bundle`). Defaults to the development URL when the app version has one.
    * `--no-open`: Print the preview URL without opening a browser.



##### start

Start the local development server for the app in the current directory, powered by [`@canva/app-scripts`](https://www.canva.dev/docs/apps/canva-app-scripts/).
    
    
    canva apps start

SHELL

Copy

  * **Flags** :

    * `--config`: Path to a canva-app config file, resolved from the project root (default: `canva-app.config.ts`).
    * `--entry`: Entry file for the app (default: `src/index.tsx`).
    * `--backend-entry`: Entry file for a backend run alongside the dev server.
    * `--use-https`: Serve the frontend over HTTPS.
    * `--override-frontend-port`: Override the frontend dev-server port.
    * `--tunnel`: Expose the backend through a public HTTPS tunnel.
    * `--preview`: Open the app preview in Canva once the server starts.
  * **Examples** :
        
        canva apps start
        
        canva apps start --preview
        
        canva apps start --use-https --tunnel

SHELL

Copy




##### build

Build the app for production and extract its translations, powered by [`@canva/app-scripts`](https://www.canva.dev/docs/apps/canva-app-scripts/).
    
    
    canva apps build

SHELL

Copy

  * **Flags** :

    * `--config`: Path to a canva-app config file, resolved from the project root (default: `canva-app.config.ts`).
    * `--entry`: Entry file for the app (default: `src/index.tsx`).
    * `--output-dir`: Build output directory (default: `dist`).
  * **Examples** :
        
        canva apps build
        
        canva apps build --output-dir out

SHELL

Copy




##### upload

Build the app and upload its JavaScript bundle and translations to the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps), as an alternative to [uploading the bundle yourself](https://www.canva.dev/docs/apps/bundling-apps/).
    
    
    canva apps upload

SHELL

Copy

The app is built the same way as [`canva apps build`](https://www.canva.dev/docs/apps/canva-cli/#build). The bundle and translations are then uploaded from the `outputDir` set in the canva-app config file, or from `dist/` for apps that don't use [`@canva/app-scripts`](https://www.canva.dev/docs/apps/canva-app-scripts/). To upload the output of a previous build instead, pass `--prebuilt`.

  * **Flags** :

    * `--app-id`: App ID to upload assets for. Defaults to the app linked in the current directory's `.env` file.
    * `--dry-run`: Preview what would be uploaded without building or uploading anything.
    * `--prebuilt`: Upload existing build output without building the app or extracting its translations.
    * `--drift-strategy`: Preselect how to resolve local `canva-app.json` differences from the Developer Portal. One of `push`, `skip`, or `abort`.
    * `--config`: Path to a canva-app config file, resolved from the project root (default: `canva-app.config.ts`).
  * **Examples** :
        
        canva apps upload
        
        canva apps upload --app-id AAEuu...
        
        canva apps upload --dry-run
        
        canva apps upload --prebuilt
        
        canva apps upload --drift-strategy skip

SHELL

Copy




##### doctor

Run diagnostics on your Canva App to identify and fix issues.
    
    
    canva apps doctor

SHELL

Copy

  * **Flags** : 
    * `--fix`: Automatically apply fixes for issues where possible.
    * `--report`: Output check results without prompting for fixes.
    * `--verbose`: Show detailed diagnostic output optimized for AI agent assistance.
    * `--check`: Specify a specific check to run.



##### migrate

Run specific code migrations to update your app to newer patterns and APIs.
    
    
    canva apps migrate <migrationName>

SHELL

Copy

  * **Arguments** :

    * `migrationName`: Name of the migration to run.

Available migrations:

      * `"apps-sdk-v1-v2"`: Migrates apps using the Apps SDK v1 packages to v2.
      * `"app-ui-kit-v5"`: Migrates apps using App UI Kit v4 to v5.
      * `"design-editor-intent"`: Migrates from direct render pattern to design intents pattern.
      * `"webpack-to-app-scripts"`: Migrates apps on a hand-rolled webpack config and `scripts/start/` runner to `@canva/app-scripts`.
  * **Flags** :

    * `--dry-run`: Preview changes without modifying files. Generates a markdown preview file showing all proposed changes.
    * `--debug`: Show detailed debug output.
    * `--force`: Proceed even when project validation warns.
  * **Examples** :
        
        canva apps migrate apps-sdk-v1-v2
        
        canva apps migrate app-ui-kit-v5
        
        canva apps migrate design-editor-intent
        
        canva apps migrate apps-sdk-v1-v2 --dry-run
        
        canva apps migrate apps-sdk-v1-v2 --debug
        
        canva apps migrate webpack-to-app-scripts

SHELL

Copy




##### config

Manage your [App Configuration](https://www.canva.dev/docs/apps/app-configuration/).
    
    
    canva apps config

SHELL

Copy

App config here is expanding. As announced in [Integrations are becoming part of apps in the Developer Portal⁠(opens in a new tab or window)](https://community.canva.dev/t/integrations-are-becoming-part-of-apps-in-the-developer-portal-soon/8881), this CLI doesn't yet support REST API configuration for apps built with the Connect API. Support is coming soon, keep an eye on the [Canva Developers Community⁠(opens in a new tab or window)](https://community.canva.dev/) for follow-up announcements.

###### pull

Fetch the [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/) config from the Developer Portal.
    
    
    canva apps config pull

SHELL

Copy

  * **Flags** : 
    * `--force`: Automatically pull config regardless of conflicts.
    * `--strategy`: Choose the resolution option for config conflicts - local, remote or manual



###### push

Submit the local [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/) to the Developer Portal.
    
    
    canva apps config push

SHELL

Copy

  * **Flags** : 
    * `--force`: Automatically push config regardless of conflicts.
    * `--strategy`: Choose the resolution option for config conflicts - local, remote or manual



###### status

Report on the status and validity of the [canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/) config.
    
    
    canva apps config status

SHELL

Copy

##### link

Link your local project to an existing Canva app by updating the .env file
    
    
    canva apps link

SHELL

Copy

  * **Flags** : 
    * `--app-id`: Specifies an App ID to select.
    * `--force`: Write `.env` without confirmation.



#### logout

Log out and revoke Canva CLI access.
    
    
    canva logout

SHELL

Copy

## Next Steps

  * [Preview your app in the Canva editor](https://www.canva.dev/docs/apps/previewing-apps/)
  * [Integrate your app with Canva using the Apps SDK](https://www.canva.dev/docs/apps/integrating-canva/)
  * [Making Canva REST API requests from the CLI](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)



## Limitations

You must manage your new app created through the Canva CLI through the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps). You can't manage apps completely through the Canva CLI.

`canva api` calls the REST APIs through Canva's own OAuth client. To build a product that calls Canva on your users' behalf, please see [create your own app with REST API access](https://www.canva.dev/docs/connect/creating-integrations/) in the developer documentation.

## Updates

To update the CLI to the latest version, run:
    
    
    npm update -g @canva/cli@latest

SHELL

Copy

## Contributions

Currently the Canva CLI doesn't accept third-party contributions. Please submit any feature requests through the [Canva Developers Community⁠(opens in a new tab or window)](https://community.canva.dev/) or raise an issue on [Github⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-cli/issues/new).

## Privacy

The Canva CLI collects anonymized analytics and diagnostic data to help improve product reliability. This data is handled in accordance with [Canva's Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

To disable collection, set `CANVA_CLI_DISABLE_TELEMETRY=true` in your environment. For example:
    
    
    export CANVA_CLI_DISABLE_TELEMETRY=true

SHELL

Copy

## License

Refer to the `LICENSE.md` file for more information.
