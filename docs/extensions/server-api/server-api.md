---
url: https://www.canva.dev/docs/extensions/server-api/server-api/
title: Overview - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:43.648876+00:00
---

# Overview - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/server-api/server-api/

App Development

[Overview](https://www.canva.dev/docs/extensions/)[Quickstart](https://www.canva.dev/docs/extensions/quickstart/)[Changelog](https://www.canva.dev/docs/extensions/changelog/)

Platform concepts

Apps

Extensions

[Regions](https://www.canva.dev/docs/extensions/platform-concepts/regions/)[Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/)[Deprecation policy](https://www.canva.dev/docs/extensions/platform-concepts/deprecation-policy/)

Extensions

Content extensions

Publish extensions

Backend development

Base URL

[Continuation](https://www.canva.dev/docs/extensions/backend-development/continuation/)

Signature verification

SDKs

Distribution

UX guidelines

[Submission checklist](https://www.canva.dev/docs/extensions/distribution/submission-checklist/)[Creating the App Directory listing](https://www.canva.dev/docs/extensions/distribution/app-directory-listing/)

Server API

[Overview](https://www.canva.dev/docs/extensions/server-api/server-api/)[GET /apps/configured](https://www.canva.dev/docs/extensions/server-api/get-apps-configured/)[POST /configuration](https://www.canva.dev/docs/extensions/server-api/post-configuration/)[POST /configuration/delete](https://www.canva.dev/docs/extensions/server-api/post-configuration-delete/)[POST /content/resources/find](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/)[POST /publish/resources/find](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/)[POST /publish/resources/get](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/)[POST /publish/resources/upload](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/)[Redirect URL](https://www.canva.dev/docs/extensions/server-api/redirect-url/)

Reference

[Languages](https://www.canva.dev/docs/extensions/reference/supported-languages/)

# Overview

Learn how Canva's Server API works.

Copy page

Depending on the [extensions](https://www.canva.dev/docs/extensions/platform-concepts/extensions/) added to an app, Canva may send HTTP requests to a web server. You can configure the URL of this web server via the Developer Portal on a per-extension basis.

This page contains some essential things to know about the interactions between Canva and your app's server.

For API reference documentation, see the "Server API" section in the sidebar.

## Requests

Canva mostly sends requests to an app's server, rather than the reverse. This means most requests are outbound (from Canva to the app) and not inbound (from the app to Canva). It's only in certain situations that apps send requests to Canva, such as at the end of an [authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/) flow.

When Canva sends requests:

  * The request bodies are serialized as JSON.
  * The properties in the request body depend on: 
    * The endpoint receiving the request.
    * How the extension is configured via the Developer Portal.
    * The action taken by the user (for example, when a user searches for something, the request body includes a `query` property).



Canva occasionally adds new properties to request bodies. This is considered a non-breaking change. Your extensions must be prepared to handle the presence of new fields.

### Base URL

Canva doesn't send all requests to a single endpoint. Instead, developers provide a **Base URL** for each of the app's extensions. Then, when sending requests, Canva appends a path to the **Base URL**. This path identifies:

  * The purpose of the request.
  * The structure of the request that Canva sends.
  * The structure of the response that Canva expects to receive.



To learn more, see [Base URL](https://www.canva.dev/docs/extensions/backend-development/base-url/).

## Responses

Apps must respond to requests with JSON bodies. The body must include a `type` property that identifies if the request was successful or not.

Apps must not include unrecognized properties in response bodies.

### Successful responses

If the value of the `type` property is `"SUCCESS"`, the response body must conform to a schema that is (typically) determined by the path of the request. The exact schemas are detailed in the API reference documentation.

This is an example of a `"SUCCESS"` response for the [`/publish/resources/upload`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/) endpoint:
    
    
    {
    
      "type": "SUCCESS",
    
      "url": "https://..."
    
    }

JSON

Copy

### Unsuccessful responses

If the value of the `type` property is `"ERROR"`, the response must contain an `errorCode` property that indicates what went wrong. The supported error codes are listed in the API reference documentation.

This is an example of an `"ERROR"` response:
    
    
    {
    
      "type": "ERROR",
    
      "errorCode": "INVALID_REQUEST"
    
    }

JSON

Copy

## Status codes

Canva expects endpoints to respond to requests with a `200` status code—even if an error has occurred. The only exception to this rule is when a request fails [signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/). In that case, the endpoint should reject the request with a `401` status code.

## Referring domains

If an app is available in the Global region, requests arrive from the `canva.com` domain. If an app is available in the China region, requests arrive from the `canva.cn` domain.

The examples in this documentation assume requests are coming from `canva.com`. If you're developing an app in China, replace references to `canva.com` with `canva.cn`.

## Timeout duration

All HTTP requests that Canva sends to an app have a timeout duration. If the app fails to respond to the request within this duration, the request fails. The exact duration depends on the request.

If timeouts occur too frequently, Canva sends an automated message to the developer. If the timeouts aren't solved within a reasonable time frame, Canva may disable the app.

## Rate limiting

Canva sends requests to apps via a handful of IP addresses. If your endpoints support rate limiting—and they should—they may start to block the requests if their frequency passes a certain threshold. To handle this, whitelist requests from Canva's domains.

## Signature verification

Before [submitting an app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/), it must support signature verification. This is a security measure that prevents third-parties from sending requests to the app, which protects your app and Canva's users from bad actors.

To learn more about signature verification, see [Signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/).
