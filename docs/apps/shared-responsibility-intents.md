---
url: https://www.canva.dev/docs/apps/shared-responsibility-intents/
title: Shared responsibility model for intents - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:43.986753+00:00
---

# Shared responsibility model for intents - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/shared-responsibility-intents/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

API reference

[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)

App UI Kit reference

[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

Canva REST API reference

[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)

Webhooks notification reference

[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

Tools

[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)

# Shared responsibility model for intents

Shared security responsibilities for developing apps inside Canva.

Copy page

## Background

Shared responsibility models clarify security responsibility between a platform provider and developers building apps that connect to that platform. This page covers the model for apps inside Canva, which are built with intents.

Building apps that connect to Canva means that developers share the same users as Canva. As a result, developers must take some responsibility to protect user data and privacy, which can differ from other Software as a Service (SaaS) product expectations. Canva, as a provider, takes some responsibility, but not all of the security responsibility.

Read through the following sections to understand your security responsibilities, as well as Canva's responsibilities.

Make sure that you read, and are complying with, the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms).

Noncompliance may result in Canva:

  * Suspending your app
  * Disabling access to it from the Canva App Marketplace



We reserve the right to amend this page from time to time at our sole discretion.

For specific recommendations on how to security harden your app, see [the Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/). For more information on authorization security, see the [Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/) and the guide on [Verifying JWTs](https://www.canva.dev/docs/apps/verifying-jwts/). For authentication steps, see the guide on [Authenticating users](https://www.canva.dev/docs/apps/authenticating-users/).

## App concepts

**Canva apps**

Apps add features to Canva. They run in the browser and are built with standard web technologies, such as JavaScript. Apps are built using the Canva Developers SDK, which is made up of libraries and capabilities that combine to build feature-rich apps. The Developers SDK enables your app to:

  * Use standard web technologies to render a user interface.
  * Use the Fetch API to integrate with the app's backend.
  * Use the Developers SDK to integrate with the core Canva experience.



**App architecture**

The App architecture is comprised of the following components:

  * Developers SDK libraries - methods that let you invoke Developers SDK functionality.
  * [UI Components⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-ui-kit/) (optional) - a component suite that lets you define app user interfaces using a React-based component library.
  * App backend (optional) - an application server that allows you to complete complex computations, expose additional resources, or store additional information your users require.



![Example App architecture](https://www.canva.dev/_next/static/media/app-architecture.903deffb.png)

**App changes**

Security responsibilities can change as you build your app. For example, if you're providing complex computations through an app backend, and storing additional information for users, you'll have additional responsibilities to maintain the security of the app backend. It's important to be aware of how your responsibilities could change if your app changes scope.

## Security operations

### Vulnerability management and disclosure

Minimize security incidents through early identification of vulnerabilities and timely remediation. Provide a framework to manage the constantly changing vulnerability landscape.

Your responsibilities| Canva's responsibilities  
---|---  
Conduct regular security reviews of infrastructure and source code using vulnerability scanning tools, vulnerability disclosure programs, or penetration testing by external parties.| Suspend apps that haven't mitigated security vulnerabilities, as explained in the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).  
Mitigate or remediate app security vulnerabilities, in accordance with the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).| Communicate with developers about vulnerabilities, in apps or the platform, that may affect their apps.  
Notify Canva of critical or high security vulnerabilities discovered in your app, in accordance with the [Canva API and App Developer Terms.⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).|   
  
### Monitoring and alerting

Your responsibilities| Canva's responsibilities  
---|---  
Ensure adequate monitoring and alerting is implemented for backend functionality to ensure the timely identification and containment of security events or incidents.| Ongoing monitoring of Developers SDK platform health, raising alerts in response to degraded performance, security, or abuse events.  
  
### Logging

Your responsibilities| Canva's responsibilities  
---|---  
Ensure your app doesn't log sensitive security data, personally identifiable information, authentication tokens, and user-generated content, or any other data that might be deemed sensitive by your data classification policy.| Maintain robust logging that includes an audit trail of actions performed within Canva.  
Ensure you implement adequate logging for backend functionality to ensure the timely identification and containment of security events or incidents.| Restrict access to logs based on organization permissions.  
  
### Incident response

As the frequency of security vulnerabilities increases, your incident response plan becomes crucial. It's essential to have effective measures in place to detect and respond to unauthorized access to your systems and data.

Your responsibilities| Canva's responsibilities  
---|---  
Promptly notify Canva of any incidents involving Developers SDK app data in accordance with the [Canva API and App Developer Terms.⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/)| Maintain a detailed action plan for responding to security incidents, including steps to contain and remediate the attack, and communicate with stakeholders.  
Develop a detailed action plan for responding to security incidents, including steps to contain and remediate the attack, and communicate with users.| Regularly test the incident response plan to ensure its effectiveness.  
Regularly test your incident response plan to ensure its effectiveness.|   
  
### Network security

Ensure appropriate network security controls are implemented preventing threat actors from accessing sensitive information while requests are in transit between services.

Your responsibilities| Canva's responsibilities  
---|---  
Use secure protocols and configurations to encrypt traffic between your app and backend, and between internal services.| Ensure that modern, secure protocols are supported by the platform.  
Handle data collected and stored in your backend according to your data classification policy, or with current best practice.|   
  
### Infrastructure security

Maintain the integrity, confidentiality, and availability of underlying infrastructure, and provide a safe computing environment.

Your responsibilities| Canva's responsibilities  
---|---  
Ensure that you have hardened the app backend, and any associated services. For more information see [OWASP Web Service Security Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html) and the [OWASP Database Security Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html).| Ensure the platform infrastructure is hardened.  
Scan regularly for security misconfigurations and vulnerabilities.| Scan regularly for security misconfigurations and vulnerabilities.  
Use the provided runtime in a way that doesn't purposely try to bypass security controls.| Provide a secure runtime for apps that prevents bypassing security controls.  
  
### Disaster recovery

Data, source code, and other business assets underpin your apps and related system functionality. It's important to minimize the impact of accidental or malicious disasters with an action plan or other recovery mechanism.

Your responsibilities| Canva's responsibilities  
---|---  
Establish a business continuity and disaster recovery plan to minimize the impact of outages to the functionality of your app during incidents, or after an accidental or malicious disaster.| Ensure that data stored by Canva on behalf of your app is backed up, and can be reasonably restored in an incident.  
| Maintain business continuity and disaster recovery plans.  
  
### Subdomain ownership and lifecycle management

Subdomains used by apps, especially those hosting authentication, authorization, or identity-related services, must be actively maintained to prevent unauthorized control. Subdomain takeover occurs when a DNS record points to an unclaimed, de-provisioned, or misconfigured resource. If an attacker gains control of such a subdomain, they can impersonate legitimate services, intercept requests, or distribute malicious content under a trusted domain.

This risk is particularly significant when subdomains are used for OAuth/OIDC authorization servers, identity providers (IdPs), or other security-critical surfaces.

Your responsibilities| Canva's responsibilities  
---|---  
Maintain ownership and active configuration of any service referenced by DNS records (for example, A, CNAME, or ALIAS records).| Monitor Canva-owned subdomains for takeover indicators or misconfigurations.  
Remove or update DNS entries that point to resources that have been deleted, renamed, expired, or migrated.| Suspend or restrict apps that introduce critical subdomain risks, in line with the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).  
Validate ownership and claim status regularly, ensuring referenced infrastructure is actively provisioned.|   
Monitor for dangling DNS records, particularly for subdomains associated with OAuth/OIDC authorization servers, identity providers (IdPs), token and introspection endpoints, `/.well-known/openid-configuration` metadata, JWKS endpoints, and redirect URIs or callback handlers.|   
Ensure that security-critical subdomains are never delegated to unmanaged or temporary resources without proper lifecycle controls.|   
Respond promptly to notices about misconfigurations or potential takeover conditions.|   
Document subdomain lifecycle events, including provisioning, migration, and decommissioning, as part of your operational security practices.|   
  
## Trust and safety

### User identity and access management

Your responsibilities| Canva's responsibilities  
---|---  
Verify user and team access to content before serving that content to a user using available mechanisms.| Authenticate user and team membership.  
Use authentication APIs for third-party platform access.| Provide authentication APIs for third-party platform access.  
| Provide a mechanism for apps to verify user and team access to Canva content.  
  
### Denial-of-service prevention

Denial-of-Service (DoS) attacks deliberately and maliciously disrupt API, system, and site operations. DoS attacks degrade user experience. Protect your app with detection and mitigation mechanisms.

Your responsibilities| Canva's responsibilities  
---|---  
Detect DoS attacks against app backends.| Detect DoS attacks executed through app frontends, or caused by apps.  
Mitigate DoS attacks against app backends.| Mitigate DoS attacks executed through app frontends, or caused by apps.  
| Suspend apps that might be misbehaving or insufficiently managing high volumes of requests.  
  
### Abuse prevention

Your responsibilities| Canva's responsibilities  
---|---  
Ensure your app works in accordance with the restrictions outlined in Section 5 of [the Canva API and App Developer Terms.⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/)| Detect and mitigate apps that disrupt the normal operations of Canva or other Canva apps.  
Ensure your app does not exceed the Canva API and Developers SDK platform quotas and limits.| Enforce platform limits, such as for storage and request throughput.  
  
## App

### Authenticating requests to the app

Ensure that all requests made to apps are sufficiently authenticated.

Your responsibilities| Canva's responsibilities  
---|---  
Authenticate users to your app, or the third-party platform, before serving additional content.| Provide a secure mechanism to authenticate with apps, or other third-party platforms.  
Adhere to current best security practices when authenticating to your platform, or to third-party platforms.| Ensure state token authenticity is verified before proceeding to the next step in the authentication workflow.  
Ensure you have verified [nonce token authenticity](https://www.canva.dev/docs/apps/authenticating-users/#validating-the-nonce) before proceeding to the next step in the authentication flow.| Authenticate the user to Canva before launching your Canva app.  
  
### Authorizing requests from the app

Ensure that every request made from apps to your backend is sufficiently authorized.

Your responsibilities| Canva's responsibilities  
---|---  
[Verify the authenticity](https://www.canva.dev/docs/apps/verifying-http-requests/) of incoming requests to your app backend.| Obtain user consent before launching your Canva app.  
[Verify that the user and team](https://www.canva.dev/docs/apps/verifying-jwts/) are authorized to access content before serving it.| Ensure that only users with access to Canva can interact with apps.  
Verify the user and team are authorized to access additional content being served through a third-party platform before providing access.| For private apps, ensure that only users with access to the team can interact with the app.  
Ensure that adequate controls are in place to prevent cross-site request forgery.|   
  
### Authorizing requests to the app

Ensure that every request made from your backend to your app is sufficiently authorized.

Your responsibilities| Canva's responsibilities  
---|---  
Verify the authenticity of incoming requests to your app from your app backend.|   
  
### App framework

Ensure frameworks and third-party libraries used to build apps are free of security bugs, and you’re applying fixes in line with the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).

Your responsibilities| Canva's responsibilities  
---|---  
Ensure the frameworks and third-party libraries used in your app are up-to-date with the latest security patches.| Apply secure development culture and practices when building the app framework.  
| Remediate defects and vulnerabilities within the Developers SDK framework.  
  
### Input validation and output encoding

Ensure sufficient input validation and output encoding within apps. For example, when returning HTML to render in the app's UI, ensure that you use HTML entity encoding for variables added to the web template. This helps protect users from attacks like cross-site scripting.

Your responsibilities| Canva's responsibilities  
---|---  
Treat all user input as unsafe and untrusted, regardless of the input source.| Appropriately encode all HTML output for UI Components.  
Adhere to current best security practices when providing or consuming data from third-party platforms.|   
Validate data sent to your app, and ensure you encode data appropriately.|   
  
### Business logic

Protect the legitimate process flow of an app, and don't expose the process flow in ways that results in negative consequences.

Your responsibilities| Canva's responsibilities  
---|---  
Identify and remediate business logic flaws through regular testing.|   
Apply security controls in layers to mitigate business logic flaws.|   
  
### Tenant security

Your responsibilities| Canva's responsibilities  
---|---  
| Ensure isolation between apps. An app, 'App A', cannot communicate with 'App B'.  
| Ensure isolation between users and teams. For example, 'Team A' can access 'App A'. Even if 'App A' is made available for 'Team B', a user in 'Team A', cannot use 'App A' to access the data of 'Team B'.  
  
### Data storage

Appropriately manage data throughout its lifecycle, from data entry to data destruction.

Your responsibilities| Canva's responsibilities  
---|---  
Ensure that data collected and processed is minimized to only collect what's required for the app to function as intended.| Maintain web storage separation and cleanup between user sessions.  
Ensure that sensitive security data, such as API keys, pre-shared keys, or encryption keys, aren't hard-coded in source code. For more information see the [OWASP Secrets Management Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) and the [OWASP Password Storage Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).|   
Ensure that sensitive security data, such as API keys, pre-shared keys, and encryption keys, aren't persisted.|   
Ensure that appropriate processes are in place to handle the revocation and rotation of sensitive security data.|   
Ensure that any personal information collected by your app is handled in accordance with your data classification policy, applicable data protection, and privacy legislation.|   
Limit disclosure of confidential information shared with employees, contractors, legal, or financial and accounting advisors to a need to know basis, as outlined in the [Canva API and App Developer Terms.⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/)|   
  
### Secure development activities

A secure software development framework is a set of functional practices that, when applied appropriately, can achieve the following:

  * Reduce the number of vulnerabilities in released software.
  * Reduce the potential impact of the exploitation of undetected or unaddressed vulnerabilities.
  * Address the root causes of vulnerabilities to prevent reoccurrences.



Your responsibilities| Canva's responsibilities  
---|---  
Adopt secure software development frameworks or practices that aid in the identification, prioritization, and remediation of security vulnerabilities. For more information see the [OWASP Secure Product Design Cheat Sheet.⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html)|   
Perform regular threat modelling on apps and their critical paths to identify, prioritize, and remediate threats that might impact the security of your app.| 
