---
url: https://www.canva.dev/blog/engineering/how-canva-combined-modern-image-processing-with-150-year-old-optics-for-a-new-approach-to-camera/
title: Combining Classic and Modern: A New Approach to Camera Simulation - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:13.665266+00:00
---

# Combining Classic and Modern: A New Approach to Camera Simulation - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/how-canva-combined-modern-image-processing-with-150-year-old-optics-for-a-new-approach-to-camera/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Computer Vision

# Combining Classic and Modern: A New Approach to Camera Simulation

Applying classic principles from physics and optics to build the best possible camera effects at Canva.

![](https://www.canva.dev/_next/static/media/thumbnail.059f71b8.png)

* * *

  * 


[Bhautik Joshi⁠(opens in a new tab or window)](https://bhautik.org)Nov 18, 2021

* * *

We _love_ the look of high-end portraits — that shallow-depth-of-field look where the subject is in-focus but the background is blurred out. But some cameras, especially those on smartphones, don't quite manage to do this convincingly. Also sometimes, you'd like to be able to adjust the blur after you've taken the photo too.

So here at Canva we've built [Auto Focus⁠(opens in a new tab or window)](https://www.canva.com/features/photo-effects/), a camera simulation tool that allows you to re-photograph your images with a high-end virtual camera lens to get that distinctive portrait look. To do this, we drew on the classic principles of optics and physics in early cameras to build the most physically-accurate digital effect possible.

![](https://www.canva.dev/_next/static/media/img-0-XoJx7ZTqJSsG47pT.e78655b8.png)

Example of Auto Focus applied to an image (original on the left)

## Why camera simulation is needed for smartphone photography

The shallow depth-of-field look is typically achieved through a combination of a large imaging surface and classic optical design allows subjects to be isolated and backgrounds to be blurred, turning image distractions into less prominent splashes of color.

![](https://www.canva.dev/_next/static/media/img-1-tao6xcybKtKpkv7X8CzMvA.3515f63b.png)

Images with shallow depth-of-field taken with a DSLR

This look isn't so easy to achieve with cell phone cameras because the heritage of cell phone optics dates back to the early days of photography. Soon after cameras were developed it became obvious that most people wanted to take photos, without having to do other things like adjust focus dials.

Kodak solved this in 1900 with the [Brownie⁠(opens in a new tab or window)](https://www.brownie-camera.com/) which was like the iPhone of the 20th century — simple user interface, no dials. Thanks to clever lens design there was no need to focus because _everything_ is in focus, and this optical design principle has carried forward to modern cellphones today. This naturally comes at the cost of shallow-depth-of-field, which now needs more complex optics (extra lenses!) or camera simulation to achieve.

## Problems with existing shallow-depth-of-field simulations

Camera simulation allows us to re-capture images through a simulation of a high-end camera. The classic simulation approach places a given pixel out of focus by processing a circle of its surrounding pixels, before finding the average colour for a new blurred pixel. The more out of focus a pixel is, the larger the circle or _kernel_ needs to be.

Unfortunately, this often results in problems with color leaking between in-focus and out-of-focus areas. It leads to artificial smoothness, in a way that doesn't look natural. This happens because the cylindrical sample for each pixel, (the kernel) includes pixels from both in-focus areas and the foreground, softening the edges of the simulation.

![](https://www.canva.dev/_next/static/media/img-0-T-pdFCap7wLrrfmv.cc57392c.png)

In the previous example showing the foreground leaking into the background (left), see the sampling kernel for a specific point (circled above). We'd expect that the defocused region behind the camera would be dark, but in the sampling kernel nearly half of it is the red plastic of the foreground object. When this is averaged, we get a muddy red instead of deep black

![](https://www.canva.dev/_next/static/media/img-1-JyxO3a8B0a9UeqHvsuccVw.93b4d31e.png)

From top to bottom, left to right: the original image, an image with the old technique, an image with the new technique, and finally, a reference image taken with a DSLR

### A quick note on depth maps

Underpinning the camera simulation techniques here are _depth maps_ , which were initially used in games and visual effects. Our _depth maps_ are generated by using a machine learning algorithm to determine the depth profile of an image. The depth of each pixel is calculated and stored, to create a 2.5D diorama from the picture. A pixel's level of blur is determined by its position on the depth map, that is, the farther away from the focus point the more out-of-focus it is.

![](https://www.canva.dev/_next/static/media/img-1-GZuhssaDigPVi3a_LHGaQQ.83ebfd6c.png)

The source image (left) and the generated depth map (right). The brighter the pixel in the depth map, the closer it is to the camera. Note how the green box and red camera are brighter, and the garage is darker

### More accurate light transport

To get a more accurate simulation, we aimed to replicate how light moves in the real world. Real cameras don't receive light in a perfectly shaped cylinder, but instead receive light that's projected in a conical pattern via the lens. As such, we aimed camera simulation to replicate this, with a pixel that is out of focus being treated as the focal point between two light cones — as shown in the diagrams below.

![](https://www.canva.dev/_next/static/media/img-0-ZI_7zhQuHHZkniP5.a8ff5d5e.png)

![](https://www.canva.dev/_next/static/media/img-0-uMUjYsv0uLfXdvwI.be54daea.png)

A top-down and isometric view of our example scene, with the red camera and green box in the foreground and the garage scene in the background. Here our updated model based on camera optics uses two cones whose apex meets at the focus depth to figure out which pixels should contribute in our kernel. Note that the pixel that is just near the edge of the in-focus object but in an out-of-focus area (along the axis of the cones) correctly excludes pixels from the in-focus region but gets most of its contribution from the background

![](https://www.canva.dev/_next/static/media/img-0-rIfDWtG4u3wpAs9v.2e97d9ea.png)

![](https://www.canva.dev/_next/static/media/img-0-Vv1SDfNr84hG1jQm.0b4a92fd.png)

The same scene but with the previous cylindrical model for sampling. Note that the out-of-focus pixel in the lower part of the diagram samples many pixels from the in-focus region, leading to the characteristic color leakage into the out-of-focus area

## Conclusion

![](https://www.canva.dev/_next/static/media/img-1-SDAO8X9tlTNQvMpAt1RHgQ.c62927d7.png)

Comparing the new results (left) versus the DSLR reference (right). Note the lack of color leakage around the foreground object edges

We're big camera and photo nerds over here at Canva, and we wanted to bring you the most faithful camera simulation we could. Designers and photographers love attention to detail; while the traditional shallow-depth-of-field simulation works, the oversmooth and leaky look puts it into uncanny valley, occasionally looking artificial.

We've extensively studied film cameras and photos to tune our new technique to bring you the best camera simulation we could make, giving you a true-to-life authentic vintage camera experience.

## Try it out!

A special thanks to [Kerry⁠(opens in a new tab or window)](https://www.linkedin.com/in/kerry-halupka/) for the ML magic, and to [Harley⁠(opens in a new tab or window)](https://www.linkedin.com/in/harleymellifont/) and the photo editor team for getting this out into the world!

We're really excited to see all the amazing things the Canva community creates with this tool. You can [try it out for yourself in Canva right now⁠(opens in a new tab or window)](https://canva.me/XggvM06Dwkb)! We hope you like it as much as we do. As a finale, enjoy the images below.

_Interested in photography, machine learning and image processing?_ [_Join us!_ ⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/)

![](https://www.canva.dev/_next/static/media/img-0-WO7lzElAZu3hLLA7.79181b9d.png)

![](https://www.canva.dev/_next/static/media/img-0-Gmf__qTSGSakWY8C.9e61e823.png)

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.c3cd408c.png)](https://www.canva.dev/blog/engineering/discovering-headroll-cve-2023-0704-in-chromium/)

[SecurityDiscovering Headroll (CVE-2023–0704) in ChromiumDiscovery of Headless Chromium security vulnerability, how it works, and mitigations that should be applied to similar configurations](https://www.canva.dev/blog/engineering/discovering-headroll-cve-2023-0704-in-chromium/)

[Zac Sims⁠(opens in a new tab or window)](https://au.linkedin.com/in/zacsims), [Rhys Elsmore⁠(opens in a new tab or window)](https://au.linkedin.com/in/rhyselsmore)Apr 5, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.ecf0ad99.jpg)](https://www.canva.dev/blog/engineering/how-we-see-groups-in-design/)

[Computer visionHow we see groups in designHow we understand and detect groups in user designs](https://www.canva.dev/blog/engineering/how-we-see-groups-in-design/)

[Xin Liang⁠(opens in a new tab or window)](https://www.linkedin.com/in/xin-liang-0968b270/)Jun 21, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.280453dc.jpg)](https://www.canva.dev/blog/engineering/alpha-blending-and-webgl/)

[FrontendAlpha Blending and WebGLThis article introduces alpha blending and some tips relating to the alpha channel in WebGL development.](https://www.canva.dev/blog/engineering/alpha-blending-and-webgl/)

[David Guan⁠(opens in a new tab or window)](https://twitter.com/davidguandev)Dec 4, 2017

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


