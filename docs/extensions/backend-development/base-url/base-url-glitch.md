---
url: https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/
title: Set up a Base URL (with Glitch) - Base URL - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:59:02.061589+00:00
---

# Set up a Base URL (with Glitch) - Base URL - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/

Base URL

[Overview](https://www.canva.dev/docs/extensions/backend-development/base-url/)[Set up a Base URL (with Glitch)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/)[Set up a Base URL (with ngrok)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/)

# Set up a Base URL (with Glitch)

Learn how to set up a Base URL with Glitch, a web-based code editor.

Copy page

In the Developer Portal, extensions have a **Base URL** field. This indicates that the extension must provide the URL of a server that can receive and respond to HTTP requests from Canva. You can use any programming language, framework, or architecture to handle these requests.

This tutorial explains how to set up a **Base URL** with:

  * [Express.js⁠(opens in a new tab or window)](https://expressjs.com/) \- A minimal web framework for Node.js.
  * [Glitch⁠(opens in a new tab or window)](https://glitch.com/) \- A free, web-based editor for developing (and automatically deploying) Node.js apps.



Don't use Glitch's free service for production apps. The servers are slow and go to sleep after a few minutes of inactivity, which causes timeout errors when opening an app.

## Step 1: Create a Glitch project

  1. Navigate to [glitch.com⁠(opens in a new tab or window)](https://glitch.com/).

  2. Log in or sign up to Glitch.

  3. Click **New Project**.

![](https://www.canva.dev/_next/static/media/img-99b7002824.caf09d04.jpeg)

  4. Select **glitch-hello-node**.




This opens Glitch's code editor.

![](https://www.canva.dev/_next/static/media/img-1daaf68525.411aea0e.jpeg)

## Step 2: Install Express.js

  1. Open the `package.json` file.
  2. Click **Add package**.
  3. Search for `"express"`.
  4. Select the first result.



This installs Express.js.

![](https://www.canva.dev/_next/static/media/img-37747da7fb.e36b34e7.jpeg)

## Step 3: Set up the server

Replace the contents of the `server.js` file with the following code:
    
    
    const express = require("express");
    
    const app = express();
    
    
    
    
    app.use(express.json());
    
    app.use(express.static("public"));
    
    
    
    
    // Routes go here
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy

This code initializes an Express.js server without any endpoints. The required endpoints depend the extensions added to the endpoint and how the extensions are configured.

Glitch automatically loads environment variables from the project's `.env` file.

## Step 3: Get the public URL of the server

For Canva to send requests to a **Base URL** , it needs to be exposed via a publicly available URL. This is something that Glitch provides without any further setup.

To get the public URL of a Glitch server:

  1. Click **Share**.
  2. Copy the URL from the **Live site** field.



This URL is the value that should be entered into an extension's **Base URL** field.

![](https://www.canva.dev/_next/static/media/img-1803799323.3bc84c56.jpeg)

## (Optional) Step 4: Open the logs

To verify that the server is running as expected—and to debug any errors that may occur—it's useful to view the logs.

Click **Logs** to view the logs of a Glitch server.

![](https://www.canva.dev/_next/static/media/img-d463915de6.2cf849c2.jpeg)

## More information

To learn more about Glitch, see the [Glitch Help Center⁠(opens in a new tab or window)](https://glitch.happyfox.com/home/).
