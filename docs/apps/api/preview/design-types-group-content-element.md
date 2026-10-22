---
url: https://www.canva.dev/docs/apps/api/preview/design-types-group-content-element/
title: GroupContentElement - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T14:42:16.999987+00:00
---

# GroupContentElement - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/api/preview/design-types-group-content-element/

[Overview](https://www.canva.dev/docs/apps/)

Build your first app

[Prerequisites](https://www.canva.dev/docs/apps/prerequisites/)[Quickstart](https://www.canva.dev/docs/apps/quickstart/)

Starter resources

[Starter kit](https://www.canva.dev/docs/apps/setting-up-starter-kit/)[Use a starter template](https://www.canva.dev/docs/apps/app-templates/)[Explore reference apps](https://www.canva.dev/docs/apps/reference-apps/)

Learn

Platform concepts

[Apps](https://www.canva.dev/docs/apps/platform-concepts-apps/)[Designs](https://www.canva.dev/docs/apps/designs/)[Elements](https://www.canva.dev/docs/apps/elements/)[Content](https://www.canva.dev/docs/apps/content/)[Assets](https://www.canva.dev/docs/apps/uploading-assets/)[Folders](https://www.canva.dev/docs/apps/platform-concepts-folders/)[Teams, groups, and users](https://www.canva.dev/docs/apps/platform-concepts-teams-groups-and-users/)[Suspension](https://www.canva.dev/docs/apps/suspension/)

[Recommended practices](https://www.canva.dev/docs/apps/rest-apis/recommended-practices/)

# GroupContentElement

API reference for the GroupContentElement type.

Copy page

An element that can exist in a group element.

## Type declaration

RectRect

ShapesShapes

EmbedsEmbeds

TextText

UnsupportedUnsupported

An element that renders a rectangle.

The rectangle can be filled with image content, video content, or a solid color.

`type``string`Read-only

RequiredView type definition

The element type

The only valid value is `"rect"`.

`fill``Fill`Read-only

RequiredView type definition

Describes how a fill is filled with color or media.

If both `media` and `color` are defined, `media` takes precedence.

For more information, see [Fill](https://www.canva.dev/docs/apps/api/preview/design-types-fill/).

`stroke``Stroke`Read-only

RequiredView type definition

The outline of the rectangle.

For more information, see [Stroke](https://www.canva.dev/docs/apps/api/preview/design-types-stroke/).

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

An element that renders a vector shape.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"shape"`.

`viewBox``AlignedBox`Read-only

RequiredView type definition

The scale and cropping of the shape.

Properties of **viewBox**

`top``number`Read-only

RequiredView type definition

The distance of the shape from the top edge of the element, in pixels.

`left``number`Read-only

RequiredView type definition

The distance of the shape from the left edge of the element, in pixels.

`width``number`Read-only

RequiredView type definition

The width of the view box, in pixels.

`height``number`Read-only

RequiredView type definition

The height of the view box, in pixels.

`paths``ReadableList<Path>`Read-only

RequiredView type definition

The paths that define the structure of the shape.

For more information, see [ReadableList](https://www.canva.dev/docs/apps/api/preview/design-types-readable-list/) and [Path](https://www.canva.dev/docs/apps/api/preview/design-types-path/).

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

An element that embeds rich media, such as a YouTube video.

`type``string`Read-only

RequiredView type definition

The type of content.

The only valid value is `"embed"`.

`url``string`Read-only

RequiredView type definition

The URL of the rich media.

This URL must be supported by the Iframely API.

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

An element that renders text content.

`type``string`Read-only

RequiredView type definition

The only valid value is `"text"`.

`text``RichtextRange`Read-only

RequiredView type definition

Provides methods for interacting with a range of formatted text.

Properties of **text**

`formatParagraph``function`

RequiredView type definition

Formats all of the paragraphs that overlap the given bounds.

  * The `\n` character indicates the end of a paragraph.
  * All paragraphs that overlap the provided bounds will be formatted in their entirety.



**Parameters**

`bounds``Bounds`

RequiredView type definition

The segment of the range on which to apply the formatting.

Properties of **bounds**

`index``number`

RequiredView type definition

The starting position of the segment.

This is zero-based, meaning the first character of the range is at index 0.

`length``number`

RequiredView type definition

The number of characters in the segment, starting from the index.

`formatting``RichtextFormatting`

RequiredView type definition

The formatting to apply to the paragraph(s).

Properties of **formatting**

`color``string`

OptionalView type definition

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`fontWeight``FontWeight`

OptionalView type definition

The weight (thickness) of the font.

The available font weights depend on the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



`fontStyle``string`

OptionalView type definition

The style of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"italic"`



`decoration``string`

OptionalView type definition

The decoration of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"underline"`



`strikethrough``string`

OptionalView type definition

The strikethrough of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"strikethrough"`



`link``string`

OptionalView type definition

An external URL that the text links to.

`fontRef``FontRef`

OptionalView type definition

A unique identifier that points to a font asset in Canva's backend.

`fontSize``number`

OptionalView type definition

The size of the text, in pixels.

  * In the Canva editor, this number is shown as points (pts), not pixels.



**Minimum** : `1`

**Maximum** : `1000`

`textAlign``string`

OptionalView type definition

The alignment of the text.

**Default value** : `"start"`

**Available values** :

  * `"start"`
  * `"center"`
  * `"end"`
  * `"justify"`



`listLevel``number`

OptionalView type definition

The list indentation level of the paragraph.

`listMarker``string`

OptionalView type definition

The appearance of list item markers.

This property only has an effect if `listLevel` is greater than 0.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"disc"`
  * `"circle"`
  * `"square"`
  * `"decimal"`
  * `"lower-alpha"`
  * `"lower-roman"`
  * `"checked"`
  * `"unchecked"`



`lineHeightEm``number`

OptionalView type definition

The line height of the paragraph, relative to the font size expressed in Em.

**Minimum** : `0.5`

**Maximum** : `2.5`

**Default value** : `1.4`

`letterSpacingEm``number`

OptionalView type definition

The spacing between characters, relative to the font size expressed in Em.

  * In the Canva editor, this number is shown as a multiple of 1000.



**Minimum** : `-0.2`

**Maximum** : `0.8`

**Default value** : `0`

**Returns**

`void`

**Examples**

**Format paragraph as a heading**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    
    
    
    range.appendText("Heading Text\nRegular paragraph text.");
    
    
    
    
    // Format just the first paragraph as a heading
    
    range.formatParagraph(
    
      { index: 0, length: 12 }, // Only need to include part of the paragraph
    
      {
    
        fontSize: 24,
    
        fontWeight: 'bold',
    
        textAlign: 'center'
    
      }
    
    );

TYPESCRIPT

Copy

**Create a bulleted list**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    const text = "Item 1\nItem 2\nItem 3";
    
    range.appendText(text);
    
    
    
    
    // Format all paragraphs as a bulleted list
    
    range.formatParagraph(
    
      { index: 0, length: text.length },
    
      {
    
        listLevel: 1,
    
        listMarker: 'disc'
    
      }
    
    );

TYPESCRIPT

Copy

`formatText``function`

RequiredView type definition

Formats a region of text with inline formatting properties.

**Parameters**

`bounds``Bounds`

RequiredView type definition

The segment of the range on which to apply the formatting.

Properties of **bounds**

`index``number`

RequiredView type definition

The starting position of the segment.

This is zero-based, meaning the first character of the range is at index 0.

`length``number`

RequiredView type definition

The number of characters in the segment, starting from the index.

`formatting``InlineFormatting`

RequiredView type definition

The formatting to apply to the text.

Properties of **formatting**

`color``string`

OptionalView type definition

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`fontWeight``FontWeight`

OptionalView type definition

The weight (thickness) of the font.

The available font weights depend on the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



`fontStyle``string`

OptionalView type definition

The style of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"italic"`



`decoration``string`

OptionalView type definition

The decoration of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"underline"`



`strikethrough``string`

OptionalView type definition

The strikethrough of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"strikethrough"`



`link``string`

OptionalView type definition

An external URL that the text links to.

**Returns**

`void`

**Examples**

**Format specific words in a paragraph**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("This text contains important information.");
    
    
    
    
    // Format just the word "important"
    
    range.formatText(
    
      { index: 16, length: 9 },
    
      {
    
        fontWeight: 'bold',
    
        color: '#FF0000'
    
      }
    
    );

TYPESCRIPT

Copy

**Add a link to text**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("Visit our website for more information.");
    
    
    
    
    // Add a link to "our website"
    
    range.formatText(
    
      { index: 6, length: 11 },
    
      {
    
        link: "https://www.example.com",
    
        decoration: 'underline',
    
        color: '#0066CC'
    
      }
    
    );

TYPESCRIPT

Copy

`appendText``function`

RequiredView type definition

Appends the specified characters to the end of the range.

**Parameters**

`characters``string`

RequiredView type definition

The characters to append to the richtext range.

`formatting``InlineFormatting`

OptionalView type definition

Optional formatting to apply to the appended text.

Properties of **formatting**

`color``string`

OptionalView type definition

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`fontWeight``FontWeight`

OptionalView type definition

The weight (thickness) of the font.

The available font weights depend on the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



`fontStyle``string`

OptionalView type definition

The style of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"italic"`



`decoration``string`

OptionalView type definition

The decoration of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"underline"`



`strikethrough``string`

OptionalView type definition

The strikethrough of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"strikethrough"`



`link``string`

OptionalView type definition

An external URL that the text links to.

**Returns**

`bounds``Bounds`

View type definition

A segment of a richtext range.

Properties of **bounds**

`index``number`

View type definition

The starting position of the segment.

This is zero-based, meaning the first character of the range is at index 0.

`length``number`

View type definition

The number of characters in the segment, starting from the index.

**Examples**

**Append plain text**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("First paragraph. ");
    
    
    
    
    // Append more text to the existing content
    
    const result = range.appendText("This is additional text.");
    
    
    
    
    // The bounds of the newly added text are returned
    
    // Do something with the bounds - result.bounds, e.g. { index: 17, length: 24 }

TYPESCRIPT

Copy

**Append formatted text**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("Normal text followed by ");
    
    
    
    
    // Append formatted text
    
    range.appendText("bold red text", {
    
      fontWeight: 'bold',
    
      color: '#FF0000'
    
    });
    
    
    
    
    // Append a new paragraph
    
    range.appendText("\nThis is a new paragraph.");

TYPESCRIPT

Copy

`replaceText``function`

RequiredView type definition

Replaces a region of text with the specified characters.

**Parameters**

`bounds``Bounds`

RequiredView type definition

The segment of the range to replace.

Properties of **bounds**

`index``number`

RequiredView type definition

The starting position of the segment.

This is zero-based, meaning the first character of the range is at index 0.

`length``number`

RequiredView type definition

The number of characters in the segment, starting from the index.

`characters``string`

RequiredView type definition

The replacement characters.

`formatting``InlineFormatting`

OptionalView type definition

The formatting to apply to the replaced text.

Properties of **formatting**

`color``string`

OptionalView type definition

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`fontWeight``FontWeight`

OptionalView type definition

The weight (thickness) of the font.

The available font weights depend on the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



`fontStyle``string`

OptionalView type definition

The style of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"italic"`



`decoration``string`

OptionalView type definition

The decoration of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"underline"`



`strikethrough``string`

OptionalView type definition

The strikethrough of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"strikethrough"`



`link``string`

OptionalView type definition

An external URL that the text links to.

**Returns**

`bounds``Bounds`

View type definition

The bounds of the replacement characters within the updated range.

Properties of **bounds**

`index``number`

View type definition

The starting position of the segment.

This is zero-based, meaning the first character of the range is at index 0.

`length``number`

View type definition

The number of characters in the segment, starting from the index.

**Examples**

**Replace text while maintaining some formatting**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("This text needs correction.");
    
    
    
    
    // Replace "needs correction" with "is correct"
    
    const result = range.replaceText(
    
      { index: 10, length: 16 },
    
      "is correct"
    
    );
    
    
    
    
    // The bounds of the replaced text are returned
    
    // Do something with the bounds - result.bounds, e.g. { index: 10, length: 10 }

TYPESCRIPT

Copy

**Replace text with formatted text**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("Regular text that needs emphasis.");
    
    
    
    
    // Replace "needs emphasis" with formatted text
    
    range.replaceText(
    
      { index: 17, length: 15 },
    
      "is important",
    
      {
    
        fontWeight: 'bold',
    
        fontStyle: 'italic',
    
        color: '#0066CC'
    
      }
    
    );

TYPESCRIPT

Copy

`readPlaintext``function`

RequiredView type definition

Returns the current state of the richtext as plaintext.

**Returns**

`string`

**Examples**

**Extract plain text content**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("First paragraph.\n", { fontWeight: 'bold' });
    
    range.appendText("Second paragraph with formatting.", { color: '#FF0000' });
    
    
    
    
    // Get plain text content without formatting
    
    const plainText = range.readPlaintext();
    
    // Do something with the plain text - plainText, e.g. "First paragraph.\nSecond paragraph with formatting."

TYPESCRIPT

Copy

**Search within text content**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("This text contains a searchable term.");
    
    
    
    
    // Search for a specific word
    
    const plainText = range.readPlaintext();
    
    const searchTerm = "searchable";
    
    const index = plainText.indexOf(searchTerm);
    
    
    
    
    if (index !== -1) {
    
      // Format the found term
    
      range.formatText(
    
        { index, length: searchTerm.length },
    
        { fontWeight: 'bold', decoration: 'underline' }
    
      );
    
    }

TYPESCRIPT

Copy

`readTextRegions``function`

RequiredView type definition

Returns the current state of the richtext as one or more text regions. Each region is an object that contains the text content and its formatting.

**Returns**

`text``string`

View type definition

The plaintext content of the region.

`formatting``Partial<RichtextFormatting>`

OptionalView type definition

The formatting of the region.

Properties of **formatting**

`color``string`

OptionalView type definition

The color of the text as a hex code.

The hex code must include all six characters and be prefixed with a `#` symbol.

**Example**
    
    
     "#ff0099"

TS

Copy

`fontWeight``FontWeight`

OptionalView type definition

The weight (thickness) of the font.

The available font weights depend on the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"thin"`
  * `"extralight"`
  * `"light"`
  * `"medium"`
  * `"semibold"`
  * `"bold"`
  * `"ultrabold"`
  * `"heavy"`



`fontStyle``string`

OptionalView type definition

The style of the font.

**Default value** : `"normal"`

**Available values** :

  * `"normal"`
  * `"italic"`



`decoration``string`

OptionalView type definition

The decoration of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"underline"`



`strikethrough``string`

OptionalView type definition

The strikethrough of the text.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"strikethrough"`



`link``string`

OptionalView type definition

An external URL that the text links to.

`fontRef``FontRef`

OptionalView type definition

A unique identifier that points to a font asset in Canva's backend.

`fontSize``number`

OptionalView type definition

The size of the text, in pixels.

  * In the Canva editor, this number is shown as points (pts), not pixels.



**Minimum** : `1`

**Maximum** : `1000`

`textAlign``string`

OptionalView type definition

The alignment of the text.

**Default value** : `"start"`

**Available values** :

  * `"start"`
  * `"center"`
  * `"end"`
  * `"justify"`



`listLevel``number`

OptionalView type definition

The list indentation level of the paragraph.

`listMarker``string`

OptionalView type definition

The appearance of list item markers.

This property only has an effect if `listLevel` is greater than 0.

**Default value** : `"none"`

**Available values** :

  * `"none"`
  * `"disc"`
  * `"circle"`
  * `"square"`
  * `"decimal"`
  * `"lower-alpha"`
  * `"lower-roman"`
  * `"checked"`
  * `"unchecked"`



`lineHeightEm``number`

OptionalView type definition

The line height of the paragraph, relative to the font size expressed in Em.

**Minimum** : `0.5`

**Maximum** : `2.5`

**Default value** : `1.4`

`letterSpacingEm``number`

OptionalView type definition

The spacing between characters, relative to the font size expressed in Em.

  * In the Canva editor, this number is shown as a multiple of 1000.



**Minimum** : `-0.2`

**Maximum** : `0.8`

**Default value** : `0`

**Examples**

**Get text with formatting information**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("Normal text ", {});
    
    range.appendText("bold text", { fontWeight: 'bold' });
    
    range.appendText(" and ", {});
    
    range.appendText("red text", { color: '#FF0000' });
    
    
    
    
    // Get formatted regions
    
    const regions = range.readTextRegions();
    
    // Do something with the regions, e.g.
    
    // [
    
    //   { text: "Normal text ", formatting: {} },
    
    //   { text: "bold text", formatting: { fontWeight: 'bold' } },
    
    //   { text: " and ", formatting: {} },
    
    //   { text: "red text", formatting: { color: '#FF0000' } }
    
    // ]

TYPESCRIPT

Copy

**Analyze formatting variations**
    
    
     import { createRichtextRange } from "@canva/design";
    
    
    
    
    const range = createRichtextRange();
    
    range.appendText("Mixed ", {});
    
    range.appendText("formatted ", { fontWeight: 'bold' });
    
    range.appendText("text", { color: '#0066CC' });
    
    
    
    
    // Analyze formatting variations
    
    const regions = range.readTextRegions();
    
    const formattingTypes = regions.map(region => {
    
      const formatting = region.formatting || {};
    
      return {
    
        text: region.text,
    
        hasWeight: !!formatting.fontWeight,
    
        hasColor: !!formatting.color
    
      };
    
    });

TYPESCRIPT

Copy

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`

An element that the SDK doesn't support.

`type``string`Read-only

RequiredView type definition

The only valid value is `"unsupported"`.

`width``number`Read-only

RequiredView type definition

A width, in pixels.

`height``number`Read-only

RequiredView type definition

A height, in pixels.

`locked``boolean`Read-only

RequiredView type definition

If `true`, the element is locked and cannot be modified.

`top``number`

RequiredView type definition

The distance from the top edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`left``number`

RequiredView type definition

The distance from the left edge of the container, in pixels.

  * The pixels are relative to their container.



**Minimum** : `-32768`

**Maximum** : `32767`

`rotation``number`

RequiredView type definition

A rotation, in degrees.

**Minimum** : `-180`

**Maximum** : `180`

`transparency``number`

RequiredView type definition

Transparency as a percentage.

**Minimum** : `0`

**Maximum** : `1`
