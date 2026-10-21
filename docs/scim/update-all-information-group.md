---
url: https://www.canva.dev/docs/scim/update-all-information-group/
title: Update all information for a group - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:07.093580+00:00
---

# Update all information for a group - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/update-all-information-group/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# Update all information for a group

Copy page

Replaces an existing group's information.

You must provide all the information for the group, as if you're creating the group for the first time. Any existing information for the group that isn't provided, including group members, is removed.

The `members` attribute of a group is an array of users, with each user represented as a `value` attribute that corresponds to the user's Canva SCIM ID.

If you only want to update a some of the group's attributes, you can use the [`PATCH` operation](https://www.canva.dev/docs/scim/update-individual-attributes-group/).

A maximum of 1000 group members are allowed in a `PUT` request.

The `members` array returned in a group's API response is always empty, even if there are members in the group. To see members of a group, you must [use the Canva web interface⁠(opens in a new tab or window)](https://www.canva.com/help/groups/).

## HTTP method and URL path

PUT` https://www.canva.com/_scim/v2/Groups/{canva_scim_id}`

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

**Available values:** The only valid value is `urn:ietf:params:scim:schemas:core:2.0:Group`.

`displayName``string`

Required

The name of the group, suitable for display to end-users.

`members``object[]`

Required

The members of the group.

Properties of **members**

`value``string`

Required

The Canva-generated SCIM ID for the user.

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
    
    
    curl --request PUT 'https://www.canva.com/_scim/v2/Groups/{canva_scim_id}' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/scim+json' \
    
    --data '{
    
      "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    
      "displayName": "White rabbits",
    
      "members": [
    
        {
    
          "value": "UAFdxab1abC"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://www.canva.com/_scim/v2/Groups/{canva_scim_id}", {
    
      method: "PUT",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/scim+json",
    
      },
    
      body: JSON.stringify({
    
        "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    
        "displayName": "White rabbits",
    
        "members": [
    
          {
    
            "value": "UAFdxab1abC"
    
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
    
                .method("PUT", HttpRequest.BodyPublishers.ofString("{\"schemas\": \"urn:ietf:params:scim:schemas:core:2.0:Group\", \"displayName\": \"White rabbits\", \"members\": [{\"value\": \"UAFdxab1abC\"}]}"))
    
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
    
        "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    
        "displayName": "White rabbits",
    
        "members": [
    
            {
    
                "value": "UAFdxab1abC"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.put("https://www.canva.com/_scim/v2/Groups/{canva_scim_id}",
    
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
    
      Method = HttpMethod.Put,
    
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Groups/{canva_scim_id}"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"schemas\": \"urn:ietf:params:scim:schemas:core:2.0:Group\", \"displayName\": \"White rabbits\", \"members\": [{\"value\": \"UAFdxab1abC\"}]}",
    
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
    
    	  "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    
    	  "displayName": "White rabbits",
    
    	  "members": [
    
    	    {
    
    	      "value": "UAFdxab1abC"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://www.canva.com/_scim/v2/Groups/{canva_scim_id}"
    
    	req, _ := http.NewRequest("PUT", url, payload)
    
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
    
      CURLOPT_CUSTOMREQUEST => "PUT",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/scim+json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "schemas" => "urn:ietf:params:scim:schemas:core:2.0:Group",
    
        "displayName" => "White rabbits",
    
        "members" => [
    
          [
    
            "value" => "UAFdxab1abC"
    
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
    
    
    
    
    request = Net::HTTP::Put.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/scim+json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    
      "displayName": "White rabbits",
    
      "members": [
    
        {
    
          "value": "UAFdxab1abC"
    
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
