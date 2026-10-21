---
url: https://www.canva.dev/docs/print-partnerships/distribution/pre-launch-checklist/
title: Pre-launch checklist - Distribution - Canva Print Partnerships Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:00.303803+00:00
---

# Pre-launch checklist - Distribution - Canva Print Partnerships Documentation

> Source: https://www.canva.dev/docs/print-partnerships/distribution/pre-launch-checklist/

Distribution

[Pre-launch checklist](https://www.canva.dev/docs/print-partnerships/distribution/pre-launch-checklist/)

# Pre-launch checklist

Copy page

Before launching an integration, partners must verify that it:

  * Works as expected.
  * Follows Canva's guidelines.
  * Meets Canva's quality standards.



This page contains a checklist to validate an integration.

## Check the autoAuthToken calculation

Integrations use the ID of a user to calculate [autoAuthTokens](https://www.canva.dev/docs/print-partnerships/tutorial/calculate-autoauthtoken/). This user ID must be unique. If it's not unique, users can view the private designs and uploads of other users.

## Follow Canva's guidelines

Canva has guidelines that partners must follow for an integration. The guidelines ensure that the integration is user friendly and respectful of Canva's brand.

To read these guidelines, see the following presentations:

  * [Brand guidelines⁠(opens in a new tab or window)](https://www.canva.com/design/DAEiFHvOisY/PYVd_iQ1VyTVW-kz58uhDw/view?utm_content=DAEiFHvOisY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
  * [UX guidelines⁠(opens in a new tab or window)](https://www.canva.com/design/DAEYPfbhBjg/bhDFRxLrS8o14I_DWP-6xg/view?utm_campaign)



## Test the loading screen

When a user opens the editor, they see a [skeleton screen⁠(opens in a new tab or window)](https://uxdesign.cc/what-you-should-know-about-skeleton-screens-a820c45a571a) or an animated Canva logo. These elements are included in the Print Partnership's SDK by default. An integration must not overwrite these with custom elements.

![A side-by-side view of the loading screens that users see when they open the editor. On the left is the skeleton screen. On the right is the animated Canva logo.](https://www.canva.dev/_next/static/media/skeleton-screen-and-logo.27a9312c.gif)

## Check the furniture

Partners can request Canva to add furniture to products. Some examples of furniture are fold lines, bleed lines, rounded borders, and circular borders.

Partners must verify if the products show the furniture as expected.

## Test the order process

Partners must play the role of a user and verify that they can:

  1. Navigate to an integration.
  2. Create a design.
  3. Proof the design.
  4. Preview the proofed design.
  5. Purchase a print of the design.



## Check the preview and print files

After a user finishes proofing a design, Canva creates:

  * **A preview file:** A low-resolution preview version of the design.
  * **A print file:** A high-quality print version of the design.



Canva creates these files based on the integration's [export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/).

Partners must verify if the export settings are correctly applied to the files. Some settings to verify are file format, bleeds, crop marks, and format. For a complete list of the available settings, refer to [Export settings](https://www.canva.dev/docs/print-partnerships/reference/export-settings/).

## Request Canva's approval

After validating an integration, partners must request Canva's approval to launch the integration.

After receiving this request, Canva:

  * Reviews the user experience of the integration.
  * Completes a test order.



If the integration meets Canva's standards and the test order is successful, Canva responds with approval to proceed with the launch. If not, Canva responds with the required changes to prepare the integration for launch.

To raise a request:

  1. Navigate to the [Canva Helpdesk⁠(opens in a new tab or window)](https://canva-external.atlassian.net/servicedesk/customer/portal/68/group/37).
  2. Select **Testing Request**.
  3. In the **Link to integration** field, specify the URL to the integration you want Canva to approve.
  4. In the **Target Launch Date** field, specify the date when you plan to launch the integration.
  5. In the **Completed QA Checklist** field, specify `Yes` if you've completed the [pre-launch checks](https://www.canva.dev/docs/print-partnerships/distribution/pre-launch-checklist/). Otherwise, specify `No`.
  6. In the **Notes** field, provide any notes, caveats, or additional information you want Canva to consider.
  7. In the **Attachment** field, attach any files or screenshots that'll help Canva better understand the information you've provided.


