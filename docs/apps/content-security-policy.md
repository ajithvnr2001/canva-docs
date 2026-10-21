---
url: https://www.canva.dev/docs/apps/content-security-policy/
title: Content Security Policy - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:55:29.142213+00:00
---

# Content Security Policy - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/content-security-policy/

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

# Content Security Policy

What is a Content Security Policy? How does it affect app development?

Copy page

A Content Security Policy (CSP) is a security mechanism that prevents web pages from accessing browser APIs and resources, reducing the risk of certain threats, such as [cross-site scripting⁠(opens in a new tab or window)](https://owasp.org/www-community/attacks/xss/).

Canva applies a Content Security Policy to the iframe that embeds an app's source code. This makes apps more secure, but:

  * The policy blocks some useful features.
  * When an app violates a policy, the app will break.



This page describes what the policy allows and how to troubleshoot violations.

## What is (and isn't) allowed

Apps can:

  * Load audio, fonts, images, and videos from data URLs and HTTPS URLs.
  * Use inline CSS.



Apps can't:

  * Use frames, web workers, or other nested browsing contexts.
  * Load JavaScript from third-party sources.
  * Load CSS stylesheets.
  * Use the `base` element.
  * Use the `form` element's `action` attribute.



To handle form submissions in the app's iframe, attach an `onSubmit` handler to the form and use the `preventDefault` method to prevent the form's default behavior.

## What directives does Canva use?

The behavior of a Content Security Policy is defined with one or more _directives_.

The app's iframe uses the following directives:
    
    
    base-uri 'none';
    
    child-src 'none';
    
    connect-src https: data: wss: https://o13855.ingest.sentry.io https://telemetry.canva.com/v1/traces;
    
    default-src 'none';
    
    font-src  data: https: https://static.canva.com;
    
    form-action 'none';
    
    frame-ancestors https://.canva.com http://localhost:*;
    
    frame-src 'none';
    
    img-src data: https: blob: https://static.canva.com;
    
    media-src  data: https: blob: https://static.canva.com;
    
    object-src 'none';
    
    script-src 'wasm-unsafe-eval'  https://thirdparty-public-apps.canva-apps-dev.com/XX/file.js https://static.canva.com 'nonce-XXXX';
    
    style-src 'unsafe-inline' https://static.canva.com;
    
    worker-src 'none';

Copy

## How to troubleshoot violations

When an app violates the Content Security Policy, an error is logged to the JavaScript Console. You can use this error to identify which policy was violated and then figure out what needs fixing.
