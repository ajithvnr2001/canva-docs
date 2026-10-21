---
url: https://www.canva.dev/docs/scim/update-individual-attributes-group/
title: Update individual attributes for a group - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:08.556273+00:00
---

# Update individual attributes for a group - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/update-individual-attributes-group/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# Update individual attributes for a group

Copy page

Updates individual attributes for a group. To update a group's attributes, you must use the correct [syntax for the operation, as defined in the SCIM specification⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.2).

The `value` attribute of an operation on the `members` path is an array of users, with each user represented as a `value` attribute that corresponds to the user's Canva SCIM ID.

For example, to remove a particular user from the group and add two others, you could use a request body similar to the following:
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
      ],
    
      "Operations": [
    
        {
    
          "op": "remove",
    
          "path": "members[value eq \"UAFdxab1abC\"]"
    
        },
    
        {
    
          "op": "add",
    
          "path": "members",
    
          "value": [
    
            {
    
              "value": "UAFdxcd1cdE"
    
            },
    
            {
    
              "value": "UAFdxfg1fgH"
    
            }
    
          ]
    
        }
    
      ]
    
    }

JSON

Copy

Doing a `replace` operation on the `members` path replaces the entire member list in the group. Doing a `replace` operation on the `members` path should be done in a separate request from any other `add` or `remove` operations on group membership.

For `add` or `remove` operations, a maximum of 1000 group members are allowed in each `value` array.

The `members` array returned in a group's API response is always empty, even if there are members in the group. To see members of a group, you must [use the Canva web interface⁠(opens in a new tab or window)](https://www.canva.com/help/groups/).

## HTTP method and URL path

PATCH` https://www.canva.com/_scim/v2/Groups/{canva_scim_id}`

## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/scim+json`.

For example: `Content-Type: application/scim+json`

## Path parameters

`canva_scim_id``string`

Required

The Canva-generated SCIM ID for the group.

## Body parameters

Expand all

`schemas``string[]`

Required

The URIs of the SCIM schemas.

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:PatchOp`.

`Operations``object[]`

Required

List of patch operations

Properties of **Operations**

`op``string`

Required

The SCIM patch operation to perform.

**Available values:**

  * `add`
  * `remove`
  * `replace`



`path``string`

Optional

An attribute path describing the target of the operation. For more information, see the [SCIM specification⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.2).

`value``object`

Optional

The value to add, remove, or replace.

## Example request

Examples for using the `/_scim/v2/Groups/{canva_scim_id}` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request PATCH 'https://www.canva.com/_scim/v2/Groups/{canva_scim_id}' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/scim+json' \
    
    --data '{
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
      ],
    
      "Operations": [
    
        {
    
          "op": "add",
    
          "path": "members",
    
          "value": [
    
            {
    
              "value": "UAFdxcd1cdE"
    
            }
    
          ]
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://www.canva.com/_scim/v2/Groups/{canva_scim_id}", {
    
      method: "PATCH",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/scim+json",
    
      },
    
      body: JSON.stringify({
    
        "schemas": [
    
          "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
        ],
    
        "Operations": [
    
          {
    
            "op": "add",
    
            "path": "members",
    
            "value": [
    
              {
    
                "value": "UAFdxcd1cdE"
    
              }
    
            ]
    
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
    
                .uri(URI.create("https://www.canva.com/_scim/v2/Groups/{canva_scim_id}"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/scim+json")
    
                .method("PATCH", HttpRequest.BodyPublishers.ofString("{\"schemas\": [\"urn:ietf:params:scim:api:messages:2.0:PatchOp\"], \"Operations\": [{\"op\": \"add\", \"path\": \"members\", \"value\": [{\"value\": \"UAFdxcd1cdE\"}]}]}"))
    
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
    
        "Content-Type": "application/scim+json"
    
    }
    
    
    
    
    data = {
    
        "schemas": [
    
            "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
        ],
    
        "Operations": [
    
            {
    
                "op": "add",
    
                "path": "members",
    
                "value": [
    
                    {
    
                        "value": "UAFdxcd1cdE"
    
                    }
    
                ]
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.patch("https://www.canva.com/_scim/v2/Groups/{canva_scim_id}",
    
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
    
      Method = HttpMethod.Patch,
    
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Groups/{canva_scim_id}"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"schemas\": [\"urn:ietf:params:scim:api:messages:2.0:PatchOp\"], \"Operations\": [{\"op\": \"add\", \"path\": \"members\", \"value\": [{\"value\": \"UAFdxcd1cdE\"}]}]}",
    
        Encoding.UTF8,
    
        "application/scim+json"
    
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
    
    	  "schemas": [
    
    	    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
    	  ],
    
    	  "Operations": [
    
    	    {
    
    	      "op": "add",
    
    	      "path": "members",
    
    	      "value": [
    
    	        {
    
    	          "value": "UAFdxcd1cdE"
    
    	        }
    
    	      ]
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://www.canva.com/_scim/v2/Groups/{canva_scim_id}"
    
    	req, _ := http.NewRequest("PATCH", url, payload)
    
    	req.Header.Add("Authorization", "Bearer {token}")
    
    	req.Header.Add("Content-Type", "application/scim+json")
    
    
    
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }

GO

Copy
    
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
    
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Groups/{canva_scim_id}",
    
      CURLOPT_CUSTOMREQUEST => "PATCH",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/scim+json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "schemas" => [
    
          "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
        ],
    
        "Operations" => [
    
          [
    
            "op" => "add",
    
            "path" => "members",
    
            "value" => [
    
              [
    
                "value" => "UAFdxcd1cdE"
    
              ]
    
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
    
    
    
    
    url = URI('https://www.canva.com/_scim/v2/Groups/{canva_scim_id}')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Patch.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/scim+json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
      ],
    
      "Operations": [
    
        {
    
          "op": "add",
    
          "path": "members",
    
          "value": [
    
            {
    
              "value": "UAFdxcd1cdE"
    
            }
    
          ]
    
        }
    
      ]
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:schemas:core:2.0:Group`.

`id``string`

The Canva-generated SCIM ID for the group.

`meta``object`

Meta properties for the group.

Properties of **meta**

`resourceType``string`

The SCIM resource type of the object.

**Available values:** The only valid value is `Group`.

`created``string`

The timestamp when the object was created.

`displayName``string`

The name of the group, suitable for display to end-users.

`members``object[]`

The `members` array returned in a group's API response is always empty, even if there are members in the group. To see members of a group, you must [use the Canva web interface⁠(opens in a new tab or window)](https://www.canva.com/help/groups/).

## Example response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:schemas:core:2.0:Group"
    
      ],
    
      "id": "GAFgrpb1abC",
    
      "meta": {
    
        "resourceType": "Group",
    
        "created": "2023-09-18T06:08:35Z"
    
      },
    
      "displayName": "White rabbits",
    
      "members": []
    
    }

JSON

Copy

## Error responses

### 404 Not found

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.

`detail``string`

**Available values:** The only valid value is `group {canva_scim_id} not found`.

`status``string`

The HTTP status code of the error.

#### Example error response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:Error"
    
      ],
    
      "detail": "group {canva_scim_id} not found",
    
      "status": "404"
    
    }

JSON

Copy

### 409 Conflict

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.

`detail``string`

**Available values:** The only valid value is `Group with name {group_name} already exists.`.

`status``string`

The HTTP status code of the error.

#### Example error response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:Error"
    
      ],
    
      "detail": "Group with name White rabbits already exists.",
    
      "status": "409"
    
    }

JSON

Copy
