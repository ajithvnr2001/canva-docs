---
url: https://www.canva.dev/docs/apps/rest-apis/changelog/
title: Changelog - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:14.654610+00:00
---

# Changelog - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/changelog/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

API reference

[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)

App UI Kit reference

[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

Canva REST API reference

[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)

Webhooks notification reference

[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

Tools

[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)

# Changelog

Copy page

### October 19, 2026

  * The [Create asset upload job via URL⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/create-url-asset-upload-job/) and [Get asset upload job via URL⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/get-url-asset-upload-job/) APIs are no longer in preview, and are now generally available.



### October 1, 2026

  * New preview APIs are available: [Create image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/create-image-generation-job/) and [Get image generation job](https://www.canva.dev/docs/apps/rest-apis/reference/generations/get-image-generation-job/). These APIs let you generate an image from a text prompt, and optionally save it to the user's Canva account as an image asset. Starting a job consumes the user's [AI credit allowance⁠(opens in a new tab or window)](https://www.canva.com/help/ai-access/).



### September 29, 2026

  * New preview APIs are available: [Create design generation job API](https://www.canva.dev/docs/apps/rest-apis/reference/generations/create-design-generation-job/) and [Get design generation job API](https://www.canva.dev/docs/apps/rest-apis/reference/generations/get-design-generation-job/). These APIs let you generate a Canva document or presentation from a text brief.



### September 23, 2026

  * Chart data fields and autofilling a video (returned by the [Get brand template dataset API](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/get-brand-template-dataset/)) are no longer in preview, and are now generally available.



### September 21, 2026

  * The [Autofill APIs](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/) are now available to apps acting on behalf of users on a Canva Pro or Canva Teams plan, in addition to Canva Enterprise.
  * New preview APIs are available: [Create image-to-design import job](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/create-image-to-design-import-job/) and [Get image-to-design import job](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/get-image-to-design-import-job/). These APIs let you convert an image already in a user's Canva account into an editable design using Magic Layers.



### September 18, 2026

  * When using the [Create design export job API](https://www.canva.dev/docs/apps/rest-apis/reference/exports/create-design-export-job/) to export a design as an MP4, the `quality` parameter is now a target number of pixels rather than a fixed output size. The exported video keeps the design's own aspect ratio, so a design whose aspect ratio doesn't match the requested quality is no longer letterboxed into it.

For example, exporting a square design as `vertical_4k` previously produced a 2160x2160 video; it now produces a 2880x2880 video, matching the same design downloaded from the Canva editor at the equivalent quality. Because the aspect ratio now follows the design, the `horizontal` and `vertical` values of a given resolution produce the same output — a 2160x3840 portrait design exported as `horizontal_4k` is 2160x3840, not 3840x2160.

We made this change without creating a new API version because the previous behavior was a bug: videos exported through the API had noticeably fewer pixels than the same design downloaded from the Canva editor.




### September 17, 2026

  * The [Get design dataset API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-dataset/) and [Get brand template dataset API](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/get-brand-template-dataset/) now return `sheet` data fields for autofillable tabular sheet data.
  * New preview APIs are available: [Create image transformation job](https://www.canva.dev/docs/apps/rest-apis/reference/image-transformations/create-image-transformation-job/) and [Get image transformation job](https://www.canva.dev/docs/apps/rest-apis/reference/image-transformations/get-image-transformation-job/). These APIs let you apply transformations, such as background removal, to an image asset, producing a new image asset. Starting a job consumes the user's [AI credit allowance⁠(opens in a new tab or window)](https://www.canva.com/help/ai-access/).



### August 25, 2026

  * The `create_from_design` and `update_design` job types, and the `chart`, `sheet`, and `video` data field types, for the [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) are no longer in preview, and are now generally available.
  * The [Get design dataset API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-dataset/) is no longer in preview, and is now generally available.



### August 12, 2026

  * Previously, the [Get asset API⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/get-asset/) returned a `500 Internal Server Error` for image assets that didn't have a title or an import filename. This issue has been fixed, and the API now returns the asset with an empty `name`.
  * Previously, the [List folder items API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) returned a `500 Internal Server Error` when a folder contained an image that didn't have a title or an import filename. This issue has been fixed, and the API now returns the image with an empty `name`.
  * The [Get folder API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/get-folder/), [Delete folder API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/delete-folder/), and [Move folder item API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/move-folder-item/) now return a `400` error with the `invalid_field` code when the supplied folder ID isn't a valid folder ID. These requests previously returned a `500` error.



### August 10, 2026

  * You can now autofill an existing design in place. The [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) now supports an `update_design` value for `type` that updates the specified design directly, instead of creating a new one. This is currently a [preview feature](https://www.canva.dev/docs/apps/rest-apis/#preview-apis).



### July 10, 2026

  * The `design_types` field on `Design` responses and the `design_type` field on `DesignPage` are now out of preview and included in every response.



### June 29, 2026

  * New preview APIs are available: [Get design analytics](https://www.canva.dev/docs/apps/rest-apis/reference/analytics/get-design-analytics/), [Get design analytics viewers](https://www.canva.dev/docs/apps/rest-apis/reference/analytics/get-design-analytics-viewers/), [Get design analytics views over time](https://www.canva.dev/docs/apps/rest-apis/reference/analytics/get-design-analytics-views-over-time/), [Get design analytics page views](https://www.canva.dev/docs/apps/rest-apis/reference/analytics/get-design-analytics-page-views/), and [Get design analytics links](https://www.canva.dev/docs/apps/rest-apis/reference/analytics/get-design-analytics-links/). These APIs let you retrieve engagement metrics for a design shared via Canva.



### June 25, 2026

  * You can now autofill a new design from an existing design that contains autofill data fields. The new [Get design dataset API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-dataset/) returns the data field names and types for a design, and the [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) now supports a `create_from_design` value for `type` that uses those fields to create the autofilled design. Both are currently [preview features](https://www.canva.dev/docs/apps/rest-apis/#preview-apis).



### June 22, 2026

  * The [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) now accepts `video` data values, letting you autofill an image data field with a video asset. Autofilling a video is currently a [preview feature](https://www.canva.dev/docs/apps/rest-apis/#preview-apis).



### June 16, 2026

  * The [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) now accepts a `type` field to support future functionality for different autofill sources. The first supported value is `create_from_brand_template`, which is the existing functionality for creating new designs from a brand template. For backwards compatibility, requests that omit `type` continue to work as before.



### June 12, 2026

  * `Design` responses now include a `design_types` field, and `DesignPage` responses now include a `design_type` field. These indicate the type of content a design or page contains, such as `doc` or `presentation`. The value `unknown` is returned when the type cannot be determined. This list may be extended in the future, so ensure unrecognized values are handled gracefully.



### June 11, 2026

  * The preview [Get design pages API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-pages/#success-response) now returns an `id` for each page, which can be used to correlate pages with per-page data from other APIs.



### June 9, 2026

  * The [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) now accepts data values for `sheet` data fields, which lets you autofill tabular data for sheet elements. Sheet data fields are currently a [preview feature](https://www.canva.dev/docs/apps/rest-apis/#preview-apis).



### June 4, 2026

  * The [Publish brand template API](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/publish-brand-template/) is now available as a preview. It publishes a design as a brand template, creating a new brand template or updating an existing one if the design is a draft of an existing template.
  * The [Get design export formats API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-export-formats/) now returns page-level format options. Each format includes the `page_numbers` that support it. If a format is supported by every page in the design, its `page_numbers` are omitted.



### June 3, 2026

  * The [List folder items API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) now supports `brand_template` as an item type. Brand templates in folders are returned in the response and can be filtered using the `item_types` parameter.



### May 27, 2026

  * The preview [Get design pages API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-pages/) now returns a `page_number` property on each page, which is a replacement for the now-deprecated `index` property. The two properties always return the same value. The `index` property will be removed in a future release after existing apps have migrated; new apps should use `page_number` instead.



### May 14, 2026

  * The [Create design API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/create-design/) now supports two new creation modes: copying an existing design using `type: design`, and creating a design from a brand template using `type: brand_template`. Both creation modes are currently a [preview feature](https://www.canva.dev/docs/apps/rest-apis/#preview-apis).



### May 12, 2026

  * The [Create design export job API](https://www.canva.dev/docs/apps/rest-apis/reference/exports/create-design-export-job/) now supports CSV export using the `csv` export file type. Only Canva Sheets designs can be exported as CSV.
  * New preview APIs are available: [Create design merge job](https://www.canva.dev/docs/apps/rest-apis/reference/merges/create-design-merge-job/) and [Get design merge job](https://www.canva.dev/docs/apps/rest-apis/reference/merges/get-design-merge-job/). These APIs let you merge design pages by inserting, moving, or deleting pages to create a new design or modify an existing one.



### March 30, 2026

  * The [Create design API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/create-design/#body-parameters) now supports `email` in the `name` field for `preset` types.



### March 26, 2026

  * A new `type` request parameter has been added to the [Create design API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/create-design/). Although this type is shown as required, for backward compatibility, if it isn't provided in a request, the request type will be assumed to be `type_and_asset`.



### March 25, 2026

  * The [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) now supports `column_configs` for chart data fields, allowing you to define column names and data types separately from your data.

  * The [Create design export job API](https://www.canva.dev/docs/apps/rest-apis/reference/exports/create-design-export-job/) now supports two additional email export formats: `html_bundle` and `html_standalone`.

Use these formats when creating export jobs for email designs, depending on whether you need bundled assets (`html_bundle`) or a standalone HTML output (`html_standalone`).




### March 2, 2026

  * The [Assets APIs⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/) now return an additional `metadata` property as part of the `asset` object.



### February 26, 2026

  * The [List folder items API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) now supports a `pin_status` parameter to filter for pinned items in a folder.



### February 19, 2026

  * The [Get design pages API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-pages/#success-response) now returns page dimensions for pages in bounded designs (unbounded designs like whiteboards and Canva Docs will not have page dimensions).



### January 8, 2026

  * The [Get design export formats API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-export-formats/) is no longer in preview, and is now generally available.



### January 5, 2026

  * The [List brand templates API](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/list-brand-templates/) now supports an optional `limit` parameter to control the number of brand templates returned per request.



### December 2, 2025

  * The [List folder items API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) now supports a `limit` parameter to control the number of folder items returned per request.



### October 20, 2025

  * The [List designs API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/list-designs/) now supports a `limit` parameter to control the number of designs returned per request.



### August 11, 2025

  * The [folders API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/) now lets you reference a user's Uploads folder using `uploads` as the folder ID.



### July 2, 2025

  * New preview APIs are available: [Create asset upload job via URL⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/create-url-asset-upload-job/) and [Get asset upload job via URL⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/get-url-asset-upload-job/). These APIs let you upload an asset to Canva from a URL.



### June 24, 2025

  * The [URL import job APIs](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/create-url-import-job/) are no longer in preview, and are now generally available. These APIs let you import a file from a publicly accessible URL as a new design in Canva.



### June 19, 2025

  * Video file support in the [Assets APIs⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/) is now out of preview and is generally available. For more information see the [Assets API overview⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/#videos).
  * The [design Resize APIs](https://www.canva.dev/docs/apps/rest-apis/reference/resizes/) are no longer in preview, and are now generally available. These APIs let you to create a resized copy of a design in Canva.
  * The [Get user capabilities API](https://www.canva.dev/docs/apps/rest-apis/reference/users/get-user-capabilities/) is no longer in preview, and is now generally available. This API lists the capabilities for the user account associated with the provided access token.



### May 12, 2025

  * A new restriction has been added to the following preview APIs, limiting messages to a maximum of 2048 characters:

    * [Create thread](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-thread/)
    * [Create reply](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-reply/).



### March 26, 2025

  * New preview APIs are available: [Create design resize job](https://www.canva.dev/docs/apps/rest-apis/reference/resizes/create-design-resize-job/) and [Get design resize job](https://www.canva.dev/docs/apps/rest-apis/reference/resizes/get-design-resize-job/). These APIs let you to create a resized copy of a design in Canva.



### March 19, 2025

  * In [Suggestion](https://www.canva.dev/docs/apps/rest-apis/webhooks/suggestion-notification/) webhook notifications, the `format` property in a formatting `suggested_edits` item can now have the values of `font_size_modifier` and `vertical_align`.



### March 17, 2025

  * The preview [Comment notification](https://www.canva.dev/docs/apps/rest-apis/webhooks/comment-notification/) webhook event now returns details about the comment event in a new `comment_event` object. The existing `comment_url` property and `comment` object are now deprecated.



### February 24, 2025

  * A new preview API is available: [Create reply](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-reply/). This API lets you create a reply to a comment or suggestion thread, and should be used instead of the removed Create reply deprecated API.



### February 20, 2025

  * A new preview API is available: [Create thread](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-thread/). This API lets you create a new comment thread, and should be used instead of the now deprecated [Create comment](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-comment/) API.



### February 19, 2025

  * The [Create design export job API](https://www.canva.dev/docs/apps/rest-apis/reference/exports/create-design-export-job/) now includes a `transparent_background` parameter when exporting PNG images. This allows you to specify whether the exported image should have a transparent background, and is only available to users on paid Canva plans.



### February 18, 2025

  * The [Get thread](https://www.canva.dev/docs/apps/rest-apis/reference/comments/get-thread/), [Get reply](https://www.canva.dev/docs/apps/rest-apis/reference/comments/get-reply/) and [List replies](https://www.canva.dev/docs/apps/rest-apis/reference/comments/list-replies/) APIs now support the suggestion type.



### February 17, 2025

  * In some situations, the `created_at` and `updated_at` properties for brand templates were incorrectly being returned as milliseconds. This has been fixed, so `created_at` and `updated_at` brand template properties now consistently represent seconds since the UNIX epoch.



### February 12, 2025

  * A new preview API is available: [List replies](https://www.canva.dev/docs/apps/rest-apis/reference/comments/list-replies/). This API lets you retrieve a list of replies to a comment thread.



### January 17, 2025

  * A new preview API is available: [Get reply](https://www.canva.dev/docs/apps/rest-apis/reference/comments/get-reply/). This API lets you retrieve a reply to a comment thread and replaces the overloaded use of the Get comment API for this purpose.
  * The preview Get comment API has been renamed to [Get thread](https://www.canva.dev/docs/apps/rest-apis/reference/comments/get-thread/). It now returns a comment thread in a new `thread` object, and the existing `comment` object is now deprecated. Using the [Get thread](https://www.canva.dev/docs/apps/rest-apis/reference/comments/get-thread/) API to retrieve a reply to a comment thread is now deprecated in favor of using the new dedicated preview [Get reply](https://www.canva.dev/docs/apps/rest-apis/reference/comments/get-reply/) API.
  * In [Suggestion](https://www.canva.dev/docs/apps/rest-apis/webhooks/suggestion-notification/) webhook notifications, the `format` property in a formatting `suggested_edits` item can now have the value `background_color`.



### January 15, 2025

  * New preview APIs are available: [Create URL import job](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/create-url-import-job/) and [Get URL import job](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/get-url-import-job/). These APIs let you import a file from a publicly accessible URL as a new design in Canva.



### January 8, 2025

  * For the preview [Get comment](https://www.canva.dev/docs/apps/rest-apis/reference/comments/get-thread/) API, if a user is mentioned in a comment and their Canva user account is later deleted, any mentions of deleted users are now returned as `[]`.



### January 7, 2025

  * Previously, passing an empty design ID to the [Create design export job API](https://www.canva.dev/docs/apps/rest-apis/reference/exports/create-design-export-job/) would result in a `500 Internal Server Error`. This issue has been fixed, and passing an empty design ID now returns `400 Bad Request` with the message `'design_id' must not be blank`.



### December 17, 2024

  * The preview [Suggestion notification](https://www.canva.dev/docs/apps/rest-apis/webhooks/suggestion-notification/) webhook event now contains a suggestion thread that can include multiple suggested edits in a single suggestion.



### December 2, 2024

  * The [Assets APIs⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/) now support video files. Support for video assets is currently provided as a [preview feature](https://www.canva.dev/docs/apps/rest-apis/#preview-apis). For a list of supported file types, see the [Assets API overview⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/#videos).



### November 29, 2024

  * The [Folder access requested](https://www.canva.dev/docs/apps/rest-apis/webhooks/folder-access-requested-notification/) webhook event now returns a `FolderSummary` object type instead of `Folder`. We've also fixed an issue where the `created_at` and `updated_at` timestamps for a folder were incorrectly returned as milliseconds since the UNIX epoch. These timestamps now correctly represent seconds since the UNIX epoch.



### November 22, 2024

  * The [Share folder](https://www.canva.dev/docs/apps/rest-apis/webhooks/share-folder-notification/) webhook event now includes `created_at` and `updated_at` timestamps for a folder. Also, the folder `name` property has been added, which should be used instead of the now-deprecated `title` property.



### November 12, 2024

  * The [Autofill APIs](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/) now return a `page_count` property for multi-page designs in a successful job.
  * The [Design import APIs](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/) now return a `page_count` property for multi-page designs in a successful job.
  * The [List folder items API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) now returns a `page_count` property for all multi-page designs in the requested folder.
  * Webhook notification events now return a `page_count` property in the design summary for all multi-page designs.



### October 25, 2024

  * A new preview API is available: [Get design export formats](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-export-formats/). This API lets you retrieve a list of supported file formats that can be used to export a design.



### October 23, 2024

  * Webhook notification events for suggestions (suggested edits in a Canva Doc) are now sent to apps that have notifications enabled. See [Suggestion notifications](https://www.canva.dev/docs/apps/rest-apis/webhooks/suggestion-notification/) for details.



### October 11, 2024

  * A new preview API is available: [Get design pages](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-pages/). This API lets you retrieve per-page metadata, which currently includes page-specific thumbnails.



### September 19, 2024

  * The [Design import APIs](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/) are no longer in preview, and are now generally available.

  * The [Folders APIs](https://www.canva.dev/docs/apps/rest-apis/reference/folders/) are no longer in preview, and are now generally available.




### September 18, 2024

  * The [List brand templates API](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/list-brand-templates/) now supports an optional `dataset` query parameter. This can be used to filter results to only include brand templates with or without data fields defined (for use with the [Autofill APIs](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/)).



### September 17, 2024

  * The [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) now accepts data values for `chart` data fields, which lets you autofill tabular data for chart elements. Chart data fields are currently a [preview feature](https://www.canva.dev/docs/apps/rest-apis/#preview-apis).
  * The [Get brand template dataset API](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/get-brand-template-dataset/) now returns `chart` data fields for brand templates which contain chart elements. Chart elements and data fields in brand templates are created using the **Data autofill** app. Chart data fields are currently a [preview feature](https://www.canva.dev/docs/apps/rest-apis/#preview-apis).
  * The responses for the preview [Design import APIs](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/) have been revised to align with the response formats used by our other asynchronous job APIs.



### September 11, 2024

  * Previously, the `created_at` property in the preview feature for webhook payloads was incorrectly returned as milliseconds since the UNIX epoch. This has been fixed, so `created_at` now correctly represents seconds since the UNIX epoch.



### September 5, 2024

  * The [Designs APIs](https://www.canva.dev/docs/apps/rest-apis/reference/designs/) now return a `page_count` property.

  * When using the [Create design export job API](https://www.canva.dev/docs/apps/rest-apis/reference/exports/create-design-export-job/) to export designs as a PNG, the `lossless` parameter is now set to `true` by default.

We made this change to the default value without creating a new API version because the previous behavior was a bug that significantly affected the user experience. Lossy PNG compression is a premium feature, and under the previous default value for the parameter, users on the Canva Free plan could not export to PNG.

  * The [List folder items](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) preview API now returns `image` instead of `asset`. The `asset` option in the `item_types` filter has also been replaced with `image`.




### September 4, 2024

  * For the [List folder items](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) preview API, the response for the `design` object type no longer includes `owner` information.

  * The [List folder items](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) preview API no longer accepts `template` as query parameter for `item_types`, and no longer returns `template` or `brand_template` item types in the response.

  * In the [Move folder item](https://www.canva.dev/docs/apps/rest-apis/reference/folders/move-folder-item/) preview API, the `from_folder_id` parameter has been removed.




### August 23, 2024

  * The [Assets APIs⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/rest-apis/reference/assets/) now return an additional `type` property as part of the `asset` object. Currently, `type` can only have the value of `image`, but more asset types are being added in future updates.



### August 22, 2024

  * The [Autofill APIs](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/) now return `created_at` and `updated_at` timestamps in the design summary for jobs with a `success` status. Temporary `urls` for viewing or editing the design have also been added to the response.



### August 16, 2024

  * The [Brand template APIs](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/) now return `created_at` and `updated_at` timestamps for all brand templates.
  * The [Designs APIs](https://www.canva.dev/docs/apps/rest-apis/reference/designs/) now return `created_at` and `updated_at` timestamps for all returned designs.
  * The [Get design import job API](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/get-design-import-job/) now returns `created_at` and `updated_at` timestamps for designs imported using the [Create design import job API](https://www.canva.dev/docs/apps/rest-apis/reference/design-imports/create-design-import-job/).
  * The [List folder items API](https://www.canva.dev/docs/apps/rest-apis/reference/folders/list-folder-items/) now returns `created_at` and `updated_at` timestamps for all designs in the requested folder.



### July 8, 2024

  * The [Autofill APIs](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/) are no longer in preview, and are now generally available.
  * The [Brand template APIs](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/) are no longer in preview, and are now generally available.



### June 18, 2024

**New API version: 2024-06-18**

  * Initial release of the Connect APIs.


