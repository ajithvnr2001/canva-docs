---
url: https://www.canva.dev/docs/audit-logs/setup/
title: Set up Canva audit logs - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:56.385630+00:00
---

# Set up Canva audit logs - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/setup/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Set up Canva audit logs

How to set up an AWS S3 bucket for Canva audit logs.

Copy page

Canva stores audit log data in an [Amazon S3 bucket⁠(opens in a new tab or window)](https://aws.amazon.com/s3/) that your organization owns and manages. We add events to your S3 bucket every minute as a gzipped archive containing [JSONL⁠(opens in a new tab or window)](https://jsonlines.org/) content. We store the files in hourly folders, in the format `orgId/yyyy/MM/dd/HH`. To let Canva send audit logs to your S3 bucket, Canva requires [`PutObject` permission⁠(opens in a new tab or window)](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) on the S3 bucket.

To start receiving audit logs, you need to:

  1. [Open the Canva Audit logs configuration page](https://www.canva.dev/docs/audit-logs/setup/#open-the-canva-audit-logs-configuration-page).
  2. [Create an Amazon S3 bucket](https://www.canva.dev/docs/audit-logs/setup/#create-an-s3-bucket).
  3. [Grant Canva access to the S3 bucket](https://www.canva.dev/docs/audit-logs/setup/#grant-canva-access-to-the-s3-bucket).
  4. [Save the S3 bucket details to your Canva account](https://www.canva.dev/docs/audit-logs/setup/#save-the-s3-bucket-details-to-your-canva-account).



This article walks you through creating the required AWS resources and adding their details to your Canva account.

## Open the Canva Audit logs configuration page

To make the process easier, we recommend you access the [Canva Audit logs page⁠(opens in a new tab or window)](https://www.canva.com/settings/audit-logs) before creating the AWS resources. This will let you input the required data during each step of the setup process. To access the Canva Audit logs settings:

  1. From the Canva homepage, go to **Settings**

  2. Under **Organization settings** , select **Audit logs**.

  3. Scroll down to the section **AWS S3 bucket and role configuration**.

![Screenshot of the form in the AWS S3 bucket and role configuration section of the audit logs settings page](https://www.canva.dev/_next/static/media/audit-logs-configuration-settings.1a80ea6e.png)

The AWS S3 bucket and role configuration section of the audit logs settings page.




## Create an S3 bucket

To create an Amazon S3 Bucket for Canva audit logs:

  1. In a new tab or window, sign into the [AWS Management Console⁠(opens in a new tab or window)](https://aws.amazon.com/console/).

  2. Open the [S3 console⁠(opens in a new tab or window)](https://console.aws.amazon.com/s3/).

  3. Select **Create bucket**.

  4. Under **General configuration** :

     1. If prompted, choose your preferred **AWS Region**.

     2. If prompted to select a **Bucket type** , select **General purpose**.

     3. Enter a **Bucket name** (for example: `canva-audit-logs`).

     4. Update the [Canva **Audit logs** settings page⁠(opens in a new tab or window)](https://www.canva.com/settings/audit-logs):

        * Select the **Region** of the S3 bucket.
        * Copy the S3 bucket name into the **S3 bucket name** field.
  5. Under **Object Ownership** , select **ACLs disabled (recommended)**.

  6. Under **Block Public Access settings for this bucket** , select **Block _all_ public access**.

  7. Under **Default encryption** , configure the default encryption for the S3 bucket. If you select an option using _AWS Key Management Service (KMS)_ , choose or enter an **AWS KMS key**.

  8. _(Optional)_ Update the remaining settings as desired or leave the default values.

  9. Click **Create bucket**.




If successful, you'll return to the S3 **Buckets** page with a banner confirming the creation of the bucket.

Make a note of the S3 bucket name. You'll need it when you [grant Canva access to the S3 bucket](https://www.canva.dev/docs/audit-logs/setup/#grant-canva-access-to-the-s3-bucket).

## Grant Canva access to the S3 bucket

Access to AWS services is managed through AWS Identity and Access Management (IAM). For audit logs, we only support IAM [Role-based access⁠(opens in a new tab or window)](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles).

You'll need to create a policy, then assign that policy to a role with limited access.

### Create a policy using the AWS IAM console

  1. Open the [IAM console⁠(opens in a new tab or window)](https://console.aws.amazon.com/iam/).
  2. In the navigation pane, under **Access management** , select **Policies**.
  3. On the **Policies** page, select **Create policy**.
  4. On the **Specify permissions** page, you need to provide a permissions policy. The type of encryption [your S3 bucket](https://www.canva.dev/docs/audit-logs/setup/#create-an-s3-bucket) uses (_SSE-S3_ , _SSE-KMS_ , or _DSSE-KMS_) determines which policy you need:



SSE-S3SSE-S3

SSE-KMS or DSSE-KMSSSE-KMS or DSSE-KMS

  1. Change the **Policy editor** from **Visual** to **JSON**.

![The specify permissions page with the visual to JSON switch on the policy editor highlighted](https://www.canva.dev/_next/static/media/switch-to-json-editor.95667c63.png)
  2. Replace the contents of the **Policy editor** with the following policy:
         
         {
         
           "Version": "2012-10-17",
         
           "Statement": [
         
             {
         
               "Effect": "Allow",
         
               "Action": ["s3:PutObject"],
         
               "Resource": "arn:aws:s3:::<audit-logs-s3-bucket-name>/*"
         
             }
         
           ]
         
         }

JSON

Copy

  3. Replace `<audit-logs-s3-bucket-name>` with the name of the AWS S3 Bucket.

For example, if you named the bucket `canva-audit-logs`, the **Resource** value would be `arn:aws:s3:::canva-audit-logs/*`.

![The AWS IAM's Create policy page, step 1 specify permissions. Shows the JSON Policy editor with the policy pasted in and the S3 Bucket in the 'Resource' is changed to canva-audit-logs](https://www.canva.dev/_next/static/media/create-policy.08754c55.png)
  4. Click **Next**.

  5. On the **Review and create** page:

     1. Enter a **Policy Name** (such as: `canva-audit-logs-s3-upload`).

     2. Make sure the policy in **Permissions defined in this policy** has the correct S3 bucket name. If not, return to the **Specify permissions** page and update the policy.

     3. _(Optional)_ Update **Tags** and **Description** ; or leave them empty.

![The IAM Review and create page, with a policy name input and the other elements unchanged](https://www.canva.dev/_next/static/media/review-and-create-policy.2ab9df04.png)
     4. Click **Create policy**.




  1. Change the **Policy editor** from **Visual** to **JSON**.

![The specify permissions page with the visual to JSON switch on the policy editor highlighted](https://www.canva.dev/_next/static/media/switch-to-json-editor.95667c63.png)
  2. Replace the contents of the **Policy editor** with the following policy:
         
         {
         
           "Version": "2012-10-17",
         
           "Statement": [
         
             {
         
               "Effect": "Allow",
         
               "Action": ["s3:PutObject"],
         
               "Resource": "arn:aws:s3:::<audit-logs-s3-bucket-name>/*"
         
             },
         
             {
         
               "Action": "kms:GenerateDataKey",
         
               "Effect": "Allow",
         
               "Resource": "<kms-bucket-encryption-key-arn>"
         
             }
         
           ]
         
         }

JSON

Copy

  3. Replace `<audit-logs-s3-bucket-name>` with the name of the AWS S3 Bucket.

For example, if you named the bucket `canva-audit-logs`, the **Resource** value would be `arn:aws:s3:::canva-audit-logs/*`.

![The AWS IAM's Create policy page, step 1 specify permissions. Shows the JSON Policy editor with the policy pasted in and the S3 Bucket in the 'Resource' is changed to canva-audit-logs](https://www.canva.dev/_next/static/media/create-policy.08754c55.png)
  4. Replace `<kms-bucket-encryption-key-arn>` with the KMS key ARN using the format `arn:aws:kms:{Region}:{Account}:key/{KeyId}`.

  5. Click **Next**.

  6. On the **Review and create** page:

     1. Enter a **Policy Name** (such as: `canva-audit-logs-s3-upload`).

     2. Make sure the policy in **Permissions defined in this policy** has the correct S3 bucket name. If not, return to the **Specify permissions** page and update the policy.

     3. _(Optional)_ Update **Tags** and **Description** ; or leave them empty.

![The IAM Review and create page, with a policy name input and the other elements unchanged](https://www.canva.dev/_next/static/media/review-and-create-policy.2ab9df04.png)
     4. Click **Create policy**.




If successful, you'll return to the IAM **Policies** page with a banner confirming the creation of the policy.

### Create a role using the AWS IAM console

  1. Open the [IAM console⁠(opens in a new tab or window)](https://console.aws.amazon.com/iam/).

  2. In the navigation pane, under **Access management** , select **Roles**.

  3. On the **Roles page** , select **Create role**.

  4. On the **Select trusted entity** page, under **Trusted entity type** , select **Custom trust policy**.

  5. In another browser tab or window, visit the Canva Audit logs settings page to get the policy:

     1. From the Canva homepage, go to **Settings**.

     2. Under **Organization settings** , select **Audit logs**.

     3. Under **Grant access to Amazon Web Services (AWS)** , copy the **Trust policy**.

The Trust policy on the **Audit logs** page is specific to your organization.

  6. Return to the AWS IAM **Select trusted entity** page and paste policy into the **Custom trust policy** editor.

![The custom trust policy editor with the JSON-based Trust policy pasted in](https://www.canva.dev/_next/static/media/select-trusted-entitiy.dd9ce162.png)
  7. Click **Next**.

  8. On the **Add permissions** page, select [the policy you created](https://www.canva.dev/docs/audit-logs/setup/#create-a-policy-using-the-aws-iam-console) (for example: `canva-audit-logs-s3-upload`).

  9. Click **Next**.

  10. Enter a **Role name** (such as: `canva-audit-logs-s3-upload-role`).

  11. _(Optional)_ Update **Description** and **Tags** , or leave them empty.

  12. Review **Step 1: Select trusted entities** and **Step 2: Add permissions** , making sure that the information is correct.

  13. Click **Create Role**.




If successful, you'll return to the IAM **Roles** page with a banner confirming the creation of the role.

#### Get the AWS role ARN

To get the AWS role ARN:

  1. On the IAM **Roles** page, find the role you created.
  2. Click the (hyperlinked) name of the role to view details about the role.
  3. Under **Summary** , copy the **ARN**.
  4. Return the [Canva **Audit logs** settings page⁠(opens in a new tab or window)](https://www.canva.com/settings/audit-logs) and paste the ARN into **AWS role ARN**.



## Save the S3 bucket details to your Canva account

To save the details of the S3 bucket and IAM Role and start audit logging:

  1. Return to the Canva **Audit logs** page.

  2. In the section **AWS S3 bucket and role configuration** , add or check the following details:

     * **Region** : The region of the AWS S3 bucket. For example: _US East (N.Virginia)_. For a list of AWS regions, visit [AWS Documentation — Amazon Simple Storage Service endpoints and quotas⁠(opens in a new tab or window)](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_region).
     * **AWS role ARN** : The Amazon Resource Name [ARN⁠(opens in a new tab or window)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) of the AWS Role Canva will use to access the S3 bucket. For example: `arn:aws:iam:region:account-id:resource-id`.
     * **S3 bucket name** : The name of your Canva audit logs S3 bucket. For example: `my-canva-audit-logs-bucket`.
     * **S3 key prefix** : An optional [S3 key prefix⁠(opens in a new tab or window)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html). For example: `bucket/canva/auditlogs`.
  3. Click **Save**.




If successful, you'll receive and on-screen notification: **AWS S3 bucket and role configuration saved.** If your users are actively using Canva, audit logs will begin arriving in your S3 bucket within a few minutes.

## Disconnect from your S3 bucket

You can disconnect your S3 bucket at any time to stop Canva from sending new audit logs. Disconnecting removes the S3 bucket and role configuration from your Canva account but doesn't affect logs that Canva has already delivered to your bucket.

To disconnect your S3 bucket:

  1. Return to the Canva **Audit logs** page.

  2. Scroll down to the section **AWS S3 bucket and role configuration**.

  3. Select **Disconnect**.

  4. In the **Disconnect S3 bucket?** dialog, select **Disconnect** to confirm.

![The Disconnect S3 bucket confirmation dialog, with Cancel and Disconnect buttons](https://www.canva.dev/_next/static/media/disconnect-s3-bucket.e1322a8e.png)

The confirmation dialog shown when disconnecting your S3 bucket.




Once disconnected, Canva stops sending new audit logs to your S3 bucket. To start receiving audit logs again, repeat the steps to [save the S3 bucket details to your Canva account](https://www.canva.dev/docs/audit-logs/setup/#save-the-s3-bucket-details-to-your-canva-account).
