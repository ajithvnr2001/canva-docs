---
url: https://www.canva.dev/blog/engineering/enabling-real-time-collaboration-with-rsocket/
title: Enabling real-time collaboration with RSocket - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:11.843728+00:00
---

# Enabling real-time collaboration with RSocket - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/enabling-real-time-collaboration-with-rsocket/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Gateway

# Enabling real-time collaboration with RSocket

This post describes how we empowered our users at Canva to collaborate by introducing services that support streaming using RSocket.

![](https://www.canva.dev/_next/static/media/thumbnail.5451a0a3.png)

* * *

  *   *   * 


[Sergey Tselovalnikov⁠(opens in a new tab or window)](https://twitter.com/SerCeMan), [Paul Tune⁠(opens in a new tab or window)](https://medium.com/@anamolous.behaviour), [Michael Belton⁠(opens in a new tab or window)](https://au.linkedin.com/in/michaelbelton)May 27, 2021

* * *

The majority of client-server interactions can be expressed with the request-response paradigm in many web applications, which maps pretty well to the HTTP protocol. However, in highly collaborative applications where users can interact, the request-response paradigm hits its limits. Users accustomed to real-time collaborative experiences expect to see each other's actions as soon as possible.

In the request-response world, clients typically initiate requests for data. However, in the real-time world, the backends need to push data to the clients before it's requested. Building such a system is difficult when the number of clients is large because every client must maintain an active connection to the backend service. The scaling and reliability considerations are significantly more complex than a request-response based system. Like the lights in a night city, the message flow never stops.

This post describes how we empowered our millions of users at Canva to collaborate at scale by introducing services that support bidirectional streaming using RSocket. We'll discuss the challenges we faced building these services and the solutions we used to meet the reliability requirements.

![](https://www.canva.dev/_next/static/media/img-1-tVtNzrtZ4Kv9GxJ-8h1YYQ.2ff3dbfa.jpeg)

Image by [Pexels⁠(opens in a new tab or window)](https://pixabay.com/users/pexels-2286921/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2178705) from [Pixabay⁠(opens in a new tab or window)](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=2178705)

## Real-time interactions

At Canva, we want to enable our users to interact with each other in real-time. However, "real-time" means different things in different contexts. Let's define what exactly we mean when we say "real-time" throughout this post.

![](https://www.canva.dev/_next/static/media/img-1-iV6GYs0-L56UJRLBIHARqA.5451a0a3.png)

In the figure above, you can see Alice and Bob. They're editing the same design in Canva together, at the same time. Alice wants to make a simple change by adding an exclamation mark to one of the headings. We want Bob to see the change as soon as possible without explicitly requesting the change to avoid any potential conflicts.

Here, real-time really means _soft real-time_. The longer the users have to wait to see changes in the design, the less useful the whole system is. The sooner we let Bob know that Alice has updated the design, the lower the chance of a conflict, which translates to a better overall user experience.

Moreover, collaborative editing by itself is non-trivial, and it's just one of many examples of a service that needs to provide an API that allows for pushing data onto the clients without explicitly requesting this data. Live presentations (also a [Canva feature](https://www.canva.dev/blog/engineering/lessons-learnt-from-building-reactive-microservices-for-canva-live/)), where the presenter's screen needs to reflect user actions as soon as possible, is another example.

Designing such systems requires a large number of considerations. Many of the issues are very similar to the request-response and streaming applications. However, despite the similarities, several differences posed a problem.

![](https://www.canva.dev/_next/static/media/img-1-LvIaOYpSogBODIqx7AaXMQ.3065c311.png)

The challenging differences are highlighted in bold

Our team had to come up with different solutions to each of those challenges. As challenges are always the most exciting part of any story, let's take a look at each of them, starting from the application.

## Application

The heart of any application is the protocol. The protocol specifies the interactions between the users and the application, and it defines many of its properties.

## Transport Protocol

There are many ways to implement the capability of pushing updates from the backends onto the client in real-time. The primary protocol candidates are long polling, server-side events (SSE), and WebSockets.

[Long polling⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Comet_\(programming\)#Ajax_with_long_polling) is a well-known classic technique, though it's no longer as popular as it once was. One of the major downsides of using long polling is its latency, as it requires sending a new request each time a response is received. Additionally, long polling presents numerous questions around the state and concurrency, and requires layering another protocol on top of it to support bi-directional communications.

[SSE⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events), while a viable option and can be implemented efficiently over HTTP/2, is also a unidirectional protocol. We'd still need to build another protocol on top of it to make it bi-directional.

WebSockets are an ideal bi-directional transport for our use case. They provide an abstraction that is similar to standard sockets — _bytes in, bytes out_. Additionally, all modern and older browsers and application servers support WebSockets.

The advantage of WebSockets is that it's relatively easy to implement the message passing for a single service. Just take JSON payloads, encode them as bytes, pack them into WebSocket frames, and send them to the server over the wire. However, many services need to provide a real-time API, so adding a WebSocket connection for each service significantly increases the load on the servers. Adding a new WebSocket connection every time a new backend starts supporting streaming APIs presents a significant challenge at Canva's scale.

There needs to be another protocol on top of WebSocket to mitigate this concern and ensure we can add more APIs easily. The protocol needs to support the multiplexing of message channels to different backends within a single connection.

Thus, the most straightforward way to implement this is to build a WebSocket Gateway. The WebSocket Gateway accepts connections from the users and forwards the related messages to the appropriate backends. Since it's also a gateway, the WebSocket Gateway handles all of the infrastructure functions that a normal API gateway would, such as authentication, authorization, tracings, and many others.

## Application Protocol

Multiplexing (and demultiplexing) is the most important role of the WebSocket Gateway as it accepts the connections from the users, reads the incoming messages, and forwards them into channels connected to different backends like in the figure below. The red messages flow to the editing backend, while green messages flow to the presentations backend even though the client sends all messages into the same connection.

![](https://www.canva.dev/_next/static/media/img-0-wlc4qxmLjHmUutDC.83b26d3e.png)

WebSocket is only a transport protocol, not an application one. It's impossible to transparently pack messages that belong to different services and unpack them on the WebSocket Gateway using only WebSockets. There needs to be an application protocol to solve the multiplexing challenge, and we chose [RSocket⁠(opens in a new tab or window)](https://rsocket.io/).

RSocket allows for multiple channels to be created within a single connection, and it manages their lifecycle. Within each channel, both sides can send messages across it. At the end of its lifecycle, the channel either completes successfully or with an error.

![](https://www.canva.dev/_next/static/media/img-0-RBL2PJqTVNcuOUd-.e8ebabff.png)

The best way to thoroughly understand how RSocket manages channels is to read the [protocol definition⁠(opens in a new tab or window)](https://github.com/rsocket/rsocket/blob/master/Protocol.md). The protocol defines a set of frames, and for each frame, its byte-by-byte layout on the wire. This makes RSocket essentially transport protocol agnostic. It can work on top of TCP or WebSockets as long as the transport protocol satisfies a set of ordering properties. Each frame has an ID of the stream it belongs to, its type, and a payload. The payload contains the data and metadata for the frame. For example, the layout of the payload frame used to send the _next message_ in a stream is shown below.

![](https://www.canva.dev/_next/static/media/img-1-F0BywvSTT-rKM5yFJb2f7g.396ec2f6.png)

[Payload ⁠(opens in a new tab or window)](https://github.com/rsocket/rsocket/blob/master/Protocol.md#payload-frame-0x0a) frame definition

The most significant difference between RSocket and other protocols is that with RSocket, each channel is equipped with independent backpressure based on reactive streams semantics. The [Reactive Streams⁠(opens in a new tab or window)](https://www.reactive-streams.org/) initiative defines how stream processing can be implemented across multiple runtimes, including Java and JavaScript. The key part of the initiative is the definition of flow control on a per-stream level.

The main idea of the flow control can be described as _the server has to continue requesting messages for the clients to continue producing them_.

So what does this property give us exactly? Consider a simple stream implementation with no backpressure at all in the figures above. Most of the time, it's going to work as expected — red messages flow to the editing service and the green to the presentation service.

Outages are, unfortunately, inevitable. It's only a question of when, not if, an outage occurs. In the figure below, without backpressure, even though the Editing service can't accept more messages, the clients do not know this and won't stop producing messages. The constant stream of messages results in a backlog. This might bring down the whole system due to the unavailability of a single service, which puts us in dire straits.

![](https://www.canva.dev/_next/static/media/img-1-Iz0XnI4fDH7au57VklAnwg.5480b0c8.png)

The only viable mitigation strategy is minimizing the blast radius, which is almost impossible without backpressure. Backpressure provides a comprehensive mitigation strategy here. If one of the services becomes unavailable, it stops requesting messages, and the clients stop producing them. The messages from the other backends are not affected, so they continue flowing through the gateway. Though one backend is down, the rest of the system functions as expected even though there are many shared resources.

![](https://www.canva.dev/_next/static/media/img-1-KA-5poIwBFf3dE76TZFQ9w.01139ee5.png)

Compared to standard techniques, like circuit breaking, there is no need to enter an error state or reach a certain error threshold before the mitigation strategies kick in. If one of the services is down, it'll stop requesting messages. If there is no demand, there is no supply — it's that simple.

While the general approach for any technology might look reasonable, its applicability is often defined by the technology's ecosystem, particularly the set of libraries that implement it in each platform.

## Backend APIs

All of our backends run on the JVM at Canva. In the JVM ecosystem, the RSocket protocol is implemented by the [RSocket-Java⁠(opens in a new tab or window)](https://github.com/rsocket/rsocket-java) library. You can try it out quickly yourself. The library is very easy to start playing with.

To use RSocket-Java, you only need to implement the business logic in the acceptor. The acceptor describes how to handle incoming requests. However, to implement the acceptor, there needs to be a way to handle the incoming streams and create the outgoing streams. RSocket-Java doesn't implement the reactive streams themselves; it uses [Project Reactor⁠(opens in a new tab or window)](https://projectreactor.io/). The library offers many operators that are necessary for writing business logic based on reactive streams. The second piece of the puzzle is transport, which describes how the rsocket frames are sent and received on the wire. RSocket-Java comes with several transport implementations built on top of [Netty⁠(opens in a new tab or window)](https://netty.io/).

Here's an example of a simple RSocket echo server built with RSocket-Java:
    
    
    public static void main(String[] args) {
    
      var server = RSocketServer.create(
    
        SocketAcceptor.forRequestChannel(s -> Flux.from(s))) // acceptor
    
        .bind(WebsocketServerTransport.create(8080)) // transport
    
        .block();
    
      System.out.println("started on " + server.address());
    
      server.onClose().block();
    
    }

JAVA

Copy

In the example above, we started a WebSocket server built on top of Netty. However, if you're already using some other network library and have built a solid reliability and observability setup, you don't have to abandon it. Instead, you can implement your own transport on top of an existing server by implementing just a few classes. The implementation comes down to implementing two methods: _sending_ and _receiving._ That is, how you send the bytes and how you receive them.

## Frontend APIs

Reactive programming has already become one of the main tools for building user interfaces on the frontend side. Many frontend engineers are already familiar with [RxJS⁠(opens in a new tab or window)](https://github.com/ReactiveX/rxjs) — an amazing library that provides reactive extensions for JavaScript. RxJS comes with a standard set of classes: _Subject_ , _Observable_ , _Subscription_ , etc. However, experienced backend engineers are often surprised to learn that RxJS _does not support backpressure_.

Upon closer inspection, the decision of the RxJS engineers makes logical sense. When the user is the source of events, it's not easy to apply backpressure as implementing support for backpressure is non-trivial. You can find a lengthy and insightful discussion about the pros and cons of RxJS backpressure support in [RxJS#71⁠(opens in a new tab or window)](https://github.com/ReactiveX/rxjs/issues/71).

So instead, the RSocket implementation in JavaScript, [RSocket-JS⁠(opens in a new tab or window)](https://github.com/rsocket/rsocket-js), comes with its own set of classes that support backpressure. For example, [Flowable⁠(opens in a new tab or window)](https://github.com/rsocket/rsocket-js/blob/master/packages/rsocket-flowable/src/Flowable.js). At Canva, we use RxJS to keep RSocket-JS compatible with the rest of the JS ecosystem. We convert any _Flowable_ with backpressure into an _Observable_ that doesn't support backpressure. This is exactly where you'd want to define your backpressure strategy: how your application will behave when the server is overloaded and cannot accept more messages.

One of the advantages of RSocket is that backpressure can be defined for a single channel rather than the whole connection. While it makes sense to buffer messages for some services, completely dropping them can be acceptable for others. For example, an analytics service could buffer messages for some time and then start dropping them because it does not affect the user experience. In contrast, it makes sense to fail as fast as possible for other critical services to ensure that user actions are not lost.

### Reconnection

Backpressure avoids major outages when one backend is not available. However, a single instance of the WebSocket Gateway might become unavailable as well. An instance can be killed, restarted, or might lose network connection. In the cloud era, any of these situations can happen at any time. A server can simply disappear into the void. In this unfortunate situation, the clients will need to reconnect.

However, if it wasn't a single server but a significant portion of the fleet experiencing issues, constantly reconnecting clients might exacerbate the outage. So instead, the clients can reconnect with an exponential backoff strategy, say, after a second, then two seconds, then four, and so on.

Finally, when the WebSocket Gateway servers are up and running after an outage, the reconnecting clients might still cause damage by all trying to connect simultaneously. To avoid this issue, the exponential backoff sequence should also incorporate jitter. Jitter adds slight randomness to the retry times. For example, some client can try to connect after 1 second while others after 3. The added jitter of when to reconnect helps to spread the reconnection load more evenly and avoid synchronized waves of users trying to reconnect simultaneously.

## Infrastructure

So far, we've discussed how we approached the application concerns. Now, let's dive into the infrastructure concerns.

## Observability

Every journey to production starts with observability. It's crucial to be able to look under the hood of a running application to prevent any possible incidents and mitigate any potential issues. The observability of streaming real-time applications is more complicated than the observability of conventional request-response applications. With request-response, a request is a unit of operation, while for streaming APIs, it's a channel with a much larger number of possible states.

One of the first graphs that come to mind when engineers talk about the health of a service is the error rate graph. With request-response applications, it's straightforward to plot: it's the number of failed requests divided by the total number of requests in a period of time. However, for streaming applications, the error rate definition is not as straightforward as the number of possible states is much larger. For example, a stream might produce a large number of _NEXT_ frames before completing with either _ERROR_ or _COMPLETE_ , as shown below.

![](https://www.canva.dev/_next/static/media/img-1-iVBrh997jtgXGgpyc0s6pg.2e9b22a4.png)

Stream lifecycle

There is still much more to it. The clients can also unsubscribe, which adds an additional level of monitoring complexity. What's more, there are two streams — a stream with incoming messages and a stream with outgoing messages. Both streams need to be accounted for. Given the number of possible states, having a single source of truth, one graph, defining the health of the service can be challenging. One possible approximation is the number of _ERROR_ frames divided by the total number of frames excluding _KEEP_ALIVE_ frames to increase the signal-to-noise ratio.

This can be expressed as:
    
    
    rate(ERROR)/rate(ALL - KEEP_ALIVE)

Copy

The above metrics are based on the transport data. RSocket provides a way to instrument the transport layer providing visibility into the underlying connection and all frames flowing through it.
    
    
    .interceptors(registry -> {
    
      // transport interceptor
    
      registry.forConnection(new RSocketConnectionInterceptor());
    
    })

JS

Copy

However, more metrics are important for getting full visibility of the application. For example, how long does it take for the server to respond to channel requests, or what is the lifetime of the channels? These metrics can be received by instrumenting the RSocket responder itself.
    
    
    .interceptors(registry -> {
    
      // transport interceptor
    
      registry.forConnection(new RSocketConnectionInterceptor());
    
      // acceptor interceptor
    
      registry.forResponder(new RSocketResponderInterceptor());
    
    })

JS

Copy

RSocket-Java already provides an instrumentation based on [micrometer⁠(opens in a new tab or window)](https://github.com/rsocket/rsocket-java/tree/master/rsocket-micrometer/src/main/java/io/rsocket/micrometer). However, you can implement interceptors for any other libraries with minimal effort.

## Logs

When performing any logging, it's important to remember that the lifecycle of a single channel doesn't match the lifecycle of a single thread most of the time. The standard Java usage of MDC (Mapped Diagnostic Context containing the request-id) is not applicable. At the same time, collecting logs for essential channel events is crucial for debugging, as a single channel can stay alive for hours. MDC can be propagated manually if the streaming scope is well defined, or alternatively, Project Reactor [provides a pattern⁠(opens in a new tab or window)](https://projectreactor.io/docs/core/release/reference/#faq.mdc) to establish MDC in a streaming application.

## Autoscaling

Autoscaling of streaming applications needs to be designed with a set of constraints in mind. While request-response applications are typically constrained by CPU only, streaming applications might also have other limitations that you need to consider. These limits are often missed when doing load testing.

Often, load tests emulate situations in which the number of messages per connection is large, and messages themselves are of significant size. Yet, for many applications, the connections are often idle, and the rate of messages is relatively low. At the same time, every connection requires some amount of memory. To account for this, you can base the primary autoscaling policy on the number of open connections and the secondary policy on the CPU.

## Load Balancing

Another crucial part of any reliable infrastructure is load balancing. The diagram below represents a single instance of a WebSocket Gateway on a high level.

![](https://www.canva.dev/_next/static/media/img-1-N01sPbGsmvida0McXblSYw.7ddea56a.png)

In the diagram, there are two types of connections: type 1 and type 2. Type 1 connections are the users that are connecting to the gateway. Every connection represents a user identity represented by the initial HTTP request. It has associated cookies, headers, etc. There are as many connections as there are users.

However, the number of type 2 connections can be very low. It's possible to create a large number of channels across a single connection with RSocket, so even a single type 2 connection is enough.

This is another essential role that WebSocket is performing. It takes the responsibility of handling a large number of connections as it's a non-trivial task. For example, handling many connections requires a lot of memory. The maximum number of open files needs to be sufficiently large, and the server needs to be configured accordingly.

Load balancing the type 1 connections is easy. At Canva, we rely on AWS Application load balancers. Every time a new user comes, the load balancer selects an instance of the WebSocket Gateway and proxies the new connection to it.

On the other hand, load balancing the channel requests within type 2 connections is more challenging. The challenge is that conventional load balancers are _not suitable for load balancing a streaming connection because they're unaware of the application protocol_.

The number of type 2 connections is small. In the case of a load balancer, WebSocket Gateway won't even know that a new backend service started because it doesn't need to establish new connections. As a result, it won't send any traffic to the newly scaled-up instances hidden behind a load balancer. The only way to resolve this problem is to make the WebSocket Gateway aware of the instances themselves and connect to the downstream backend services directly. Then it can load balance channels rather than connections. To do so, it needs to know the IP addresses of the downstream services.

### Service Registry

A service registry is required to make direct connections possible. When a new backend starts up, it immediately registers itself in the service registry, and every WebSocket Gateway instance listens to the updates and can connect to the new backend.

![](https://www.canva.dev/_next/static/media/img-1-VoztKPOWuj9IAmveNNkxPA.8026818c.png)

Service Registry

It's important to note that the round-robin algorithm is not the optimal load balancing strategy for long-lived connections. For example, imagine a situation where a gateway connects to two backends, and it opens 50,000 channels to each one.

![](https://www.canva.dev/_next/static/media/img-1-rKUPPSjbXgaq55cZ4u3_BQ.4f27e978.png)

After noticing that the first two instances are becoming overloaded, autoscaling adds a new service into the fleet. Because the channels are long-lived, the round-robin algorithm would continue opening new channels to all registered backends regardless of their age, even the old ones that are already getting overloaded, putting even more load onto them. Instead, using the least loaded algorithm is more suitable for the scenarios where the services mostly handle long-lived channels.

## Deployments

What is redeployment? In essence, redeployment is about replacing the entire fleet of instances running the old version of the application with instances running the new version. Doing this simultaneously can result in a huge spike in latency and errors like in the graph below.

![](https://www.canva.dev/_next/static/media/img-0-Mv9TpKp5Zzzofba-.36e41d67.png)

It is still important to handle the load spike from all of the clients trying to connect at the same time. One day all of the gateway instances can become unavailable, for example, due to a major cloud provider outage. In this case, the latency spikes might be acceptable. Yet during usual redeployments, you should avoid any latency spikes.

The standard way to handle redeployments with the load balancers is to use [_deregistration delay_ ⁠(opens in a new tab or window)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#deregistration-delay). Once the new fleet of instances is attached to the load balancer, it doesn't remove (deregister) the old fleet immediately. Instead, it keeps the connections open but doesn't send the new requests there, allowing the existing requests to complete gracefully during the delay. This approach works great for conventional request-response applications.

However, the default deregistration delay doesn't work well for streaming services because the connections are long-lived so it takes a long time for them to go away naturally. Even though the new requests result in establishing connections to the new fleet of instances, old connections are not going anywhere. They're long-lived, and we want them to be long-lived.

Instead, the application itself needs to gradually close the connections when it is being deregistered. One possible solution is to use a deregistration event that can be subscribed to with AWS Event Bridge. With the appropriate setup, the event can be routed to a lambda function or any other piece of software that can inspect it and understand which instances are about to be deregistered. Then, it can notify the application, which can start closing the connections gradually, forcing the clients to reconnect.

![](https://www.canva.dev/_next/static/media/img-0--8Vw5jZoiaKJjHc6.2bcd2b63.png)

That way, new versions of WebSocket Gateways can get successfully released, and engineers enjoy beautiful graphs where the connections are shifted gradually between different versions of the application.

![](https://www.canva.dev/_next/static/media/img-1-A0Nl4i5P6LIZQoBvw2AJxg.752a2dae.png)

## Conclusion

Real-time streaming services have many application and infrastructure features drastically different from the services written in the request-response paradigm. Every difference comes with its own complexity, and much of the complexity stems from the streaming domain.

Building such services is not an easy task. However, the benefits are immense as it significantly improves the user experience. Fortunately, as we've shown, an amazing set of protocols and libraries provide a great model for managing the complexity.

We hope that the lessons we learned while implementing these services at Canva provide value when implementing your own streaming services.

_If you're as passionate about building reliable production systems as we are, check out our open positions in the_ [_Core Platform and Libraries team_ ⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/).

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.7a551639.png)](https://www.canva.dev/blog/engineering/service-aligned-data-platform-architecture/)

[Data PlatformService-aligned Data Platform ArchitectureHow the data analytics platform team scaled data ingestion from various services at Canva.](https://www.canva.dev/blog/engineering/service-aligned-data-platform-architecture/)

[Jaskirat Grover⁠(opens in a new tab or window)](https://www.linkedin.com/in/jaskiratgrover/), [Justin Ty⁠(opens in a new tab or window)](https://www.linkedin.com/in/justinty/)Jun 9, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.c69dca35.png)](https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/)

[Data AnalyticsMeasuring Commercial Impact at Scale at CanvaHow We Built Canva's IMPACT App with Streamlit in Snowflake](https://www.canva.dev/blog/engineering/measuring-commerical-impact-at-scale/)

[Jun Ye⁠(opens in a new tab or window)](https://www.linkedin.com/in/jun-ye-0798/)Jun 20, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.eeec7a21.png)](https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/)

[Quality AssuranceHow We Used Data to Optimize Our Quality Assistance ModelFrom firefighting chaos to problem solving zen.](https://www.canva.dev/blog/engineering/how-we-used-data-to-optimize-our-quality-assistance-model/)

[Zi Yang Pang⁠(opens in a new tab or window)](https://www.linkedin.com/in/pangzy/)Aug 29, 2022

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


