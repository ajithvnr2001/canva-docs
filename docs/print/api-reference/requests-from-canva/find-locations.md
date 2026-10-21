---
url: https://www.canva.dev/docs/print/api-reference/requests-from-canva/find-locations/
title: Find locations - Requests from Canva - Canva Print API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:30.161962+00:00
---

# Find locations - Requests from Canva - Canva Print API Documentation

> Source: https://www.canva.dev/docs/print/api-reference/requests-from-canva/find-locations/

Requests from Canva

[Overview](https://www.canva.dev/docs/print/api-reference/requests-from-canva/)[Create order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/create-order/)[Get order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/get-order/)[Update order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/update-order/)[Cancel order](https://www.canva.dev/docs/print/api-reference/requests-from-canva/cancel-order/)[Find locations](https://www.canva.dev/docs/print/api-reference/requests-from-canva/find-locations/)

# Find locations

Copy page

Gets up-to-date information on the print partner's locations that support in-store pickup.

Canva is interested in:

  * The address of each pickup location.
  * Production and transfer locations that supply to each pickup location.
  * The opening hours of each pickup location.



## HTTP method and URL path

GET` https://{yourPrintApiUrl}/locations`

## Header parameters

`X-Canva-Public-Api-Version``string`

Optional

The version of the Canva Print API used in the request. If not specified, the latest version is assumed.

`X-Canva-Signature``string`

Required

The Canva request signature. This is used to verify the request is legitimate and was not tampered with in transit.

## Query parameters

`country``string`

Optional

The ISO 3166-1 alpha-2 country code to filter the returned partner locations.

`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list.

To retrieve all items, you might need to make multiple requests.

`limit``integer`

Required

The limit for the number of results to return. If the available items are more than the limit, then the response will include a continuation token.

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`locations``PickupLocation[]`

List of pickup locations currently available for the partner.

Properties of **locations**

`id``string`

The internal reference of the location on the partners system.

**Maximum length:** `255`

`display_name``string`

The display name of the location. This is what Canva customers can expect the location to be called.

**Maximum length:** `255`

`phone``string`

The contact phone number of the location.

**Maximum length:** `255`

`timezone``string`

The timezone of the location in tz format.

**Maximum length:** `255`

`address``Address`

An address.

Properties of **address**

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

`geolocation``Geolocation`

Longitude and latitude of a location.

Properties of **geolocation**

`latitude``number`

The latitude of the geolocation.

**Minimum:** `-90`

**Maximum:** `90`

`longitude``number`

The longitude of the geolocation.

**Minimum:** `-180`

**Maximum:** `180`

`pickup_hours``PickupHours`

Pickup hours for a pickup location. If hours do not exist for a day, the store is considered closed.

Properties of **pickup_hours**

`monday_hours``Hours`

Optional

Details on the opening and closing time for a pickup location.

The open time must be before close time. Hours must be open for at least a minute.

Properties of **monday_hours**

`open_time_hour``integer`

The hour part of the time the store opens in 24-hour format.

**Maximum:** `23`

`open_time_minute``integer`

The minute part of the time the store opens.

**Maximum:** `59`

`close_time_hour``integer`

The hour part of the time the store closes in 24-hour format.

**Maximum:** `23`

`close_time_minute``integer`

The minute part of the time the store closes.

**Maximum:** `59`

`tuesday_hours``Hours`

Optional

Details on the opening and closing time for a pickup location.

The open time must be before close time. Hours must be open for at least a minute.

Properties of **tuesday_hours**

`open_time_hour``integer`

The hour part of the time the store opens in 24-hour format.

**Maximum:** `23`

`open_time_minute``integer`

The minute part of the time the store opens.

**Maximum:** `59`

`close_time_hour``integer`

The hour part of the time the store closes in 24-hour format.

**Maximum:** `23`

`close_time_minute``integer`

The minute part of the time the store closes.

**Maximum:** `59`

`wednesday_hours``Hours`

Optional

Details on the opening and closing time for a pickup location.

The open time must be before close time. Hours must be open for at least a minute.

Properties of **wednesday_hours**

`open_time_hour``integer`

The hour part of the time the store opens in 24-hour format.

**Maximum:** `23`

`open_time_minute``integer`

The minute part of the time the store opens.

**Maximum:** `59`

`close_time_hour``integer`

The hour part of the time the store closes in 24-hour format.

**Maximum:** `23`

`close_time_minute``integer`

The minute part of the time the store closes.

**Maximum:** `59`

`thursday_hours``Hours`

Optional

Details on the opening and closing time for a pickup location.

The open time must be before close time. Hours must be open for at least a minute.

Properties of **thursday_hours**

`open_time_hour``integer`

The hour part of the time the store opens in 24-hour format.

**Maximum:** `23`

`open_time_minute``integer`

The minute part of the time the store opens.

**Maximum:** `59`

`close_time_hour``integer`

The hour part of the time the store closes in 24-hour format.

**Maximum:** `23`

`close_time_minute``integer`

The minute part of the time the store closes.

**Maximum:** `59`

`friday_hours``Hours`

Optional

Details on the opening and closing time for a pickup location.

The open time must be before close time. Hours must be open for at least a minute.

Properties of **friday_hours**

`open_time_hour``integer`

The hour part of the time the store opens in 24-hour format.

**Maximum:** `23`

`open_time_minute``integer`

The minute part of the time the store opens.

**Maximum:** `59`

`close_time_hour``integer`

The hour part of the time the store closes in 24-hour format.

**Maximum:** `23`

`close_time_minute``integer`

The minute part of the time the store closes.

**Maximum:** `59`

`saturday_hours``Hours`

Optional

Details on the opening and closing time for a pickup location.

The open time must be before close time. Hours must be open for at least a minute.

Properties of **saturday_hours**

`open_time_hour``integer`

The hour part of the time the store opens in 24-hour format.

**Maximum:** `23`

`open_time_minute``integer`

The minute part of the time the store opens.

**Maximum:** `59`

`close_time_hour``integer`

The hour part of the time the store closes in 24-hour format.

**Maximum:** `23`

`close_time_minute``integer`

The minute part of the time the store closes.

**Maximum:** `59`

`sunday_hours``Hours`

Optional

Details on the opening and closing time for a pickup location.

The open time must be before close time. Hours must be open for at least a minute.

Properties of **sunday_hours**

`open_time_hour``integer`

The hour part of the time the store opens in 24-hour format.

**Maximum:** `23`

`open_time_minute``integer`

The minute part of the time the store opens.

**Maximum:** `59`

`close_time_hour``integer`

The hour part of the time the store closes in 24-hour format.

**Maximum:** `23`

`close_time_minute``integer`

The minute part of the time the store closes.

**Maximum:** `59`

`receiving_from_locations``string[]`

Optional

A list of locations that are allowed to produce or transfer items to this pickup location.

**Minimum length:** `1`

`continuation``string`

Optional

A continuation token. If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list. This value should be NULL if no more results are available.

**Maximum length:** `255`

## Example response
    
    
    {
    
      "locations": [
    
        {
    
          "id": "partnerLocation1234",
    
          "display_name": "Partner Fake Location",
    
          "phone": "(555) 555-1234",
    
          "timezone": "Australia/Melbourne",
    
          "address": {
    
            "address_line1": "374 Johnson Ave, Brooklyn",
    
            "address_line2": "Unit 1",
    
            "city": "New York",
    
            "subdivision": "US-NY",
    
            "postcode": "11206",
    
            "country": "US"
    
          },
    
          "geolocation": {
    
            "latitude": -33.8853,
    
            "longitude": 151.2088
    
          },
    
          "receiving_from_locations": [
    
            "partnerLocation1234_production",
    
            "partnerLocation1234_transfer"
    
          ],
    
          "pickup_hours": {
    
            "monday_hours": {
    
              "open_time_hour": 10,
    
              "open_time_minute": 0,
    
              "close_time_hour": 17,
    
              "close_time_minute": 30
    
            },
    
            "tuesday_hours": {
    
              "open_time_hour": 10,
    
              "open_time_minute": 0,
    
              "close_time_hour": 17,
    
              "close_time_minute": 30
    
            },
    
            "wednesday_hours": {
    
              "open_time_hour": 10,
    
              "open_time_minute": 0,
    
              "close_time_hour": 17,
    
              "close_time_minute": 30
    
            },
    
            "thursday_hours": {
    
              "open_time_hour": 10,
    
              "open_time_minute": 0,
    
              "close_time_hour": 17,
    
              "close_time_minute": 30
    
            },
    
            "friday_hours": {
    
              "open_time_hour": 10,
    
              "open_time_minute": 0,
    
              "close_time_hour": 17,
    
              "close_time_minute": 30
    
            },
    
            "saturday_hours": {
    
              "open_time_hour": 9,
    
              "open_time_minute": 0,
    
              "close_time_hour": 17,
    
              "close_time_minute": 30
    
            },
    
            "sunday_hours": {
    
              "open_time_hour": 9,
    
              "open_time_minute": 0,
    
              "close_time_hour": 12,
    
              "close_time_minute": 0
    
            }
    
          }
    
        }
    
      ],
    
      "continuation": "edf3"
    
    }

JSON

Copy

## Error responses

### 400 Bad Request. For example, an invalid payload format.

### 401 Unauthorized. For example, an invalid signature.
