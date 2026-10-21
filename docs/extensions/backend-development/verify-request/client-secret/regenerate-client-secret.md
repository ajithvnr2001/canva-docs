---
url: https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/
title: Regenerate a client secret - Signature verification - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:54.721443+00:00
---

# Regenerate a client secret - Signature verification - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/

Signature verification

[Overview](https://www.canva.dev/docs/extensions/backend-development/verify-request/)

Client secret

[Client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/)[Decode a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/decode-client-secret/)[Regenerate a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/)

Verify and test

[Verify POST request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/)[Verify GET request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/)[Verify timestamp](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/)[Test signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/)

# Regenerate a client secret

What to do when a client secret is leaked.

Copy page

If your app's client secret is leaked or committed to source control, the secret is no longer secure and you need to regenerate it. But this poses a problem: disabling the current secret will cause verified requests to fail until the app starts using the new secret.

To avoid this problem, Canva supports _key rotation_. This means you can generate a new secret without immediately disabling the existing secret.

When more than one client secret is active at a time, Canva sends multiple request signatures with every request. Each signature is calculated using one of the active client secrets. The app only needs to verify one of these signatures to confirm the authenticity of the request. This allows you to regenerate client secrets without causing downtime.

![](https://www.canva.dev/_next/static/media/img-6a3d4a68db.1004aa30.jpeg)

To regenerate your app's client secret:

  1. Navigate to an app via the Developer Portal.
  2. Open the **Verification** page.
  3. Click **Regenerate**.
  4. In the **Expiry time** field, enter the number of hours the existing client secret should remain active for. The maximum value is 168 hours (7 days).
  5. Click **Regenerate client secret**.



The new client secret appears in the **Client secret** field.
