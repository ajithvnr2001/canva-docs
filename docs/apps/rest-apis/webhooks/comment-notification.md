---
url: https://www.canva.dev/docs/apps/rest-apis/webhooks/comment-notification/
title: Comment notifications - Webhooks notification reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:41.466494+00:00
---

# Comment notifications - Webhooks notification reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/webhooks/comment-notification/

Webhooks notification reference

[Overview](https://www.canva.dev/docs/apps/rest-apis/webhooks/)

Access

[Design access requested](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-access-requested-notification/)[Folder access requested](https://www.canva.dev/docs/apps/rest-apis/webhooks/folder-access-requested-notification/)[Team invite](https://www.canva.dev/docs/apps/rest-apis/webhooks/team-invite-notification/)

Approvals

[Design approval requested](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-approval-requested-notification/)[Design approval response](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-approval-response-notification/)[Design approval reviewer invalidated](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-approval-reviewer-invalidated-notification/)

Collaborating

[Comment](https://www.canva.dev/docs/apps/rest-apis/webhooks/comment-notification/)[Suggestion](https://www.canva.dev/docs/apps/rest-apis/webhooks/suggestion-notification/)

Sharing

[Share design](https://www.canva.dev/docs/apps/rest-apis/webhooks/share-design-notification/)[Share folder](https://www.canva.dev/docs/apps/rest-apis/webhooks/share-folder-notification/)

# Comment notifications

The NotificationContent sent when a user comments on a design.

Copy page

Webhook notifications are currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview features won't produce a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/).
  * Public apps that use preview features will not pass the review process, and can't be made available to all Canva users.



This webhook isn't triggered for a user's own comments, as users don't receive notifications for their own comments in Canva.

If the `type` of [notification](https://www.canva.dev/docs/apps/rest-apis/webhooks/#notification) is `comment`, the webhook payload object contains the following parameters:

`id``string`

The unique identifier for the notification.

`created_at``integer`

When the notification was created, as a UNIX timestamp (in seconds since the UNIX epoch).

`content``object`

The notification content for when someone comments on a design.

Properties of **content**

`type``string`

**Available values:** The only valid value is `comment`.

`triggering_user``User`

Metadata for the user, consisting of the User ID and display name.

Properties of **triggering_user**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`receiving_team_user``TeamUser`

Metadata for the user, consisting of the User ID, Team ID, and display name.

Properties of **receiving_team_user**

`user_id``string`

Optional

The ID of the user.

`team_id``string`

Optional

The ID of the user's Canva Team.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`design``DesignSummary`

Basic details about the design, such as the design's ID, title, and URL.

Properties of **design**

`id``string`

The design ID.

`urls``DesignLinks`

A temporary set of URLs for viewing or editing the design.

Properties of **urls**

`edit_url``string`

A temporary editing URL for the design. This URL is only accessible to the user that made the API request, and is designed to support [return navigation](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/) workflows.

This is not a permanent URL, it is only valid for 30 days.

`view_url``string`

A temporary viewing URL for the design. This URL is only accessible to the user that made the API request, and is designed to support [return navigation](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/) workflows.

This is not a permanent URL, it is only valid for 30 days.

`created_at``integer`

When the design was created in Canva, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the design was last updated in Canva, as a Unix timestamp (in seconds since the Unix Epoch).

`title``string`

Optional

The design title.

`url``string`

Optional

URL of the design.

`thumbnail``Thumbnail`

Optional

A thumbnail image representing the object.

Properties of **thumbnail**

`width``integer`

The width of the thumbnail image in pixels.

`height``integer`

The height of the thumbnail image in pixels.

`url``string`

A URL for retrieving the thumbnail image. This URL expires after 15 minutes. This URL includes a query string that's required for retrieving the thumbnail.

`page_count``integer`

Optional

The total number of pages in the design. Some design types don't have pages (for example, Canva docs).

`comment_event``CommentEvent`

Optional

The type of comment event, including additional type-specific properties.

newnew

assignedassigned

resolvedresolved

replyreply

mentionmention

Event type for a new comment thread.

`type``string`

**Available values:** The only valid value is `new`.

`comment_url``string`

A URL to the design, focused on the comment thread.

`comment``Thread`

A discussion thread on a design.

The `type` of the thread can be found in the `thread_type` object, along with additional type-specific properties. The `author` of the thread might be missing if that user account no longer exists.

Properties of **comment**

`id``string`

The ID of the thread.

You can use this ID to create replies to the thread using the [Create reply API](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-reply/).

`design_id``string`

The ID of the design that the discussion thread is on.

`thread_type``ThreadType`

The type of the discussion thread, along with additional type-specific properties.

commentcomment

suggestionsuggestion

A comment thread.

`type``string`

**Available values:** The only valid value is `comment`.

`content``CommentContent`

The content of a comment thread or reply.

Properties of **content**

`plaintext``string`

The content in plaintext. Any user mention tags are shown in the format `[user_id:team_id]`.

`markdown``string`

Optional

The content in markdown. Any user mention tags are shown in the format `[user_id:team_id]`

`mentions``object`

The Canva users mentioned in the comment thread or reply.

Properties of **mentions**

`<KEY>``object of UserMentions`

Information about the user mentioned in a comment thread or reply. Each user mention is keyed using the user's user ID and team ID separated by a colon (`user_id:team_id`).
    
    
    {
    
      "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP": {
    
        "tag": "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP",
    
        "user": {
    
          "user_id": "oUnPjZ2k2yuhftbWF7873o",
    
          "team_id": "oBpVhLW22VrqtwKgaayRbP",
    
          "display_name": "John Doe"
    
        }
    
      }
    
    }

JSON

Copy

`tag``string`

The mention tag for the user mentioned in the comment thread or reply content. This has the format of the user's user ID and team ID separated by a colon (`user_id:team_id`).

`user``TeamUser`

Metadata for the user, consisting of the User ID, Team ID, and display name.

Properties of **user**

`user_id``string`

Optional

The ID of the user.

`team_id``string`

Optional

The ID of the user's Canva Team.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`assignee``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **assignee**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`resolver``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **resolver**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

A suggestion thread.

`type``string`

**Available values:** The only valid value is `suggestion`.

`suggested_edits``SuggestedEdit[]`

The type of the suggested edit, along with additional type-specific properties.

**Minimum items:** `1`

addadd

deletedelete

formatformat

A suggestion to add some text.

`type``string`

**Available values:** The only valid value is `add`.

`text``string`

A suggestion to delete some text.

`type``string`

**Available values:** The only valid value is `delete`.

`text``string`

A suggestion to format some text.

`type``string`

**Available values:** The only valid value is `format`.

`format``string`

The suggested format change.

**Available values:**

  * `font_family`
  * `font_size`
  * `font_weight`
  * `font_style`
  * `color`
  * `background_color`
  * `decoration`
  * `strikethrough`
  * `link`
  * `letter_spacing`
  * `line_height`
  * `direction`
  * `text_align`
  * `list_marker`
  * `list_level`
  * `margin_inline_start`
  * `text_indent`
  * `font_size_modifier`
  * `vertical_align`



`status``string`

The current status of the suggestion.

**Available values:**

  * `open`: A suggestion was made, but it hasn't been accepted or rejected yet.
  * `accepted`: A suggestion was accepted and applied to the design.
  * `rejected`: A suggestion was rejected and not applied to the design.



`created_at``integer`

When the thread was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the thread was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`author``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **author**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

Event type for a comment thread that has been assigned.

`type``string`

**Available values:** The only valid value is `assigned`.

`comment_url``string`

A URL to the design, focused on the comment thread.

`comment``Thread`

A discussion thread on a design.

The `type` of the thread can be found in the `thread_type` object, along with additional type-specific properties. The `author` of the thread might be missing if that user account no longer exists.

Properties of **comment**

`id``string`

The ID of the thread.

You can use this ID to create replies to the thread using the [Create reply API](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-reply/).

`design_id``string`

The ID of the design that the discussion thread is on.

`thread_type``ThreadType`

The type of the discussion thread, along with additional type-specific properties.

commentcomment

suggestionsuggestion

A comment thread.

`type``string`

**Available values:** The only valid value is `comment`.

`content``CommentContent`

The content of a comment thread or reply.

Properties of **content**

`plaintext``string`

The content in plaintext. Any user mention tags are shown in the format `[user_id:team_id]`.

`markdown``string`

Optional

The content in markdown. Any user mention tags are shown in the format `[user_id:team_id]`

`mentions``object`

The Canva users mentioned in the comment thread or reply.

Properties of **mentions**

`<KEY>``object of UserMentions`

Information about the user mentioned in a comment thread or reply. Each user mention is keyed using the user's user ID and team ID separated by a colon (`user_id:team_id`).
    
    
    {
    
      "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP": {
    
        "tag": "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP",
    
        "user": {
    
          "user_id": "oUnPjZ2k2yuhftbWF7873o",
    
          "team_id": "oBpVhLW22VrqtwKgaayRbP",
    
          "display_name": "John Doe"
    
        }
    
      }
    
    }

JSON

Copy

`tag``string`

The mention tag for the user mentioned in the comment thread or reply content. This has the format of the user's user ID and team ID separated by a colon (`user_id:team_id`).

`user``TeamUser`

Metadata for the user, consisting of the User ID, Team ID, and display name.

Properties of **user**

`user_id``string`

Optional

The ID of the user.

`team_id``string`

Optional

The ID of the user's Canva Team.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`assignee``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **assignee**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`resolver``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **resolver**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

A suggestion thread.

`type``string`

**Available values:** The only valid value is `suggestion`.

`suggested_edits``SuggestedEdit[]`

The type of the suggested edit, along with additional type-specific properties.

**Minimum items:** `1`

addadd

deletedelete

formatformat

A suggestion to add some text.

`type``string`

**Available values:** The only valid value is `add`.

`text``string`

A suggestion to delete some text.

`type``string`

**Available values:** The only valid value is `delete`.

`text``string`

A suggestion to format some text.

`type``string`

**Available values:** The only valid value is `format`.

`format``string`

The suggested format change.

**Available values:**

  * `font_family`
  * `font_size`
  * `font_weight`
  * `font_style`
  * `color`
  * `background_color`
  * `decoration`
  * `strikethrough`
  * `link`
  * `letter_spacing`
  * `line_height`
  * `direction`
  * `text_align`
  * `list_marker`
  * `list_level`
  * `margin_inline_start`
  * `text_indent`
  * `font_size_modifier`
  * `vertical_align`



`status``string`

The current status of the suggestion.

**Available values:**

  * `open`: A suggestion was made, but it hasn't been accepted or rejected yet.
  * `accepted`: A suggestion was accepted and applied to the design.
  * `rejected`: A suggestion was rejected and not applied to the design.



`created_at``integer`

When the thread was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the thread was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`author``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **author**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

Event type for a comment thread that has been resolved.

`type``string`

**Available values:** The only valid value is `resolved`.

`comment_url``string`

A URL to the design, focused on the comment thread.

`comment``Thread`

A discussion thread on a design.

The `type` of the thread can be found in the `thread_type` object, along with additional type-specific properties. The `author` of the thread might be missing if that user account no longer exists.

Properties of **comment**

`id``string`

The ID of the thread.

You can use this ID to create replies to the thread using the [Create reply API](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-reply/).

`design_id``string`

The ID of the design that the discussion thread is on.

`thread_type``ThreadType`

The type of the discussion thread, along with additional type-specific properties.

commentcomment

suggestionsuggestion

A comment thread.

`type``string`

**Available values:** The only valid value is `comment`.

`content``CommentContent`

The content of a comment thread or reply.

Properties of **content**

`plaintext``string`

The content in plaintext. Any user mention tags are shown in the format `[user_id:team_id]`.

`markdown``string`

Optional

The content in markdown. Any user mention tags are shown in the format `[user_id:team_id]`

`mentions``object`

The Canva users mentioned in the comment thread or reply.

Properties of **mentions**

`<KEY>``object of UserMentions`

Information about the user mentioned in a comment thread or reply. Each user mention is keyed using the user's user ID and team ID separated by a colon (`user_id:team_id`).
    
    
    {
    
      "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP": {
    
        "tag": "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP",
    
        "user": {
    
          "user_id": "oUnPjZ2k2yuhftbWF7873o",
    
          "team_id": "oBpVhLW22VrqtwKgaayRbP",
    
          "display_name": "John Doe"
    
        }
    
      }
    
    }

JSON

Copy

`tag``string`

The mention tag for the user mentioned in the comment thread or reply content. This has the format of the user's user ID and team ID separated by a colon (`user_id:team_id`).

`user``TeamUser`

Metadata for the user, consisting of the User ID, Team ID, and display name.

Properties of **user**

`user_id``string`

Optional

The ID of the user.

`team_id``string`

Optional

The ID of the user's Canva Team.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`assignee``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **assignee**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`resolver``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **resolver**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

A suggestion thread.

`type``string`

**Available values:** The only valid value is `suggestion`.

`suggested_edits``SuggestedEdit[]`

The type of the suggested edit, along with additional type-specific properties.

**Minimum items:** `1`

addadd

deletedelete

formatformat

A suggestion to add some text.

`type``string`

**Available values:** The only valid value is `add`.

`text``string`

A suggestion to delete some text.

`type``string`

**Available values:** The only valid value is `delete`.

`text``string`

A suggestion to format some text.

`type``string`

**Available values:** The only valid value is `format`.

`format``string`

The suggested format change.

**Available values:**

  * `font_family`
  * `font_size`
  * `font_weight`
  * `font_style`
  * `color`
  * `background_color`
  * `decoration`
  * `strikethrough`
  * `link`
  * `letter_spacing`
  * `line_height`
  * `direction`
  * `text_align`
  * `list_marker`
  * `list_level`
  * `margin_inline_start`
  * `text_indent`
  * `font_size_modifier`
  * `vertical_align`



`status``string`

The current status of the suggestion.

**Available values:**

  * `open`: A suggestion was made, but it hasn't been accepted or rejected yet.
  * `accepted`: A suggestion was accepted and applied to the design.
  * `rejected`: A suggestion was rejected and not applied to the design.



`created_at``integer`

When the thread was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the thread was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`author``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **author**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

Event type for a reply to a comment thread.

`type``string`

**Available values:** The only valid value is `reply`.

`reply_url``string`

A URL to the design, focused on the comment reply.

`reply``Reply`

A reply to a thread.

The `author` of the reply might be missing if that user account no longer exists.

Properties of **reply**

`id``string`

The ID of the reply.

`design_id``string`

The ID of the design that the thread for this reply is attached to.

`thread_id``string`

The ID of the thread this reply is in.

`content``CommentContent`

The content of a comment thread or reply.

Properties of **content**

`plaintext``string`

The content in plaintext. Any user mention tags are shown in the format `[user_id:team_id]`.

`markdown``string`

Optional

The content in markdown. Any user mention tags are shown in the format `[user_id:team_id]`

`mentions``object`

The Canva users mentioned in the comment thread or reply.

Properties of **mentions**

`<KEY>``object of UserMentions`

Information about the user mentioned in a comment thread or reply. Each user mention is keyed using the user's user ID and team ID separated by a colon (`user_id:team_id`).
    
    
    {
    
      "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP": {
    
        "tag": "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP",
    
        "user": {
    
          "user_id": "oUnPjZ2k2yuhftbWF7873o",
    
          "team_id": "oBpVhLW22VrqtwKgaayRbP",
    
          "display_name": "John Doe"
    
        }
    
      }
    
    }

JSON

Copy

`tag``string`

The mention tag for the user mentioned in the comment thread or reply content. This has the format of the user's user ID and team ID separated by a colon (`user_id:team_id`).

`user``TeamUser`

Metadata for the user, consisting of the User ID, Team ID, and display name.

Properties of **user**

`user_id``string`

Optional

The ID of the user.

`team_id``string`

Optional

The ID of the user's Canva Team.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`created_at``integer`

When the reply was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the reply was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`author``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **author**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

Event type for a mention in a comment thread or reply.

`type``string`

**Available values:** The only valid value is `mention`.

`content``MentionEventContent`

The type of mention event content, along with additional type-specific properties.

threadthread

replyreply

Content for a mention in a comment thread.

`type``string`

**Available values:** The only valid value is `thread`.

`comment_url``string`

A URL to the design, focused on the comment thread.

`comment``Thread`

A discussion thread on a design.

The `type` of the thread can be found in the `thread_type` object, along with additional type-specific properties. The `author` of the thread might be missing if that user account no longer exists.

Properties of **comment**

`id``string`

The ID of the thread.

You can use this ID to create replies to the thread using the [Create reply API](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-reply/).

`design_id``string`

The ID of the design that the discussion thread is on.

`thread_type``ThreadType`

The type of the discussion thread, along with additional type-specific properties.

commentcomment

suggestionsuggestion

A comment thread.

`type``string`

**Available values:** The only valid value is `comment`.

`content``CommentContent`

The content of a comment thread or reply.

Properties of **content**

`plaintext``string`

The content in plaintext. Any user mention tags are shown in the format `[user_id:team_id]`.

`markdown``string`

Optional

The content in markdown. Any user mention tags are shown in the format `[user_id:team_id]`

`mentions``object`

The Canva users mentioned in the comment thread or reply.

Properties of **mentions**

`<KEY>``object of UserMentions`

Information about the user mentioned in a comment thread or reply. Each user mention is keyed using the user's user ID and team ID separated by a colon (`user_id:team_id`).
    
    
    {
    
      "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP": {
    
        "tag": "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP",
    
        "user": {
    
          "user_id": "oUnPjZ2k2yuhftbWF7873o",
    
          "team_id": "oBpVhLW22VrqtwKgaayRbP",
    
          "display_name": "John Doe"
    
        }
    
      }
    
    }

JSON

Copy

`tag``string`

The mention tag for the user mentioned in the comment thread or reply content. This has the format of the user's user ID and team ID separated by a colon (`user_id:team_id`).

`user``TeamUser`

Metadata for the user, consisting of the User ID, Team ID, and display name.

Properties of **user**

`user_id``string`

Optional

The ID of the user.

`team_id``string`

Optional

The ID of the user's Canva Team.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`assignee``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **assignee**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`resolver``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **resolver**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

A suggestion thread.

`type``string`

**Available values:** The only valid value is `suggestion`.

`suggested_edits``SuggestedEdit[]`

The type of the suggested edit, along with additional type-specific properties.

**Minimum items:** `1`

addadd

deletedelete

formatformat

A suggestion to add some text.

`type``string`

**Available values:** The only valid value is `add`.

`text``string`

A suggestion to delete some text.

`type``string`

**Available values:** The only valid value is `delete`.

`text``string`

A suggestion to format some text.

`type``string`

**Available values:** The only valid value is `format`.

`format``string`

The suggested format change.

**Available values:**

  * `font_family`
  * `font_size`
  * `font_weight`
  * `font_style`
  * `color`
  * `background_color`
  * `decoration`
  * `strikethrough`
  * `link`
  * `letter_spacing`
  * `line_height`
  * `direction`
  * `text_align`
  * `list_marker`
  * `list_level`
  * `margin_inline_start`
  * `text_indent`
  * `font_size_modifier`
  * `vertical_align`



`status``string`

The current status of the suggestion.

**Available values:**

  * `open`: A suggestion was made, but it hasn't been accepted or rejected yet.
  * `accepted`: A suggestion was accepted and applied to the design.
  * `rejected`: A suggestion was rejected and not applied to the design.



`created_at``integer`

When the thread was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the thread was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`author``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **author**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

Content for a mention in a comment reply.

`type``string`

**Available values:** The only valid value is `reply`.

`reply_url``string`

A URL to the design, focused on the comment reply.

`reply``Reply`

A reply to a thread.

The `author` of the reply might be missing if that user account no longer exists.

Properties of **reply**

`id``string`

The ID of the reply.

`design_id``string`

The ID of the design that the thread for this reply is attached to.

`thread_id``string`

The ID of the thread this reply is in.

`content``CommentContent`

The content of a comment thread or reply.

Properties of **content**

`plaintext``string`

The content in plaintext. Any user mention tags are shown in the format `[user_id:team_id]`.

`markdown``string`

Optional

The content in markdown. Any user mention tags are shown in the format `[user_id:team_id]`

`mentions``object`

The Canva users mentioned in the comment thread or reply.

Properties of **mentions**

`<KEY>``object of UserMentions`

Information about the user mentioned in a comment thread or reply. Each user mention is keyed using the user's user ID and team ID separated by a colon (`user_id:team_id`).
    
    
    {
    
      "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP": {
    
        "tag": "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP",
    
        "user": {
    
          "user_id": "oUnPjZ2k2yuhftbWF7873o",
    
          "team_id": "oBpVhLW22VrqtwKgaayRbP",
    
          "display_name": "John Doe"
    
        }
    
      }
    
    }

JSON

Copy

`tag``string`

The mention tag for the user mentioned in the comment thread or reply content. This has the format of the user's user ID and team ID separated by a colon (`user_id:team_id`).

`user``TeamUser`

Metadata for the user, consisting of the User ID, Team ID, and display name.

Properties of **user**

`user_id``string`

Optional

The ID of the user.

`team_id``string`

Optional

The ID of the user's Canva Team.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`created_at``integer`

When the reply was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the reply was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`author``User`

Optional

Metadata for the user, consisting of the User ID and display name.

Properties of **author**

`id``string`

The ID of the user.

`display_name``string`

Optional

The name of the user as shown in the Canva UI.

`comment_url``string`

Deprecated

A URL to the design, focused on the new comment.

The `comment_url` property is deprecated. For details of the comment event, use the `comment_event` property instead.

`comment``CommentEventDeprecated`

Deprecated

Basic details about the comment.

The `comment` property is deprecated. For details of the comment event, use the `comment_event` property instead.

Properties of **comment**

`type``string`

Deprecated

The type of comment event.

**Available values:**

  * `comment`
  * `reply`
  * `mention`
  * `assign`
  * `resolve`



`data``Comment`

Deprecated

The comment object, which contains metadata about the comment. Deprecated in favor of the new `thread` object.

parentparent

replyreply

Data about the comment, including the message, author, and the object (such as a design) the comment is attached to.

`type``string`

Deprecated

The type of comment. When creating a new parent (top-level) comment, the `type` is `parent`.

**Available values:** The only valid value is `parent`.

`id``string`

Deprecated

The ID of the comment.

You can use this ID to create replies to the comment using the [Create reply API](https://www.canva.dev/docs/apps/rest-apis/reference/comments/create-reply/).

`message``string`

Deprecated

The comment message. This is the comment body shown in the Canva UI. User mentions are shown here in the format `[user_id:team_id]`.

`author``User`

Deprecated

Metadata for the user, consisting of the User ID and display name.

Properties of **author**

`id``string`

Deprecated

The ID of the user.

`display_name``string`

Deprecated

The name of the user as shown in the Canva UI.

`created_at``integer`

Deprecated

When the comment or reply was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

Deprecated

When the comment or reply was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`assignee``User`

Deprecated

Metadata for the user, consisting of the User ID and display name.

Properties of **assignee**

`id``string`

Deprecated

The ID of the user.

`display_name``string`

Deprecated

The name of the user as shown in the Canva UI.

`resolver``User`

Deprecated

Metadata for the user, consisting of the User ID and display name.

Properties of **resolver**

`id``string`

Deprecated

The ID of the user.

`display_name``string`

Deprecated

The name of the user as shown in the Canva UI.

`mentions``object`

Deprecated

The Canva users mentioned in the comment.

Properties of **mentions**

`<KEY>``object of TeamUsers`

Metadata for the user, consisting of the User ID, Team ID, and display name.

`user_id``string`

Deprecated

The ID of the user.

`team_id``string`

Deprecated

The ID of the user's Canva Team.

`display_name``string`

Deprecated

The name of the user as shown in the Canva UI.

`attached_to``CommentObject`

Deprecated

Identifying information about the object (such as a design) that the comment is attached to.

If the comment is attached to a Canva Design.

`type``string`

Deprecated

**Available values:** The only valid value is `design`.

`design_id``string`

Deprecated

The ID of the design this comment is attached to.

Data about the reply comment, including the message, author, and the object (such as a design) the comment is attached to.

`type``string`

Deprecated

The type of comment. When creating a reply to a top-level comment, the `type` is `reply`.

**Available values:** The only valid value is `reply`.

`id``string`

Deprecated

The ID of the comment.

`message``string`

Deprecated

The comment message. This is the comment body shown in the Canva UI. User mentions are shown here in the format `[user_id:team_id]`.

`author``User`

Deprecated

Metadata for the user, consisting of the User ID and display name.

Properties of **author**

`id``string`

Deprecated

The ID of the user.

`display_name``string`

Deprecated

The name of the user as shown in the Canva UI.

`thread_id``string`

Deprecated

The ID of the comment thread this reply is in. This ID is the same as the `id` of the parent comment.

`created_at``integer`

Deprecated

When the comment or reply was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

Deprecated

When the comment or reply was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`mentions``object`

Deprecated

The Canva users mentioned in the comment.

Properties of **mentions**

`<KEY>``object of TeamUsers`

Metadata for the user, consisting of the User ID, Team ID, and display name.

`user_id``string`

Deprecated

The ID of the user.

`team_id``string`

Deprecated

The ID of the user's Canva Team.

`display_name``string`

Deprecated

The name of the user as shown in the Canva UI.

`attached_to``CommentObject`

Deprecated

Identifying information about the object (such as a design) that the comment is attached to.

If the comment is attached to a Canva Design.

`type``string`

Deprecated

**Available values:** The only valid value is `design`.

`design_id``string`

Deprecated

The ID of the design this comment is attached to.

## Example: Comment notification
    
    
    {
    
      "id": "eb595730",
    
      "created_at": 1377396000,
    
      "content": {
    
        "type": "comment",
    
        "triggering_user": {
    
          "id": "uKakKUfI03Fg8k2gZ6OkT",
    
          "display_name": "John Doe"
    
        },
    
        "receiving_team_user": {
    
          "user_id": "auDAbliZ2rQNNOsUl5OLu",
    
          "team_id": "Oi2RJILTrKk0KRhRUZozX",
    
          "display_name": "Jane Doe"
    
        },
    
        "design": {
    
          "id": "DAFVztcvd9z",
    
          "title": "My summer holiday",
    
          "url": "https://www.canva.com/design/DAFVztcvd9z/edit",
    
          "thumbnail": {
    
            "width": 595,
    
            "height": 335,
    
            "url": "https://document-export.canva.com/Vczz9/zF9vzVtdADc/2/thumbnail/0001.png?<query-string>"
    
          },
    
          "urls": {
    
            "edit_url": "https://www.canva.com/api/design/eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiZXhwaXJ5IjoxNzQyMDk5NDAzMDc5fQ..GKLx2hrJa3wSSDKQ.hk3HA59qJyxehR-ejzt2DThBW0cbRdMBz7Fb5uCpwD-4o485pCf4kcXt_ypUYX0qMHVeZ131YvfwGPIhbk-C245D8c12IIJSDbZUZTS7WiCOJZQ.sNz3mPSQxsETBvl_-upMYA/edit",
    
            "view_url": "https://www.canva.com/api/design/eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwiZXhwaXJ5IjoxNzQyMDk5NDAzMDc5fQ..GKLx2hrJa3wSSDKQ.hk3HA59qJyxehR-ejzt2DThBW0cbRdMBz7Fb5uCpwD-4o485pCf4kcXt_ypUYX0qMHVeZ131YvfwGPIhbk-C245D8c12IIJSDbZUZTS7WiCOJZQ.sNz3mPSQxsETBvl_-upMYA/view"
    
          },
    
          "created_at": 1377396000,
    
          "updated_at": 1692928800,
    
          "page_count": 3
    
        },
    
        "comment_event": {
    
          "type": "new",
    
          "comment_url": "https://www.canva.com/design/3WCduQdjayTcPVM/z128cqanFu7E3/edit?ui=OdllGgZ4Snnq3MD8uI10bfA",
    
          "comment": {
    
            "id": "KeAbiEAjZEj",
    
            "design_id": "DAFVztcvd9z",
    
            "thread_type": {
    
              "type": "comment",
    
              "content": {
    
                "plaintext": "Great work [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!",
    
                "markdown": "*_Great work_* [oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP]!"
    
              },
    
              "mentions": {
    
                "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP": {
    
                  "tag": "oUnPjZ2k2yuhftbWF7873o:oBpVhLW22VrqtwKgaayRbP",
    
                  "user": {
    
                    "user_id": "oUnPjZ2k2yuhftbWF7873o",
    
                    "team_id": "oBpVhLW22VrqtwKgaayRbP",
    
                    "display_name": "John Doe"
    
                  }
    
                }
    
              },
    
              "assignee": {
    
                "id": "uKakKUfI03Fg8k2gZ6OkT",
    
                "display_name": "John Doe"
    
              },
    
              "resolver": {
    
                "id": "uKakKUfI03Fg8k2gZ6OkT",
    
                "display_name": "John Doe"
    
              }
    
            },
    
            "author": {
    
              "id": "uKakKUfI03Fg8k2gZ6OkT",
    
              "display_name": "John Doe"
    
            },
    
            "created_at": 1692928800,
    
            "updated_at": 1692928900
    
          }
    
        }
    
      }
    
    }

JSON

Copy
