---
url: https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/
title: Set up a web server - Tutorials - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:04.592180+00:00
---

# Set up a web server - Tutorials - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/

Tutorials

[Getting started](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/)[Set up a web server](https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/)[Initialize the Partnership SDK](https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/)[Show the product catalog](https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/)[Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/)[Create a new design](https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/)[Preview the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/)[Purchase the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/)

# Set up a web server

Copy page

Creating a Print Partnership integration requires client-side and server-side development. For the most part, it doesn't matter what programming language or framework you use for this development. The only strict requirement is that, for some of the client-side work, you need to use Canva's Partnership SDK. This means you must write some JavaScript (or a language that compiles to JavaScript, such as TypeScript).

To kick things off, this part of the tutorial explains how to set up a web server with Express.js. This server will render client-side code and handle some back-end processing.

If you're not familiar with Express.js, follow along anyway. You should at least end up with a high-level understanding of how integrations work.

## Step 1: Create a new project

In a terminal, create a new directory:
    
    
    mkdir print-partner-example

BASH

Copy

Then navigate into this directory:
    
    
    cd print-partner-example

BASH

Copy

Then initialize a Node.js project:
    
    
    npm init --yes

BASH

Copy

## Step 2: Install the dependencies

This project relies on the following _runtime_ dependencies:

  * [`express`⁠(opens in a new tab or window)](https://www.npmjs.com/package/express) \- A web application framework.
  * [`ejs`⁠(opens in a new tab or window)](https://www.npmjs.com/package/ejs) \- A templating engine.
  * [`axios`⁠(opens in a new tab or window)](https://www.npmjs.com/package/axios) \- A library for sending HTTP requests.
  * [`dotenv`⁠(opens in a new tab or window)](https://www.npmjs.com/package/dotenv) \- A library for loading environment variables from an `.env` file.



To install these dependencies, run the following command:
    
    
    npm install express ejs axios dotenv --save

BASH

Copy

This project also relies on the following _development_ dependencies:

  * [`nodemon`⁠(opens in a new tab or window)](https://www.npmjs.com/package/nodemon) \- A tool for automatically restarting a Node.js server on file changes.



To install these dependencies, run the following command:
    
    
    npm install nodemon --save-dev

BASH

Copy

After running these commands, the project's `package.json` looks like this:
    
    
    {
    
      "name": "print-partner-example",
    
      "version": "1.0.0",
    
      "description": "",
    
      "main": "index.js",
    
      "scripts": {
    
        "test": "echo \"Error: no test specified\" && exit 1"
    
      },
    
      "keywords": [],
    
      "author": "",
    
      "license": "ISC",
    
      "dependencies": {
    
        "axios": "^0.19.2",
    
        "dotenv": "^8.2.0",
    
        "ejs": "^3.1.3",
    
        "express": "^4.17.1"
    
      },
    
      "devDependencies": {
    
        "nodemon": "^2.0.4"
    
      }
    
    }

JSON

Copy

## Step 3: Set up the project structure

In the project's directory, create the following structure:

  * src/ 
    * views/
    * server.js
  * .env
  * package.json



To create the directories, run the following command:
    
    
    mkdir src src/views

BASH

Copy

To create the files, run the following command:
    
    
    touch .env src/server.js

BASH

Copy

The `touch` command is not available on Windows. You need to create the files manually.

## Step 4: Add credentials to the `.env` file

In the `.env` file, add the integration's [credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/):
    
    
    PARTNER_ID=
    
    PARTNER_API_KEY=
    
    PARTNER_API_SECRET=
    
    ARTWORK_API_SECRET=

BASH

Copy

This ensures that:

  * You can securely access sensitive values (that is, the secrets).
  * You can transition between test and production environments by providing different credentials for each environment.



While developing the integration, use the integration's _test_ credentials. If you use the production credentials, you're billed for usage.

Secrets are sensitive values. You should never share or commit them to source control. Doing so may allow attackers to steal your user's private designs. If the secrets are leaked, contact us and we can regenerate them.

## Step 5: Initialize the server

Copy the following code into the `server.js` file:
    
    
    require("dotenv").config();
    
    const express = require("express");
    
    const app = express();
    
    
    
    
    app.set("views", "./src/views");
    
    app.set("view engine", "ejs");
    
    
    
    
    app.use(express.json());
    
    app.use(express.urlencoded({ extended: true }));
    
    
    
    
    // Routes go here
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy

This code:

  * Loads the environment variables from the `.env` file.
  * Creates a web server with Express.js.
  * Sets EJS as the "[template engine⁠(opens in a new tab or window)](https://expressjs.com/en/guide/using-template-engines.html)" for Express.js.
  * Enables the [`express.json()`⁠(opens in a new tab or window)](https://expressjs.com/en/api.html#express.json) and [`express.urlencoded()`⁠(opens in a new tab or window)](https://expressjs.com/en/api.html#express.urlencoded) middleware.
  * Listens for requests on port 3000.



## Step 7: Start the server

Add the following script to the `package.json` file:
    
    
    "scripts": {
    
      "start": "nodemon ./src/server.js"
    
    },

JSON

Copy

This script uses `nodemon` to reload the server on file changes.

Then run the following command:
    
    
    npm run start

BASH

Copy

The URL of the server is <http://localhost:3000>[⁠(opens in a new tab or window)](http://localhost:3000). The `server.js` file doesn't contain any routes though, so the URL doesn't return anything (yet).

You can stop the server at any time with the `CTRL` \+ `C` shortcut.

## Example

### src/server.js
    
    
    require("dotenv").config();
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.set("views", "./src/views");
    
    app.set("view engine", "ejs");
    
    
    
    
    app.use(express.json());
    
    app.use(express.urlencoded({ extended: true }));
    
    
    
    
    // Routes go here
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy

### .env
    
    
    PARTNER_ID=
    
    PARTNER_API_KEY=
    
    PARTNER_API_SECRET=
    
    ARTWORK_API_SECRET=

BASH

Copy

### package.json
    
    
    {
    
      "name": "print-partner-example",
    
      "version": "1.0.0",
    
      "description": "",
    
      "main": "index.js",
    
      "scripts": {
    
        "start": "nodemon ./src/server.js"
    
      },
    
      "keywords": [],
    
      "author": "",
    
      "license": "ISC",
    
      "dependencies": {
    
        "axios": "^0.19.2",
    
        "dotenv": "^8.2.0",
    
        "ejs": "^3.1.3",
    
        "express": "^4.17.1"
    
      },
    
      "devDependencies": {
    
        "nodemon": "^2.0.4"
    
      }
    
    }

JSON

Copy
