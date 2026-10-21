---
url: https://www.canva.dev/blog/engineering/functional-completeness-and-local-hermeticity/
title: Functional completeness and local hermeticity - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:13.528197+00:00
---

# Functional completeness and local hermeticity - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/functional-completeness-and-local-hermeticity/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

DevOps

# Functional completeness and local hermeticity

Maintaining a functionally complete yet airtight local development environment is something we consider to be of critical importance.

![](https://www.canva.dev/_next/static/media/thumbnail.a4baa635.png)

* * *

  * 


David HearndenMar 25, 2015

* * *

 _Originally published by David Hearnden at_ [product.canva.com⁠(opens in a new tab or window)](https://product.canva.com/hermeticity/) _on March 25, 2015._

Today, I'm testing new features of Canva's dynamic flag system. Next to me, a fellow engineer is working on the pipeline that updates design images in response to design edits. These are separate features, and both have broad reach through components that make up Canva. As we iterate, each of us is running an isolated, functionally-complete Canva universe, of between 16 and 32 separate components (depending on how you count). We can exercise Canva's full suite of features: creating and publishing designs, searching images, purchasing and downloading prints, browsing the social graph, interacting with designs in the stream, and so on. We're not doing this using a vast network of distributed machines; we're doing this entirely within the confines of our laptops, without even needing network.

Canva's production environment is quite different. It is distributed, and depends on a long list of services, including AWS (S3, CloudFront, ELB, SQS, SNS, SES, SWF), ZooKeeper, Cassandra, MongoDB, MySQL, Solr, and Redis. While many of these services can be deployed on a developer's workstation (what we call a "local") environment, many cannot, particularly those from AWS.

Maintaining a functionally complete yet airtight local development environment is something we consider to be of critical importance to our engineering health, since it directly impacts the ease and speed of developing new features as well as diagnosing problems.

_Functional completeness_ means that anything that can be done on [www.canva.com⁠(opens in a new tab or window)](https://www.canva.com/) can be done in this local environment.

_Local hermeticity_ means that the scope of dependencies and side-effects does not extend beyond a single machine. This post describes, with practical examples, how we achieve functional completeness and local hermeticity in our development environments in a way that is transparent to application logic.

## Configuration Flavors

We maintain a handful of environment configurations that we call flavors, including `local` for local development, and `prod` for production. A flavor name is passed to a component at runtime, either as an environment variable or command argument, and our application launchers use that name for dynamic selection of flavor-specific configuration resources, using filename conventions. For example, flavor-specific property configurations are defined in files named `<component>.<flavor>.properties`. Flavor names never appear as literals in code. This keeps the set of environments open, and we can introduce ad-hoc flavors, such as `loadtest` and `unittest`, without code changes, simply by dropping in suites of suitably-named configuration resources for the relevant components.

As a concrete example, we allocate worker threads in our import server with an `import.worker.threads` property.
    
    
    @Named
    
    public final class ImportServer implements ImportService {
    
      @Inject
    
      public ImportServer(@Value("${import.worker.threads}") int workerThreads, ...) {
    
        ...
    
      }
    
    }

JAVA

Copy

The environment-specific value of this property is controlled by the following properties files:

`import.local.properties`:
    
    
    import.worker.threads=2

PROPERTIES

Copy

`import.prod.properties`:
    
    
    import.worker.threads=16

PROPERTIES

Copy

Nothing sophisticated is happening here — controlling configuration in properties is pretty standard practice — but it is the mechanism on which we build hermeticity that is transparent to application logic.

Most of the services we rely on are popular open-source tools, and functional instances can be installed locally with `apt-get` or `brew`. Usually, some minor additional configuration is required to lower resource consumption, allowing several such services to co-exist happily on a single machine. Completeness and hermeticity for these services is then a simple matter of using flavor-specific configuration to control addressing. For example, we configure ZooKeeper hosts as follows:

`zk.local.properties`:
    
    
    zk.host=localhost:2181
    
    ...

PROPERTIES

Copy

`zk.staging.properties`:
    
    
    zk.host=10.0.32.55,10.0.33.55:2181
    
    ...

PROPERTIES

Copy

`zk.prod.properties`:
    
    
    zk.host=10.0.32.4,10.0.33.4,10.0.34.4,10.0.35.4:2181
    
    ...

PROPERTIES

Copy

## Dependency injection with fakes

For the remaining services that are not locally deployable, particularly services from AWS, we achieve functional completeness using abstracted interfaces and dependency-injected [fakes⁠(opens in a new tab or window)](http://martinfowler.com/articles/mocksArentStubs.html).

Our application code never refers to AWS services directly, but instead references our own minimal interfaces that define only the parts and modes those services that are required. For each of these interfaces, we've written multiple implementations, including one that is a simple pass-through to the AWS SDK, and another that uses an implementation strategy suitable for local, hermetic development. The abstract interfaces for those services, which we end up re-using across many of our components, only include the subset of AWS functionality that we use, keeping the fake implementations simple. The implementation to use in a given environment is named using a flavor-specific property, and bound at runtime using dependency injection.

For example, the Canva component that imports images requires a message-queue service (`QueueClient`) and a file storage service (`BlobStore`). In our staging and production environments, we bind those interfaces to implementations that forward to S3 and SQS, but in our local development and CI environments, we bind them to implementations that work locally. The local implementations are discussed further in the next section.

![](https://www.canva.dev/_next/static/media/img-0-YeX7uoUBlU8gueQz.a4baa635.png)

`aws.local.properties`:
    
    
    blobstore.impl=FileBlobStore
    
    queue.impl=FileQueueClient
    
    ...

PROPERTIES

Copy

`aws.prod.properties`:
    
    
    blobstore.impl=SQSBlobStore
    
    queue.impl=SQSQueueClient
    
    ...

PROPERTIES

Copy

Using implementations of an essential service that differ between local development and production is a risk, since it results in code that rarely gets exercised outside production, but is mitigated by specifically modelling the intermediate interfaces such that the binding to AWS is as trivial as possible. Nevertheless, all complex services have quirks lurking somewhere, and when they are discovered, we replicate those quirks in the local implementations, to make them as functionally authentic as we can. This is one of the trade-offs that we've accepted in exchange for hermeticity.

## Faking services with the filesystem

There are several implementation strategies that are viable for local fakes of services like AWS. Embedded, in-memory implementations are typically quick to implement, and are great for narrow-scope testing, but they only work for components running in the same process/JVM. A logical progression is then to encapsulate that in-memory implementation in a dedicated server, to define a client/server protocol, and to implement fakes as clients of that server; another option is to research and to emulate an existing protocol. In order to be readily available, that server can be installed as a daemon, or developers can start/stop it continuously as they iterate. [fake-s3⁠(opens in a new tab or window)](https://github.com/jubos/fake-s3), [fake-sqs⁠(opens in a new tab or window)](https://github.com/iain/fake_sqs), and [fake-sns⁠(opens in a new tab or window)](https://github.com/yourkarma/fake_sns) are projects that are pursuing this direction. Persisting state across restarts is a subsequent challenge, as is ensuring that state can be conveniently inspected and manipulated out of band; i.e., is "hackable".

An alternative direction is to leverage an existing service that is always available in development environments: a POSIX file system. It works seamlessly across processes, its state is easy to inspect and manipulate out of band, and it is naturally persistent across restarts. Emulating services on top of the file system inherits these features for free, and you can often write a functional fake in a few hours rather than a few weeks.

With this strategy, we've written Java and Python fakes for blob storage, message queues, event notifications, emails, and a workflow engine. The implementations are kept simple, they are not intended to be performant or to be scalable, but they are completely functional, and have proved to be more than sufficient for local development.

The following sections give a high-level summary of the strategies used by fakes that we substitute for services from AWS during local development. All these fakes store state in a configurable location on the filesystem, typically `/var/canva`. Paths referenced in examples are relative to that location. To give a sense of scale, the initial implementation of each of these fakes took no more than a day to complete, and each is roughly a few hundred LOC.

## Blobs (S3)

The file-based blob service stores blobs in the obvious manner:
    
    
    s3/<bucket>/<key>

Copy

Basic S3 operations, like get and put, map trivially to file operations, and are straightforward to implement. More complex operations, like paginated or prefixed listing, can be implemented simply if some inefficiences can be tolerated. For example, we implement paginated listing by loading the full result set of all matching files upfront, and paginating in memory.

We emulate versioned buckets by marking them with a top-level `s3/<bucket>/.versioned` file, and appending a version tag to the filename, with a scheme of `s3/<bucket>/<key>.<version>`.

In order to generate URLs that function in a browser, both for downloads and uploads, we run a ~250LOC node.js HTTP server. That server replicates, to the degree that we require, S3's path-encoding behavior, CORS mechanisms, and access control policies.

Example files:
    
    
    s3/static.canva.com/images/icon_arrow_down.png
    
    s3/static.canva.com/images/icon_arrow_down_hover.png
    
    s3/static.canva.com/images/icon_arrow_down_on.png
    
    s3/static.canva.com/images/icon_arrow_up.png
    
    s3/static.canva.com/images/icon_arrow_up_hover.png
    
    ...

Copy

## Message queues (SQS)

The file-based message client each queue in a single directory, with the following structure:
    
    
    sqs/<queue-name>/.lock/
    
    sqs/<queue-name>/conf
    
    sqs/<queue-name>/messages

Copy

  * `.lock` is used to establish a cross-process mutex lock, by leveraging the atomicity of `mkdir` in a POSIX filesystem. All read and write operations on the queue are performed in critical sections scoped by possession of that lock.
  * `messages` contains the queue messages, one message per line, including the requeue count, visibility deadline, receipt id, and message contents.
  * `conf` contains the queue configuration; specifically, its redrive policy.



Some queue operations (push) can be implemented efficiently by appending to the messages file, but others (pull/delete) are implemented by preparing an entirely new file, then renaming it to `messages`. This is another inefficiency concession that turns out to be perfectly acceptable for local development, and keeps the implementation simple. For example, pushing messages to a queue, with an optional delivery delay, is implemented as follows:
    
    
    private void lock(File lock) throws InterruptedException {
    
        while (!lock.mkdir()) {
    
          Thread.sleep(50);
    
        }
    
      }

JAVA

Copy
    
    
    private void unlock(File lock) {
    
        lock.delete();
    
      }
    
    
    
    
      @Override
    
      public void push(String queueUrl, Integer delay, String... messages)
    
          throws InterruptedException, IOException {
    
        String queue = fromUrl(queueUrl);
    
        File messages = getMessagesFile(queue);
    
        File lock = getLockFile(queue);
    
        long visibileFrom = (delaySeconds != null) ? now() + TimeUnit.SECONDS.toMillis(delaySeconds) : 0L;
    
    
    
    
        lock(lock);
    
        try (PrintWriter pw = new PrintWriter(new FileWriter(messages, true))) {  // append
    
          for (String message : messages) {
    
            pw.println(Record.create(visibileFrom, message));
    
          }
    
        } finally {
    
          unlock(lock);
    
        }
    
      }

JAVA

Copy

Continuing the example of our image import pipeline, here is a snapshot of the state of a local image import queue, contained in `sqs/import/messages`. The first two lines are in-flight messages on their first attempt; the remaining lines beginning with `0:0::` indicate queued and available messages (no prior attempts, visible from time `0`, and no receipt id).
    
    
    1:1424923314560:fe758b7b-6907-4131-ad1f-a43b17226a81:{"media":"MABJs6beuEg",...}
    
    1:1424923315074:4fc9cedf-b8c2-4463-abfb-343b80833b74:{"media":"MABJs3yZEDI",...}
    
    0:0::{"media":"MABJsxUmBps",...}
    
    0:0::{"media":"MABJs6ktg-M",...}
    
    0:0::{"media":"MABJsy0ef-c",...}

Copy

## Notifications (SNS)

In our use of SNS, the only subscribers to topics are SQS queues. Since this is the only behavior we need to replicate in the file-system client, the implementation is trivial. The file-based notification service encodes each topic as a directory, containing a single `queues` file that lists the names of the subscribed queues.
    
    
    sns/<topic>/queues

Copy

Publishing a message to a topic is done as follows:
    
    
    private final QueueClient queue;

JAVA

Copy
    
    
    @Override
    
    public void publish(String topic, String message) {
    
      try {
    
        for (String queueName : Files.readLines(queuesFile(topic), Charsets.UTF_8)) {
    
          queue.push(queue.getQueueUrl(queueName), message);
    
        }
    
      } catch (IOException e) {
    
        throw Throwables.propagate(e);
    
      }
    
    }

JAVA

Copy

## Workflows (SWF)

SWF is one of the lesser known services provided by AWS. In the [Design Marketplace⁠(opens in a new tab or window)](https://about.canva.com/news/canva-launches-design-marketplace/), designers can submit their content for inclusion in the Canva library as layouts. This submission flow involves capturing the design state, preparing rendered images, a review process, final publishing, and indexing. Some of these tasks are synchronous, some are asynchronous, some are automatic, some are manual. We use SWF to connect these distributed tasks together into a coherent flow.

The file-based workflow engine is the most complex fake we use. Before unfolding workflow state into multiple files and directories, we started with an in-memory implementation of a workflow engine where all state was externalized into serializable classes:
    
    
    class WorkflowExecution {
    
      String id;
    
      WorkflowType type;
    
      List<HistoryEvent> history;
    
      String queue;
    
      Status state;
    
      Date dateOpened;
    
      Date dateClosed;
    
      CloseStatus closeStatus;
    
    }

JAVA

Copy
    
    
    class ActivityExecution {
    
      WorkflowExecution workflow;
    
      String id;
    
      ActivityType type;
    
      String input;
    
      String queue;
    
      long scheduledEventId;
    
      long startedEventId;
    
    }

JAVA

Copy
    
    
    class State {
    
      /** Workflows indexed by their run id. This map grows continuously. */
    
      Map<String, WorkflowExecution> workflows = new HashMap<>();
    
      /** Open workflows, indexed by workflow id. */
    
      Map<String, WorkflowExecution> openWorkflows = new HashMap<>();
    
      /** Parent/child workflows: row=parent, column=child, cell=childWFInitiatedEventId */
    
      Table<String, String, String> openParentChildWorkflows;
    
      Map<String, Queue<WorkflowExecution>> decisionQueues;
    
      Map<String, Queue<ActivityExecution>> activityQueues;
    
      Map<String, WorkflowExecution> activeDecisions;
    
      Map<String, ActivityExecution> activeActivities;
    
      /** For id generation. */
    
      int tokenCounter;
    
    }

JAVA

Copy

Using that state to implement the subset of SWF operations that we use then turns out to be relatively straightforward. From that in-memory implementation, the file-based implementation follows a similar strategy to the file-based queue: the state of a domain is stored in a single file, as JSON, protected by a lock.
    
    
    swf/<domain>/.lock/
    
    swf/<domain>/engine.json

Copy

All workflow operations are implemented by deserializing the full domain state into memory, then using the in-memory engine to perform the operation, then serializing the full state back to disk, all within the scope of holding a lock directory. For the scale of work this engine has to handle during local development, this brute-force method has never warranted further optimization.
    
    
    public class FileWorkflowEngine implements WorkflowEngine {
    
      ...
    
      @Override
    
      public ActivityTask getActivityTask(String activityQueue) throws InterruptedException {
    
        long startTime = clock.currentTimeMillis();
    
        do {
    
          lock();  // same as in the file-based queue
    
          try {
    
            State state = loadState();
    
            WorkflowEngine delegate = new InMemoryWorkflowEngine(state);
    
            ActivityTask result = memory.getActivityTask(activityQueue);
    
            if (result != null) {
    
              saveState(state);
    
            }
    
            return result;
    
          } finally {
    
            unlock();
    
          }
    
          Thread.sleep(POLL_WAIT_MS);
    
        } while (clock.currentTimeMillis() - startTime < POLL_TIMEOUT_MS);
    
        return null;
    
      }
    
      ...
    
    }

JAVA

Copy

## … and the rest

Using the same patterns above, we configure our local environments to use functional in-memory or file-system fakes for several other services such as emailing, billing, analytics, and content-distribution.

## Where to from here?

It only takes the few simple strategies outlined above — clean separation of configuration, local installations for services that are available, and dependency-injected fakes for those that are not — to achieve basic functional completeness and local hermeticity in a way that is transparent to application logic. We hope the examples above give you a sense of how easily you can apply these principles in practice.

As the complexity of our production architecture increases, we're looking towards more sophisticated techniques to maintain a hermetic development environment but with increased parity with our production deployment. In an upcoming post, Josh Graham will reveal what we're doing with virtualization and containers in order to achieve this goal, and in another, Brendan Humpheys will talk about adaptive rate limiting.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.4c1ba47e.png)](https://www.canva.dev/blog/engineering/standardizing-the-development-environment/)

[ToolingStandardizing the development environmentHow we've built a Standard Development Environment (SDE).](https://www.canva.dev/blog/engineering/standardizing-the-development-environment/)

Josh GrahamApr 21, 2015

[![](https://www.canva.dev/_next/static/media/thumbnail.3ac4421d.png)](https://www.canva.dev/blog/engineering/faster-ci-builds-at-canva/)

[InfrastructureFaster continuous integration builds at CanvaHow we improved our continuous integration build times from hours to less than 30 minutes.](https://www.canva.dev/blog/engineering/faster-ci-builds-at-canva/)

[Marco Lacava⁠(opens in a new tab or window)](https://www.linkedin.com/in/marco-lacava/), [Arpit Sharma⁠(opens in a new tab or window)](https://www.linkedin.com/in/notarpit/)Jul 30, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.b928bce2.png)](https://www.canva.dev/blog/engineering/when-url-parsers-disagree-cve-2023-38633/)

[SecurityWhen URL parsers disagree (CVE-2023-38633)Discovery and walkthrough of CVE-2023-38633 in librsvg, when two URL parser implementations (Rust and Glib) disagree on file scheme parsing leading to path traversal.](https://www.canva.dev/blog/engineering/when-url-parsers-disagree-cve-2023-38633/)

[Zac Sims⁠(opens in a new tab or window)](https://au.linkedin.com/in/zacsims)Sep 5, 2023

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


