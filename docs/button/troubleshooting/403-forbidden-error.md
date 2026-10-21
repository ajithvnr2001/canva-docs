---
url: https://www.canva.dev/docs/button/troubleshooting/403-forbidden-error/
title: Forbidden (403) - Troubleshooting - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:59.724517+00:00
---

# Forbidden (403) - Troubleshooting - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/troubleshooting/403-forbidden-error/

Troubleshooting

[Forbidden (403)](https://www.canva.dev/docs/button/troubleshooting/403-forbidden-error/)

# Forbidden (403)

Copy page

While creating an integration, you may encounter the following **Forbidden (403)** error:

![](https://www.canva.dev/_next/static/media/the-403-forbidden-error.bf0b498f.jpg)

This error can occur for a few different reasons.

## Design permissions

A user can only edit a design that they created. If you call the method to edit a design and pass through an ID of a design not created by the current user, Canva responds with a `403` error.

## Domain restrictions

By default, Canva Button API keys are locked to the following domains:

  * canva.com
  * localhost



If you try to use a Canva Button API key from other domains, Canva blocks the request and responds with a `403` error. To learn how to add other domains to Canva's allowlist, refer to [Adding domains to the allowlist](https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/#adding-domains-to-the-allowlist).

## Local development

Because of [domain restrictions](https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/), it's not possible to add the Canva Button to an HTML file on your local machine and open that file in a web browser. You need to serve the HTML file via `localhost`. To learn how to develop locally with the Canva Button, refer to [Local development](https://www.canva.dev/docs/button/platform-concepts/local-development/).

## Referrer-Policy HTTP header

When an integration loads, the request that's sent to Canva must include the `Referer` HTTP header. Canva uses the `Referer` header to identify if the integration's domain is on the allowlist.

Sometimes though, the `Referrer-Policy` header is set to a value that prevents Canva from receiving the `Referer` header:
    
    
    Referrer-Policy: no-referrer
    
    Referrer-Policy: no-referrer-when-downgrade

Copy

As a result, Canva can't confirm if the origin domain is on the allowlist and blocks the request, causing the 403 error.

To fix this problem, Canva recommends setting the `Referrer-Policy` header to the `strict-origin-when-cross-origin` header. This ensures that the origin is sent with cross-origin requests, which allows Canva to verify if the origin domain is on the allowlist.

For more information, refer to [Referrer-Policy⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy).
