---
url: https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/
title: Create order - Requests from Canva - Canva Print API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:31.892168+00:00
---

# Create order - Requests from Canva - Canva Print API Documentation

> Source: https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/

Requests from Canva

[Overview](https://www.canva.dev/docs/print/api-reference/requests-from-canva/)[Create order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/)[Get order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/get-order/)[Update order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/update-order/)[Cancel order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/cancel-order/)[Find locations](https://www.canva.dev/docs/print/api-reference/requests-from-canva/find-locations/)

# Create order

Copy page

Creates an order on the print partner's system. This operation lets Canva request a partner to commence production on an order.

As part of the request, Canva sends an `orderReferenceId` and a list of `items` to print.

Requests to this endpoint should be idempotent. If a provided `orderReferenceId` already exists in the partner system, and:

  * The item `item_reference_id`s match and are not canceled: A success response should be returned.
  * The item `item_reference_id`s match but items requested in the request are canceled: An error response should be returned.
  * The item `item_reference_id`s don't match: An error response should be returned.



## HTTP method and URL path

POST` https://{yourPrintApiUrl}/v1/orders`

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

## Body parameters

Expand all

`request_type``string`

Required

The type of request being made.

**Available values:** The only valid value is `create_order`.

`order``CreateOrder`

Required

Describes an order to create.

pickuppickup

deliverydelivery

Pickup order to create.

`order_type``string`

Required

The type of order.

**Available values:** The only valid value is `pickup`.

`order_reference_id``string`

Required

A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

**Maximum length:** `255`

`items``CreateItem[]`

Required

Items to create.

**Minimum length:** `1`

Properties of **items**

`item_reference_id``string`

Required

A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

**Maximum length:** `255`

`sku_reference``string`

Required

Partner-facing reference for an item's SKU. Describes a specific variant of a product to be produced.

**Maximum length:** `255`

`artworks``Artwork[]`

Required

The artworks of the item.

**Minimum length:** `1`

Properties of **artworks**

`url``string`

Required

A temporary URL for the partner to download a production-quality print file for an item.

`print_area``string`

Required

Where on a product an artwork file is expected to appear.

  * `cover`
  * `front`
  * `back`
  * `sheets`
  * `none`



**Maximum length:** `255`

`orientation``string`

Required

The physical orientation of the file.

**Maximum length:** `255`

**Available values:**

  * `portrait`
  * `landscape`
  * `square`



`pages``integer`

Optional

The number of the pages in the file. Only provided for PDF.

`quantity``integer`

Required

The number of copies of an item to produce.

`attributes``object`

Required

A key-value pair of attributes describing an item. These pairs complement the SKU by enumerating the unique attributes it describes. If used by the print partner, the expected values must be confirmed with Canva.

Properties of **attributes**

`<KEY>``object of strings`

Required

A key-value pair of attributes describing an item. These pairs complement the SKU by enumerating the unique attributes it describes. If used by the print partner, the expected values must be confirmed with Canva.
    
    
    {
    
      "paperFinish": "matte",
    
      "paperType": "premium",
    
      "productSize": "portrait"
    
    }

JSON

Copy

`add_on_sku_reference``string`

Optional

Partner-facing reference for an item add on SKU. Sometimes referred to as a stock item. For example, envelopes with postcards.

**Maximum length:** `255`

`mockup_url``string`

Optional

A temporary URL for the partner to download a mockup file displaying artwork imposed on a product for an item. This is included for certain products, generally apparel. This is controlled by Canva's internal product definition and not an API configuration.

`quoted_latest_fulfillment_date``integer`

Optional

The latest date Canva has shown to the customer by which the order will be delivered or available for pickup, as a Unix timestamp (in seconds since the Unix Epoch).

`customer_details``CustomerDetails`

Required

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



`preferred_production_location_reference``string`

Required

The reference ID for the preferred production location for the order. Partners can override this if the selected location is unsuitable, but partners must notify Canva through a production update if this occurs.

**Maximum length:** `255`

`pickup_location_reference``string`

Required

The reference ID for the pickup location of an order, as specified by the Canva user placing the order. Partners can't override this selection.

**Maximum length:** `255`

`pickup_tier``string`

Optional

The pickup tier selected by the customer. Pickup tiers are Canva-defined values that describe different speeds and costs of pickup. Partners are expected to interpret this according to contractual agreements.

`order_invoice_url``string`

Optional

A temporary URL for the print partner to download an order invoice. This can be a taxation requirement for some countries. This is only included for certain partners, and can be configured in the API settings.

Delivery order to create.

`order_type``string`

Required

The type of order.

**Available values:** The only valid value is `delivery`.

`order_reference_id``string`

Required

A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

**Maximum length:** `255`

`items``CreateItem[]`

Required

Items to create.

**Minimum length:** `1`

Properties of **items**

`item_reference_id``string`

Required

A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

**Maximum length:** `255`

`sku_reference``string`

Required

Partner-facing reference for an item's SKU. Describes a specific variant of a product to be produced.

**Maximum length:** `255`

`artworks``Artwork[]`

Required

The artworks of the item.

**Minimum length:** `1`

Properties of **artworks**

`url``string`

Required

A temporary URL for the partner to download a production-quality print file for an item.

`print_area``string`

Required

Where on a product an artwork file is expected to appear.

  * `cover`
  * `front`
  * `back`
  * `sheets`
  * `none`



**Maximum length:** `255`

`orientation``string`

Required

The physical orientation of the file.

**Maximum length:** `255`

**Available values:**

  * `portrait`
  * `landscape`
  * `square`



`pages``integer`

Optional

The number of the pages in the file. Only provided for PDF.

`quantity``integer`

Required

The number of copies of an item to produce.

`attributes``object`

Required

A key-value pair of attributes describing an item. These pairs complement the SKU by enumerating the unique attributes it describes. If used by the print partner, the expected values must be confirmed with Canva.

Properties of **attributes**

`<KEY>``object of strings`

Required

A key-value pair of attributes describing an item. These pairs complement the SKU by enumerating the unique attributes it describes. If used by the print partner, the expected values must be confirmed with Canva.
    
    
    {
    
      "paperFinish": "matte",
    
      "paperType": "premium",
    
      "productSize": "portrait"
    
    }

JSON

Copy

`add_on_sku_reference``string`

Optional

Partner-facing reference for an item add on SKU. Sometimes referred to as a stock item. For example, envelopes with postcards.

**Maximum length:** `255`

`mockup_url``string`

Optional

A temporary URL for the partner to download a mockup file displaying artwork imposed on a product for an item. This is included for certain products, generally apparel. This is controlled by Canva's internal product definition and not an API configuration.

`quoted_latest_fulfillment_date``integer`

Optional

The latest date Canva has shown to the customer by which the order will be delivered or available for pickup, as a Unix timestamp (in seconds since the Unix Epoch).

`customer_details``CustomerDetails`

Required

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

Required

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

`delivery_shipping_tier``string`

Required

The shipping tier selected by the customer. Shipping tiers are Canva-defined values that describe different speeds and costs of delivery. Partners are expected to interpret this according to contractual agreements. For example, `economy`, `standard` and `express`.

`preferred_production_location_reference``string`

Required

The reference ID for the preferred production location for the order. Partners can override this if the selected location is unsuitable, but partners must notify Canva through a production update if this occurs.

**Maximum length:** `255`

`preferred_dispatch_location_reference``string`

Required

The reference ID for the preferred dispatch location for an order, as determined by Canva's internal routing. Partners can override this if the selected location is unsuitable, but partners must notify Canva through a production update if this occurs. Generally, this is the same as the preferred production location, but they are separated for future flexibility.

**Maximum length:** `255`

`order_invoice_url``string`

Optional

A temporary URL for the print partner to download an order invoice. This can be a taxation requirement for some countries. This is only included for certain partners, and can be configured in the API settings.

## Example requests

### Create order: delivery, single item (invitation)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "IN00030",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "preferred_dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
    
      }
    
    }

