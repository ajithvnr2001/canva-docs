---
url: https://www.canva.dev/blog/developers/helping-your-users-write-better-prompts/
title: Helping your users write better prompts - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:06.204385+00:00
---

# Helping your users write better prompts - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/helping-your-users-write-better-prompts/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

AI

# Helping your users write better prompts

Learn how you can lead your users to better write prompts for AI apps.

![](https://www.canva.dev/_next/static/media/thumbnail.a4fb80d1.jpg)

* * *

  * 


[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Aug 22, 2023

* * *

AI apps are popping up everywhere. We’ve all played around with ChatGPT to write an email for us, used a Text to Image app to generate a silly image, or created a new headshot with an AI app. But users are seeing varied success with many of these apps. One of the reasons? The prompts they’re entering.

Let’s take a look at Canva’s [Text to Image⁠(opens in a new tab or window)](https://www.canva.com/your-apps/text-to-image) app. The app has us enter a text prompt and choose a selected style. We’ll go ahead and use a prompt like “a warrior panda riding into battle”.

![Putting a prompt into the text to image app](https://www.canva.dev/_next/static/media/text-to-image-prompt.cf558f03.jpg)

After some AI Magic, Canva gives us 4 results.

![The results!](https://www.canva.dev/_next/static/media/warrior-panda-results.236a4922.jpg)

Now these results aren’t bad. We can clearly see this is a panda that is a warrior, but there doesn’t seem to be much of a battle around. Or any riding for that matter.

One thing most users do is focus on the subject of the image. This helps create a high-fidelity subject, but it’s missing lots of the details that make it realistic. When entering a prompt, describe the details of the image. Think of things like “blue eyes” or “wearing a red scarf”, additionally describing the form, style, and composition. Many apps include a Style selector to make sure users do this. We can use more selectors to make sure our users are including more detail. And lastly, encourage users to use more adjectives and adverbs. This will help add more complexity to our prompt without making it overly wordy.

This is where something like our Prompt Improver app comes into play!

The Prompt Improver app is an app I built for myself during an internal hackathon. This is not nor will ever be a release app. This is to illustrate what kind of messaging or assistance you can add to your AI app to help users write better prompts.

![How our prompt improver app changes as we type](https://www.canva.dev/_next/static/media/prompt-improver.f09982f3.gif)

Encouraging us to add more descriptive language based on the prompt, the Prompt Improver app suggested some changes, and as we add them, removes them from the list of suggestions. This is done using a Parts of Speech ([pos⁠(opens in a new tab or window)](https://www.npmjs.com/package/pos)) npm package that classifies the words in the sentence as a user types in their prompt. You can use these parts of speech to ensure users are entering critical things like adjectives and adverbs, and suggest prompt improvements.

Now let’s take our improved prompt, “a warrior panda riding a horse into a chaotic battle scene”, and see what Text to Image returns for us.

![The results! But better!](https://www.canva.dev/_next/static/media/panda-warrior-chaotic.09baf3ae.jpg)

Now we have some more details showing up in our image, like the people in the background and the panda on a panda-horse.

We know that as the developer training your models, you know them best. You’ll know what kind of prompts work best, and what data users should be entering to achieve the best results. Make sure to share your knowledge with users! Add some tool tips or info text to your app UI to inform users about key things to include (or avoid!) in their prompt. Sometimes adding cues to what key descriptors users are missing in their prompt can go a long way with garnering user love for your app.

Happy AI Creating!

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.4b7da7e8.jpg)](https://www.canva.dev/blog/developers/external-monetization-community-tips/)

[MonetizationExternal monetization for Canva AppsA community member's tips and tricks for monetizing your app](https://www.canva.dev/blog/developers/external-monetization-community-tips/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Jun 4, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.f388d5fa.jpg)](https://www.canva.dev/blog/developers/lambda-functions-for-canva-apps/)

[lambdaGetting Started with Lambda Functions for Canva AppsLearn how to use Lambda functions](https://www.canva.dev/blog/developers/lambda-functions-for-canva-apps/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Oct 4, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.f5e81b12.png)](https://www.canva.dev/blog/developers/gen-ai-startup-solved-product-gaps-with-apps-sdk/)

[Apps SDKHow a Gen AI Startup solved its product gaps with the Canva Apps SDKHow Krikey AI developed an App on Canva to fill their product gaps.](https://www.canva.dev/blog/developers/gen-ai-startup-solved-product-gaps-with-apps-sdk/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Mar 1, 2024
