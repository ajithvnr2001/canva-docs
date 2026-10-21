---
url: https://www.canva.dev/docs/audit-logs/actions/websites/
title: Websites - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:55.685232+00:00
---

# Websites - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/websites/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Websites

Copy page

## Create a website domain

An `actor` triggers this event when they register a new domain for their website. For information on Canva websites, visit these Canva Help Center articles:

  * [Publish Canva websites⁠(opens in a new tab or window)](https://www.canva.com/help/publishing-canva-websites/).
  * [Change website slug, favicon, and other settings⁠(opens in a new tab or window)](https://www.canva.com/help/website-settings/).



`type``string`

**Default value:** `CREATE_WEBSITE_DOMAIN`

**Available values:** The only valid value is `CREATE_WEBSITE_DOMAIN`.

`name``string`

The domain name (subdomain and the top-level domain).

`domain_type``string`

Optional

The type of domain being created.

**Available values:**

  * `FREE`: A [free my.canva.site domain name⁠(opens in a new tab or window)](https://www.canva.com/help/publishing-websites-for-free/) selected by the user or allocated by Canva.
  * `BRING_YOUR_OWN`: An [existing domain name⁠(opens in a new tab or window)](https://www.canva.com/help/publishing-websites-own-domains/) owned by the user.
  * `PURCHASED`: A domain name [purchased by the user⁠(opens in a new tab or window)](https://www.canva.com/help/publishing-websites-purchasing-domains/) from Canva.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_WEBSITE_DOMAIN",
    
        "domain_type": "FREE",
    
        "name": "example.com"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a website domain's details

An `actor` triggers this event when they modify the data associated with an existing domain.

`type``string`

**Default value:** `UPDATE_WEBSITE_DOMAIN`

**Available values:** The only valid value is `UPDATE_WEBSITE_DOMAIN`.

`update_type``string`

Optional

**Available values:**

  * `RENEW`: Renew a previously purchased domain name registration for an additional period.
  * `REDEEM`: Redeem an expired domain name before it enters the redemption grace period.
  * `RENAME`: Rename a domain to a new public domain, including the website deployed to the current domain.
  * `CONNECT_TO_CANVA`: Connect a domain to Canva for hosting content.
  * `DISCONNECT_FROM_CANVA`: Disconnect a domain from Canva to host content on a different platform.
  * `TRANSFER_DOMAIN`: Unlock a purchased domain and initiate transfer of domain ownership to a different registrar.
  * `CANCEL_TRANSFER`: Cancel an in-progress domain transfer.
  * `UPDATE_DNS_RECORDS`: Update DNS records for the domain.
  * `UPDATE_NAMESERVERS`: Update the nameserver records for the domain.
  * `RESET_NAMESERVERS`: Reset the nameserver records for the domain to their default.
  * `UPDATE_CONTACT`: Update contact information for the domain.



`old_domain_name``string`

Optional

The old domain name (shown when the `update_type` is `RENAME`)

`new_domain_name``string`

Optional

The new domain name (shown when the `update_type` is `RENAME`)

`old_dns_records``DnsRecord[]`

Optional

The old DNS records (shown when the `update_type` is either `UPDATE_DNS_RECORDS` or `RESET_NAMESERVERS`).

Properties of **old_dns_records**

`name``string`

The record name.

`type``string`

The record type.

**Available values:**

  * `A`: IPv4 address record.
  * `AAAA`: IPv6 address record.
  * `CNAME`: Canonical name record.
  * `MX`: Mail exchange record.
  * `TXT`: Text record.
  * `NS`: Nameserver record.
  * `SRV`: Service record.
  * `CAA`: Certificate Authority Authorization record.



`value``string`

The record value.

`new_dns_records``DnsRecord[]`

Optional

The new custom DNS records (shown when the `update_type` is either `UPDATE_DNS_RECORDS` or `RESET_NAMESERVERS`).

Properties of **new_dns_records**

`name``string`

The record name.

`type``string`

The record type.

**Available values:**

  * `A`: IPv4 address record.
  * `AAAA`: IPv6 address record.
  * `CNAME`: Canonical name record.
  * `MX`: Mail exchange record.
  * `TXT`: Text record.
  * `NS`: Nameserver record.
  * `SRV`: Service record.
  * `CAA`: Certificate Authority Authorization record.



`value``string`

The record value.

`new_contact_info``ContactInfo`

Optional

The contact information for a domain owner.

Properties of **new_contact_info**

`name``string`

The combined first and last name of the owner.

`email``string`

The owner's email address.

`phone``string`

The owner's phone number.

`address``string`

The street and number of the owner's address.

`city``string`

The city in the owner's address.

`country``string`

The two-letter ISO country code representing the country in the owner's address.

`organization_name``string`

Optional

The name of the organization that owns the domain.

`postcode``string`

Optional

The postal code in the owner's address.

`state``string`

Optional

The state of the owner's address.

`language``string`

Optional

Language used for messaging the owner.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_WEBSITE_DOMAIN",
    
        "update_type": "RENEW",
    
        "old_domain_name": "old-example.com",
    
        "new_domain_name": "new-example.com",
    
        "old_dns_records": [
    
          {
    
            "name": "example.com",
    
            "type": "A",
    
            "value": "192.168.0.1"
    
          },
    
          {
    
            "name": "example.com",
    
            "type": "CNAME",
    
            "value": "subdomain.example.com"
    
          }
    
        ],
    
        "new_dns_records": [
    
          {
    
            "name": "example.com",
    
            "type": "A",
    
            "value": "192.168.0.12"
    
          },
    
          {
    
            "name": "example.com",
    
            "type": "CNAME",
    
            "value": "subdomain.example.com"
    
          }
    
        ],
    
        "new_contact_info": {
    
          "name": "John Doe",
    
          "email": "john.doe@example.com",
    
          "organization_name": "Acme Corporation",
    
          "phone": "+1-555-555-5555",
    
          "address": "123 Main St",
    
          "postcode": "78701",
    
          "state": "Texas",
    
          "city": "Austin",
    
          "country": "US",
    
          "language": "en"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete a website domain

An `actor` triggers this event when they delete a domain.

`type``string`

**Default value:** `DELETE_WEBSITE_DOMAIN`

**Available values:** The only valid value is `DELETE_WEBSITE_DOMAIN`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_WEBSITE_DOMAIN"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Create an SSO connection for Canva Websites

An `actor` triggers this event when they complete the set up of an SSO connection for Canva Websites.

`type``string`

**Default value:** `CREATE_WEBSITE_SSO_CONNECTION`

**Available values:** The only valid value is `CREATE_WEBSITE_SSO_CONNECTION`.

`domains``AuditLogWebsiteDomain[]`

The domains protected by this SSO connection.

Properties of **domains**

`id``string`

The Web Domain ID.

`name``string`

Optional

The domain name.

`name``string`

Optional

The display name of the SSO connection.

`idp_issuer``string`

Optional

The unique identifier of the SAML application, provided by the Identity Provider (IdP).

`idp_login_url``string`

Optional

The login URL where users are redirected for authentication.

`idp_certificate``string`

Optional

The PEM-encoded X.509 public certificate provided by an Identity Provider (IdP) for SAML authentication.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_WEBSITE_SSO_CONNECTION",
    
        "domains": [
    
          {
    
            "id": "dyTYOgOEyqd",
    
            "name": "example.com"
    
          }
    
        ],
    
        "name": "SSO for example.com",
    
        "idp_issuer": "https://mysecurityprovider.com/123",
    
        "idp_login_url": "https://mysecurityprovider.com/sso/saml",
    
        "idp_certificate": "-----BEGIN CERTIFICATE-----\\nMIIC...\\n-----END CERTIFICATE-----"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an SSO connection for Canva Websites

An `actor` triggers this event when they modify an existing SSO connection for Canva Websites, including certificate updates.

We only log the team properties that the actor requested changes for. The changed fields are listed in the `changed_fields` array.

`type``string`

**Default value:** `UPDATE_WEBSITE_SSO_CONNECTION`

**Available values:** The only valid value is `UPDATE_WEBSITE_SSO_CONNECTION`.

`changed_fields``string[]`

Optional

Fields requested to be changed in this update.

**Available values:**

  * `NAME`: Update the display name of the SSO connection.
  * `DOMAINS`: Update the domains protected by this SSO connection.
  * `IDP_ISSUER`: Update the unique identifier of the SAML application, provided by the Identity Provider (IdP).
  * `IDP_LOGIN_URL`: Update the login URL where users are redirected for authentication.
  * `IDP_CERTIFICATE`: Update the X.509 certificate provided by the Identity Provider (IdP) for SAML authentication.



`old_name``string`

Optional

The previous name of the SSO connection.

`new_name``string`

Optional

The updated name of the SSO connection.

`old_domains``AuditLogWebsiteDomain[]`

Optional

The previous domains protected by this SSO connection.

Properties of **old_domains**

`id``string`

The Web Domain ID.

`name``string`

Optional

The domain name.

`new_domains``AuditLogWebsiteDomain[]`

Optional

The updated domains protected by this SSO connection.

Properties of **new_domains**

`id``string`

The Web Domain ID.

`name``string`

Optional

The domain name.

`old_idp_issuer``string`

Optional

The previous Identity Provider (IdP) issuer.

`new_idp_issuer``string`

Optional

The updated Identity Provider (IdP) issuer.

`old_idp_login_url``string`

Optional

The previous login URL.

`new_idp_login_url``string`

Optional

The updated login URL.

`old_idp_certificate``string`

Optional

The previous PEM-encoded X.509 public certificate provided by an Identity Provider (IdP) for SAML authentication.

`new_idp_certificate``string`

Optional

The updated PEM-encoded X.509 public certificate provided by an Identity Provider (IdP) for SAML authentication.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_WEBSITE_SSO_CONNECTION",
    
        "changed_fields": [
    
          "NAME",
    
          "DOMAINS",
    
          "IDP_ISSUER",
    
          "IDP_LOGIN_URL",
    
          "IDP_CERTIFICATE"
    
        ],
    
        "old_name": "Old SSO Connection",
    
        "new_name": "New SSO Connection",
    
        "old_domains": [
    
          {
    
            "id": "dyTYOgOEyqd",
    
            "name": "example.com"
    
          }
    
        ],
    
        "new_domains": [
    
          {
    
            "id": "dyTYOgOEyqd",
    
            "name": "example.com"
    
          }
    
        ],
    
        "old_idp_issuer": "https://mysecurityprovider.com/123-old",
    
        "new_idp_issuer": "https://mysecurityprovider.com/456-new",
    
        "old_idp_login_url": "https://mysecurityprovider.com/sso/old",
    
        "new_idp_login_url": "https://mysecurityprovider.com/sso/new",
    
        "old_idp_certificate": "-----BEGIN CERTIFICATE-----\\nMIIC...\\n-----END CERTIFICATE-----",
    
        "new_idp_certificate": "-----BEGIN CERTIFICATE-----\\nMIID...\\n-----END CERTIFICATE-----"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete an SSO connection for Canva Websites

An `actor` triggers this event when they delete an SSO connection for Canva Websites.

`type``string`

**Default value:** `DELETE_WEBSITE_SSO_CONNECTION`

**Available values:** The only valid value is `DELETE_WEBSITE_SSO_CONNECTION`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_WEBSITE_SSO_CONNECTION"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