JSON

Copy

### Create order: delivery, single item (T-shirt)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "TSHIRT_DELUXE_WHITE_MENS_M",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/JIB6bESKbphJ/9hi0gly7f7e016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "front",
    
                "orientation": "portrait"
    
              },
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "back",
    
                "orientation": "portrait"
    
              }
    
            ],
    
            "mockup_url": "https://print-prepress-file.canva.com/KIB6bRTYbphJ/325135e5c95c0161e2d3770dad48bba05db8c6ef2ef43e0d34c3612954f3f555.png?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
            "quantity": 1,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "preferred_dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
    
      }
    
    }

JSON

Copy

### Create order: delivery, single item (photobook)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "PHBOOK_11X8.5IN_HARD-COVER_SOFT-TOUCH",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/JIB6bESKbphJ/9hi0gly7f7e016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "cover",
    
                "orientation": "portrait",
    
                "pages": 1
    
              },
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 20
    
              }
    
            ],
    
            "quantity": 1,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "preferred_dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
    
      }
    
    }

JSON

Copy

### Create order: delivery, single item (canvas)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "CANVAS_PREMIUM_11X14IN_WOODGRAIN-FRAME",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait"
    
              }
    
            ],
    
            "quantity": 1,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "preferred_dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
    
      }
    
    }

