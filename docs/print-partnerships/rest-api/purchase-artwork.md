---
url: https://www.canva.dev/docs/print-partnerships/rest-api/purchase-artwork/
title: Purchase an artwork - REST API - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:03.026325+00:00
---

# Purchase an artwork - REST API - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/rest-api/purchase-artwork/

REST API

[Delete a user](https://www.canva.dev/docs/print-partnerships/rest-api/delete-a-user/)[Purchase an artwork](https://www.canva.dev/docs/print-partnerships/rest-api/purchase-artwork/)[Restore a user](https://www.canva.dev/docs/print-partnerships/rest-api/restore-a-user/)

# Purchase an artwork

Purchase the print-quality version of the user's artwork.

Copy page

When an end user purchases a print via a partner's website, the partner must purchase the print-quality version of the user's artwork from Canva. In response to this purchase, Canva immediately provides a URL to download the print-quality artwork.

For security reasons, you **must** send this request from a backend server. If you send this request via a browser, Canva rejects the request.

## Request

### Method

POST

### Endpoint
    
    
    https://api.canva.com/_tpi/partnership/<partner_id>/artworks/<artwork_id>

BASH

Copy

### Headers

Header| Description  
---|---  
`Authorization`| The integration's Artwork API secret.  
  
### Path parameters

Parameter| Type| Required| Description  
---|---|---|---  
`partner_id`| string| Yes| The integration's Partner ID.  
`artwork_id`| string| Yes| The ID of the user's artwork.  
  
### Body

Property| Type| Required| Description  
---|---|---|---  
`purchaseConfirmation`| object| Yes| Information about the purchase.  
`purchaseConfirmation.currency`| string| Yes| The currency of the purchase in the [ISO 4217⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/ISO_4217#Active_codes) format.  
`purchaseConfirmation.discountAmount`| number| Yes| The amount deducted from the gross amount using coupons, gift certificates, and other redeemable incentives. If there's no discount to apply, set to `0.00`.  
`purchaseConfirmation.grossAmount`| number| Yes| The price of the order excluding discounts, but including shipping fees, taxes, and other charges applied to the order value.  
`purchaseConfirmation.item`| string| Yes| The ID of the order's item in the partner's back-end system.  
`purchaseConfirmation.netAmount`| number| Yes| The price of the order excluding discounts, shipping fees, taxes, and other charges applied to the order value.  
`purchaseConfirmation.order`| string| Yes| The ID of the order in the partner's back-end system.  
`purchaseConfirmation.quantity`| int32| Yes| The quantity of items the user is purchasing with the order.  
`purchaseConfirmation.sku`| string| Yes| The SKU of the item in the partner's back-end system.  
`purchaseConfirmation.extraDetails`| string| No| Free-form field for additional details about the purchase.  
  
#### Example
    
    
    {
    
      "purchaseConfirmation": {
    
        "order": "OR_12345672",
    
        "item": "IT_12345672-003",
    
        "sku": "PS034509",
    
        "quantity": 5,
    
        "currency": "USD",
    
        "grossAmount": 65.5,
    
        "discountAmount": 6.55,
    
        "netAmount": 58.95
    
      }
    
    }

JSON

Copy

## Response

### 200 - Success

The response when the purchase is successful.

Name| Type| Required| Description  
---|---|---|---  
`id`| string| Yes| The ID of the artwork.  
`productionFile` (deprecated)| string| No| The URL of the print-quality artwork. This URL expires after 15 minutes. This property has been superseded by `productionFiles`.  
`productionFiles`| string| Yes| A list of URLs for downloading the print-quality version of the user's artwork. For JPG and PNG file formats, there's a separate URL for each page. For PDF file formats, there's one URL for the entire artwork. The URL is in the form `https://partnership-artwork.canva.com/<export_file>`. If you're using the China version of the SDK, the TLD is `.cn` instead of `.com`. You can take the necessary security measures to protect the URL from any malicious attacks.  
  
#### Example
    
    
    {
    
      "id": "123456",
    
      "productionFiles": ["https://...", "https://...", "https://..."]
    
    }

JSON

Copy

### 401 - Unauthorized

The response when Canva doesn't recognize the supplied [credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/).

## Example
    
    
    const axios = require("axios");
    
    
    
    
    (async () => {
    
      const response = await axios.request({
    
        baseURL: "https://api.canva.com",
    
        url: `/_tpi/partnership/<partner_id>/artworks/<artwork_id>`,
    
        method: "post",
    
        headers: {
    
          Authorization: "<artwork_api_secret>",
    
        },
    
        data: {
    
          purchaseConfirmation: {
    
            order: "OR_12345672",
    
            item: "IT_12345672-003",
    
            sku: "PS034509",
    
            quantity: 5,
    
            currency: "USD",
    
            grossAmount: 65.5,
    
            discountAmount: 6.55,
    
            netAmount: 58.95,
    
          },
    
        },
    
      });
    
    
    
    
      console.log(response.data);
    
    })();

JAVASCRIPT

Copy
