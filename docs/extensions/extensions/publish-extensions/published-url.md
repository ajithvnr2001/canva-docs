---
url: https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/
title: Published URL - Publish extensions - Canva Extensions Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:52.242409+00:00
---

# Published URL - Publish extensions - Canva Extensions Documentation

> Source: https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/

Publish extensions

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/)[Quickstart](https://www.canva.dev/docs/extensions/extensions/publish-extensions/quickstart/)[Continuation](https://www.canva.dev/docs/extensions/extensions/publish-extensions/pagination/)[Search](https://www.canva.dev/docs/extensions/extensions/publish-extensions/search/)[Published URL](https://www.canva.dev/docs/extensions/extensions/publish-extensions/published-url/)[Messages](https://www.canva.dev/docs/extensions/extensions/publish-extensions/messages/)[Authentication](https://www.canva.dev/docs/extensions/extensions/publish-extensions/authentication/)

Layouts

[Overview](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/)[Basic layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/basic-layout/)[Flat list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/flat-list-layout/)[Nested list layout](https://www.canva.dev/docs/extensions/extensions/publish-extensions/layouts/nested-list-layout/)

# Published URL

Share an external link for users to view their published assets.

Copy page

When a [publish extension](https://www.canva.dev/docs/extensions/extensions/publish-extensions/) uploads a user's design to the destination platform, the [`/publish/resources/upload`](https://www.canva.dev/docs/extensions/server-api/post-publish-resources-upload/) endpoint can provide a `url`:
    
    
    {
    
      "type": "SUCCESS",
    
      "url": "https://example.com"
    
    }

JSON

Copy

This URL is shown in the dialog that appears after the design is published.

For an app to be approved for release via the [Apps Directory⁠(opens in a new tab or window)](https://canva.com/apps), it must provide a URL that satisfies the [UX guidelines](https://www.canva.dev/docs/extensions/distribution/ux-guidelines/publish-extensions/).

## Generate external link

You can configure a publish extension to display the URL of the published design with the anchor text "View in [App name]" instead of the complete URL.

To do this:

  1. Navigate to an app via the Developer Portal.
  2. From the **Extensions** page, expand the **Publish** pane.
  3. Enable **Generate external link**.



## UX guidelines

At a minimum, the URL must allow the user to view their published design in the context of the destination platform. For example, if a user publishes a design to Twitter, they should see a link to their tweet.

If the destination platform expects further action, the URL should take the user to where they can complete that action. For example, a website creation tool may provide the URL of a page that allows the user to choose where to place their published design.

The URL must be fewer than 2000 characters.
