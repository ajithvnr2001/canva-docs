---
url: https://www.canva.dev/docs/apps/rest-apis/webhooks/share-design-notification/
title: Share design notifications - Webhooks notification reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:42.812266+00:00
---

# Share design notifications - Webhooks notification reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/webhooks/share-design-notification/

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

# Share design notifications

The NotificationContent sent when a user shares a design.

Copy page

Webhook notifications are currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview features won't produce a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/).
  * Public apps that use preview features will not pass the review process, and can't be made available to all Canva users.



If the `type` of [notification](https://www.canva.dev/docs/apps/rest-apis/webhooks/#notification) is `share_design`, the webhook payload object contains the following parameters:

`id``string`

The unique identifier for the notification.

`created_at``integer`

When the notification was created, as a UNIX timestamp (in seconds since the UNIX epoch).

`content``object`

The notification content for when someone shares a design.

Properties of **content**

`type``string`

**Available values:** The only valid value is `share_design`.

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

`share_url``string`

A URL that the user who receives the notification can use to access the shared design.

`share``ShareAction`

Optional

Metadata about the share event.

Properties of **share**

`message``string`

The optional message users can include when sharing something with another user using the Canva UI.

## Example: Share design notification
    
    
    {
    
      "id": "eb595730",
    
      "created_at": 1377396000,
    
      "content": {
    
        "type": "share_design",
    
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
    
        "share_url": "https://www.canva.com/api/action?token=zWiz3GqRaWVkolwSgfBa9sKbsKgfHAoxv_mjs-mlX2M",
    
        "share": {
    
          "message": "Check this out!"
    
        }
    
      }
    
    }

JSON

Copy
