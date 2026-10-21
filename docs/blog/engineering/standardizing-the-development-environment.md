---
url: https://www.canva.dev/blog/engineering/standardizing-the-development-environment/
title: Standardizing the development environment - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:17.368019+00:00
---

# Standardizing the development environment - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/standardizing-the-development-environment/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Tooling

# Standardizing the development environment

How we've built a Standard Development Environment (SDE).

![](https://www.canva.dev/_next/static/media/thumbnail.4c1ba47e.png)

* * *

  * 


Josh GrahamApr 21, 2015

* * *

 _Originally published by Josh Graham at_ [product.canva.com⁠(opens in a new tab or window)](https://product.canva.com/sde/) _on April 21, 2015._

As an engineering team grows (along with functionality and number of users), the need for consistency in some areas increases dramatically. You quickly notice problems if the technology with which the software is developed differs from the technology on which it is deployed, and if developers have local environments that differ because their machines are self-managed. It also makes for an increasingly challenging exercise for new starters to become effective quickly. We've decided to build a Standard Development Environment (SDE) to address these issues.

In [Dave's last post](https://www.canva.dev/blog/engineering/functional-completeness-and-local-hermeticity/), he described how we achieve functional completeness and local hermiticity. These are important properties of a development environment as they directly impact the ease and speed of developing new features as well as diagnosing problems.

Another important property is that the application and infrastructural services behave in a corresponding way under all required circumstances — and as we know, that ends up being a pretty broad set of circumstances! We're all familiar with the "it works on my machine" assertion. Even in production, differences between two instances exist that can create perplexing oddities that are hard to track down.

To recap these properties:

  * _Functional completeness_ means that anything that can be done on [www.canva.com⁠(opens in a new tab or window)](http://www.canva.com) can be done in this local environment.
  * _Local hermeticity_ means that the scope of dependencies and side-effects does not extend beyond a single machine.



And introducing another property:

  * _Behavioral parity_ means the differences between environments are eliminated or reduced such that they are not relevant to the correct operation of the application.



Collective code ownership, continuous integration, continuous delivery, infrastructure-as-code, immutable infrastructure, and anti-fragile techniques greatly mitigate the risk of differences causing unintended or unreproducible issues. We'd like to apply those approaches to help deal with the rapidly increasing scale of the application, infrastructure, and engineering team.

## Operating System

Like many modern software development shops, Canva's engineering team uses OS/X machines for development but deploys to Linux machines in production.

Although the majority of the software runs on a JVM (and we benefit from its cross-platform compatibilities), there are some critical components that do not run on a JVM. With excellent tools like [homebrew⁠(opens in a new tab or window)](https://brew.sh/) at our disposal, the gap between OS/X and Linux is made a lot smaller, however there are enough differences to make life interesting. Just a few include:

  * Filesystem: Case-aware-but-insensitive (HFS Extended) versus case-sensitive (ext4)
  * Init systems: launchd versus init+upstart+systemd
  * Resource names (e.g. en0 versus eth0)
  * Directory layout and naming standards (e.g. /Users versus /home)
  * System administration tools (e.g. `sed -i`, `mktemp -d`, `md5`/`md5sum`, and package managers)



These all impact provisioning steps, and often impact runtime behaviour in subtle ways.

A small example of provisioning differences can be seen when we're trying to work out user timezone, CPU count, and system memory capacity:

![](https://www.canva.dev/_next/static/media/img-0-M_fSy7t91yv_dGqk.deb3f069.png)

**OS/X**

  * Timezone `$TZ` or `sudo -n systemsetup -gettimezone`
  * CPUs `sysctl -n hw.ncpu`
  * RAM `sysctl -n hw.memsize`



**Ubuntu**

  * Timezone `$TZ` or `cat /etc/timezone` or `timedatectl | awk '/Timezone:/ {print $2}'`
  * CPUs `nproc`
  * RAM `awk -F: '/MemTotal/ {print $2}' /proc/meminfo | awk '{print $1}'`



## Hardware

While the physical infrastructure in production is completely different to a developer's machine, these days this only manifests as differences in performance characteristics: network latency and number of available resources like CPU cores, RAM, and IOPS. Those things are quite predictable on developer machines. They are not quite so predictable (and certainly more variable) on Heroku dynos and AWS instances.

In some cases, like compilation, the developer machines are faster. As a side-effect of how we achieve functional completeness, we run some combination (sometimes all) of the services on a single developer machine, whereas in production, they are spread out over scores (and, soon enough, hundreds) of nodes. On top of browsers, IDE, team chat, and sundry apps, we can start to tax even the beefiest MacBook Pros.

## Configuration

The configuration of developer machines has been pretty much left up to individual developers. They use whatever browser(s) they like, mail client, editor, window management, screen capture, etc. However, as the company grows and matures, some IT constraints have been applied, like hard disk encryption (FileVault) and firewall turned on, and perhaps centralized authentication and access control.

On the other hand, production instances are far more tightly managed. While we're not quite at immutable infrastructure yet, our instances are all built from source, with ephemeral storage for all post-installation files, and AMIs created that strictly remain on the code release branch that created them.

Additionally, in production, software runs under particular user accounts, like "nobody", "cassandra", and so on. On the development machines, the software is run in the developer's user account (e.g. "josh"). This opens the door for problems with paths, permissions, ownership, and other differences in the process environment.

## Virtualization

As we use the latest official Ubuntu LTS AMIs in production, we're also happy to use the latest official Ubuntu LTS Vagrant base box. In both cases, we upgrade the distribution and packages so we get to the same point on both production and developer VMs, just via different paths. We can further remove differences in the future by building our base box using [Packer⁠(opens in a new tab or window)](https://packer.io/) (see below).

At first, we used a number of OS/X implementations (e.g. of database servers) and a bunch of homebrew-supplied ports of the Linux packages we use to supplement the JVM services. This entailed a long, growing, tedious, and often out-of-date set of instructions on how to mangle a developer's Mac into something that could run Canva. As the application grew, and the number of people needing to consume this hybrid platform increased, this became a progressively less appealing solution.

Of course, we turned to virtualization of the Linux platform on OS/X. As we want infrastructure as source code too, we wanted a mostly declarative, textual, repeatable means of creating and managing the virtual machines running on developer machines. [Vagrant⁠(opens in a new tab or window)](https://www.vagrantup.com/) to the rescue!

For now, we're using [VirtualBox⁠(opens in a new tab or window)](https://www.virtualbox.org/) as the virtual machine engine. There are possible performance improvements in using [Fusion⁠(opens in a new tab or window)](https://www.vmware.com/products/fusion), however most of the Vagrant ecosystem is focussed on VirtualBox.

## Synchronize Folders

While the virtualization steps above allow us to run components in a production-like environment, developers still prefer to use host-native tools for development: browsers, IDEs, etc. We also only want to run production components in the VM. To be effective in a virtualized runtime, we need a mechanism that exposes source files efficiently to both the Host and the VM.

When using the VirtualBox provider, Vagrant uses VirtualBox's default "shared folders" mechanism, which is fine for sharing files that have infrequent I/O or are the root of small directory trees.

Directories like `$HOME/.m2` and large source code repositories, however, have lots of I/O occurring during builds and are often large, deep trees containing thousands or tens of thousands of nodes.

The fastest way to share file access between the Host and the VM is with NFS. We have heavily optimized the mount options for the NFS shares to acknowledge that we're working over a host-only private network interface and we don't need access times updated. Here's the Ruby function from our `Vagrantfile` that we use to share an OS/X folder to the VM over NFS:
    
    
    def sync_nfs(config, host_path, vm_path)
    
      config.vm.synced_folder host_path, vm_path, type: "nfs", mount_options: [
    
        'async',
    
        'fsc',
    
        'intr',
    
        'lookupcache=pos',
    
        'noacl',
    
        'noatime',
    
        'nodiratime',
    
        'nosuid',
    
        'rsize=1048576',
    
        'wsize=1048576'
    
      ]
    
    end

PY

Copy

Unfortunately, there is no NFSv4.x server on OS/X (it was introduced a mere 12 years ago, after all). We will be investigating doing the sharing from the VM out to the Host (`nfsd` running on Linux and mounting the exported directories on OS/X). This gives us access to potential performance improvements in NFSv4.x (e.g. pNFS) and also means the highest I/O (build) isn't happening over NFS. The drawback will be that those directories aren't available unless the VM is running.

Specifically for VirtualBox, the `virtio` network driver, which you'd expect to be the fastest, isn't that great at dealing with NFS traffic (and possibly other types of traffic). The `Am79C973` driver is substantially faster. This, of course, may change over time, so if this sort of performance is important to you, try the different options from time to time.

We're using laptops which have batteries so we can also configure the SATA Controller in VirtualBox to use an I/O cache. Here's a snippet from our `Vagrantfile` showing how we share the Maven local repository and instruct VirtualBox to add the I/O cache:
    
    
    HOST_HOME = ENV["HOME"] || abort("You must have the HOME environment variable set")
    
    #...
    
    
    
    
    Vagrant.configure(2) do |config|
    
      #...
    
    
    
    
      sync_nfs(config, "#{HOST_HOME}/.m2/", "/home/vagrant/.m2/")
    
      #...
    
    
    
    
      config.vm.network "private_network", ip: "172.28.128.2" # needed for NFS export
    
      config.vm.provider "virtualbox" do |v|
    
        #...
    
        v.customize ["storagectl", :id, "--name", "SATAController", "--hostiocache", "on"] # assumes a battery-backed device (like a laptop)
    
      end
    
    end

BASH

Copy

### git

Git generally works just great, no matter how big the directory structure is, or what the latency is between git and the storage device.

However, `git status` must scan the entire working directory tree, looking for any untracked files. We use `cachefilesd` and `git config --system core.preloadindex true` in the VM to dramatically improve the situation. We could use `git status --untracked-files=no`, but that's not the most sensible thing to do.

The `git status` across 35,000+ files takes 0.35 - 0.4 seconds on the Host (native file system) and 0.48 - 0.55 seconds on the VM (optimized NFS and NIC). On the `virtio` NIC, as mentioned above, it is much slower — sometimes as many as 8 seconds!

### Maven

Currently, we build >30 application artifacts out of a single code repository. On the Host, it takes approximately 80 seconds to `mvn clean install` the Canva application. Even over NFS, it takes approximately 220 seconds in the VM. This isn't as bad as it sounds in practice. The vast majority of the time, the IDE is compiling changed source. Developers are also free to build on the host side because we're using the same JDK (the excellent [Zulu⁠(opens in a new tab or window)](http://www.azulsystems.com/products/zulu)® 8 OpenJDK™).

As well as exploring NFSv4, another more important mitigation will be to pull ancillary components out of the repository (possibly even one-repo-per-service in the future). This reduces the directory tree and reduces the amount of I/O required to build the app when the majority of components haven't changed.

## Forward Ports

Because some of the software (especially functional tests) expects the application to be running on `localhost`, but we might be attempting to access it from the Host, we need to forward some of those ports out of the VM to the Host.

We're using a fixed IP for the VM that is managed by VirtualBox (`172.28.128.2` on the `vboxnet1` interface), so we have a DNS entry for our VM `sde.local.canva.io` and our developer machines have an entry for `sde` in the `/etc/hosts` file.

In most cases when we're trying to connect to a process in the VM we can use the VM's hostname; however, we haven't quite re-tooled everything to be "SDE aware" yet. Port forwarding is only needed for ports being listened to by processes that bind to an address on the loopback interface (i.e. `::1/128` or `127.0.0.1/8`). Processes that bind to all interfaces (i.e. `::/0` or `0.0.0.0`) can typically be accessed by the VM's hostname.

In our `Vagranfile`, we forward the ports for our S3 fake, the Jetty-based web component (CFE), and the Solr admin console:
    
    
    # S3 fake (because http://localhost:1337/)
    
    config.vm.network "forwarded_port", guest: 1337, host: 1337
    
    
    
    
    # CFE (because http://localhost:8080/)
    
    config.vm.network "forwarded_port", guest: 8080, host: 8080
    
    
    
    
    # Solr Admin (web console which only listens on localhost)
    
    config.vm.network "forwarded_port", guest: 8983, host: 8983

BASH

Copy

## The toolchain

Here are a few key tools we use to build and run the Standard Development Environment:

![](https://www.canva.dev/_next/static/media/img-1-Tn6-hVlJKgJ10SBVu0RTsw.3bb86251.png)

## Future

In future articles, we'll talk about App Containers (Docker, Rocket), PaaS (Flynn, CoreOS), service discovery (Consul, etcd), and infrastructure-as-code (Puppet, Boxen, and Packer).

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.699fbc58.png)](https://www.canva.dev/blog/engineering/simple-fast-and-scalable-reverse-image-search-using-perceptual-hashes-and-dynamodb/)

[Image HashingSimple, Fast, and Scalable Reverse Image Search Using Perceptual Hashes and DynamoDBHow we built our first iteration of content matching at Canva.](https://www.canva.dev/blog/engineering/simple-fast-and-scalable-reverse-image-search-using-perceptual-hashes-and-dynamodb/)

[Christopher Bong⁠(opens in a new tab or window)](https://au.linkedin.com/in/christopherbong)Oct 16, 2022

[![](https://www.canva.dev/_next/static/media/thumbnail.c3cd408c.png)](https://www.canva.dev/blog/engineering/discovering-headroll-cve-2023-0704-in-chromium/)

[SecurityDiscovering Headroll (CVE-2023–0704) in ChromiumDiscovery of Headless Chromium security vulnerability, how it works, and mitigations that should be applied to similar configurations](https://www.canva.dev/blog/engineering/discovering-headroll-cve-2023-0704-in-chromium/)

[Zac Sims⁠(opens in a new tab or window)](https://au.linkedin.com/in/zacsims), [Rhys Elsmore⁠(opens in a new tab or window)](https://au.linkedin.com/in/rhyselsmore)Apr 5, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.733607a9.jpg)](https://www.canva.dev/blog/engineering/endpoint-vulnerability-management-at-scale/)

[SecurityEndpoint vulnerability management at scaleHow we do endpoint vulnerability management at Canva.](https://www.canva.dev/blog/engineering/endpoint-vulnerability-management-at-scale/)

[Santiago Gutiérrez⁠(opens in a new tab or window)](https://www.linkedin.com/in/santiago-gutierrez-z/)May 7, 2024

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


