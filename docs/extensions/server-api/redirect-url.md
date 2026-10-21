---
url: https://www.canva.dev/docs/extensions/server-api/redirect-url/
title: Redirect URL - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:46.644421+00:00
---

# Redirect URL - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/server-api/redirect-url/

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

# Redirect URL

API reference for the "Redirect URL" endpoint.

Copy page

When a user attempts to authenticate with an app, Canva begins the authentication flow by opening a pop-up window. This window:

  * Redirects users to the app's **Redirect URL**.
  * Appends query parameters to the **Redirect URL**.



You can configure an app's **Redirect URL** via the Developer Portal.

![](https://www.canva.dev/_next/static/media/img-ed8965fca1.9cf4857b.jpg)

The query parameters include the user's ID, which the app can use to authenticate the user.

To learn more, refer to [Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).

## Request

### Endpoint
    
    
    GET <redirect_url>

BASH

Copy

### Query

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`brand`| string| Yes| The ID of the user's team.  
`extensions`| string| Yes| The extension points the user is attempting to authenticate with.  
`signatures`| string| Yes| A comma-separated list of request signatures.  
`state`| string| Yes| A token the app must return to Canva at the end of the authentication flow.  
`time`| string| Yes| The UNIX timestamp (in seconds) of when the user started the authentication flow.  
`user`| string| Yes| The ID of the user.  
  
#### Example
    
    
    <redirect_url>?brand=<brand>&extensions=<extensions>&signatures=<signatures>&state=<state>&time=<time>&user=<user>

BASH

Copy
