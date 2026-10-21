---
url: https://www.canva.dev/docs/admin/api-reference/teams/find-team-invitation/
title: Find team invitation - Teams - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:36.297026+00:00
---

# Find team invitation - Teams - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/teams/find-team-invitation/

Teams

[Create team](https://www.canva.dev/docs/admin/api-reference/teams/create-team/)[Get team](https://www.canva.dev/docs/admin/api-reference/teams/get-team/)[List teams](https://www.canva.dev/docs/admin/api-reference/teams/list-teams/)[Update team](https://www.canva.dev/docs/admin/api-reference/teams/update-team/)[Delete team](https://www.canva.dev/docs/admin/api-reference/teams/delete-team/)[Create team member](https://www.canva.dev/docs/admin/api-reference/teams/create-team-member/)[Get team member](https://www.canva.dev/docs/admin/api-reference/teams/get-team-member/)[List team members](https://www.canva.dev/docs/admin/api-reference/teams/list-team-members/)[Update team member](https://www.canva.dev/docs/admin/api-reference/teams/update-team-member/)[Delete team member](https://www.canva.dev/docs/admin/api-reference/teams/delete-team-member/)[Create team invitation](https://www.canva.dev/docs/admin/api-reference/teams/create-team-invitation/)[Find team invitation](https://www.canva.dev/docs/admin/api-reference/teams/find-team-invitation/)[List team invitations](https://www.canva.dev/docs/admin/api-reference/teams/list-team-invitations/)[Cancel team invitation](https://www.canva.dev/docs/admin/api-reference/teams/cancel-team-invitation/)

# Find team invitation

Copy page

Finds a pending single-use email invitation for a team in the caller's organization.

The email address is restricted data and is accepted only in the JSON request body. The response contains zero or one invitation. A matching invitation includes the invitation URL so the caller can deliver it without refreshing the invitation.

Treat the returned `url` as a secret. Don't log the URL or send it over insecure channels.

## HTTP method and URL path

POST` https://api.canva.com/admin/v1/teams/{teamId}/invitations/find`

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

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/json`.

For example: `Content-Type: application/json`

## Path parameters

`teamId``string`

Required

The team ID.

## Body parameters

`email``string`

Required

The email address associated with the invitation.

**Minimum length:** `1`

**Maximum length:** `254`

## Example request

Examples for using the `/v1/teams/{teamId}/invitations/find` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/admin/v1/teams/{teamId}/invitations/find' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "email": "drsmith@brightsmiledental.com"
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams/{teamId}/invitations/find", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
      },
    
      body: JSON.stringify({
    
        "email": "drsmith@brightsmiledental.com"
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams/{teamId}/invitations/find"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"email\": \"drsmith@brightsmiledental.com\"}"))
    
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
    
        "email": "drsmith@brightsmiledental.com"
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/admin/v1/teams/{teamId}/invitations/find",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams/{teamId}/invitations/find"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"email\": \"drsmith@brightsmiledental.com\"}",
    
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
    
    	  "email": "drsmith@brightsmiledental.com"
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/admin/v1/teams/{teamId}/invitations/find"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams/{teamId}/invitations/find",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "email" => "drsmith@brightsmiledental.com"
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams/{teamId}/invitations/find')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "email": "drsmith@brightsmiledental.com"
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`invitation``TeamInvitation`

Optional

A pending invitation for an email address to join a team. The invitation record exists only while the invitation can still be accepted.

Properties of **invitation**

`team_id``string`

The ID of the team the invitation grants access to.

`email``string`

The invited email address. Only an account with this email can accept.

`role``string`

The role of the member in the team.

**Available values:**

  * `admin`
  * `designer`
  * `member`



`expires_at``integer`

When the invitation expires, as a Unix timestamp (in seconds). This is always 30 days after the create or refresh request that issued it. Expired invitations can't be accepted.

`url``string`

Optional

The invitation URL. Redirect the invitee to this URL to accept the invitation. Treat it as a secret: don't log it or send it over insecure channels. Create and a matched find result always return this field. Unfiltered list responses omit it.

## Example responses

### A pending invitation matches the email
    
    
    {
    
      "invitation": {
    
        "team_id": "BAAAAAAAAA1",
    
        "email": "drsmith@brightsmiledental.com",
    
        "role": "member",
    
        "expires_at": 1788499200,
    
        "url": "https://www.canva.com/brand/join?token=EXAMPLEQi1pbnZpdGU&referrer=team-invite"
    
      }
    
    }

JSON

Copy

### No pending invitation matches the email
    
    
    {}

JSON

Copy

## Error responses

### 400 Bad Request

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### The email address is not valid
    
    
    {
    
      "code": "invalid_field",
    
      "message": "'email' must be a valid email address."
    
    }

JSON

Copy

### 404 Not Found

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### The team was not found
    
    
    {
    
      "code": "team_not_found",
    
      "message": "Team {teamId} not found"
    
    }

JSON

Copy
