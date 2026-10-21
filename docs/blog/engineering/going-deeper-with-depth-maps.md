---
url: https://www.canva.dev/blog/engineering/going-deeper-with-depth-maps/
title: Going Deeper with Depth Maps - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:13.608525+00:00
---

# Going Deeper with Depth Maps - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/going-deeper-with-depth-maps/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Computer Vision

# Going Deeper with Depth Maps

How we use machine learning to estimate depth and salience maps for photos in Canva.

![](https://www.canva.dev/_next/static/media/thumbnail.5e886671.jpeg)

* * *

  * 


[Kerry Halupka⁠(opens in a new tab or window)](https://medium.com/@kerry.halupka)Dec 15, 2021

* * *

The Canva Photo Editor Group's mission is to make our user's photos look amazing. So recently, we released a new tool called [Auto Focus⁠(opens in a new tab or window)](https://www.canva.com/features/photo-effects/) that lets users edit the focus point of their photo after it was taken, applying a shallow depth of field effect that helps their subject pop.

![](https://www.canva.dev/_next/static/media/img-0-6O4-IGU-k4x3p2lT.e8dae585.png)

Example of Auto Focus applied to an image (original left)

Essentially, this effect keeps the subject in focus while blurring things around them. In the image above, where the focus point is the person in the center, pixels in the background (and therefore further away from the focus depth) are blurred. Also, if any objects were closer to the camera than the subject, they too are blurred.

Note that "blurred" is a very hand-wavy term for the cool camera simulation process that's actually happening. For more information about this simulation, check out [our earlier blog post](https://www.canva.dev/blog/engineering/how-canva-combined-modern-image-processing-with-150-year-old-optics-for-a-new-approach-to-camera/).

To apply the Auto Focus effect, we need two things:

  * An estimation of the depth, or relative distance from the camera, of every pixel in the image, and
  * A depth at which to focus.



This blog post describes how we estimate these for a user's photo.

## Depth Estimation from Stereo Vision

> "Depth perception jokes are always near misses. You don't see the punchline until it's too late."
> 
> — Anonymous

Humans have a well-developed sense of depth. For example, while you might not know the exact distance of your monitor from your eyes, you do know how close it is relative to everything else in your field of view. There are several ways that you achieve this, referred to as _depth cues_.

The most common depth cue is _binocular vision_ , which is receiving two slightly different images to each eye. The location of the objects you see from your left eye is slightly different to their location seen from your right eye. If an object is relatively close, like the person shown in the following diagram, the discrepancy between your left and right eyes is greater than for objects farther away, like the tree. This is called the [_parallax effect_ ⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Parallax), and your brain interprets this information to inform your estimate of the relative distance of objects in your visual field.

![](https://www.canva.dev/_next/static/media/img-0-iQ6lb7QJMYKftSJR.5f7a148a.png)

A person standing in front of a tree, as seen from the left and right eyes separately

Phones with dual cameras capture stereo images like this and can use the two images to estimate depth. However, in the Canva use case, users generally upload images from a single viewpoint, and from all sorts of different devices, so we can't rely on stereo vision technology.

## Depth Estimation from Monocular Vision

> "What's the difference between a butt kisser and a brown noser? Depth perception"
> 
> — Helen Mirren, maybe

The good news is that we can perform depth estimation from a single viewpoint. We know this because we still have a good sense of depth perception if we walk around with one eye closed. We use more depth cues than just stereo cues, as shown in the following diagram. In each of the examples, a depth cue makes it appear that the purple cylinder is closer to the camera than the turquoise cylinder.

![](https://www.canva.dev/_next/static/media/img-0-YePCk1eqVtIQEQcY.43395bfb.png)

_Common depth cues the brain uses to perceive depth without stereo vision._

And for bonus points, notice that the "cylinders" aren't actually cylinders at all. We use shading (a version of the "cast shadows" depth cue) to make it appear that a flat, two-dimensional shape has depth.

![](https://www.canva.dev/_next/static/media/img-0-vhSNHQcFo5mQgzO-.087c0204.gif)

All of this inherent information in a scene means that it's possible to estimate a depth map from a single image, as shown in the following example.

![](https://www.canva.dev/_next/static/media/img-0-VtInuKIDbndmz28C.c8482f10.png)

An RGB image (left) and the corresponding depth map (right). The closer to the camera an object is, the brighter it appears in the depth map

## Focusing on the right point

> "Tip: Don't drink water while you're trying to focus. It will reduce your concentration."
> 
> — WHO, probably

The second requirement of our system is to work out the depth to focus on so that the object in focus, by default, is the subject of the photo. Of course, users can adjust that focus depth if they want to pick a different subject, but we want to estimate smart defaults to minimize the number of steps it takes to make a photo look great.

To estimate the subject of an image, we use a concept called a [_saliency map_ ⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Saliency_map). A saliency map indicates the level of importance of each pixel in an image to the human visual system. Usually, the area of an image a human looks at first is more salient than any other area. Determining salience value is a tricky concept because it is very subjective. For example, when I'm hungry, you can bet I'll look at ice cream in a photo before I look at the person holding it.

![](https://www.canva.dev/_next/static/media/img-0-8jebOX_Rmu-IMRJz.246e318f.png)

What's the most salient thing in this image? There's no wrong answer (except the apple, that's definitely wrong)

## Machine learning to the rescue

> "I miss hugging people. It might be a depth perception issue."
> 
> — me

The current state-of-the-art approaches to estimating a depth map from a single image utilize supervised deep learning approaches, such as [convolutional neural networks⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Convolutional_neural_network) (CNNs) and [vision transformers⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Vision_transformer) (ViTs). "Supervised" means that we show the neural networks thousands of images and have it predict the depth of each of the pixels. Then, we compare the predictions to the "ground truth", which is the known depth of each image.

Canva needs to estimate depth relatively quickly, on a wide range of photos, with varying degrees of quality. Inspired by recent depth map prediction approaches, we opted for a pre-trained [ResNet⁠(opens in a new tab or window)](https://arxiv.org/abs/1512.03385) as the backbone. To use ResNet as the encoder for dense depth prediction, we removed the final pooling, fully connected, and softmax layers. The ResNet encoder generates feature maps of decreasing size but with increasing receptive fields, enabling the network to identify depth cues at both small and large scales.

We pass these feature maps to the decoder through skip connections. The decoder progressively grows the depth prediction from coarse to fine through residual convolution blocks and upsampling operations. The output of this process is a feature map at half the resolution of the input image, with 256 channels. There is a huge amount of information about each pixel contained in this feature map. To make sense of this information, we apply two convolutional layers to condense the output to a single channel over two steps. We'll call these layers the depth map-specific layers. We then upscale the output to the original size using bilinear interpolation, and re-scale it to a range of 0—1.

![](https://www.canva.dev/_next/static/media/img-1-ZHzo_Kf4HQCDL-FmuPRBRQ.d24919bd.gif)

Final CNN architecture used for the Auto Focus tool. The network involves an encoder/decoder architecture with task-specific layers for depth map and saliency map estimation. The saliency map is shown prior to thresholding

This sort of network will look pretty familiar for anyone who has worked with pixel-wise tasks like depth prediction and semantic segmentation. We trained this network to estimate depth for a wide range of images. However, in addition to depth map prediction, our specific use case also requires estimating the most salient location in the image (and the corresponding depth) to set the default focus depth.

One option to achieve this would be to train a separate network to estimate a saliency map for each image. However, this would necessitate either computing the depth and saliency in sequence, which would take more time, or computing them in parallel, which would require more compute resources. So instead, we hypothesized that a network trained to predict depth would also compute useful features for saliency. If true, the information-dense final layer of the decoder might contain these useful features.

To test the hypothesis, after the depth prediction network reached an acceptable level of performance, we froze the weights of the encoder/decoder network and depth map-specific layers. We also branched off the final layer of the decoder network with a randomly initialized set of saliency map-specific layers, which were then trained on a saliency dataset using a binary classification task with salient regions as the positive class.

We designed the training protocol this way because the primary concern of the network is to estimate an accurate, high-resolution depth map, with the saliency result being secondary. While we didn't specifically train encoder/decoder layers to extract a saliency map, we found that the detected salient regions were sufficiently accurate.

By using binary classification as the task to train the saliency map prediction, the resulting saliency values ranged between 0 and 1. We then applied a threshold at 0.8. This relatively high threshold means that some images without a well-defined salient region might not have any pixels classified as salient. In such cases, a default focus depth at the halfway point of the depth map is used, which we found to be a better user experience than the result produced by lowering the saliency threshold. In the images below, the pixels highlighted in red are classified as salient using this definition. We then calculate the default focus depth as the median depth of all salient pixels.

![](https://www.canva.dev/_next/static/media/img-1-K8yOAE_Y6UV1zvve3XO6MA.b275bcb7.png)

Left: Photos of Willow, the most beautiful dog in the world*. Middle: Depth map predictions for the two photos, with pixels classified as salient highlighted in red. Right: The result of applying Auto Focus in Canva using the predicted default depth, making Willow (if anything) more beautiful

## Try it out!

We're really excited to see all the amazing things the Canva community creates with this tool. [You can try it out for yourself in Canva right now⁠(opens in a new tab or window)](https://canva.me/XggvM06Dwkb)! We hope you like it as much as we do.

_Interested in photography, machine learning and image processing?_ [_Join us!_ ⁠(opens in a new tab or window)](https://www.canva.com/careers/engineering/)

## Acknowledgements

Special thanks to [Bhautik Joshi⁠(opens in a new tab or window)](https://bhautik.org/) for the camera simulation magic. Huge thanks to [Grant Noble⁠(opens in a new tab or window)](https://www.linkedin.com/in/grant-noble-8253994a/) and [Paul Tune⁠(opens in a new tab or window)](https://www.linkedin.com/in/paul-tune-0ba18116/) for suggestions in improving the post.

* **Editor's note:** this is the author's personal (very) biased opinion towards one particularly cute Whippet. All views shared here may not be views shared by Canva.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.afd174a5.jpg)](https://www.canva.dev/blog/engineering/fonts-are-still-a-helvetica-of-a-problem/)

[SecurityFonts are still a Helvetica of a ProblemCVEs in three strange places and the unique problem of safely processing and handling fonts.](https://www.canva.dev/blog/engineering/fonts-are-still-a-helvetica-of-a-problem/)

Angus Cornall, [Peter Kydas⁠(opens in a new tab or window)](https://www.linkedin.com/in/peter-kydas)Mar 6, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.733607a9.jpg)](https://www.canva.dev/blog/engineering/endpoint-vulnerability-management-at-scale/)

[SecurityEndpoint vulnerability management at scaleHow we do endpoint vulnerability management at Canva.](https://www.canva.dev/blog/engineering/endpoint-vulnerability-management-at-scale/)

[Santiago Gutiérrez⁠(opens in a new tab or window)](https://www.linkedin.com/in/santiago-gutierrez-z/)May 7, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.5df784be.png)](https://www.canva.dev/blog/engineering/behind-the-scenes-of-canvas-designdna-campaign/)

[Machine LearningBehind the scenes of Canva's DesignDNA campaignHow we used generative AI to build our year-in-review campaign](https://www.canva.dev/blog/engineering/behind-the-scenes-of-canvas-designdna-campaign/)

[Divya Patel⁠(opens in a new tab or window)](https://www.linkedin.com/in/divyapat1/)Feb 24, 2025

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


