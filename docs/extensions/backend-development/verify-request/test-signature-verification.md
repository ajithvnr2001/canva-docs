---
url: https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/
title: Test signature verification - Signature verification - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:56.381220+00:00
---

# Test signature verification - Signature verification - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/

Signature verification

[Overview](https://www.canva.dev/docs/extensions/backend-development/verify-request/)

Client secret

[Client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/)[Decode a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/decode-client-secret/)[Regenerate a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/)

Verify and test

[Verify POST request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/)[Verify GET request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/)[Verify timestamp](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/)[Test signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/)

# Test signature verification

Check if your app is correctly verifying request signatures.

Copy page

If your app has [signature verification check](https://www.canva.dev/docs/extensions/backend-development/verify-request/) enabled, you must ensure that the verification logic is implemented correctly before [submitting your app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/). You can do this by running a signature verification test via the Developer Portal.

The signature verification test works by sending a combination of valid and invalid requests to your app's endpoints. To pass the test, the app must respond to each request with an expected status code. The expected status code depends on the test and the endpoint.

If your app only has extensions that don't require signature verification, the testing feature and signature verification is disabled and running a test is not required. However, if your app has authentication enabled, the testing feature and signature verification is enabled by default.

## Disabling verification checks

While we consider it a best practice for all apps to leave signature verification checks enabled, you're allowed to disable them if your app uses public APIs, doesn't handle user data, and doesn't require authentication.

If signature verification checks are enabled, you can only [submit an app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/) after verifying its requests. If you disable signature verification checks, you can only [submit an app for review](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/submit-public-app/) after explaining why you're disabling the checks and providing the URL of the public API's documentation. This applies to both [public apps](https://www.canva.dev/docs/extensions/platform-concepts/apps/public-apps/) and [team apps](https://www.canva.dev/docs/extensions/platform-concepts/apps/team-apps/).

To disable signature verification checks:

  1. Navigate to the **Verification** page.
  2. Toggle the **Enable Signature Verification Checks** switch off.
  3. In the **Reason for disabling signature verification checks** field, explain why you're disabling signature verification checks.
  4. In the **Public API Documentation URL** field, enter the URL of the public API's documentation.



![](https://www.canva.dev/_next/static/media/img-ab8db1014f.4e615638.jpeg)

Apps that support [authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/) must leave the signature verification check enabled.

## Running the test

If you navigate to an app's **Submission** page, the signature verification test runs automatically.

To run the test manually:

  1. Navigate to an app via the Developer Portal.
  2. Click **Verification**.
  3. Click **Run signature verification test**.



You can re-run the test on-demand, but to prevent people from using Canva for a DoS attack, there's a limit of 100 requests per 24-hour period. If you exceed this limit, an error occurs. The more endpoints the app supports, the faster you'll reach the limit.

![](https://www.canva.dev/_next/static/media/img-75bb942438.4f9747e9.jpeg)

The timeout duration for the signature verification test is 5 seconds. If the app fails to respond to Canva's requests within 5 seconds, the test will fail.

## Understanding the results

After running the test, a table appears that contains a list of endpoints that the app might support. This list is based on the app's extensions.

![](https://www.canva.dev/_next/static/media/img-3a10c6b10a.2c03d6aa.jpeg)

### Supported tests

For each endpoint, Canva runs the following tests:

#### Invalid signature

Canva sends a request to the endpoint with an invalid request signature. This simulates what happens when someone other than Canva sends a request to the app.

#### Invalid timestamp

Canva sends two requests to the endpoint with invalid timestamps. One of these timestamps is too far in the future, while the other is too far in the past. This simulates what happens during a [replay attack⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Replay_attack).

#### Mixed valid/invalid signatures

Canva sends a request to the endpoint with a comma-separated list of request signatures, only one of which is valid. This simulates what happens when you [regenerate the app's client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/).

### Status codes

For each test result, Canva shows the following status codes:

  * **Expected** \- The status code that Canva expects to receive from the endpoint. In some cases, more than one status code is considered valid.
  * **Received** \- The status code that Canva received from the endpoint when running the test.



When the **Received** status code matches an **Expected** status code, the test passes. If the codes don't match, the test fails. This indicates an issue with how the endpoint is verifying requests.

The **Expected** status code will always be one of the following:

  * `200`
  * `404`
  * `401`



If the **Received** code doesn't match and you're not sure why, see [HTTP response status codes⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) for a complete list of possible status codes. The descriptions may help you identify the reason for the mismatch.

#### 404 status codes

For some tests, the `404` status code is valid. This is because some endpoints are sometimes optional. For example, a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) that uses the [Basic](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/) layout doesn't support the following endpoints:

  * [`/publish/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-find/)
  * [`/publish/resources/get`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-get/)



But these endpoints still appear in the signature verification test, regardless of how the extension is configured. Other endpoints are always optional, so a `404` status is always valid.
