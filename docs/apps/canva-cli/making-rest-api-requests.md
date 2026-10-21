---
url: https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/
title: Making Canva REST API requests from the CLI - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:28.970917+00:00
---

# Making Canva REST API requests from the CLI - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/

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

# Making Canva REST API requests from the CLI

How to use the canva api command to make Canva REST API requests from your terminal.

Copy page

`canva api` calls Canva's [REST APIs](https://www.canva.dev/docs/apps/rest-apis/) using your Canva CLI login. Commands are grouped by the resource they act on, such as `canva api designs create`, and `--help` works at every level to show the available groups, commands, and flags.

This page explains how to find a command, pass input to it, and read the JSON response. The examples later on the page are optional starting points. You don't need to run them to use `canva api`.

Choose the approach that matches what you're doing:

  * **Work with your own designs by chatting with an AI assistant:** Set up the [Canva AI Connector⁠(opens in a new tab or window)](https://www.canva.com/help/mcp-agent-setup/).
  * **Build a product that acts on your users' Canva accounts:** See [Quickstart](https://www.canva.dev/docs/apps/quickstart/).
  * **Interact with Canva from a terminal, a script, or a coding agent, using files on your machine:** Use `canva api`.



## Before you begin

You need:

  * Node.js `v24`
  * npm `v11`
  * A [Canva⁠(opens in a new tab or window)](https://www.canva.com/) account
  * The Canva CLI. For install steps, see [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/).



Commands act as the account you're logged in to the CLI with, so run `canva login` if you aren't logged in.

Earlier versions of the CLI didn't ask for the access that `canva api` needs, so if a call fails with a `MISSING_SCOPE` error, log in again to grant it.

## Find a command

Every supported REST API operation is a command like this:
    
    
    canva api <group> <command>

SHELL

Copy

Groups collect related operations, such as `designs` or `exports`. You don't need to memorize the tree. Print it with `--help`, or print one command's contract as JSON with `canva api describe`:
    
    
    canva api --help
    
    canva api designs --help
    
    canva api designs create --help
    
    canva api describe designs create

SHELL

Copy

Commands are named after the REST API operation rather than its URL path. For example, the [Get design](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design/) operation, `GET /v1/designs/{designId}`, is `canva api designs get`.

IDs such as a design ID can be a positional argument or a kebab-case flag. These two commands call the same operation:
    
    
    canva api designs get DAF123abc
    
    canva api designs get --design-id DAF123abc

SHELL

Copy

Confirm a command's flags with `--help` instead of guessing them. If a call asks you to log in, run `canva login` and try the call again.

## Pass input to a command

You can pass input with operation flags (recommended) or with `--body` (advanced). Use flags when `--help` lists them. Use `--body` when flags can't express a nested payload, such as JSON copied from the REST API reference.

### Pass input with flags (recommended)

Run `canva api <group> <command> --help` to see the flags for that operation. For example, this command creates a presentation:
    
    
    canva api designs create --type type_and_asset --design-type preset --design-type-name presentation --title "Q3 Review"

SHELL

Copy

### Pass a JSON body (advanced)

`--body` is only available on operations that send a JSON request body. Commands that only read data, such as `designs get`, don't accept it.
    
    
    canva api designs create --body @payload.json

SHELL

Copy

### Check a command before you send it

Add `--dry-run` to check a command's arguments and your login without calling the REST API. This is useful before a command that creates or changes something.
    
    
    canva api designs create --type type_and_asset --design-type preset --design-type-name presentation --title "Q3 Review" --dry-run

SHELL

Copy

## Understand the JSON response

When a call reaches the REST API, or when it fails after the CLI accepts your arguments, the CLI prints one JSON object to stdout and nothing else. You can pipe that object into `jq` or a script.

If you omit a required argument or pass an unknown flag, the CLI prints a usage message to standard error instead of JSON.

A successful response looks like this:
    
    
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
    
        "durationMs": 12,
    
        "profile": "default"
    
      }
    
    }

JSON

Copy

A failed call looks like this:
    
    
    {
    
      "ok": false,
    
      "error": {
    
        "code": "API_FAILURE",
    
        "message": "Design not found.",
    
        "upstreamErrorCode": "not_found"
    
      },
    
      "next": [],
    
      "meta": {
    
        "status": 404,
    
        "durationMs": 18,
    
        "profile": "default"
    
      }
    
    }

JSON

Copy

