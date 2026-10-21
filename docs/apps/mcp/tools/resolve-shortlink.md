---
url: https://www.canva.dev/docs/apps/mcp/tools/resolve-shortlink/
title: resolve-shortlink - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:11.028131+00:00
---

# resolve-shortlink - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/resolve-shortlink/

Tools

Discovery

[search-designs](https://www.canva.dev/docs/apps/mcp/tools/search-designs/)[get-design](https://www.canva.dev/docs/apps/mcp/tools/get-design/)[get-design-content](https://www.canva.dev/docs/apps/mcp/tools/get-design-content/)[get-design-pages](https://www.canva.dev/docs/apps/mcp/tools/get-design-pages/)[resolve-shortlink](https://www.canva.dev/docs/apps/mcp/tools/resolve-shortlink/)

Generation

[generate-design](https://www.canva.dev/docs/apps/mcp/tools/generate-design/)[create-design-from-candidate](https://www.canva.dev/docs/apps/mcp/tools/create-design-from-candidate/)[create-design](https://www.canva.dev/docs/apps/mcp/tools/create-design/)[get-create-design-async-job](https://www.canva.dev/docs/apps/mcp/tools/get-create-design-async-job/)[separate-image-layers](https://www.canva.dev/docs/apps/mcp/tools/separate-image-layers/)[get-separate-image-layers-job](https://www.canva.dev/docs/apps/mcp/tools/get-separate-image-layers-job/)

Design operations

[copy-design](https://www.canva.dev/docs/apps/mcp/tools/copy-design/)[resize-design](https://www.canva.dev/docs/apps/mcp/tools/resize-design/)[merge-designs](https://www.canva.dev/docs/apps/mcp/tools/merge-designs/)[import-design-from-url](https://www.canva.dev/docs/apps/mcp/tools/import-design-from-url/)

Editing

[start-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/start-editing-transaction/)[perform-editing-operations](https://www.canva.dev/docs/apps/mcp/tools/perform-editing-operations/)[commit-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/commit-editing-transaction/)[cancel-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/cancel-editing-transaction/)

Images

[generate-image](https://www.canva.dev/docs/apps/mcp/tools/generate-image/)[get-generate-image-job](https://www.canva.dev/docs/apps/mcp/tools/get-generate-image-job/)[remove-background](https://www.canva.dev/docs/apps/mcp/tools/remove-background/)

Brand templates and autofill

[search-brand-templates](https://www.canva.dev/docs/apps/mcp/tools/search-brand-templates/)[create-brand-template-draft](https://www.canva.dev/docs/apps/mcp/tools/create-brand-template-draft/)[publish-brand-template](https://www.canva.dev/docs/apps/mcp/tools/publish-brand-template/)[list-brand-kits](https://www.canva.dev/docs/apps/mcp/tools/list-brand-kits/)[create-design-from-brand-template](https://www.canva.dev/docs/apps/mcp/tools/create-design-from-brand-template/)[get-brand-template-dataset](https://www.canva.dev/docs/apps/mcp/tools/get-brand-template-dataset/)[get-design-dataset](https://www.canva.dev/docs/apps/mcp/tools/get-design-dataset/)[autofill-design](https://www.canva.dev/docs/apps/mcp/tools/autofill-design/)

Folders

[create-folder](https://www.canva.dev/docs/apps/mcp/tools/create-folder/)[list-folder-items](https://www.canva.dev/docs/apps/mcp/tools/list-folder-items/)[search-folders](https://www.canva.dev/docs/apps/mcp/tools/search-folders/)[move-item-to-folder](https://www.canva.dev/docs/apps/mcp/tools/move-item-to-folder/)

Comments

[comment-on-design](https://www.canva.dev/docs/apps/mcp/tools/comment-on-design/)[reply-to-comment](https://www.canva.dev/docs/apps/mcp/tools/reply-to-comment/)[list-comments](https://www.canva.dev/docs/apps/mcp/tools/list-comments/)[list-replies](https://www.canva.dev/docs/apps/mcp/tools/list-replies/)

Assets and export

[upload-asset-from-url](https://www.canva.dev/docs/apps/mcp/tools/upload-asset-from-url/)[create-upload-url](https://www.canva.dev/docs/apps/mcp/tools/create-upload-url/)[get-assets](https://www.canva.dev/docs/apps/mcp/tools/get-assets/)[get-export-formats](https://www.canva.dev/docs/apps/mcp/tools/get-export-formats/)[export-design](https://www.canva.dev/docs/apps/mcp/tools/export-design/)

Help

[help](https://www.canva.dev/docs/apps/mcp/tools/help/)

# resolve-shortlink

Expand a Canva shortlink into the full design URL it points to.

Copy page

Use `resolve-shortlink` when a user shares a Canva shortlink and the linked design needs to be opened, read, or edited. Other tools don't accept shortlinks, so resolve the link first and then pass the full URL, or the design ID inside it, to the next tool.

## Example prompt

_"Open this design:<https://canva.link/abc123>[⁠(opens in a new tab or window)](https://canva.link/abc123)"_

Pass the `shortlink_id`, which is the path segment after the shortlink domain, without the domain or slashes. For `https://canva.link/abc123`, the `shortlink_id` is `abc123`.

## Example response

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.
    
    
    {
    
      "target_url": "https://www.canva.com/design/DAF_EXAMPLE/EXAMPLE_TOKEN/edit"
    
    }

JSON

Copy

Returns the `target_url` the shortlink redirects to. Pass it as the `design_id` to [get-design](https://www.canva.dev/docs/apps/mcp/tools/get-design/), which accepts a full share URL and forwards any collaboration token it contains.

A shortlink that doesn't resolve returns a `not_found` error.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [get-design](https://www.canva.dev/docs/apps/mcp/tools/get-design/)
  * [get-design-content](https://www.canva.dev/docs/apps/mcp/tools/get-design-content/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


