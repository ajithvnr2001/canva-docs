---
url: https://www.canva.dev/docs/apps/mcp/tools/create-upload-url/
title: create-upload-url - Tools - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:08.183442+00:00
---

# create-upload-url - Tools - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/mcp/tools/create-upload-url/

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

# create-upload-url

Get a single-use URL for uploading a file to Canva.

Copy page

Use `create-upload-url` to upload a file that your AI application has the bytes for, such as a chat attachment, a local file, or generated content. The tool supports images, videos, PDFs, and other documents. For a small image or video file that's already at a public URL, use [upload-asset-from-url](https://www.canva.dev/docs/apps/mcp/tools/upload-asset-from-url/) instead.

Uploading a file takes two steps:

  1. Call `create-upload-url` to get an `uploadUrl`.
  2. Send the file's raw bytes as the body of a single HTTP `POST` request to the `uploadUrl`, with the header `Content-Type: application/octet-stream`. Don't use a multipart form, base64 encoding, or a JSON wrapper.



## Example prompt

_"Upload this logo to my Canva account."_

The tool takes no parameters.

## Example responses

IDs, URLs, and tokens below are placeholders; field names and structure are exactly as returned.

The tool returns the upload URL and HTTP method:
    
    
    {
    
      "uploadUrl": "https://www.canva.com/_blob/upload/ingress/upload/file/agent-tool?_sat=EXAMPLE_TOKEN",
    
      "httpMethod": "POST",
    
      "resultNote": "The upload response contains resource IDs for the uploaded file; pass them to other Canva tools to reference the file."
    
    }

JSON

Copy

The response to the `POST` request contains the ID of the uploaded file. The ID's name depends on the file type: `mediaId` for images, `videoId` for videos, and `fileId` for documents, such as PDFs.
    
    
    {
    
      "mediaId": "MEDIA_EXAMPLE"
    
    }

JSON

Copy

Pass the ID to other tools to reference the file, such as in `imageReferences` for [generate-image](https://www.canva.dev/docs/apps/mcp/tools/generate-image/).

Each upload URL allows exactly one upload and expires after a short time. If the URL has been used, has expired, or the upload was rejected, call `create-upload-url` again for a new URL. Never retry a used or expired URL.

## Learn more

  * [MCP tools and rate limits](https://www.canva.dev/docs/apps/mcp/tools/)
  * [upload-asset-from-url](https://www.canva.dev/docs/apps/mcp/tools/upload-asset-from-url/)
  * [Verify your Canva MCP app](https://www.canva.dev/docs/apps/mcp/verify-app/)


