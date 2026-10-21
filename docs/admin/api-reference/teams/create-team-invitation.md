---
url: https://www.canva.dev/docs/admin/api-reference/teams/create-team-invitation/
title: Create team invitation - Teams - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:34.711405+00:00
---

# Create team invitation - Teams - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/teams/create-team-invitation/

Teams

[Create team](https://www.canva.dev/docs/admin/api-reference/teams/create-team/)[Get team](https://www.canva.dev/docs/admin/api-reference/teams/get-team/)[List teams](https://www.canva.dev/docs/admin/api-reference/teams/list-teams/)[Update team](https://www.canva.dev/docs/admin/api-reference/teams/update-team/)[Delete team](https://www.canva.dev/docs/admin/api-reference/teams/delete-team/)[Create team member](https://www.canva.dev/docs/admin/api-reference/teams/create-team-member/)[Get team member](https://www.canva.dev/docs/admin/api-reference/teams/get-team-member/)[List team members](https://www.canva.dev/docs/admin/api-reference/teams/list-team-members/)[Update team member](https://www.canva.dev/docs/admin/api-reference/teams/update-team-member/)[Delete team member](https://www.canva.dev/docs/admin/api-reference/teams/delete-team-member/)[Create team invitation](https://www.canva.dev/docs/admin/api-reference/teams/create-team-invitation/)[Find team invitation](https://www.canva.dev/docs/admin/api-reference/teams/find-team-invitation/)[List team invitations](https://www.canva.dev/docs/admin/api-reference/teams/list-team-invitations/)[Cancel team invitation](https://www.canva.dev/docs/admin/api-reference/teams/cancel-team-invitation/)

# Create team invitation

Copy page

Creates a unique, email-bound, single-use invitation to join a team in the caller's organization, and returns the invitation URL for the caller to deliver to the invitee. Canva doesn't send an email unless the caller explicitly requests it.

Unlike `createTeamMember`, the invitee doesn't need to be managed by the organization: any email address can be invited, including addresses on domains the organization hasn't verified. The invitee consents by accepting the invitation, logging in to their existing Canva account or signing up with the invited email, and then joins the team.

Treat the returned `url` as a secret. Anyone with the URL can start the acceptance flow, although only an account with the invited email address can complete it. Don't log the URL or send it over insecure channels.

This operation is create-or-refresh per team and email: if a pending invitation already exists for the invitee, it's returned with its expiry reset to 30 days from the request and its role updated to the requested role, rather than a duplicate being created. Callers must not assume the response is byte-for-byte immutable, because an expired-and-reaped invitation yields a new URL. It sends another email and replaces the reminder schedule when `send_email` is true. A call within the cooldown period returns a `429` without refreshing the invitation, sending email, or changing reminders.

## HTTP method and URL path

POST` https://api.canva.com/admin/v1/teams/{teamId}/invitations`

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

## Path parameters

`teamId``string`

Required

The team ID.

## Body parameters

`email``string`

Required

The email address to invite. The email domain doesn't need to be verified by the organization.

**Minimum length:** `1`

**Maximum length:** `254`

`role``string`

Required

The role of the member in the team.

**Available values:**

  * `admin`
  * `designer`
  * `member`



`send_email``boolean`

Optional

When true, Canva sends the invitation email and its standard reminders. When false or omitted, Canva sends no email or reminder.

**Default value:** `false`

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
    
    
    curl --request POST 'https://api.canva.com/admin/v1/teams/{teamId}/invitations' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "email": "drsmith@brightsmiledental.com",
    
      "role": "member"
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/teams/{teamId}/invitations", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
      },
    
      body: JSON.stringify({
    
        "email": "drsmith@brightsmiledental.com",
    
        "role": "member"
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/teams/{teamId}/invitations"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"email\": \"drsmith@brightsmiledental.com\", \"role\": \"member\"}"))
    
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
    
        "email": "drsmith@brightsmiledental.com",
    
        "role": "member"
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/admin/v1/teams/{teamId}/invitations",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/teams/{teamId}/invitations"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"email\": \"drsmith@brightsmiledental.com\", \"role\": \"member\"}",
    
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
    
    	  "email": "drsmith@brightsmiledental.com",
    
    	  "role": "member"
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/admin/v1/teams/{teamId}/invitations"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/teams/{teamId}/invitations",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "email" => "drsmith@brightsmiledental.com",
    
        "role" => "member"
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/teams/{teamId}/invitations')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "email": "drsmith@brightsmiledental.com",
    
      "role": "member"
    
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

## Example response
    
    
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

### 403 Forbidden

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error responses

##### A target team has reached its maximum member capacity
    
    
    {
    
      "code": "max_limit_reached",
    
      "message": "One or more provided teams have reached its maximum member capacity"
    
    }

JSON

Copy

##### The organization restricts invitations to email domains it owns
    
    
    {
    
      "code": "domain_restricted",
    
      "message": "An invitation can't be created for this email because only users with an email owned by the organization can be invited"
    
    }

JSON

Copy

##### An invitation can't be created for this team or recipient
    
    
    {
    
      "code": "permission_denied",
    
      "message": "An invitation can't be created for this team or recipient"
    
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

### 409 Conflict

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### The invitee is already a member of the team
    
    
    {
    
      "code": "user_already_member",
    
      "message": "A user with this email is already a member of team {teamId}"
    
    }

JSON

Copy

### 429 Too many requests

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### An invitation email can't be resent for this recipient
    
    
    {
    
      "code": "too_many_requests",
    
      "message": "Email can't be resent for this recipient within the resend cooldown"
    
    }

JSON

Copy
