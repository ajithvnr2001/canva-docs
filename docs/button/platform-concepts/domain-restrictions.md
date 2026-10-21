---
url: https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/
title: Domain restrictions - Platform concepts - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:59.556801+00:00
---

# Domain restrictions - Platform concepts - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/

Platform concepts

[Domain restrictions](https://www.canva.dev/docs/button/platform-concepts/domain-restrictions/)[HTML API vs. JavaScript API](https://www.canva.dev/docs/button/platform-concepts/html-api-vs-js-api/)[Local development](https://www.canva.dev/docs/button/platform-concepts/local-development/)

# Domain restrictions

Copy page

By default, Canva Button API keys are locked to the following domains:

  * canva.com
  * localhost



If you try to use your API keys from other domains, Canva blocks the request and responds with a [Forbidden (403)](https://www.canva.dev/docs/button/troubleshooting/403-forbidden-error/) error.

Because of domain restrictions, it's not possible to add the Canva Button to an HTML file on your local machine and open that file in a web browser. You need to serve the HTML file via `localhost`. To learn more, refer to [Local development](https://www.canva.dev/docs/button/platform-concepts/local-development/).

## Adding domains to the allowlist

To add a domain to Canva's allowlist:

  1. Log in to the [Developer Portal⁠(opens in a new tab or window)](https://canva.com/developers).
  2. Under the **Your Canva Button integrations** heading, find the relevant integration and select **View**.
  3. Select **Add a referrer domain**.
  4. Enter a domain in the text field, such as `example.com`.



Changes to the form save automatically.

### Using wildcard symbols

You can use the wildcard symbol (an asterisk) when adding domains in the allowlist. This makes it possible for Canva to accept requests from variations of a domain name.

The following table demonstrates some ways to use the wildcard symbol:

Domain| Matches  
---|---  
`example.com`| The exact domain name.  
`*.example.com`| The domain name and subdomains.  
`*.example.com*`| The domain name, subdomains, and subdirectories.
