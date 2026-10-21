---
url: https://www.canva.dev/docs/print/changelog/
title: Changelog - Canva Print API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:35.396968+00:00
---

# Changelog - Canva Print API Documentation

> Source: https://www.canva.dev/docs/print/changelog/

Canva Print API

[Overview](https://www.canva.dev/docs/print/)

Guides

[Verifying requests from Canva](https://www.canva.dev/docs/print/verifying-requests-from-canva/)

API reference

Requests from Canva

Requests to Canva

Appendix

[Changelog](https://www.canva.dev/docs/print/changelog/)

# Changelog

Copy page

### September 7, 2026

  * A `quoted_latest_fulfillment_date` field has been introduced as an optional field on each item of a `CreateOrder`.

This allows Canva to send the latest date Canva has shown to the customer by which the order will be delivered or available for pickup, as a Unix timestamp in seconds.




### August 28, 2026

  * The `carrier` field has been updated to accept a non-empty string.

Currently supported carriers have been listed in the description.




### August 27, 2026

  * A `tax_details` field has been introduced as an optional field on `CustomerDetails`.

This allows Canva to send the customer's tax identification number and whether it belongs to an individual or business. There should be no changes for existing integrations.

  * The list of available carriers has been updated.

These values have been added: `france_express`, `jadlog`, `pakman`, `quality`.




### August 6, 2026

  * The description of the `subdivision` field has been updated to list the countries for which this field is required.



### August 4, 2026

  * The list of available carriers has been updated.

These values have been added: `ontime`.




### July 15, 2026

  * The list of available carriers has been updated.

These values have been added: `planzer`.




### July 13, 2026

  * The list of available carriers has been updated.

These values have been added: `bring`, `brt`, `colissimo`, `nacex`, `shiprocket`.




### June 15, 2026

  * The list of available carriers has been updated.

These values have been added: `new_zealand_post`.




### May 8, 2026

  * The description of the `delivery_shipping_tier` field has been updated to remove the list of available values.

This is to allow for additional shipping tiers based on contractual agreements to be sent in the future. There should be no changes for existing integrations.

  * A `pickup_tier` field has been introduced as an optional field on `CreateOrder` and `Order` for pickup orders.

This is to allow for additional pickup tiers based on contractual agreements to be sent in the future. There should be no changes for existing integrations.

  * The example URLs for item `mockup_url` and artworks have been updated with realistic Canva URLs.




### April 7, 2026

  * The list of available carriers has been updated.

These values have been added: `japan_post`.




### February 11, 2026

  * The title for the 'Get Locations' operation has been renamed to 'Find Locations'. The `operationId` in the OpenAPI description has also been renamed.



### January 16, 2026

  * The list of available carriers has been updated.

These values have been added: `norsk_global`.




### December 29, 2025

  * The example requests for the [Create order API](https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/) have been updated to remove the properties in the `attributes` object.

This is to reduce confusion because the attribute values may differ per integration.




### October 16, 2025

  * The description of the `country` field has been updated to include the exceptionally reserved ISO 3166-2 alpha-2 code IC for the autonomous Spanish region Canary Islands.



### October 2, 2025

  * The list of available carriers has been updated.

These values have been added: `fleet_optics`, `newzealand_couriers`.




### September 29, 2025

  * The list of available carriers has been updated.

These values have been added: `uniuni`.




### September 19, 2025

  * Description updated to mention the valid order type for `ready_for_pickup` and `picked_up` item status updates.

  * The list of available carriers has been updated.

These values have been added: `amazon`.




### September 10, 2025

  * Single item and Multi item example requests for order production events have been updated.

The new examples remove an incorrect `example` object from the request body.




### September 4, 2025

  * The list of available carriers has been updated.

These values have been added: `chronopost`.




### August 12, 2025

  * The maximum length of the continuation field in a response has been updated from 10 characters to 255.



### July 18, 2025

  * Additional examples for order error, shipment and production events have been added.

The new examples show multiple items in the request body.




### June 18, 2025

  * The order examples have been updated.

Some properties were incorrectly shown as numbers instead of strings. For example, postcode shown as `2017` instead of `"2017"`.

These examples have been fixed to now show as strings.

  * The example cost summary events have been updated.

The previous monetary values were incorrectly shown as numbers instead of strings, and one cost summary example had `total_major_unit` instead of `total_major_units`.

All cost summary event examples now have the correct monetary values and the correct labels.




### April 29, 2025

  * The example cost summary events have been updated.

The previous values incorrectly showed that the `request_type` was `cost_summary` instead of `cost_summary_event`.

All cost summary event examples now have the correct `request_type` value `cost_summary_event`.




### April 16, 2025

  * The list of available carriers has been updated.

These values have been removed: `dhl_express`, `dhl_us`, `quorier`, `major_express`.

These values have been added: `correos`, `correos_express`, `gls`, `landmark_global`, `evri`, `spring_gds`, `chitchats`.




### April 14, 2025

**New API version: 2025-04-14**

  * Initial release of the Print API.


