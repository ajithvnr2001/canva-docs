---
url: https://www.canva.dev/docs/admin/api-reference/teams/list-team-invitations/
title: List team invitations - Teams - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:35.793492+00:00
---

# List team invitations - Teams - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/teams/list-team-invitations/

Teams

[Create team](https://www.canva.dev/docs/admin/api-reference/teams/create-team/)[Get team](https://www.canva.dev/docs/admin/api-reference/teams/get-team/)[List teams](https://www.canva.dev/docs/admin/api-reference/teams/list-teams/)[Update team](https://www.canva.dev/docs/admin/api-reference/teams/update-team/)[Delete team](https://www.canva.dev/docs/admin/api-reference/teams/delete-team/)[Create team member](https://www.canva.dev/docs/admin/api-reference/teams/create-team-member/)[Get team member](https://www.canva.dev/docs/admin/api-reference/teams/get-team-member/)[List team members](https://www.canva.dev/docs/admin/api-reference/teams/list-team-members/)[Update team member](https://www.canva.dev/docs/admin/api-reference/teams/update-team-member/)[Delete team member](https://www.canva.dev/docs/admin/api-reference/teams/delete-team-member/)[Create team invitation](https://www.canva.dev/docs/admin/api-reference/teams/create-team-invitation/)[Find team invitation](https://www.canva.dev/docs/admin/api-reference/teams/find-team-invitation/)[List team invitations](https://www.canva.dev/docs/admin/api-reference/teams/list-team-invitations/)[Cancel team invitation](https://www.canva.dev/docs/admin/api-reference/teams/cancel-team-invitation/)

# List team invitations

Copy page

Lists pending single-use email invitations for a team in the caller's organization.

The response contains pending invitations only. Accepted, cancelled, and expired invitations are omitted. Items include team, email, role, and expiry. They never include the invitation URL.

Paginate with `limit` and `continuation`. `continuation` is an opaque token. Presence of `continuation` means more records exist. The last page omits `continuation`.

## HTTP method and URL path

GET` https://api.canva.com/admin/v1/teams/{teamId}/invitations`

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

## Path parameters

`teamId``string`

Required

The team ID.

## Query parameters

`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list, for example `?continuation={continuation}`.

To retrieve all items, you might need to make multiple requests.

`limit``integer`

Optional

The maximum number of invitations to return.

**Minimum:** `1`

**Maximum:** `100`

**Default value:** `50`

## Example request

Examples for using the `/v1/teams/{teamId}/invitations` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request GET 'https://api.canva.com/admin/v1/teams/{teamId}/invitations' \
    
    --header 'Authorization: Bearer {token}'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams/{teamId}/invitations", {
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams/{teamId}/invitations"))
    
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
    
    
    
    
    response = requests.get("https://api.canva.com/admin/v1/teams/{teamId}/invitations",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams/{teamId}/invitations"),
    
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
    
    	url := "https://api.canva.com/admin/v1/teams/{teamId}/invitations"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams/{teamId}/invitations",
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams/{teamId}/invitations')
    
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

`items``TeamInvitation[]`

A pending invitation for an email address to join a team. The invitation record exists only while the invitation can still be accepted.

Properties of **items**

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

`continuation``string`

Optional

If the success response contains a continuation token, the list contains more items you can list. You can use this token as a query parameter and retrieve more items from the list, for example `?continuation={continuation}`.

To retrieve all items, you might need to make multiple requests.

## Example response
    
    
    {
    
      "items": [
    
        {
    
          "team_id": "BAAAAAAAAA1",
    
          "email": "drsmith@brightsmiledental.com",
    
          "role": "member",
    
          "expires_at": 1788499200,
    
          "url": "https://www.canva.com/brand/join?token=EXAMPLEQi1pbnZpdGU&referrer=team-invite"
    
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

#### Example error response

##### The team was not found
    
    
    {
    
      "code": "team_not_found",
    
      "message": "Team {teamId} not found"
    
    }

JSON

Copy

### 429 Too many requests

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response
    
    
    {
    
      "code": "string",
    
      "message": "string"
    
    }

JSON

Copy
