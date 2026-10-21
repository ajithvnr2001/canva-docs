---
url: https://www.canva.dev/docs/apps/rest-apis/webhooks/
title: Webhooks - Webhooks notification reference - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:40.637945+00:00
---

# Webhooks - Webhooks notification reference - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/webhooks/

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

# Webhooks

Receive real-time notification data for your users.

Copy page

Webhook notifications are currently provided as a preview. Be aware of the following:

  * There might be unannounced breaking changes.
  * Any breaking changes to preview features won't produce a new [API version](https://www.canva.dev/docs/apps/rest-apis/versions/).
  * Public apps that use preview features will not pass the review process, and can't be made available to all Canva users.



Webhooks allow Canva to send real-time information to your app, without polling or manual intervention. Your app will receive webhooks for events relevant to the authenticated user. Here's how a webhook typically works:

  1. An event occurs in Canva. For example, John comments on Jane's design.
  2. Canva sends the event information to your app as a `POST` request.
  3. The request contains event information, such as John's comment, when John made the comment, and what design it was made on.
  4. Your app receives the request, and sends a `200` status code back to Canva in response, which indicates the webhook was successfully received and processed (other status codes indicate an error).



When receiving requests, your app can perform further actions based on the event information. For example, sending an auto-reply to John's comment.

Canva only supports outgoing webhooks. For information on responding to comments, check the [Comments API documentation](https://www.canva.dev/docs/apps/rest-apis/reference/comments/).

## Scopes

If you want your app to receive specific web notifications from Canva, enable the following scopes:

Notification type| Required scopes  
---|---  
Comments| 

  * `collaboration:event`
  * `design:meta:read`
  * `comment:read`

  
Design access requests| 

  * `collaboration:event`
  * `design:meta:read`

  
Design approvals| 

  * `collaboration:event`
  * `design:meta:read`

  
Design sharing events| 

  * `collaboration:event`
  * `design:meta:read`

  
Folder access requests| 

  * `collaboration:event`
  * `folder:permission:write`

  
Folder sharing events| 

  * `collaboration:event`
  * `folder:read`

  
Team access invitations| 

  * `collaboration:event`

  
  
When enabling and using scopes, you must be explicit.

For example, the `asset:write` scope doesn't grant `asset:read` permissions. To get both read and write permissions for assets, you must enable both scopes in your app's settings, and request both scopes during the authorization process.

## Notification

A notification is generated once an event occurs in Canva. The webhook payload object consists of the required information about the event that has occurred.

The content depends on the `type` of the notification. For:

  * `comment`, see [Comment](https://www.canva.dev/docs/apps/rest-apis/webhooks/comment-notification/).
  * `design_access_requested`, see [Design access requested](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-access-requested-notification/).
  * `design_approval_requested`, see [Design approval requested](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-approval-requested-notification/).
  * `design_approval_response`, see [Design approval response](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-approval-response-notification/).
  * `design_approval_reviewer_invalidated`, see [Design approval reviewer invalidated](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-approval-reviewer-invalidated-notification/).
  * `design_mention`, see [Design mention](https://www.canva.dev/docs/apps/rest-apis/webhooks/design-mention-notification/).
  * `folder_access_requested`, see [Folder access requested](https://www.canva.dev/docs/apps/rest-apis/webhooks/folder-access-requested-notification/).
  * `share_design`, see [Share design](https://www.canva.dev/docs/apps/rest-apis/webhooks/share-design-notification/).
  * `share_folder`, see [Share folder](https://www.canva.dev/docs/apps/rest-apis/webhooks/share-folder-notification/).
  * `suggestion`, see [Suggestion](https://www.canva.dev/docs/apps/rest-apis/webhooks/suggestion-notification/).
  * `team_invite`, see [Team invite](https://www.canva.dev/docs/apps/rest-apis/webhooks/team-invite-notification/).


