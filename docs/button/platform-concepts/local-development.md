---
url: https://www.canva.dev/docs/button/platform-concepts/local-development/
title: Local development - Platform concepts - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:59.527970+00:00
---

# Local development - Platform concepts - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/platform-concepts/local-development/

Platform concepts

[Domain restrictions](https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/)[HTML API vs. JavaScript API](https://www.canva.dev/docs/button/platform-concepts/html-api-vs-js-api/)[Local development](https://www.canva.dev/docs/button/platform-concepts/local-development/)

# Local development

Copy page

If you're using the HTML or JavaScript API, it's not possible to add the Canva Button to an HTML file on your local machine and open that file in a web browser. If you do this, you'll encounter a [Forbidden (403)](https://www.canva.dev/docs/button/troubleshooting/403-forbidden-error/) error.

This is because Canva expects requests to come from:

  * canva.com
  * localhost
  * a domain on Canva's allowlist



This guide explains how to develop locally by serving an HTML file via `localhost`.

You can [add a domain to Canva's allowlist](https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/) via the [Developer Portal⁠(opens in a new tab or window)](https://canva.com/developers).

## Step 1: Install `http-server`

`http-server` is "a simple, zero-configuration command-line HTTP server." You can use it to make a file (or a directory of files) available via `localhost`.

You can install `http-server` via npm or Homebrew.

### npm
    
    
    npm install http-server --global

BASH

Copy

### Homebrew
    
    
    brew install http-server

BASH

Copy

You don't _have_ to use `http-server` to start a local server. There are many other tools that serve a similar purpose.

## Step 2: Navigate into the project's directory

Use the `cd` command to navigate into the directory that contains the HTML file:
    
    
    cd [dir_path]

BASH

Copy

## Step 3: Start the local server

To start the local server, run the `http-server` command:
    
    
    http-server

BASH

Copy

By default, the local server becomes available at <http://localhost:8080>[⁠(opens in a new tab or window)](http://localhost:8080).

For a complete list of the arguments and flags that `http-server` supports, refer to [the official documentation⁠(opens in a new tab or window)](https://www.npmjs.com/package/http-server).
