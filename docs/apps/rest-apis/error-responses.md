---
url: https://www.canva.dev/docs/apps/rest-apis/error-responses/
title: Error responses - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:15.142639+00:00
---

# Error responses - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/error-responses/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

API reference

[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)

App UI Kit reference

[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

Canva REST API reference

[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)

Webhooks notification reference

[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

Tools

[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)

# Error responses

Copy page

When an API request fails, an error response is returned that includes a structured error object. This error object contains:

  * A `code` property with a standardized error code that can be used for programmatic error handling.
  * A `message` property with a human-readable description of what went wrong.



For example:
    
    
    {
    
      "code": "invalid_access_token",
    
      "message": "Access token is invalid"
    
    }

JSON

Copy

## Error codes

The following error codes can be returned by the Canva REST APIs:

  * `internal_error`
  * `invalid_field`
  * `invalid_header_value`
  * `permission_denied`
  * `too_many_requests`
  * `not_found`
  * `bad_request_body`
  * `bad_http_method`
  * `bad_request_params`
  * `bad_query_params`
  * `user_role_required`
  * `endpoint_not_found`
  * `endpoint_gone`
  * `unsupported_version`
  * `invalid_access_token`
  * `revoked_access_token`
  * `missing_field`
  * `missing_scope`
  * `invalid_grant`
  * `invalid_request`
  * `invalid_client`
  * `unauthorized_client`
  * `unsupported_grant_type`
  * `invalid_scope`
  * `invalid_basic_header`
  * `invalid_file_format`
  * `quota_exceeded`
  * `credit_quota_exceeded`
  * `credit_quota_cooldown`
  * `unsupported_content_type`
  * `request_too_large`
  * `folder_not_found`
  * `item_in_multiple_folders`
  * `asset_not_found`
  * `unsupported_asset`
  * `asset_not_ready`
  * `max_limit_reached`
  * `permission_not_found`
  * `permission_exists`
  * `unauthorized_user`
  * `user_not_found`
  * `user_not_eligible`
  * `group_not_found`
  * `app_not_found`
  * `app_has_non_draft_versions`
  * `invalid_status_transition`
  * `translation_validation_failed`
  * `content_not_found`
  * `doctype_not_found`
  * `design_not_found`
  * `offset_too_large`
  * `page_not_found`
  * `design_or_comment_not_found`
  * `design_or_thread_not_found`
  * `review_dismissed`
  * `design_type_not_found`
  * `team_not_found`
  * `team_is_default`
  * `comment_not_found`
  * `too_many_comments`
  * `too_many_replies`
  * `message_too_long`
  * `thread_not_found`
  * `reply_not_found`
  * `design_not_fillable`
  * `autofill_data_invalid`
  * `feature_not_available`
  * `unsupported_design_type`
  * `design_generation_not_enabled`
  * `design_generation_rejected`
  * `license_required`
  * `input_unsafe`
  * `display_name_unavailable`
  * `user_not_managed`
  * `saml_team_id_conflict`
  * `saml_name_id_not_available`
  * `user_linked_to_another_idp`
  * `user_email_unverified`
  * `user_not_active`
  * `user_pending_consent`
  * `account_exists`
  * `domain_restricted`
  * `user_already_member`



## Handling errors

Use the error `code` to handle errors programmatically in your platform. The error codes are standardized across all REST API endpoints, so you can implement consistent error handling logic.

For example:
    
    
    try {
    
      const response = await fetch('/v1/designs', {
    
        headers: {
    
          'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    
        }
    
      });
    
    
    
    
      if (!response.ok) {
    
        const error = await response.json();
    
    
    
    
        switch (error.code) {
    
          case 'invalid_access_token':
    
            // Handle authentication errors
    
            redirectToLogin();
    
            break;
    
          case 'permission_denied':
    
            // Handle authorization errors
    
            showPermissionError();
    
            break;
    
          case 'not_found':
    
            // Handle resource not found
    
            showNotFoundError();
    
            break;
    
          default:
    
            // Handle other errors
    
            showGenericError(error.message);
    
        }
    
      }
    
    } catch (err) {
    
      // Handle network errors
    
      showNetworkError();
    
    }

JAVASCRIPT

Copy

## Troubleshooting common errors

The following table provides guidance on common error codes you may encounter when using the REST APIs:

Error Code| What it means| How to troubleshoot  
---|---|---  
`invalid_access_token`| The provided access token is malformed, expired, or invalid.| Check that your access token is correctly formatted and hasn't expired. Refresh the token if needed, or re-authenticate the user. For more information, see [Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/).  
`permission_denied`| The user doesn't have permission to access the specified resource, such as a design.| Handle the error and consider notifying the user that they don't have permission to access the resource.  
`missing_scope`| The access token doesn't include a required scope for this endpoint.| Add the missing scope to your OAuth authorization request and have the user re-authorize your app. For more information, see [Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/)  
`not_found`| The requested resource doesn't exist or isn't accessible.| Verify the resource ID is correct and the user has access to it. The resource may have been deleted or moved.  
`design_not_found`| The specified design doesn't exist or isn't accessible.| Check the design ID is valid and the user has permission to access it. The design may have been deleted or is in a team the user can't access.  
`too_many_requests`| You've exceeded the API rate limits.| Implement exponential backoff and retry logic. Review your request patterns and consider caching responses to reduce API calls. For polling asynchronous job endpoints, see [API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/#job-polling-strategies).  
`bad_request_body`| The request body is malformed or contains invalid data.| Validate your JSON payload against the API schema. Check for missing required fields or incorrect data types.  
`bad_request_params`| Invalid parameters in the request URL.| Review the endpoint documentation and ensure all required parameters are provided with correct values.  
`invalid_field`| A specific field in your request contains invalid data.| Check the error message for details about which field is invalid and review the expected format or constraints.  
`missing_field`| A required field is missing from your request.| Add all required fields as specified in the API documentation for the endpoint you're calling.  
`internal_error`| An unexpected error occurred on Canva's servers.| This is usually a temporary issue. Retry your request after a brief delay. If the problem persists, see if there is a known incident on [Canva Status⁠(opens in a new tab or window)](https://www.canvastatus.com/) or contact Canva support.
