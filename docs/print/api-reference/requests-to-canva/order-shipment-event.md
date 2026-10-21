---
url: https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-shipment-event/
title: Create order shipment event - Requests to Canva - Canva Print API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:34.361823+00:00
---

# Create order shipment event - Requests to Canva - Canva Print API Documentation

> Source: https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-shipment-event/

Requests to Canva

[Overview](https://www.canva.dev/docs/print/api-reference/requests-to-canva/)[Generate access token](https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/)[Create order production event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-production-event/)[Create order shipment event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-shipment-event/)[Create order cost summary event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-cost-summary-event/)[Create order error event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-error-event/)[Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/)

# Create order shipment event

Copy page

Creates an event to notify Canva about a shipment for an order in the print partner's system.

## HTTP method and URL path

POST` https://api.canva.com/print/v1/events/order-shipment`

## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/json`.

For example: `Content-Type: application/json`

`X-Canva-Print-Client-Id``string`

Required

Unique ID of the print partner making the request.

## Body parameters

Expand all

`request_type``string`

Required

**Available values:** The only valid value is `shipment_event`.

`order_reference_id``string`

Required

A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

**Maximum length:** `255`

`shipments``ShipmentEvent[]`

Required

A list of shipments for the order.

**Minimum items:** `1`

Properties of **shipments**

`tracking_number``string`

Required

The tracking number provided by the carrier.

**Minimum length:** `1`

**Maximum length:** `255`

`carrier``string`

Required

The Canva-supported carrier delivering the shipment. Valid carrier values include: `allied_express`, `allwayex`, `amazon`, `ams`, `asendia`, `aus_post`, `b2c`, `blue_dart`, `bpost`, `bring`, `bring_no`, `brt`, `canada_post`, `carriers`, `chitchats`, `chronopost`, `colissimo`, `correios`, `correos`, `correos_express`, `couriers_please`, `deutsche_post`, `dhl`, `dpd`, `dpd_uk`, `estafeta`, `evri`, `fastway`, `fedex`, `fleet_optics`, `france_express`, `gls`, `hunter_express`, `ics`, `icumulus`, `india_post`, `jadlog`, `japan_post`, `landmark_global`, `laposte`, `loomis_express`, `lotte`, `nacex`, `new_zealand_post`, `newzealand_couriers`, `norsk_global`, `ontime`, `pakman`, `paquetexpress`, `parcel_force`, `pitney_bowes`, `planzer`, `post_nl`, `post_nord`, `purolator`, `quality`, `qxpress`, `royal_mail`, `sagawa`, `sda`, `seur`, `shiprocket`, `spring_gds`, `star_track`, `swiss_post`, `tnt`, `toll`, `uniuni`, `ups`, `usps`, `yamato`.

**Minimum length:** `1`

`items``ShipmentItem[]`

Required

The items included in the shipment.

**Minimum items:** `1`

Properties of **items**

`item_reference_id``string`

Required

A unique, case-sensitive ID for an order item that the partner can use when communicating with Canva.

**Maximum length:** `255`

`quantity``integer`

Required

The number of copies of an item that were shipped.

`dispatch_location_reference``string`

Required

The location reference ID of where the shipment was dispatched.

**Maximum length:** `255`

`dispatched_at``integer`

Required

When the shipment was dispatched, as a Unix timestamp (in seconds since the Unix Epoch).

## Example requests

### Single item, single shipment

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/print/v1/events/order-shipment' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    
    --data '{
    
      "request_type": "shipment_event",
    
      "order_reference_id": "FO123456789",
    
      "shipments": [
    
        {
    
          "tracking_number": "123456789",
    
          "carrier": "fedex",
    
          "items": [
    
            {
    
              "item_reference_id": "FI123456789",
    
              "quantity": 50
    
            }
    
          ],
    
          "dispatched_at": 1726448251,
    
          "dispatch_location_reference": "partnerLocation1234"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/print/v1/events/order-shipment", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
    
      },
    
      body: JSON.stringify({
    
        "request_type": "shipment_event",
    
        "order_reference_id": "FO123456789",
    
        "shipments": [
    
          {
    
            "tracking_number": "123456789",
    
            "carrier": "fedex",
    
            "items": [
    
              {
    
                "item_reference_id": "FI123456789",
    
                "quantity": 50
    
              }
    
            ],
    
            "dispatched_at": 1726448251,
    
            "dispatch_location_reference": "partnerLocation1234"
    
          }
    
        ]
    
      }),
    
    })
    
      .then(async (response) => {
    
        const data = await response.json();
    
        console.log(data);
    
      })
    
      .catch(err => console.error(err));

