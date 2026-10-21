---
url: https://www.canva.dev/docs/admin/api-reference/groups/update-group/
title: Update group - Groups - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:33.463705+00:00
---

# Update group - Groups - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/groups/update-group/

Groups

[Create group](https://www.canva.dev/docs/admin/api-reference/groups/create-group/)[Get group](https://www.canva.dev/docs/admin/api-reference/groups/get-group/)[List groups](https://www.canva.dev/docs/admin/api-reference/groups/list-groups/)[Update group](https://www.canva.dev/docs/admin/api-reference/groups/update-group/)[Delete group](https://www.canva.dev/docs/admin/api-reference/groups/delete-group/)[Create group member](https://www.canva.dev/docs/admin/api-reference/groups/create-group-member/)[Get group member](https://www.canva.dev/docs/admin/api-reference/groups/get-group-member/)[List group members](https://www.canva.dev/docs/admin/api-reference/groups/list-group-members/)[Update group member](https://www.canva.dev/docs/admin/api-reference/groups/update-group-member/)[Delete group member](https://www.canva.dev/docs/admin/api-reference/groups/delete-group-member/)

# Update group

Copy page

Updates a group in a team.

## HTTP method and URL path

PATCH` https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}`

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

`name``string`

Optional

A display name for the group.

**Minimum length:** `1`

**Maximum length:** `255`

`description``string`

Optional

A description for the group.

**Maximum length:** `255`

## Example request

Examples for using the `/v1/teams/{teamId}/groups/{groupId}` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request PATCH 'https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "name": "ACME Marketing Group",
    
      "description": "All staff members in the marketing department."
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}", {
    
      method: "PATCH",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
      },
    
      body: JSON.stringify({
    
        "name": "ACME Marketing Group",
    
        "description": "All staff members in the marketing department."
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .method("PATCH", HttpRequest.BodyPublishers.ofString("{\"name\": \"ACME Marketing Group\", \"description\": \"All staff members in the marketing department.\"}"))
    
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
    
        "name": "ACME Marketing Group",
    
        "description": "All staff members in the marketing department."
    
    }
    
    
    
    
    response = requests.patch("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"name\": \"ACME Marketing Group\", \"description\": \"All staff members in the marketing department.\"}",
    
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
    
    	  "name": "ACME Marketing Group",
    
    	  "description": "All staff members in the marketing department."
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}",
    
      CURLOPT_CUSTOMREQUEST => "PATCH",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "name" => "ACME Marketing Group",
    
        "description" => "All staff members in the marketing department."
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams/{teamId}/groups/{groupId}')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Patch.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "name": "ACME Marketing Group",
    
      "description": "All staff members in the marketing department."
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`group``Group`

A group.

Properties of **group**

`id``string`

The group ID. This ID is generated by Canva and is unique within the team.

`name``string`

The name of the group.

`created_at``integer`

When the group was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

When the group was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`description``string`

Optional

The description of the group.

## Example response
    
    
    {
    
      "group": {
    
        "id": "GAAAAAAAAA1",
    
        "name": "ACME Marketing Group",
    
        "description": "All staff members in the marketing department.",
    
        "created_at": 1601404800,
    
        "updated_at": 1601404900
    
      }
    
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

##### A group with the same name already exists
    
    
    {
    
      "code": "display_name_unavailable",
    
      "message": "A group with the same name already exists in the team."
    
    }

JSON

Copy

##### The input is unsafe
    
    
    {
    
      "code": "input_unsafe",
    
      "message": "Input is unsafe"
    
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
