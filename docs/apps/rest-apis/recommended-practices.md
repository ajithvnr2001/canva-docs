---
url: https://www.canva.dev/docs/apps/rest-apis/recommended-practices/
title: Recommended practices - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:14.888707+00:00
---

# Recommended practices - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/recommended-practices/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# Recommended practices

Learn how to make a meaningful app.

Copy page

We want to make it easy for you to integrate Canva into your product, while also adhering to the practices provided on this page. These practices apply to apps built for Canva for your platform using the Canva REST APIs. Canva has developed these guidelines to ensure all our shared users receive the same delightful experience.

## General practices

Things to keep in mind while creating your app.

### Define clear goals and objectives

Before you start building your app, it's crucial to define clear goals and objectives. Identify clear use cases for your business to integrate with Canva and identify what data will be exchanged.

### Apps must be familiar extensions of Canva

The experience of your app should feel familiar, with the app enhancing usability and not disrupting the workflow. Integrate Canva's features in a contextually relevant way to the user's workflow. Ensure your app adds value and enhances the user experience.

### Apps must be secure

Your app must be a secure web app. Ensure that your app's backend securely handles client information, and don't create apps in environments where it's difficult to securely store credentials, such as a mobile app, desktop app, browser extension, Progressive Web App (with no backend), or Single Page App. Make sure that your app follows the [Security recommendations for the Canva REST APIs](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/).

### Don’t replicate Canva features

Your app should enhance or add to the Canva experience, not replace any integrated products or features. Don’t re-create the Canva editor or the Canva UI.

### Test and monitor your app

Before deploying your app, you must fully test your app's components, data mapping, and workflows. Testing can help identify and resolve issues before they become problems in production.

### Provide efficient error-handling

Develop a comprehensive error-handling system that gracefully informs users of what went wrong and why. Don't confront or confuse the user with low-level system error messages. Provide guidance on troubleshooting common errors and known issues, including any relevant error codes or explanations.

### Maintain performance

Maintain good system responsiveness for various user interactions, because poor performance can lead to a negative user experience.

### Troubleshooting and support

Create a section dedicated to troubleshooting common issues that might occur during the integration process. Provide a list of frequently-asked questions (FAQs) and their solutions. Include contact information for support resources, such as customer support or community forums.

## User experience (UX) practices

See [User experience guidelines](https://www.canva.dev/docs/apps/rest-apis/experience-guidelines/).
