---
url: https://www.canva.dev/docs/admin/api-reference/users/update-user/
title: Update user - Users - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:38.949460+00:00
---

# Update user - Users - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/users/update-user/

Users

[Create user](https://www.canva.dev/docs/admin/api-reference/users/create-user/)[Find user](https://www.canva.dev/docs/admin/api-reference/users/find-user/)[Get user](https://www.canva.dev/docs/admin/api-reference/users/get-user/)[List users](https://www.canva.dev/docs/admin/api-reference/users/list-users/)[Update user](https://www.canva.dev/docs/admin/api-reference/users/update-user/)[List user team memberships](https://www.canva.dev/docs/admin/api-reference/users/list-user-team-memberships/)[List user group memberships](https://www.canva.dev/docs/admin/api-reference/users/list-user-group-memberships/)

# Update user

Copy page

Updates a user that is already managed by the caller's organization. Only the fields provided in the request are updated, and any omitted fields are left unchanged.

The `name` object fields (`display_name`, `first_name`, and `last_name`) must be updated together. To clear a first or last name, set it to an empty string. Blank first and last names are allowed.

## HTTP method and URL path

PATCH` https://api.canva.com/admin/v1/users/{userId}`

## Authentication and authorization

This endpoint requires a valid access token that was generated using client credentials.

### Scopes

The access token must have all the following [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) (permissions):

  * `admin:user:write`



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

`userId``string`

Required

The user ID.

## Body parameters

Expand all

`name``UserNameUpdate`

Optional

The name fields to update for the user.

Properties of **name**

`display_name``string`

Required

The display name of the user.

**Minimum length:** `1`

`first_name``string`

Required

The first name of the user. Set to an empty string to clear the first name.

`last_name``string`

Required

The last name of the user. Set to an empty string to clear the last name.

`locale``string`

Optional

The locale of the user, as an IETF BCP 47 language tag. Must be a supported language.

`saml_account``SamlAccount`

Optional

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

## Example request

Examples for using the `/v1/users/{userId}` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request PATCH 'https://api.canva.com/admin/v1/users/{userId}' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "name": {
    
        "display_name": "Joe Smith",
    
        "first_name": "Joe",
    
        "last_name": "Smith"
    
      },
    
      "locale": "en-GB",
    
      "saml_account": {
    
        "idp_issuer": "https://sso.acme.com/saml/metadata",
    
        "name_id": "joe.smith@acme.com"
    
      }
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/users/{userId}", {
    
      method: "PATCH",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/json",
    
      },
    
      body: JSON.stringify({
    
        "name": {
    
          "display_name": "Joe Smith",
    
          "first_name": "Joe",
    
          "last_name": "Smith"
    
        },
    
        "locale": "en-GB",
    
        "saml_account": {
    
          "idp_issuer": "https://sso.acme.com/saml/metadata",
    
          "name_id": "joe.smith@acme.com"
    
        }
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/users/{userId}"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/json")
    
                .method("PATCH", HttpRequest.BodyPublishers.ofString("{\"name\": {\"display_name\": \"Joe Smith\", \"first_name\": \"Joe\", \"last_name\": \"Smith\"}, \"locale\": \"en-GB\", \"saml_account\": {\"idp_issuer\": \"https://sso.acme.com/saml/metadata\", \"name_id\": \"joe.smith@acme.com\"}}"))
    
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
    
        "name": {
    
            "display_name": "Joe Smith",
    
            "first_name": "Joe",
    
            "last_name": "Smith"
    
        },
    
        "locale": "en-GB",
    
        "saml_account": {
    
            "idp_issuer": "https://sso.acme.com/saml/metadata",
    
            "name_id": "joe.smith@acme.com"
    
        }
    
    }
    
    
    
    
    response = requests.patch("https://api.canva.com/admin/v1/users/{userId}",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/users/{userId}"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"name\": {\"display_name\": \"Joe Smith\", \"first_name\": \"Joe\", \"last_name\": \"Smith\"}, \"locale\": \"en-GB\", \"saml_account\": {\"idp_issuer\": \"https://sso.acme.com/saml/metadata\", \"name_id\": \"joe.smith@acme.com\"}}",
    
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
    
    	  "name": {
    
    	    "display_name": "Joe Smith",
    
    	    "first_name": "Joe",
    
    	    "last_name": "Smith"
    
    	  },
    
    	  "locale": "en-GB",
    
    	  "saml_account": {
    
    	    "idp_issuer": "https://sso.acme.com/saml/metadata",
    
    	    "name_id": "joe.smith@acme.com"
    
    	  }
    
    	}`)
    
    
    
    
    	url := "https://api.canva.com/admin/v1/users/{userId}"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/users/{userId}",
    
      CURLOPT_CUSTOMREQUEST => "PATCH",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "name" => [
    
          "display_name" => "Joe Smith",
    
          "first_name" => "Joe",
    
          "last_name" => "Smith"
    
        ],
    
        "locale" => "en-GB",
    
        "saml_account" => [
    
          "idp_issuer" => "https://sso.acme.com/saml/metadata",
    
          "name_id" => "joe.smith@acme.com"
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/users/{userId}')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Patch.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "name": {
    
        "display_name": "Joe Smith",
    
        "first_name": "Joe",
    
        "last_name": "Smith"
    
      },
    
      "locale": "en-GB",
    
      "saml_account": {
    
        "idp_issuer": "https://sso.acme.com/saml/metadata",
    
        "name_id": "joe.smith@acme.com"
    
      }
    
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

#### Example error responses

##### The display name is not allowed
    
    
    {
    
      "code": "invalid_field",
    
      "message": "The supplied display_name is not allowed."
    
    }

JSON

Copy

##### The locale is not a supported language
    
    
    {
    
      "code": "invalid_field",
    
      "message": "The locale {locale} is not a supported language."
    
    }

JSON

Copy

##### The user is not managed by the organization
    
    
    {
    
      "code": "user_not_managed",
    
      "message": "User {userId} is not managed by the organization"
    
    }

JSON

Copy

### 403 Forbidden

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### The SAML identity provider is not owned by the caller's organization (or doesn't exist)
    
    
    {
    
      "code": "permission_denied",
    
      "message": "The identity provider is not owned by your organization."
    
    }

JSON

Copy

### 409 Conflict

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error responses

##### The user is already linked to a different SAML identity provider
    
    
    {
    
      "code": "user_linked_to_another_idp",
    
      "message": "User {userId} already has a SAML account linked to a different identity provider."
    
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

##### The user is awaiting consent from a previous request
    
    
    {
    
      "code": "user_pending_consent",
    
      "message": "A previous request for this user is awaiting their consent. Wait for them to accept before retrying."
    
    }

JSON

Copy
