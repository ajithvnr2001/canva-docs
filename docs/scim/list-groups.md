---
url: https://www.canva.dev/docs/scim/list-groups/
title: List groups - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:08.290307+00:00
---

# List groups - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/list-groups/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# List groups

Copy page

Gets a paginated list of all user groups in a Canva team.

You can use the `startIndex` and `count` parameters to control the pagination of the response.

You can also provide a `filter` parameter to narrow down the groups returned to only include those matching the filter.

The `members` array returned in a group's API response is always empty, even if there are members in the group. To see members of a group, you must [use the Canva web interface⁠(opens in a new tab or window)](https://www.canva.com/help/groups/).

## HTTP method and URL path

GET` https://www.canva.com/_scim/v2/Groups`

## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

## Query parameters

`startIndex``integer`

Optional

Used to paginate the response: the index of the first result to return.

`count``integer`

Optional

Used to paginate the response: the number of results to return. Must be between `1` and `10`.

`filter``string`

Optional

A filter to narrow down the results returned, using the equals (`eq`) query parameter. The following filters are supported:

  * Return the group matching the SCIM `displayName` value: `displayName eq "{display_name}"`.

For example: `GET /_scim/v2/Groups?filter=displayName%20eq%20"White rabbits"`




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
    
    
    curl --request GET 'https://www.canva.com/_scim/v2/Groups' \
    
    --header 'Authorization: Bearer {token}'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://www.canva.com/_scim/v2/Groups", {
    
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
    
                .uri(URI.create("https://www.canva.com/_scim/v2/Groups"))
    
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
    
    
    
    
    response = requests.get("https://www.canva.com/_scim/v2/Groups",
    
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
    
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Groups"),
    
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
    
    	url := "https://www.canva.com/_scim/v2/Groups"
    
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
    
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Groups",
    
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
    
    
    
    
    url = URI('https://www.canva.com/_scim/v2/Groups')
    
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

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:ListResponse`.

`totalResults``integer`

The total number of results matching the query.

`startIndex``integer`

The index of the first result.

`itemsPerPage``integer`

The number of results returned in the current page.

`resources``ScimGroupResponse[]`

An array of the groups returned in the current page of results.

Properties of **resources**

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
    
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    
      ],
    
      "totalResults": 1,
    
      "startIndex": 1,
    
      "itemsPerPage": 10,
    
      "resources": [
    
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
    
      ]
    
    }

JSON

Copy

## Error responses

### 403 Forbidden

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.

`detail``string`

**Available values:** The only valid value is `Unsupported filter field`.

`status``string`

The HTTP status code of the error.

#### Example error response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:Error"
    
      ],
    
      "detail": "Unsupported filter field",
    
      "status": "403"
    
    }

JSON

Copy
