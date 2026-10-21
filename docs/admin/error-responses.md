---
url: https://www.canva.dev/docs/admin/error-responses/
title: Error responses - Canva Admin API Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:54:39.115612+00:00
---

# Error responses - Canva Admin API Documentation

> Source: https://www.canva.dev/docs/admin/error-responses/

Getting started

[Overview](https://www.canva.dev/docs/admin/)[Creating clients](https://www.canva.dev/docs/admin/creating-clients/)

Fundamentals

[API requests & responses](https://www.canva.dev/docs/admin/api-requests-responses/)[Authentication](https://www.canva.dev/docs/admin/authentication/)[Canva concepts](https://www.canva.dev/docs/admin/canva-concepts/)

API reference

Authentication

Organizations

Teams

Groups

Users

Audit events

Appendix

[Scopes](https://www.canva.dev/docs/admin/appendix/scopes/)[Error responses](https://www.canva.dev/docs/admin/error-responses/)[Changelog](https://www.canva.dev/docs/admin/changelog/)

# Error responses

Copy page

When an API request fails, an error response is returned that includes a structured error object. This error object contains:

  * A `code` property with a standardized error code that can be used for programmatic error handling.
  * A `message` property with a human-readable description of what went wrong.



For example:
    
    
    {
    
      "code": "team_not_found",
    
      "message": "Team {teamId} not found"
    
    }

JSON

Copy

## Error codes

The following error codes can be returned by the Admin APIs:

  * `permission_denied`
  * `too_many_requests`
  * `max_limit_reached`
  * `bad_request_body`
  * `bad_http_method`
  * `bad_request_params`
  * `bad_query_params`
  * `endpoint_not_found`
  * `invalid_access_token`
  * `missing_scope`
  * `invalid_field`
  * `input_unsafe`
  * `display_name_unavailable`
  * `team_not_found`
  * `group_not_found`
  * `team_is_default`
  * `user_not_found`
  * `saml_team_id_conflict`
  * `user_not_managed`
  * `saml_name_id_not_available`
  * `user_linked_to_another_idp`
  * `user_email_unverified`
  * `user_not_active`
  * `user_pending_consent`
  * `account_exists`
  * `domain_restricted`
  * `user_already_member`



## Handling errors

Use the error `code` to handle errors programmatically in your application. The error codes are standardized across all Admin API endpoints, so you can implement consistent error handling logic. The specific errors an individual endpoint can return are shown in the **Error responses** section of that endpoint's reference page.
