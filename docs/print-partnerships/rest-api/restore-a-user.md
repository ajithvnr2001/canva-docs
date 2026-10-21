---
url: https://www.canva.dev/docs/print-partnerships/rest-api/restore-a-user/
title: Restore a user - REST API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:03.799976+00:00
---

# Restore a user - REST API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/rest-api/restore-a-user/

REST API

[Delete a user](https://www.canva.dev/docs/print-partnerships/rest-api/delete-a-user/)[Purchase an artwork](https://www.canva.dev/docs/print-partnerships/rest-api/purchase-artwork/)[Restore a user](https://www.canva.dev/docs/print-partnerships/rest-api/restore-a-user/)

# Restore a user

Copy page

Partners can restore a [deleted user](https://www.canva.dev/docs/print-partnerships/rest-api/delete-a-user/) within 14 days of deleting them. After 14 days, Canva deletes the user permanently.

When a partner restores a deleted user, Canva recovers the designs, artworks, media uploads, and all other information related to the user.

## Request

### Method

POST

### Endpoint
    
    
    https://api.canva.com/_tpi/partnership/<partnerId>/users/<externalUserId>/undelete

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

The response when Canva successfully restores a deleted user.

### 401 - Unauthorized

The response when Canva doesn't recognize a partner ID or an Artwork API secret.

### 403 - Forbidden

The response when the user ID belongs to an active user or a permanently deleted user.

### 404 - Not Found

The response when Canva doesn't recognize a user ID.

## Example
    
    
    curl -XPOST -H 'Authorization: <artwork_api_secret>' 'https://api.canva.com/_tpi/partnership/<partnerId>/users/<externalUserId>/undelete'

Copy
