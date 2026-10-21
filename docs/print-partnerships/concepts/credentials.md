---
url: https://www.canva.dev/docs/print-partnerships/concepts/credentials/
title: Credentials overview - General information - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:59.890062+00:00
---

# Credentials overview - General information - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/concepts/credentials/

General information

[Evaluating Canva](https://www.canva.dev/docs/print-partnerships/concepts/evaluating-canva/)[Authentication](https://www.canva.dev/docs/print-partnerships/concepts/authentication/)[Credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/)[Request credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/)[Product catalog](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/)[Proofing](https://www.canva.dev/docs/print-partnerships/concepts/proofing/)[Security](https://www.canva.dev/docs/print-partnerships/concepts/security/)[User journey](https://www.canva.dev/docs/print-partnerships/concepts/user-journey/)

# Credentials overview

Copy page

To set up the integration, partners need credentials.

There are two variations of these credentials:

  * Production
  * Test



You must use the production credentials for integrations running in a _live_ environment. A live environment is where users can purchase prints of their designs. You can use the test credentials while developing an integration to avoid being charged for test purchases.

## List of credentials

Partners need the following credentials:

### Partner ID

A unique ID that identifies you as a print partner.

### Partner API key

A public API key for initializing the Partnership SDK.

### Partner API secret

A secret API key for generating an autoAuthToken.

### Artwork API secret

A secret API key for purchasing the print-quality version of a user's artwork.

Secrets are sensitive values. You should never share or commit them to source control. Doing so may allow attackers to steal your user's private designs.

We recommend loading secrets into your integration via environment variables.

## Request credentials

For security reasons, Canva sends credentials to partners via encrypted files. Canva creates the encrypted files using a public key that partners provide. Partners then decrypt the files using their private key.

To request credentials from Canva, see [Request credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/).

## Domain restrictions

By default, the API keys are locked to the following domains:

  * canva.com
  * localhost



If requests don't originate from these domains, Canva responds to requests with a `403` error.

To use the API keys from domains where you intend to deploy and test the integration, [add the domains to Canva's allowlist](https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/#step-2-provide-the-public-key-to-canva).

## Rotate credentials

For security reasons, Canva recommends rotating the credentials periodically.

Specifically, these:

  * Partner API key.
  * Partner API secret.
  * Artwork API secret.



The Partner ID doesn't change.

To rotate the credentials:

  1. Request new credentials from Canva. To raise a request, see [Request credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/).
  2. Update the integration to use the new credentials.



Rotating credentials results in a downtime. The integration remains down from the time Canva creates the new credentials until the partner updates the integration to use those credentials.
