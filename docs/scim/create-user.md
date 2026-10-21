---
url: https://www.canva.dev/docs/scim/create-user/
title: Create a user with SCIM - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:05.688987+00:00
---

# Create a user with SCIM - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/create-user/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# Create a user with SCIM

Copy page

Using information from an identity provider (IdP), create a Canva user in a Canva team.

The values for the `email` or `userName` parameters must be unique and can't already be in use.

This API is rate limited to 1 request per second.

## HTTP method and URL path

POST` https://www.canva.com/_scim/v2/Users`

## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/scim+json`.

For example: `Content-Type: application/scim+json`

## Body parameters

Expand all

`schemas``string[]`

Required

The URIs of the SCIM schemas.

**Available values:** The only valid value is `urn:ietf:params:scim:schemas:core:2.0:User`.

`userName``string`

Required

A unique identifier for the user.

`emails``object[]`

Required

The email address for the user.

The Canva SCIM API only supports one email address for each user.

Properties of **emails**

`primary``boolean`

Required

Whether the email is the primary address. Only one email address for a user can be the primary one.

`value``string`

Required

The email address.

`type``string`

Required

The type of email address for the user. The Canva SCIM API only supports `work` as the type of the email address.

**Available values:** The only valid value is `work`.

`externalId``string`

Optional

A string that is an identifier for the resource as defined by the provisioning client.

`displayName``string`

Optional

The name of the user, suitable for display to end-users.

`name``name`

Optional

The components of the user's name.

Properties of **name**

`givenName``string`

Optional

The first or 'given' name for the user.

`familyName``string`

Optional

The last or 'family' name for the user.

`locale``string`

Optional

The user's default location, for example `en_AU`.

`role``string`

Optional

The role of the user.

If an invalid value is provided, the role defaults to `Member`.

