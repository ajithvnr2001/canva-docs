---
url: https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/decode-client-secret/
title: Decode a client secret - Signature verification - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:54.666580+00:00
---

# Decode a client secret - Signature verification - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/decode-client-secret/

Signature verification

[Overview](https://www.canva.dev/docs/extensions/backend-development/verify-request/)

Client secret

[Client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/)[Decode a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/decode-client-secret/)[Regenerate a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/)

Verify and test

[Verify POST request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/)[Verify GET request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/)[Verify timestamp](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/)[Test signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/)

# Decode a client secret

Learn how to convert a string into a byte array.

Copy page

To calculate a [request signature](https://www.canva.dev/docs/extensions/backend-development/verify-request/), an extension must decode the app's [client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/) into a byte array. This page demonstrates how to decode a client secret with a few different programming languages.

## Go
    
    
    package main
    
    
    
    
    import (
    
        b64 "encoding/base64"
    
        "fmt"
    
        "log"
    
    )
    
    
    
    
    func main() {
    
        secret := "CLIENT SECRET GOES HERE"
    
        key, error := := b64.StdEncoding.DecodeString(secret)
    
    
    
    
        if error != nil {
    
            log.Fatal(error)
    
        }
    
    
    
    
        fmt.Println(key)
    
    }

GO

Copy

## Java
    
    
    import java.util.Base64;
    
    
    
    
    public class Example {
    
        public static void main(String[] args) {
    
            String secret = "CLIENT SECRET GOES HERE";
    
            byte[] key = Base64.getDecoder().decode(secret);
    
            System.out.println(key);
    
        }
    
    }

JAVA

Copy

## JavaScript
    
    
    const secret = "CLIENT SECRET GOES HERE";
    
    const key = Buffer.from(secret, "base64");
    
    console.log(key);

JAVASCRIPT

Copy

## PHP
    
    
    $secret = "CLIENT SECRET GOES HERE";
    
    $key = base64_decode($secret);
    
    echo($key);

PHP

Copy

## Python
    
    
    import base64
    
    secret = "CLIENT SECRET GOES HERE"
    
    key = base64.b64decode(secret)
    
    print(key)

PYTHON

Copy

## Ruby
    
    
    require "base64"
    
    secret = "CLIENT SECRET GOES HERE"
    
    key = Base64.decode64(secret)
    
    puts key

RUBY

Copy

## TypeScript
    
    
    const secret = "CLIENT SECRET GOES HERE";
    
    const key = Buffer.from(secret, "base64");
    
    console.log(key);

JAVASCRIPT

Copy
