---
url: https://www.canva.dev/docs/admin/api-reference/groups/update-group-member/
title: Update group member - Groups - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:33.282534+00:00
---

# Update group member - Groups - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/groups/update-group-member/

Groups

[Create group](https://www.canva.dev/docs/admin/api-reference/groups/create-group/)[Get group](https://www.canva.dev/docs/admin/api-reference/groups/get-group/)[List groups](https://www.canva.dev/docs/admin/api-reference/groups/list-groups/)[Update group](https://www.canva.dev/docs/admin/api-reference/groups/update-group/)[Delete group](https://www.canva.dev/docs/admin/api-reference/groups/delete-group/)[Create group member](https://www.canva.dev/docs/admin/api-reference/groups/create-group-member/)[Get group member](https://www.canva.dev/docs/admin/api-reference/groups/get-group-member/)[List group members](https://www.canva.dev/docs/admin/api-reference/groups/list-group-members/)[Update group member](https://www.canva.dev/docs/admin/api-reference/groups/update-group-member/)[Delete group member](https://www.canva.dev/docs/admin/api-reference/groups/delete-group-member/)

# Update group member

Copy page

Updates a member of a group. Currently, you can only update the member's role in the group.

## HTTP method and URL path

PATCH` https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}`

## Authentication and authorization

This endpoint requires a valid access token that was generated using client credentials.

### Scopes

The access token must have all the following [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) (permissions):

  * `admin:group:write`



## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/json`.

For example: `Content-Type: application/json`

## Path parameters

`teamId``string`

Required

The team ID.

`groupId``string`

Required

The group ID.

`userId``string`

Required

The user ID.

## Body parameters

`role``string`

Required

The role of the user in the group.

**Available values:**

  * `admin`
  * `member`



## Example request

Examples for using the `/v1/teams/{teamId}/groups/{groupId}/members/{userId}` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request PATCH 'https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "role": "admin"
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}", {
    
      method: "PATCH",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
      },
    
      body: JSON.stringify({
    
        "role": "admin"
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .method("PATCH", HttpRequest.BodyPublishers.ofString("{\"role\": \"admin\"}"))
    
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
    
        "Content-Type": "application/json"
    
    }
    
    
    
    
    data = {
    
        "role": "admin"
    
    }
    
    
    
    
    response = requests.patch("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"role\": \"admin\"}",
    
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
    
    	  "role": "admin"
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}"
    
    	req, _ := http.NewRequest("PATCH", url, payload)
    
    	req.Header.Add("Authorization", "Bearer {token}")
    
    	req.Header.Add("Content-Type", "application/json")
    
    
    
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }

GO

Copy
    
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}",
    
      CURLOPT_CUSTOMREQUEST => "PATCH",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "role" => "admin"
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members/{userId}')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Patch.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "role": "admin"
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`group_member``GroupMember`

A member in a group.

Properties of **group_member**

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



## Example response
    
    
    {
    
      "group_member": {
    
        "user_id": "UAAAAAAAAA1",
    
        "group_id": "GAAAAAAAAAA",
    
        "team_id": "BAAAAAAAAAA",
    
        "role": "member"
    
      }
    
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

##### The user is not a member of the group
    
    
    {
    
      "code": "user_not_found",
    
      "message": "User {userId} is not a member of group {groupId}"
    
    }

JSON

Copy
