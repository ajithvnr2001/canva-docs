---
url: https://www.canva.dev/docs/apps/rest-apis/webhooks/suggestion-notification/
title: Suggestion notifications - Webhooks notification reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:42.568194+00:00
---

# Suggestion notifications - Webhooks notification reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/webhooks/suggestion-notification/

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

# Suggestion notifications

The NotificationContent sent when a user suggests an edit to a design.

Copy page

Webhook notifications are currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview features won't produce a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/).
  * Public apps that use preview features will not pass the review process, and can't be made available to all Canva users.



If the `type` of [notification](https://www.canva.dev/docs/apps/rest-apis/webhooks/#notification) is `suggestion`, the webhook payload object contains the following parameters:

`id``string`

The unique identifier for the notification.

`created_at``integer`

When the notification was created, as a UNIX timestamp (in seconds since the UNIX epoch).

`content``object`

The notification content when someone does one of the following actions:

  * Suggests edits to a design.
  * Applies or rejects a suggestion.
  * Replies to a suggestion.
  * Mentions a user in a reply to a suggestion.



Properties of **content**

`type``string`

**Available values:** The only valid value is `suggestion`.

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

`suggestion_event_type``SuggestionEventType`

The type of suggestion event, along with additional type-specific properties.

newnew

acceptedaccepted

rejectedrejected

replyreply

mentionmention

Event type for a new suggestion.

`type``string`

**Available values:** The only valid value is `new`.

`suggestion_url``string`

A URL to the design, focused on the suggestion.

`suggestion``Thread`

A discussion thread on a design.

The `type` of the thread can be found in the `thread_type` object, along with additional type-specific properties. The `author` of the thread might be missing if that user account no longer exists.

Properties of **suggestion**

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

Event type for a suggestion that has been accepted.

`type``string`

**Available values:** The only valid value is `accepted`.

`suggestion_url``string`

A URL to the design, focused on the suggestion.

`suggestion``Thread`

A discussion thread on a design.

The `type` of the thread can be found in the `thread_type` object, along with additional type-specific properties. The `author` of the thread might be missing if that user account no longer exists.

Properties of **suggestion**

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

Event type for a suggestion that has been rejected.

`type``string`

**Available values:** The only valid value is `rejected`.

`suggestion_url``string`

A URL to the design, focused on the suggestion.

`suggestion``Thread`

A discussion thread on a design.

The `type` of the thread can be found in the `thread_type` object, along with additional type-specific properties. The `author` of the thread might be missing if that user account no longer exists.

Properties of **suggestion**

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

Event type for a reply to a suggestion.

`type``string`

**Available values:** The only valid value is `reply`.

`reply_url``string`

A URL to the design, focused on the suggestion reply.

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

Event type for a mention in a reply to a suggestion.

`type``string`

**Available values:** The only valid value is `mention`.

`reply_url``string`

A URL to the design, focused on the suggestion reply.

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

## Example: Suggestion notification
    
    
    {
    
      "id": "eb595730",
    
      "created_at": 1377396000,
    
      "content": {
    
        "type": "suggestion",
    
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
    
        "suggestion_event_type": {
    
          "type": "new",
    
          "suggestion_url": "https://www.canva.com/design/3WCduQdjayTcPVM/z128cqanFu7E3/edit?ui=OdllGgZ4Snnq3MD8uI10bfA",
    
          "suggestion": {
    
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
