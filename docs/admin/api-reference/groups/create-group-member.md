---
url: https://www.canva.dev/docs/admin/api-reference/groups/create-group-member/
title: Create group member - Groups - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:30.435749+00:00
---

# Create group member - Groups - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/groups/create-group-member/

Groups

[Create group](https://www.canva.dev/docs/admin/api-reference/groups/create-group/)[Get group](https://www.canva.dev/docs/admin/api-reference/groups/get-group/)[List groups](https://www.canva.dev/docs/admin/api-reference/groups/list-groups/)[Update group](https://www.canva.dev/docs/admin/api-reference/groups/update-group/)[Delete group](https://www.canva.dev/docs/admin/api-reference/groups/delete-group/)[Create group member](https://www.canva.dev/docs/admin/api-reference/groups/create-group-member/)[Get group member](https://www.canva.dev/docs/admin/api-reference/groups/get-group-member/)[List group members](https://www.canva.dev/docs/admin/api-reference/groups/list-group-members/)[Update group member](https://www.canva.dev/docs/admin/api-reference/groups/update-group-member/)[Delete group member](https://www.canva.dev/docs/admin/api-reference/groups/delete-group-member/)

# Create group member

Copy page

Adds a member to a group.

## HTTP method and URL path

POST` https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members`

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

## Body parameters

`user_id``string`

Required

The user ID.

`role``string`

Required

The role of the user in the group.

**Available values:**

  * `admin`
  * `member`



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
    
    
    curl --request POST 'https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "user_id": "UAAAAAAAAA1",
    
      "role": "admin"
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
      },
    
      body: JSON.stringify({
    
        "user_id": "UAAAAAAAAA1",
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"user_id\": \"UAAAAAAAAA1\", \"role\": \"admin\"}"))
    
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
    
        "user_id": "UAAAAAAAAA1",
    
        "role": "admin"
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"user_id\": \"UAAAAAAAAA1\", \"role\": \"admin\"}",
    
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
    
    	  "user_id": "UAAAAAAAAA1",
    
    	  "role": "admin"
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members"
    
    	req, _ := http.NewRequest("POST", url, payload)
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "user_id" => "UAAAAAAAAA1",
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}/members')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "user_id": "UAAAAAAAAA1",
    
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

### 403 Forbidden

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### The user has reached the maximum number of groups
    
    
    {
    
      "code": "max_limit_reached",
    
      "message": "User {userId} has reached the maximum number (70) of groups"
    
    }

JSON

Copy

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

##### The user is not a member of the team
    
    
    {
    
      "code": "user_not_found",
    
      "message": "User {userId} is not a member of team {teamId}"
    
    }

JSON

Copy
