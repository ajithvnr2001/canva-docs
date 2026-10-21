---
url: https://www.canva.dev/docs/print-partnerships/rest-api/delete-a-user/
title: Delete a user - REST API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:02.641077+00:00
---

# Delete a user - REST API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/rest-api/delete-a-user/

REST API

[Delete a user](https://www.canva.dev/docs/print-partnerships/rest-api/delete-a-user/)[Purchase an artwork](https://www.canva.dev/docs/print-partnerships/rest-api/purchase-artwork/)[Restore a user](https://www.canva.dev/docs/print-partnerships/rest-api/restore-a-user/)

# Delete a user

Copy page

Partners may want to delete a user who signed in to an integration using the [autoAuthToken](https://www.canva.dev/docs/print-partnerships/concepts/authentication/).

When a partner deletes a user, Canva marks the user's data as deleted for 14 days. The user's data includes designs, artworks, media uploads, and all other information related to the user.

Within 14 days, partners can [restore](https://www.canva.dev/docs/print-partnerships/rest-api/restore-a-user/) a deleted user if they want. After 14 days, Canva deletes the user permanently.

## Notes

  * Partners can delete only one user at a time.
  * Partners can't purchase an artwork of a deleted user.



## Request

### Method

DELETE

### Endpoint
    
    
    https://api.canva.com/_tpi/partnership/<partnerId>/users/<externalUserId>

BASH

Copy

### Headers

Header| Description  
---|---  
`Authorization`| An integration's [Artwork API secret](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#artwork-api-secret).  
  
### Path parameters

Parameter| Type| Required| Description  
---|---|---|---  
`partnerId`| string| Yes| An integration's [partner ID](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-id).  
`externalUserId`| string| Yes| The user ID in the partner's backend system. This is the user ID used when generating the autoAuthToken.  
  
### Body

The request body is empty.

## Response

### 200 - Success

The response when Canva successfully marks a user as deleted for 14 days.

### 401 - Unauthorized

The response when Canva doesn't recognize a partner ID or an Artwork API secret.

### 404 - Not Found

The response when:

  * Canva doesn't recognize a user ID.
  * The user ID belongs to a user who is permanently deleted or marked as deleted.



## Example
    
    
    curl -XDELETE -H 'Authorization: <artwork_api_secret>' 'https://api.canva.com/_tpi/partnership/<partnerId>/users/<externalUserId>'

Copy
