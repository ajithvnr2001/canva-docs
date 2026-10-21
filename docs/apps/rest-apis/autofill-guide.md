---
url: https://www.canva.dev/docs/apps/rest-apis/autofill-guide/
title: Autofill designs with data - Canva for your platform - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:14.254852+00:00
---

# Autofill designs with data - Canva for your platform - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/rest-apis/autofill-guide/

Canva for your platform

[About Canva's REST APIs](https://www.canva.dev/docs/apps/rest-apis/)

Fundamentals

[API requests and responses](https://www.canva.dev/docs/apps/rest-apis/requests-responses/)[Authentication](https://www.canva.dev/docs/apps/rest-apis/authentication/)[Capabilities](https://www.canva.dev/docs/apps/rest-apis/capabilities/)[API versions](https://www.canva.dev/docs/apps/rest-apis/versions/)

Development guides

[Autofill designs with data](https://www.canva.dev/docs/apps/rest-apis/autofill-guide/)[Return users to your platform](https://www.canva.dev/docs/apps/rest-apis/return-navigation-guide/)

Design guidelines

[User experience guidelines](https://www.canva.dev/docs/apps/rest-apis/experience-guidelines/)[UI guidelines](https://www.canva.dev/docs/apps/rest-apis/ui-guidelines/)[Brand guidelines](https://www.canva.dev/docs/apps/rest-apis/brand-guidelines/)

# Autofill designs with data

How to generate dynamic designs using brand templates, designs, and the Autofill APIs.

Copy page

Autofill and brand templates are available to users on Canva Pro (including Canva Education and Canva for Nonprofits), Canva Teams, or Canva Enterprise. **Usage limits will be introduced in the future.** Autofill can be used with designs or brand templates.

This guide demonstrates how you can autofill brand templates with your own data to generate dynamic designs in Canva, using the Canva REST APIs.

The following example generates a design based on variables from a custom data source. A city name and weather information from a dataset is sent to the API in a request, and then the supplied information is applied to a template to create a new design.

![autofill workflow example](https://www.canva.dev/_next/static/media/autofill-workflow.cd8fbd99.png)

## Prerequisites

### Create a Canva account

To start building your app you'll need to create a Canva account. Your account must:

  * Have [Multi-factor Authentication (MFA)⁠(opens in a new tab or window)](https://www.canva.com/help/login-verification/) enabled.
  * Be on a Canva plan that includes Autofill, such as Canva Pro, Canva Teams, or Canva Enterprise.



### Create an app

  1. If you haven't already created an app, follow the steps in [Quickstart](https://www.canva.dev/docs/apps/quickstart/) to create an app and enable the REST APIs on it.

  2. In the Developer Portal, go to **Outside Canva > Configuration**, then under **Scopes** enable the following:

     * **design:content** : Read and Write
     * **design:meta** : Read
     * **brandtemplate:meta** : Read
     * **brandtemplate:content** : Read
     * **asset** : Read and Write



After creating your app, you should have the following details for your app:

  * Your Client ID.
  * Your Client secret.
  * A list of your app's scopes.
  * At least one authorization redirect URL.



## Create an autofillable template

For this guide, we'll use a pre-built template. If you would like to create your own, tag the elements you want to fill as data fields: in the Canva editor, search for **Bulk Create** under **Apps** in the side panel, select **Labels** , then select an element and add a **Data field**. For details, read the Canva Help Center articles on [using brand templates⁠(opens in a new tab or window)](https://www.canva.com/help/using-brand-templates/) and [setting up Autofill⁠(opens in a new tab or window)](https://www.canva.com/help/autofill/).

  1. Open the pre-built template below.

[Open template in Canva(opens in a new tab or window)](https://canva.link/onzr85gkx1gv2bb)

The pre-built template contains three data fields:

     * Two text fields named `CITY` and `TEMPERATURE`.
     * One image field named `BACKGROUND`.
  2. [Publish your design as a brand template⁠(opens in a new tab or window)](https://www.canva.com/help/publish-team-template/#publish-brand-templates) and note the brand template ID. Locate the brand template ID by examining the URL of your _published_ brand template. For example, in the URL `https://www.canva.com/brand/brand-templates/AEN3TrQftXo` the brand template ID is the `AEN3TrQftXo` string at the end of the URL.

You can save this ID now for use in the next steps, or retrieve it later using the [List brand templates API](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/list-brand-templates/).




## Authenticate with OAuth

  1. Follow the [Authentication guide](https://www.canva.dev/docs/apps/rest-apis/authentication/) to get an authorization code, then generate an access token for your requests. For this process you need:

     * Your Client ID.
     * Your Client secret.
     * A URL-encoded list of your app's scopes.
     * One of your nominated redirect URLs.
  2. (Optional) If you've already authenticated but your token has expired, you can skip step 1 and [request a new token using your refresh token](https://www.canva.dev/docs/apps/rest-apis/reference/authentication/generate-access-token/).




When you've successfully authenticated and obtained a bearer token, you're ready to upload your assets and generate your autofilled design.

## Preparing assets for autofill

All media used in autofill must first be uploaded to the asset library. We'll upload an asset for the `BACKGROUND` field before creating the autofill job.

### Step 1. Upload your asset

We'll use the [Create asset upload job API](https://www.canva.dev/docs/apps/rest-apis/reference/assets/create-asset-upload-job/) to create an [asynchronous asset upload job](https://www.canva.dev/docs/apps/rest-apis/requests-responses/#asynchronous-job-endpoints).

  1. Upload your image with a call to `POST /asset-uploads`.
         
         curl --request POST 'https://api.canva.com/rest/v1/asset-uploads' \
         
           --header 'Authorization: Bearer {TOKEN}' \
         
           --header 'Content-Type: application/octet-stream' \
         
           --header 'Asset-Upload-Metadata: { "name_base64": "YmFja2dyb3VuZC5qcGc=" }' \
         
           --data-binary '@/path/to/your/image.jpg'

SHELL

Copy

The `Asset-Upload-Metadata` header requires the asset name encoded in Base64. For example, "background.jpg" encoded in Base64 is `YmFja2dyb3VuZC5qcGc=`.

  2. The endpoint returns an upload job with its ID and status.
         
         {
         
           "job": {
         
             "id": "e08861ae-3b29-45db-8dc1-1fe0bf7f1cc8",
         
             "status": "in_progress"
         
           }
         
         }

JSON

Copy

Save the job ID so you can retrieve your asset ID when the job is complete.




### Step 2. Get your asset upload job

With the job ID from the previous step, use the [Get asset upload job API](https://www.canva.dev/docs/apps/rest-apis/reference/assets/get-asset-upload-job/) to periodically poll the status of the job until the asset is ready.

  1. Call `GET /asset-uploads/{JOB-ID}`.
         
         curl --request GET \
         
           --url https://api.canva.com/rest/v1/asset-uploads/{JOB-ID} \
         
           --header 'Authorization: Bearer {TOKEN}'

SHELL

Copy

  2. The endpoint returns the job's status. A successfully completed job has the status `success` and includes the asset details in the response.
         
         {
         
           "job": {
         
             "id": "e08861ae-3b29-45db-8dc1-1fe0bf7f1cc8",
         
             "status": "success",
         
             "asset": {
         
               "id": "Msd59349ff",
         
               "type": "image",
         
               "name": "background.jpg"
         
             }
         
           }
         
         }

JSON

Copy

Save the `asset.id` value so you can include it in your autofill job request.




### Limitations

There are some limitations to what assets can be used for autofill:

Image and video data fields accept uploaded assets only, referenced by `asset_id`. External image URLs can't be passed directly to these fields.

External image URLs can be uploaded as assets using the [Create asset upload job via URL](https://www.canva.dev/docs/apps/rest-apis/reference/assets/create-url-asset-upload-job/).

Sheet data fields can include media cells that reference an external image or video URL directly.

## Generate an autofilled design

The process of generating an autofilled design involves querying your brand template's dataset, creating an autofill job with your data, and retrieving the generated design.

This guide uses the `create_from_brand_template` API mode, where we start from a brand template with tagged fields and create a new design by filling the tagged fields with provided content. The API also supports the following modes:

  * `create_from_design`: Starts with an existing design with tagged fields. Pass in `design_id` (instead of `brand_template_id` like in the example) to create a new design, filling the tagged fields with provided content.
  * `update_design`: Starts with an existing design with tagged fields. Pass in `design_id` (instead of `brand_template_id` like in the example), filling the tagged fields with provided content **without creating a new design**.



![Workflow for using the Autofill API to generate a design](https://www.canva.dev/_next/static/media/api-create-flow.63cb328c.png)

### Step 0. (Optional) Get a list of all brand templates

If you don't know your brand template's ID, you can get a [list of all brand templates](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/list-brand-templates/).

### Step 1. Query your brand template

Use the [Get brand template dataset API](https://www.canva.dev/docs/apps/rest-apis/reference/brand-templates/get-brand-template-dataset/) to query your brand template's dataset and get a list of autofillable fields. If you're starting from a tagged design instead, use the [Get design dataset API](https://www.canva.dev/docs/apps/rest-apis/reference/designs/get-design-dataset/).

  1. Request your template's dataset with a call to `GET /brand-templates/{TEMPLATE-ID}/dataset`.
         
         curl --request GET \
         
           --url https://api.canva.com/rest/v1/brand-templates/{TEMPLATE-ID}/dataset \
         
           --header 'Authorization: Bearer {TOKEN}'

SHELL

Copy

  2. The endpoint returns the available fields and their data type in the `dataset` object.
         
         {
         
           "dataset": {
         
             "CITY": {
         
               "type": "text"
         
             },
         
             "TEMPERATURE": {
         
               "type": "text"
         
             },
         
             "BACKGROUND": {
         
               "type": "image"
         
             }
         
           }
         
         }

JSON

Copy




### Step 2. Create a design autofill job

Use the [Create design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/create-design-autofill-job/) to create your new design, with your autofill data in the body of the request. This API creates an [asynchronous job](https://www.canva.dev/docs/apps/rest-apis/requests-responses/#asynchronous-job-endpoints) to generate the design.

You don't have to fill every available field. If you omit a field, Canva uses the default value from your template when generating your final design.

  1. Initiate your job with a call to `POST /autofills`.
         
         curl --request POST \
         
         --url https://api.canva.com/rest/v1/autofills \
         
         --header 'Authorization: Bearer {TOKEN}' \
         
         --header 'Content-Type: application/json' \
         
         --data '{
         
           "brand_template_id": "{TEMPLATE-ID}",
         
           "data": {
         
             "CITY": {
         
               "type": "text",
         
               "text": "Sydney"
         
             },
         
             "TEMPERATURE": {
         
               "type": "text",
         
               "text": "25C"
         
             },
         
             "BACKGROUND": {
         
               "type": "image",
         
               "asset_id": "{ASSET-ID}"
         
             }
         
           }
         
         }'

SHELL

Copy

  2. The endpoint returns an autofill job with its ID and status.
         
         {
         
           "job": {
         
             "id": "a71ef223-571c-48a2-9572-e6cf85e3b943",
         
             "status": "in_progress"
         
           }
         
         }

JSON

Copy

Save the ID so you can retrieve your design when the job is complete.




### Step 3. Get your design autofill job

Asynchronous jobs might take some time to complete. With the job ID from the previous step, use the [Get design autofill job API](https://www.canva.dev/docs/apps/rest-apis/reference/autofills/get-design-autofill-job/) to periodically poll the status of the job until the design is ready.

  1. Call `GET /autofills/{JOB-ID}`.
         
         curl --request GET \
         
         --url https://api.canva.com/rest/v1/autofills/a71ef223-571c-48a2-9572-e6cf85e3b943 \
         
         --header 'Authorization: Bearer {TOKEN}'

SHELL

Copy

  2. The endpoint returns the job's status. A successfully completed job has the status `success` and includes the design details in the response.
         
         {
         
           "job": {
         
             "id": "{ID}",
         
             "status": "success",
         
             "result": {
         
               "type": "create_design",
         
               "design": {
         
                 "url": "https://www.canva.com/design/{DESIGN-ID}/edit",
         
                 "thumbnail": {
         
                   "url": "https://export-download.canva.com/{THUMBNAIL-RESOURCE}"
         
                 }
         
               }
         
             }
         
           }
         
         }

JSON

Copy

Direct your user to the design's URL so they can open it in the Canva editor and adjust or export it as required.

![Generated design](https://www.canva.dev/_next/static/media/generated-design.423c3de5.png)




## Next steps

Once the autofill job is complete and you have the final design, you can use the REST APIs to automate further steps in your workflow:

  * Export the design in your preferred format using [Create design export job](https://www.canva.dev/docs/apps/rest-apis/reference/exports/create-design-export-job/).
  * Move the design to a designated folder using [Move folder item](https://www.canva.dev/docs/apps/rest-apis/reference/folders/move-folder-item/).


