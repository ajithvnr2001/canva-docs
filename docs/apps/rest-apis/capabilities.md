---
url: https://www.canva.dev/docs/apps/rest-apis/capabilities/
title: Capabilities - Canva for your platform - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:14.707679+00:00
---

# Capabilities - Canva for your platform - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/capabilities/

Canva for your platform

[About Canva's REST APIs](https://www.canva.dev/docs/apps/rest-apis/)

Fundamentals

[API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/)[Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/)[Capabilities](https://www.canva.dev/docs/apps/rest-apis/capabilities/)[API versions](https://www.canva.dev/docs/apps/rest-apis/versions/)

Development guides

[Autofill designs with data](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/)[Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/)

Design guidelines

[User experience guidelines](https://www.canva.dev/docs/apps/rest-apis/experience-guidelines/)[UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/)[Brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/)

# Capabilities

Copy page

Capabilities are features or permissions associated with a user's account, and are often tied to a user's Canva plan. Capabilities are used to control access to premium Canva functionality, and to help apps expose features in a responsive and user-friendly way.

For example, the [resize API](https://www.canva.dev/docs/apps/rest-apis/reference/resizes/) requires the `resize` capability. If a user doesn't have the capability, any request on behalf of the user to that API fails with an error response. An app can pre-check whether or not a user has the `resize` capability before making a request to the resize API.

## APIs that require capabilities

Not all APIs require a capability. If an API requires a capability, it's listed in the reference documentation for the API operation, as well as in its [OpenAPI specification](https://www.canva.dev/docs/apps/rest-apis/#openapi-description), under the `x-required-capabilities` property.

If an API operation lists multiple capabilities, only one capability is required for a user to access the API. This allows for flexible access control across different Canva plans.

## Check user capabilities

Before making a request to an API that requires a capability, apps should use the [Get user capabilities API](https://www.canva.dev/docs/apps/rest-apis/reference/users/get-user-capabilities/) to check whether a user has a required capability.

After checking a user's capabilities, apps can make informed decisions on the user experience, such as:

  * Showing or hiding UI elements
  * Informing the user that a feature is unavailable
  * Avoiding unnecessary API calls that would result in errors



## Error handling

If an app attempts to access an API on behalf of a user that doesn't have a required capability, the API returns a `403 Forbidden` error with a descriptive error message indicating the required capabilities. For example:
    
    
    Not allowed to access getResizeJob, requires one of capabilities ["resize"]

Copy
