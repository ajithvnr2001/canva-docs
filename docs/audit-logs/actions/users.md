---
url: https://www.canva.dev/docs/audit-logs/actions/users/
title: Users - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:55.432622+00:00
---

# Users - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/users/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Users

Copy page

## Create a user

An `actor` triggers this event when they create (or provision) a new Canva user, including when an individual creates a Canva user account by visiting a team invitation link.

The `reason` field contains the reason the user was created. For example, they accepted a team invitation or they were provisioned by a SCIM provider.

`type``string`

**Default value:** `CREATE_USER`

**Available values:** The only valid value is `CREATE_USER`.

`display_name``string`

Optional

The user's display name. This is used to represent the user with text in a UI.

`first_name``string`

Optional

The user's first name.

`last_name``string`

Optional

The user's last name.

`email``string`

Optional

The user's email address.

`email_verified``boolean`

Optional

Whether the user's email address has been verified.

`phone_number``string`

Optional

The user's phone number.

`country_code``string`

Optional

The user's country code, shown on user's public profile page.

`locale``string`

Optional

The supported locale for the user.

`managing_entity``ManagingEntity`

Optional

The entity that manages the user.

TEAMTEAM

ORGANIZATIONORGANIZATION

A managing entity that is a team.

`type``string`

**Default value:** `TEAM`

**Available values:** The only valid value is `TEAM`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A managing entity that is an organization.

`type``string`

**Default value:** `ORGANIZATION`

**Available values:** The only valid value is `ORGANIZATION`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`saml_accounts``SamlAccount[]`

Optional

SAML accounts for the user.

Properties of **saml_accounts**

`idp_issuer``string`

A unique identifier for the SAML identity provider.

`name_id``string`

The unique identifier for the user, within the scope of `idp_issuer`. This value is often an email address.

`oauth_accounts``OauthAccount[]`

Optional

OAuth accounts for the user.

Properties of **oauth_accounts**

`platform``string`

The OAuth platform.

`external_user_id``string`

The account ID for the user on the external platform.

`totp_mfa_enabled``boolean`

Optional

Whether TOTP MFA (Time-based One-Time Password Multi-Factor Authentication) is enabled for the user.

`sms_mfa_enabled``boolean`

Optional

Whether SMS MFA (SMS-based Multi-Factor Authentication) is enabled for the user.

`reason``TeamMembershipChangeReason`

Optional

The reason for the change.

INVITATION_ACCEPTEDINVITATION_ACCEPTED

JOIN_POLICY_ALLOWEDJOIN_POLICY_ALLOWED

REQUEST_TO_JOIN_APPROVEDREQUEST_TO_JOIN_APPROVED

SCIMSCIM

SAML_JIT_PROVISIONINGSAML_JIT_PROVISIONING

PROVISIONING_POLICYPROVISIONING_POLICY

ADMIN_APIADMIN_API

An invitation to join team was accepted

`type``string`

**Default value:** `INVITATION_ACCEPTED`

**Available values:** The only valid value is `INVITATION_ACCEPTED`.

`inviter``AuditLogUser`

Optional

A Canva user.

Properties of **inviter**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

