---
url: https://www.canva.dev/docs/apps/mcp/access/
title: Access and permissions - Canva for AI assistants - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:06.860180+00:00
---

# Access and permissions - Canva for AI assistants - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/access/

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

# Access and permissions

How users authenticate to the Canva MCP server, and what they can do once connected.

Copy page

Every user of the Canva MCP server authenticates individually, and the operations available to them match their own level of access in Canva. This page covers how your AI application gets access to the Canva MCP server, how it authenticates, what a user's permissions allow, and which capabilities require a paid Canva plan.

## Getting access

Before users can authorize your AI application, create an app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps) and turn on Canva MCP. The app's credentials give you a client ID and client secret, and you manage the app's redirect URLs in the Developer Portal. For the setup steps, follow the Canva for AI assistants path in the [Quickstart](https://www.canva.dev/docs/apps/quickstart/).

## Authentication

The Canva MCP server authenticates your AI application with OAuth. Your app identifies itself with the client ID and client secret from its **Credentials** in the Developer Portal.

Canva requires each user to authenticate individually to access the MCP. This also means each user of Canva's tools in your AI assistant will need to have a Canva account. Canva stores and manages designs, assets, and permissions on a per-user basis, not at the organization level.

## Permissions

The operations available to a user match their level of access to a design or asset. For example, editing operations are only available on designs and assets for which you have edit permissions.

## Availability by plan

Some features require a paid Canva plan:

  * **All plans:** Design generation, editing, search, exports, comments, asset uploads, and most core features
  * **Canva Pro and above:** Design resizing to new dimensions, autofill, brand kits, and brand templates



## Next steps

  * [Quickstart](https://www.canva.dev/docs/apps/quickstart/)
  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


