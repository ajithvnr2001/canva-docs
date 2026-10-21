---
url: https://www.canva.dev/docs/admin/api-reference/users/create-user/
title: Create user - Users - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:38.133229+00:00
---

# Create user - Users - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/users/create-user/

Users

[Create user](https://www.canva.dev/docs/admin/api-reference/users/create-user/)[Find user](https://www.canva.dev/docs/admin/api-reference/users/find-user/)[Get user](https://www.canva.dev/docs/admin/api-reference/users/get-user/)[List users](https://www.canva.dev/docs/admin/api-reference/users/list-users/)[Update user](https://www.canva.dev/docs/admin/api-reference/users/update-user/)[List user team memberships](https://www.canva.dev/docs/admin/api-reference/users/list-user-team-memberships/)[List user group memberships](https://www.canva.dev/docs/admin/api-reference/users/list-user-group-memberships/)

# Create user

Copy page

Creates a managed user in the caller's organization. The request must meet the following requirements:

  * The email domain must be a verified domain owned by the caller's organization.
  * The SAML identity provider, resolved using the provided `idp_issuer` value, must belong to that organization.



If the email address already belongs to an existing Canva account that isn't part of an organization, that account is brought into the organization instead of a new one being created, and the person might be asked to confirm this. Any existing properties for that user aren't updated with the values provided in the request.

If successful, the response contains the user's Canva ID, email address, display name, first name, last name, SAML account (if any), and organization role.

## HTTP method and URL path

POST` https://api.canva.com/admin/v1/users`

## Authentication and authorization

This endpoint requires a valid access token that was generated using client credentials.

### Scopes

The access token must have all the following [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) (permissions):

  * `admin:user:write`
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

Expand all

`email``string`

Required

The email address of the user. The email domain must be a verified domain owned by the caller's organization.

**Minimum length:** `1`

**Maximum length:** `254`

`display_name``string`

Required

The display name of the user.

**Minimum length:** `1`

`saml_account``SamlAccount`

Required

The SAML account details used to link the user to the organization's identity provider for SSO.

Properties of **saml_account**

`idp_issuer``string`

Required

The issuer id or entity id of the SAML identity provider. Often a unique URL, but not always. Must resolve to an identity provider owned by the caller's organization.

**Minimum length:** `1`

`name_id``string`

Required

The SAML NameID that identifies the user to the identity provider. This value is case sensitive, and shouldn't change.

**Minimum length:** `1`

`team_memberships``TeamMembership[]`

Required

The teams the user is added to. At least one team membership is required so that the user is visible in the [Get user](https://www.canva.dev/docs/admin/api-reference/users/get-user/) and [List users](https://www.canva.dev/docs/admin/api-reference/users/list-users/) API responses.

**Minimum items:** `1`

Properties of **team_memberships**

`team_id``string`

Required

The team ID.

`role``string`

Required

The role of the member in the team.

**Available values:**

  * `admin`
  * `designer`
  * `member`



`first_name``string`

Optional

The first name of the user.

`last_name``string`

Optional

The last name of the user.

`locale``string`

Optional

The locale of the user, as an IETF BCP 47 language tag. Must be a supported language. Defaults to `en` if not provided.

**Default value:** `en`

## Example request

Examples for using the `/v1/users` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/admin/v1/users' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "email": "joe@acme.com",
    
      "display_name": "Joe Smith",
    
      "first_name": "Joe",
    
      "last_name": "Smith",
    
      "locale": "en",
    
      "saml_account": {
    
        "idp_issuer": "https://sso.acme.com/saml/metadata",
    
        "name_id": "joe.smith@acme.com"
    
      },
    
      "team_memberships": [
    
        {
    
          "team_id": "BAAAAAAAAA1",
    
          "role": "member"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/users", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
      },
    
      body: JSON.stringify({
    
        "email": "joe@acme.com",
    
        "display_name": "Joe Smith",
    
        "first_name": "Joe",
    
        "last_name": "Smith",
    
        "locale": "en",
    
        "saml_account": {
    
          "idp_issuer": "https://sso.acme.com/saml/metadata",
    
          "name_id": "joe.smith@acme.com"
    
        },
    
        "team_memberships": [
    
          {
    
            "team_id": "BAAAAAAAAA1",
    
            "role": "member"
    
          }
    
        ]
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/users"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"email\": \"joe@acme.com\", \"display_name\": \"Joe Smith\", \"first_name\": \"Joe\", \"last_name\": \"Smith\", \"locale\": \"en\", \"saml_account\": {\"idp_issuer\": \"https://sso.acme.com/saml/metadata\", \"name_id\": \"joe.smith@acme.com\"}, \"team_memberships\": [{\"team_id\": \"BAAAAAAAAA1\", \"role\": \"member\"}]}"))
    
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
    
        "email": "joe@acme.com",
    
        "display_name": "Joe Smith",
    
        "first_name": "Joe",
    
        "last_name": "Smith",
    
        "locale": "en",
    
        "saml_account": {
    
            "idp_issuer": "https://sso.acme.com/saml/metadata",
    
            "name_id": "joe.smith@acme.com"
    
        },
    
        "team_memberships": [
    
            {
    
                "team_id": "BAAAAAAAAA1",
    
                "role": "member"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.post("https://api.canva.com/admin/v1/users",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/users"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"email\": \"joe@acme.com\", \"display_name\": \"Joe Smith\", \"first_name\": \"Joe\", \"last_name\": \"Smith\", \"locale\": \"en\", \"saml_account\": {\"idp_issuer\": \"https://sso.acme.com/saml/metadata\", \"name_id\": \"joe.smith@acme.com\"}, \"team_memberships\": [{\"team_id\": \"BAAAAAAAAA1\", \"role\": \"member\"}]}",
    
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
    
    	  "email": "joe@acme.com",
    
    	  "display_name": "Joe Smith",
    
    	  "first_name": "Joe",
    
    	  "last_name": "Smith",
    
    	  "locale": "en",
    
    	  "saml_account": {
    
    	    "idp_issuer": "https://sso.acme.com/saml/metadata",
    
    	    "name_id": "joe.smith@acme.com"
    
    	  },
    
    	  "team_memberships": [
    
    	    {
    
    	      "team_id": "BAAAAAAAAA1",
    
    	      "role": "member"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/admin/v1/users"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/users",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "email" => "joe@acme.com",
    
        "display_name" => "Joe Smith",
    
        "first_name" => "Joe",
    
        "last_name" => "Smith",
    
        "locale" => "en",
    
        "saml_account" => [
    
          "idp_issuer" => "https://sso.acme.com/saml/metadata",
    
          "name_id" => "joe.smith@acme.com"
    
        ],
    
        "team_memberships" => [
    
          [
    
            "team_id" => "BAAAAAAAAA1",
    
            "role" => "member"
    
          ]
    
        ]
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/users')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "email": "joe@acme.com",
    
      "display_name": "Joe Smith",
    
      "first_name": "Joe",
    
      "last_name": "Smith",
    
      "locale": "en",
    
      "saml_account": {
    
        "idp_issuer": "https://sso.acme.com/saml/metadata",
    
        "name_id": "joe.smith@acme.com"
    
      },
    
      "team_memberships": [
    
        {
    
          "team_id": "BAAAAAAAAA1",
    
          "role": "member"
    
        }
    
      ]
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `200` response with a JSON body with the following parameters:

`user``User`

A user.

Properties of **user**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

`email``string`

Optional

The email address of the user.

`first_name``string`

Optional

The first name of the user.

`last_name``string`

Optional

The last name of the user.

`last_active_at``integer`

Optional

When the user was last active, as a Unix timestamp (in seconds since the Unix Epoch).

`locale``string`

Optional

The locale of the user, as an IETF BCP 47 language tag.

`role``string`

Optional

The role of the user in the organization.

**Available values:**

  * `admin`
  * `brand_designer`
  * `member`



`saml_account``SamlAccount`

Optional

The SAML account details used to link the user to the organization's identity provider for SSO.

Properties of **saml_account**

`idp_issuer``string`

The issuer id or entity id of the SAML identity provider. Often a unique URL, but not always. Must resolve to an identity provider owned by the caller's organization.

**Minimum length:** `1`

`name_id``string`

The SAML NameID that identifies the user to the identity provider. This value is case sensitive, and shouldn't change.

**Minimum length:** `1`

## Example response
    
    
    {
    
      "user": {
    
        "id": "UAAAAAAAAA1",
    
        "display_name": "Joe Smith",
    
        "email": "joe@acme.com",
    
        "first_name": "Joe",
    
        "last_name": "Smith",
    
        "last_active_at": 1750300000,
    
        "locale": "en",
    
        "role": "admin"
    
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

##### The display name is not allowed
    
    
    {
    
      "code": "invalid_field",
    
      "message": "The supplied display_name is not allowed."
    
    }

JSON

Copy

### 403 Forbidden

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error responses

##### The SAML identity provider is not owned by the caller's organization (or doesn't exist)
    
    
    {
    
      "code": "permission_denied",
    
      "message": "The identity provider is not owned by your organization."
    
    }

JSON

Copy

##### The email domain is not a verified domain owned by the caller's organization
    
    
    {
    
      "code": "permission_denied",
    
      "message": "The email domain is not in your organization's verified domains."
    
    }

JSON

Copy

##### A target team has reached its maximum member capacity
    
    
    {
    
      "code": "max_limit_reached",
    
      "message": "One or more provided teams have reached its maximum member capacity"
    
    }

JSON

Copy

##### The user has reached the maximum number of teams
    
    
    {
    
      "code": "max_limit_reached",
    
      "message": "User {userId} has reached the maximum number of teams"
    
    }

JSON

Copy

### 409 Conflict

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error responses

##### The user matching the email is not active
    
    
    {
    
      "code": "user_not_active",
    
      "message": "The existing user matching this email is not active and can't be added."
    
    }

JSON

Copy

##### The user is awaiting consent from a previous request
    
    
    {
    
      "code": "user_pending_consent",
    
      "message": "A previous request for this user is awaiting their consent. Wait for them to accept before retrying."
    
    }

JSON

Copy

##### The SAML name ID is already in use
    
    
    {
    
      "code": "saml_name_id_not_available",
    
      "message": "The SAML name ID {nameId} is already associated with another user."
    
    }

JSON

Copy

##### An account already exists for this email
    
    
    {
    
      "code": "account_exists",
    
      "message": "That email address is already associated with a Canva account."
    
    }

JSON

Copy

##### The existing account's email is not verified
    
    
    {
    
      "code": "user_email_unverified",
    
      "message": "The existing account for this email hasn't verified its email address, so it can't be linked to your organization."
    
    }

JSON

Copy
