---
url: https://www.canva.dev/docs/scim/create-group/
title: Create a group with SCIM - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:06.196033+00:00
---

# Create a group with SCIM - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/create-group/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# Create a group with SCIM

Copy page

Creates a user group in a Canva team.

The `displayName` of the group can't already be in use by an existing group within the same Canva Team.

You can't provide a list of group members when creating a group. To add users to a group, you can use either the [`PUT`](https://www.canva.dev/docs/scim/update-all-information-group/) or [`PATCH`](https://www.canva.dev/docs/scim/update-individual-attributes-group/) operations after the group is created.

## HTTP method and URL path

POST` https://www.canva.com/_scim/v2/Groups`

## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/scim+json`.

For example: `Content-Type: application/scim+json`

## Body parameters

`schemas``string[]`

Required

**Available values:** The only valid value is `urn:ietf:params:scim:schemas:core:2.0:Group`.

`displayName``string`

Required

The name of the group, suitable for display to end-users.

## Example request

Examples for using the `/_scim/v2/Groups` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://www.canva.com/_scim/v2/Groups' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/scim+json' \
    
    --data '{
    
      "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    
      "displayName": "White rabbits"
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://www.canva.com/_scim/v2/Groups", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/scim+json",
    
      },
    
      body: JSON.stringify({
    
        "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    
        "displayName": "White rabbits"
    
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
    
                .uri(URI.create("https://www.canva.com/_scim/v2/Groups"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/scim+json")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"schemas\": \"urn:ietf:params:scim:schemas:core:2.0:Group\", \"displayName\": \"White rabbits\"}"))
    
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
    
        "displayName": "White rabbits"
    
    }
    
    
    
    
    response = requests.post("https://www.canva.com/_scim/v2/Groups",
    
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
    
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Groups"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"schemas\": \"urn:ietf:params:scim:schemas:core:2.0:Group\", \"displayName\": \"White rabbits\"}",
    
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
    
    	  "displayName": "White rabbits"
    
    	}`)
    
    
    
    
    	url := "https://www.canva.com/_scim/v2/Groups"
    
    	req, _ := http.NewRequest("POST", url, payload)
    
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
    
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Groups",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/scim+json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "schemas" => "urn:ietf:params:scim:schemas:core:2.0:Group",
    
        "displayName" => "White rabbits"
    
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
    
    
    
    
    url = URI('https://www.canva.com/_scim/v2/Groups')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/scim+json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "schemas": "urn:ietf:params:scim:schemas:core:2.0:Group",
    
      "displayName": "White rabbits"
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `201` response with a JSON body with the following parameters:

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
