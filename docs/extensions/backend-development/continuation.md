---
url: https://www.canva.dev/docs/extensions/backend-development/continuation/
title: Continuation - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:42.922741+00:00
---

# Continuation - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/continuation/

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

# Continuation

Copy page

When Canva sends an HTTP request to endpoints, it limits the number of resources that can be included in the response. For example, when Canva sends a request to the `/content/resources/find` endpoint, the endpoint must respond with 100 or fewer resources.

If an extension needs to respond with more resources than this limit allows, it can use _continuation_ to deliver the resources across multiple requests and responses.

This topic explains what continuation is and how to support it.

Continuation is also known as _cursor-based pagination_.

## Request-response cycle

Any endpoint that returns a list of resources can support continuation, including:

  * [`/content/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/)
  * [`/publish/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/)



If an endpoint supports continuation, it can include a `continuation` property in the response body:
    
    
    {
    
      "type": "SUCCESS",
    
      "resources": [],
    
      "continuation": "<continuation_token>"
    
    }

JSON

Copy

This property must contain a _continuation token_. A continuation token is a string of characters that, when passed back to the server, identifies how to return the next logical batch of resources. It can be as simple as a page number or a complex string that encodes more information.

The presence of the `continuation` property tells Canva to send another request to the endpoint when more resources are required, such as when a user scrolls through content in a content extension.

The subsequent request that Canva sends has a `continuation` property in the request body. This property contains the continuation token from the previous response:
    
    
    {
    
      "limit": 100,
    
      "user": "<user>",
    
      "brand": "<brand>",
    
      "label": "<label>",
    
      "locale": "<locale>",
    
      "type": "<type>",
    
      "continuation": "<continuation_token>"
    
    }

JSON

Copy

The endpoint can use the token to respond with the relevant resources. For example, if the `continuation` property contains a value of `"2"`, the endpoint can identify and return the resources that belong to that page.

When there are no more resources to retrieve, the endpoint can set the `continuation` property in the response body to `null`:
    
    
    {
    
      "type": "SUCCESS",
    
      "resources": [],
    
      "continuation": null
    
    }

JSON

Copy

This tells Canva to stop sending additional requests to the endpoint.

## Further reading

  * [Paginating Requests in APIs⁠(opens in a new tab or window)](https://ignaciochiazzo.medium.com/paginating-requests-in-apis-d4883d4c1c4c) (medium.com)
  * [“Cursor Pagination” Profile⁠(opens in a new tab or window)](https://jsonapi.org/profiles/ethanresnick/cursor-pagination/) (jsonapi.org)
  * [How to implement cursors for pagination in an api⁠(opens in a new tab or window)](https://stackoverflow.com/questions/18314687/how-to-implement-cursors-for-pagination-in-an-api) (stackoverflow.com)



## Next steps

To learn how to add continuation to an extension, see the following guides:

  * [Continuation for content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/pagination/)
  * [Continuation for publish extensions](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)


