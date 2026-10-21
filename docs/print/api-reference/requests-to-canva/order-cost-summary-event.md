---
url: https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-cost-summary-event/
title: Create order cost summary event - Requests to Canva - Canva Print API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:33.638834+00:00
---

# Create order cost summary event - Requests to Canva - Canva Print API Documentation

> Source: https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-cost-summary-event/

Requests to Canva

[Overview](https://www.canva.dev/docs/print/api-reference/requests-to-canva/)[Generate access token](https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/)[Create order production event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-production-event/)[Create order shipment event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-shipment-event/)[Create order cost summary event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-cost-summary-event/)[Create order error event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-error-event/)[Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/)

# Create order cost summary event

Copy page

Creates an event to notify Canva about the break down of costs and taxes for an order in the print partner's system.

It's expected that partners will send a cost summary after the order is completely shipped or is ready for pickup. Partners can omit shipment cost information for shipments that use Canva-provided shipping accounts.

This endpoint isn't a replacement for the established invoicing flow. This endpoint is for tracking purposes only, and isn't associated with any payable account.

## HTTP method and URL path

POST` https://api.canva.com/print/v1/events/order-cost-summary`

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

The type of request.

**Available values:** The only valid value is `cost_summary_event`.

`order_reference_id``string`

Required

A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

**Maximum length:** `255`

`pre_tax_total_major_units``string`

Required

Total cost (excluding tax) of the order. This is value must be:

  * In major units.
  * In the currency provided.
  * A numerical value. The currency symbol must be omitted.



**Maximum length:** `255`

`tax_major_units``string`

Required

Total tax of the order. This is value must be:

  * In major units.
  * In the currency provided.
  * A numerical value. The currency symbol must be omitted.



**Maximum length:** `255`

`post_tax_total_major_units``string`

Required

Total cost (including tax) of the order. This is value must be:

  * In major units.
  * In the currency provided.
  * A numerical value. The currency symbol must be omitted.



**Maximum length:** `255`

`currency``string`

Required

ISO 4217 currency code for the values provided in the cost summary.

**Maximum length:** `3`

`order_cost_items``OrderCostItem[]`

Required

A break down of the cost components included in the cost summary.

**Minimum items:** `1`

Properties of **order_cost_items**

`type``string`

Required

The type of the cost item.

**Available values:**

  * `product`
  * `add_on`
  * `packaging`
  * `shipment`



`cost_major_units``string`

Required

Total cost (excluding tax) of the cost item. This is value must be:

  * In major units.
  * In the currency provided.
  * A numerical value. The currency symbol must be omitted.



**Maximum length:** `255`

`tax_major_units``string`

Required

Total tax of the cost item. This is value must be:

  * In major units.
  * In the currency provided.
  * A numerical value. The currency symbol must be omitted.



**Maximum length:** `255`

`total_major_units``string`

Required

Total cost (including tax) of the cost item. This is value must be:

  * In major units.
  * In the currency provided.
  * A numerical value. The currency symbol must be omitted.



**Maximum length:** `255`

`currency``string`

Required

ISO 4217 currency code for the values provided in the cost summary.

**Maximum length:** `3`

`item_reference_id``string`

Optional

A unique, case-sensitive ID for an order item that the print partner can use when communicating with Canva. This is only provided when the `OrderCostItem` is a `product`, `add_on`, or `packaging`.

**Maximum length:** `255`

`tracking_number``string`

Optional

The tracking number provided by the carrier. This is only provided when the `OrderCostItem` is a `shipment`.

**Maximum length:** `255`

`handling_major_units``string`

Optional

The total cost (excluding tax) of the handling component of the cost item. This is value must be:

  * In major units.
  * In the currency provided.
  * A numerical value. The currency symbol must be omitted.



**Maximum length:** `255`

## Example requests

### Delivery order: multiple items, multiple shipments

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/print/v1/events/order-cost-summary' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    
    --data '{
    
      "request_type": "cost_summary_event",
    
      "order_reference_id": "FB123456789",
    
      "handling_major_units": "0.35",
    
      "pre_tax_total_major_units": "16.02",
    
      "tax_major_units": "1.75",
    
      "post_tax_total_major_units": "17.77",
    
      "currency": "USD",
    
      "order_cost_items": [
    
        {
    
          "type": "product",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "product",
    
          "item_reference_id": "FI123456788",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456788",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "shipment",
    
          "tracking_number": "TR12345671",
    
          "cost_major_units": "4.55",
    
          "tax_major_units": "0.45",
    
          "total_major_units": "5.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "shipment",
    
          "tracking_number": "TR12345672",
    
          "cost_major_units": "3.12",
    
          "tax_major_units": "0.42",
    
          "total_major_units": "3.54",
    
          "currency": "USD"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/print/v1/events/order-cost-summary", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
    
      },
    
      body: JSON.stringify({
    
        "request_type": "cost_summary_event",
    
        "order_reference_id": "FB123456789",
    
        "handling_major_units": "0.35",
    
        "pre_tax_total_major_units": "16.02",
    
        "tax_major_units": "1.75",
    
        "post_tax_total_major_units": "17.77",
    
        "currency": "USD",
    
        "order_cost_items": [
    
          {
    
            "type": "product",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "3.60",
    
            "tax_major_units": "0.40",
    
            "total_major_units": "4.00",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "packaging",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "0.40",
    
            "tax_major_units": "0.04",
    
            "total_major_units": "0.44",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "product",
    
            "item_reference_id": "FI123456788",
    
            "cost_major_units": "3.60",
    
            "tax_major_units": "0.40",
    
            "total_major_units": "4.00",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "packaging",
    
            "item_reference_id": "FI123456788",
    
            "cost_major_units": "0.40",
    
            "tax_major_units": "0.04",
    
            "total_major_units": "0.44",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "shipment",
    
            "tracking_number": "TR12345671",
    
            "cost_major_units": "4.55",
    
            "tax_major_units": "0.45",
    
            "total_major_units": "5.00",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "shipment",
    
            "tracking_number": "TR12345672",
    
            "cost_major_units": "3.12",
    
            "tax_major_units": "0.42",
    
            "total_major_units": "3.54",
    
            "currency": "USD"
    
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
    
                .uri(URI.create("https://api.canva.com/print/v1/events/order-cost-summary"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"cost_summary_event\", \"order_reference_id\": \"FB123456789\", \"handling_major_units\": \"0.35\", \"pre_tax_total_major_units\": \"16.02\", \"tax_major_units\": \"1.75\", \"post_tax_total_major_units\": \"17.77\", \"currency\": \"USD\", \"order_cost_items\": [{\"type\": \"product\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"product\", \"item_reference_id\": \"FI123456788\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456788\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"shipment\", \"tracking_number\": \"TR12345671\", \"cost_major_units\": \"4.55\", \"tax_major_units\": \"0.45\", \"total_major_units\": \"5.00\", \"currency\": \"USD\"}, {\"type\": \"shipment\", \"tracking_number\": \"TR12345672\", \"cost_major_units\": \"3.12\", \"tax_major_units\": \"0.42\", \"total_major_units\": \"3.54\", \"currency\": \"USD\"}]}"))
    
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
    
        "request_type": "cost_summary_event",
    
        "order_reference_id": "FB123456789",
    
        "handling_major_units": "0.35",
    
        "pre_tax_total_major_units": "16.02",
    
        "tax_major_units": "1.75",
    
        "post_tax_total_major_units": "17.77",
    
        "currency": "USD",
    
        "order_cost_items": [
    
            {
    
                "type": "product",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "3.60",
    
                "tax_major_units": "0.40",
    
                "total_major_units": "4.00",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "packaging",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "0.40",
    
                "tax_major_units": "0.04",
    
                "total_major_units": "0.44",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "product",
    
                "item_reference_id": "FI123456788",
    
                "cost_major_units": "3.60",
    
                "tax_major_units": "0.40",
    
                "total_major_units": "4.00",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "packaging",
    
                "item_reference_id": "FI123456788",
    
                "cost_major_units": "0.40",
    
                "tax_major_units": "0.04",
    
                "total_major_units": "0.44",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "shipment",
    
                "tracking_number": "TR12345671",
    
                "cost_major_units": "4.55",
    
                "tax_major_units": "0.45",
    
                "total_major_units": "5.00",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "shipment",
    
                "tracking_number": "TR12345672",
    
                "cost_major_units": "3.12",
    
                "tax_major_units": "0.42",
    
                "total_major_units": "3.54",
    
                "currency": "USD"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/print/v1/events/order-cost-summary",
    
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
    
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-cost-summary"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
    
      },
    
      Content = new StringContent(
    
        "{\"request_type\": \"cost_summary_event\", \"order_reference_id\": \"FB123456789\", \"handling_major_units\": \"0.35\", \"pre_tax_total_major_units\": \"16.02\", \"tax_major_units\": \"1.75\", \"post_tax_total_major_units\": \"17.77\", \"currency\": \"USD\", \"order_cost_items\": [{\"type\": \"product\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"product\", \"item_reference_id\": \"FI123456788\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456788\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"shipment\", \"tracking_number\": \"TR12345671\", \"cost_major_units\": \"4.55\", \"tax_major_units\": \"0.45\", \"total_major_units\": \"5.00\", \"currency\": \"USD\"}, {\"type\": \"shipment\", \"tracking_number\": \"TR12345672\", \"cost_major_units\": \"3.12\", \"tax_major_units\": \"0.42\", \"total_major_units\": \"3.54\", \"currency\": \"USD\"}]}",
    
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
    
    	  "request_type": "cost_summary_event",
    
    	  "order_reference_id": "FB123456789",
    
    	  "handling_major_units": "0.35",
    
    	  "pre_tax_total_major_units": "16.02",
    
    	  "tax_major_units": "1.75",
    
    	  "post_tax_total_major_units": "17.77",
    
    	  "currency": "USD",
    
    	  "order_cost_items": [
    
    	    {
    
    	      "type": "product",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "3.60",
    
    	      "tax_major_units": "0.40",
    
    	      "total_major_units": "4.00",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "packaging",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "0.40",
    
    	      "tax_major_units": "0.04",
    
    	      "total_major_units": "0.44",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "product",
    
    	      "item_reference_id": "FI123456788",
    
    	      "cost_major_units": "3.60",
    
    	      "tax_major_units": "0.40",
    
    	      "total_major_units": "4.00",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "packaging",
    
    	      "item_reference_id": "FI123456788",
    
    	      "cost_major_units": "0.40",
    
    	      "tax_major_units": "0.04",
    
    	      "total_major_units": "0.44",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "shipment",
    
    	      "tracking_number": "TR12345671",
    
    	      "cost_major_units": "4.55",
    
    	      "tax_major_units": "0.45",
    
    	      "total_major_units": "5.00",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "shipment",
    
    	      "tracking_number": "TR12345672",
    
    	      "cost_major_units": "3.12",
    
    	      "tax_major_units": "0.42",
    
    	      "total_major_units": "3.54",
    
    	      "currency": "USD"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/print/v1/events/order-cost-summary"
    
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
    
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-cost-summary",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "request_type" => "cost_summary_event",
    
        "order_reference_id" => "FB123456789",
    
        "handling_major_units" => "0.35",
    
        "pre_tax_total_major_units" => "16.02",
    
        "tax_major_units" => "1.75",
    
        "post_tax_total_major_units" => "17.77",
    
        "currency" => "USD",
    
        "order_cost_items" => [
    
          [
    
            "type" => "product",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "3.60",
    
            "tax_major_units" => "0.40",
    
            "total_major_units" => "4.00",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "packaging",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "0.40",
    
            "tax_major_units" => "0.04",
    
            "total_major_units" => "0.44",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "product",
    
            "item_reference_id" => "FI123456788",
    
            "cost_major_units" => "3.60",
    
            "tax_major_units" => "0.40",
    
            "total_major_units" => "4.00",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "packaging",
    
            "item_reference_id" => "FI123456788",
    
            "cost_major_units" => "0.40",
    
            "tax_major_units" => "0.04",
    
            "total_major_units" => "0.44",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "shipment",
    
            "tracking_number" => "TR12345671",
    
            "cost_major_units" => "4.55",
    
            "tax_major_units" => "0.45",
    
            "total_major_units" => "5.00",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "shipment",
    
            "tracking_number" => "TR12345672",
    
            "cost_major_units" => "3.12",
    
            "tax_major_units" => "0.42",
    
            "total_major_units" => "3.54",
    
            "currency" => "USD"
    
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
    
    
    
    
    url = URI('https://api.canva.com/print/v1/events/order-cost-summary')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    
    request.body = <<REQUEST_BODY
    
    {
    
      "request_type": "cost_summary_event",
    
      "order_reference_id": "FB123456789",
    
      "handling_major_units": "0.35",
    
      "pre_tax_total_major_units": "16.02",
    
      "tax_major_units": "1.75",
    
      "post_tax_total_major_units": "17.77",
    
      "currency": "USD",
    
      "order_cost_items": [
    
        {
    
          "type": "product",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "product",
    
          "item_reference_id": "FI123456788",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456788",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "shipment",
    
          "tracking_number": "TR12345671",
    
          "cost_major_units": "4.55",
    
          "tax_major_units": "0.45",
    
          "total_major_units": "5.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "shipment",
    
          "tracking_number": "TR12345672",
    
          "cost_major_units": "3.12",
    
          "tax_major_units": "0.42",
    
          "total_major_units": "3.54",
    
          "currency": "USD"
    
        }
    
      ]
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

### Delivery order with add on

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/print/v1/events/order-cost-summary' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    
    --data '{
    
      "request_type": "cost_summary_event",
    
      "order_reference_id": "FB123456789",
    
      "handling_major_units": "0.35",
    
      "pre_tax_total_major_units": "16.02",
    
      "tax_major_units": "1.75",
    
      "post_tax_total_major_units": "17.77",
    
      "currency": "USD",
    
      "order_cost_items": [
    
        {
    
          "type": "product",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "add_on",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "shipment",
    
          "tracking_number": "TR12345671",
    
          "cost_major_units": "4.55",
    
          "tax_major_units": "0.45",
    
          "total_major_units": "5.00",
    
          "currency": "USD"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/print/v1/events/order-cost-summary", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
    
      },
    
      body: JSON.stringify({
    
        "request_type": "cost_summary_event",
    
        "order_reference_id": "FB123456789",
    
        "handling_major_units": "0.35",
    
        "pre_tax_total_major_units": "16.02",
    
        "tax_major_units": "1.75",
    
        "post_tax_total_major_units": "17.77",
    
        "currency": "USD",
    
        "order_cost_items": [
    
          {
    
            "type": "product",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "3.60",
    
            "tax_major_units": "0.40",
    
            "total_major_units": "4.00",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "packaging",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "0.40",
    
            "tax_major_units": "0.04",
    
            "total_major_units": "0.44",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "add_on",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "3.60",
    
            "tax_major_units": "0.40",
    
            "total_major_units": "4.00",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "packaging",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "0.40",
    
            "tax_major_units": "0.04",
    
            "total_major_units": "0.44",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "shipment",
    
            "tracking_number": "TR12345671",
    
            "cost_major_units": "4.55",
    
            "tax_major_units": "0.45",
    
            "total_major_units": "5.00",
    
            "currency": "USD"
    
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
    
                .uri(URI.create("https://api.canva.com/print/v1/events/order-cost-summary"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"cost_summary_event\", \"order_reference_id\": \"FB123456789\", \"handling_major_units\": \"0.35\", \"pre_tax_total_major_units\": \"16.02\", \"tax_major_units\": \"1.75\", \"post_tax_total_major_units\": \"17.77\", \"currency\": \"USD\", \"order_cost_items\": [{\"type\": \"product\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"add_on\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"shipment\", \"tracking_number\": \"TR12345671\", \"cost_major_units\": \"4.55\", \"tax_major_units\": \"0.45\", \"total_major_units\": \"5.00\", \"currency\": \"USD\"}]}"))
    
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
    
        "request_type": "cost_summary_event",
    
        "order_reference_id": "FB123456789",
    
        "handling_major_units": "0.35",
    
        "pre_tax_total_major_units": "16.02",
    
        "tax_major_units": "1.75",
    
        "post_tax_total_major_units": "17.77",
    
        "currency": "USD",
    
        "order_cost_items": [
    
            {
    
                "type": "product",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "3.60",
    
                "tax_major_units": "0.40",
    
                "total_major_units": "4.00",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "packaging",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "0.40",
    
                "tax_major_units": "0.04",
    
                "total_major_units": "0.44",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "add_on",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "3.60",
    
                "tax_major_units": "0.40",
    
                "total_major_units": "4.00",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "packaging",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "0.40",
    
                "tax_major_units": "0.04",
    
                "total_major_units": "0.44",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "shipment",
    
                "tracking_number": "TR12345671",
    
                "cost_major_units": "4.55",
    
                "tax_major_units": "0.45",
    
                "total_major_units": "5.00",
    
                "currency": "USD"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/print/v1/events/order-cost-summary",
    
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
    
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-cost-summary"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
    
      },
    
      Content = new StringContent(
    
        "{\"request_type\": \"cost_summary_event\", \"order_reference_id\": \"FB123456789\", \"handling_major_units\": \"0.35\", \"pre_tax_total_major_units\": \"16.02\", \"tax_major_units\": \"1.75\", \"post_tax_total_major_units\": \"17.77\", \"currency\": \"USD\", \"order_cost_items\": [{\"type\": \"product\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"add_on\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"shipment\", \"tracking_number\": \"TR12345671\", \"cost_major_units\": \"4.55\", \"tax_major_units\": \"0.45\", \"total_major_units\": \"5.00\", \"currency\": \"USD\"}]}",
    
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
    
    	  "request_type": "cost_summary_event",
    
    	  "order_reference_id": "FB123456789",
    
    	  "handling_major_units": "0.35",
    
    	  "pre_tax_total_major_units": "16.02",
    
    	  "tax_major_units": "1.75",
    
    	  "post_tax_total_major_units": "17.77",
    
    	  "currency": "USD",
    
    	  "order_cost_items": [
    
    	    {
    
    	      "type": "product",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "3.60",
    
    	      "tax_major_units": "0.40",
    
    	      "total_major_units": "4.00",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "packaging",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "0.40",
    
    	      "tax_major_units": "0.04",
    
    	      "total_major_units": "0.44",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "add_on",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "3.60",
    
    	      "tax_major_units": "0.40",
    
    	      "total_major_units": "4.00",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "packaging",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "0.40",
    
    	      "tax_major_units": "0.04",
    
    	      "total_major_units": "0.44",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "shipment",
    
    	      "tracking_number": "TR12345671",
    
    	      "cost_major_units": "4.55",
    
    	      "tax_major_units": "0.45",
    
    	      "total_major_units": "5.00",
    
    	      "currency": "USD"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/print/v1/events/order-cost-summary"
    
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
    
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-cost-summary",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "request_type" => "cost_summary_event",
    
        "order_reference_id" => "FB123456789",
    
        "handling_major_units" => "0.35",
    
        "pre_tax_total_major_units" => "16.02",
    
        "tax_major_units" => "1.75",
    
        "post_tax_total_major_units" => "17.77",
    
        "currency" => "USD",
    
        "order_cost_items" => [
    
          [
    
            "type" => "product",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "3.60",
    
            "tax_major_units" => "0.40",
    
            "total_major_units" => "4.00",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "packaging",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "0.40",
    
            "tax_major_units" => "0.04",
    
            "total_major_units" => "0.44",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "add_on",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "3.60",
    
            "tax_major_units" => "0.40",
    
            "total_major_units" => "4.00",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "packaging",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "0.40",
    
            "tax_major_units" => "0.04",
    
            "total_major_units" => "0.44",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "shipment",
    
            "tracking_number" => "TR12345671",
    
            "cost_major_units" => "4.55",
    
            "tax_major_units" => "0.45",
    
            "total_major_units" => "5.00",
    
            "currency" => "USD"
    
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
    
    
    
    
    url = URI('https://api.canva.com/print/v1/events/order-cost-summary')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    
    request.body = <<REQUEST_BODY
    
    {
    
      "request_type": "cost_summary_event",
    
      "order_reference_id": "FB123456789",
    
      "handling_major_units": "0.35",
    
      "pre_tax_total_major_units": "16.02",
    
      "tax_major_units": "1.75",
    
      "post_tax_total_major_units": "17.77",
    
      "currency": "USD",
    
      "order_cost_items": [
    
        {
    
          "type": "product",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "add_on",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "shipment",
    
          "tracking_number": "TR12345671",
    
          "cost_major_units": "4.55",
    
          "tax_major_units": "0.45",
    
          "total_major_units": "5.00",
    
          "currency": "USD"
    
        }
    
      ]
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

### Pickup order

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/print/v1/events/order-cost-summary' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    
    --data '{
    
      "request_type": "cost_summary_event",
    
      "order_reference_id": "FB123456789",
    
      "handling_major_units": "0.35",
    
      "pre_tax_total_major_units": "16.02",
    
      "tax_major_units": "1.75",
    
      "post_tax_total_major_units": "17.77",
    
      "currency": "USD",
    
      "order_cost_items": [
    
        {
    
          "type": "product",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "add_on",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/print/v1/events/order-cost-summary", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
    
      },
    
      body: JSON.stringify({
    
        "request_type": "cost_summary_event",
    
        "order_reference_id": "FB123456789",
    
        "handling_major_units": "0.35",
    
        "pre_tax_total_major_units": "16.02",
    
        "tax_major_units": "1.75",
    
        "post_tax_total_major_units": "17.77",
    
        "currency": "USD",
    
        "order_cost_items": [
    
          {
    
            "type": "product",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "3.60",
    
            "tax_major_units": "0.40",
    
            "total_major_units": "4.00",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "packaging",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "0.40",
    
            "tax_major_units": "0.04",
    
            "total_major_units": "0.44",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "add_on",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "3.60",
    
            "tax_major_units": "0.40",
    
            "total_major_units": "4.00",
    
            "currency": "USD"
    
          },
    
          {
    
            "type": "packaging",
    
            "item_reference_id": "FI123456789",
    
            "cost_major_units": "0.40",
    
            "tax_major_units": "0.04",
    
            "total_major_units": "0.44",
    
            "currency": "USD"
    
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
    
                .uri(URI.create("https://api.canva.com/print/v1/events/order-cost-summary"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"cost_summary_event\", \"order_reference_id\": \"FB123456789\", \"handling_major_units\": \"0.35\", \"pre_tax_total_major_units\": \"16.02\", \"tax_major_units\": \"1.75\", \"post_tax_total_major_units\": \"17.77\", \"currency\": \"USD\", \"order_cost_items\": [{\"type\": \"product\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"add_on\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}]}"))
    
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
    
        "request_type": "cost_summary_event",
    
        "order_reference_id": "FB123456789",
    
        "handling_major_units": "0.35",
    
        "pre_tax_total_major_units": "16.02",
    
        "tax_major_units": "1.75",
    
        "post_tax_total_major_units": "17.77",
    
        "currency": "USD",
    
        "order_cost_items": [
    
            {
    
                "type": "product",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "3.60",
    
                "tax_major_units": "0.40",
    
                "total_major_units": "4.00",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "packaging",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "0.40",
    
                "tax_major_units": "0.04",
    
                "total_major_units": "0.44",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "add_on",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "3.60",
    
                "tax_major_units": "0.40",
    
                "total_major_units": "4.00",
    
                "currency": "USD"
    
            },
    
            {
    
                "type": "packaging",
    
                "item_reference_id": "FI123456789",
    
                "cost_major_units": "0.40",
    
                "tax_major_units": "0.04",
    
                "total_major_units": "0.44",
    
                "currency": "USD"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/print/v1/events/order-cost-summary",
    
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
    
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-cost-summary"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
    
      },
    
      Content = new StringContent(
    
        "{\"request_type\": \"cost_summary_event\", \"order_reference_id\": \"FB123456789\", \"handling_major_units\": \"0.35\", \"pre_tax_total_major_units\": \"16.02\", \"tax_major_units\": \"1.75\", \"post_tax_total_major_units\": \"17.77\", \"currency\": \"USD\", \"order_cost_items\": [{\"type\": \"product\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}, {\"type\": \"add_on\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"3.60\", \"tax_major_units\": \"0.40\", \"total_major_units\": \"4.00\", \"currency\": \"USD\"}, {\"type\": \"packaging\", \"item_reference_id\": \"FI123456789\", \"cost_major_units\": \"0.40\", \"tax_major_units\": \"0.04\", \"total_major_units\": \"0.44\", \"currency\": \"USD\"}]}",
    
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
    
    	  "request_type": "cost_summary_event",
    
    	  "order_reference_id": "FB123456789",
    
    	  "handling_major_units": "0.35",
    
    	  "pre_tax_total_major_units": "16.02",
    
    	  "tax_major_units": "1.75",
    
    	  "post_tax_total_major_units": "17.77",
    
    	  "currency": "USD",
    
    	  "order_cost_items": [
    
    	    {
    
    	      "type": "product",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "3.60",
    
    	      "tax_major_units": "0.40",
    
    	      "total_major_units": "4.00",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "packaging",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "0.40",
    
    	      "tax_major_units": "0.04",
    
    	      "total_major_units": "0.44",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "add_on",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "3.60",
    
    	      "tax_major_units": "0.40",
    
    	      "total_major_units": "4.00",
    
    	      "currency": "USD"
    
    	    },
    
    	    {
    
    	      "type": "packaging",
    
    	      "item_reference_id": "FI123456789",
    
    	      "cost_major_units": "0.40",
    
    	      "tax_major_units": "0.04",
    
    	      "total_major_units": "0.44",
    
    	      "currency": "USD"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/print/v1/events/order-cost-summary"
    
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
    
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-cost-summary",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "request_type" => "cost_summary_event",
    
        "order_reference_id" => "FB123456789",
    
        "handling_major_units" => "0.35",
    
        "pre_tax_total_major_units" => "16.02",
    
        "tax_major_units" => "1.75",
    
        "post_tax_total_major_units" => "17.77",
    
        "currency" => "USD",
    
        "order_cost_items" => [
    
          [
    
            "type" => "product",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "3.60",
    
            "tax_major_units" => "0.40",
    
            "total_major_units" => "4.00",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "packaging",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "0.40",
    
            "tax_major_units" => "0.04",
    
            "total_major_units" => "0.44",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "add_on",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "3.60",
    
            "tax_major_units" => "0.40",
    
            "total_major_units" => "4.00",
    
            "currency" => "USD"
    
          ],
    
          [
    
            "type" => "packaging",
    
            "item_reference_id" => "FI123456789",
    
            "cost_major_units" => "0.40",
    
            "tax_major_units" => "0.04",
    
            "total_major_units" => "0.44",
    
            "currency" => "USD"
    
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
    
    
    
    
    url = URI('https://api.canva.com/print/v1/events/order-cost-summary')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    
    request.body = <<REQUEST_BODY
    
    {
    
      "request_type": "cost_summary_event",
    
      "order_reference_id": "FB123456789",
    
      "handling_major_units": "0.35",
    
      "pre_tax_total_major_units": "16.02",
    
      "tax_major_units": "1.75",
    
      "post_tax_total_major_units": "17.77",
    
      "currency": "USD",
    
      "order_cost_items": [
    
        {
    
          "type": "product",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "add_on",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "3.60",
    
          "tax_major_units": "0.40",
    
          "total_major_units": "4.00",
    
          "currency": "USD"
    
        },
    
        {
    
          "type": "packaging",
    
          "item_reference_id": "FI123456789",
    
          "cost_major_units": "0.40",
    
          "tax_major_units": "0.04",
    
          "total_major_units": "0.44",
    
          "currency": "USD"
    
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
