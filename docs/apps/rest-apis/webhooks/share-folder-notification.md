---
url: https://www.canva.dev/docs/apps/rest-apis/webhooks/share-folder-notification/
title: Share folder notifications - Webhooks notification reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:41.944855+00:00
---

# Share folder notifications - Webhooks notification reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/webhooks/share-folder-notification/

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

# Share folder notifications

The NotificationContent sent when a user shares a folder.

Copy page

Webhook notifications are currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview features won't produce a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/).
  * Public apps that use preview features will not pass the review process, and can't be made available to all Canva users.



If the `type` of [notification](https://www.canva.dev/docs/apps/rest-apis/webhooks/#notification) is `share_folder`, the webhook payload object contains the following parameters:

`id``string`

The unique identifier for the notification.

`created_at``integer`

When the notification was created, as a UNIX timestamp (in seconds since the UNIX epoch).

`content``object`

The notification content for when someone shares a folder.

Properties of **content**

`type``string`

**Available values:** The only valid value is `share_folder`.

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

`folder``FolderSummary`

This object contains some folder metadata. You can retrieve additional metadata using the folder ID and the `/v1/folders/{folderId}` endpoint.

Properties of **folder**

`id``string`

The folder ID.

`name``string`

The folder name, as shown in the Canva UI.

`created_at``integer`

When the folder was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the folder was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`url``string`

Optional

The folder URL.

`title``string`

Deprecated

The folder name, as shown in the Canva UI. This property is deprecated, so you should use the `name` property instead.

`share``ShareAction`

Optional

Metadata about the share event.

Properties of **share**

`message``string`

The optional message users can include when sharing something with another user using the Canva UI.

## Example: Share folder notification
    
    
    {
    
      "id": "eb595730",
    
      "created_at": 1377396000,
    
      "content": {
    
        "type": "share_folder",
    
        "triggering_user": {
    
          "id": "uKakKUfI03Fg8k2gZ6OkT",
    
          "display_name": "John Doe"
    
        },
    
        "receiving_team_user": {
    
          "user_id": "auDAbliZ2rQNNOsUl5OLu",
    
          "team_id": "Oi2RJILTrKk0KRhRUZozX",
    
          "display_name": "Jane Doe"
    
        },
    
        "folder": {
    
          "id": "FAF2lZtloor",
    
          "name": "My awesome holiday",
    
          "created_at": 1377396000,
    
          "updated_at": 1692928800,
    
          "url": "https://www.canva.com/folder/FAF2lZtloor"
    
        },
    
        "share": {
    
          "message": "Check this out!"
    
        }
    
      }
    
    }

JSON

Copy
