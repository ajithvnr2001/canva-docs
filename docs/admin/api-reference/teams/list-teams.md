---
url: https://www.canva.dev/docs/admin/api-reference/teams/list-teams/
title: List teams - Teams - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:36.473218+00:00
---

# List teams - Teams - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/teams/list-teams/

Teams

[Create team](https://www.canva.dev/docs/admin/api-reference/teams/create-team/)[Get team](https://www.canva.dev/docs/admin/api-reference/teams/get-team/)[List teams](https://www.canva.dev/docs/admin/api-reference/teams/list-teams/)[Update team](https://www.canva.dev/docs/admin/api-reference/teams/update-team/)[Delete team](https://www.canva.dev/docs/admin/api-reference/teams/delete-team/)[Create team member](https://www.canva.dev/docs/admin/api-reference/teams/create-team-member/)[Get team member](https://www.canva.dev/docs/admin/api-reference/teams/get-team-member/)[List team members](https://www.canva.dev/docs/admin/api-reference/teams/list-team-members/)[Update team member](https://www.canva.dev/docs/admin/api-reference/teams/update-team-member/)[Delete team member](https://www.canva.dev/docs/admin/api-reference/teams/delete-team-member/)[Create team invitation](https://www.canva.dev/docs/admin/api-reference/teams/create-team-invitation/)[Find team invitation](https://www.canva.dev/docs/admin/api-reference/teams/find-team-invitation/)[List team invitations](https://www.canva.dev/docs/admin/api-reference/teams/list-team-invitations/)[Cancel team invitation](https://www.canva.dev/docs/admin/api-reference/teams/cancel-team-invitation/)

# List teams

Copy page

Lists teams.

## HTTP method and URL path

GET` https://api.canva.com/admin/v1/teams`

## Authentication and authorization

This endpoint requires a valid access token that was generated using client credentials.

### Scopes

The access token must have all the following [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) (permissions):

  * `admin:team:read`



## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

## Query parameters

`saml_team_id``string`

Optional

An identifier you assign to a team. When a user signs in through SSO, Canva reads the SAML `TeamId` attribute and adds them to the team with the matching `saml_team_id`. Must be unique within your organization.

**Minimum length:** `1`

**Maximum length:** `255`

`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list, for example `?continuation={continuation}`.

To retrieve all items, you might need to make multiple requests.

`limit``integer`

Optional

The maximum number of teams to return.

**Minimum:** `1`

**Maximum:** `100`

**Default value:** `50`

## Example request

Examples for using the `/v1/teams` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request GET 'https://api.canva.com/admin/v1/teams' \
    
    --header 'Authorization: Bearer {token}'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams", {
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams"))
    
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
    
    
    
    
    response = requests.get("https://api.canva.com/admin/v1/teams",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams"),
    
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
    
    	url := "https://api.canva.com/admin/v1/teams"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams",
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams')
    
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

`items``Team[]`

A team.

Properties of **items**

`id``string`

The team ID.

`name``string`

The name of the team.

`created_at``integer`

When the team was created, as a Unix timestamp (in seconds since the Unix Epoch).

`updated_at``integer`

Optional

When the team was last updated, as a Unix timestamp (in seconds since the Unix Epoch).

`saml_team_id``string`

Optional

An identifier you assign to a team. When a user signs in through SSO, Canva reads the SAML `TeamId` attribute and adds them to the team with the matching `saml_team_id`. Must be unique within your organization.

**Minimum length:** `1`

**Maximum length:** `255`

`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list, for example `?continuation={continuation}`.

To retrieve all items, you might need to make multiple requests.

## Example response
    
    
    {
    
      "continuation": "RkFGMgXlsVTDbMd:MR3L0QjiaUzycIAjx0yMyuNiV0OildoiOwL0x32G4NjNu4FwtAQNxowUQNMMYN",
    
      "items": [
    
        {
    
          "id": "BAAAAAAAAA1",
    
          "name": "Acme Team",
    
          "created_at": 1601404800,
    
          "updated_at": 1601404900
    
        }
    
      ]
    
    }

JSON

Copy

## Error responses

### 400 Bad Request

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### Continuation is not supported for listing teams by SAML team ID
    
    
    {
    
      "code": "bad_query_params",
    
      "message": "Continuation is not supported for listing teams by SAML team ID."
    
    }

JSON

Copy