Except for `Member`, all other role values map to the Canva "Brand Designer" role. For more information on Canva roles, see [Team roles and permissions⁠(opens in a new tab or window)](https://www.canva.com/help/roles-and-permissions/).

**Default value:** `Member`

**Available values:**

  * `Member`
  * `Teacher`
  * `Staff`
  * `Admin`
  * `Template-designer`
  * `Aide`
  * `Administrator`
  * `School administrator`
  * `School`
  * `Tenant`
  * `Faculty`



`active``boolean`

Optional

Whether the user account is active. Setting this to `false` deprovisions the user in Canva.

## Example request

Examples for using the `/_scim/v2/Users` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://www.canva.com/_scim/v2/Users' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/scim+json' \
    
    --data '{
    
      "schemas": [
    
        "urn:ietf:params:scim:schemas:core:2.0:User"
    
      ],
    
      "externalId": "{idp_provided_external_id}",
    
      "userName": "aliddell",
    
      "displayName": "Alice Liddell",
    
      "name": {
    
        "givenName": "Alice",
    
        "familyName": "Liddell"
    
      },
    
      "emails": [
    
        {
    
          "primary": true,
    
          "value": "alice@acme.com",
    
          "type": "work"
    
        }
    
      ],
    
      "locale": "en_US",
    
      "role": "Member"
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://www.canva.com/_scim/v2/Users", {
    
      method: "POST",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/scim+json",
    
      },
    
      body: JSON.stringify({
    
        "schemas": [
    
          "urn:ietf:params:scim:schemas:core:2.0:User"
    
        ],
    
        "externalId": "{idp_provided_external_id}",
    
        "userName": "aliddell",
    
        "displayName": "Alice Liddell",
    
        "name": {
    
          "givenName": "Alice",
    
          "familyName": "Liddell"
    
        },
    
        "emails": [
    
          {
    
            "primary": true,
    
            "value": "alice@acme.com",
    
            "type": "work"
    
          }
    
        ],
    
        "locale": "en_US",
    
        "role": "Member"
    
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
    
                .uri(URI.create("https://www.canva.com/_scim/v2/Users"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/scim+json")
    
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"schemas\": [\"urn:ietf:params:scim:schemas:core:2.0:User\"], \"externalId\": \"{idp_provided_external_id}\", \"userName\": \"aliddell\", \"displayName\": \"Alice Liddell\", \"name\": {\"givenName\": \"Alice\", \"familyName\": \"Liddell\"}, \"emails\": [{\"primary\": true, \"value\": \"alice@acme.com\", \"type\": \"work\"}], \"locale\": \"en_US\", \"role\": \"Member\"}"))
    
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
    
        "Content-Type": "application/scim+json"
    
    }
    
    
    
    
    data = {
    
        "schemas": [
    
            "urn:ietf:params:scim:schemas:core:2.0:User"
    
        ],
    
        "externalId": "{idp_provided_external_id}",
    
        "userName": "aliddell",
    
        "displayName": "Alice Liddell",
    
        "name": {
    
            "givenName": "Alice",
    
            "familyName": "Liddell"
    
        },
    
        "emails": [
    
            {
    
                "primary": True,
    
                "value": "alice@acme.com",
    
                "type": "work"
    
            }
    
        ],
    
        "locale": "en_US",
    
        "role": "Member"
    
    }
    
    
    
    
    response = requests.post("https://www.canva.com/_scim/v2/Users",
    
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
    
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Users"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"schemas\": [\"urn:ietf:params:scim:schemas:core:2.0:User\"], \"externalId\": \"{idp_provided_external_id}\", \"userName\": \"aliddell\", \"displayName\": \"Alice Liddell\", \"name\": {\"givenName\": \"Alice\", \"familyName\": \"Liddell\"}, \"emails\": [{\"primary\": true, \"value\": \"alice@acme.com\", \"type\": \"work\"}], \"locale\": \"en_US\", \"role\": \"Member\"}",
    
        Encoding.UTF8,
    
        "application/scim+json"
    
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
    
    	  "schemas": [
    
    	    "urn:ietf:params:scim:schemas:core:2.0:User"
    
    	  ],
    
    	  "externalId": "{idp_provided_external_id}",
    
    	  "userName": "aliddell",
    
    	  "displayName": "Alice Liddell",
    
    	  "name": {
    
    	    "givenName": "Alice",
    
    	    "familyName": "Liddell"
    
    	  },
    
    	  "emails": [
    
    	    {
    
    	      "primary": true,
    
    	      "value": "alice@acme.com",
    
    	      "type": "work"
    
    	    }
    
    	  ],
    
    	  "locale": "en_US",
    
    	  "role": "Member"
    
    	}`)
    
    
    
    
    	url := "https://www.canva.com/_scim/v2/Users"
    
    	req, _ := http.NewRequest("POST", url, payload)
    
    	req.Header.Add("Authorization", "Bearer {token}")
    
    	req.Header.Add("Content-Type", "application/scim+json")
    
    
    
    
    	res, _ := http.DefaultClient.Do(req)
    
    	defer res.Body.Close()
    
    	body, _ := io.ReadAll(res.Body)
    
    	fmt.Println(string(body))
    
    }

GO

Copy
    
    
    $curl = curl_init();
    
    curl_setopt_array($curl, array(
    
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Users",
    
      CURLOPT_CUSTOMREQUEST => "POST",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/scim+json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "schemas" => [
    
          "urn:ietf:params:scim:schemas:core:2.0:User"
    
        ],
    
        "externalId" => "{idp_provided_external_id}",
    
        "userName" => "aliddell",
    
        "displayName" => "Alice Liddell",
    
        "name" => [
    
          "givenName" => "Alice",
    
          "familyName" => "Liddell"
    
        ],
    
        "emails" => [
    
          [
    
            "primary" => true,
    
            "value" => "alice@acme.com",
    
            "type" => "work"
    
          ]
    
        ],
    
        "locale" => "en_US",
    
        "role" => "Member"
    
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
    
    
    
    
    url = URI('https://www.canva.com/_scim/v2/Users')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Post.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/scim+json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:schemas:core:2.0:User"
    
      ],
    
      "externalId": "{idp_provided_external_id}",
    
      "userName": "aliddell",
    
      "displayName": "Alice Liddell",
    
      "name": {
    
        "givenName": "Alice",
    
        "familyName": "Liddell"
    
      },
    
      "emails": [
    
        {
    
          "primary": true,
    
          "value": "alice@acme.com",
    
          "type": "work"
    
        }
    
      ],
    
      "locale": "en_US",
    
      "role": "Member"
    
    }
    
    REQUEST_BODY
    
    
    
    
    response = http.request(request)
    
    puts response.read_body

RUBY

Copy

## Success response

Expand all

If successful, the endpoint returns a `201` response with a JSON body with the following parameters:

`schemas``string[]`

The URIs of the SCIM schemas.

**Available values:** The only valid value is `urn:ietf:params:scim:schemas:core:2.0:User`.

`id``string`

The Canva-generated SCIM ID for the user.

`meta``object`

Meta properties for the user.

Properties of **meta**

`resourceType``string`

The SCIM resource type of the object.

**Available values:** The only valid value is `User`.

`created``string`

The timestamp when the object was created.

`userName``string`

A unique identifier for the user.

`displayName``string`

The name of the user, suitable for display to end-users.

`emails``object[]`

The email address for the user.

The Canva SCIM API only supports one email address for each user.

Properties of **emails**

`primary``boolean`

Whether the email is the primary address. Only one email address for a user can be the primary one.

`value``string`

The email address.

`type``string`

The type of email address for the user. The Canva SCIM API only supports `work` as the type of the email address.

**Available values:** The only valid value is `work`.

`active``boolean`

Whether the user account is active. Setting this to `false` deprovisions the user in Canva.

`role``string`

The role of the user.

If an invalid value is provided, the role defaults to `Member`.

Except for `Member`, all other role values map to the Canva "Brand Designer" role. For more information on Canva roles, see [Team roles and permissions⁠(opens in a new tab or window)](https://www.canva.com/help/roles-and-permissions/).

**Default value:** `Member`

**Available values:**

  * `Member`
  * `Teacher`
  * `Staff`
  * `Admin`
  * `Template-designer`
  * `Aide`
  * `Administrator`
  * `School administrator`
  * `School`
  * `Tenant`
  * `Faculty`



`externalId``string`

Optional

A string that is an identifier for the resource as defined by the provisioning client.

`name``name`

Optional

The components of the user's name.

Properties of **name**

`givenName``string`

Optional

The first or 'given' name for the user.

`familyName``string`

Optional

The last or 'family' name for the user.

`locale``string`

Optional

The user's default location, for example `en_AU`.

## Example response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:schemas:core:2.0:User"
    
      ],
    
      "id": "UAFdxab1abC",
    
      "externalId": "abcd1234",
    
      "meta": {
    
        "resourceType": "User",
    
        "created": "2023-09-18T06:08:35Z"
    
      },
    
      "userName": "aliddell",
    
      "displayName": "Alice Liddell",
    
      "name": {
    
        "givenName": "Alice",
    
        "familyName": "Liddell"
    
      },
    
      "emails": [
    
        {
    
          "primary": true,
    
          "value": "alice@acme.com",
    
          "type": "work"
    
        }
    
      ],
    
      "active": true,
    
      "locale": "en_US",
    
      "role": "Member"
    
    }

JSON

Copy

## Error responses

### 400 Bad request

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.

`detail``string`

**Available values:** The only valid value is `No SSO configurations found, please check the settings page`.

`status``string`

The HTTP status code of the error.

#### Example error response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:Error"
    
      ],
    
      "detail": "No SSO configurations found, please check the settings page",
    
      "status": "400"
    
    }

JSON

Copy

### 403 Forbidden

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.

`detail``string`

**Available values:** The only valid value is `Email domain not authorized for SCIM.`.

`status``string`

The HTTP status code of the error.

#### Example error response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:Error"
    
      ],
    
      "detail": "Email domain not authorized for SCIM.",
    
      "status": "403"
    
    }

JSON

Copy

### 409 Conflict

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.

`detail``string`

**Available values:**

  * `userName not available`
  * `Account with email can not be updated. User needs to accept SSO linking`
  * `Account with email already exists. User must first log in with SAML to confirm account ownership`
  * `Account with email is soft deleted. The user must first log in to reactivate their account`



`status``string`

The HTTP status code of the error.

#### Example error response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:Error"
    
      ],
    
      "detail": "userName not available",
    
      "status": "409"
    
    }

JSON

Copy