JS

Copy
    
    
    import java.io.IOException;
    
    import java.net.URI;
    
    import java.net.http.*;
    
    
    
    
    public class ApiExample {
    
        public static void main(String[] args) throws IOException, InterruptedException {
    
            HttpRequest request = HttpRequest.newBuilder()
    
                .uri(URI.create("https://api.canva.com/print/v1/events/order-shipment"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 50}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}"))
    
                .build();
    
    
    
    
            HttpResponse<String> response = HttpClient.newHttpClient().send(
    
                request,
    
                HttpResponse.BodyHandlers.ofString()
    
            );
    
            System.out.println(response.body());
    
        }
    
    }

JAVA

Copy
    
    
    import requests
    
    
    
    
    headers = {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28="
    
    }
    
    
    
    
    data = {
    
        "request_type": "shipment_event",
    
        "order_reference_id": "FO123456789",
    
        "shipments": [
    
            {
    
                "tracking_number": "123456789",
    
                "carrier": "fedex",
    
                "items": [
    
                    {
    
                        "item_reference_id": "FI123456789",
    
                        "quantity": 50
    
                    }
    
                ],
    
                "dispatched_at": 1726448251,
    
                "dispatch_location_reference": "partnerLocation1234"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/print/v1/events/order-shipment",
    
        headers=headers,
    
        json=data
    
    )
    
    print(response.json())

PY

Copy
    
    
    using System.Net.Http;
    
    
    
    
    var client = new HttpClient();
    
    var request = new HttpRequestMessage
    
    {
    
      Method = HttpMethod.Post,
    
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-shipment"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
    
      },
    
      Content = new StringContent(
    
        "{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 50}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}",
    
        Encoding.UTF8,
    
        "application/json"
    
      ),
    
    };
    
    
    
    
    using (var response = await client.SendAsync(request))
    
    {
    
      response.EnsureSuccessStatusCode();
    
      var body = await response.Content.ReadAsStringAsync();
    
      Console.WriteLine(body);
    
    };

CSHARP

Copy
    
    
    package main
    
    
    
    
    import (
    
    	"fmt"
    
    	"io"
    
    	"net/http"
    
    	"strings"
    
    )
    
    
    
    
    func main() {
    
    	payload := strings.NewReader(`{
    
    	  "request_type": "shipment_event",
    
    	  "order_reference_id": "FO123456789",
    
    	  "shipments": [
    
    	    {
    
    	      "tracking_number": "123456789",
    
    	      "carrier": "fedex",
    
    	      "items": [
    
    	        {
    
    	          "item_reference_id": "FI123456789",
    
    	          "quantity": 50
    
    	        }
    
    	      ],
    
    	      "dispatched_at": 1726448251,
    
    	      "dispatch_location_reference": "partnerLocation1234"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/print/v1/events/order-shipment"
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer {token}")
    
    	req.Header.Add("Content-Type", "application/json")
    
    	req.Header.Add("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
    
    
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }

GO

Copy
    
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
    
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-shipment",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "request_type" => "shipment_event",
    
        "order_reference_id" => "FO123456789",
    
        "shipments" => [
    
          [
    
            "tracking_number" => "123456789",
    
            "carrier" => "fedex",
    
            "items" => [
    
              [
    
                "item_reference_id" => "FI123456789",
    
                "quantity" => 50
    
              ]
    
            ],
    
            "dispatched_at" => 1726448251,
    
            "dispatch_location_reference" => "partnerLocation1234"
    
          ]
    
        ]
    
      ])
    
    ));
    
    
    
    
    $response = curl_exec($curl);
    
    $err = curl_error($curl);
    
    curl_close($curl);
    
    
    
    
    if (empty($err)) {
    
      echo $response;
    
    } else {
    
      echo "Error: " . $err;
    
    }

PHP

Copy
    
    
    require 'net/http'
    
    require 'uri'
    
    
    
    
    url = URI('https://api.canva.com/print/v1/events/order-shipment')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    
    request.body = <<REQUEST_BODY
    
    {
    
      "request_type": "shipment_event",
    
      "order_reference_id": "FO123456789",
    
      "shipments": [
    
        {
    
          "tracking_number": "123456789",
    
          "carrier": "fedex",
    
          "items": [
    
            {
    
              "item_reference_id": "FI123456789",
    
              "quantity": 50
    
            }
    
          ],
    
          "dispatched_at": 1726448251,
    
          "dispatch_location_reference": "partnerLocation1234"
    
        }
    
      ]
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

### Multiple items, single shipment

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/print/v1/events/order-shipment' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    
    --data '{
    
      "request_type": "shipment_event",
    
      "order_reference_id": "FO123456789",
    
      "shipments": [
    
        {
    
          "tracking_number": "123456789",
    
          "carrier": "fedex",
    
          "items": [
    
            {
    
              "item_reference_id": "FI123456789",
    
              "quantity": 50
    
            },
    
            {
    
              "item_reference_id": "FI987654321",
    
              "quantity": 10
    
            }
    
          ],
    
          "dispatched_at": 1726448251,
    
          "dispatch_location_reference": "partnerLocation1234"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/print/v1/events/order-shipment", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
    
      },
    
      body: JSON.stringify({
    
        "request_type": "shipment_event",
    
        "order_reference_id": "FO123456789",
    
        "shipments": [
    
          {
    
            "tracking_number": "123456789",
    
            "carrier": "fedex",
    
            "items": [
    
              {
    
                "item_reference_id": "FI123456789",
    
                "quantity": 50
    
              },
    
              {
    
                "item_reference_id": "FI987654321",
    
                "quantity": 10
    
              }
    
            ],
    
            "dispatched_at": 1726448251,
    
            "dispatch_location_reference": "partnerLocation1234"
    
          }
    
        ]
    
      }),
    
    })
    
      .then(async (response) => {
    
        const data = await response.json();
    
        console.log(data);
    
      })
    
      .catch(err => console.error(err));

JS

Copy
    
    
    import java.io.IOException;
    
    import java.net.URI;
    
    import java.net.http.*;
    
    
    
    
    public class ApiExample {
    
        public static void main(String[] args) throws IOException, InterruptedException {
    
            HttpRequest request = HttpRequest.newBuilder()
    
                .uri(URI.create("https://api.canva.com/print/v1/events/order-shipment"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 50}, {\"item_reference_id\": \"FI987654321\", \"quantity\": 10}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}"))
    
                .build();
    
    
    
    
            HttpResponse<String> response = HttpClient.newHttpClient().send(
    
                request,
    
                HttpResponse.BodyHandlers.ofString()
    
            );
    
            System.out.println(response.body());
    
        }
    
    }

JAVA

Copy
    
    
    import requests
    
    
    
    
    headers = {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28="
    
    }
    
    
    
    
    data = {
    
        "request_type": "shipment_event",
    
        "order_reference_id": "FO123456789",
    
        "shipments": [
    
            {
    
                "tracking_number": "123456789",
    
                "carrier": "fedex",
    
                "items": [
    
                    {
    
                        "item_reference_id": "FI123456789",
    
                        "quantity": 50
    
                    },
    
                    {
    
                        "item_reference_id": "FI987654321",
    
                        "quantity": 10
    
                    }
    
                ],
    
                "dispatched_at": 1726448251,
    
                "dispatch_location_reference": "partnerLocation1234"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/print/v1/events/order-shipment",
    
        headers=headers,
    
        json=data
    
    )
    
    print(response.json())

PY

Copy
    
    
    using System.Net.Http;
    
    
    
    
    var client = new HttpClient();
    
    var request = new HttpRequestMessage
    
    {
    
      Method = HttpMethod.Post,
    
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-shipment"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
    
      },
    
      Content = new StringContent(
    
        "{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 50}, {\"item_reference_id\": \"FI987654321\", \"quantity\": 10}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}",
    
        Encoding.UTF8,
    
        "application/json"
    
      ),
    
    };
    
    
    
    
    using (var response = await client.SendAsync(request))
    
    {
    
      response.EnsureSuccessStatusCode();
    
      var body = await response.Content.ReadAsStringAsync();
    
      Console.WriteLine(body);
    
    };

CSHARP

Copy
    
    
    package main
    
    
    
    
    import (
    
    	"fmt"
    
    	"io"
    
    	"net/http"
    
    	"strings"
    
    )
    
    
    
    
    func main() {
    
    	payload := strings.NewReader(`{
    
    	  "request_type": "shipment_event",
    
    	  "order_reference_id": "FO123456789",
    
    	  "shipments": [
    
    	    {
    
    	      "tracking_number": "123456789",
    
    	      "carrier": "fedex",
    
    	      "items": [
    
    	        {
    
    	          "item_reference_id": "FI123456789",
    
    	          "quantity": 50
    
    	        },
    
    	        {
    
    	          "item_reference_id": "FI987654321",
    
    	          "quantity": 10
    
    	        }
    
    	      ],
    
    	      "dispatched_at": 1726448251,
    
    	      "dispatch_location_reference": "partnerLocation1234"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/print/v1/events/order-shipment"
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer {token}")
    
    	req.Header.Add("Content-Type", "application/json")
    
    	req.Header.Add("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
    
    
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }

GO

Copy
    
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
    
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-shipment",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "request_type" => "shipment_event",
    
        "order_reference_id" => "FO123456789",
    
        "shipments" => [
    
          [
    
            "tracking_number" => "123456789",
    
            "carrier" => "fedex",
    
            "items" => [
    
              [
    
                "item_reference_id" => "FI123456789",
    
                "quantity" => 50
    
              ],
    
              [
    
                "item_reference_id" => "FI987654321",
    
                "quantity" => 10
    
              ]
    
            ],
    
            "dispatched_at" => 1726448251,
    
            "dispatch_location_reference" => "partnerLocation1234"
    
          ]
    
        ]
    
      ])
    
    ));
    
    
    
    
    $response = curl_exec($curl);
    
    $err = curl_error($curl);
    
    curl_close($curl);
    
    
    
    
    if (empty($err)) {
    
      echo $response;
    
    } else {
    
      echo "Error: " . $err;
    
    }

PHP

Copy
    
    
    require 'net/http'
    
    require 'uri'
    
    
    
    
    url = URI('https://api.canva.com/print/v1/events/order-shipment')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    
    request.body = <<REQUEST_BODY
    
    {
    
      "request_type": "shipment_event",
    
      "order_reference_id": "FO123456789",
    
      "shipments": [
    
        {
    
          "tracking_number": "123456789",
    
          "carrier": "fedex",
    
          "items": [
    
            {
    
              "item_reference_id": "FI123456789",
    
              "quantity": 50
    
            },
    
            {
    
              "item_reference_id": "FI987654321",
    
              "quantity": 10
    
            }
    
          ],
    
          "dispatched_at": 1726448251,
    
          "dispatch_location_reference": "partnerLocation1234"
    
        }
    
      ]
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

### Single item, multi shipment

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/print/v1/events/order-shipment' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    
    --data '{
    
      "request_type": "shipment_event",
    
      "order_reference_id": "FO123456789",
    
      "shipments": [
    
        {
    
          "tracking_number": "123456789",
    
          "carrier": "fedex",
    
          "items": [
    
            {
    
              "item_reference_id": "FI123456789",
    
              "quantity": 25
    
            }
    
          ],
    
          "dispatched_at": 1726448251,
    
          "dispatch_location_reference": "partnerLocation1234"
    
        },
    
        {
    
          "tracking_number": "987654321",
    
          "carrier": "fedex",
    
          "items": [
    
            {
    
              "item_reference_id": "FI123456789",
    
              "quantity": 25
    
            }
    
          ],
    
          "dispatched_at": 1726448251,
    
          "dispatch_location_reference": "partnerLocation1234"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/print/v1/events/order-shipment", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
    
      },
    
      body: JSON.stringify({
    
        "request_type": "shipment_event",
    
        "order_reference_id": "FO123456789",
    
        "shipments": [
    
          {
    
            "tracking_number": "123456789",
    
            "carrier": "fedex",
    
            "items": [
    
              {
    
                "item_reference_id": "FI123456789",
    
                "quantity": 25
    
              }
    
            ],
    
            "dispatched_at": 1726448251,
    
            "dispatch_location_reference": "partnerLocation1234"
    
          },
    
          {
    
            "tracking_number": "987654321",
    
            "carrier": "fedex",
    
            "items": [
    
              {
    
                "item_reference_id": "FI123456789",
    
                "quantity": 25
    
              }
    
            ],
    
            "dispatched_at": 1726448251,
    
            "dispatch_location_reference": "partnerLocation1234"
    
          }
    
        ]
    
      }),
    
    })
    
      .then(async (response) => {
    
        const data = await response.json();
    
        console.log(data);
    
      })
    
      .catch(err => console.error(err));

JS

Copy
    
    
    import java.io.IOException;
    
    import java.net.URI;
    
    import java.net.http.*;
    
    
    
    
    public class ApiExample {
    
        public static void main(String[] args) throws IOException, InterruptedException {
    
            HttpRequest request = HttpRequest.newBuilder()
    
                .uri(URI.create("https://api.canva.com/print/v1/events/order-shipment"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 25}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}, {\"tracking_number\": \"987654321\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 25}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}"))
    
                .build();
    
    
    
    
            HttpResponse<String> response = HttpClient.newHttpClient().send(
    
                request,
    
                HttpResponse.BodyHandlers.ofString()
    
            );
    
            System.out.println(response.body());
    
        }
    
    }

JAVA

Copy
    
    
    import requests
    
    
    
    
    headers = {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28="
    
    }
    
    
    
    
    data = {
    
        "request_type": "shipment_event",
    
        "order_reference_id": "FO123456789",
    
        "shipments": [
    
            {
    
                "tracking_number": "123456789",
    
                "carrier": "fedex",
    
                "items": [
    
                    {
    
                        "item_reference_id": "FI123456789",
    
                        "quantity": 25
    
                    }
    
                ],
    
                "dispatched_at": 1726448251,
    
                "dispatch_location_reference": "partnerLocation1234"
    
            },
    
            {
    
                "tracking_number": "987654321",
    
                "carrier": "fedex",
    
                "items": [
    
                    {
    
                        "item_reference_id": "FI123456789",
    
                        "quantity": 25
    
                    }
    
                ],
    
                "dispatched_at": 1726448251,
    
                "dispatch_location_reference": "partnerLocation1234"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/print/v1/events/order-shipment",
    
        headers=headers,
    
        json=data
    
    )
    
    print(response.json())

PY

Copy
    
    
    using System.Net.Http;
    
    
    
    
    var client = new HttpClient();
    
    var request = new HttpRequestMessage
    
    {
    
      Method = HttpMethod.Post,
    
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-shipment"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
    
      },
    
      Content = new StringContent(
    
        "{\"request_type\": \"shipment_event\", \"order_reference_id\": \"FO123456789\", \"shipments\": [{\"tracking_number\": \"123456789\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 25}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}, {\"tracking_number\": \"987654321\", \"carrier\": \"fedex\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"quantity\": 25}], \"dispatched_at\": 1726448251, \"dispatch_location_reference\": \"partnerLocation1234\"}]}",
    
        Encoding.UTF8,
    
        "application/json"
    
      ),
    
    };
    
    
    
    
    using (var response = await client.SendAsync(request))
    
    {
    
      response.EnsureSuccessStatusCode();
    
      var body = await response.Content.ReadAsStringAsync();
    
      Console.WriteLine(body);
    
    };

CSHARP

Copy
    
    
    package main
    
    
    
    
    import (
    
    	"fmt"
    
    	"io"
    
    	"net/http"
    
    	"strings"
    
    )
    
    
    
    
    func main() {
    
    	payload := strings.NewReader(`{
    
    	  "request_type": "shipment_event",
    
    	  "order_reference_id": "FO123456789",
    
    	  "shipments": [
    
    	    {
    
    	      "tracking_number": "123456789",
    
    	      "carrier": "fedex",
    
    	      "items": [
    
    	        {
    
    	          "item_reference_id": "FI123456789",
    
    	          "quantity": 25
    
    	        }
    
    	      ],
    
    	      "dispatched_at": 1726448251,
    
    	      "dispatch_location_reference": "partnerLocation1234"
    
    	    },
    
    	    {
    
    	      "tracking_number": "987654321",
    
    	      "carrier": "fedex",
    
    	      "items": [
    
    	        {
    
    	          "item_reference_id": "FI123456789",
    
    	          "quantity": 25
    
    	        }
    
    	      ],
    
    	      "dispatched_at": 1726448251,
    
    	      "dispatch_location_reference": "partnerLocation1234"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/print/v1/events/order-shipment"
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer {token}")
    
    	req.Header.Add("Content-Type", "application/json")
    
    	req.Header.Add("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
    
    
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }

GO

Copy
    
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
    
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-shipment",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "request_type" => "shipment_event",
    
        "order_reference_id" => "FO123456789",
    
        "shipments" => [
    
          [
    
            "tracking_number" => "123456789",
    
            "carrier" => "fedex",
    
            "items" => [
    
              [
    
                "item_reference_id" => "FI123456789",
    
                "quantity" => 25
    
              ]
    
            ],
    
            "dispatched_at" => 1726448251,
    
            "dispatch_location_reference" => "partnerLocation1234"
    
          ],
    
          [
    
            "tracking_number" => "987654321",
    
            "carrier" => "fedex",
    
            "items" => [
    
              [
    
                "item_reference_id" => "FI123456789",
    
                "quantity" => 25
    
              ]
    
            ],
    
            "dispatched_at" => 1726448251,
    
            "dispatch_location_reference" => "partnerLocation1234"
    
          ]
    
        ]
    
      ])
    
    ));
    
    
    
    
    $response = curl_exec($curl);
    
    $err = curl_error($curl);
    
    curl_close($curl);
    
    
    
    
    if (empty($err)) {
    
      echo $response;
    
    } else {
    
      echo "Error: " . $err;
    
    }

PHP

Copy
    
    
    require 'net/http'
    
    require 'uri'
    
    
    
    
    url = URI('https://api.canva.com/print/v1/events/order-shipment')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    
    request.body = <<REQUEST_BODY
    
    {
    
      "request_type": "shipment_event",
    
      "order_reference_id": "FO123456789",
    
      "shipments": [
    
        {
    
          "tracking_number": "123456789",
    
          "carrier": "fedex",
    
          "items": [
    
            {
    
              "item_reference_id": "FI123456789",
    
              "quantity": 25
    
            }
    
          ],
    
          "dispatched_at": 1726448251,
    
          "dispatch_location_reference": "partnerLocation1234"
    
        },
    
        {
    
          "tracking_number": "987654321",
    
          "carrier": "fedex",
    
          "items": [
    
            {
    
              "item_reference_id": "FI123456789",
    
              "quantity": 25
    
            }
    
          ],
    
          "dispatched_at": 1726448251,
    
          "dispatch_location_reference": "partnerLocation1234"
    
        }
    
      ]
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

If successful, the endpoint returns the status code `204 No content` without a response body.

## Error responses

### 400 Invalid request. For example, an invalid data format.

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically.

**Available values:**

  * `invalid_field`
  * `invalid_header_value`
  * `invalid_request`
  * `permission_denied`
  * `too_many_requests`
  * `not_found`
  * `bad_request_body`
  * `bad_http_method`
  * `bad_request_params`
  * `bad_query_params`
  * `endpoint_not_found`
  * `unsupported_version`
  * `invalid_access_token`
  * `revoked_access_token`
  * `invalid_client`
  * `unauthorized_client`
  * `invalid_basic_header`



`message``string`

A human-readable description of what went wrong.

#### Example error response

##### Bad request
    
    
    {
    
      "code": "invalid_request",
    
      "message": "The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed."
    
    }

JSON

Copy

### 401 Invalid or unauthorized client ID or secret.

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically.

**Available values:**

  * `invalid_field`
  * `invalid_header_value`
  * `invalid_request`
  * `permission_denied`
  * `too_many_requests`
  * `not_found`
  * `bad_request_body`
  * `bad_http_method`
  * `bad_request_params`
  * `bad_query_params`
  * `endpoint_not_found`
  * `unsupported_version`
  * `invalid_access_token`
  * `revoked_access_token`
  * `invalid_client`
  * `unauthorized_client`
  * `invalid_basic_header`



`message``string`

A human-readable description of what went wrong.

#### Example error response

##### Unauthorized
    
    
    {
    
      "code": "unauthorized_client",
    
      "message": "The client is not authorized for action."
    
    }

JSON

Copy

### 403 Partner has no access to the order.

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically.

**Available values:**

  * `invalid_field`
  * `invalid_header_value`
  * `invalid_request`
  * `permission_denied`
  * `too_many_requests`
  * `not_found`
  * `bad_request_body`
  * `bad_http_method`
  * `bad_request_params`
  * `bad_query_params`
  * `endpoint_not_found`
  * `unsupported_version`
  * `invalid_access_token`
  * `revoked_access_token`
  * `invalid_client`
  * `unauthorized_client`
  * `invalid_basic_header`



`message``string`

A human-readable description of what went wrong.

#### Example error response

##### Forbidden
    
    
    {
    
      "code": "permission_denied",
    
      "message": "The resource owner or authorization server denied the request."
    
    }

JSON

Copy
