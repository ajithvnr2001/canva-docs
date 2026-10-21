---
url: https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/
title: Shared responsibility model for the Canva REST APIs - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:40.455193+00:00
---

# Shared responsibility model for the Canva REST APIs - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/

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

# Shared responsibility model for the Canva REST APIs

Shared security responsibilities for apps built on the Canva REST APIs.

Copy page

Shared responsibility models clarify security responsibility between a platform provider and developers building apps that use that platform.

Building an app that connects to Canva means that developers share the same users as Canva. As a result, developers must take some responsibility to protect Canva user data and privacy, which can differ from other Software as a Service (SaaS) product expectations. Canva, as a provider, takes some responsibility, but not all of the security responsibility.

Read through the following sections to understand what are your security responsibilities, and what are Canva's responsibilities.

We reserve the right to amend this page from time to time in our sole discretion.

Make sure that you read, and are complying with, the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms).

Noncompliance may result in Canva:

  * Suspending your app.
  * Disabling access to your app in the Canva Apps Marketplace.
  * Discontinuing your access to Canva APIs.



For specific security advice on recommended security practices or how to handle access management, see the [security recommendations for the Canva REST APIs](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/), and the [Authentication guide](https://www.canva.dev/docs/apps/rest-apis/authentication/).

## App concepts

**Apps and data flow** Apps allow third-party app developers to extend key Canva capabilities off-platform. As a result, apps allow Canva to share data with third parties. This data sharing happens even when a user isn't actively designing in Canva. The flow of data from Canva through to third parties is controlled by app architecture. The essential component for this data flow is the REST APIs.

**REST APIs**

The REST APIs use resource-oriented URLs. They accept requests with parameters, and return JSON responses with standard HTTP response codes. For more information, see [API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/).

**App architecture** Some examples of app architectures built with the REST APIs can include, but aren't limited to:

  * Keeping Canva in sync with cloud storage and content management apps.
  * Enabling collaboration and communication with different platforms.
  * Embedding Canva into project management workflows.



Consider your app architecture, such as where customer data flows, where that data is stored, and where potential vulnerabilities may emerge. There could be implications for your security responsibilities.

## Security responsibilities

### Vulnerability management & disclosure

Minimize security incidents through early identification of vulnerabilities, and timely remediation. This includes notifying stakeholders of vulnerabilities. Provide a framework or policy to meet the challenge of a constantly changing vulnerability landscape.

Your responsibilities| Canva's responsibilities  
---|---  
Conduct regular security reviews of infrastructure and source code using vulnerability scanning tools, vulnerability disclosure programs, or penetration testing by external parties.| Suspend apps that haven't mitigated security vulnerabilities, as explained in the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).  
Mitigate or remediate app security vulnerabilities within the timelines expected in the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).| Communicate with developers about vulnerabilities in the platform or apps that may affect their apps.  
Notify Canva of critical or high security vulnerabilities in your app, in accordance with the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).|   
  
### Monitoring and alerting

Your responsibilities| Canva's responsibilities  
---|---  
Implement adequate monitoring and alerting for backend functionality to ensure timely identification and containment of security events or incidents.| Ongoing monitoring of REST API platform health, and raising alerts in response to degraded performance, security, or abuse events.  
  
### Logging

Your responsibilities| Canva's responsibilities  
---|---  
Ensure your app doesn't log sensitive security data, personally identifiable information, authentication tokens, and user-generated content, or any other data that may be deemed sensitive by your data classification policy.| Maintain robust logging that includes an audit trail of actions performed by an app.  
Implement adequate logging for backend functionality to ensure the timely identification and containment of security events or incidents.| Restrict access to logs based on organization permissions.  
  
### Incident response

As the number of security vulnerabilities and exploits increase, its crucial to develop, maintain, and test effective measures to detect and respond to unauthorized system and data access.

Your responsibilities| Canva's responsibilities  
---|---  
Notify Canva of any incidents involving Canva app data, in accordance with the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).| Maintain a detailed plan of action for responding to security incidents, including steps to contain and remediate the attack, and communicate with stakeholders.  
Develop a detailed plan of action for responding to security incidents, including steps to contain and remediate the attack, and communicate with users.| Regularly test the incident response plan to ensure its effectiveness.  
Regularly test your incident response plan to ensure its effectiveness.|   
  
### Network security

Implement appropriate network security controls to prevent threat actors from accessing sensitive information when requests move between services.

