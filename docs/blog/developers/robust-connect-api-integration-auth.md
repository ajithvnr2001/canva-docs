---
url: https://www.canva.dev/blog/developers/robust-connect-api-integration-auth/
title: Robust authentication for your Connect API integration on native apps - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:07.726077+00:00
---

# Robust authentication for your Connect API integration on native apps - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/robust-connect-api-integration-auth/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Connect API

# Robust authentication for your Connect API integration on native apps

Best practices for authenticating users using the Connect API on native apps.

![](https://www.canva.dev/_next/static/media/thumbnail.b1a6fec5.jpg)

* * *

  * 


Sidney AmaniApr 4, 2024

* * *

With the [Connect API](https://www.canva.dev/docs/connect/) launch around the corner, here are some tips for building a robust authentication flow for Connect API integrations on mobile and desktop clients. Our main advice is to _favor a browser-based authentication flow when redirecting users to log in or sign up on Canva_.

Let’s dive deeper. The Connect API lets you access your Canva designs, assets, folders, and so on, directly in your product. It's a REST API built on top of the OAuth protocol. Apps that use the Connect API are called integrations (this is a way of differentiating them from SDK apps that live within the Canva editor). For example, the Connect API powers the new [Canva integration for Slack⁠(opens in a new tab or window)](https://www.canva.com/integrations/slack/).

When building an integration, OAuth requires that users log in to Canva to consent to the permissions scopes requested by your integration. Your integration is expected to redirect users to the authorization endpoint, where they're presented with login options. When logged in, they can consent to the scopes.

![Browser-based authentication flow](https://www.canva.dev/_next/static/media/my-app.c29d0718.png)

As stated previously, we strongly recommend that your integration implements a browser-based authentication flow for users to log in and sign up on Canva. In a browser-based authentication flow, users are taken out of a native app and into their default web browser, where they log in to Canva to consent to scopes. The user is then taken back to the native app where they can use the features of your integration.

This is in contrast to an embedded browser-based authentication flow. An embedded browser, sometimes called a webview, is a browser that is embedded in a native app to display web content. These can be found on mobile and desktop apps. The problem with embedded browsers is that a malicious developer can transform them into [phishing or sniffing vessels⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc8252#section-8.12) and release an app that put users privacy at risk. Because embedded browsers don't have an address bar, users can't check whether they're logging in on canva.com instead of a rogue copy. A browser-based authentication flow protects users from these risks.

Some identity providers (for example, Google) now completely reject authentication requests originating from an embedded browser and other identity provider are likely to join Google on this path. If your integration has to use an embedded browser flow, be aware that users can't use the **Continue with Google** option on the Canva login page.

There are pros and cons to browser-based vs embedded browser authentication. A common concern is that browser-based authentication disrupts the user experience by taking them out of their native app. While this is true, consider the security benefits mentioned previously. There are also usability benefits. Your users are likely already logged in on their default browsers so they no longer need to copy credentials over to the embedded browser. If you want to experience a browser flow in action, try the [Canva desktop app⁠(opens in a new tab or window)](https://www.canva.com/en_au/help/canva-desktop-app/) or the [Slack integration for Canva⁠(opens in a new tab or window)](https://www.canva.com/integrations/slack/).

We recommend that when the user consents to scopes, you redirect to an endpoint controlled by your integration’s backend and exchange the authorization code for your tokens from there. This way, you can call the exchange endpoint while securely passing the client's ID and secrets. Currently, the Connect API only supports confidential OAuth clients, meaning your integration must be able to store secrets securely. The Connect API won’t let you register in-app redirect URIs with custom protocol or schemes because public OAuth clients typically used these. We also recommend encryption at rest for secrets and tokens.

In conclusion, the key takeaways from this article are:

  * When using Canva OAuth, we recommend a browser-based authentication flow because it offers better security for users.
  * Some identity providers reject embedded browser authentication requests.
  * Make sure your integration can securely exchange the authorization code for tokens. We recommend using encryption at rest to store these tokens.



For more information, see:

  * [OAuth 2.0 for Native Apps⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc8252)
  * [Auth0's Mobile Device Login Flow Best Practices⁠(opens in a new tab or window)](https://auth0.com/docs/get-started/authentication-and-authorization-flow/device-authorization-flow/mobile-device-login-flow-best-practices#phishing-and-security-issues)



_Special thanks to Grant Noble his review and to Jesse Birthisel for the illustrations._

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.c59330ae.jpg)](https://www.canva.dev/blog/developers/building-with-content-publisher-part1/)

[Content Publisher IntentMeet the Content Publisher Intent - Part 1Understanding data flow and structure for publishing](https://www.canva.dev/blog/developers/building-with-content-publisher-part1/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Feb 19, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.8a859554.jpg)](https://www.canva.dev/blog/developers/searchable-list-view-config/)

[App ComponentConfiguring your SearchableListViewYour guide to all of the properties of the SearchableListView app component configs](https://www.canva.dev/blog/developers/searchable-list-view-config/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)May 16, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.2a37fda3.jpg)](https://www.canva.dev/blog/developers/canva-developers-wrapped-2024/)

[2024Canva Developers 2024 WrappedAnother exciting year for Canva Developers is coming to a close. Learn about all the amazing growth our ecosystem has seen this year.](https://www.canva.dev/blog/developers/canva-developers-wrapped-2024/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Dec 20, 2024
