---
url: https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/
title: Getting started - Tutorials - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:03.750455+00:00
---

# Getting started - Tutorials - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/

Tutorials

[Getting started](https://www.canva.dev/docs/print-partnerships/tutorial/getting-started/)[Set up a web server](https://www.canva.dev/docs/print-partnerships/tutorial/set-up-web-server/)[Initialize the Partnership SDK](https://www.canva.dev/docs/print-partnerships/tutorial/initialize-partnership-sdk/)[Show the product catalog](https://www.canva.dev/docs/print-partnerships/tutorial/show-product-catalog/)[Calculate an autoAuthToken](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/)[Create a new design](https://www.canva.dev/docs/print-partnerships/tutorial/create-new-design/)[Preview the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/preview-user-artwork/)[Purchase the user's artwork](https://www.canva.dev/docs/print-partnerships/tutorial/purchase-user-artwork/)

# Getting started

Copy page

If you've never setup a Print Partnership integration before, you've come to the right place. This tutorial takes you step-by-step through the entire process. By the end of the tutorial, you'll understand what integrations are, how they work, and how you can get one up and running.

## What you'll build

This tutorial explains how to create a basic Print Partnership integration.

This integration lets users:

  * View a list of products and templates.
  * Open a product or template in the Canva editor.
  * Navigate through a proofing process to prepare their design for printing.
  * Download a PDF preview of their finished artwork.
  * "Purchase" the print-quality artwork. (The word "purchase" is in quotes because this tutorial doesn't explain how to integrate with a payment processor.)



### Disclaimer

This tutorial is not exhaustive. It doesn't talk about a range of important topics, such as security or deployment. This is because print partners usually integrate with existing systems, which a tutorial can't account for (at least not in meaningful detail).

Because of this, the goal of this tutorial is to help you create a simple yet complete integration as quickly as possible. Then you can apply what you've learned to your specific environment.

## Before you begin

This tutorial assumes you have the following credentials:

  * [Partner ID](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-id)
  * [Partner API key](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-key)
  * [Partner API secret](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#partner-api-secret)
  * [Artwork API secret](https://www.canva.dev/docs/print-partnerships/concepts/credentials/#artwork-api-secret)



If you don't have these credentials, [register as a print partner](https://www.canva.dev/docs/print-partnerships/quickstart/#step-1-register-as-a-print-partner).

## Prerequisites

This tutorial assumes experience with:

  * JavaScript
  * Node.js
  * Express.js



You don't have to develop the server-side features of an integration with Node.js. This documentation's examples use Node.js for illustrative purposes.

## System requirements

This tutorial assumes you have the following tools installed:

  * [Node.js⁠(opens in a new tab or window)](https://nodejs.org/en/download/)
  * [npm⁠(opens in a new tab or window)](https://www.npmjs.com/get-npm)



For the most part, this tutorial is compatible with the major operating systems, including Windows, macOS, and Linux, but some commands may not work on Windows.