Your responsibilities| Canva's responsibilities  
---|---  
Use secure protocols and configurations to encrypt traffic between your app and backend, and between internal services.| Ensure that contemporary, secure protocols are supported by the platform.  
Handle data collected and stored in your backend according to your data classification policy, or with current best practice.|   
  
### Infrastructure security

Maintain the integrity, confidentiality, and availability of underlying infrastructure, and provide a safe computing environment.

Your responsibilities| Canva's responsibilities  
---|---  
Harden any associated services in the app backend. For more information, see the [OWASP Web Service Security Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Web_Service_Security_Cheat_Sheet.html) and the [OWASP Database Security Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html).| Ensure the platform infrastructure is hardened.  
Scan for security misconfigurations and vulnerabilities.| Scan for security misconfigurations and vulnerabilities.  
Provide a secure runtime for apps that prevents any security control bypasses.|   
Use the provided runtime in a way that doesn't purposely try to bypass security controls.|   
  
### Disaster recovery

Data, source code, and other business assets support apps and related system functionality. It's important to have mechanisms that minimize the impact of accidental or malicious disasters on essential system functionality.

Your responsibilities| Canva's responsibilities  
---|---  
| Establish a business continuity and disaster recovery plan to minimize the impact of outages to the functionality of your app during incidents, or after an accidental or malicious disaster.  
| Ensure that data stored by Canva on behalf of your app is backed up, and can be reasonably restored in an incident.  
| Maintain business continuity and disaster recovery plans.  
  
## Trust and safety

### User identity and access management

Your responsibilities| Canva's responsibilities  
---|---  
Use the mechanisms made available to verify user and team access to content before serving it to a user.| Provide APIs for authentication with third-party platforms.  
Use the APIs for authenticating users to third-party platforms.| Provide mechanisms for apps to verify user and team access to Canva content.  
  
### Denial of service prevention

Your responsibilities| Canva's responsibilities  
---|---  
Detect denial of service attacks against app backends.| Detect denial of service attacks executed via app frontends, or caused by apps.  
Mitigate denial of service attacks against app backends.| Mitigate denial of service attacks executed via app frontends, or caused by apps.  
| Suspend apps that may be misbehaving or insufficiently managing high volumes of requests.  
  
### Abuse prevention

Your responsibilities| Canva's responsibilities  
---|---  
Ensure your app complies with the restrictions contained within Section 5 of the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).| Detect and mitigate apps that disrupt the normal operations of Canva or other Canva apps.  
Ensure your app does not exceed the Canva API and REST API platform quotas and limits.| Enforce platform limits for storage, request throughput, and other points of data flow.  
  
## App

### Authentication of requests to the app

Ensure that every request made to the app is sufficiently authenticated.

Your responsibilities| Canva's responsibilities  
---|---  
Ensure the secure storage and handling of client credentials (for example, the client ID and client secret). This includes protecting credentials from exposure in source code through the app, and securely transmitting them only over encrypted connections.| Provide support for secure and recommended client authentication methods.  
Securely handle access tokens, refresh tokens, and ID tokens obtained from Canva. Ensure that tokens are used in an authenticated manner for accessing protected resources and that they are transmitted securely.|   
  
### Authorization of requests to the app

Ensure that every request made to the app is sufficiently authorized.

Your responsibilities| Canva's responsibilities  
---|---  
Verify the authenticity of incoming webhook messages to your app before displaying them to users.| Ensure that users with access to Canva can use your app.  
Verify that organizations, teams, and users are authorized to access content before serving it.| For private apps, ensure that only users with access to the team use the app.  
  
### Input validation and output encoding

Ensure sufficient input validation and output encoding is applied within the app.

Your responsibilities| Canva's responsibilities  
---|---  
Implement input validation in your app to ensure that only properly formatted data is sent to Canva. This includes validating URLs, scopes, and any data received from users before making an OAuth request.| Ensure all data received from your app, including redirect URLs, scopes, and client credentials, undergo stringent validation against expected formats and values.  
Apply appropriate encoding mechanisms to any user-generated output that might be rendered in your platform to prevent Cross-Site-Scripting (XSS) vulnerabilities. Ensuring data is safely encoded before it is displayed can protect against injection attacks that might compromise the client or the user.|   
Carefully inspect and validate authorization responses from the server. This includes ensuring that the state returned matches the one sent in the authorization request, and that access tokens and ID tokens are correctly parsed and validated before use.|   
  