The change was permitted by your [Team discovery and settings⁠(opens in a new tab or window)](https://www.canva.com/help/team-discovery/).

`type``string`

**Default value:** `JOIN_POLICY_ALLOWED`

**Available values:** The only valid value is `JOIN_POLICY_ALLOWED`.

A user request to join your team was approved.

`type``string`

**Default value:** `REQUEST_TO_JOIN_APPROVED`

**Available values:** The only valid value is `REQUEST_TO_JOIN_APPROVED`.

The change was made through your team's configured [SCIM Identity Provider⁠(opens in a new tab or window)](https://www.canva.com/help/scim-provisioning-and-deprovisioning/).

`type``string`

**Default value:** `SCIM`

**Available values:** The only valid value is `SCIM`.

SAML Just-In-Time provisioning. This event can be triggered by events like a user [linking their Canva account with your SSO provider⁠(opens in a new tab or window)](https://www.canva.com/help/sso-linking/) or when you [set up Single Sign-On (SSO)⁠(opens in a new tab or window)](https://www.canva.com/help/set-up-sso/) for your team.

`type``string`

**Default value:** `SAML_JIT_PROVISIONING`

**Available values:** The only valid value is `SAML_JIT_PROVISIONING`.

This change was triggered by an provisioning policy.

`type``string`

**Default value:** `PROVISIONING_POLICY`

**Available values:** The only valid value is `PROVISIONING_POLICY`.

`provisioning_policy``AuditLogProvisioningPolicy`

Optional

A Canva provisioning policy.

Properties of **provisioning_policy**

`id``string`

The provisioning policy ID.

`name``string`

Optional

The provisioning policy name.

The change was made through the Admin API.

`type``string`

**Default value:** `ADMIN_API`

**Available values:** The only valid value is `ADMIN_API`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_USER",
    
        "display_name": "Jane Doe",
    
        "first_name": "Jane",
    
        "last_name": "Doe",
    
        "email": "jane.doe@example.com",
    
        "email_verified": true,
    
        "phone_number": 1234567890,
    
        "country_code": 65,
    
        "locale": "en-AU",
    
        "managing_entity": {
    
          "team": {
    
            "id": "BXeFatjDhdR",
    
            "display_name": "Acme Team"
    
          },
    
          "type": "TEAM"
    
        },
    
        "saml_accounts": [
    
          {
    
            "idp_issuer": "http://www.exampleidp.com/abcdefgh12345",
    
            "name_id": "alex.doe@example.com"
    
          }
    
        ],
    
        "oauth_accounts": [
    
          {
    
            "platform": "EXAMPLE_OAUTH_PLATFORM",
    
            "external_user_id": "3371C5F5-9577-444D-B788-8F4B2CC461A7"
    
          }
    
        ],
    
        "totp_mfa_enabled": true,
    
        "sms_mfa_enabled": true,
    
        "reason": {
    
          "type": "INVITATION_ACCEPTED",
    
          "inviter": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          }
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a user's details

An `actor` triggers this event when they update a user's account details. This includes when a user updates their own account details.

We only log the user properties that the actor requested changes for. The changed fields are listed in the `changed_fields` array.

Some changed fields, such as `PASSWORD`, might be in the `changed_fields` array but won't have a property included in the log.

If the user was updated as part of the login process, the actor might be set to `ANONYMOUS`.

`type``string`

**Default value:** `UPDATE_USER`

**Available values:** The only valid value is `UPDATE_USER`.

`changed_fields``string[]`

Optional

Fields requested to be changed in this update.

**Available values:**

  * `PASSWORD`: The user's password.
  * `DISPLAY_NAME`: The user's display name.
  * `FIRST_NAME`: The user's first name.
  * `LAST_NAME`: The user's last name.
  * `EMAIL`: The user's email address.
  * `EMAIL_VERIFIED`: Whether the user's email address has been verified.
  * `PHONE_NUMBER`: The user's phone number.
  * `CITY`: The user's city.
  * `COUNTRY_CODE`: The user's country code.
  * `LOCALE`: The user's locale.
  * `MANAGING_ENTITY`: The entity that manages the user.
  * `SAML_ACCOUNTS`: SAML accounts.
  * `OAUTH_ACCOUNTS`: OAUTH accounts.
  * `TOTP_MFA_ENABLED`: Whether TOTP MFA (Time-based One-Time Password Multi-Factor Authentication) is enabled for the user.
  * `SMS_MFA_ENABLED`: Whether SMS MFA (SMS-based Multi-Factor Authentication) is enabled for the user.
  * `PASSKEYS`: The user's passkeys.



`display_name``string`

Optional

The user's display name. This is used to represent the user with text in a UI.

`first_name``string`

Optional

The user's first name.

`last_name``string`

Optional

The user's last name.

`email``string`

Optional

The user's email address.

`email_verified``boolean`

Optional

Whether the user's email address has been verified.

`phone_number``string`

Optional

The user's phone number.

`country_code``string`

Optional

The user's country code, shown on user's public profile page.

`locale``string`

Optional

The supported locale for the user.

`managing_entity``ManagingEntity`

Optional

The entity that manages the user.

TEAMTEAM

ORGANIZATIONORGANIZATION

A managing entity that is a team.

`type``string`

**Default value:** `TEAM`

**Available values:** The only valid value is `TEAM`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A managing entity that is an organization.

`type``string`

**Default value:** `ORGANIZATION`

**Available values:** The only valid value is `ORGANIZATION`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`saml_accounts``SamlAccount[]`

Optional

SAML accounts for the user.

Properties of **saml_accounts**

`idp_issuer``string`

A unique identifier for the SAML identity provider.

`name_id``string`

The unique identifier for the user, within the scope of `idp_issuer`. This value is often an email address.

`oauth_accounts``OauthAccount[]`

Optional

OAuth accounts for the user.

Properties of **oauth_accounts**

`platform``string`

The OAuth platform.

`external_user_id``string`

The account ID for the user on the external platform.

`totp_mfa_enabled``boolean`

Optional

Whether TOTP MFA (Time-based One-Time Password Multi-Factor Authentication) is enabled for the user.

`sms_mfa_enabled``boolean`

Optional

Whether SMS MFA (SMS-based Multi-Factor Authentication) is enabled for the user.

`passkeys``Passkey[]`

Optional

Passkeys for the user.

Properties of **passkeys**

`id``string`

The passkey ID.

`reason``UpdateUserChangeReason`

Optional

Why the user's details changed.

PASSWORD_RESET_WITH_LINKPASSWORD_RESET_WITH_LINK

PASSWORD_RESET_WITH_SMS_CODEPASSWORD_RESET_WITH_SMS_CODE

PASSWORD_RESET_WITH_EMAIL_CODEPASSWORD_RESET_WITH_EMAIL_CODE

The user's password was reset and their identity was verified using a link in an email.

`type``string`

**Default value:** `PASSWORD_RESET_WITH_LINK`

**Available values:** The only valid value is `PASSWORD_RESET_WITH_LINK`.

`email``string`

Optional

The email address used for verification when resetting the password.

The user's password was reset and their identity was verified using a code the user received via SMS.

`type``string`

**Default value:** `PASSWORD_RESET_WITH_SMS_CODE`

**Available values:** The only valid value is `PASSWORD_RESET_WITH_SMS_CODE`.

`phone_number``string`

Optional

The phone number used for verification when resetting the password.

The user's password was reset and their identity was verified using an email code.

`type``string`

**Default value:** `PASSWORD_RESET_WITH_EMAIL_CODE`

**Available values:** The only valid value is `PASSWORD_RESET_WITH_EMAIL_CODE`.

`email``string`

Optional

The email address used for verification when resetting the password.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_USER",
    
        "changed_fields": [
    
          "PASSWORD",
    
          "DISPLAY_NAME",
    
          "FIRST_NAME",
    
          "LAST_NAME",
    
          "EMAIL",
    
          "EMAIL_VERIFIED",
    
          "PHONE_NUMBER",
    
          "CITY",
    
          "COUNTRY_CODE",
    
          "LOCALE",
    
          "MANAGING_ENTITY",
    
          "SAML_ACCOUNTS",
    
          "OAUTH_ACCOUNTS",
    
          "TOTP_MFA_ENABLED",
    
          "SMS_MFA_ENABLED",
    
          "PASSKEYS"
    
        ],
    
        "display_name": "Jane Doe",
    
        "first_name": "Jane",
    
        "last_name": "Doe",
    
        "email": "jane.doe@example.com",
    
        "email_verified": true,
    
        "phone_number": 1234567890,
    
        "country_code": 65,
    
        "locale": "en-AU",
    
        "managing_entity": {
    
          "team": {
    
            "id": "BXeFatjDhdR",
    
            "display_name": "Acme Team"
    
          },
    
          "type": "TEAM"
    
        },
    
        "saml_accounts": [
    
          {
    
            "idp_issuer": "http://www.exampleidp.com/abcdefgh12345",
    
            "name_id": "alex.doe@example.com"
    
          }
    
        ],
    
        "oauth_accounts": [
    
          {
    
            "platform": "EXAMPLE_OAUTH_PLATFORM",
    
            "external_user_id": "3371C5F5-9577-444D-B788-8F4B2CC461A7"
    
          }
    
        ],
    
        "totp_mfa_enabled": true,
    
        "sms_mfa_enabled": true,
    
        "passkeys": [
    
          {
    
            "id": "00320131-4957-4EBD-9569-FDED5F0A4F2D"
    
          }
    
        ],
    
        "reason": {
    
          "type": "PASSWORD_RESET_WITH_LINK",
    
          "email": "jane.doe@example.com"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete a user

An `actor` triggers this event when they delete a user's account. This includes when a user deletes their own account.

`type``string`

**Default value:** `DELETE_USER`

**Available values:** The only valid value is `DELETE_USER`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_USER"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Cancel the deletion of a user

An `actor` triggers this event when they cancel or undo the deletion of a user's account. This includes when a user cancels the deletion of their own account.

`type``string`

**Default value:** `UNDELETE_USER`

**Available values:** The only valid value is `UNDELETE_USER`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UNDELETE_USER"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Create multi-factor authentication (MFA) backup codes

An `actor` triggers this event when they generate multi-factor authentication (MFA) backup codes for their account. For details on generating MFA backup codes, see [Canva Help: Setting up Multi-Factor Authentication (MFA) — Generate backup codes⁠(opens in a new tab or window)](https://www.canva.com/help/login-verification/).

`type``string`

**Default value:** `CREATE_MFA_BACKUP_CODES`

**Available values:** The only valid value is `CREATE_MFA_BACKUP_CODES`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_MFA_BACKUP_CODES"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Log in

An `actor` triggers this event when they log into Canva.

The actor will be `USER` if the login is successful. If the login is unsuccessful, the actor will be `ANONYMOUS`.

`type``string`

**Default value:** `LOGIN`

**Available values:** The only valid value is `LOGIN`.

`login_type``string`

Optional

The general type of user login being attempted.

**Available values:**

  * `PASSWORD`: User login with credentials, such as email address, user ID, phone number, and password.
  * `ONE_TIME_PASSWORD`: User login with a temporary code delivered to the user's email address or phone.
  * `MULTI_FACTOR_AUTHENTICATION`: User login with multi-factor authentication.
  * `OAUTH`: User login with a social account or other third-party provider.
  * `SAML`: User login with single sign-on for a specific email domain.
  * `PASSKEY`: User login with a passkey (such as a security key).
  * `OTHER`: Other types of user login.
  * `LEARNING_TOOLS_INTEROPERABILITY`: User login for education users from a Learning Management System.



`oauth_platform``string`

Optional

The OAuth platform used for login. Only set if the `login_type` is `OAUTH`.

**Available values:**

  * `APPLE`
  * `ATLASSIAN`
  * `CLEVER`
  * `DROPBOX`
  * `FACEBOOK`
  * `GITHUB`
  * `GOOGLE`
  * `HUAWEI`
  * `INSTAGRAM`
  * `KAKAO`
  * `LARK`
  * `LINE`
  * `LINKEDIN`
  * `MAILCHIMP`
  * `MICROSOFT`
  * `NAVER`
  * `CHATGPT`
  * `PINTEREST`
  * `QQ`
  * `SLACK`
  * `TRELLO`
  * `TUMBLR`
  * `TURKEY_EDU`
  * `TWITTER`
  * `WECHAT`
  * `WEIBO`
  * `YAHOO_JAPAN`



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "LOGIN",
    
        "login_type": "PASSWORD",
    
        "oauth_platform": "APPLE"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Log out

An `actor` triggers this event when they log out of Canva.

`type``string`

**Default value:** `LOGOUT`

**Available values:** The only valid value is `LOGOUT`.

`all_users``boolean`

Optional

Whether the `actor` has requested that all users on the device are logged out. If `false`, only the current user is logged out.

`all_sessions``boolean`

Optional

Whether the `actor` has requested that all sessions across all devices are logged out. If `false`, only the current session is logged out.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "LOGOUT",
    
        "all_users": false,
    
        "all_sessions": true
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
