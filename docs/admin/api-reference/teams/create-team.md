---
url: https://www.canva.dev/docs/admin/api-reference/teams/create-team/
title: Create team - Teams - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:35.351459+00:00
---

# Create team - Teams - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/teams/create-team/

Teams

[Create team](https://www.canva.dev/docs/admin/api-reference/teams/create-team/)[Get team](https://www.canva.dev/docs/admin/api-reference/teams/get-team/)[List teams](https://www.canva.dev/docs/admin/api-reference/teams/list-teams/)[Update team](https://www.canva.dev/docs/admin/api-reference/teams/update-team/)[Delete team](https://www.canva.dev/docs/admin/api-reference/teams/delete-team/)[Create team member](https://www.canva.dev/docs/admin/api-reference/teams/create-team-member/)[Get team member](https://www.canva.dev/docs/admin/api-reference/teams/get-team-member/)[List team members](https://www.canva.dev/docs/admin/api-reference/teams/list-team-members/)[Update team member](https://www.canva.dev/docs/admin/api-reference/teams/update-team-member/)[Delete team member](https://www.canva.dev/docs/admin/api-reference/teams/delete-team-member/)[Create team invitation](https://www.canva.dev/docs/admin/api-reference/teams/create-team-invitation/)[Find team invitation](https://www.canva.dev/docs/admin/api-reference/teams/find-team-invitation/)[List team invitations](https://www.canva.dev/docs/admin/api-reference/teams/list-team-invitations/)[Cancel team invitation](https://www.canva.dev/docs/admin/api-reference/teams/cancel-team-invitation/)

# Create team

Copy page

Creates a new team in the organization.

Team names are not unique within an organization. Multiple teams with the same name are allowed, so you should track teams by their team ID rather than by name.

## HTTP method and URL path

POST` https://api.canva.com/admin/v1/teams`

## Authentication and authorization

This endpoint requires a valid access token that was generated using client credentials.

### Scopes

The access token must have all the following [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) (permissions):

  * `admin:team:write`



## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/json`.

For example: `Content-Type: application/json`

## Body parameters

`name``string`

Required

The display name for the team.

**Minimum length:** `1`

**Maximum length:** `255`

`saml_team_id``string`

Optional

An identifier you assign to a team. When a user signs in through SSO, Canva reads the SAML `TeamId` attribute and adds them to the team with the matching `saml_team_id`. Must be unique within your organization.

**Minimum length:** `1`

**Maximum length:** `255`

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
    
    
    curl --request POST 'https://api.canva.com/admin/v1/teams' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "name": "ACME Marketing Team",
    
      "saml_team_id": "brokerage-123"
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
      },
    
      body: JSON.stringify({
    
        "name": "ACME Marketing Team",
    
        "saml_team_id": "brokerage-123"
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"name\": \"ACME Marketing Team\", \"saml_team_id\": \"brokerage-123\"}"))
    
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
    
        "name": "ACME Marketing Team",
    
        "saml_team_id": "brokerage-123"
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/admin/v1/teams",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"name\": \"ACME Marketing Team\", \"saml_team_id\": \"brokerage-123\"}",
    
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
    
    	  "name": "ACME Marketing Team",
    
    	  "saml_team_id": "brokerage-123"
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/admin/v1/teams"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "name" => "ACME Marketing Team",
    
        "saml_team_id" => "brokerage-123"
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "name": "ACME Marketing Team",
    
      "saml_team_id": "brokerage-123"
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`team``Team`

A team.

Properties of **team**

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

## Example response

### A team was successfully created
    
    
    {
    
      "team": {
    
        "id": "BAAAAAAAAA1",
    
        "name": "Acme Team",
    
        "created_at": 1601404800,
    
        "updated_at": 1601404800
    
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

#### Example error response

##### The team name contains unsafe input
    
    
    {
    
      "code": "input_unsafe",
    
      "message": "Team name contains unsafe input."
    
    }

JSON

Copy

### 409 Conflict

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### A team with the same SAML team ID already exists
    
    
    {
    
      "code": "saml_team_id_conflict",
    
      "message": "A team with this SAML team ID already exists in the organization."
    
    }

JSON

Copy
