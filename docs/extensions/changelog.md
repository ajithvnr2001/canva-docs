---
url: https://www.canva.dev/docs/extensions/changelog/
title: Changelog - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:41.175641+00:00
---

# Changelog - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/changelog/

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

# Changelog

The latest updates to Canva's app development platform.

Copy page

**2021-09-02**

  * [Content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/) can now import video files. To learn more, see [Videos](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/videos/).



**2021-06-29**

  * Content extensions can now include multiple types of content, such as images _and_ embeds, in a single response. This is a backwards-compatible change that makes content extensions a lot more flexible. To learn more, see [Content types](https://www.canva.dev/docs/extensions/extensions/content-extensions/content-types/).



**2021-06-22**

  * When Canva sends requests to the [`/content/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/) endpoint, it now includes a `types` property in the request body. This property contains an array of content types that can appear in the response, which is in preparation for a change that will let [content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/) return different types of resources (for example, images _and_ embeds) in a single response. The existing `type` property, which can only contain a string, is now deprecated.



**2021-05-19**

  * When a user publishes a design via a publish extension, the `designId` property in the [find resources request](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/) and [upload request](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/) is no longer obfuscated. This makes it possible to open published designs via the [Canva Button⁠(opens in a new tab or window)](https://www.canva.com/button/).



**2021-05-13**

  * [Content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/) can now import HEIC images into Canva.



**2021-02-03**

  * Apps that support authentication can now let users disconnect (de-authenticate) from the app. To learn more, refer to [Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).



**2021-01-15**

  * When a user publishes a design via a publish extension, [the find resources request](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/) now includes a `designId` property.



**2020-12-16**

  * When a user publishes a design via a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/), [the upload request](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/) now includes a `designId` property. This property contains the ID of the user's design. This ID is obfuscated and does not change between uploads, which allows extensions to detect when a user is re-publishing a design.



**2020-12-09**

  * Improved the **Client secret** field in the Developer Portal. Previously, the key was provided as a base64url-encoded string and your app needed to convert it into a base64-encoded string. The key is now provided as a base64-encoded string.


