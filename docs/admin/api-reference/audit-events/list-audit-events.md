---
url: https://www.canva.dev/docs/admin/api-reference/audit-events/list-audit-events/
title: List audit events - Audit events - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:30.652327+00:00
---

# List audit events - Audit events - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/audit-events/list-audit-events/

Audit events

[List audit events](https://www.canva.dev/docs/admin/api-reference/audit-events/list-audit-events/)

# List audit events

Copy page

Lists audit events.

## HTTP method and URL path

GET` https://api.canva.com/admin/v1/audit-events`

## Authentication and authorization

This endpoint requires a valid access token that was generated using client credentials.

### Scopes

The access token must have all the following [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) (permissions):

  * `admin:auditevent:read`



## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

## Query parameters

`ingested_after``integer`

Optional

The inclusive lower limit for the time when audit events were ingested into the log (in seconds since the Unix Epoch). As this is based on the time when events were ingested, the returned list of events may contain some events that occurred before this timestamp.

`ingested_before``integer`

Optional

The exclusive upper limit for the time when audit events were ingested into the log (in seconds since the Unix Epoch). As this is based on the time when events were ingested, the returned list of events may contain some events that occurred after this timestamp.

`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list, for example `?continuation={continuation}`.

To retrieve all items, you might need to make multiple requests.

`limit``integer`

Optional

The maximum number of events to return.

**Minimum:** `1`

**Maximum:** `1000`

**Default value:** `50`

## Example request

Examples for using the `/v1/audit-events` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request GET 'https://api.canva.com/admin/v1/audit-events' \
    
    --header 'Authorization: Bearer {token}'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/audit-events", {
    
      method: "GET",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
      },
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/audit-events"))
    
                .header("Authorization", "Bearer {token}")
    
                .method("GET", HttpRequest.BodyPublishers.noBody())
    
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
    
        "Authorization": "Bearer {token}"
    
    }
    
    
    
    
    response = requests.get("https://api.canva.com/admin/v1/audit-events",
    
        headers=headers
    
    )
    
    print(response.json())

PY

Copy
    
    
    using System.Net.Http;
    
    
    
    
    var client = new HttpClient();
    
    var request = new HttpRequestMessage
    
    {
    
      Method = HttpMethod.Get,
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/audit-events"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
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
    
    )
    
    
    
    
    func main() {
    
    	url := "https://api.canva.com/admin/v1/audit-events"
    
    	req, _ := http.NewRequest("GET", url, nil)
    
    	req.Header.Add("Authorization", "Bearer {token}")
    
    
    
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }

GO

Copy
    
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/audit-events",
    
      CURLOPT_CUSTOMREQUEST => "GET",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
      ),
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/audit-events')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Get.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`items``object[]`

A JSON object representing an audit event. For the structure of each event, see [Audit events](https://www.canva.dev/docs/audit-logs/audit-events/).

`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list, for example `?continuation={continuation}`.

To retrieve all items, you might need to make multiple requests.

## Example response
    
    
    {
    
      "items": [
    
        {
    
          "id": "3849ef51-ca85-4028-bae3-1b8de3ee5738",
    
          "timestamp": 1704070800123,
    
          "actor": {
    
            "type": "USER",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            },
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          "target": {
    
            "target_type": "RESOURCE",
    
            "resource_type": "DESIGN",
    
            "id": "DXWEBartcNg",
    
            "owner": {
    
              "user": {
    
                "display_name": "Jane Doe",
    
                "email": "jane.doe@example.com"
    
              },
    
              "team": {
    
                "id": "BXeFatjDhdR",
    
                "display_name": "Acme Team"
    
              }
    
            }
    
          },
    
          "action": {
    
            "type": "VIEW_DESIGN",
    
            "view_type": "VIEW_IN_EDITOR",
    
            "design_type": "Presentation (16:9)"
    
          },
    
          "outcome": {
    
            "result": "PERMITTED"
    
          },
    
          "context": {
    
            "ip_address": "192.0.2.123",
    
            "session": "41cfef61",
    
            "request_id": "220d18b47fcb2d23c72a2a954dff09cb",
    
            "device_id": "d2805fafb9b50fe3f3d6ebbe221fc0e0883bf06b6bc285389147f3b259c2c4c1"
    
          }
    
        }
    
      ],
    
      "continuation": "RkFGMgXlsVTDbMd:MR3L0QjiaUzycIAjx0yMyuNiV0OildoiOwL0x32G4NjNu4FwtAQNxowUQNMMYN"
    
    }

JSON

Copy

## Error responses

### 400 Bad Request

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error responses

##### The continuation token is invalid
    
    
    {
    
      "code": "bad_query_params",
    
      "message": "The continuation token is malformed or was obtained from a different set of request parameters."
    
    }

JSON

Copy

##### The request uses invalid parameters
    
    
    {
    
      "code": "bad_query_params",
    
      "message": "The request uses invalid parameters."
    
    }

JSON

Copy

### 403 Forbidden

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### Client does not have permission to access audit events
    
    
    {
    
      "code": "permission_denied",
    
      "message": "Client does not have permission to access audit events."
    
    }

JSON

Copy
