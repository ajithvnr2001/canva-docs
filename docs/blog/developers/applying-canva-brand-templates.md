---
url: https://www.canva.dev/blog/developers/applying-canva-brand-templates/
title: Apply Canva Brand templates with the Autofill API - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:03.260552+00:00
---

# Apply Canva Brand templates with the Autofill API - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/applying-canva-brand-templates/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

connect API

# Apply Canva Brand templates with the Autofill API

How to identify and consistently apply Canva Brand Templates using the Brand template API and Autofill API.

![](https://www.canva.dev/_next/static/media/thumbnail.1b60cf41.jpg)

* * *

  *   * 


Timo Bingaman, Joe RobinsonOct 9, 2024

* * *

Protecting brand integrity means sometimes defending a brand fiercely, and always applying the brand design consistently. If your project or web app can’t provide your customers a consistent way to find and apply brand templates, you risk spending time catching up on repeated request for a brand template feature. Canva Connect API provides the solution, giving your customers consistency in how they:

  * Access and apply Canva Brand Templates.
  * Automatically fill out new designs from templates.



This guide shows you how to build an example integration using the Brand template and Autofill APIs to access Canva Brand Templates and apply them consistently to a design. These APIs let your web app apply a Canva Brand Template to a Canva design entirely within your integration. Your customers won’t need to use the Canva editor to edit their design manually.

You can try out the APIs right now:

  * [From the docs page](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/#try-it-out) (be aware this sends API requests to your Canva account's live data).
  * [Using the Canva Connect API Starter Kit](https://www.canva.dev/docs/apps/quickstart/), which provides a working e-commerce web app showcasing the API's features.



When you're ready to use the Autofill API for your own applications, see the [Autofill guide](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/). It explains how to create a Canva Brand Template and apply it to a new design automatically.

## Before you begin

Before applying a brand template, you need:

  * **A Canva account** : With multi-factor authentication enabled.
  * **An[integration in your account](https://www.canva.dev/docs/connect/creating-integrations/)**: To connect your application to Canva, prepare for authorization, and configure API scopes.
  * **A Canva Brand Template with data fields** : Brand templates are available on Canva Pro, Canva Teams, and Canva Enterprise. To tag elements as data fields, open **Bulk Create** under **Apps** in the editor and select **Labels**. For details, see [Set up your designs for Autofill⁠(opens in a new tab or window)](https://www.canva.com/help/autofill/).
  * **An access token** : To [create a token](https://www.canva.dev/docs/connect/creating-integrations/): 
    1. Create [an authorization URL](https://www.canva.dev/docs/connect/authentication/#create-the-authorization-url) to get an authorization code.
    2. [Generate an access token](https://www.canva.dev/docs/connect/authentication/#generate-access-tokens) using a [request to the Authentication API](https://www.canva.dev/docs/connect/api-reference/authentication/generate-access-token/).
  * **Tools** : 
    * Text editor
    * Command-line shell with the [Node.js CLI⁠(opens in a new tab or window)](https://nodejs.org/api/cli.html) (version 18 or higher) installed.



When you have your access token ready, you can use it to test out the Brand template and Autofill APIs.

Access tokens have a limited lifespan. When your current token expires, use the refresh token to request a new access token.

## Configure API scopes

Scopes let you specify what actions your integration can perform on behalf of the end user. To grant Brand template and Autofill APIs access to your integration, go to **Outside Canva > Configuration** in the Developer Portal and set the following scope permissions under **Scopes** :

  * `design:content:write`
  * `design:content:read`
  * `brandtemplate:content:read`
  * `brandtemplate:meta:read`
  * `asset:read` and `asset:write` (needed if your template has image or video fields).



## Step 1. Collect and view brand templates

The example in the following steps uses JavaScript and the `node` command to make an API call, collect your Canva Brand Templates, and display the response returned by the Canva API in the console. The logged output can give you an idea of what parameters you can parse and display when building your integration.

To collect your Canva Brand Template and view the API response:

  1. Create a new JavaScript file named `brandTemplate.js` and add the following.
         
         module.exports.init = function () {
         
             fetch("https://api.canva.com/rest/v1/brand-templates?dataset=non_empty", {
         
                 method: "GET",
         
                 headers: {
         
                    "Authorization": "Bearer <Add your Access Token Here>",
         
                 },
         
               })
         
                 .then(async (response) => {
         
                   const data = await response.json();
         
                   console.log(data);
         
                 })
         
                 .catch(err => console.error(err));
         
             }

JS

Copy

Use the `dataset=non_empty` [query parameter](https://www.canva.dev/docs/connect/api-reference/brand-templates/list-brand-templates/#query-parameters) to filter and return only Canva Brand Templates that have a dataset.

  2. Run the following `node` command to make your API request.
         
         node -e 'require("./brandTemplate.js").init()'

SHELL

Copy

The API response returns a list of available Canva Brand Templates, as well as other important response parameters, as shown in the following example.
         
         {
         
           continuation: '<token-value>',
         
           items: [
         
             {
         
               id: '<id-value>',
         
               title: 'Limited Presentation',
         
               view_url: 'https://www.canva.com/design/<id-value>/view',
         
               create_url: 'https://www.canva.com/design/<id-value>/remix',
         
               thumbnail: [Object],
         
               created_at: 1701760702,
         
               updated_at: 1715904777
         
             },

JSON

Copy




If customers have more Canva Brand Templates than the response's pagination parameters can handle, the response returns a [`continuation` token](https://www.canva.dev/docs/connect/api-reference/brand-templates/list-brand-templates/#success-response). Use this token in your integration as a query parameter to request the next set of results.

The Brand Template API returns the Canva Brand Template ID, which you need to apply templates consistently. The next step uses this ID to retrieve the information you need about each template so you can apply it to a design.

## Step 2. Collect a brand template dataset

To collect information about a specific brand template, including the dataset for applying the template to a design:

  1. Create a new JavaScript file named `getBrandTemplate.js` and add the following code.
         
         module.exports.init = function () {
         
             fetch("https://api.canva.com/rest/v1/brand-templates/<add your Canva Brand Template ID here>/dataset", {
         
                 method: "GET",
         
                 headers: {
         
                   "Authorization": "Bearer <Add your access token here>",
         
                 },
         
               })
         
                 .then(async (response) => {
         
                   const data = await response.json();
         
                   console.log(data);
         
                 })
         
                 .catch(err => console.error(err));
         
             }

JS

Copy

  2. Run the following `node` command to make the API request.
         
         node -e 'require("./getBrandTemplate.js").init()'

SHELL

Copy

A successful response returns the requested Canva Brand Template's dataset, including the data fields you can change when creating a new design from the template.

If you receive the following error when testing your web application, check your integration has the correct permissions to access the brand template.
         
         {
         
           code: 'permission_denied',
         
           message: 'Not allowed to get brand template with ID <ID-value>'
         
         }

JSON

Copy




## Step 3. Apply the brand template using the Autofill API

To apply the brand template using the Autofill API:

  1. Create a new file called `autofillBrand.js` and add the following code.
         
         module.exports.init = function () {
         
             fetch("https://api.canva.com/rest/v1/autofills", {
         
                 method: "POST",
         
                 headers: {
         
                   "Authorization": "Bearer <Add your Access Token Here>",
         
                   "Content-Type": "application/json"
         
                 },
         
                 body: JSON.stringify({
         
                     "brand_template_id": "<Add your Canva Brand Template ID here>",
         
                     "title": "string",
         
                     "data": {
         
                       "title": {
         
                         "type": "text",
         
                         "text": "Brand template autofill completed"
         
                       }
         
                     }
         
                   }),
         
               })
         
                 .then(async (response) => {
         
                   const data = await response.json();
         
                   console.log(data);
         
                 })
         
                 .catch(err => console.error(err));
         
             }

JS

Copy

This request initiates an asynchronous design autofill job based on the included Canva Brand Template data and ID. If successful, it creates a new design based on the template.

  2. Run the following `node` command to send the `POST` request and check for a response.
         
         node -e 'require("./autofillBrand.js").init()'

SHELL

Copy
         
         {
         
           "job": {
         
             "id": "<design autofill job id value>",
         
             "status": "in_progress"
         
           }
         
         }

JSON

Copy




A successful response means the design autofill job has started and is in progress, as indicated by the `status`. In the [next step](https://www.canva.dev/blog/developers/applying-canva-brand-templates/#step-4-query-autofill-job-status), use the Autofill job ID (`job.id`) to check on the status of the new design.

### Troubleshoot the asset ID
    
    
    {
    
     "code": "invalid_field",
    
      "message": "'asset_id' must not be null."
    
    }

JSON

Copy

If the response returns this error, your Canva Brand Template has an image data field, so you must supply a Canva asset ID in the Autofill API body section. You can use the [Assets Canva API endpoint⁠(opens in a new tab or window)](https://www.canva.dev/docs/connect/api-reference/assets/) to provide customers with the ability to upload their image assets. The Assets API can help you access and use uploaded media asset IDs when automatically filling designs from Canva Brand Templates.

## Step 4. Query autofill job status

To check if a new design is successfully created from a Canva Brand Template, you can query the autofill job's status:

  1. Create a new file named `queryAutofill.js` and add the following code.
         
         module.exports.init = function () {
         
             fetch("https://api.canva.com/rest/v1/autofills/<Add your autofill job id value here>", {
         
                 method: "GET",
         
                 headers: {
         
                   "Authorization": "Bearer <Add your Access Token Here>",
         
                 },
         
               })
         
                 .then(async (response) => {
         
                   const data = await response.json();
         
                   console.log(util.inspect(data, { depth: null }));
         
                 }) //util.inspect makes sure the console.log displays the response object in full.
         
                 .catch(err => console.error(err));
         
             }

JS

Copy

  2. Run the following `node` command to query the autofill job.
         
         node -e 'require("./queryAutofill.js").init()'

SHELL

Copy




### Poll autofill job status

Polling the autofill job often, and parsing the response, provides useful information for your web app's user experience.

While the autofill job is running, the [Get design autofill job API](https://www.canva.dev/docs/connect/api-reference/autofills/get-design-autofill-job/) returns the following response.
    
    
    {
    
      "job": {
    
        "id": "<autofill design job id>",
    
        "status": "in_progress"
    
      }
    
    }

JSON

Copy

While the status is `in_progress`, you can provide customers with a loading state, then display a new message when the status changes to `success`. The following side-by-side example shows the `queryAutofill.js` response alongside a response from the same `GET` request directly on the [Autofill API docs page](https://www.canva.dev/docs/connect/api-reference/autofills/get-design-autofill-job/).

![Two images that show near-identical JSON output, one from Canva Docs and the other from the terminal shell. Some of the output is obscured](https://www.canva.dev/_next/static/media/poll-autofill-job-status.860a68ae.jpg)

The successful response includes a link to view the design, which is the `view_url`. You can display this link in your integration to show users how the design looks.

## Apply Canva Brand Templates for consistent designs

Using the Autofill API in your integration helps your customers apply their Canva Brand Templates consistently. They can view exactly what aspects of a design they're able to modify, and know the design follows their branding.

Remember, you can try out the Canva APIs in [the Connect API documentation](https://www.canva.dev/docs/connect/) anytime, and [the Connect API Starter Kit⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-connect-api-starter-kit) is available for a complete demonstration of what you can build.

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.f15531a9.jpg)](https://www.canva.dev/blog/developers/festive-fun-with-shapes-with-fill/)

[ChristmasAdd some Festive Fun to your App with Shapes with FillCreate some Christmas designs with our these shapes](https://www.canva.dev/blog/developers/festive-fun-with-shapes-with-fill/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Dec 8, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.a4fb80d1.jpg)](https://www.canva.dev/blog/developers/helping-your-users-write-better-prompts/)

[AIHelping your users write better promptsLearn how you can lead your users to better write prompts for AI apps.](https://www.canva.dev/blog/developers/helping-your-users-write-better-prompts/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Aug 22, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.7785249e.jpg)](https://www.canva.dev/blog/developers/user-favorite-canva-apps/)

[Apps SDKWhat makes these 3 Canva apps user favorites?Uncover and apply elements that resonate with users.](https://www.canva.dev/blog/developers/user-favorite-canva-apps/)

[Faria Anzum⁠(opens in a new tab or window)](https://www.linkedin.com/in/farianzum)Feb 12, 2025
