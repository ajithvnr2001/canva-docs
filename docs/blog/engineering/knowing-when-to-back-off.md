---
url: https://www.canva.dev/blog/engineering/knowing-when-to-back-off/
title: Knowing when to back off - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:15.195419+00:00
---

# Knowing when to back off - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/knowing-when-to-back-off/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Performance

# Knowing when to back off

During periods of heavy use, we needed a mechanism to ask the browser and mobile apps to back off and reduce the frequency of auto-saves.

![](https://www.canva.dev/_next/static/media/thumbnail.8f0b991b.png)

* * *

  * 


[Brendan Humphreys⁠(opens in a new tab or window)](https://www.linkedin.com/in/brendanhumphreys/)May 28, 2015

* * *

 _Originally published by_ [_Brendan Humphreys_ ⁠(opens in a new tab or window)](https://twitter.com/brendanh) _at_ [product.canva.com⁠(opens in a new tab or window)](https://product.canva.com/backing-off/) _on May 28, 2015._

[Canva's design editor⁠(opens in a new tab or window)](https://www.canva.com/) features an auto-save function. While you're working on a design we periodically send differences to our server. This means you don't lose too much work if your computer crashes or you accidentally close your browser tab. During periods of heavy use, we needed a mechanism to ask the browser and iOS applications to back off and reduce the frequency of auto-saves.

## Tradeoffs

There is an obvious technical trade-off with the auto-save rate: the more often we save your design, the less you lose in the event of a mishap, but with more write operations occurring through the backend and to the database cluster. We happen to use a [MongoDB⁠(opens in a new tab or window)](https://mongodb.com/) cluster to store the design information as it efficiently stores the data in the way the design editor works with it.

We initially opted for an aggressive auto-save rate (every five seconds in a constantly changing design), which worked well under normal load. However, we occasionally get large spikes in design activity, and these would rapidly consume our available write capacity on the database, leading to severe performance degradation for everyone using Canva. Similarly, we may wish to perform a live migration or other maintenance on the database cluster, which again reduces available write capacity. This shouldn't make Canva unusable. The biggest contributor to write load was the auto-save feature.

One option to deal with this is to increase our steady-state write capacity by scaling up our database cluster, but this means under normal load much of our newly acquired (and expensive) write capacity goes unused.

Instead, we wanted a way to dynamically adjust the design auto-save rate, asking each client to back off for a while. This would allow us to smooth out and control the demand for writes to the database during usage spikes. In networking terms, what we wanted was a way to send a [back pressure⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Back_pressure#Back_pressure_in_information_technology) signal to each client, telling it to change its auto-save rate.

## Implementing a go-slow signal

The solution we implemented allows us to set auto-save thresholds for both throughput (in terms of queries-per-second, or QPS) and latency (in terms of milliseconds). A monitor tracks a five minute moving average of throughput and latency for the update-content method (which backs the auto-save feature). If either configured threshold is exceeded, we add a `"throttle": true` attribute to the response sent back to the client.

## Monitor

The threshold monitor implementation is simple enough, backed by a [Metrics Timer⁠(opens in a new tab or window)](https://dropwizard.github.io/metrics):
    
    
    public class ThresholdMonitor {
    
      private final int maxQps;
    
      private final int maxLatency;
    
      private final Timer timer;
    
    
    
    
      public ThresholdMonitor(int maxQps, int maxLatency) {
    
        this.maxQps = maxQps;
    
        this.maxLatency = maxLatency;
    
        this.timer = new Timer();
    
      }
    
    
    
    
      public Context start() {
    
        return timer.time();
    
      }
    
    
    
    
      public boolean thresholdExceeded() {
    
        int qps = (int) timer.getFiveMinuteRate();
    
        int latency = (int) TimeUnit.NANOSECONDS.toMillis((long) timer.getSnapshot().getMedian());
    
        return qps > maxQps || latency > maxLatency;
    
      }
    
    }

JAVA

Copy

Usage is similarly simple. Here's a generic example setting target thresholds of 15 QPS throughput, and 500ms latency:
    
    
    private final ThresholdMonitor monitor = new ThresholdMonitor(15, 500);
    
    
    
    
    public void expensiveOp() {
    
      Context t = monitor.start();
    
      // do something you want to monitor and threshold
    
      t.stop();
    
    
    
    
      if (monitor.thresholdExceeded()) {
    
        // take some action to throttle or degrade
    
      }
    
    }

JAVA

Copy

In our real-world usage, we configure the monitor with dynamic thresholds that can be adjusted at runtime, allowing us to tune the thresholds. We also need to factor in the number of running instances of the service when calculating the thresholds.

We're deliberately not using a `try...finally` to unconditionally call `t.stop()` on our monitor. In our usage, we don't want failures to contribute to the monitor statistics as failures tend to be fast, and so would skew the monitoring.

## Telling clients to throttle

For a variety of reasons we elected to communicate throttling information to clients using a single boolean attribute in the JSON response. An alternative might be to use a custom HTTP Header:
    
    
    Canva-Throttle: true

Copy

## Fast slow down, slow speed up

Both our iOS and web clients respond to the throttle signal using a technique borrowed from TCP congestion control: [Additive Increase / Multiplicative Decrease⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Additive_increase/multiplicative_decrease) (AIMD). Every time a client receives a response with `"throttle": true`, it halves the rate of auto-saves (the multiplicative decrease), down to a minimum allowed rate. Conversely, when a `"throttle": false` is received, we increase the rate of auto-saves by a set amount (the additive increase), up to an allowed maximum rate. In our iOS app, the code looks like this:
    
    
    -(void) updateThrottle: (BOOL) throttle {
    
      NSTimeInterval interval = self.syncInterval;
    
      if (throttle) {
    
        interval *= 2.0f;
    
      }
    
      else {
    
        interval -= 1.0f;
    
      }
    
      self.syncInterval = MIN(MAX(interval, kCANMinSyncInterval), kCANMaxSyncInterval);
    
    }

OBJECTIVEC

Copy

Using AIMD Clients rapidly back off when a threshold is exceeded, quickly reducing write load on the backend. Once the load is below the target threshold, clients slowly increase their autosave rate, each converging on the rate that will maintain write operations at a level just below the target threshold. This is another advantage of AIMD: all clients will converge on the same rate, so the auto-save capacity is shared fairly.

## Watching clients back off

![](https://www.canva.dev/_next/static/media/img-0-ZpM8Al93_zmLUokJ.8f0b991b.png)

Here we have singled out three production instances of the document service, handling about 14 QPS of update-content traffic between them in steady state. We then applied a threshold of 6 QPS throughput across all three (averaging 2 QPS per node). The impact is immediate, as clients receive the throttle signal and back off by halving their auto-save rate until the target threshold is achieved, at which point throughput levels off. Once the threshold is removed, clients slowly revert to their preferred update rate.

The shapes of the response curves are determined by the AIMD parameters, and are worth experimenting with to get the desired behavior.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.7caec38f.png)](https://www.canva.dev/blog/engineering/testing-search-engine-optimization-scalably-without-breaking-a-sweat/)

[Search Engine OptimizationTesting Search Engine Optimization Scalably without Breaking a SweatScaling pre-development, rollout, and post-production SEO testing at Canva.](https://www.canva.dev/blog/engineering/testing-search-engine-optimization-scalably-without-breaking-a-sweat/)

[Siddharth Salunke⁠(opens in a new tab or window)](https://www.linkedin.com/in/siddharthsalunke/)Jun 20, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.c3cd408c.png)](https://www.canva.dev/blog/engineering/discovering-headroll-cve-2023-0704-in-chromium/)

[SecurityDiscovering Headroll (CVE-2023–0704) in ChromiumDiscovery of Headless Chromium security vulnerability, how it works, and mitigations that should be applied to similar configurations](https://www.canva.dev/blog/engineering/discovering-headroll-cve-2023-0704-in-chromium/)

[Zac Sims⁠(opens in a new tab or window)](https://au.linkedin.com/in/zacsims), [Rhys Elsmore⁠(opens in a new tab or window)](https://au.linkedin.com/in/rhyselsmore)Apr 5, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.212d94a6.png)](https://www.canva.dev/blog/engineering/our-journey-to-snowflake-monitoring-mastery/)

[SnowflakeOur journey to Snowflake monitoring masteryHow I learned to stop worrying and love metadata.](https://www.canva.dev/blog/engineering/our-journey-to-snowflake-monitoring-mastery/)

[Rob Scriva⁠(opens in a new tab or window)](https://www.linkedin.com/in/robertscriva/)Nov 12, 2024

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


