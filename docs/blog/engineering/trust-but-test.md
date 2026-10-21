---
url: https://www.canva.dev/blog/engineering/trust-but-test/
title: Trust but test: Vendor security testing at Canva - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:28.763897+00:00
---

# Trust but test: Vendor security testing at Canva - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/trust-but-test/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Security

# Trust but test: Vendor security testing at Canva

How we validate vendor security at Canva by going beyond compliance.

![](https://www.canva.dev/_next/static/media/thumbnail.8c4d6cb8.jpg)

* * *

  *   * 


[Kane Narraway⁠(opens in a new tab or window)](https://www.linkedin.com/in/kane-n/), [CJ Fairhead⁠(opens in a new tab or window)](https://www.linkedin.com/in/chris-fairhead/)Mar 10, 2024

* * *

Canva has a value to be a _Force for Good_ , and our security team contributes to this value through our Security Testing team, unofficially known as Priority Zero. The inspiration for this team's creation came from groups like [Google's Project Zero⁠(opens in a new tab or window)](https://googleprojectzero.blogspot.com/) and [Facebook's Red Team X⁠(opens in a new tab or window)](https://engineering.fb.com/2022/07/20/security/how-meta-and-the-security-industry-collaborate-to-secure-the-internet/) but with a Canva twist.

When choosing a vendor, we must pick the right vendor to achieve the desired outcome. Larger vendors often have resources that allow them to operate a dedicated internal security function to focus on the security of their products and environment. However, we recognize that plenty of smaller, innovative vendors deliver much value but don't always have the resources dedicated to security. To help close this gap, we partner with vendors we deem critical to data security at Canva to perform active testing and adversary simulations. These go beyond the standard automated test suites and have dedicated engineers using their skills to hunt for vulnerabilities in the product.

This allows us to proactively discover issues and impact in a safe space for Canva. Still, it also allows us to work with our vendors to discover previously unknown threats and collaborate in the remediation process. The goal here is twofold:

  * We create a tighter relationship with our vendors' security and engineering teams.


  * We aid in securing their systems for all customers, thus promoting our value of being a Force for Good by ultimately making the internet a safer place.



Like all companies, Canva uses vendors to help achieve our goals, and when choosing our vendors, we need to ensure they reach our high-security standards. These vendors can range from the cloud infrastructure Canva runs on to the software libraries we use in our products. It’s all-encompassing, and as the interconnectedness of software increases, the risk of a single point of failure grows, as evidenced by the amount of supply chain breaches over the past few years. We want to create an ecosystem of trusted, _tested_ vendors to ensure Canva remains a secure and hardened product for even our most security-conscious customers.

## Scoping

When a new tool comes in, our Governance, Risk & Compliance (GRC) team evaluates it and assigns it an inherent risk level that aligns with our risk management framework. If that risk is deemed high or critical, it comes to us for further analysis. However, even though something is a critical risk, it doesn't mean we _always_ test it.

Consider, for example, a cloud service provider (CSP) like AWS, GCP, or Azure would probably not be a good target for our testing program because of the following:

  * CSPs are too complex, and there are too many moving parts. Effective testing would take our small team years.
  * CSPs extensively test their products internally, externally, and using bug bounties. Because of the amount of testing they already go through, our additional testing has less value.
  * These CSPs are big players with lots of resources. We prefer to build in external testing as a contractual requirement instead of providing our services.



Instead, we aim to test areas where we can provide the most value, including smaller vendors, open-source libraries, and niche areas still critical to Canva and many other companies. For something like a CSP, we prefer to partner with them and have our infrastructure security team look after a longer-term engagement.

### Product or vendor

A common question for our team is whether we're here to test our vendors or their products, to which we answer, why not both?

While it’s true we’re generally engaging with a vendor to make use of their SaaS offerings, these web applications represent only a portion of a vendor's external attack surface. Often, there are large amounts of supporting infrastructure enabling the functionality and support of a product, and the security posture of these areas is equally as important as the product itself. With this in mind, we prefer to consider many alternatives when scoping our assessments so we can review a vendor's entire public-facing footprint.

This approach allows us a more comprehensive view of the external environment and often results in identifying some forgotten assets that were thought to be decommissioned long ago.

## Engagements

A typical engagement runs for 5-10 business days, depending on the scope and complexity of the application. Usually, this process requires very little time and effort from the vendor. We have an initial kick-off call, which lasts 30 minutes, with a security or engineering contact at the company. We then spin up a dedicated Slack channel running with the appropriate vendor stakeholders during this time. This allows for general back-and-forth communication and acts as an avenue for escalating any critical issues discovered.

We take the security and reliability of our vendors seriously, so we take a few precautions to reduce any chances of issues during our testing:

  * We don't run any automated scans which could lead to a dedicated denial of service (DDoS).
  * We run our tests in separate accounts that the vendor spins up when possible.
  * If we discover critical vulnerabilities or issues that would unveil other customers' data, we stop testing immediately and report the problem.



When we've completed our testing, we send a report with any findings found during our test. We're also happy to meet with the vendor to explain any issues or discuss areas where we think there might be issues, but require more thorough testing.

## Remediation

Bugs happen; it's a fact of life. Finding bugs isn't an issue, but ensuring we prioritize and remediate bugs in line with the bug's severity is. Working with vendors, we find a great indicator of their security posture is in how they respond to bugs. Some valuable signals we look for when collaborating with vendors include:

  * If the vendor has set sprints and remediation dates on when they can fix issues.
  * If they can prioritize fixes based on criticality.
  * If they value critical fixes above product work.
  * If they have processes and procedures in place for bug fixes.
  * And, of course, If they’re even willing to action reports in the first place.



We've had cases where we've found serious issues, but the vendor has gone above and beyond to fix the problems in a _timely manner_. We partnered with the vendor to remediate issues and improve their security program, leading to fewer bugs in the future. We're also more than willing to work with these vendors to retest fixes and do additional testing of new product lines we're considering for internal use because we want to secure our customers for the long term.

Of course, the opposite exists, where we've not found anything too serious, but the vendors were unwilling to work with us and raised concerns about how they ran their security program. This is still better than the worst-case scenario, where the vendor has significant bugs and no drive to fix them at all, let alone promptly.

Most vendors we work with leave long-lasting positive interactions, regardless of the security review results, and become a valued part of Canva. Ultimately, however, we still help Canva make an informed business decision about vendor security. We’ve had a small number of cases where a vendor's security posture was not up to Canva's standards, and we decided to walk away from engagements with them.

## What we’ve learned

Having operated for over 2 years, our team has tested a diverse range of vendors and their products, giving us a unique perspective on the state of the SaaS vendor space. The following sections outline some of our high-level observations.

### External security testing can be hard to get right

One of the things we love about our program is that we’re often more invested in the product's security than anyone else. After all, external testers get paid whether there are findings or not. Instead of filling reports with lower-value content, our approach reduces false positives that are often seen with automated security scanners, leading to more impactful reports. We offer this service at no cost to our vendors because it helps both Canva and the vendor to become more secure.

We've had occasions where we've delayed our testing, waiting for a company to come back with its annual penetration test. When they provide the report, we read it, and it contains no significant risks. Our team then goes on to find multiple critical vulnerabilities within hours of looking.

Pentest vendors, of course, do have a place in the industry. Plenty of amazing people and companies in this space do incredible work. We recommend the following techniques to increase the effectiveness of any testing you get done:

  * Research penetration testing vendors in your industry. Generally, industry- or location-specific vendors, give you better outcomes.
  * Consider using named consultants and having your security team interview them before any engagement. Larger companies can hire thousands of pentesters where quality varies wildly.
  * If you want to look at the quality of a company's reports, consider looking at the vendors you use to see if they use the same company. You've probably got them from the procurement documentation.
  * Consider combining penetration testing with a public bug bounty. Pentests are great for point-in-time assurance, but bug bounties give continued testing of your products.



### Some vendors outright refuse

We understand this isn't for everyone. There are highly regulated sectors where this isn't always possible, but most vendors who refuse, cite time as the primary blocker.

If a vendor can dedicate less than 2 hours of a single employee's time to working with us, we provide what is equivalent to a market-rate pentest for _free_. If more vendors understood that and the benefits they could gain from this engagement, they’d be more willing to accept.

If a vendor refuses, we don't do any active testing but look at more public signals around their security, which are lower fidelity. We still decide whether to proceed from these signals, but it's a difficult call, so we encourage vendors to work with us in a symbiotic relationship.

## Wrapping things up

In this blog post, we shared a bit about our team and the process we use. By sharing this information, we highlight the lengths we go to to keep our customers' data secure and ultimately create a more secure ecosystem for everyone.

Our team goes beyond regular third-party risk evaluations, which only look at public-facing compliance documentation, such as questionnaires and SOC2 documentation. We want to encourage others to take a similar approach and live the "Trust, but Verify" motto regarding third-party risk.

In the future, we plan to follow this up with some of the trusted vendors we've partnered with and investigate deeper into the techniques we've used, the bugs we've found, and how they've responded. If you're a vendor who works with us, you can rest assured we keep the reports private. We know everyone isn't willing to share, and that's totally OK. We occasionally reach out to a few select vendors for permission to publish our stories where we think the findings are particularly interesting and might be helpful to others. These reports are created in collaboration with the vendor, don’t share private information, and contain only bugs already remediated.

Stay tuned for more!

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.180dbd86.png)](https://www.canva.dev/blog/engineering/behind-the-draw/)

[PerformanceBehind the draw - How Canva's drawing tool worksSome of the engineering challenges we encountered while developing our vector drawing tool](https://www.canva.dev/blog/engineering/behind-the-draw/)

[Alex Gemberg⁠(opens in a new tab or window)](https://www.linkedin.com/in/grebmeg/)Mar 14, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.364a86da.png)](https://www.canva.dev/blog/engineering/optimising-s3-savings/)

[Amazon S3How Canva saves millions annually in Amazon S3 costsUnderstanding our data and usage patterns was the real key.](https://www.canva.dev/blog/engineering/optimising-s3-savings/)

[Josh Smith⁠(opens in a new tab or window)](https://www.linkedin.com/in/joshuanathansmith/)May 4, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.0b03c2dc.png)](https://www.canva.dev/blog/engineering/infrastructure-is-distribution/)

[InfrastructureInfrastructure is DistributionHow we position Infrastructure Engineering as a value-add.](https://www.canva.dev/blog/engineering/infrastructure-is-distribution/)

[Ryan Armstrong⁠(opens in a new tab or window)](https://www.linkedin.com/in/ryanarmstrongwa/)Mar 14, 2022

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


