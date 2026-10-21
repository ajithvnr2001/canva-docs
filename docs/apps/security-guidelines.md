---
url: https://www.canva.dev/docs/apps/security-guidelines/
title: Security guidelines - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:42.873306+00:00
---

# Security guidelines - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/security-guidelines/

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

# Security guidelines

How to keep your app (and its users) secure.

Copy page

At Canva, the security of our platform is paramount, and we expect app developers to maintain similar standards. This page outlines some of the key recommendations to keep your app (and its users) secure.

Canva maintains some responsibility for security, but not all responsibilities. For a complete list of security responsibilities you'll need to consider for your app, see [Shared responsibility model for intents](https://www.canva.dev/docs/apps/shared-responsibility-intents/).

## Use reasonable security measures

Security is a huge topic, and it's beyond the scope of this documentation to explain every measure you could take to keep an app secure, but a good starting point is to ensure your app is not vulnerable to the [OWASP Top 10⁠(opens in a new tab or window)](https://owasp.org/www-project-top-ten/).

## Respect Canva's Content Security Policy

Canva applies a Content Security Policy (CSP) to the app's iframe. This policy prevents apps from loading certain resources within the iframe, such as third-party scripts. Apps can't circumvent the policy, but the app may break in surprising ways if it violates the policy, so it's important to be mindful of the restrictions.

To learn more, see [Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/).

## Configure Cross-Origin Resource Sharing

Cross-Origin Resource Sharing (CORS) is a security feature of web browsers that blocks client-side HTTP requests between different origins. We recommend setting the most restrictive policy possible.

To learn more, see [Cross-Origin Resource Sharing](https://www.canva.dev/docs/apps/cross-origin-resource-sharing/).

## Verify HTTP requests

When an app sends an HTTP request to a backend, the backend should verify that the request is from a known, trusted source. This prevents bad actors from sending arbitrary (and potentially malicious) requests to the backend.

For Node.js backends, we recommend using the [`@canva/app-middleware`⁠(opens in a new tab or window)](https://www.npmjs.com/package/@canva/app-middleware) package, which provides built-in JWT verification, JWKS caching, and error handling.

To learn more, see [HTTP request verification](https://www.canva.dev/docs/apps/verifying-http-requests/).

## Store secrets securely

Apps often need to store secrets and tokens, such as API keys or access tokens. There are inherent risks to this, so it's important to consider those risks and mitigate against them.

Here's what we recommend:

  * When extracting information about the current user from a JSON Web Token (JWT), always verify the token. This ensures the token has not been tampered with. For Node.js backends, use the [`@canva/app-middleware`⁠(opens in a new tab or window)](https://www.npmjs.com/package/@canva/app-middleware) package for secure JWT verification. To learn more, see [JSON Web Tokens](https://www.canva.dev/docs/apps/verifying-jwts/).
  * When integrating with third-party services, use tokens that have the least amount of access to that service as possible. This reduces the potential impact of a breach.
  * Use storage mechanisms, such as JavaScript closures instead of WebStorage APIs, to store sensitive values such as API keys. WebStorage APIs can be accessed by anyone with access to the machine, simply by opening the browser's developer tools.
  * Keep secrets and tokens masked from users after they are stored in a database; avoid logging them to the console or displaying them after creation.
  * Use rate-limiting to prevent the misuse of tokens.
  * Transmit tokens securely using `POST` requests rather than including them in the URL query string, to avoid exposure through third-party logging.
  * Always associate access tokens with the combination of the ID of the user _and_ the ID of their team. This ensures that, if a user is removed from the team, their access through the app is also revoked.
  * If an access token is no longer needed, delete the token immediately. For example, delete access tokens as soon as a user deletes their account, data, or connection between Canva and a third-party platform.
  * Maintain strict token and capability isolation, ensuring that all token-bound functionality is available only to the user it was issued to.
  * Use Transport Layer Security (TLS) protocols and ciphers to encrypt traffic between your app, its backend, and other services. This ensures any access tokens or secrets are never transmitted unencrypted.



## Maintain ownership of subdomains

Many apps rely on dedicated subdomains to host backend services, identity endpoints, or other functional components. Because these subdomains often represent trusted surfaces to both users and relying parties, it's essential to ensure they remain properly configured and under your control at all times.

A subdomain may become vulnerable if its DNS records point to a resource that's unclaimed, de-provisioned, or misconfigured. This can enable a subdomain takeover, where an attacker gains control of the subdomain and can serve malicious content or impersonate your service.

For example, if an attacker controls any of these subdomains, they may be able to:

  * Issue fraudulent tokens or present malicious signing keys
  * Steal authorization or refresh tokens
  * Spoof authentication or authorization flows
  * Intercept or manipulate redirect flows
  * Masquerade as your IdP or authorization server



Because modern authentication protocols rely heavily on domain trust, you must monitor and secure these subdomains.

To reduce the risk of subdomain takeover, we recommend you do the following:

  * Regularly verify that any referenced service is actually running and under your control.
  * If a backend or identity service is decommissioned or migrated, update your DNS configuration immediately.
  * Make sure you have strict lifecycle oversight of these subdomains because of the severe impact of compromise.
  * Check DNS configurations, hosting status, and any service-specific ownership checks.
  * Avoid pointing subdomains to temporary, unmanaged, or short-lived resources unless you have processes ensuring they can't become orphaned.
  * Monitor for misconfigurations or unintended DNS targets. Even short periods of misalignment can be enough for an attacker to claim a subdomain.
  * Document subdomain lifecycle events, including provisioning, migration, and decommissioning, as part of your operational security practices.



## Don't require users to download files

Your app should never ask or require users to download external files — especially executable ones. External files are a significant security risk and, at the very least, requiring users to download them erodes trust.