JSON

Copy

### Create order: delivery, single item (invitations) with add ons (envelopes)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "IN00030",
    
            "add_on_sku_reference": "EN00006",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "preferred_dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
    
      }
    
    }

JSON

Copy

### Create Order: delivery, multiple items (canvas and invitations)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "CANVAS_PREMIUM_11X14IN_WOODGRAIN-FRAME",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait"
    
              }
    
            ],
    
            "quantity": 1,
    
            "attributes": {}
    
          },
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "IN00030",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "preferred_dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
    
      }
    
    }

JSON

Copy

### Create Order: delivery, multiple items (canvas and invitations) with add ons (envelopes)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "CANVAS_PREMIUM_11X14IN_WOODGRAIN-FRAME",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait"
    
              }
    
            ],
    
            "quantity": 1,
    
            "attributes": {}
    
          },
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "IN00030",
    
            "add_on_sku_reference": "EN00006",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "preferred_dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf"
    
      }
    
    }

JSON

Copy

### Create order: pickup, single item (invitations)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "pickup",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "IN00030",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "pickup_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice"
    
      }
    
    }

JSON

Copy

### Create order: pickup, single item (invitations) with add ons (envelopes)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "pickup",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "IN00030",
    
            "add_on_sku_reference": "EN00006",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "pickup_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice"
    
      }
    
    }

JSON

Copy

### Create order: pickup, multiple items (invitations and canvas)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "pickup",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "IN00030",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          },
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "CANVAS_PREMIUM_11X14IN_WOODGRAIN-FRAME",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait"
    
              }
    
            ],
    
            "quantity": 1,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "pickup_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice"
    
      }
    
    }

JSON

Copy

### Create order: pickup, multiple items (invitations) with add ons (envelopes)
    
    
    {
    
      "request_type": "create_order",
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "pickup",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "sku_reference": "IN00030",
    
            "add_on_sku_reference": "EN00006",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/F6YuSy55hyT_/d48bba05dbe016e9b4c0b2b7555552a0155555a5ac453c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          },
    
          {
    
            "item_reference_id": "FI987654321",
    
            "sku_reference": "IN00030",
    
            "artworks": [
    
              {
    
                "url": "https://print-prepress-file.canva.com/Sy55hyF6YuT_/16e9b4c0b2b7555552a0155555a5ac4d48bba05dbe053c2e55555gb7237226d3.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256",
    
                "print_area": "sheets",
    
                "orientation": "portrait",
    
                "pages": 2
    
              }
    
            ],
    
            "quantity": 50,
    
            "attributes": {}
    
          }
    
        ],
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "preferred_production_location_reference": "partnerLocation1234",
    
        "pickup_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice"
    
      }
    
    }

