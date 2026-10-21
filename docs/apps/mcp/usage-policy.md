---
url: https://www.canva.dev/docs/apps/mcp/usage-policy/
title: Usage policy - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:11.638531+00:00
---

# Usage policy - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/usage-policy/

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

# Usage policy

Guidelines on appropriate and responsible use of Canva’s MCP server.

Copy page

Review our usage policy to confirm your AI use adheres to our guidelines. If your implementation breaches these guidelines, we may ask you to remediate the breach or we may opt to remove it.

## 1\. Purpose and scope

This policy applies to external partners building MCP-based experiences that integrate with the Canva MCP server through the Canva REST APIs and tools.

It governs:

  * Brand use and representation.
  * UX and integration quality.
  * Data privacy and security.
  * Brand Kit and template handling.
  * Agent permissions and execution behavior.
  * API usage, rate limits, and credits.
  * Distribution and review readiness.



Partners must comply with:

  * Canva Terms presented during OAuth authorization.
  * Developer Portal technical guidance.
  * Platform review standards.



This policy supplements [Canva’s API and App Developer Terms⁠(opens in a new tab or window)](https://www.canva.com/policies/canva-developer-terms/) and any applicable platform documentation. If there is any inconsistency, the Developer Terms (and any applicable written agreement with Canva) will prevail.

Canva reserves the right to suspend or withdraw MCP access for violations of this policy.

Some requirements relate to partner-side behavior Canva cannot continuously monitor; compliance may be verified via evidence/audit and enforced using the suspension/withdrawal rights above.

## 2\. Brand use and representation

### 2.1 Naming and representation

  * Apps must clearly indicate that users are accessing Canva MCP functionality.
  * Use only compatibility language (e.g., “for Canva,” “works with Canva”).
  * Don't imply the app is built, endorsed, or certified by Canva unless formally authorized.



### 2.2 Logo usage

  * Only approved Canva logo assets may be used.
  * Logos must not be altered, recolored, distorted, or embedded within third-party wordmarks.
  * Logo usage must not imply endorsement or certification.



## 3\. UX and integration quality

### 3.1 Integration standards

Partners must:

  * Define clear use cases.
  * Map data flows explicitly.
  * Implement secure OAuth flows.
  * Validate inputs before MCP invocation.
  * Monitor integration health.
  * Implement robust error handling and retry logic.



### 3.2 Accessibility requirements

Apps must meet baseline accessibility standards:

  * Alt text where applicable.
  * Keyboard navigability.
  * Adequate color contrast.
  * Clear labeling.
  * Plain language messaging.



### 3.3 UI alignment

  * Apps should align with [UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/) for the REST APIs.
  * The experience should feel cohesive without mimicking native Canva features.
  * Avoid parallel or duplicative flows that create user confusion.



## 4\. Data privacy, security, and shared responsibility

### 4.1 Shared responsibility model

Partners are responsible for:

  * Securing their infrastructure.
  * Respecting granted OAuth scopes.
  * Protecting tokens and credentials.
  * Handling webhooks securely.
  * Monitoring and mitigating abuse.



Canva enforces:

  * Platform-level protections.
  * Health and error monitoring.
  * Rate limiting.
  * App suspension where necessary.



Canva-sourced data, prompts, outputs, Brand Kit elements, or design structures must not be used to train, fine-tune, evaluate, or improve external AI models.

### 4.2 Data minimization

  * Only request scopes necessary for declared use cases.
  * Don't request speculative or unused scopes.
  * Authenticated flows must not be accessible without authentication.



### 4.3 Privacy and sensitive data handling

When handling user content or Brand Kit data:

  * Respect privacy preferences and opt-outs.
  * Avoid unnecessary human review of generated content.
  * Apply secure storage and transmission practices.
  * Don't retain data beyond operational necessity.



## 5\. Brand template and Brand Kit handling

### 5.1 Brand Kit usage

Brand Kits retrieved through MCP:

  * May only be used to generate or modify Canva designs.
  * Must not be exported for non-Canva design generation workflows.
  * Must not be extracted, cached, transformed, or reused outside Canva-rendered outputs.
  * Must not be used to train, fine-tune, or enrich external AI systems.
  * Must not be converted into generalized style embeddings.



Apps must not crawl, pre-fetch, enumerate, or index user designs, folders, or Brand Kits without explicit user action.

**Explicit user action** is defined as a deliberate, user-initiated request at the time of access (for example, a click or typed prompt) to retrieve or operate on specific content. Scheduled or background retrieval (including recurring “daily brief” style use cases), bulk indexing, pre-fetching, or syncing must be explicitly opt-in, provide clear user controls, and must not be enabled by default.

### 5.2 Canva template usage

  * Canva templates must not be programmatically analyzed, decomposed, or replicated outside Canva’s design environment.
  * Apps must not expose template internals (layout logic, component hierarchy, token structure).



### 5.3 Multi-brand handling

  * When Brand Kit context is provided, outputs must use only the active Brand Kit.
  * Brand assets from multiple Brand Kits may only be merged if the user has access to each Brand Kit and explicitly requests multi-brand output.



## 6\. Agent identity and permission controls

### 6.1 User-level permissions

MCP agents must:

  * Execute strictly within the authenticated user’s permission scope.
  * Not escalate privileges beyond the OAuth token used at invocation.
  * Not access designs, folders, or Brand Kits outside the user’s access graph.



### 6.2 Shared agent governance

For shared MCP agents:

  * Shared agents must not execute using another user’s Canva OAuth token.
  * Sharing an agent may only share its configuration and logic. Each user must authenticate their own Canva account before they can run the agent or access Canva-derived outputs.
  * Each execution must evaluate permissions at runtime per invoking user.
  * Clearly indicate what user content is being accessed or shared.
  * Shared agents must not retain or reuse user context across users with different permissions.
  * Cross-user caching of design metadata, Brand Kit data, or prompts is prohibited.
  * Logs must segment user sessions logically.



### 6.3 No implicit delegation

  * Agents may not act on behalf of another user without explicit delegation authorization.
  * Delegated workflows must require explicit approval and scope validation.



## 7\. API usage, rate limits, and credits

### 7.1 Rate limits

  * MCP tools follow per-user limits aligned with the documentation for the REST APIs.
  * Some tools may have extended execution time (e.g., `generate-design` may take up to 60 seconds).
  * OAuth endpoints enforce per-client protections and aren't partner-tunable.



Partners must:

  * Implement exponential backoff on 429 responses.
  * Avoid bulk automation that circumvents per-user limits.



### 7.2 Reliability

  * Apps must monitor error rates.
  * Persistent high error rates may result in suspension.
  * Retry logic must be predictable and bounded.



### 7.3 Credit model

  * Canva’s credit model applies to applicable MCP tools (e.g., `generate-design`).
  * Where possible, partners must show the user's Canva credit usage in the UX or tool call response.
  * Apps must not mask or obscure credit consumption.



## 8\. Distribution and review readiness

Before launching a public app, partners must:

  * Confirm compliance with Canva brand and UI guidelines.
  * Validate naming and logo usage.
  * Verify OAuth flows and scopes.
  * Test rate-limit handling.
  * Confirm secure data handling.
  * Ensure error monitoring is in place.



## Learn more

  * Review the [Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/) for additional restrictions
  * Overview of [About Canva MCP](https://www.canva.dev/docs/apps/mcp/) for AI assistants


