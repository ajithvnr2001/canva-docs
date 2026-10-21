---
url: https://www.canva.dev/docs/extensions/server-api/get-apps-configured/
title: GET /apps/configured - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:43.850064+00:00
---

# GET /apps/configured - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/server-api/get-apps-configured/

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

# GET /apps/configured

API reference for the "/apps/configured" endpoint.

Copy page

When a user reaches the end of an authentication flow, an app must perform a `302` redirect to the following URL:
    
    
    https://www.canva.com/apps/configured

BASH

Copy

This redirect:

  * Closes the authentication pop-up window.
  * Reloads the app (or displays an error, if the authentication is unsuccessful).
  * Protects the app against [cross-site request forgery⁠(opens in a new tab or window)](https://owasp.org/www-community/attacks/csrf) (CSRF) attacks.



The app must also append the required [query parameters](https://www.canva.dev/docs/extensions/server-api/get-apps-configured/#query).

To learn more, refer to [Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).

For guidelines on creating a delightful authentication flow, see [Optimizing the authentication flow](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/authentication/).

If you're creating an app via [canva.cn⁠(opens in a new tab or window)](https://www.canva.cn), redirect users to the `canva.cn` domain instead of `canva.com`.

## Request

### Endpoint
    
    
    GET https://www.canva.com/apps/configured

BASH

Copy

### Query

#### Properties

Property| Type| Required| Description  
---|---|---|---  
`state`| string| Yes| A token that Canva provides to the app at the start of the authentication flow. The app must return this token to Canva at the end of the authentication flow. This protects the app against [Cross-Site Request Forgery⁠(opens in a new tab or window)](https://owasp.org/www-community/attacks/csrf) (CSRF) attacks.  
`success`| boolean| Yes| If `true`, Canva closes the authentication pop-up window and reloads the app. If `false`, Canva closes the authentication pop-up window and displays an error.  
  
#### Example
    
    
    https://www.canva.com/apps/configured?success=true&state=<state>

BASH

Copy
