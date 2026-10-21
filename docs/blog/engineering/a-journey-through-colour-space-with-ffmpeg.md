---
url: https://www.canva.dev/blog/engineering/a-journey-through-colour-space-with-ffmpeg/
title: A journey through color space with FFmpeg - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:10.768673+00:00
---

# A journey through color space with FFmpeg - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/a-journey-through-colour-space-with-ffmpeg/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Color Space

# A journey through color space with FFmpeg

For those who want to understand what color spaces are, find out how to transform videos from one color space into another one, or read about how I almost went crazy trying to find out why videos generated with Canva look slightly off in terms of color.

![](https://www.canva.dev/_next/static/media/thumbnail.0dd77367.png)

* * *

  * 


[Sven Schindler⁠(opens in a new tab or window)](https://www.linkedin.com/in/sven-schindler-de-au/)Apr 17, 2023

* * *

 _“Hello @cop A user reported that their exported video looks less saturated compared to how it looks like on the editor.”_ This is the sentence that started it all. A user wanted to export a number of colorful Canva slides to a video file. I just recently joined Canva's video group and thought this might be a great starter task. I mean, we’re talking about converting a bunch of images to a video and apparently, there’s a minor color space issue. At least that’s what I thought, without really grasping the complexity behind color spaces. Oh gosh, what had I done!

My first naive approach was, of course, to find out whether someone else on the internet had the same or a similar problem. Luckily, my amazing team gave me a good place to start. “Just try to convert an image to a video in the Rec. 709 color space using FFmpeg and you’ll see what the problem is.” We’ll talk about what Rec. 709 is later in the article.

After a bit of googling, I discovered the following excellent blog post: [Talking About Colorspaces and FFmpeg⁠(opens in a new tab or window)](https://medium.com/invideo-io/talking-about-colorspaces-and-ffmpeg-f6d0b037cc2f). Luckily, the post didn’t just talk about how to transform color spaces with FFmpeg but also highlighted a similar issue about pale videos generated using images. The following command was supposed to fix it all.
    
    
    ffmpeg -i img%03d.png -pix_fmt yuv420p \
    
      -vf colorspace=all=bt709:iall=bt601-6-625:fast=1 \
    
      -colorspace 1 -color_primaries 1 -color_trc 1 video.mp4

Copy

I had one minor and one big issue with this command. My minor issue was that even though the command helped make my video look slightly better, it was still a bit brighter and weaker in terms of colors compared to how it should look. My big issue was that I had no clue what it does! What is color space `1`? And what are primaries? And if I ask what a `trc` is, will everyone laugh at me? So, I started digging deeper to find out what exactly was happening here, why we have to use these exact values, and if there was a chance to make our videos look even better.

In the following sections, I’d like to share my learnings with you and hope you’re as amazed by this domain as I am. Part I is to help you understand how we perceive colors. In Part II, we’ll look into color spaces before diving into FFmpeg-specific color transformations in Part III.

## Part I: A quick detour into biology and human vision

As a software engineer, I love clearly defined functions and their boundaries, predictable outcomes, and derivable numbers. This is one reason why I always avoid less stable or predictable sciences such as biology. But, it turns out, this time, we can’t escape. The design of color spaces, image compression, and storage is just too close to the biology of human vision, so we can’t ignore it. So, before we start looking into color spaces, let’s quickly detour into the world of biology and find out how the human eye perceives colors and lights.

### Sorry, but you’ll never know how a real green looks like

Light comprises photons that move with specific wavelengths toward our eyes. Our eyes have cone cells (S, M, and L cone cells, to be precise) that pick up different wavelengths of light. The following diagram shows that the S-cone cells pick up the short wavelengths, which make up the blue colors, the M cones, which pick up the green colors, and the L cones, which pick up the red colors. I like to use the mnemonics S=short, M=medium, and L=large wavelengths to remember all of this.

![Different cones in our eyes pick up different color frequencies.](https://www.canva.dev/_next/static/media/cones.7f5854f4.jpg)

Different cones in our eyes pick up different color frequencies, image by Vanessa Ezekowitz, [CC BY 3.0 Creative Commons — Attribution 3.0 Unported — CC BY 3.0⁠(opens in a new tab or window)](https://creativecommons.org/licenses/by/3.0), from [wikipedia.org/wiki/LMS_color_space⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/LMS_color_space).

Note that the diagram data is normalized, meaning it doesn’t accurately represent the sensitivity of our cells for each of the wavelengths, which brings me to another interesting point. Your eyes are pretty biased when it comes to color. Your S cones are much less sensitive than your M cones, which means you need many more photons for the blue light to make a blue light look as bright as a green light. Similarly, your L cones are slightly less sensitive than your M cones. You might have noticed in the past that, in a color diagram, green always seems to look the brightest. This is no coincidence.

Obviously, you can “see” more than these three colors. Your brain helps you to turn any combination of signals within this wavelength range into a color, including multiple wavelengths at once (but more on this later).

You might have noticed something interesting here. If I wanted to show you something green, I would have to pick something that emits or reflects light with a wavelength of about 550 nanometers. Although you’d see a green color, your L cones, responsible for the red colors, still contribute. I can't generate a wavelength that triggers only a single cone type in your eye. In theory, a pure green that wouldn't trigger any other cones is called hyper-green. Unfortunately, it’s impossible for me to show you what it would look like.

You might also be wondering, what’s up with the colors below approximately 400 or above 700 nanometers? The short answer is you can’t see them. Except if you’re a Predator from the 1987 movie, in which case you might be able to see infrared, which is the red following our “reddest” visible red at 700 nanometers. On the other side, things don’t look much better for us humans, because we can’t see ultraviolet light either. At least not directly. Remember the fancy black lights installed in clubs and bars, and the phosphors in your shirt which turned these UV-A waves below 400 nm into the most amazing colors? This is one trick to make them visible but you can't see the UV lights at their original wavelengths.

### You prefer the dark side

Your vision isn’t linear. An interesting aspect of human vision is that you can differentiate shadows and darker areas much better than brighter ones. This is an aspect to remember when we talk about gamma correction later. From a software engineering perspective, you could say that if you wanted to store a picture, you’d need a lot more space on your disk for the darker colors than for the brighter ones because you have to visualize a lot more dark grey tones than bright ones.

### Your eyes seem to care more about brightness than color

You might not be old enough to remember black and white TVs. I was pretty young when these were around, but I remember being quite happy watching some of my favorite kids shows on these. Black and white televisions essentially only show brightness, and it worked. Have you ever thought about watching TV on a device that only shows different colors but all with the same brightness? Believe me, the experience wouldn’t be great. This is because our human eye seems to have a higher resolution for brightness than for color. This comes in handy when we talk about chroma subsampling later, where we reduce the color information we store but keep as much of the brightness information as possible.

## Part II: What is a color space and why do I need it?

Now that we know how we can see things let’s think about how we can make others see things the same way we do.

Imagine you have a day off, it’s a beautiful day, and you decide to enjoy the amazing weather at the ocean. Of course, you want to share this experience with your friends and colleagues, or maybe you want to make them jealous. Either way, you take out your mobile phone to take a picture of the beautiful ocean and send it to your friends. In the evening, you’re reminiscing about the beautiful day, watching the picture you took on your shiny new smart TV, which you finally got for Christmas. (I have to admit, this example is a little far-fetched. I mean, who gets a smart TV for Christmas? Anyway, let’s get to the point.)

Why does the picture on the mobile phone look pretty much identical to the picture on the smart TV? And for your friends and colleagues, all using different devices to view your ocean picture, how can you be sure that it looks the same for them? I mean, the ocean is blue, right, but what exactly is blue? How does it get stored, and how does my smart TV know what kind of blue the ocean is? Is it dark blue? Light blue? Ocean blue? As a software engineer, I know I can represent images pixel by pixel using a combination of red, green, and blue (RGB values), each having a value between 0 and 255. So [R=0,G=0,B=255] represents a pretty strong blue and potentially one color in my ocean picture. But how blue exactly is [0,0,255]? This is where color spaces come in.

A color space defines the range of colors you’re allowed to use. It also tells us exactly how blue the ocean in our picture should be. Different devices might support different color spaces, and different color spaces might define different color ranges. If we’re unlucky, our ocean blue might not be part of a specific color space. Luckily, we can transform between different color spaces to make things look as close to our original scene as possible. Now you might ask how this is possible. Wouldn’t we need a reference color space for that? A system that includes all possible colors and where we can map our color spaces into? And you’re right. This is where CIE 1931 comes in.

### CIE 1931 for all visible colors, and more

Long before people started googling FFmpeg filter chains, in 1931, the Commission on Illumination (Commission Internationale de l'éclairage, aka CIE) came up with a chromaticity diagram that included all visible colors at their maximum luminance (don’t worry about the term luminance yet, more on this later).

![The CIE chromaticity diagram.](https://www.canva.dev/_next/static/media/cie-chromaticity.74ba98f0.jpg)

The CIE chromaticity diagram, Image provided by BenRG to Public Domain, from [wikipedia.org/wiki/CIE_1931_color_space⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/CIE_1931_color_space).

You might have seen this diagram before. The area within the horseshoe shape represents all colors visible to the human eye, and you can start using it to define the boundaries of your own color space. In practice, this diagram can’t show you all the colors, but more about this later. What you see in this diagram is essentially a flattened plot of the CIE XYZ color space. First, let’s talk about how we got here.

Unfortunately, the construction of this diagram wasn’t as simple as it seems, at least not in 1931. It started with experiments involving humans trying to match different possible colors, which can be produced using a single wavelength by only using three lights, a red, a green, and a blue one. The amount of red, green, and blue required to match a light of a specific wavelength was added to the chromaticity diagram, which ended up having this horseshoe-like shape (please ignore the triangle around the space for now):

![The CIE 1931 primaries.](https://www.canva.dev/_next/static/media/cie-original-measurements.65e78377.jpg)

CIE 1931 primaries, from [wikipedia.org/wiki/CIE_1931_color_space⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/CIE_1931_color_space).

Notice the numbers around the horseshoe. They represent the wavelength for each color on the edge of this shoe. Here's a fun fact, all outer colors, except for the bottom ones, are essentially the colors of a rainbow. All other colors within the shape are combinations of the outer colors. So if someone tells you they saw magenta in a rainbow, they’re either lying to you, or they saw the colors of the rainbow combined with other colors that happened to be in the scenery, such as the evening sky or even a second rainbow.

Another interesting aspect of this diagram is that some color coordinates are negative. This is because some colors can’t be matched by adding red, green, and blue together. You have to remove a color to get a match (in practice, this was done by adding the color to the matching light). We could stop here and use this coordinate system to draw in our color space boundaries, but then we’d have to deal with negative values when defining the color space.

To fix this, the CIE transformed (squeezing and stretching) this space into the one I showed you in the first CIE diagram, containing only positive values. Interestingly, the CIE picked three impossible colors, Cr, Cg, and Cb, to make this linear transformation happen. But why? Remember that we said we want every color to be representable by some red, green, and blue values? If you’d have picked three colors from within the horseshoe shape, you'd have never been able to generate all colors without exceeding the space boundaries. Try it yourself; draw any triangle into the CIE 1931 diagram, and you’ll see that you’ll not be able to fit all possible colors into your triangle.

We’re almost there, I promise. What we have now is the so-called CIE XYZ color space. This is like the foundation for all possible color spaces, and you’ll even see this one again later when we talk about FFmpeg. So how do you define a color space? Simple, draw a triangle into the CIE diagram (there’s more, actually, but for now, this will do it).

![A color space defined in the coordinates of the CIE XYZ color space.](https://www.canva.dev/_next/static/media/a-colour-space.04952dcc.jpg)

A color space defined in the coordinates of the CIE XYZ color space, image by Sakurambo, [CC BY-SA 3.0 Creative Commons — Attribution-ShareAlike 3.0 Unported — CC BY-SA 3.0⁠(opens in a new tab or window)](https://creativecommons.org/licenses/by-sa/3.0), from [wikipedia.org/wiki/Rec._709⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Rec._709).

That’s it. By drawing a triangle into the CIE XZY color space, you just defined something called primaries, an essential property of your color space. The primaries define the exact boundaries of your space. In this case, we picked R=[x:0.64, y:0.33], G=[x:0.30, y:0.60], and B=[x:0.15, y:0.06]. In theory, you could have picked any three points in the CIE XYZ color space, but it’s pretty common to pick some value for blue, some for green, and some for red for most color spaces you're dealing with.

Are you curious about the dot in the middle with the label “D65”? This is called a white point to define what’s white in our color space and is another important property of our color space. Different color spaces might consider different colors as “white”. In our diagram, we picked a pretty common one, approximately a daylight white that sits at [x:0.3127, y:0.3290], with a light temperature of 6500 Kelvin (which also explains the 65 in D65).

I have to admit that the values we picked here are not entirely random. They’re taken from the Rec. 709 color space, which we’ll look into later.

### Gamma correction

You might remember from Part I of this blog post that our human vision isn’t linear. Unfortunately, the rules for camera sensors are a bit different. A camera might indeed see our nice ocean picture very linearly. But what does this mean? As you can see in the diagrams below, the human eye is very sensitive in low-light areas. It needs fewer photons to perceive something as, let’s say, 20% bright but also a lot more energy to perceive something as twice as bright. In practice, this is a good thing. We won’t go crazy when leaving a dark room to grab a coffee on a sunny day and we can take in the beautiful nature around us without any problem. The camera, however, keeps it simple. It just needs 50% of photons to make something look 50% bright and twice the amount of energy to make something appear twice as bright.

![Gamma correction - camera sensor vs human vision vs CRT screens.](https://www.canva.dev/_next/static/media/gamma-correction.fe88eab0.png)

Gamma correction - In contrast to a common camera sensor, the human vision and CRT screens don't handle light linearly.

So what would happen if we viewed our unprocessed, linear ocean picture on an old CRT (cathode-ray tube) monitor? I deliberately chose a CRT monitor here because they need gamma correction. Coincidentally, CRT screens share a very similar behavior with the human eye, just the other way around, essentially inverting the eye’s gamma curve. You can see in the diagram that it requires a high voltage to reach 50% brightness. So if we’d just send our unprocessed linear image to this monitor, it would look quite dark because it needs a lot more energy than the camera image indicates. But why am I talking about old CRT monitors here? Haven’t we moved on from them? In fact, when it comes to this behavior, we haven’t really. Newer LCD screens still implement this behavior, and it’s actually not too bad, as we’ll find out later.

But for now, what can we do to fix this? It's easy. We apply a transformation to our image so that it has an inverse brightness curve compared to the curve of our eye. Therefore, the final image on our screen has a linear brightness. This is also called gamma correction.

We said earlier that to make the human eye happy, we need more data/bits for the darker areas of a picture than for the brighter ones. By applying the inverse transformation before storing the final image on our phone, we can have both: an auto-corrected image and more details in the darker area. This is because the inverse function quickly pushes our darker values into the brighter space, allowing us to save all shades in a manner our eye considers nice and evenly distributed.

And why did I tell you all of this? What does this have to do with color spaces? To plot the graphs above, I cheekily used an exponent of 2.5 (or 1/2.5). So I calculated y = x^(1/2.5) for all brightness values x between 0 and 1, meaning I applied a gamma correction value of 1/2.5, which is pretty close to how your eyes work. Other gamma values might be a better choice for some devices and use cases. Think about an old movie theatre projector, for example. The bottom line is there isn’t one gamma function. _Different color space standards might define different functions for their gamma correction_. These functions are often referred to as transfer characteristics (trc) or transfer function. They don’t necessarily have this simple form, and many functions are a combination of linear and exponential functions, implementing various thresholds. When we transform between different color spaces later, we have to take this into account.

If you’d like to learn more about this topic, I highly recommend checking out [Unravel | Understanding Gamma⁠(opens in a new tab or window)](https://www.unravel.com.au/understanding-gamma) and [Understanding Gamma Correction⁠(opens in a new tab or window)](https://www.cambridgeincolour.com/tutorials/gamma-correction.htm). Both are excellent articles on this topic.

### Does it always have to be red, green, and blue? What about YUV and Y’CbCr?

So far, we’ve defined the colors in our color space using some combination of red, green, and blue. But aren’t there other ways to represent color? Y’CbCr is probably one of the most common alternatives. Instead of using red, green, and blue, Y’CbCr uses Y' to represent the luma value of a color (the brightness) and the chroma values Cb and Cr to represent the color. Let’s have a closer look.

Before explaining things further, it’s worth noting we can transform any of our RGB color values into Y’CbCr values using the following equations:

  * Y' = 0.299R + 0.587G + 0.114B
  * Cb = -0.168935R - 0.331665G + 0.50059B
  * Cr = 0.499813R - 0.418531G - 0.081282B



If you’re now even more confused, I was too when I saw this the first time. And what makes it more confusing is that different sources have different equations. In fact, I simplified this equation slightly. For example, Y’CbCr commonly expects Y' to be in a limited range between 16 and 235, whereas the value produced here is unscaled, between 0 and 255. But let’s ignore scaling for now. We’ll talk about ranges in a later section.

Instead, let’s have a look at what’s happening here. So Y', our brightness value, combines all three RGB values. The coefficients for our RGB values (0.299, 0.587, and 0.114) are called luma coefficients (you can think of them as weights). The coefficients can usually be mathematically derived from the color space primaries and white point. However, not all color space standards follow this and might use slightly different coefficients. The little prime symbol (') in Y' actually matters. It means we’re working with gamma-corrected RGB data, not linearised data. If you don’t know what I’m talking about, look back at the previous section on gamma correction.

The values for Cb and Cr look even more confusing, even containing negative values. However, things get a little easier when you look at YUV. Y’CbCr and YUV are often used interchangeably (even in the FFmpeg’s code base), but technically, they're different. YUV is something from our good old analog television world. In YUV, or Y’UV to be exact, U and V have the following definitions:

  * U = B - Y'
  * V = R - Y'



So all we’re doing is subtracting our luma (brightness) value from our blue and red values. That looks a lot simpler. And if you re-arrange the equations a little, you’ll see that Y', U, and V provide enough information to determine our original RGB values. Y’CbCr is based on this Y’UV representation but goes a step further. To get Cb and Cr for our Y’CbCr representation out of the Y’UV one, we’re essentially just squeezing the U and V values into a range of 16-240. This is explained in detail in [About YUV Video - Win32 apps⁠(opens in a new tab or window)](https://learn.microsoft.com/en-us/windows/win32/medfound/about-yuv-video) and is outside the scope of this blog post.

You’ll often find the conversion equations nicely packed into a 3x3 matrix you can multiply with the RGB values. If you want to learn more about this topic, I recommend checking out [About YUV Video - Win32 apps⁠(opens in a new tab or window)](https://learn.microsoft.com/en-us/windows/win32/medfound/about-yuv-video) and [[MS-RDPRFX]: Color Conversion (RGB to YCbCr)⁠(opens in a new tab or window)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rdprfx/b550d1b5-f7d9-4a0c-9141-b3dca9d7f525).

### Oh yeah, and then there’s color ranges

Remember earlier when I said RGB values are usually between 0 and 255? It turns out this isn’t always true. In fact, many videos contain RGB values between 16 and 235 (for example, most Rec. 709 HD content). In this case, 16 is the darkest black, and 235 is the brightest white. This is called either full range or limited range and was again done for historical reasons. I don’t want to dive too deep into this, but if you’re curious, I recommend the following article [Full RGB vs. Limited RGB: Is There a Difference?⁠(opens in a new tab or window)](https://www.benq.com/en-au/knowledge-center/knowledge/full-rgb-vs-limited-rgb-is-there-a-difference.html).

What’s important to know for our use case is that most images are encoded in full range, whereas our expected Rec. 709 video output should be in limited range. If we forget to take range conversion into account, our video might look a little washed out.

### So what makes a color space?

If you've made it this far, you pretty much have all the tools you need to define your own color space. We talked about how you can define the colors for your space, the expected gamma correction, and even what factors you should use to transform the colors of your space from RGB to YUV or Y’CbCr. So in summary, to create your own color space, you need to define:

  * A bunch of primaries (preferable red, green and blue except you want to confuse people)
  * A white point
  * A transfer function / gamma correction



Additionally, if you define your own color space standard, with the expectation that your color values get represented in YUV or Y’CbCr, you might want to define the expected luma coefficients to (these can be mathematically derived but don’t have to be).

At this point, I must admit that I've kept things simple and hidden a few things from you. Some video standards that include a color space definition define many more properties, including frame rate, bit depth per pixel, and more. Because these are less relevant to us, I decided to keep these out of the scope of this document. Now, let’s have a look at some actual color spaces.

### sRGB - let’s talk about our first actual color space

The sRGB color space is probably one of the most famous color spaces. It's the default color space for many of the pictures you’ll find online and is probably what your screen is optimized for.

You can find the primaries, the transfer function, the white point, and the luma coefficients on the Wikipedia page for [sRGB⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/SRGB), so there’s no need for me to repeat them in this blog post.

However, I want to mention an interesting fact about this color space. sRGB is very similar to Rec. 709 (which we’ll discuss in a second) in that it uses the same primaries and white point and, therefore, the same luma coefficients. However, it's a little confusing because it defines its transfer characteristics. While researching this topic, I noticed that the two spaces are often treated as equal without considering the gamma correction, which leads to outputs that look slightly off.

One more fun fact before we move on. When looking at the sRGB primaries, you’ll realize I lied when I showed you the CIE 1931 diagram. As I mentioned before, your screen can probably show you colors that live close to the sRGB space. But it can’t show you what’s outside its little triangle. In fact, and this might be disappointing, no RGB screen in the world can show you the entire CIE 1931 diagram. Remember the primaries for CIE XYZ? They’re impossible colors that no device can emit.

### Rec. 709

Let’s look at one more color space. [Rec. 709⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/Rec._709), also known as BT.709 or ITU 709 (just to make you remember more acronyms) is used for HD video material. I’m mentioning this color space because it's our default export color space for videos at Canva.

The Rec. 709 primaries, white point, transfer function, and luma coefficients can all be found on Wikipedia, so we don’t need to dive into this again. It is worth highlighting that Rec. 709 and sRGB share the same primaries. However, their transfer functions and luma coefficients differ.

### Converting between color spaces

From the introduction of this blog post, you might remember that I’m trying to convert an sRGB PNG image into a Rec. 709 video. This brings us to the next topic, color space transformations. As the name suggests, a color space transformation is a transformation of color values from one color space into another color space. Let’s take a step back and consider why and when these transformations are necessary.

Each color space is designed for a different purpose. For example, you might have an HD video optimized for your Rec. 709 TV display. What if you wanted to play this video on an SD TV? To ensure everything looks OK even on your SD display, you might want to convert your video into one with the Rec. 601 color space. Similarly, when you’re watching a video in a different color space than the one supported by your display, you might want your video player to do the required conversions for you.

But how do you transform a color from one color space into another? You might remember the CIE XYZ color space where we said this is like a super color space, able to represent any visible color (and even more) from any space. The good news is that each common color space defines a conversion matrix to and from CIE XYZ. Unfortunately, we can’t apply this matrix with our de-linearised (gamma-corrected) input, so we must first linearise the data. It’s easiest to do this transformation with RGB data. So in case you only have Y’CbCr data lying around, you’ll want to transform it to RGB first. This leaves us with the following steps to convert a color _CA_ from one color space _A_ to another color _CB_ in space _B_ (this is just one possible way, of course):

  1. Convert the Y’CbCr values of color _CA_ to RGB using the luma coefficients for _A_ (skip this step if you already have RGB data).
  2. Linearise _CA_ using the transfer characteristics for _A_.
  3. Transform _CA_ to CIE XYZ using the CIE XYZ transformation matrix for _A_.
  4. Transform CIE XYZ to _CB_ using the CIE XZY transformation matrix for _B_.
  5. De-linearise _CB_ using the transfer characteristics for _B_.
  6. Scale your RGB range (if your input and output ranges are different, for example, from limited to full).
  7. Convert RGB of _CB_ to Y’CbCr using the luma coefficients for _B_ (skip this step if you don’t need a Y’CbCr data stream, but for Rec. 709, you probably want Y’CbCr values).



Now you know how to convert colors from one color space to another. At least in theory. Luckily, FFmpeg is doing this work for us, so we only have to specify the different properties of our color space. Before diving into FFmpeg, though, let’s quickly clarify how the colors spaces are stored.

### Where is color space information stored?

It's important to remember that the RGB or Y’CbCr information of your image doesn’t reveal what color space they belong to. So if someone tells you, “My new push bike has the color R=24, G=55, B =255.”, you need to ask, “What color space are we talking about?”.

At the beginning of this section, we asked how our friends' TVs and mobile phones know how to present the picture of our day at the ocean. Color spaces help us ensure that the target devices know exactly what colors to use when presenting an image and apply the required transformations. But where is this color space information stored? The answer to this question is it depends.

Different file formats have different support for meta information. PNG, for example, has a special so-called “chunk” that can embed a color profile. The mp4 video container format contains something similar, a so-called “colr” atom, which stores primaries, transfer functions, and so on. Unfortunately, there’s no guarantee that this meta information around the color space is actually available. You could, for example, generate a picture or a video without adding any color information at all. In this case, the image viewer or video player will probably run a best-effort attempt and guess the color space, which doesn’t always yield the best results.

### A quick note on chroma subsampling

I left this to last in this section because chroma subsampling doesn’t fit well into the domain of color spaces. But as we’re using it in our FFmpeg command (`-pix_fmt yuv420p`), we should at least quickly clarify what it is.

Remember we said that when it comes to resolution, your eyes are much less fussed about lower color resolutions as long as the brightness resolution is sufficient? This is a property leveraged by chroma subsampling. Color models, such as Y’CbCr, make it easy for us to separate chroma from luma or brightness information. Remember, the brightness being exclusively in the Y'? Now we can use the fact that our eyes and brain care less about the color value for each pixel and are more interested in a high resolution of luma values. How, you ask? Simple, we combine the chroma values for a bunch of neighboring pixels, effectively reducing the resolution, and at the same time, keeping the luma values in their high resolution. For example, if we have 2 pixels, _p1_ and _p2_ , we keep _Y’p1_ and _Y’p2_ separate but we combine _Cbp1_ and _Cbp2_ as well as _Crp1_ and _Crp2_ into only two chroma values _Cbp12_ and _Crp12_. We saved 2 data points by doing this.

In my example, I decided to combine 2 pixels, but there are many different ways you can accomplish this. You’ll often see acronyms like yuv422 or yuv420. These are short for different ways to combine pixel information, and they define exactly how to combine two lines of pixels. For example, yuv**422** says, “take **4** pixels, in the first line and combine **2** of them into 1, in the second line combine **2** of them into 1”. yuv**420** says, “combine **4** pixels, take **2** pixels from the first line, take **0** pixels from the second line and combine them into 0”. yuv420 essentially combines the chroma information for 4 different pixels (2 in each line) into only 2 pixel values. The number of lines that chroma subsampling affects is always 2 in these cases. It might be a bit confusing, but this 2 is not contained in the acronym.

There are many other ways to combine pixels for chroma subsampling and even more details on storing and transferring the pixel data. However, this is out of the scope of this document and isn't required to understand our FFmpeg color space transformation examples.

### Part II summary

We opened this section with the question of how we can make sure our friends and colleagues can enjoy our nice ocean picture on their devices with the same beautiful colors as we do. We learned how color spaces help us and our devices achieve this. We also learned that color space standards define several things, such as primaries, white point, gamma correction, and more. Of course, there’s no guarantee that your friends' devices will follow all the color space definitions we defined so passionately in our ocean picture. But at least we gave it our best.

This should give us enough input to convert color spaces with FFmpeg. By now, you probably have a general idea of what our initially confusing FFmpeg command at the beginning of this blog post is doing. If not, don’t worry. We’ll get to it.

I want to emphasize again that I'm only touching the surface on color spaces. There’s a lot more interesting stuff to learn. If you’d like to dig deeper into color spaces in general, I recommend the following excellent articles: [Unravel | Understanding Color Spaces⁠(opens in a new tab or window)](https://www.unravel.com.au/understanding-color-spaces) and [The Hitchhiker's Guide to Digital Colour⁠(opens in a new tab or window)](https://hg2dc.com/).

## Part III: Color space conversion with FFmpeg

Now that we have all the theory to convert some color spaces with FFmpeg, this third part of my blog post examines how we can do it.

Our use case is to convert an sRGB PNG file into a Rec. 709 video. Here again is the initial FFmpeg command I found in [Talking About Colorspaces and FFmpeg⁠(opens in a new tab or window)](https://medium.com/invideo-io/talking-about-colorspaces-and-ffmpeg-f6d0b037cc2f)
    
    
    ffmpeg -i img%03d.png -pix_fmt yuv420p \
    
    -vf colorspace=all=bt709:iall=bt601-6-625:fast=1 \
    
    -colorspace 1 -color_primaries 1 -color_trc 1 video.mp4

Copy

Note that the input files in the linked blog might differ from ours, so we have to verify if these parameters make sense for us. Let’s quickly walk through some of these parameters:

  * `-pix_fmt yuv420p`: We’d like a yuv420p chroma subsampling.
  * `-vf colorspace=all=bt709:iall=bt601-6-625:fast=1`: We’d like to use the `colorspace` filter, the output is set to Rec. 709 (or BT.709 as we learned earlier), and the input is Rec. 601 (aka BT.601, essentially SD material). Let’s talk about `fast=1` in a second.
  * `-colorspace 1 -color_primaries 1 -color_trc 1`: These parameters add the meta information for the selected color space to the output video. It’s important to note they don’t change anything about the video content itself, so they don’t transform the color space of the video. This is the task of the `colorspace` filter. As you might have already guessed, the `1` behind each of these parameters maps to Rec. 709. internally.



In the following sections, we'll review the main color space properties and see what parameters and values best apply to our use case.

### The primaries

So, what primaries should we be using? Our input is an sRGB PNG, so we should use sRGB primaries. And for the output? Easy, we’re going to use Rec. 709 primaries. Let’s look at the original filter definition.
    
    
    colorspace=all=bt709:iall=bt601-6-625:fast=1

Copy

The output looks good, set to BT.709, the same as Rec. 709. How about the input? This doesn’t work in our scenario. The Rec. 601 color space is different from the sRGB color space. It's also worth mentioning that we don’t want to do a fast conversion. Why? Let’s have a look at what the filter documentation says about the fast parameter: _“Do a fast conversion, which skips gamma/primary correction.“_. Let’s think about this, could we skip the primary and gamma corrections? Remember, the sRGB and Rec. 709 primaries are the same, so we should be fine with the primaries selection. Unfortunately, the function used for the gamma correction in both standards differs. Therefore, we have to remove the `fast` parameter.

My naive past self thought, let’s give the following a try (because it totally makes sense right?).
    
    
    colorspace=all=bt709:iall=srgb

Copy

And this is what I got.

![FFmpeg output shows error due to invalid color space selection](https://www.canva.dev/_next/static/media/ffmpeg-error.9f2f8196.png)

Some higher power doesn’t want me to use the sRGB color space as an input. And to be honest, this error message doesn’t tell me why. Looking at the documentation, it seems that for the `iall` parameter, we can only choose one of the following values: `bt470m`, `bt470bg`, `bt601-6-525`, `_bt601-6-625`, `bt709`, `smpte170m`, `smpte240m`, or `bt2020`. So it looks like what we need is just not there.

But all is not lost. Remember what I said earlier about sRGB using the same primaries, white point, and therefore luma coefficients as Rec. 709, but a different gamma function? Luckily, the colorspace filter allows us to define all these properties individually (at least indirectly). So, let’s start by explicitly defining our input primaries.
    
    
    colorspace=all=bt709:iprimaries=bt709

Copy

As you can see, I dropped the `iall` parameter for now and replaced it with `iprimaries`. At this point, I'll mention that the `all` parameter is a bit confusing. I initially assumed that `all` set defaults for the input and output parameters. However, looking at the filter source code, it seems that `all` defines just the output color parameters, not the input ones. `iall` defines the input parameters and other parameters having the `i` prefix. And by the way, you can use the `iprimaries` parameter in conjunction with `iall`, in which case, `iprimaries` overrules whatever primaries `iall` would have defined.

### Gamma correction and TRC

Now that we've defined our primaries, let’s look at how to apply a gamma correction. Unfortunately, sRGB and Rec. 709 use different functions for gamma correction. But this time, we’re in luck because the `colorspace` filter directly supports our sRGB transfer function and is as easy as the following.
    
    
    colorspace=all=bt709:iprimaries=bt709:itrc=srgb

Copy

### Luma coefficients

This is a confusing one. To begin with, no parameter looks like it would explicitly define luma coefficients. As we talked about before, the luma coefficients should be mathematically derived from primaries and white point. Still, some standards might define different values, and I wanted to be sure we're picking the correct values. So, being a little desperate, I checked out the FFmpeg source to see how the luma coefficient selection works internally. It turns out the coefficients are selected purely based on the `space`/`ispace` parameters. And we should be fine using these, provided we overwrite other color space properties that don’t apply to us, such as `trc`.

Similar to the primaries, there’s no space parameter for sRGB. Looking at the documentation, we can only select one of the following color space values: `bt709`, `fcc`, `bt470bg`, `smpte170m`, `smpte240m`, `ycgco`, or `bt2020ncl`. Because sRGB and Rec. 709 share the same primaries and white point, we can safely fall back to the Rec. 709 color space again to make the filter use the correct luma coefficients.
    
    
    colorspace=all=bt709:iprimaries=bt709:itrc=srgb:ispace=bt709

Copy

### Color range

Defining the range property almost drove me crazy! Remember, sRGB and Rec. 709 use different color ranges. For Rec. 709, an RGB value of [R=16, G=16, B=16] is absolute darkness, whereas for sRGB, it’s [R=0, G=0, B=0]. The `colorspace` filter allows us to define input and output color ranges using the `irange` and `range` parameters. You can use the `tv` value to define a limited range, whereas you can use the `pc` value to define a full range. Since we’re converting a full range sRGB PNG image to a limited range Rec. 709 video, this should be the filter expression, right?
    
    
    colorspace=all=bt709:iprimaries=bt709:itrc=srgb:ispace=bt709:range=tv:irange=pc

Copy

Oh, how wrong I was. The correct answer is the following.
    
    
    colorspace=all=bt709:iprimaries=bt709:itrc=srgb:ispace=bt709:range=tv:irange=tv

Copy

Alternatively, you can drop the range definition altogether. Are you as confused as I was? Check out the next section to find out exactly why this is happening.

### FFmpeg adds a scale filter without telling you

That I could skip the color range transformation without knowing why bothered me a lot. I wanted to find out exactly what was happening, so I started compiling my own version of FFmpeg with additional debug information. As it turns out, there’s a lot more going on than I initially thought.

When looking at the `colorspace` filter source, I discovered the following code snippet.
    
    
    static int query_formats(AVFilterContext *ctx)
    
    {
    
        static const enum AVPixelFormat pix_fmts[] = {
    
            AV_PIX_FMT_YUV420P,   AV_PIX_FMT_YUV422P,   AV_PIX_FMT_YUV444P,
    
            AV_PIX_FMT_YUV420P10, AV_PIX_FMT_YUV422P10, AV_PIX_FMT_YUV444P10,
    
            AV_PIX_FMT_YUV420P12, AV_PIX_FMT_YUV422P12, AV_PIX_FMT_YUV444P12,
    
            AV_PIX_FMT_YUVJ420P,  AV_PIX_FMT_YUVJ422P,  AV_PIX_FMT_YUVJ444P,
    
            AV_PIX_FMT_NONE
    
        };
    
        // ... more setup

Copy

To give you some context, each FFmpeg filter can define the kind of inputs it accepts in a function called `query_formats`. Do you notice something peculiar about this one? Our `colorspace` filter doesn't support RGB inputs. So how could it take in our PNG image, which is obviously provided in RGB? As it turns out, FFmpeg adds in a `scale` filter that converts our RGB data to YUV for us. If you run FFmpeg with `-report`, you can see this happening.
    
    
    [Parsed_colorspace_0 @ 0x7f7f8cf04b80] auto-inserting filter 'auto_scale_0' between the filter 'graph 0 input from stream 0:0' and the filter 'Parsed_colorspace_0'

Copy

Remember from our earlier sections that to transform to YUV/Y’CbCr, you need luma coefficients for the corresponding color space. Unfortunately, FFmpeg’s PNG decoder doesn't evaluate the `colr` chunk, which contains our color space information (fun fact: the encoder does write it). This means the `scale` filter falls back to an unspecified color space. Luckily, the coefficients used for an unspecified color space equal the ones of our sRGB color space. If you’re ever working with a PNG file that’s in a color space different from sRGB, you’ll have to keep this in mind. It’s also worth mentioning that the behavior might differ for different input file formats. In the case of a JPG file, for example, the color space information seems to be parsed and passed on to the filters correctly.

And to make things more confusing, the `scale` filter uses a different representation of the luma coefficients than the `colorspace` filter internally. The `scale` filter uses a representation defined in `yuv2rgb.c`, whereas the `colorspace` filter uses the one in `csp.c`, and both sets of values have a very different structure with different coefficients. The good news is it’s purely a different representation, and they're mathematically equivalent. However, you must keep this in mind when experimenting with your luma coefficients.

Another interesting aspect of the scale filter is that it’s actually a lot more powerful than it pretends to be. I initially thought, “It’s called scale, what can it possible do? Scale something, right?”. It turns out the `scale` filter can do entire color space transformations too. It doesn’t seem able to do gamma correction, but it knows how to deal with primaries and color ranges, for example. And this brings me to the next interesting point. In our scenario, the `scale` filter translated our full range RGB image to a limited range one before passing it on to our `colorspace` filter. I hope this explains why we don’t need the explicit range definition in the `colorspace` filter itself.

### The final FFmpeg command

Here is the final FFmpeg command I used to transform a PNG image into an h264 video in the Rec. 709 color space
    
    
    ffmpeg -loop 1 -i image.png -pix_fmt yuv420p -c:v libx264 -t 1 \
    
      -vf "colorspace=all=bt709:iprimaries=bt709:itrc=srgb:ispace=bt709" \
    
      -color_range 1 -colorspace 1 -color_primaries 1 out.mp4

Copy

And if you want to shorten this a little, you can use the `iall` parameter instead of explicitly defining the `iprimaries` and `ispace` parameters.
    
    
    ffmpeg -loop 1 -i image.png -pix_fmt yuv420p -c:v libx264 -t 1 \
    
      -vf "colorspace=all=bt709:iall=bt709:itrc=srgb" \
    
      -color_range 1 -colorspace 1 -color_primaries 1 out.mp4

Copy

Here's a recap of some of our FFmpeg learnings:

  * `-report` is a handy FFmpeg parameter to get some more insights.
  * If an input is provided in RGB (for example, for PNG files) but a filter requires YUV, FFmpeg silently injects a `scale` filter (`vf_scale`).
  * The `vf_scale` filter does much more than just scaling, such as YUV and color space conversions (without gamma correction).
  * When using the colorspace filter, don’t use `fast=1` if you want gamma correction.
  * The PNG decoder ignores the `colr` chunk on read, leading to an unspecified input color space, whereas the JPG decoder doesn’t. However, the PNG encoder does write the `colr` chunk.
  * `-colorspace 1 -color_primaries 1 -color_trc 1` only set meta color profile information. They don’t cause an actual change to the video.



## Summary

I hope this blog post clarifies what color spaces are, why you should care about them, and how you can use FFmpeg to transform color spaces. If you have any more questions on this topic, please let me know and I’ll try to shed some light on the missing spots. Also, if you find mistakes and feel like things need correcting, please let me know and I’ll get it fixed.

## A quick checklist for when your video looks off

Before I let you go, here's a quick checklist you can use if your generated video looks slightly off in terms of colors:

  * Do the input and output primaries look okay?
  * What about the input and output trc and gamma correction?
  * Have you thought about the ranges?
  * Are the luma coefficients correct? They should if you picked the correct primaries and white point.



## Acknowledgements

I'd like to give special shout outs to [Chris Cook⁠(opens in a new tab or window)](https://www.linkedin.com/in/christopher-cook-aus/), [Bela Babik⁠(opens in a new tab or window)](https://www.linkedin.com/in/belababik/) and [Peter Camilleri⁠(opens in a new tab or window)](https://www.linkedin.com/in/pdcamilleri/) for their support and inspiration on this crazy color space journey.

## Some great links for further reading

Here are some additional sources of information I found useful:

  * [The Hitchhiker's Guide to Digital Colour⁠(opens in a new tab or window)](https://hg2dc.com/)
  * [Unravel | Understanding Color Spaces⁠(opens in a new tab or window)](https://www.unravel.com.au/understanding-color-spaces)
  * [Unravel | Understanding Gamma⁠(opens in a new tab or window)](https://www.unravel.com.au/understanding-gamma)
  * [Understanding Gamma Correction⁠(opens in a new tab or window)](https://www.cambridgeincolour.com/tutorials/gamma-correction.htm)
  * [colorspace – FFmpeg⁠(opens in a new tab or window)](https://trac.ffmpeg.org/wiki/colorspace)
  * [About YUV Video - Win32 apps⁠(opens in a new tab or window)](https://learn.microsoft.com/en-us/windows/win32/medfound/about-yuv-video)
  * [Opponent Color Spaces⁠(opens in a new tab or window)](https://engineering.purdue.edu/~bouman/ece637/notes/pdf/Opponent.pdf).



## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.212d94a6.png)](https://www.canva.dev/blog/engineering/our-journey-to-snowflake-monitoring-mastery/)

[SnowflakeOur journey to Snowflake monitoring masteryHow I learned to stop worrying and love metadata.](https://www.canva.dev/blog/engineering/our-journey-to-snowflake-monitoring-mastery/)

[Rob Scriva⁠(opens in a new tab or window)](https://www.linkedin.com/in/robertscriva/)Nov 12, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.a4baa635.png)](https://www.canva.dev/blog/engineering/functional-completeness-and-local-hermeticity/)

[DevOpsFunctional completeness and local hermeticityMaintaining a functionally complete yet airtight local development environment is something we consider to be of critical importance.](https://www.canva.dev/blog/engineering/functional-completeness-and-local-hermeticity/)

David HearndenMar 25, 2015

[![](https://www.canva.dev/_next/static/media/thumbnail.8c4d6cb8.jpg)](https://www.canva.dev/blog/engineering/trust-but-test/)

[SecurityTrust but test: Vendor security testing at CanvaHow we validate vendor security at Canva by going beyond compliance.](https://www.canva.dev/blog/engineering/trust-but-test/)

[Kane Narraway⁠(opens in a new tab or window)](https://www.linkedin.com/in/kane-n/), [CJ Fairhead⁠(opens in a new tab or window)](https://www.linkedin.com/in/chris-fairhead/)Mar 10, 2024

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


