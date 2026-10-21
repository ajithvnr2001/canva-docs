---
url: https://www.canva.dev/docs/apps/mcp/tools/create-brand-template-draft/
title: create-brand-template-draft - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:07.753344+00:00
---

# create-brand-template-draft - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/create-brand-template-draft/

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

# create-brand-template-draft

Create an editable draft design from a Brand Template.

Copy page

Brand Templates are available to users on Canva Pro, Business, and Enterprise plans.

Use `create-brand-template-draft` to get a design that you can edit and then publish back as the updated Brand Template. If a draft already exists for the Brand Template, the tool returns the existing draft.

To update a Brand Template:

  1. Call `create-brand-template-draft` with the Brand Template's ID.
  2. Edit the returned design in an editing transaction, starting with [start-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/start-editing-transaction/).
  3. Publish the edited design as the Brand Template with [publish-brand-template](https://www.canva.dev/docs/apps/mcp/tools/publish-brand-template/).



## Example prompt

_"Update our brand template for event flyers with the new logo."_

Pass the `brand_template_id`. To find Brand Templates and their IDs, use [search-brand-templates](https://www.canva.dev/docs/apps/mcp/tools/search-brand-templates/).

## Example response

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.
    
    
    {
    
      "design": {
    
        "id": "DAF_EXAMPLE",
    
        "title": "Event Flyer Template",
    
        "owner": { "user_id": "USER_EXAMPLE", "team_id": "TEAM_EXAMPLE" },
    
        "thumbnail": { "width": 595, "height": 842, "url": "https://document-export.canva.com/EXAMPLE_THUMBNAIL" },
    
        "urls": { "edit_url": "https://www.canva.com/d/EXAMPLE_EDIT", "view_url": "https://www.canva.com/d/EXAMPLE_VIEW" },
    
        "created_at": 1784078449,
    
        "updated_at": 1784078449,
    
        "page_count": 1
    
      }
    
    }

JSON

Copy

Returns the draft `design` with its `id`, `edit_url`, and `view_url`. Use the `id` to edit the draft, and later to publish it. The `thumbnail` is generated asynchronously, so it might not be present in the response.

This tool requires the `brandtemplate:content:write` scope. If the call fails with `Missing scopes: [brandtemplate:content:write]`, the user needs to disconnect and reconnect Canva in your AI application to grant the scope.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [publish-brand-template](https://www.canva.dev/docs/apps/mcp/tools/publish-brand-template/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


