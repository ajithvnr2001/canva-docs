---
url: https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/
title: Canva Designs, Folders, and Assets - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:56.453581+00:00
---

# Canva Designs, Folders, and Assets - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Canva Designs, Folders, and Assets

Explanations of some key Canva resources.

Copy page

## Designs

A design is anything you create in Canva, including:

  * [Documents⁠(opens in a new tab or window)](https://www.canva.com/docs/)
  * [Presentations⁠(opens in a new tab or window)](https://www.canva.com/presentations/)
  * [Print products⁠(opens in a new tab or window)](https://www.canva.com/print/), such as T-shirts, mugs, and business cards
  * [Social media content⁠(opens in a new tab or window)](https://www.canva.com/social-media/), such as Instagram posts
  * [Videos⁠(opens in a new tab or window)](https://www.canva.com/video-editor/)
  * [Websites⁠(opens in a new tab or window)](https://www.canva.com/website-builder/)
  * [Whiteboards⁠(opens in a new tab or window)](https://www.canva.com/whiteboards/)



This doesn't include elements within a design, such as:

  * Images and videos uploaded by a user.
  * Built-in elements, such as shapes and stock images.



Most Canva designs are between 40 × 40 pixels and 8,000 × 8,000 pixels and can have multiple pages, with exceptions for some design types, such as Documents (unlimited length) and Whiteboards (unlimited width and height).

## Folders

Folders are a collection of items, such as:

  * Other folders.
  * Assets, such as uploaded images, audio, and videos.
  * Designs, such as Instagram posts, Presentations, and Documents (Canva Docs).
  * Brand Templates.



When identifying folders, we recommend using the folder's `id`, which can't be changed by a user. The top level of the user's content library, [Projects⁠(opens in a new tab or window)](https://www.canva.com/help/find-designs-and-folders/), is represented in APIs as a folder with the ID `root`.

## Assets

Assets, known as [Uploads⁠(opens in a new tab or window)](https://www.canva.com/help/manage-uploads/) in the Canva UI, are user-upload _images_ , _audio tracks_ , and _videos_. Assets are stored in the user's [Projects⁠(opens in a new tab or window)](https://www.canva.com/help/find-designs-and-folders/) along with their designs, and users can add their assets, or shared assets, to designs using the [Uploads tab⁠(opens in a new tab or window)](https://www.canva.com/help/manage-uploads/) in the Canva editor. Users can also add [tags⁠(opens in a new tab or window)](https://www.canva.com/help/add-edit-tags/) to their assets to help them search through their assets.
