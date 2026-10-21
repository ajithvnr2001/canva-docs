---
url: https://www.canva.dev/docs/apps/rest-apis/security-recommendations/
title: Security recommendations for the Canva REST APIs - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:40.284568+00:00
---

# Security recommendations for the Canva REST APIs - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/security-recommendations/

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

# Security recommendations for the Canva REST APIs

Recommended security practices for your app.

Copy page

**Important Note:** Apps that use the Canva REST APIs must be associated with a web app. We don’t support apps in environments where it's difficult to securely store credentials, such as mobile or desktop apps, browser extensions, Progressive Web Apps (with no backend), and Single Page Apps.

Avoid using the REST APIs in these environments, because they don't offer the necessary security features to protect the API credentials.

Canva uses a shared responsibility model to define what developers are responsible for when creating apps, and what Canva is responsible for as the owner of the platform. For a list of security responsibilities that you'll need to consider when creating your app, see the [Shared responsibility model for the Canva REST APIs](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/).

## Redirect URIs

Redirect URIs appear as URLs and are safe to include in published code. However, make sure that the redirect URIs defined in your apps are only limited to domain names that you directly control. After you complete local development and testing, you must remove `127.0.0.1`, `localhost`, and related domains from your app’s configuration.

## Scopes

Your app should only request the minimum scopes needed to perform its functions. If any of your app's tokens become compromised, this can help limit the amount of damage that can occur. You should periodically review the list of scopes requested by your app, and remove any scopes that are unused or no longer required.

## Secure secret storage

A _client ID_ identifies your app, and frequently appears in OAuth requests and other contexts. Your client ID can be shared freely in code and email, and cannot be used alone to act on your app's behalf. A _client secret_ asserts your platform’s access rights and identity, when generating the user access tokens or refresh tokens.

Using your client secret, you can generate:

  * User access tokens to access the REST APIs on a user's behalf.
  * Refresh tokens that can generate new user access tokens.



You must securely store your client secret and any generated user access tokens and refresh tokens. Secure storage depends on your platform's architecture and security risk model, so there isn't a single approach that suits everyone.

### Client secrets

Don't distribute client secrets in email, chat, public code repositories, or anywhere else where it might be leaked to unauthorized users.

If you are generating access or refresh tokens using a web app or backend server, consider storing your client secret in a secrets storage vault, such as AWS Secrets Manager or HashiCorp Vault. If these options aren’t available, an encrypted environment variable or server secret might be adequate.

Don't expose client secrets in source code or platform configuration, and never retrieve secrets using HTTP API calls (or similar) when generating access tokens on the client.

## User access tokens and refresh tokens

User access tokens should be encrypted and stored separately from refresh tokens. Think carefully about the systems and processes that can access these tokens. Discard tokens when they are no longer needed.

## GitHub secret scanning

Canva has partnered with GitHub secret scanning to automatically detect and revoke Canva secrets that have been published to GitHub repositories. As a result, if GitHub detects your access token or client secret in a public GitHub repository, we will automatically revoke it to help minimize the harm of leaked secrets.

## App security

This is a list of good practices to help secure your app.

  * Don't expose tokens to the end-user after they're stored in your database.
  * Ensure there’s no functionality that echoes tokens (or any other customer secrets) back to the user: 
    * Pay close attention to error scenarios that might cause a token to be visible in error messages or debug logs.
  * If a secret storage vault is not an option, consider creating a middleware layer instead of storing the token in your app's code.
  * To help prevent misuse of the token, lock down the usage of your app itself.
  * Consider how an attacker can abuse your app's functionality to gain access to a token, or trigger functionality that might be undesirable. Review the [OWASP Top 10 Web Vulnerabilities⁠(opens in a new tab or window)](https://owasp.org/www-project-top-ten/), such as XSS, CSRF, and SQLi.
  * Implement rate-limiting. Ensure your app uses rate-limiting in a way that prevents misuse of tokens.
  * Use a database to store tokens, and don't store tokens in the code.
  * Ensure there is no way to expose one user's token (or the functionality of that token) to another user.
  * Ensure tokens are stored in a way that directly links them to the Canva user and team.
  * If a user deletes their account or revokes consent for your app, ensure you delete any tokens for the user from your systems.
  * If you no longer need a customer's token, delete it immediately from your systems.
  * Conduct regular vulnerability scans against your app, and ensure that secret scanning is enabled on all related code repositories.
  * Ensure that client secrets, user access tokens, and refresh tokens aren't sent to your platform's logs.



## External services

External services (such as databases, email providers, AWS, third-party APIs) should be used in a secure way. This includes the following good practices:

  * Don't share service credentials across different apps. Each app should have unique credentials for accessing external services.
  * Ensure that service credentials have the minimal set of permissions to perform operations.
  * Ensure that all communications to external services use secure transport mechanisms that don't transport data in plaintext.
  * Require secure transport mechanisms (such as HTTPS/TLS) that are resistant to eavesdropping.
  * Requests must fail if they return a transport security error (such as expired TLS certificates, or server name mismatch).



## Logging

We recommend adding security-specific logging and telemetry to your platform, as this can provide useful information in the event of a security incident. A security log should include the following:

  * Authentication and authorization events. This should include failed attempts.
  * Service configuration changes.
  * Object reads and writes.
  * Permission changes.



Your logs should use consistent timestamps for each event. Logs should also include a reference to the user’s identity and an IP address.

Don't log client secrets, user access tokens, or refresh tokens.

## Infrastructure and hosting

Ensure you follow the security recommendations from your cloud service or hosting provider. This can include:

  * Enabling Multi-Factor Authentication (MFA).
  * Using strong passwords.
  * Ensuring that accounts with access to your production systems actually need that access.
  * If you are backing up your data, ensure that you store it in a safe location. Unsecured backups are easy targets for attackers to steal your app's data and secrets.


