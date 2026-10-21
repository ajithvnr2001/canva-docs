---
url: https://www.canva.dev/docs/apps/prerequisites/
title: Prerequisites - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:12.825788+00:00
---

# Prerequisites - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/prerequisites/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Prerequisites

The accounts, tools, and skills you need to build with the Canva Developers SDK.

Copy page

For the most part, building an app with the Canva Developers SDK is similar to developing any other web-based software, so any knowledge you have of modern coding standards, tools, and workflows will be beneficial. However, we don't want to assume that everyone has the same background, so this page outlines exactly what you'll need. What you need also depends on the surface you're building for, so start with the summary for your surface and then read the detail below it.

## What you need

Find the list for the surface you're building for. You only need the tooling for the surfaces you build on:

  * **Apps inside Canva:**
    * A relatively modern web browser
    * A free [Canva⁠(opens in a new tab or window)](https://www.canva.com/) account
    * A command line application, such as **Terminal** on macOS
    * An installation of git, and Node.js (`v24`) with npm (`v11`)
    * Some knowledge of TypeScript and React
  * **Canva for your platform:**
    * A [Canva⁠(opens in a new tab or window)](https://www.canva.com/) account
    * [Multi-Factor Authentication (MFA)⁠(opens in a new tab or window)](https://www.canva.com/help/login-verification/) set up on your Canva account
    * An installation of git, and Node.js (`v24`) with npm (`v11`)
  * **Canva for AI assistants:**
    * A [Canva⁠(opens in a new tab or window)](https://www.canva.com/) account, on any plan
    * An AI tool or assistant that supports the Model Context Protocol



## Canva account

Canva has a [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers) for creating, configuring, and otherwise managing apps. Anyone with a standard Canva account has complete access to the Developer Portal. To sign up for Canva, [click here⁠(opens in a new tab or window)](https://www.canva.com/signup/).

Before you use the Canva REST APIs, set up [Multi-Factor Authentication (MFA)⁠(opens in a new tab or window)](https://www.canva.com/help/login-verification/) on your Canva account.

## Web browser

You need a relatively modern web browser to build apps inside Canva. For a list of supported browsers, see Canva's official [technical requirements⁠(opens in a new tab or window)](https://www.canva.com/help/technical-requirements/).

It's worth noting, however, that:

  * Some browsers, such as Safari, have security features that interfere with the development workflow.
  * Internally, we use the latest version of Google Chrome, so that's the version we can actively support.
  * It's easier to preview an app in a standalone browser, rather than using Canva's [desktop app⁠(opens in a new tab or window)](https://www.canva.com/download).



## Terminal

A terminal is an application for running commands that deliver instructions to a computer. This is in contrast to graphical user interfaces (GUIs) that rely on button presses and other forms of interaction. You'll need access to a terminal for various parts of the development workflow, along with some basic command line experience.

All major operating systems have a default terminal:

  * On macOS, the default terminal is called **Terminal**.
  * On Windows, the default terminal is called **Command Prompt**.
  * On Linux, the default terminal depends on the distribution.



## git

git is a version control system that makes it easier to collaborate on and release new versions of code. We use git repositories to distribute the starter kits for building apps, so you'll need to know how to clone (download) a repository and, ideally, pull the latest changes as updates are released. To learn more about the starter kit for apps inside Canva, see [Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/).

### Installing git

macOSmacOS

WindowsWindows

LinuxLinux

To install git on macOS, we recommend using the [Homebrew⁠(opens in a new tab or window)](https://brew.sh/) package manager:

  1. Install Homebrew:
         
         /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

BASH

Copy

  2. Run the following command:
         
         brew install git

BASH

Copy




To learn more about installing git, including alternative options, see [the official documentation⁠(opens in a new tab or window)](https://git-scm.com/download/mac).

To install git on Windows, run the following command:
    
    
    winget install --id Git.Git -e --source winget

BASH

Copy

This command assumes that [the winget tool is installed⁠(opens in a new tab or window)](https://learn.microsoft.com/en-us/windows/package-manager/winget/) To learn more about installing git, including alternative options, see [the official documentation⁠(opens in a new tab or window)](https://git-scm.com/download/windows).

To install git on Linux, use the distribution's package manager:
    
    
    # Debian/Ubuntu
    
    apt-get install git
    
    
    
    
    # Fedora
    
    dnf install git
    
    
    
    
    # Arch Linux
    
    pacman -Syu git

BASH

Copy

To learn more about installing git, including alternative options, see [the official documentation⁠(opens in a new tab or window)](https://git-scm.com/download/linux).

## Node.js (`v24`)

Node.js is a JavaScript runtime that allows JavaScript to run outside of a browser. We use Node.js in the starter kits and CLI templates as it's a key dependency of developer tooling that we rely on.

The starter kits require Node.js `v24`.

### Installing Node.js

To install Node.js, we recommend using [Node Version Manager⁠(opens in a new tab or window)](https://github.com/nvm-sh/nvm) (nvm). This is a tool for managing multiple versions of Node.js on a single system, which reduces the risk of frustrating versioning errors.

macOSmacOS

WindowsWindows

LinuxLinux

  1. Install nvm by running the following command:
         
         curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

BASH

Copy

  2. At the root of the starter repo, install Node.js by running the following command:
         
         nvm install

BASH

Copy




  1. Install nvm by running the following command:
         
         winget install -e --id CoreyButler.NVMforWindows

BASH

Copy

  2. At the root of the starter repo, install Node.js by running the following command:
         
         nvm install

BASH

Copy




This command assumes that [the winget tool is installed⁠(opens in a new tab or window)](https://learn.microsoft.com/en-us/windows/package-manager/winget/)

  1. Install nvm by running the following command:
         
         curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

BASH

Copy

  2. At the root of the starter repo, install Node.js by running the following command:
         
         nvm install

BASH

Copy




To verify that the correct version is available in the current terminal session, run the following command:
    
    
    node -v

BASH

Copy

If the correct version isn't returned, run the following command from the starter kit directory:
    
    
    nvm use

BASH

Copy

This will set the correct version based on the starter kit's `.nvmrc` file. Each starter kit has one in its root directory, so running `nvm install` from the kit's directory also picks up the correct version: see the [`.nvmrc` for apps inside Canva⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/blob/main/.nvmrc) and the [`.nvmrc` for Canva for your platform⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-connect-api-starter-kit/blob/main/.nvmrc).

You can automatically switch to the appropriate Node.js version by updating your bash or zsh profile to detect the presence of `.nvmrc` files. To learn more, see [the official documentation⁠(opens in a new tab or window)](https://github.com/nvm-sh/nvm#deeper-shell-integration).

## npm (v11)

npm is a package manager for Node.js. The starter kits use npm to install and manage dependencies.

npm 11 is bundled with Node.js 24, so no separate installation is required. Once you have Node.js 24 installed, npm is already available.

To verify that npm is available, run the following command:
    
    
    npm -v

SHELL

Copy

## TypeScript

TypeScript is a superset of JavaScript that adds a variety of features to the language. These features — in particular, static typing — make the language more robust, reducing the likelihood of common errors.

Technically speaking, TypeScript is not required to develop an app. You can use JavaScript. The starter kits are set up to use TypeScript though, and all of the documentation and code samples assume that you're using it.

To learn TypeScript, read [the official documentation⁠(opens in a new tab or window)](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html).

## React

React is a library for creating fast and interactive user interfaces. For apps inside Canva, it's not strictly required, but it's what we use in the starter kit and documentation, and it's required to use the App UI Kit.

To learn React, read [the official documentation⁠(opens in a new tab or window)](https://react.dev/learn).

## `@canva/app-scripts`

Apps inside Canva must be uploaded to the Developer Portal as a single JavaScript file, a process known as [bundling](https://www.canva.dev/docs/apps/bundling-apps/). [`@canva/app-scripts`](https://www.canva.dev/docs/apps/canva-app-scripts/) is the package that handles this for you. It's what powers the `canva apps start` and `canva apps build` [Canva CLI](https://www.canva.dev/docs/apps/canva-cli/) commands, using [Rsbuild⁠(opens in a new tab or window)](https://rsbuild.dev/) as its bundler by default.

You don't need any bundler knowledge to develop an app. `@canva/app-scripts` is designed so the bundler stays out of your way, with sensible defaults already configured for React, TypeScript, CSS modules, SVGs, and translation extraction. Some familiarity may still be useful if you want to customize the build.

To learn more, see [Canva App Scripts](https://www.canva.dev/docs/apps/canva-app-scripts/).

## AI tool or assistant

For Canva for AI assistants, you need an AI tool or assistant that supports the Model Context Protocol, which is how it connects to the Canva MCP server. Many popular AI tools already have access. For more information, see [About Canva MCP](https://www.canva.dev/docs/apps/mcp/).

## Next steps

Once you have what you need for your surface, see [Quickstart](https://www.canva.dev/docs/apps/quickstart/) to get an app up and running.
