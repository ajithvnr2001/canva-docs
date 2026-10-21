---
url: https://www.canva.dev/docs/extensions/backend-development/sdks/java/spark/
title: extensions-spark - SDKs - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:32.720805+00:00
---

# extensions-spark - SDKs - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/backend-development/sdks/java/spark/

SDKs

[Overview](https://www.canva.dev/docs/extensions/backend-development/sdks/)[Java SDKs](https://www.canva.dev/docs/extensions/backend-development/sdks/java/)[extensions-core](https://www.canva.dev/docs/extensions/backend-development/sdks/java/core/)[extensions-spark](https://www.canva.dev/docs/extensions/backend-development/sdks/java/spark/)

# extensions-spark

Java SDK for developing apps with the Spark framework.

Copy page

The `extensions-spark` module is one of Canva's [Java SDKs](https://www.canva.dev/docs/extensions/backend-development/sdks/java/) for developing server-side extensions. It streamlines the development process and helps you avoid common pitfalls, such as misspelled field names and signature verification issues. Additionally, it provides everything you need to integrate Canva Apps with the [Spark⁠(opens in a new tab or window)](http://sparkjava.com) framework.

This module contains:

  * Publish, Content and Configuration `Controller` classes which handle the correct API endpoints, validate requests, and [verify signatures](https://www.canva.dev/docs/extensions/backend-development/verify-request/verify-post-request-signature/).
  * Publish, Content and Configuration `Service` interfaces which you implement with your apps functionality.
  * Everything provided by the [`extensions-core`](https://www.canva.dev/docs/extensions/backend-development/sdks/java/core/) module.



## Usage

  1. Download the module via Maven Central: [search.maven.org/artifact/com.canva/extensions-spark⁠(opens in a new tab or window)](https://search.maven.org/artifact/com.canva/extensions-spark)
  2. Import the relevant components:


    
    
    // Controllers
    
    import com.canva.extensions.content.ContentApiController;
    
    import com.canva.extensions.publish.PublishApiController;
    
    import com.canva.extensions.configuration.ConfigurationApiController;
    
    
    
    
    // Services
    
    import com.canva.extensions.content.ContentApiService;
    
    import com.canva.extensions.publish.PublishApiService;
    
    import com.canva.extensions.configuration.ConfigurationApiService;
    
    
    
    
    // Models
    
    import com.canva.extensions.content.model.*;
    
    import com.canva.extensions.publish.model.*;

JAVA

Copy

### Services

You'll want to implement a service for each extension your app implements. The `ContentApiService` for [content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/), and the `PublishApiService` for [publish extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/), respectively.

Each service interface contains methods which are supported by the particular extension. For example, the `ContentApiService` exposes a `findResources` method, which corresponds to the [`content/resources/find`](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/) endpoint.

The `ConfigurationApiService` is recommended if your content or publish extension requires [authentication](https://www.canva.dev/docs/extensions/platform-concepts/authentication/).

In the example below, all that's required is to implement the `findResources` method, by handling the `FindResourcesRequest` and returning a `FindResourcesResponse`. See the [API specification](https://www.canva.dev/docs/extensions/server-api/post-content-resources-find/) for more details.
    
    
    import com.canva.extensions.content.ContentApiService;
    
    import com.canva.extensions.content.model.*;
    
    
    
    
    public class ContentApiServiceImpl implements ContentApiService {
    
    
    
    
        @Override
    
        public FindResourcesResponse findResources(FindResourcesRequest request) {
    
            throw new RuntimeException("Implement me :)");
    
        }
    
    }

JAVA

Copy

### Controllers

You'll want to register a controller for each extension your app implements. The `ContentApiController` for [content extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/), and the `PublishApiController` for [publish extensions](https://www.canva.dev/docs/extensions/extensions/content-extensions/), respectively.

The controllers handle:

  * Deserialization & serialization of request & responses.
  * Signature verification.
  * Request validation.
  * Mapping HTTP endpoints to Service methods - for example, a `POST` to `/content/resources/find` will invoke `ContentApiService#findResources`.



Each Controller exposes a `register` method, which must be invoked on initialization of the [Spark⁠(opens in a new tab or window)](http://sparkjava.com) application. This binds the Controllers to the supported HTTP paths and methods.

### Example: Using the `extensions-spark` module

This example demonstrates how to wire up the controllers and services for an app with a content and publish extension that requires authentication. You need to call this in your Spark application's equivalent of a `main` method.
    
    
    import com.canva.extensions.configuration.ConfigurationApiController;
    
    import com.canva.extensions.content.ContentApiController;
    
    import com.canva.extensions.publish.PublishApiController;
    
    import com.canva.extensions.util.Signer;
    
    import com.fasterxml.jackson.databind.ObjectMapper;
    
    
    
    
    import java.time.Clock;
    
    
    
    
    public class Example {
    
        public static void main(String[] args) {
    
            // Initialize your service implementation classes, with whatever dependencies they need. Left
    
            // empty here for illustratory purposes.
    
            final var contentService = new ContentApiServiceImpl();
    
            final var publishService = new PublishApiServiceImpl();
    
            final var configService = new ConfigurationServiceApiImpl();
    
    
    
    
            // The Signer (from extensions-core) implements the signature verifcation logic. It requires the
    
            // shared secret to be instantiated.
    
            final var signer = new Signer("canvaSecret");
    
            // A java.time.Clock instance, used to support signature verification.
    
            final var clock = Clock.systemUTC();
    
            // Used for serializing & deserializing request/response classes.
    
            final var mapper = new ObjectMapper();
    
    
    
    
            // Finally, register each controller.
    
            ContentApiController.register(contentService, signer, mapper, clock);
    
            PublishApiController.register(publishService, signer, mapper, clock);
    
            ConfigurationApiController.register(configService, signer, mapper, clock);
    
        }
    
    }

JAVA

Copy

Do not commit the secret to the `Signer` in plaintext. Instead, provide it through an environment variable, configuration file, etc.
