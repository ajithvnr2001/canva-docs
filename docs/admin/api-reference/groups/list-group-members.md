---
url: https://www.canva.dev/docs/admin/api-reference/groups/list-group-members/
title: List group members - Groups - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:32.731022+00:00
---

# List group members - Groups - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/groups/list-group-members/

Groups

[Create group](https://www.canva.dev/docs/admin/api-reference/groups/create-group/)[Get group](https://www.canva.dev/docs/admin/api-reference/groups/get-group/)[List groups](https://www.canva.dev/docs/admin/api-reference/groups/list-groups/)[Update group](https://www.canva.dev/docs/admin/api-reference/groups/update-group/)[Delete group](https://www.canva.dev/docs/admin/api-reference/groups/delete-group/)[Create group member](https://www.canva.dev/docs/admin/api-reference/groups/create-group-member/)[Get group member](https://www.canva.dev/docs/admin/api-reference/groups/get-group-member/)[List group members](https://www.canva.dev/docs/admin/api-reference/groups/list-group-members/)[Update group member](https://www.canva.dev/docs/admin/api-reference/groups/update-group-member/)[Delete group member](https://www.canva.dev/docs/admin/api-reference/groups/delete-group-member/)

# List group members

Copy page

Lists members in a group.

## HTTP method and URL path

GET` https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members`

## Authentication and authorization

This endpoint requires a valid access token that was generated using client credentials.

### Scopes

The access token must have all the following [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) (permissions):

  * `admin:group:read`



## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

## Path parameters

`teamId``string`

Required

The team ID.

`groupId``string`

Required

The group ID.

## Query parameters

`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list, for example `?continuation={continuation}`.

To retrieve all items, you might need to make multiple requests.

`limit``integer`

Optional

The maximum number of members to return.

**Minimum:** `1`

**Maximum:** `100`

**Default value:** `50`

## Example request

Examples for using the `/v1/teams/{teamId}/groups/{groupId}/members` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request GET 'https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members' \
    
    --header 'Authorization: Bearer {token}'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members", {
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members"))
    
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
    
    
    
    
    response = requests.get("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members"),
    
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
    
    	url := "https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members",
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members')
    
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

`items``GroupMember[]`

A member in a group.

Properties of **items**

`user_id``string`

The user ID.

`group_id``string`

The group ID.

`team_id``string`

The team ID.

`role``string`

The role of the user in the group.

**Available values:**

  * `admin`
  * `member`



`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list, for example `?continuation={continuation}`.

To retrieve all items, you might need to make multiple requests.

## Example response
    
    
    {
    
      "items": [
    
        {
    
          "user_id": "UAAAAAAAAA1",
    
          "group_id": "GAAAAAAAAAA",
    
          "team_id": "BAAAAAAAAAA",
    
          "role": "member"
    
        }
    
      ],
    
      "continuation": "RkFGMgXlsVTDbMd:MR3L0QjiaUzycIAjx0yMyuNiV0OildoiOwL0x32G4NjNu4FwtAQNxowUQNMMYN"
    
    }

JSON

Copy

## Error responses

### 404 Not Found

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error responses

##### The team was not found
    
    
    {
    
      "code": "team_not_found",
    
      "message": "Team {teamId} not found"
    
    }

JSON

Copy

##### The group was not found
    
    
    {
    
      "code": "group_not_found",
    
      "message": "Group {groupId} not found"
    
    }

JSON

Copy
