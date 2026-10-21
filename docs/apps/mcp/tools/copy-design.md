---
url: https://www.canva.dev/docs/apps/mcp/tools/copy-design/
title: copy-design - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:07.686819+00:00
---

# copy-design - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/copy-design/

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

# copy-design

Duplicate a design, or selected pages of it, into a new design.

Copy page

Use `copy-design` to make a separate working copy of an existing design, for example to fork it, keep a backup, or preserve the original before making changes. The source design is unchanged. It copies from a single source design only; to combine pages from more than one design, use [merge-designs](https://www.canva.dev/docs/apps/mcp/tools/merge-designs/).

## Example prompt

_"Make a copy of my sales deck with just slides 1, 3, and 5."_

Pass the `design_id` of the source design, and optionally `page_numbers`, an array of 1-based page numbers to include. Omit `page_numbers` to copy every page.

## Example response

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.

This tool returns the new design directly; it doesn't create a job.
    
    
    {
    
      "design": {
    
        "id": "DAF_EXAMPLE_COPY",
    
        "title": "Sales Deck",
    
        "owner": { "user_id": "USER_EXAMPLE", "team_id": "TEAM_EXAMPLE" },
    
        "urls": {
    
          "edit_url": "https://www.canva.com/d/EXAMPLE_EDIT",
    
          "view_url": "https://www.canva.com/d/EXAMPLE_VIEW"
    
        },
    
        "created_at": 1784078449,
    
        "updated_at": 1784078449,
    
        "page_count": 3,
    
        "design_types": ["presentation"]
    
      }
    
    }

JSON

Copy

Returns the new `design` with its `id`, `title`, `owner`, `urls`, `created_at`, `updated_at`, `page_count`, and `design_types`; a `thumbnail` is included when available. Give the user the `edit_url` to open the copy.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [get-design](https://www.canva.dev/docs/apps/mcp/tools/get-design/)
  * [search-designs](https://www.canva.dev/docs/apps/mcp/tools/search-designs/)
  * [merge-designs](https://www.canva.dev/docs/apps/mcp/tools/merge-designs/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


