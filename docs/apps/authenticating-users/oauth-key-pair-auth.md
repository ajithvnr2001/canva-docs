---
url: https://www.canva.dev/docs/apps/authenticating-users/oauth-key-pair-auth/
title: Key-pair authentication - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:32.106047+00:00
---

# Key-pair authentication - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/authenticating-users/oauth-key-pair-auth/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Key-pair authentication

Authenticate with OAuth providers using RSA key pairs instead of client secrets.

Copy page

Key-pair authentication is an alternative to [client secret authentication](https://www.canva.dev/docs/apps/authenticating-users/oauth/#prerequisite-configure-developer-portal) for OAuth providers. Instead of using a shared client secret, your app authenticates using a private/public RSA key pair to generate JWT Bearer tokens, as defined in [RFC 7523⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7523).

When you configure key-pair authentication, Canva uses the private key to generate and sign a JWT Bearer token, then sends the token to the OAuth provider's token exchange endpoint. The provider verifies the token's signature using the corresponding public key.

## When to use key-pair authentication

Use key-pair authentication when your OAuth provider requires JWT Bearer token authentication instead of client secret authentication. Some providers don't support client secrets for custom OAuth clients and require key-pair authentication instead.

Key-pair authentication offers several benefits:

  * **Enhanced security:** Eliminates the need for a shared client secret with the provider and reduces exposure of credentials in outbound requests.
  * **Industry standard:** Compliant with [RFC 7523⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7523), supported by multiple OAuth providers.
  * **Programmatic access:** Ideal for service-to-service authentication without interactive user sessions.



If your OAuth provider supports client secret authentication, you can use the [standard OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/) instead.

## Key requirements

Canva supports the following key specifications for key-pair authentication:

Requirement| Value  
---|---  
Key type| RSA only (ECDSA isn't supported)  
Key format| PEM (PKCS#8)  
Key size| Minimum 2048 bits  
Algorithm| RS256 only  
  
## Generate an RSA key pair

To generate a compliant RSA key pair, use OpenSSL:

  1. Generate a 2048-bit RSA private key in PKCS#8 PEM format:
         
         openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

SHELL

Copy

  2. Extract the public key from the private key:
         
         openssl pkey -in private_key.pem -pubout -out public_key.pem

SHELL

Copy




Store your private key securely. Never commit private keys to version control, share them in plaintext, or expose them in client-side code. If your private key is compromised, generate a new key pair and update your credential immediately.

The private key must be in PKCS#8 PEM format. A valid private key file starts with `-----BEGIN PRIVATE KEY-----` and ends with `-----END PRIVATE KEY-----`:
    
    
    -----BEGIN PRIVATE KEY-----
    
    MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC7...
    
    (base64-encoded key data)
    
    ...
    
    -----END PRIVATE KEY-----

Copy

Keys in PKCS#1 format (starting with `-----BEGIN RSA PRIVATE KEY-----`) aren't supported. Use the OpenSSL commands in the previous section to generate a key in the correct format.

## Configure key-pair authentication in the Developer Portal

To configure key-pair authentication for an OAuth provider:

  1. Locate your app in the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).

  2. Go to **Inside Canva > Auth providers**. This page appears once your app has an intent.

  3. Complete the settings below, using the information supplied by the authorization server:

     * **Provider** : The issuer field defined by the authorization server.
     * **Client ID** : A unique identifier for your app. Issued by the authorization server.
     * **Authentication method** : Select **Key Pair**.
     * **Private Key** : Your RSA private key in PEM format (PKCS#8).
     * **Authorization server URL** : The URL where your app redirects the user, letting them authenticate and authorize access for your app. Issued by the authorization server.
     * **Token exchange URL** : The URL where the client exchanges an authorization code for an access token. Issued by the authorization server.
     * **Revocation exchange URL (Optional)** : The URL where the client can request the invalidation of a previously issued token. Issued by the authorization server.
     * **PKCE** : Should be set to on if the authorization server supports it, and set to off if it doesn't (enabled by default).



For more information about configuring OAuth providers, see [Prerequisite: Configure Developer Portal](https://www.canva.dev/docs/apps/authenticating-users/oauth/#prerequisite-configure-developer-portal).

## Public key fingerprint

When you provide a private key, Canva automatically extracts the public key and computes a SHA-256 fingerprint. The fingerprint is in the format `SHA256:{base64-hash}` and is displayed in the Developer Portal after you save the credential.

Some OAuth providers require the public key fingerprint during setup. You can copy the fingerprint from the Developer Portal and provide it to your OAuth provider.

## JWT assertion claims

When using key-pair authentication, Canva generates a JWT Bearer token for each token request, following the [RFC 7523⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7523) standard. The JWT contains the following claims:

Claim| Description| Value  
---|---|---  
`iss` (issuer)| Identifies the principal that issued the JWT.| The client ID  
`sub` (subject)| Identifies the principal that's the subject of the JWT.| The client ID  
`aud` (audience)| Identifies the recipients that the JWT is intended for.| The token exchange URL  
`iat` (issued at)| The time at which the JWT was issued.| Current timestamp  
`exp` (expiration)| The expiration time of the JWT.| 5 minutes from `iat`  
  
Canva generates and signs the JWT automatically using the RS256 algorithm. You don't need to construct or sign the JWT yourself.

## Security considerations

When using key-pair authentication, keep the following security practices in mind:

  * **Secure storage:** Store private keys in a secure location, such as a secrets manager or hardware security module (HSM). Never store private keys in plaintext or in version control.
  * **Key rotation:** Rotate your key pairs regularly by generating a new key pair and updating the credential in the Developer Portal. Key rotation is a manual process. Old credentials continue to work until you explicitly update them.
  * **Least privilege:** Generate dedicated key pairs for each OAuth provider. Don't reuse key pairs across different providers or applications.



## Related documentation

  * [OAuth integration](https://www.canva.dev/docs/apps/authenticating-users/oauth/) — General OAuth concepts and setup
  * [OAuth troubleshooting](https://www.canva.dev/docs/apps/authenticating-users/oauth-troubleshooting/) — Error codes and troubleshooting
  * [RFC 7523: JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants⁠(opens in a new tab or window)](https://datatracker.ietf.org/doc/html/rfc7523)