### Business logic

Ensure that the app doesn't expose ways of using a legitimate process flow of an app in a way that results in a negative consequence.

Your responsibilities| Canva's responsibilities  
---|---  
Ensure that your app correctly implements the OAuth authorization code flow with PKCE (Proof Key of Code Exchange) as per the standard specifications, avoiding custom modifications that could introduce vulnerabilities.|   
Properly validate redirect URLs on the app side to prevent open redirect vulnerabilities, ensuring that redirects lead only to trusted or expected locations.|   
Implement secure error handling that doesn't expose sensitive information, ensuring that error messages are generic and logged appropriately.|   
Request only the necessary scopes required for the functionality of the app, adhering to the principle of least privilege.|   
Securely manage the state parameter within OAuth flows to mitigate Cross-Site Request Forgery (CSRF) attacks, ensuring that the state is validated for each authorization request and response.|   
Apply security controls in layers to mitigate business logic flaws.|   
  
### App framework

Ensure the frameworks and third-party libraries used to build apps don't include security bugs, and that fixes are implemented according to the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).

Your responsibilities| Canva's responsibilities  
---|---  
Choose and implement app frameworks and libraries that are robust and well-maintained. When using libraries to assist with the handling of OAuth flows, only use those recommended by the OAuth community.| Offer detailed documentation, SDKs, and libraries that facilitate building apps with the authorization server. This includes examples of secured configurations, recommended practices for integration, and troubleshooting tips.  
Configure the app framework securely, ensuring that default settings that may be insecure are adjusted according to your security guidelines. This includes secure handling of redirect URLs, ensuring proper scope requests, and correctly implementing token handling processes.| Ensure that any updates or changes to the REST API authorization flow are backward compatible or clearly communicated to developers in advance.  
Conduct thorough testing of the integrated OAuth flow within the app to identify and address any security or functional flaws that may result from incorrect handling of data from the authorization server.| Clearly communicate any known security considerations specific to the app framework or libraries provided, including regular security updates and advisories regarding known vulnerabilities.  
  
### Tenant security

Your responsibilities| Canva's responsibilities  
---|---  
Implement authentication mechanisms that robustly identify and authenticate users based on their tenant context, ensuring that access tokens and other credentials are strictly scoped to the user’s tenant.| Provide robust support for multi-tenancy within Canva, including mechanisms for team identification, and management within the OAuth flows.  
Ensure that your platform's logic and data storage mechanisms are designed to segregate and manage data on a per-tenant basis, preventing cross-tenant access or leaks.| Issue access tokens that are explicitly scoped and labeled based on the team, ensuring that resources accessible with a token are limited to those belonging to the appropriate team.  
Safely configure tenant-specific settings and customizations in the app to avoid introducing vulnerabilities that could affect tenant data security.| Offer access controls allowing for tailored configurations that respect the unique security needs of each team and organization.  
  
### Data storage

Appropriately manage data throughout its lifecycle, from data entry to data destruction.

Your responsibilities| Canva's responsibilities  
---|---  
Ensure that the data collected and processed is limited to only what is required for the app to function as intended.| Maintain web storage separation and cleanup between user sessions.  
Ensure that sensitive security data, such as API keys, pre-shared keys, or encryption keys are not hard-coded in source code. For more information, see the [OWASP Secrets Management Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) and the [OWASP Password Storage Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).|   
Ensure that you have appropriate processes to handle the revocation and rotation of sensitive security data.|   
Ensure that any personal information collected by your app is handled in accordance with the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/), your data classification policy, and applicable data protection and privacy legislation.|   
Only use confidential information in accordance with the [Canva API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/).|   
  
### Secure development activities

Secure development activities are functional practices that, when applied appropriately, can achieve the following:

  * Reduce released software vulnerabilities.
  * Reduce the potential impact of undetected or unaddressed exploitation of vulnerabilities.
  * Address the root causes of vulnerabilities to prevent recurrences.



Your responsibilities| Canva's responsibilities  
---|---  
Adopt secure development activities or practices that aid in the identification, prioritization, and remediation of security vulnerabilities. For more information, see the [OWASP Secure Product Design Cheat Sheet⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Product_Design_Cheat_Sheet.html).|   
Perform regular threat modeling on apps and their critical paths, to identify, prioritize and remediate threats that may impact the security of your app.| 
