---
url: https://www.canva.dev/docs/apps/mcp/tools/resize-design/
title: resize-design - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:10.344043+00:00
---

# resize-design - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/resize-design/

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

# resize-design

Create a copy of a design adapted to a different canvas size.

Copy page

Resizing requires a Canva plan with premium features, such as Canva Pro. Users on the Canva Free plan have access to a limited trial.

Use `resize-design` to create a copy of an existing design at new dimensions, with the layout rearranged to fit. The original is unchanged. It isn't for resizing a single element within a page.

## Example prompt

_"Resize my Instagram post to 1920 by 1080 for a presentation slide."_

Pass the `design_id` and a `design_type`, either a preset name or custom `width` and `height` in pixels.

## Example response

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.

This tool wraps results in an asynchronous `job` object. The server waits for the resize to finish (up to about a minute) before responding, so `status` is normally `success` or `failed`; check it before using the result.
    
    
    {
    
      "job": {
    
        "id": "job_EXAMPLE",
    
        "status": "success",
    
        "result": {
    
          "design": {
    
            "id": "DAF_EXAMPLE_RESIZED",
    
            "title": "Summer Campaign",
    
            "urls": {
    
              "edit_url": "https://www.canva.com/d/EXAMPLE_EDIT",
    
              "view_url": "https://www.canva.com/d/EXAMPLE_VIEW"
    
            },
    
            "created_at": 1784078449,
    
            "updated_at": 1784078453,
    
            "page_count": 1
    
          }
    
        }
    
      }
    
    }

JSON

Copy

Returns a `job` whose `result.design` is the new design; a `thumbnail` is included when available. Give the user the `edit_url`. A failed resize returns `status: "failed"` with an `error` containing a `code` and `message`.

If the user has exhausted their resize allowance, the tool returns a `quota_exceeded` error whose message includes an upgrade link to show the user.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [get-design](https://www.canva.dev/docs/apps/mcp/tools/get-design/)
  * [copy-design](https://www.canva.dev/docs/apps/mcp/tools/copy-design/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


