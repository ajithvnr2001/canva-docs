---
url: https://www.canva.dev/docs/print/api-reference/requests-from-canva/update-order/
title: Update order - Requests from Canva - Canva Print API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:32.491294+00:00
---

# Update order - Requests from Canva - Canva Print API Documentation

> Source: https://www.canva.dev/docs/print/api-reference/requests-from-canva/update-order/

Requests from Canva

[Overview](https://www.canva.dev/docs/print/api-reference/requests-from-canva/)[Create order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/)[Get order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/get-order/)[Update order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/update-order/)[Cancel order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/cancel-order/)[Find locations](https://www.canva.dev/docs/print/api-reference/requests-from-canva/find-locations/)

# Update order

Copy page

Updates an order in the print partner's system.

  * Changes to an order are restricted only to the delivery address and customer details of the order.
  * Updates to an order aren't allowed if every item of the order has been canceled.
  * The order update request can be denied if the update isn't possible. For example, if the order contains items that have already shipped.



## HTTP method and URL path

PATCH` https://{yourPrintApiUrl}/v1/orders/{orderReferenceId}`

## Header parameters

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/json`.

For example: `Content-Type: application/json`

`X-Canva-Public-Api-Version``string`

Optional

The version of the Canva Print API used in the request. If not specified, the latest version is assumed.

`X-Canva-Signature``string`

Required

The Canva request signature. This is used to verify the request is legitimate and was not tampered with in transit.

## Path parameters

`orderReferenceId``string`

Required

Unique, case-sensitive string identifying the order in Canva's system.

## Body parameters

Expand all

`request_type``string`

Required

The type of request being made.

**Available values:** The only valid value is `update_order`.

`order_reference_id``string`

Required

A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

**Maximum length:** `255`

`updates``Updates`

Required

Updates to the order. The request must contain at least one of `customer_details` or `delivery_address`.

Properties of **updates**

`customer_details``CustomerDetails`

Optional

The customer.

Properties of **customer_details**

`name``string`

Required

The full name of the customer.

**Maximum length:** `255`

`phone``string`

Required

The phone number of the customer.

**Maximum length:** `255`

`email``string`

Required

The email address of the customer.

**Maximum length:** `255`

`tax_details``TaxDetails`

Optional

The customer's tax identification details.

Properties of **tax_details**

`tax_id``string`

Required

The customer's tax identification number.

`type``string`

Required

Whether the tax identification number belongs to an individual or a business.

**Available values:**

  * `individual`
  * `business`



`delivery_address``Address`

Optional

An address.

Properties of **delivery_address**

`address_line1``string`

Required

The address line 1 portion of the address.

**Maximum length:** `255`

`city``string`

Required

The city portion of the address.

**Maximum length:** `255`

`country``string`

Required

ISO 3166-1 alpha-2 country code of the address. Includes the exceptionally reserved code IC for the autonomous Spanish region Canary Islands.

**Maximum length:** `2`

`address_line2``string`

Optional

The address line 2 portion of the address. Can contain additional address information such as unit number or house name.

**Maximum length:** `255`

`subdivision``string`

Optional

ISO 3166-2 subdivision code of the address. Required for AU, BR, CA, IN, JP, KR, MX, NZ, US.

**Maximum length:** `6`

`postcode``string`

Optional

The postcode/zipcode portion of the address.

**Maximum length:** `12`

## Example requests

### Update customer details and delivery address for a delivery order
    
    
    {
    
      "request_type": "update_order",
    
      "order_reference_id": "FB123456789",
    
      "updates": {
    
        "customer_details": {
    
          "name": "NotCharles Boyle",
    
          "phone": "(555) 555-0000",
    
          "email": "notcharlesboyle@email.com"
    
        },
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 2",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        }
    
      }
    
    }

JSON

Copy

### Update customer details for a pickup order
    
    
    {
    
      "request_type": "update_order",
    
      "order_reference_id": "FB123456789",
    
      "updates": {
    
        "customer_details": {
    
          "name": "NotCharles Boyle",
    
          "phone": "(555) 555-0000",
    
          "email": "notcharlesboyle@email.com"
    
        }
    
      }
    
    }

JSON

Copy

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`order``Order`

An order.

pickuppickup

deliverydelivery

An order that will be picked up from a location by the customer.

`order_type``string`

The type of order.

**Available values:** The only valid value is `pickup`.

`order_reference_id``string`

A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

**Maximum length:** `255`

`items``Item[]`

The items in the order.

**Minimum length:** `1`

Properties of **items**

`item_reference_id``string`

A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

**Maximum length:** `255`

`status``string`

The updated production status of the item.

**Available values:**

  * `received`: The order item was received and is pending further processing.
  * `producing`: The order item production has started.
  * `produced`: The order item production has completed.
  * `packaging`: The order item packaging has started.
  * `ready_for_pickup`: The order item was shipped to the receiver.
  * `picked_up`: The order item is ready for pickup in store.
  * `shipped`: The order item was picked up from the store.
  * `canceled`: The order item was canceled.



`sku_reference``string`

Partner-facing reference for an item's SKU. Describes a specific variant of a product to be produced.

**Maximum length:** `255`

`quantity``integer`

The number of copies of an item to produce.

`add_on_sku_reference``string`

Optional

Partner-facing reference for an item add on SKU. Sometimes referred to as a stock item. For example, envelopes with postcards.

**Maximum length:** `255`

`error_details``ErrorDetails`

Optional

The error details of the item. Errors details should be cleared from an item after it has been resolved.

Properties of **error_details**

`issue_origin``string`

The origin of the issue.

**Available values:**

  * `production`
  * `order_url`
  * `user_details`
  * `user_address`
  * `delivery`
  * `unknown`



`description``string`

A human readable message that describes the cause of the error.

**Maximum length:** `255`

`customer_details``CustomerDetails`

The customer.

Properties of **customer_details**

`name``string`

The full name of the customer.

**Maximum length:** `255`

`phone``string`

The phone number of the customer.

**Maximum length:** `255`

`email``string`

The email address of the customer.

**Maximum length:** `255`

`tax_details``TaxDetails`

Optional

The customer's tax identification details.

Properties of **tax_details**

`tax_id``string`

The customer's tax identification number.

`type``string`

Whether the tax identification number belongs to an individual or a business.

**Available values:**

  * `individual`
  * `business`



`production_location_reference``string`

The reference ID for the production location of the order.

**Maximum length:** `255`

`pickup_location_reference``string`

The reference ID for the pickup location of an order, as specified by the Canva user placing the order.

**Maximum length:** `255`

`created_at``integer`

When the order was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the order was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`pickup_tier``string`

Optional

The pickup tier selected by the customer. Pickup tiers are Canva-defined values that describe different speeds and costs of pickup. Partners are expected to interpret this according to contractual agreements.

`order_invoice_url``string`

Optional

A temporary URL for the print partner to download an order invoice. This can be a taxation requirement for some countries. This is only included for certain partners, and can be configured in the API settings.

An order that will be delivered to the customer.

`order_type``string`

The type of order.

**Available values:** The only valid value is `delivery`.

`order_reference_id``string`

A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

**Maximum length:** `255`

`items``Item[]`

The Items in the order.

**Minimum length:** `1`

Properties of **items**

`item_reference_id``string`

A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

**Maximum length:** `255`

`status``string`

The updated production status of the item.

**Available values:**

  * `received`: The order item was received and is pending further processing.
  * `producing`: The order item production has started.
  * `produced`: The order item production has completed.
  * `packaging`: The order item packaging has started.
  * `ready_for_pickup`: The order item was shipped to the receiver.
  * `picked_up`: The order item is ready for pickup in store.
  * `shipped`: The order item was picked up from the store.
  * `canceled`: The order item was canceled.



`sku_reference``string`

Partner-facing reference for an item's SKU. Describes a specific variant of a product to be produced.

**Maximum length:** `255`

`quantity``integer`

The number of copies of an item to produce.

`add_on_sku_reference``string`

Optional

Partner-facing reference for an item add on SKU. Sometimes referred to as a stock item. For example, envelopes with postcards.

**Maximum length:** `255`

`error_details``ErrorDetails`

Optional

The error details of the item. Errors details should be cleared from an item after it has been resolved.

Properties of **error_details**

`issue_origin``string`

The origin of the issue.

**Available values:**

  * `production`
  * `order_url`
  * `user_details`
  * `user_address`
  * `delivery`
  * `unknown`



`description``string`

A human readable message that describes the cause of the error.

**Maximum length:** `255`

`customer_details``CustomerDetails`

The customer.

Properties of **customer_details**

`name``string`

The full name of the customer.

**Maximum length:** `255`

`phone``string`

The phone number of the customer.

**Maximum length:** `255`

`email``string`

The email address of the customer.

**Maximum length:** `255`

`tax_details``TaxDetails`

Optional

The customer's tax identification details.

Properties of **tax_details**

`tax_id``string`

The customer's tax identification number.

`type``string`

Whether the tax identification number belongs to an individual or a business.

**Available values:**

  * `individual`
  * `business`



`delivery_address``Address`

An address.

Properties of **delivery_address**

`address_line1``string`

The address line 1 portion of the address.

**Maximum length:** `255`

`city``string`

The city portion of the address.

**Maximum length:** `255`

`country``string`

ISO 3166-1 alpha-2 country code of the address. Includes the exceptionally reserved code IC for the autonomous Spanish region Canary Islands.

**Maximum length:** `2`

`address_line2``string`

Optional

The address line 2 portion of the address. Can contain additional address information such as unit number or house name.

**Maximum length:** `255`

`subdivision``string`

Optional

ISO 3166-2 subdivision code of the address. Required for AU, BR, CA, IN, JP, KR, MX, NZ, US.

**Maximum length:** `6`

`postcode``string`

Optional

The postcode/zipcode portion of the address.

**Maximum length:** `12`

`delivery_shipping_tier``string`

The shipping tier selected by the customer. Shipping tiers are Canva-defined values that describe different speeds and costs of delivery. Partners are expected to interpret this according to contractual agreements. For example, `economy`, `standard` and `express`.

`production_location_reference``string`

The reference ID for the production location of the order.

**Maximum length:** `255`

`dispatch_location_reference``string`

The reference ID for the dispatch location for the order.

**Maximum length:** `255`

`created_at``integer`

When the order was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the order was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`shipments``Shipment[]`

Optional

A list of shipments for the order.

Properties of **shipments**

`items``ShipmentItem[]`

The items included in the shipment.

**Minimum length:** `1`

Properties of **items**

`item_reference_id``string`

A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

**Maximum length:** `255`

`quantity``integer`

The number of copies of an item that were shipped.

`tracking_number``string`

Optional

The tracking number provided by the carrier.

**Minimum length:** `1`

**Maximum length:** `255`

`carrier``string`

Optional

The Canva-supported carrier delivering the shipment. Valid carrier values include: `allied_express`, `allwayex`, `amazon`, `ams`, `asendia`, `aus_post`, `b2c`, `blue_dart`, `bpost`, `bring`, `bring_no`, `brt`, `canada_post`, `carriers`, `chitchats`, `chronopost`, `colissimo`, `correios`, `correos`, `correos_express`, `couriers_please`, `deutsche_post`, `dhl`, `dpd`, `dpd_uk`, `estafeta`, `evri`, `fastway`, `fedex`, `fleet_optics`, `france_express`, `gls`, `hunter_express`, `ics`, `icumulus`, `india_post`, `jadlog`, `japan_post`, `landmark_global`, `laposte`, `loomis_express`, `lotte`, `nacex`, `new_zealand_post`, `newzealand_couriers`, `norsk_global`, `ontime`, `pakman`, `paquetexpress`, `parcel_force`, `pitney_bowes`, `planzer`, `post_nl`, `post_nord`, `purolator`, `quality`, `qxpress`, `royal_mail`, `sagawa`, `sda`, `seur`, `shiprocket`, `spring_gds`, `star_track`, `swiss_post`, `tnt`, `toll`, `uniuni`, `ups`, `usps`, `yamato`.

**Minimum length:** `1`

`dispatched_at``integer`

Optional

When the shipment was dispatched, as a Unix timestamp (in seconds since the Unix Epoch).

`dispatch_location_reference``string`

Optional

The location ID of where the shipment was dispatched.

**Maximum length:** `255`

`order_invoice_url``string`

Optional

A temporary URL for the print partner to download an order invoice. This can be a taxation requirement for some countries. This is only included for certain partners, and can be configured in the API settings.

## Example responses

### Update customer details and delivery address for a delivery order
    
    
    {
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "customer_details": {
    
          "name": "NotCharles Boyle",
    
          "phone": "(555) 555-0000",
    
          "email": "notcharlesboyle@email.com"
    
        },
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "status": "received",
    
            "sku_reference": "IN00030",
    
            "quantity": 50
    
          }
    
        ],
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 2",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "production_location_reference": "partnerLocation1234",
    
        "dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice",
    
        "created_at": 1726448251,
    
        "updated_at": 1726449800
    
      }
    
    }

JSON

Copy

### Update customer details for a pickup order
    
    
    {
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "pickup",
    
        "customer_details": {
    
          "name": "NotCharles Boyle",
    
          "phone": "(555) 555-0000",
    
          "email": "notcharlesboyle@email.com"
    
        },
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "status": "received",
    
            "sku_reference": "IN00030",
    
            "quantity": 50
    
          }
    
        ],
    
        "production_location_reference": "partnerLocation1234",
    
        "pickup_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice",
    
        "created_at": 1726448251,
    
        "updated_at": 1726449800
    
      }
    
    }

JSON

Copy

## Error responses

### 400 Bad Request. For example, an invalid payload format.

### 401 Unauthorized. For example, an invalid signature.

### 403 Forbidden. For example, an idempotent order issue, or the order doesn't exist.

### 405 Not Allowed. For example, the request isn't allowed because of the order state, or it isn't supported or implemented.
