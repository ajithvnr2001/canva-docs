---
url: https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/
title: Set up a Base URL (with ngrok) - Base URL - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:59:02.408371+00:00
---

# Set up a Base URL (with ngrok) - Base URL - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/

Base URL

[Overview](https://www.canva.dev/docs/extensions/backend-development/base-url/)[Set up a Base URL (with Glitch)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/)[Set up a Base URL (with ngrok)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/)

# Set up a Base URL (with ngrok)

Learn how to set up Base URL with ngrok, an SSH tunneling service.

Copy page

In the Developer Portal, extensions have a **Base URL** field. This indicates that the extension must provide the URL of a server that can receive and respond to HTTP requests from Canva. You can use any programming language, framework, or architecture to handle these requests.

This tutorial explains how to set up a **Base URL** with:

  * [Express.js⁠(opens in a new tab or window)](https://expressjs.com/) \- A minimal web framework for Node.js.
  * [ngrok⁠(opens in a new tab or window)](https://ngrok.com/) \- A free CLI that exposes a local server via a publicly accessible URL.



ngrok is a useful tool, but it has inherent security risks, such as someone figuring out the URL of your server and accessing proprietary information. Be mindful of the risks, and if you're working as part of an organization, talk to your IT department.

## Step 1: Install Node.js

To check if Node.js is installed, run the following command:
    
    
    node --version

BASH

Copy

You should see something like this:
    
    
    $ node --version
    
    v14.15.0

BASH

Copy

If it's not installed, [download it from the official website⁠(opens in a new tab or window)](https://nodejs.org/en/).

## Step 2: Set up a new project

Create a project with the following structure:

  * my-app 
    * src/ 
      * server.js
    * .env
    * package.json



To create this structure, run the following commands:
    
    
    mkdir my-app
    
    cd my-app
    
    npm init --yes # yarn init
    
    mkdir src
    
    touch .env src/server.js

BASH

Copy

The `touch` command is not available on Windows. If you're using Windows, create the files manually.

Then copy the following code into the `server.js` file:
    
    
    require("dotenv").config();
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    // Routes go here
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy

This code initializes an Express.js server without any endpoints. The required endpoints depend on the app's extensions and how they're configured.

## Step 3: Install the dependencies

Install the following runtime dependencies:

  * [`express`⁠(opens in a new tab or window)](https://www.npmjs.com/package/express)
  * [`dotenv`⁠(opens in a new tab or window)](https://www.npmjs.com/package/dotenv)
  * [`nodemon`⁠(opens in a new tab or window)](https://www.npmjs.com/package/nodemon)



To install these dependencies, run the following command:
    
    
    npm install express dotenv --save && npm install nodemon --save-dev
    
    # yarn add express dotenv && yarn add nodemon --dev

BASH

Copy

## Step 4: Start the local server

Copy the following script into the `package.json` file:
    
    
    "scripts": {
    
      "start": "nodemon src/server.js"
    
    }

JSON

Copy

Then start the local server with the `start` command:
    
    
    npm run start
    
    # yarn start

BASH

Copy

The local server becomes available at <http://localhost:3000>[⁠(opens in a new tab or window)](http://localhost:3000).

## Step 5: Expose the local server

For Canva to send requests to a local server, it needs to be exposed via a publicly available URL. One of the easiest ways to do this is with ngrok.

ngrok is a free tool that creates a secure tunnel to a local server. You can create tunnels without an account, but the tunnels expire after a few hours of activity. If you have an account, the tunnels don't expire.

To install ngrok, run the following command:
    
    
    npm install ngrok --global

BASH

Copy

To verify that ngrok is installed, run the following command:
    
    
    ngrok version

BASH

Copy

You should see something like this:
    
    
    $ ngrok version
    
    ngrok version 2.3.35

BASH

Copy

If you run into any errors, refer to [the official installation instructions⁠(opens in a new tab or window)](https://ngrok.com/download).

To start an ngrok tunnel, run the following command in a separate terminal _while_ the local server is still running:
    
    
    ngrok http 3000

BASH

Copy

This command assumes the port of the local server is `3000`.

After running this command, ngrok provides a HTTPS-enabled URL that can receive requests from Canva. You can enter this URL into the extension's **Base URL** field.

## Example

### src/server.js
    
    
    require("dotenv").config();
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    // Routes go here
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy

### .env
    
    
    # add environment variables here

BASH

Copy

### package.json
    
    
    {
    
      "name": "my-app",
    
      "version": "1.0.0",
    
      "description": "",
    
      "main": "server.js",
    
      "scripts": {
    
        "start": "nodemon src/server.js"
    
      },
    
      "keywords": [],
    
      "author": "",
    
      "license": "ISC",
    
      "dependencies": {
    
        "dotenv": "^8.2.0",
    
        "express": "^4.17.1"
    
      },
    
      "devDependencies": {
    
        "nodemon": "^2.0.6"
    
      }
    
    }

JSON

Copy
