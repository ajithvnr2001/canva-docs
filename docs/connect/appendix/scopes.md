---
url: https://www.canva.dev/docs/connect/appendix/scopes/
title: Scopes - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:38.941264+00:00
---

# Scopes - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/connect/appendix/scopes/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

API reference

[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)

App UI Kit reference

[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

Canva REST API reference

[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)

Webhooks notification reference

[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

Tools

[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)

# Scopes

Copy page

The `scope` parameter specifies the types of access that your app needs for a user's account. The list of possible scopes used in the Canva REST APIs are shown below:

Scope| Description  
---|---  
`asset:read`| View the metadata for the user's assets, such as uploaded images.  
`asset:write`| Upload, update, or delete assets on the user's behalf.  
`brandtemplate:content:read`| Read the content of the brand templates associated with the user's brand.  
`brandtemplate:content:write`| Publish brand templates associated with the user's brand.  
`brandtemplate:meta:read`| View the metadata of the brand templates associated with the user's brand.  
`collaboration:event`| Receive webhook notifications about events relevant to the user.  
`comment:read`| View the comments on the user's designs, and the associated metadata.  
`comment:write`| Create comments and replies on the user's designs.  
`design:content:read`| View the contents of the user's designs.  
`design:content:write`| Create designs on the user's behalf.  
`design:meta:read`| View the metadata of the user's designs.  
`email`| Read user email address through OIDC.  
`folder:permission:write`| Set, update, or remove permissions assigned to the user's folders.  
`folder:read`| View the metadata and contents of the user's folders, including their **Projects** folder.  
`folder:write`| Add, move, or remove the user's folders. It also lets you edit folder metadata, such as the folder's name.  
`openid`| Read user information through Open ID Connect (OIDC).  
`profile`| Read user profile information through OIDC.  
`profile:read`| Read a user's profile and account information.  
  
For example, if you just require your app to read design metadata, you can use the `design:meta:read` scope. If you require your app to read designs, as well as write to any folder, you can use both the `design:meta:read` and the `folder:write` scopes.

When enabling and using scopes, you must be explicit.

For example, the `asset:write` scope doesn't grant `asset:read` permissions. To get both read and write permissions for assets, you must enable both scopes for your app, and request both scopes during the authorization process.
