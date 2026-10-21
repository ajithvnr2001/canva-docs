---
url: https://www.canva.dev/blog/developers/spotlight-on-the-background/
title: Spotlight on the background - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:09.355186+00:00
---

# Spotlight on the background - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/spotlight-on-the-background/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Background

# Spotlight on the background

![](https://www.canva.dev/_next/static/media/thumbnail.eab8445b.png)

* * *

  * 


[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Jan 22, 2024

* * *

If you were following along with our [Christmas Drops⁠(opens in a new tab or window)](https://community.canva.dev/tag/developer-christmas) in our Developer Community, you know that we recently GA’ed the `setCurrentPageBackground` method, along with the `background` property for `addPage`. So we want to take a moment to celebrate an often overlooked but design game changing layer: the background!

A design’s background can elevate or distract from it’s main message, so it’s a important background player 😆. With the release of our new background properties and methods, you can programmatically update page backgrounds with your generated AI images and videos, color schemes, and more. You can also add new pages with those backgrounds, allowing your app users to keep the design pages consistent.

Let’s take a look at a couple ways to use the background property and method.

## Set a Page Background

Using the `setCurrentPageBackground` you can update a design’s background. Based on which page a user has selected, that will set the context for the Current Page. This is useful if you're generating scenes or low fidelity imagery that aren’t the focal point of the design. Once the new image is generated, you can upload it and add it as the background.

Using an example, such as a sci-fi landscape model from [Hugging Face⁠(opens in a new tab or window)](https://huggingface.co/Joeythemonster/sci-fi-landscape), we can generate a futuristic background scene for our design. We’ll go ahead and generate the image and wait for a response. Once that response returns, we want to convert the blob to a DataUrl and then upload it. Once it’s uploaded, we can use the returned image ref to add it as a background.
    
    
    async function getImage() {
    
     const response = await fetch(
    
       "https://api-inference.huggingface.co/models/Joeythemonster/sci-fi-landscape",
    
       {
    
         headers: headers,
    
         method: "POST",
    
         body: JSON.stringify({"inputs": "a green sun setting over a blue city"}),
    
       }
    
     );
    
     const result = await response.blob();
    
     return result;
    
     }
    
    
    
    
     const setBackgroundImage = async () => {
    
       setLoading(true);
    
       const image = await getImage();
    
       const dataURL = await blobToDataURL(image);
    
       const { ref } = await upload({
    
         type: "IMAGE",
    
         mimeType: "image/jpeg",
    
         url: dataURL,
    
         thumbnailUrl: dataURL,
    
         width: 540,
    
         height: 720,
    
       });
    
       await setCurrentPageBackground({
    
         asset: { type: "IMAGE", ref },
    
       });
    
       setLoading(false);
    
     };

JS

Copy

![Drag Racing](https://www.canva.dev/_next/static/media/scifi-landscape.f9c1aa51.png)

## Add a New Page with a Background

The `addPage` method now has a new property for the background. You can add pages from your app that have consistent design themes. If you're generating full page designs to add to a user’s design, this enables you to now incorporate a background design or color to that page.

Let’s use an example of generating certificates for a class completion. We want to add the award design to the page, plus give it an antique paper color background. We’ll add a group of elements for the certificate design and set the background property to a color, something like #f4f0e8.
    
    
    await addPage({
    
      title: "Certificate",
    
      elements: [
    
        {
    
          ...certElement,
    
          width: headerElementWidth,
    
          height: "auto",
    
          top: 0,
    
          left: 0,
    
        },
    
        {
    
          ...nameElement,
    
          width: headerElementWidth,
    
          height: "auto",
    
          top: 356,
    
          left: 0,
    
        },
    
      ],
    
      background:{
    
        color:  "#f4f0e8",
    
      },
    
    });

JS

Copy

![Drag Racing](https://www.canva.dev/_next/static/media/award-example.1605f693.png)

Think your app could benefit from a refresh with this launch? Or maybe now a new use has popped into your mind for the next app to build! Well we can’t wait to see. As always, if you have any questions that you would like community help with, join our [Developer Community⁠(opens in a new tab or window)](http://community.canva.dev) to connect with your peers and the team behind Canva Developers. Happy building!

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.b66d472b.jpg)](https://www.canva.dev/blog/developers/simplebooklet-partner-solution/)

[Content Publisher IntentSimplebooklet partner solutionHow Simplebooklet achieved a 10x user increase with Canva's Content Publisher Intent.](https://www.canva.dev/blog/developers/simplebooklet-partner-solution/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)May 19, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.d9204a0c.jpg)](https://www.canva.dev/blog/developers/canva-and-coding-agents-platforms/)

[Connect APIUsing Canva with your coding agentGuidance for using Canva with coding assistants, Dev MCP, remote MCP, and the Connect APIs.](https://www.canva.dev/blog/developers/canva-and-coding-agents-platforms/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Jun 9, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.f388d5fa.jpg)](https://www.canva.dev/blog/developers/lambda-functions-for-canva-apps/)

[lambdaGetting Started with Lambda Functions for Canva AppsLearn how to use Lambda functions](https://www.canva.dev/blog/developers/lambda-functions-for-canva-apps/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Oct 4, 2023
