---
url: https://www.canva.dev/docs/scim/update-individual-attributes-user/
title: Update individual attributes for a user - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:09.000948+00:00
---

# Update individual attributes for a user - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/update-individual-attributes-user/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# Update individual attributes for a user

Copy page

Updates individual attributes for a user. To update a user's attributes, you must use the correct [syntax for the operation, as defined in the SCIM specification⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.2).

For example, to update a user's `work` email and `familyName` values, use the following for the request body:
    
    
    {
    
      "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    
      "Operations": [
    
        {
    
          "op": "replace",
    
          "path": "emails[type eq \"work\"].value",
    
          "value": "my.new.email@example.com"
    
        },
    
        {
    
          "op": "replace",
    
          "path": "name.familyName",
    
          "value": "New-Family-Name"
    
        }
    
      ]
    
    }

JSON

Copy

To deprovision a SCIM user, you can use an operation to set the `active` attribute to `false`. For example:
    
    
    {
    
      "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    
      "Operations": [
    
        {
    
          "op": "replace",
    
          "path": "active",
    
          "value": false
    
        }
    
      ]
    
    }

JSON

Copy

Alternatively, you can provide an operation's `value` object as a list of paths and values to modify. For example:
    
    
    {
    
      "schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
    
      "Operations": [
    
        {
    
          "op": "add",
    
          "value": {
    
            "name.givenName": "New-Given-Name",
    
            "name.familyName": "New-Family-Name",
    
            "externalId": "abcd1234"
    
          }
    
        }
    
      ]
    
    }

JSON

Copy

## HTTP method and URL path

PATCH` https://www.canva.com/_scim/v2/Users/{canva_scim_id}`

## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/scim+json`.

For example: `Content-Type: application/scim+json`

## Path parameters

`canva_scim_id``string`

Required

The Canva-generated SCIM ID for the user.

## Body parameters

Expand all

`schemas``string[]`

Required

The URIs of the SCIM schemas.

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:PatchOp`.

`Operations``object[]`

Required

List of patch operations

Properties of **Operations**

`op``string`

Required

The SCIM patch operation to perform.

**Available values:**

  * `add`
  * `remove`
  * `replace`



`path``string`

Optional

An attribute path describing the target of the operation. For more information, see the [SCIM specification⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.2).

`value``object`

Optional

The value to add, remove, or replace.

## Example request

Examples for using the `/_scim/v2/Users/{canva_scim_id}` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request PATCH 'https://www.canva.com/_scim/v2/Users/{canva_scim_id}' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/scim+json' \
    
    --data '{
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
      ],
    
      "Operations": [
    
        {
    
          "op": "replace",
    
          "path": "name.familyName",
    
          "value": "Liddell"
    
        }
    
      ]
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://www.canva.com/_scim/v2/Users/{canva_scim_id}", {
    
      method: "PATCH",
    
      headers: {
    
        "Authorization": "Bearer {token}",
    
        "Content-Type": "application/scim+json",
    
      },
    
      body: JSON.stringify({
    
        "schemas": [
    
          "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
        ],
    
        "Operations": [
    
          {
    
            "op": "replace",
    
            "path": "name.familyName",
    
            "value": "Liddell"
    
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
    
                .uri(URI.create("https://www.canva.com/_scim/v2/Users/{canva_scim_id}"))
    
                .header("Authorization", "Bearer {token}")
    
                .header("Content-Type", "application/scim+json")
    
                .method("PATCH", HttpRequest.BodyPublishers.ofString("{\"schemas\": [\"urn:ietf:params:scim:api:messages:2.0:PatchOp\"], \"Operations\": [{\"op\": \"replace\", \"path\": \"name.familyName\", \"value\": \"Liddell\"}]}"))
    
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
    
            "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
        ],
    
        "Operations": [
    
            {
    
                "op": "replace",
    
                "path": "name.familyName",
    
                "value": "Liddell"
    
            }
    
        ]
    
    }
    
    
    
    
    response = requests.patch("https://www.canva.com/_scim/v2/Users/{canva_scim_id}",
    
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
    
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Users/{canva_scim_id}"),
    
      Headers =
    
      {
    
        { "Authorization", "Bearer {token}" },
    
      },
    
      Content = new StringContent(
    
        "{\"schemas\": [\"urn:ietf:params:scim:api:messages:2.0:PatchOp\"], \"Operations\": [{\"op\": \"replace\", \"path\": \"name.familyName\", \"value\": \"Liddell\"}]}",
    
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
    
    	    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
    	  ],
    
    	  "Operations": [
    
    	    {
    
    	      "op": "replace",
    
    	      "path": "name.familyName",
    
    	      "value": "Liddell"
    
    	    }
    
    	  ]
    
    	}`)
    
    
    
    
    	url := "https://www.canva.com/_scim/v2/Users/{canva_scim_id}"
    
    	req, _ := http.NewRequest("PATCH", url, payload)
    
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
    
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Users/{canva_scim_id}",
    
      CURLOPT_CUSTOMREQUEST => "PATCH",
    
      CURLOPT_RETURNTRANSFER => true,
    
      CURLOPT_HTTPHEADER => array(
    
        'Authorization: Bearer {token}',
    
        'Content-Type: application/scim+json',
    
      ),
    
      CURLOPT_POSTFIELDS => json_encode([
    
        "schemas" => [
    
          "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
        ],
    
        "Operations" => [
    
          [
    
            "op" => "replace",
    
            "path" => "name.familyName",
    
            "value" => "Liddell"
    
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
    
    
    
    
    url = URI('https://www.canva.com/_scim/v2/Users/{canva_scim_id}')
    
    http = Net::HTTP.new(url.host, url.port)
    
    http.use_ssl = true
    
    
    
    
    request = Net::HTTP::Patch.new(url)
    
    request['Authorization'] = 'Bearer {token}'
    
    request['Content-Type'] = 'application/scim+json'
    
    request.body = <<REQUEST_BODY
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    
      ],
    
      "Operations": [
    
        {
    
          "op": "replace",
    
          "path": "name.familyName",
    
          "value": "Liddell"
    
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

### 404 Not found

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:Error`.

`detail``string`

**Available values:** The only valid value is `No user found for id {canva_scim_id}`.

`status``string`

The HTTP status code of the error.

#### Example error response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:Error"
    
      ],
    
      "detail": "No user found for id {canva_scim_id}",
    
      "status": "404"
    
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
