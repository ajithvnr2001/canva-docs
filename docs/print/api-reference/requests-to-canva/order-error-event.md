---
url: https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-error-event/
title: Create order error event - Requests to Canva - Canva Print API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:35.326869+00:00
---

# Create order error event - Requests to Canva - Canva Print API Documentation

> Source: https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-error-event/

Requests to Canva

[Overview](https://www.canva.dev/docs/print/api-reference/requests-to-canva/)[Generate access token](https://www.canva.dev/docs/print/api-reference/requests-to-canva/oauth/generate-access-token/)[Create order production event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-production-event/)[Create order shipment event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-shipment-event/)[Create order cost summary event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-cost-summary-event/)[Create order error event](https://www.canva.dev/docs/print/api-reference/requests-to-canva/order-error-event/)[Get signing keys](https://www.canva.dev/docs/print/api-reference/requests-to-canva/keys/)

# Create order error event

Copy page

Creates an event to notify Canva about errors and issues for an order in the print partner's system.

## HTTP method and URL path

POST` https://api.canva.com/print/v1/events/order-error`

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

**Available values:** The only valid value is `error_event`.

`order_reference_id``string`

Required

A unique, case-sensitive ID of the order in Canva's system. This must be the same value as the `orderReferenceId` path parameter.

**Maximum length:** `255`

`items``ItemErrorEvent[]`

Required

A list of updates to items in the order.

**Minimum items:** `1`

Properties of **items**

`item_reference_id``string`

Required

A unique, case-sensitive ID for an order item that the print partner can use when communicating with Canva.

**Maximum length:** `255`

`error_details``ErrorDetails`

Required

The error details of the item. Errors details should be cleared from an item after it has been resolved.

Properties of **error_details**

`issue_origin``string`

Required

The origin of the issue.

**Available values:**

  * `production`
  * `order_url`
  * `user_details`
  * `user_address`
  * `delivery`
  * `unknown`



`description``string`

Required

A human readable message that describes the cause of the error.

**Maximum length:** `255`

## Example requests

### Single item, single error

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/print/v1/events/order-error' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    
    --data '{
    
      "request_type": "error_event",
    
      "order_reference_id": "FO123456789",
    
      "items": [
    
        {
    
          "item_reference_id": "FI123456789",
    
          "error_details": {
    
            "issue_origin": "user_address",
    
            "description": "Address cannot be found. Please specify a valid delivery address."
    
          }
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/print/v1/events/order-error", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
    
      },
    
      body: JSON.stringify({
    
        "request_type": "error_event",
    
        "order_reference_id": "FO123456789",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "error_details": {
    
              "issue_origin": "user_address",
    
              "description": "Address cannot be found. Please specify a valid delivery address."
    
            }
    
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
    
                .uri(URI.create("https://api.canva.com/print/v1/events/order-error"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"error_event\", \"order_reference_id\": \"FO123456789\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"error_details\": {\"issue_origin\": \"user_address\", \"description\": \"Address cannot be found. Please specify a valid delivery address.\"}}]}"))
    
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
    
        "request_type": "error_event",
    
        "order_reference_id": "FO123456789",
    
        "items": [
    
            {
    
                "item_reference_id": "FI123456789",
    
                "error_details": {
    
                    "issue_origin": "user_address",
    
                    "description": "Address cannot be found. Please specify a valid delivery address."
    
                }
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/print/v1/events/order-error",
    
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
    
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-error"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
    
      },
    
      Content = new StringContent(
    
        "{\"request_type\": \"error_event\", \"order_reference_id\": \"FO123456789\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"error_details\": {\"issue_origin\": \"user_address\", \"description\": \"Address cannot be found. Please specify a valid delivery address.\"}}]}",
    
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
    
    	  "request_type": "error_event",
    
    	  "order_reference_id": "FO123456789",
    
    	  "items": [
    
    	    {
    
    	      "item_reference_id": "FI123456789",
    
    	      "error_details": {
    
    	        "issue_origin": "user_address",
    
    	        "description": "Address cannot be found. Please specify a valid delivery address."
    
    	      }
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/print/v1/events/order-error"
    
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
    
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-error",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "request_type" => "error_event",
    
        "order_reference_id" => "FO123456789",
    
        "items" => [
    
          [
    
            "item_reference_id" => "FI123456789",
    
            "error_details" => [
    
              "issue_origin" => "user_address",
    
              "description" => "Address cannot be found. Please specify a valid delivery address."
    
            ]
    
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
    
    
    
    
    url = URI('https://api.canva.com/print/v1/events/order-error')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    
    request.body = <<REQUEST_BODY
    
    {
    
      "request_type": "error_event",
    
      "order_reference_id": "FO123456789",
    
      "items": [
    
        {
    
          "item_reference_id": "FI123456789",
    
          "error_details": {
    
            "issue_origin": "user_address",
    
            "description": "Address cannot be found. Please specify a valid delivery address."
    
          }
    
        }
    
      ]
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

### Multi item, multi error

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/print/v1/events/order-error' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --header 'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=' \
    
    --data '{
    
      "request_type": "error_event",
    
      "order_reference_id": "FO123456789",
    
      "items": [
    
        {
    
          "item_reference_id": "FI123456789",
    
          "error_details": {
    
            "issue_origin": "user_address",
    
            "description": "Address cannot be found. Please specify a valid delivery address."
    
          }
    
        },
    
        {
    
          "item_reference_id": "F987654321",
    
          "error_details": {
    
            "issue_origin": "user_address",
    
            "description": "Address cannot be found. Please specify a valid delivery address."
    
          }
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/print/v1/events/order-error", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
        "X-Canva-Print-Client-Id": "Ym9zY236Ym9zY28=",
    
      },
    
      body: JSON.stringify({
    
        "request_type": "error_event",
    
        "order_reference_id": "FO123456789",
    
        "items": [
    
          {
    
            "item_reference_id": "FI123456789",
    
            "error_details": {
    
              "issue_origin": "user_address",
    
              "description": "Address cannot be found. Please specify a valid delivery address."
    
            }
    
          },
    
          {
    
            "item_reference_id": "F987654321",
    
            "error_details": {
    
              "issue_origin": "user_address",
    
              "description": "Address cannot be found. Please specify a valid delivery address."
    
            }
    
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
    
                .uri(URI.create("https://api.canva.com/print/v1/events/order-error"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .header("X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"request_type\": \"error_event\", \"order_reference_id\": \"FO123456789\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"error_details\": {\"issue_origin\": \"user_address\", \"description\": \"Address cannot be found. Please specify a valid delivery address.\"}}, {\"item_reference_id\": \"F987654321\", \"error_details\": {\"issue_origin\": \"user_address\", \"description\": \"Address cannot be found. Please specify a valid delivery address.\"}}]}"))
    
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
    
        "request_type": "error_event",
    
        "order_reference_id": "FO123456789",
    
        "items": [
    
            {
    
                "item_reference_id": "FI123456789",
    
                "error_details": {
    
                    "issue_origin": "user_address",
    
                    "description": "Address cannot be found. Please specify a valid delivery address."
    
                }
    
            },
    
            {
    
                "item_reference_id": "F987654321",
    
                "error_details": {
    
                    "issue_origin": "user_address",
    
                    "description": "Address cannot be found. Please specify a valid delivery address."
    
                }
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/print/v1/events/order-error",
    
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
    
      RequestUri = new Uri("https://api.canva.com/print/v1/events/order-error"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
        { "X-Canva-Print-Client-Id", "Ym9zY236Ym9zY28=" },
    
      },
    
      Content = new StringContent(
    
        "{\"request_type\": \"error_event\", \"order_reference_id\": \"FO123456789\", \"items\": [{\"item_reference_id\": \"FI123456789\", \"error_details\": {\"issue_origin\": \"user_address\", \"description\": \"Address cannot be found. Please specify a valid delivery address.\"}}, {\"item_reference_id\": \"F987654321\", \"error_details\": {\"issue_origin\": \"user_address\", \"description\": \"Address cannot be found. Please specify a valid delivery address.\"}}]}",
    
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
    
    	  "request_type": "error_event",
    
    	  "order_reference_id": "FO123456789",
    
    	  "items": [
    
    	    {
    
    	      "item_reference_id": "FI123456789",
    
    	      "error_details": {
    
    	        "issue_origin": "user_address",
    
    	        "description": "Address cannot be found. Please specify a valid delivery address."
    
    	      }
    
    	    },
    
    	    {
    
    	      "item_reference_id": "F987654321",
    
    	      "error_details": {
    
    	        "issue_origin": "user_address",
    
    	        "description": "Address cannot be found. Please specify a valid delivery address."
    
    	      }
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/print/v1/events/order-error"
    
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
    
      CURLOPT_URL => "https://api.canva.com/print/v1/events/order-error",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
        'X-Canva-Print-Client-Id: Ym9zY236Ym9zY28=',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "request_type" => "error_event",
    
        "order_reference_id" => "FO123456789",
    
        "items" => [
    
          [
    
            "item_reference_id" => "FI123456789",
    
            "error_details" => [
    
              "issue_origin" => "user_address",
    
              "description" => "Address cannot be found. Please specify a valid delivery address."
    
            ]
    
          ],
    
          [
    
            "item_reference_id" => "F987654321",
    
            "error_details" => [
    
              "issue_origin" => "user_address",
    
              "description" => "Address cannot be found. Please specify a valid delivery address."
    
            ]
    
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
    
    
    
    
    url = URI('https://api.canva.com/print/v1/events/order-error')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request['X-Canva-Print-Client-Id'] = 'Ym9zY236Ym9zY28='
    
    request.body = <<REQUEST_BODY
    
    {
    
      "request_type": "error_event",
    
      "order_reference_id": "FO123456789",
    
      "items": [
    
        {
    
          "item_reference_id": "FI123456789",
    
          "error_details": {
    
            "issue_origin": "user_address",
    
            "description": "Address cannot be found. Please specify a valid delivery address."
    
          }
    
        },
    
        {
    
          "item_reference_id": "F987654321",
    
          "error_details": {
    
            "issue_origin": "user_address",
    
            "description": "Address cannot be found. Please specify a valid delivery address."
    
          }
    
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
