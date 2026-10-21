---
url: https://www.canva.dev/docs/apps/mcp/tools/autofill-design/
title: autofill-design - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:07.316554+00:00
---

# autofill-design - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/autofill-design/

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

# autofill-design

Populate a design's data fields with text, images, videos, or chart data.

Copy page

Use `autofill-design` to fill the data fields of a Brand Template or an existing design with structured values, producing a new design or updating the source in place. Check the available fields first with [get-brand-template-dataset](https://www.canva.dev/docs/apps/mcp/tools/get-brand-template-dataset/) or [get-design-dataset](https://www.canva.dev/docs/apps/mcp/tools/get-design-dataset/).

Autofill is available to users on Canva Pro, Business, and Enterprise plans.

## Example prompt

_"Fill in the event flyer template with 'Spring Launch', our new hero photo, and this ticket sales table."_

Pass exactly one of `brand_template_id` or `design_id`, plus a `data` object whose keys match the source's field names and whose values match each field's type. Optional `title` and `update_in_place` are described in the tool's schema.

## Example response

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.

This tool wraps results in an asynchronous `job` object. The Canva MCP server polls the job for you for up to about a minute before responding, so `status` is normally `success` or `failed` by the time you receive it.
    
    
    {
    
      "job": {
    
        "id": "job_EXAMPLE",
    
        "status": "success",
    
        "result": {
    
          "type": "create_design",
    
          "design": {
    
            "id": "DAF_EXAMPLE",
    
            "title": "Spring Launch Flyer",
    
            "url": "https://www.canva.com/d/EXAMPLE",
    
            "urls": {
    
              "edit_url": "https://www.canva.com/d/EXAMPLE_EDIT",
    
              "view_url": "https://www.canva.com/d/EXAMPLE_VIEW"
    
            },
    
            "created_at": 1704110400,
    
            "updated_at": 1704110400,
    
            "page_count": 1
    
          }
    
        }
    
      }
    
    }

JSON

Copy

On success, `job.result.design` holds the populated design, and `result.type` is `create_design` or `update_design`. Give the user the `edit_url`. If `status` is `failed`, `job.error` contains a `code` and `message` instead.

`update_in_place` replaces the existing design's content and can't be undone, so only set it when the user explicitly asks to refill that design.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [get-brand-template-dataset](https://www.canva.dev/docs/apps/mcp/tools/get-brand-template-dataset/)
  * [upload-asset-from-url](https://www.canva.dev/docs/apps/mcp/tools/upload-asset-from-url/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