JSON

Copy

## Success response

Expand all

If successful, the endpoint returns a `201` response with a JSON body with the following parameters:

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

### Delivery order, single item (invitation)
    
    
    {
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
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
    
          "address_line2": "Unit 1",
    
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
    
        "updated_at": 1726448251
    
      }
    
    }

JSON

Copy

### Delivery order, single item (invitation) with add ons (envelopes)
    
    
    {
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "status": "received",
    
            "sku_reference": "IN00030",
    
            "add_on_sku_reference": "EN00006",
    
            "quantity": 50
    
          }
    
        ],
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
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
    
        "updated_at": 1726448251
    
      }
    
    }

JSON

Copy

### Delivery order, multiple items (invitation and canvas) with add ons (envelopes)
    
    
    {
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "delivery",
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "status": "received",
    
            "sku_reference": "IN00030",
    
            "add_on_sku_reference": "EN00006",
    
            "quantity": 50
    
          },
    
          {
    
            "item_reference_id": "FI987654321",
    
            "status": "received",
    
            "sku_reference": "CANVAS_PREMIUM_16X20_STRETCHED",
    
            "quantity": 5
    
          }
    
        ],
    
        "delivery_address": {
    
          "address_line1": "374 Johnson Ave, Brooklyn",
    
          "address_line2": "Unit 1",
    
          "city": "New York",
    
          "subdivision": "US-NY",
    
          "postcode": "11206",
    
          "country": "US"
    
        },
    
        "delivery_shipping_tier": "economy",
    
        "production_location_reference": "partnerLocation1234",
    
        "dispatch_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice.pdf",
    
        "created_at": 1726448251,
    
        "updated_at": 1726448251
    
      }
    
    }

JSON

Copy

### Pickup order, single item (invitation)
    
    
    {
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "pickup",
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
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
    
        "updated_at": 1726448251
    
      }
    
    }

JSON

Copy

### Pickup order, single item (invitation) with add ons (envelopes)
    
    
    {
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "pickup",
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "status": "received",
    
            "sku_reference": "IN00030",
    
            "add_on_sku_reference": "EN00006",
    
            "quantity": 50
    
          }
    
        ],
    
        "production_location_reference": "partnerLocation1234",
    
        "pickup_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice",
    
        "created_at": 1726448251,
    
        "updated_at": 1726448251
    
      }
    
    }

JSON

Copy

### Pickup order, multiple items (invitation and canvas) with add ons (envelopes)
    
    
    {
    
      "order": {
    
        "order_reference_id": "FB123456789",
    
        "order_type": "pickup",
    
        "customer_details": {
    
          "name": "Charles Boyle",
    
          "phone": "(555) 555-1234",
    
          "email": "charlesboyle@email.com"
    
        },
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "status": "received",
    
            "sku_reference": "IN00030",
    
            "add_on_sku_reference": "EN00006",
    
            "quantity": 50
    
          },
    
          {
    
            "item_reference_id": "FI987654321",
    
            "status": "received",
    
            "sku_reference": "CANVAS_PREMIUM_16X20_STRETCHED",
    
            "quantity": 5
    
          }
    
        ],
    
        "production_location_reference": "partnerLocation1234",
    
        "pickup_location_reference": "partnerLocation1234",
    
        "order_invoice_url": "https://s3-external-1.amazonaws.com/bucket/FI123456789/invoice",
    
        "created_at": 1726448251,
    
        "updated_at": 1726448251
    
      }
    
    }

JSON

Copy

## Error responses

### 400 Bad Request. For example, an invalid payload format.

### 401 Unauthorized. For example, an invalid signature.
