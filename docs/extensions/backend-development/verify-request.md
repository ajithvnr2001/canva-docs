---
url: https://www.canva.dev/docs/extensions/backend-development/verify-request/
title: Signature verification - Signature verification - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:23.239329+00:00
---

# Signature verification - Signature verification - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/verify-request/

Signature verification

[Overview](https://www.canva.dev/docs/extensions/backend-development/verify-request/)

Client secret

[Client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/)[Decode a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/decode-client-secret/)[Regenerate a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/)

Verify and test

[Verify POST request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/)[Verify GET request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/)[Verify timestamp](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/)[Test signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/)

# Signature verification

What is signature verification? Why verify request signatures?

Copy page

If your app has extensions that receive HTTP requests, it is recommended that you verify that any requests it receives are actually arriving from Canva (and not from some nefarious third-party). This protects your app and our users from a variety of attacks.

## What requests need to be verified?

Once you enable signature verification checks, all HTTP requests that Canva sends to an app must be verified. This includes `POST` requests, such as requests sent to the `/content/resources/find` endpoint, and `GET` requests, such as the request sent to the app's **Redirect URL**.

If an app supports authentication, it must also verify the authenticity of the authentication flow. This is a little different from verifying requests. To learn more, see [Authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).

## How Canva confirms that requests are verified

The signature verification test is available via the Developer Portal. The test sends a combination of valid and invalid requests to the app. The app must accept the valid requests and reject the invalid requests.

To learn more, see [Signature verification test](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/).

## How to verify a request

The steps for verifying a request depend on whether it's a `GET` or `POST` request. To learn more, see the following guides:

  * [Verify a `GET` request](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/)
  * [Verify a `POST` request](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/)



## Example

This example demonstrates how to verify `POST` and `GET` requests in Express.js.
    
    
    const { createHmac } = require("crypto");
    
    const express = require("express");
    
    
    
    
    const app = express();
    
    
    
    
    app.use(
    
      express.json({
    
        verify: (request, response, buffer) => {
    
          request.rawBody = buffer.toString();
    
        },
    
      })
    
    );
    
    
    
    
    app.post("/content/resources/find", async (request, response) => {
    
      if (!isValidPostRequest(process.env.CLIENT_SECRET, request)) {
    
        response.sendStatus(401);
    
        return;
    
      }
    
    
    
    
      response.send({
    
        type: "SUCCESS",
    
        resources: [],
    
      });
    
    });
    
    
    
    
    app.get("/my-redirect-url", async (request, response) => {
    
      if (!isValidGetRequest(process.env.CLIENT_SECRET, request)) {
    
        response.sendStatus(401);
    
        return;
    
      }
    
    
    
    
      response.sendStatus(200);
    
    });
    
    
    
    
    const isValidPostRequest = (secret, request) => {
    
      // Verify the timestamp
    
      const sentAtSeconds = request.header("X-Canva-Timestamp");
    
      const receivedAtSeconds = new Date().getTime() / 1000;
    
    
    
    
      if (!isValidTimestamp(sentAtSeconds, receivedAtSeconds)) {
    
        return false;
    
      }
    
    
    
    
      // Construct the message
    
      const version = "v1";
    
      const timestamp = request.header("X-Canva-Timestamp");
    
      const path = getPathForSignatureVerification(request.path);
    
      const body = request.rawBody;
    
      const message = `${version}:${timestamp}:${path}:${body}`;
    
    
    
    
      // Calculate a signature
    
      const signature = calculateSignature(secret, message);
    
    
    
    
      // Reject requests with invalid signatures
    
      if (!request.header("X-Canva-Signatures").includes(signature)) {
    
        return false;
    
      }
    
    
    
    
      return true;
    
    };
    
    
    
    
    const isValidGetRequest = (secret, request) => {
    
      // Verify the timestamp
    
      const sentAtSeconds = request.query.time;
    
      const receivedAtSeconds = new Date().getTime() / 1000;
    
    
    
    
      if (!isValidTimestamp(sentAtSeconds, receivedAtSeconds)) {
    
        return false;
    
      }
    
    
    
    
      // Construct the message
    
      const version = "v1";
    
      const { time, user, brand, extensions, state } = request.query;
    
      const message = `${version}:${time}:${user}:${brand}:${extensions}:${state}`;
    
    
    
    
      // Calculate a signature
    
      const signature = calculateSignature(secret, message);
    
    
    
    
      // Reject requests with invalid signatures
    
      if (!request.query.signatures.includes(signature)) {
    
        return false;
    
      }
    
    
    
    
      return true;
    
    };
    
    
    
    
    const isValidTimestamp = (
    
      sentAtSeconds,
    
      receivedAtSeconds,
    
      leniencyInSeconds = 300
    
    ) => {
    
      return (
    
        Math.abs(Number(sentAtSeconds) - Number(receivedAtSeconds)) <
    
        Number(leniencyInSeconds)
    
      );
    
    };
    
    
    
    
    const getPathForSignatureVerification = (input) => {
    
      const paths = [
    
        "/configuration",
    
        "/configuration/delete",
    
        "/content/resources/find",
    
        "/publish/resources/find",
    
        "/publish/resources/get",
    
        "/publish/resources/upload",
    
      ];
    
    
    
    
      return paths.find((path) => input.endsWith(path));
    
    };
    
    
    
    
    const calculateSignature = (secret, message) => {
    
      // Decode the client secret
    
      const key = Buffer.from(secret, "base64");
    
    
    
    
      // Calculate the signature
    
      return createHmac("sha256", key).update(message).digest("hex");
    
    };
    
    
    
    
    app.listen(process.env.PORT || 3000);

JAVASCRIPT

Copy
