---
url: https://www.canva.dev/docs/extensions/backend-development/sdks/java/core/
title: extensions-core - SDKs - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:32.855657+00:00
---

# extensions-core - SDKs - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/sdks/java/core/

SDKs

[Overview](https://www.canva.dev/docs/extensions/backend-development/sdks/)[Java SDKs](https://www.canva.dev/docs/extensions/backend-development/sdks/java/)[extensions-core](https://www.canva.dev/docs/extensions/backend-development/sdks/java/core/)[extensions-spark](https://www.canva.dev/docs/extensions/backend-development/sdks/java/spark/)

# extensions-core

A framework-agnostic SDK for developing apps with Java.

Copy page

The `extensions-core` module is one of Canva's [Java SDKs](https://www.canva.dev/docs/extensions/backend-development/sdks/java/) for developing server-side extensions. It streamlines the development process and helps you avoid common pitfalls, such as misspelled field names and signature verification issues.

This module contains:

  * A `Signer` utility for [generating request signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/).
  * Plain Old Java Objects (POJOs) with JSON marshalling for API requests, responses, and models.
  * Classes for implementing common functionality, such as request validation.



## Usage

  1. Download the module via Maven Central: [search.maven.org/artifact/com.canva/extensions-core⁠(opens in a new tab or window)](https://search.maven.org/artifact/com.canva/extensions-core)

  2. Import the relevant components:
         
         import com.canva.extensions.content.model.*;

JAVA

Copy




## Requests and responses

This snippet demonstrates how to serialize and deserialize the request and response objects for the [`/content/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/) endpoint:
    
    
    import com.canva.extensions.content.model.*;
    
    import com.fasterxml.jackson.databind.ObjectMapper;
    
    
    
    
    public class Example {
    
    
    
    
      private static final ObjectMapper objectMapper = new ObjectMapper();
    
    
    
    
      public static String handleFindResourcesRequest(String jsonBody) {
    
        // Deserialize a FindResourcesRequest from the JSON body of the HTTP request.
    
        var request = objectMapper.readValue(jsonBody, FindResourcesRequest.class);
    
    
    
    
        // Serialize the FindResourcesResponse.
    
        var resources = List.<Resource>of();
    
        var findResourcesResponse = new FindResourcesSuccessResponse(resources, null);
    
        return objectMapper.writeValueAsString(findResourcesResponse);
    
      }
    
    }

JAVA

Copy

## Models

This snippet demonstrates how to use a `Resource` object to create an `"IMAGE"` resource for a [content extension](https://www.canva.dev/docs/extensions/extensions/content-extensions/):
    
    
    import java.util.List;
    
    
    
    
    import com.canva.extensions.content.model.*;
    
    import com.fasterxml.jackson.databind.ObjectMapper;
    
    
    
    
    public class Example {
    
    
    
    
      private static final ObjectMapper objectMapper = new ObjectMapper();
    
    
    
    
      public static String handleFindResourcesRequest(String jsonBody) {
    
        // Deserialize a FindResourcesRequest from the JSON body of the HTTP request.
    
        var request = objectMapper.readValue(jsonBody, FindResourcesRequest.class);
    
    
    
    
        // Handle the request - return a list of Resource objects satisfying the request.
    
        var imageThumbnail = new Thumbnail("picsum.photos/id/237/200", 800, 600);
    
        var imageResource = new Resource("imageId", "An Image", ResourceType.IMAGE, "image/jpeg",
    
            imageThumbnail, "https://url.to/image.png");
    
        var resources = List.of(imageResource);
    
    
    
    
        // Serialize the FindResourcesResponse.
    
        var findResourcesResponse = new FindResourcesSuccessResponse(resources, "aContinuationToken");
    
        return objectMapper.writeValueAsString(findResourcesResponse);
    
      }
    
    }

JAVA

Copy

## Signature verification

If your app has [signature verification check](https://www.canva.dev/docs/extensions/backend-development/verify-request/) enabled, you must verify the [signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/) and [timestamps](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-timestamp/) of all HTTP requests. To simplify this process, the `extensions-core` module includes a `Signer` class for generating request signatures.

This snippet demonstrates how to use the `Signer` class with the [Spark](https://www.canva.dev/docs/extensions/backend-development/sdks/java/spark/) framework:
    
    
    import com.canva.extensions.util.Signer;
    
    import java.util.List;
    
    import static spark.Spark.post;
    
    
    
    
    public class Example {
    
    
    
    
        // Instantiated here for illustrative purposes. Ideally, provide via the constructor as a singleton.
    
        private static final Signer signer = new Signer("clientSecret");
    
    
    
    
        public static void main(String[] args) {
    
            post("/content/resources/find", (request, response) -> {
    
                var signatures = List.of(request.headers("X-Canva-Signatures").split(","));
    
                var sentAtSeconds = Long.parseLong(request.headers("X-Canva-Timestamp"));
    
                var path = "/content/resources/find";
    
                var signature = signer.signRequest(sentAtSeconds, path, request.body());
    
    
    
    
                if (!signatures.contains(signature)) {
    
                    response.status(401);
    
                    return response;
    
                }
    
                var receivedAtSeconds = System.currentTimeMillis() / 1000;
    
                var leniencyInSeconds = 5 * 60; // 5 minutes
    
                if (receivedAtSeconds - sentAtSeconds > leniencyInSeconds) {
    
                    response.status(401);
    
                    return response;
    
                }
    
                // If the above has passed, then the request is valid and can be handled safely.
    
                // Here we'd handle the findResources request and return a FindResources(Success|Error)Response.
    
                return response;
    
            });
    
        }
    
    }

JAVA

Copy
