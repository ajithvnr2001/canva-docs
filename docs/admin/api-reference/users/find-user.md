---
url: https://www.canva.dev/docs/admin/api-reference/users/find-user/
title: Find user - Users - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:37.251534+00:00
---

# Find user - Users - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/api-reference/users/find-user/

Users

[Create user](https://www.canva.dev/docs/admin/api-reference/users/create-user/)[Find user](https://www.canva.dev/docs/admin/api-reference/users/find-user/)[Get user](https://www.canva.dev/docs/admin/api-reference/users/get-user/)[List users](https://www.canva.dev/docs/admin/api-reference/users/list-users/)[Update user](https://www.canva.dev/docs/admin/api-reference/users/update-user/)[List user team memberships](https://www.canva.dev/docs/admin/api-reference/users/list-user-team-memberships/)[List user group memberships](https://www.canva.dev/docs/admin/api-reference/users/list-user-group-memberships/)

# Find user

Copy page

Finds a user in the caller's organization by exact email.

The email address is restricted data and is accepted only in the JSON request body. The response contains zero or one user.

## HTTP method and URL path

POST` https://api.canva.com/admin/v1/users/find`

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

`Content-Type``string`

Required

Indicates the media type of the information sent in the request. This must be set to `application/json`.

For example: `Content-Type: application/json`

## Body parameters

`email``string`

Required

The email address of the user to find.

**Minimum length:** `1`

**Maximum length:** `254`

## Example request

Examples for using the `/v1/users/find` endpoint:

cURLcURL

Node.jsNode.js

JavaJava

PythonPython

C#C#

GoGo

PHPPHP

RubyRuby
    
    
    curl --request POST 'https://api.canva.com/admin/v1/users/find' \
    
    --header 'Authorization: Bearer {token}' \
    
    --header 'Content-Type: application/json' \
    
    --data '{
    
      "email": "drsmith@brightsmiledental.com"
    
    }'

SH

Copy
    
    
    const fetch = require("node-fetch");
    
    
    
    
    fetch("https://api.canva.com/admin/v1/users/find", {
    
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
    
                .uri(URI.create("https://api.canva.com/admin/v1/users/find"))
    
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
    
    
    
    
    response = requests.post("https://api.canva.com/admin/v1/users/find",
    
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
    
      RequestUri = new Uri("https://api.canva.com/admin/v1/users/find"),
    
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
    
    
    
    
    	url := "https://api.canva.com/admin/v1/users/find"
    
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
    
      CURLOPT_URL => "https://api.canva.com/admin/v1/users/find",
    
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
    
    
    
    
    url = URI('https://api.canva.com/admin/v1/users/find')
    
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

`user``User`

Optional

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

## Example responses

### Found user
    
    
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

### No matching user found
    
    
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
    
    
    {
    
      "code": "string",
    
      "message": "string"
    
    }

JSON

Copy
