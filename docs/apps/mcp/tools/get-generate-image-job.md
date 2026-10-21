---
url: https://www.canva.dev/docs/apps/mcp/tools/get-generate-image-job/
title: get-generate-image-job - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:09.237007+00:00
---

# get-generate-image-job - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/get-generate-image-job/

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

# get-generate-image-job

Check the status of an image generation job and get the generated image.

Copy page

Use `get-generate-image-job` to poll a job started by [generate-image](https://www.canva.dev/docs/apps/mcp/tools/generate-image/).

## Example prompt

_"Is my image ready yet?"_

Pass the `jobId` that `generate-image` returned.

## Example responses

IDs below are placeholders; field names and structure are exactly as returned.
    
    
    {
    
      "status": "SUCCESS",
    
      "result": {
    
        "results": [ { "type": "MEDIA", "id": "MEDIA_EXAMPLE", "version": "1" } ]
    
      }
    
    }

JSON

Copy

A `status` of `SUCCESS` returns the generated image as a `MEDIA` reference in `result.results`. Use its `id` to refer to the image in other tools, such as in `imageReferences` when editing the image with `generate-image`.

While the job runs, the response is `{ "status": "PENDING" }`. Continue polling with the same `jobId` until the `status` is `SUCCESS` or `FAILURE`. Don't start a new generation job just because the existing one is still pending.

If the job fails, the response contains a `failureType` and `failureMessage`:
    
    
    {
    
      "status": "FAILURE",
    
      "failureType": "SERVER_GENERIC",
    
      "failureMessage": "Something went wrong while generating the image. Please try again."
    
    }

JSON

Copy

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [generate-image](https://www.canva.dev/docs/apps/mcp/tools/generate-image/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


