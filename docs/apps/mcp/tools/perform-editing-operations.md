---
url: https://www.canva.dev/docs/apps/mcp/tools/perform-editing-operations/
title: perform-editing-operations - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:10.489358+00:00
---

# perform-editing-operations - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/perform-editing-operations/

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

# perform-editing-operations

Apply one or more edits within an open editing transaction.

Copy page

Use `perform-editing-operations` after [start-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/start-editing-transaction/). Edits stay in draft until you commit with [commit-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/commit-editing-transaction/).

## Example prompt

_"Update the headline to 'Introducing Canva AI Editing'."_

Pass `transaction_id`, `page_index`, and `operations` (an array of `{type, element_id, text}`).

## Example response

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.
    
    
    {
    
      "richtexts": [
    
        { "page_index": 1, "regions": [ { "type": "character", "text": "Introducing Canva AI Editing" } ], "containerElement": { "type": "TEXT", "position": { "top": 399.67, "left": 160.92 }, "dimension": { "width": 758.16, "height": 175.35 } }, "element_id": "ELEMENT_EXAMPLE_1" }
    
      ],
    
      "fills": [ { "type": "image", "asset_id": "ASSET_EXAMPLE", "page_index": 1, "editable": true, "element_id": "ELEMENT_EXAMPLE_2" } ],
    
      "thumbnails": [ { "width": -1, "height": -1, "url": "https://design-manipulation-download.canva.com/EXAMPLE" } ],
    
      "edit_operation_results": [ { "status": "success", "operation_info": { "type": "replace_text", "element_id": "ELEMENT_EXAMPLE_1" } } ],
    
      "pages": [ { "page_id": "PAGE_EXAMPLE", "page_number": 1, "dimension": { "width": 1080, "height": 1350 }, "is_responsive": false, "is_empty": false, "is_editable": true } ]
    
    }

JSON

Copy

`operations` is an array of operation objects. Check `edit_operation_results` for a per-operation `status` of `success`. On responsive pages, use `find_and_replace_text` rather than `replace_text`.

Don't pass a raw image URL into an editing operation. Upload it first with [upload-asset-from-url](https://www.canva.dev/docs/apps/mcp/tools/upload-asset-from-url/) to get an `asset_id`.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [start-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/start-editing-transaction/)
  * [commit-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/commit-editing-transaction/)
  * [upload-asset-from-url](https://www.canva.dev/docs/apps/mcp/tools/upload-asset-from-url/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


