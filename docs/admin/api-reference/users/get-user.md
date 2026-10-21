---
url: https://www.canva.dev/docs/admin/api-reference/users/get-user/
title: Get user - Users - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:37.627471+00:00
---

# Get user - Users - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/users/get-user/

Users

[Create user](https://www.canva.dev/docs/admin/api-reference/users/create-user/)[Find user](https://www.canva.dev/docs/admin/api-reference/users/find-user/)[Get user](https://www.canva.dev/docs/admin/api-reference/users/get-user/)[List users](https://www.canva.dev/docs/admin/api-reference/users/list-users/)[Update user](https://www.canva.dev/docs/admin/api-reference/users/update-user/)[List user team memberships](https://www.canva.dev/docs/admin/api-reference/users/list-user-team-memberships/)[List user group memberships](https://www.canva.dev/docs/admin/api-reference/users/list-user-group-memberships/)

# Get user

Copy page

Gets a user.

## HTTP method and URL path

GET` https://api.canva.com/admin/v1/users/{userId}`

## Authentication and authorization

This endpoint requires a valid access token that was generated using client credentials.

### Scopes

The access token must have all the following [scopes](https://www.canva.dev/docs/admin/appendix/scopes/) (permissions):

  * `admin:user:read`



## Header parameters

`Authorization``string`

Required

Provides credentials to authenticate the request, in the form of a `Bearer` token.

For example: `Authorization: Bearer {token}`

## Path parameters

`userId``string`

Required

The user ID.

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
    
    
    curl --request GET 'https://api.canva.com/admin/v1/users/{userId}' \
    
    --header 'Authorization: Bearer {token}'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/users/{userId}", {
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/users/{userId}"))
    
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
    
    
    
    
    response = requests.get("https://api.canva.com/admin/v1/users/{userId}",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/users/{userId}"),
    
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
    
    	url := "https://api.canva.com/admin/v1/users/{userId}"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/users/{userId}",
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/users/{userId}')
    
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

### 404 Not Found

`code``string`

A short string indicating what failed. This field can be used to handle errors programmatically. For a complete list of error codes, see [Error responses](https://www.canva.dev/docs/admin/error-responses/).

`message``string`

A human-readable description of what went wrong.

#### Example error response

##### The user was not found
    
    
    {
    
      "code": "user_not_found",
    
      "message": "User {userId} not found"
    
    }

JSON

Copy
