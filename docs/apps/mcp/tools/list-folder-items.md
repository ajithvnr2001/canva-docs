---
url: https://www.canva.dev/docs/apps/mcp/tools/list-folder-items/
title: list-folder-items - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:09.764507+00:00
---

# list-folder-items - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/list-folder-items/

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

# list-folder-items

Browse the designs, folders, and images inside a Canva folder.

Copy page

Use `list-folder-items` to review what a folder contains, locate an item in a known folder, or check its contents before reorganizing. If you don't know the folder yet, find it with [search-folders](https://www.canva.dev/docs/apps/mcp/tools/search-folders/) first.

## Example prompt

_"What's in my 'Q3 campaign' folder? Just the designs, newest first."_

Pass the `folder_id` (use `"root"` for the top level). Optionally filter with `item_types` (`design`, `folder`, `image`) and order the results with `sort_by` (for example `modified_descending`).

## Example response

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.
    
    
    {
    
      "items": [
    
        {
    
          "type": "folder",
    
          "folder": {
    
            "id": "FOLDER_EXAMPLE",
    
            "name": "Assets",
    
            "created_at": 1758000000,
    
            "updated_at": 1758000000
    
          }
    
        },
    
        {
    
          "type": "design",
    
          "design": {
    
            "id": "DAF_EXAMPLE",
    
            "title": "Q3 launch deck",
    
            "urls": {
    
              "edit_url": "https://www.canva.com/d/EXAMPLE_EDIT",
    
              "view_url": "https://www.canva.com/d/EXAMPLE_VIEW"
    
            },
    
            "created_at": 1758000000,
    
            "updated_at": 1758000000,
    
            "page_count": 12
    
          }
    
        },
    
        {
    
          "type": "image",
    
          "image": {
    
            "type": "image",
    
            "id": "ASSET_EXAMPLE",
    
            "name": "Hero photo",
    
            "tags": ["campaign"],
    
            "created_at": 1758000000,
    
            "updated_at": 1758000000,
    
            "thumbnail": {
    
              "width": 595,
    
              "height": 335,
    
              "url": "https://document-export.canva.com/EXAMPLE_THUMBNAIL"
    
            }
    
          }
    
        }
    
      ],
    
      "continuation": "EXAMPLE_TOKEN"
    
    }

JSON

Copy

Each item has a `type` and a matching `folder`, `design`, or `image` object that carries the item's `id`. If the response includes a `continuation` token, pass it back unchanged with the same `folder_id` to get the next page; if it's absent, there are no more items.

Thumbnail URLs expire after 15 minutes. Use them immediately, and don't store or share them.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [search-folders](https://www.canva.dev/docs/apps/mcp/tools/search-folders/)
  * [create-folder](https://www.canva.dev/docs/apps/mcp/tools/create-folder/)
  * [move-item-to-folder](https://www.canva.dev/docs/apps/mcp/tools/move-item-to-folder/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


