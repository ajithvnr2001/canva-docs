---
url: https://www.canva.dev/docs/apps/mcp/troubleshooting/
title: Troubleshooting and common questions - Canva for AI assistants - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:11.524227+00:00
---

# Troubleshooting and common questions - Canva for AI assistants - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/troubleshooting/

Canva for AI assistants

[About Canva MCP](https://www.canva.dev/docs/apps/mcp/)

Getting started

[Access and permissions](https://www.canva.dev/docs/apps/mcp/access/)[Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)[Best practices for Canva MCP](https://www.canva.dev/docs/apps/mcp/best-practices/)[Troubleshooting](https://www.canva.dev/docs/apps/mcp/troubleshooting/)[Tools](https://www.canva.dev/docs/apps/mcp/tools/search-designs/)[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)

Workflows

[Design edit handoff](https://www.canva.dev/docs/apps/mcp/workflows/design-edit/)

Add your tool to Canva AI

[Connectors in Canva AI](https://www.canva.dev/docs/apps/mcp/canva-ai/)

Policies

[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

# Troubleshooting and common questions

Commonly asked questions when integrating with the Canva MCP server.

Copy page

Here are some common issues we've seen raised about working with the MCP.

## Timeouts

Most operations will complete without any issues. The `generate-design` tool can have longer execution times. If you experience a timeout with these operations in the Canva MCP, we recommend increasing your timeout to 60 seconds.

## Getting a client ID and client secret

Create an app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) and turn on Canva MCP. The app's **Credentials** give you a client ID and client secret, and you manage the app's redirect URLs in the Portal. For the steps, follow the Canva for AI assistants path in the [Quickstart](https://www.canva.dev/docs/apps/quickstart/).

## Organization level authentication

Canva doesn't support organization level authentication. Each user must authenticate individually with Canva. Unlike some APIs where you can authenticate at the application level, the Canva MCP requires per-user authentication for the following reasons:

  * **Access varies by user:** Users have different permissions to designs, brand kits, and assets based on their Canva account and team memberships
  * **Personal content:** Users can only access their own designs and resources, or those shared with them specifically
  * **Security and privacy:** Individual authentication ensures users only see content they're authorized to access



You can't set up a single "service account" or application-level authentication that works for all users. Each user connecting through your platform will need to complete the OAuth flow with Canva to grant access to their personal content.

## Enabling the right domains

Canva's MCP server communicates over two domains:

  * `canva.com`
  * `canva.ai`



Your client will need to allow responses from both domains for optimal performance and to avoid cross-origin request restrictions.
