---
url: https://www.canva.dev/docs/scim/list-users/
title: List users - Canva SCIM API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:07.468529+00:00
---

# List users - Canva SCIM API Documentation

> Source: https://www.canva.dev/docs/scim/list-users/

Canva SCIM API

[Overview](https://www.canva.dev/docs/scim/)[Authentication](https://www.canva.dev/docs/scim/authentication/)[Users, Groups, and Teams](https://www.canva.dev/docs/scim/users-groups-and-teams/)

SCIM User API reference

[Create a user](https://www.canva.dev/docs/scim/create-user/)[Get a user](https://www.canva.dev/docs/scim/get-user/)[List users](https://www.canva.dev/docs/scim/list-users/)[Update all information for a user](https://www.canva.dev/docs/scim/update-all-information-user/)[Update individual attributes for a user](https://www.canva.dev/docs/scim/update-individual-attributes-user/)[Delete a user](https://www.canva.dev/docs/scim/delete-user/)

SCIM Group API reference

[Create a group](https://www.canva.dev/docs/scim/create-group/)[Get a group](https://www.canva.dev/docs/scim/get-group/)[List groups](https://www.canva.dev/docs/scim/list-groups/)[Update all information for a group](https://www.canva.dev/docs/scim/update-all-information-group/)[Update individual attributes for a group](https://www.canva.dev/docs/scim/update-individual-attributes-group/)[Delete a group](https://www.canva.dev/docs/scim/delete-group/)

# List users

Copy page

Gets a paginated list of all users in a Canva team, including inactive users.

You can use the `startIndex` and `count` parameters to control the pagination of the response.

You can also provide a `filter` parameter to narrow down the users returned to only include those matching the filter.

## HTTP method and URL path

GET` https://www.canva.com/_scim/v2/Users`

## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

## Query parameters

`startIndex``integer`

Optional

Used to paginate the response: the index of the first result to return.

`count``integer`

Optional

Used to paginate the response: the number of results to return. Must be between `1` and `10`.

`filter``string`

Optional

A filter to narrow down the results returned, using the equals (`eq`) query parameter. The following filters are supported:

  * Return the user matching the SCIM `userName` value: `userName eq "{saml_name_id}"`.

For example: `GET /_scim/v2/Users?filter=userName%20eq%20"aliddell"`

  * Return the user matching the SCIM `externalId` value: `externalId eq "{idp_provided_external_id}"`.

For example: `GET /_scim/v2/Users?filter=externalId%20eq%20"abcdefgh12345678"`




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
    
    
    curl --request GET 'https://www.canva.com/_scim/v2/Users' \
    
    --header 'Authorization: Bearer {token}'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://www.canva.com/_scim/v2/Users", {
    
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
    
                .uri(URI.create("https://www.canva.com/_scim/v2/Users"))
    
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
    
    
    
    
    response = requests.get("https://www.canva.com/_scim/v2/Users",
    
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
    
      RequestUri = new Uri("https://www.canva.com/_scim/v2/Users"),
    
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
    
    	url := "https://www.canva.com/_scim/v2/Users"
    
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
    
      CURLOPT_URL => "https://www.canva.com/_scim/v2/Users",
    
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
    
    
    
    
    url = URI('https://www.canva.com/_scim/v2/Users')
    
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

`schemas``string[]`

**Available values:** The only valid value is `urn:ietf:params:scim:api:messages:2.0:ListResponse`.

`totalResults``integer`

The total number of results matching the query.

`startIndex``integer`

The index of the first result.

`itemsPerPage``integer`

The number of results returned in the current page.

`resources``ScimUserResponse[]`

An array of the users returned in the current page of results.

Properties of **resources**

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
    
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    
      ],
    
      "totalResults": 1,
    
      "startIndex": 1,
    
      "itemsPerPage": 10,
    
      "resources": [
    
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
    
      ]
    
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

**Available values:** The only valid value is `Unsupported filter field`.

`status``string`

The HTTP status code of the error.

#### Example error response
    
    
    {
    
      "schemas": [
    
        "urn:ietf:params:scim:api:messages:2.0:Error"
    
      ],
    
      "detail": "Unsupported filter field",
    
      "status": "403"
    
    }

JSON

Copy