The object has these fields:

  * **`ok`:** `true` when the call succeeded, `false` when it failed.
  * **`data`:** The REST API response body, unwrapped, so the API reference still applies. On failure, `error` occupies this slot instead, with `code`, `message`, and an optional `upstreamErrorCode` holding the REST API's own error code.
  * **`next`:** Suggested follow-up commands, such as `canva login` if you need to sign in. You can ignore these hints.
  * **`meta.status`:** The HTTP status from the API. It's `0` when the CLI didn't call the API, for example if you aren't logged in, the input is invalid, or you pass `--dry-run`.
  * **`meta.durationMs`:** How long the call took, in milliseconds.
  * **`meta.profile`:** The stored login the command ran as.



For example, to extract the link for editing a design:
    
    
    canva api designs get DAF123abc | jq -r .data.design.urls.edit_url

SHELL

Copy

## Examples

The following commands are optional examples, not required steps. Replace the IDs with values from your own account, and run `--help` on each command to confirm its flags.

### Look up a design
    
    
    canva api designs get DAF123abc

SHELL

Copy

### List your designs
    
    
    canva api designs list

SHELL

Copy

### List the items in a folder

For the folder IDs you can use and the shape of each item, see [List folder items](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/).
    
    
    canva api folders list-items --folder-id root

SHELL

Copy

A `continuation` value in the response means the folder holds more items than one response returns. Pass it back to get the next page, and repeat until a response has no `continuation`:
    
    
    canva api folders list-items --folder-id root --continuation "RkFGMgXlsVTDbMd:MR3L0QjiaUzycIAjx0yMyuNiV0O"

SHELL

Copy

### Create a design
    
    
    canva api designs create --type type_and_asset --design-type preset --design-type-name presentation --title "Q3 Review"

SHELL

Copy

The `data` field of the response includes the URLs for editing and viewing the design, and an ID you can pass to other commands:
    
    
    {
    
      "design": {
    
        "id": "DAFVztcvd9z",
    
        "title": "Q3 Review",
    
        "urls": {
    
          "edit_url": "https://www.canva.com/api/design/eyJhbGciOiJkaXIiLCJlbmMi/edit",
    
          "view_url": "https://www.canva.com/api/design/eyJhbGciOiJkaXIiLCJlbmMi/view"
    
        }
    
      }
    
    }

JSON

Copy

### Upload a file from your machine

This example adds a local file to your Canva content library, which gives you an asset ID you can use in other calls. For the supported file types, see [Assets](https://www.canva.dev/docs/apps/rest-apis/reference/assets/).

Uploading creates an [asynchronous job](https://www.canva.dev/docs/apps/rest-apis/requests-responses/#asynchronous-job-endpoints). You start the job, then poll it until the job finishes. The CLI doesn't wait for the job.

Run `canva api assets create-upload --help` to confirm how to pass the file path and the asset name.

  1. Start the job with a call to `canva api assets create-upload`.
         
         canva api assets create-upload --file ./cover-photo.jpg --name "Q3 cover photo"

SHELL

Copy

  2. The command returns an upload job with its ID and status in `data`.
         
         {
         
           "job": {
         
             "id": "e08861ae-3b29-45db-8dc1-1fe0bf7f1cc8",
         
             "status": "in_progress"
         
           }
         
         }

JSON

Copy

Save the job ID so you can check the job's status.

  3. With the job ID from the previous step, use `canva api assets get-upload` to poll the job until `data.job.status` changes from `in_progress` to either `success` or `failed`. For how often to call it, see [Job polling strategies](https://www.canva.dev/docs/apps/rest-apis/requests-responses/#job-polling-strategies).
         
         canva api assets get-upload e08861ae-3b29-45db-8dc1-1fe0bf7f1cc8

SHELL

Copy

  4. A successfully completed job includes the new asset.
         
         {
         
           "job": {
         
             "id": "e08861ae-3b29-45db-8dc1-1fe0bf7f1cc8",
         
             "status": "success",
         
             "asset": {
         
               "id": "Msd59349ff",
         
               "type": "image",
         
               "name": "Q3 cover photo"
         
             }
         
           }
         
         }

JSON

Copy

Use `data.job.asset.id` wherever a call takes an asset ID. A `failed` job has no `asset`, and instead has an `error` with the reason, such as a file that's too big. For details, see [Create asset upload job](https://www.canva.dev/docs/apps/rest-apis/reference/assets/create-asset-upload-job/).




## Next steps

  * [`api` command in the Canva CLI reference](https://www.canva.dev/docs/apps/canva-cli/)
  * [About Canva's REST APIs](https://www.canva.dev/docs/apps/rest-apis/)


