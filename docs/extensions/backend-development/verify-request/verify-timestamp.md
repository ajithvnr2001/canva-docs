---
url: https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/
title: Verify timestamp - Signature verification - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:55.227431+00:00
---

# Verify timestamp - Signature verification - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/

Signature verification

[Overview](https://www.canva.dev/docs/extensions/backend-development/verify-request/)

Client secret

[Client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/)[Decode a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/decode-client-secret/)[Regenerate a client secret](https://www.canva.dev/docs/extensions/backend-development/verify-request/client-secret/regenerate-client-secret/)

Verify and test

[Verify POST request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/)[Verify GET request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/)[Verify timestamp](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/)[Test signature verification](https://www.canva.dev/docs/extensions/backend-development/verify-request/test-signature-verification/)

# Verify timestamp

Code samples for verifying the timestamps of requests.

Copy page

When Canva sends an HTTP request to an app, it includes a UNIX timestamp (in seconds) of when the request was sent. To protect itself against [replay attacks⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Replay_attack), an app must:

  1. Compare the timestamp of when the request was sent with when it was received.
  2. Verify that the timestamps are within 5 minutes (300 seconds) of one another.



When the timestamps are _not_ within 5 minutes of one another, the app must reject the request by returning a `401` status code.

This page provides functions in a variety of programming languages to verify timestamps.

For step-by-step tutorials, refer to:

  * [Verify a `GET` request](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-get-request-signature/)
  * [Verify a `POST` request](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/)



## Examples

This section provides examples in the following languages:

  * [Go](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/#go)
  * [Java](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/#java)
  * [JavaScript](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/#javascript)
  * [PHP](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/#php)
  * [Python](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/#python)
  * [Ruby](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/#ruby)
  * [TypeScript](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/#typescript)



### Go
    
    
    package main
    
    
    
    
    import (
    
        "fmt"
    
        "math"
    
    )
    
    
    
    
    func IsValidTimestamp(sentAtSeconds int, receivedAtSeconds int, leniencyInSeconds int) bool {
    
        return int(math.Abs(float64(sentAtSeconds - receivedAtSeconds))) < leniencyInSeconds
    
    }
    
    
    
    
    func main() {
    
        // Valid timestamps
    
        fmt.Println(IsValidTimestamp(1590980773, 1590980773, 300)) // => true
    
        fmt.Println(IsValidTimestamp(1590980773, 1590980523, 300)) // => true
    
        fmt.Println(IsValidTimestamp(1590980773, 1590981023, 300)) // => true
    
    
    
    
        // Invalid timestamps
    
        fmt.Println(IsValidTimestamp(1590980773, 1590980273, 300)) // => false
    
        fmt.Println(IsValidTimestamp(1590980773, 1590981273, 300)) // => false
    
    }

GO

Copy

### Java
    
    
    public class Example {
    
        public static void main(String[] args) {
    
            // Valid timestamps
    
            System.out.println(isValidTimestamp(1590980773, 1590980773, 300)); // => true
    
            System.out.println(isValidTimestamp(1590980773, 1590980523, 300)); // => true
    
            System.out.println(isValidTimestamp(1590980773, 1590981023, 300)); // => true
    
    
    
    
            // Invalid timestamps
    
            System.out.println(isValidTimestamp(1590980773, 1590980273, 300)); // => false
    
            System.out.println(isValidTimestamp(1590980773, 1590981273, 300)); // => false
    
        }
    
    
    
    
        static Boolean isValidTimestamp(Integer sentAtSeconds, Integer receivedAtSeconds, Integer leniencyInSeconds) {
    
            return Math.abs(sentAtSeconds - receivedAtSeconds) < leniencyInSeconds;
    
        }
    
    }

JAVA

Copy

### JavaScript
    
    
    function isValidTimestamp(
    
      sentAtSeconds,
    
      receivedAtSeconds,
    
      leniencyInSeconds = 300
    
    ) {
    
      return Math.abs(sentAtSeconds - receivedAtSeconds) < leniencyInSeconds;
    
    }
    
    
    
    
    // Valid timestamps
    
    console.log(isValidTimestamp(1590980773, 1590980773)); // => true
    
    console.log(isValidTimestamp(1590980773, 1590981023)); // => true
    
    console.log(isValidTimestamp(1590980773, 1590980523)); // => true
    
    
    
    
    // Invalid timestamps
    
    console.log(isValidTimestamp(1590980773, 1590980273)); // => false
    
    console.log(isValidTimestamp(1590980773, 1590981273)); // => false

JAVASCRIPT

Copy

### PHP
    
    
    <?php
    
    
    
    
    function isValidTimestamp(int $sentAtSeconds, int $receivedAtSeconds, int $leniencyInSeconds = 300) {
    
        return abs($sentAtSeconds - $receivedAtSeconds) < $leniencyInSeconds;
    
    }
    
    
    
    
    // Valid timestamps
    
    var_dump(isValidTimestamp(1590980773, 1590980773)); // => bool(true)
    
    var_dump(isValidTimestamp(1590980773, 1590980523)); // => bool(true)
    
    var_dump(isValidTimestamp(1590980773, 1590981023)); // => bool(true)
    
    
    
    
    // Invalid timestamps
    
    var_dump(isValidTimestamp(1590980773, 1590980273)); // => bool(false)
    
    var_dump(isValidTimestamp(1590980773, 1590981273)); // => bool(false)
    
    
    
    
    ?>

PHP

Copy

### Python
    
    
    def is_valid_timestamp(sent_at_seconds, received_at_seconds, leniency_in_seconds = 300):
    
        return abs(sent_at_seconds - received_at_seconds) < leniency_in_seconds
    
    
    
    
    # Valid timestamps
    
    print(is_valid_timestamp(1590980773, 1590980773)) # => True
    
    print(is_valid_timestamp(1590980773, 1590980523)) # => True
    
    print(is_valid_timestamp(1590980773, 1590981023)) # => True
    
    
    
    
    # Invalid timestamps
    
    print(is_valid_timestamp(1590980773, 1590980273)) # => False
    
    print(is_valid_timestamp(1590980773, 1590981273)) # => False

PYTHON

Copy

### Ruby
    
    
    def is_valid_timestamp(sent_at_seconds, received_at_seconds, leniency_in_seconds = 300)
    
        (sent_at_seconds - received_at_seconds).abs < leniency_in_seconds
    
    end
    
    
    
    
    # Valid timestamps
    
    puts is_valid_timestamp(1590980773, 1590980773) # => true
    
    puts is_valid_timestamp(1590980773, 1590980523) # => true
    
    puts is_valid_timestamp(1590980773, 1590981023) # => true
    
    
    
    
    # Invalid timestamps
    
    puts is_valid_timestamp(1590980773, 1590980273) # => false
    
    puts is_valid_timestamp(1590980773, 1590981273) # => false

RUBY

Copy

### TypeScript
    
    
    function isValidTimestamp(
    
      sentAtSeconds: number,
    
      receivedAtSeconds: number,
    
      leniencyInSeconds: number = 300
    
    ): boolean {
    
      return Math.abs(sentAtSeconds - receivedAtSeconds) < leniencyInSeconds;
    
    }
    
    
    
    
    // Valid timestamps
    
    console.log(isValidTimestamp(1590980773, 1590980773)); // => true
    
    console.log(isValidTimestamp(1590980773, 1590981023)); // => true
    
    console.log(isValidTimestamp(1590980773, 1590980523)); // => true
    
    
    
    
    // Invalid timestamps
    
    console.log(isValidTimestamp(1590980773, 1590980273)); // => false
    
    console.log(isValidTimestamp(1590980773, 1590981273)); // => false

JAVASCRIPT

Copy
