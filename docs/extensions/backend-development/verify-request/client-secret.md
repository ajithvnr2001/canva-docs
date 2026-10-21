---
url: https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/
title: Client secret - Signature verification - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:54.482614+00:00
---

# Client secret - Signature verification - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/

Signature verification

[Overview](https://www.canva.dev/docs/extensions/backend-development/verify-request/)

Client secret

[Client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/)[Decode a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/decode-client-secret/)[Regenerate a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/)

Verify and test

[Verify POST request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/)[Verify GET request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/)[Verify timestamp](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/)[Test signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/)

# Client secret

What is a client secret? Why use one?

Copy page

Every app has a unique _client secret_. This is a sensitive value that's shared between Canva and your app. You need this secret to [verify request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/).

![](https://www.canva.dev/_next/static/media/img-eeeddf1e63.6897a066.jpeg)

To get your app's client secret:

  1. Navigate to an app via the Developer Portal.
  2. Open the **Verification** page.
  3. Under the **Client secret** field, click **Copy**.



We recommend storing client secrets as environment variables.

You should never share a client secret or commit it to source control.
