---
url: https://www.canva.dev/docs/apps/mcp/tools/get-assets/
title: get-assets - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:08.370249+00:00
---

# get-assets - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/get-assets/

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

# get-assets

Get names, tags, types, and thumbnails for images and videos used in a design.

Copy page

Use `get-assets` to look up the images or videos on a page, for example to work out which one the user means before changing it. Asset IDs come from the `fills` returned by [start-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/start-editing-transaction/).

## Example prompt

_"Which of the photos on slide 3 is the team photo? Swap that one out."_

Pass `asset_ids`, an array of image or video IDs.

## Example response

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.

The result is a list of content blocks rather than one JSON value. For each requested ID, in the order you supplied them, there's a text block holding that asset's JSON, followed by an image block with the asset itself when the lookup succeeded. A request for two IDs where the second can't be found returns three blocks:

  1. A text block for the first ID:
         
         {
         
           "asset": {
         
             "type": "image",
         
             "id": "ASSET_EXAMPLE_1",
         
             "name": "Team photo",
         
             "tags": ["team", "offsite"],
         
             "created_at": 1758000000,
         
             "updated_at": 1758000000,
         
             "owner": { "user_id": "USER_EXAMPLE", "team_id": "TEAM_EXAMPLE" },
         
             "thumbnail": {
         
               "width": 595,
         
               "height": 335,
         
               "url": "https://document-export.canva.com/EXAMPLE_THUMBNAIL"
         
             },
         
             "import_status": { "state": "success" },
         
             "metadata": { "type": "image", "width": 1920, "height": 1080, "smart_tags": ["people", "outdoors"] }
         
           }
         
         }

JSON

Copy

  2. An image block containing the first asset's image data.

  3. A text block for the second ID:
         
         { "error": { "code": "asset_not_found", "message": "<human-readable description>" } }

JSON

Copy




`asset.type` is `image` or `video`, and `metadata` carries the dimensions (and `duration` for videos) when available. The call succeeds as a whole even if individual assets fail, so check each text block.

Thumbnail URLs expire after 15 minutes. Use them immediately, and don't store or share them.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [start-editing-transaction](https://www.canva.dev/docs/apps/mcp/tools/start-editing-transaction/)
  * [perform-editing-operations](https://www.canva.dev/docs/apps/mcp/tools/perform-editing-operations/)
  * [upload-asset-from-url](https://www.canva.dev/docs/apps/mcp/tools/upload-asset-from-url/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


