---
url: https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/
title: Request credentials - General information - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.115587+00:00
---

# Request credentials - General information - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/

General information

[Evaluating Canva](https://www.canva.dev/docs/print-partnerships/concepts/evaluating-canva/)[Authentication](https://www.canva.dev/docs/print-partnerships/concepts/authentication/)[Credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/)[Request credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/request-credentials/)[Product catalog](https://www.canva.dev/docs/print-partnerships/concepts/product-catalog/)[Proofing](https://www.canva.dev/docs/print-partnerships/concepts/proofing/)[Security](https://www.canva.dev/docs/print-partnerships/concepts/security/)[User journey](https://www.canva.dev/docs/print-partnerships/concepts/user-journey/)

# Request credentials

Copy page

To set up a Print Partnership integration, partners need [credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#list-of-credentials) from Canva.

For security reasons, Canva sends these credentials via encrypted files. Canva creates the encrypted files using a public key that partners provide. Partners then decrypt the files using their private key.

This guide explains how to request credentials from Canva.

If you're [rotating an integration's credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#rotate-credentials), back up the existing credentials before requesting new ones.

## Prerequisites

Partners need:

  * A tool to generate a public key and a private key. We recommend `ssh-keygen`, as it's installed on most major operating systems by default. To learn more, visit [openssh.com⁠(opens in a new tab or window)](https://www.openssh.com/).
  * A tool to decrypt Canva's encrypted files that contain the credentials. We recommend `openssl`. To learn more, visit [openssl.com⁠(opens in a new tab or window)](https://www.openssl.org/).



## Step 1: Generate a key pair

Partners must generate:

  * A public key, which Canva can use to create encrypted files with the [credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#list-of-credentials).
  * A private key, which partners can use to decrypt Canva's encrypted files.



To generate the keys:

  1. Run the following command.
         
         ssh-keygen -t rsa -C "<email address>" -m pem

BASH

Copy

Replace `<email_address>` with your email address.

  2. When prompted for a file name and passphrase, accept the default values.




By default, `ssh-keygen` creates the following files:

  * `~/.ssh/id_rsa`, which contains the private key.
  * `~/.ssh/id_rsa.pub`, which contains the public key.



To change the file location, pass the `-f` argument with a file path. The path must end with a file name. For example, `ssh-keygen -t rsa -C "smith@example.com" -m pem -f ~/credentials/keys`.

## Step 2: Provide the public key to Canva

Canva uses the public key to create two encrypted files with the [credentials](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#list-of-credentials) encoded. One file is for the production environment, the other is for the test environment.

To provide the public key to Canva:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **API Keys Request**.
  3. Copy the public key into the **Public RSA Key** field.
  4. In the **Domains** field, provide a list of domains where you intend to deploy and test the integration. Canva will add them to the [allowlist](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#domain-restrictions).



## Step 3: Download Canva's encrypted files

After receiving your public key, Canva:

  * Generates the encrypted files containing the integration's credentials.
  * Attaches the files to the support ticket.



You'll receive an email notification when the files are available to download.

Download the encrypted files.

## Step 4: Decrypt Canva's encrypted files

To decrypt the files:

  1. Run the following command:
         
         openssl rsautl -decrypt -inkey <private_key_file_path> -in <encrypted_file_path> -out <output_file_path>

BASH

Copy

Replace the placeholders with these values:

     * `<private_key_file_path>` \- The file path of the private key.
     * `<encrypted_file_path>` \- The file path of an encrypted file received from Canva.
     * `<output_file_path>` \- The file path to output the decrypted credentials.

For example:
    
    openssl rsautl -decrypt -inkey ~/.ssh/id_ed25519 -in ~/credentials/canva-partner-prod -out ~/credentials/canva-api-keys

BASH

Copy

  2. Update the integration to use the credentials.



