---
url: https://www.canva.dev/docs/connect/mcp-server/
title: Dev MCP server - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:38.030059+00:00
---

# Dev MCP server - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/connect/mcp-server/

[Overview](https://www.canva.dev/docs/apps/build/)

Build with Canva

Apps inside Canva

Canva for your platform

Canva for AI assistants

Developer resources

[Canva CLI](https://www.canva.dev/docs/apps/canva-cli/)[Canva App Scripts](https://www.canva.dev/docs/apps/canva-app-scripts/)[Dev MCP server](https://www.canva.dev/docs/apps/dev-mcp-server/)

# Dev MCP server

How to configure the Canva Dev MCP server for an AI-assisted developer experience.

Copy page

Looking for the Canva AI Connector to help with your Canva designs? See our [Help Center⁠(opens in a new tab or window)](https://www.canva.com/help/mcp-agent-setup/).

The Canva Dev Model Context Protocol (MCP) server provides AI-powered development assistance for Canva apps. By connecting your preferred MCP client (such as Cursor, Claude Desktop, or other compatible tools) to canva.dev, you can access specialized tools and documentation to enhance your development workflow.

## Before you begin

To follow this guide, you'll need to install the following prerequisites:

  * git
  * Node.js v24 (or later)
  * npm
  * A compatible MCP client. For example, Cursor, Claude Desktop.



If you need help with any of these prerequisites, including how to set up the required tooling, see the [Prerequisites](https://www.canva.dev/docs/apps/prerequisites/).

## Step 1: Configure your MCP client

Each MCP client requires specific configuration to communicate with the Canva Dev MCP server. Follow the instructions below for your client.

CursorCursor

Claude DesktopClaude Desktop

Claude CodeClaude Code

VS CodeVS Code

MCP tools are currently only available in Agent mode.

You can automatically set up the MCP server using this [Cursor configuration link⁠(opens in a new tab or window)](cursor://anysphere.cursor-deeplink/mcp/install?name=canva-dev&config=eyJjb21tYW5kIjoibnB4IC15IEBjYW52YS9jbGlAbGF0ZXN0IG1jcCJ9). Alternatively, you can manually create the configuration with the following steps:

  1. In your project directory, create the configuration directory and file:
         
         mkdir -p .cursor
         
         touch .cursor/mcp.json

SHELL

Copy

  2. Add the following configuration to `.cursor/mcp.json`:
         
         {
         
           "mcpServers": {
         
             "canva-dev": {
         
               "command": "npx",
         
               "args": [
         
                 "-y",
         
                 "@canva/cli@latest",
         
                 "mcp"
         
               ]
         
             }
         
           }
         
         }

JSON

Copy




For more information, see the [Cursor MCP documentation⁠(opens in a new tab or window)](https://docs.cursor.com/context/model-context-protocol#configuring-mcp-servers).

Although Claude Desktop is good at documentation assistance, we recommend using Cursor or Claude Code for active development because of their superior feedback mechanisms.

  1. Open Claude Desktop Settings:

     * On Windows, use the keyboard shortcut `Ctrl + ,`.
     * On macOS, use the keyboard shortcut `Command + ,`.
  2. Navigate to the **Developer** tab.

  3. Click **Edit Config** and add the following configuration to the config file:
         
         {
         
           "mcpServers": {
         
             "canva-dev": {
         
               "command": "npx",
         
               "args": [
         
                 "-y",
         
                 "@canva/cli@latest",
         
                 "mcp"
         
               ]
         
             }
         
           }
         
         }

JSON

Copy




For more information, see the [MCP quickstart guide⁠(opens in a new tab or window)](https://modelcontextprotocol.io/quickstart/user).

Run the following command in your terminal:
    
    
    claude mcp add canva-dev -- npx -y @canva/cli@latest mcp

SHELL

Copy

For more information, see the [Claude Code documentation⁠(opens in a new tab or window)](https://docs.anthropic.com/en/docs/claude-code/mcp)

MCP tools are only available in Agent mode.

  1. In your workspace, create the VS Code configuration directory and file:
         
         mkdir -p .vscode
         
         touch .vscode/mcp.json

SHELL

Copy

  2. Add the following to `.vscode/mcp.json`:
         
         {
         
           "servers": {
         
             "canva-dev": {
         
               "type": "stdio",
         
               "command": "npx",
         
               "args": [
         
                 "-y",
         
                 "@canva/cli@latest",
         
                 "mcp"
         
               ]
         
             }
         
           }
         
         }

JSON

Copy




For more information, see the [VS Code MCP documentation⁠(opens in a new tab or window)](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

## Step 2: Restart your MCP client

  1. Save all configuration changes.
  2. Restart your MCP client (for example, Cursor, Claude Desktop, or VS Code) to apply the new settings.



## Step 3: Verify the connection

To confirm the MCP server is working:

  * Look for visual indicators in your client.

For example, in Claude Desktop, click the **+** button at the bottom of the chat box, and select **Connectors** > **Manage connectors** to see the connected local "Desktop" MCP servers and their available tools.

  * Ask a simple question to test the connection. For example:

> How many components are in the App UI Kit?

If your connection is successful, your client should display a tool invocation prompt for you to accept.

![MCP tool confirmation dialog](https://www.canva.dev/_next/static/media/Cursor_tool_calling.ea9e442c.png)




MCP tools are LLM-controlled and can't be invoked directly. To invoke the MCP tools using your agent or LLM, include relevant keywords in your queries such as "App UI Kit", "Canva Developers SDK", or request specific Canva documentation references.

## Troubleshooting

  * If your MCP client can't find enabled tools:

    1. Make sure the MCP server is configured correctly (see [Step 1](https://www.canva.dev/docs/apps/dev-mcp-server/#step-1-configure-your-mcp-client)).
    2. Restart the application to refresh your client.
  * If you receive incorrect or inconsistent responses:

    * Try starting a new chat session to reset the conversation context.
    * Be specific in your queries and include relevant keywords such as "App UI Kit" or "Developers SDK".
    * Request explicit references to Canva documentation.



## Security and privacy

The MCP server operates locally on your device, fetching Canva documentation from canva.dev and other sources. Your AI agent receives context and information regarding your Canva app, and uses it to enhance its output and recommendations. The MCP server doesn't transmit your code or prompts to any other sources other than to your AI agent or LLM tool.
