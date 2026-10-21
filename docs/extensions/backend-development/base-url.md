---
url: https://www.canva.dev/docs/extensions/backend-development/base-url/
title: Base URL - Base URL - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:59:00.045552+00:00
---

# Base URL - Base URL - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/base-url/

Base URL

[Overview](https://www.canva.dev/docs/extensions/backend-development/base-url/)[Set up a Base URL (with Glitch)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/)[Set up a Base URL (with ngrok)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/)

# Base URL

What is a Base URL? Why do you need one?

Copy page

In the Developer Portal, [extensions](https://www.canva.dev/docs/extensions/platform-concepts/extensions/) have a **Base URL** field. The presence of this field indicates that you must provide Canva with the URL of a web server.

Throughout the lifecycle of the extension, Canva:

  * Sends HTTP requests to the web server.
  * Uses the responses to determine the extension's behavior.



## Handling requests

Unlike some APIs that you may be familiar with—for example, Stripe's [Webhooks API⁠(opens in a new tab or window)](https://stripe.com/docs/webhooks)—Canva doesn't send all requests to a single endpoint.

Instead, when sending requests, Canva appends a path to the **Base URL**. (This is why the field is called **Base URL** and not **Endpoint URL**.)

The appended path identifies:

  * The purpose of the request.
  * The structure of the request that Canva sends.
  * The structure of the response that Canva expects to receive.



For example, if the **Base URL** of a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) is `example.com`, Canva may send requests to the following endpoints:

  * `example.com/publish/resources/find`
  * `example.com/publish/resources/get`
  * `example.com/publish/resources/upload`



For each of these endpoints, Canva sends a request that conforms to a schema and expects the responses to conform to a schema of their own.

The documentation for each extension point explains:

  * The endpoints an extension needs to support. (This can change depending on the extension's configuration.)
  * The structure of the requests that Canva sends to an extension.
  * The structure of the responses that an extension must send back to Canva.



You can find this documentation in the sidebar, under the **Extension points** heading.

## Setting up a Base URL

You can use any programming language, framework, or architecture to set up a **Base URL** , but for Canva to send requests and receive responses, the server must be available via public URL (that is, not `localhost`).

For examples of how to set up a **Base URL** , see the following guides:

  * [Set up a Base URL (with Glitch)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-glitch/)
  * [Set up a Base URL (with ngrok)](https://www.canva.dev/docs/extensions/backend-development/base-url/base-url-ngrok/)



All server-side examples in this documentation use Express.js. This is because the framework is not opinionated, which keeps the examples simple.
