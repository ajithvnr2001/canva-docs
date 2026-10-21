---
url: https://www.canva.dev/docs/audit-logs/actions/brands/
title: Brands - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:50.287124+00:00
---

# Brands - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/brands/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Brands

Copy page

## Create a Brand Kit

An `actor` triggers this event when they create a new Brand Kit. For details, see [Canva Help: Setting up Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).

`type``string`

**Default value:** `CREATE_BRAND_KIT`

**Available values:** The only valid value is `CREATE_BRAND_KIT`.

`name``string`

Optional

The name of the Brand Kit.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "CREATE_BRAND_KIT",
    
        "name": "Acme Corp Brand Kit"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update a Brand Kit's details

An `actor` triggers this event when they update a Brand Kit. For details, see [Canva Help: Setting up Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).

`type``string`

**Default value:** `UPDATE_BRAND_KIT`

**Available values:** The only valid value is `UPDATE_BRAND_KIT`.

`changed_fields``string[]`

Optional

The fields the `actor` requested changes for in this update.

**Available values:**

  * `NAME`: The name of the Brand Kit.
  * `SHARES`: The shares of the Brand Kit.
  * `FONTS`: The fonts of the Brand Kit.
  * `FOLDER_LINKS`: The links to the Brand Kit folders.
  * `INGREDIENT`: The ingredient of the Brand Kit.
  * `ICON`: The icon of the Brand Kit.
  * `GUIDELINES`: The guidelines design of the Brand Kit.



`old_name``string`

Optional

The previous name of the Brand Kit.

`new_name``string`

Optional

The new name of the Brand Kit.

`old_shares``BrandKitShare[]`

Optional

The shares of the Brand Kit.

TEAMTEAM

FOLDERFOLDER

ORGANIZATIONORGANIZATION

USERUSER

GROUPGROUP

A team the Brand Kit is shared with.

`type``string`

**Default value:** `TEAM`

**Available values:** The only valid value is `TEAM`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A folder the Brand Kit is shared with.

`type``string`

**Default value:** `FOLDER`

**Available values:** The only valid value is `FOLDER`.

`folder``AuditLogFolder`

A Canva folder.

Properties of **folder**

`id``string`

The folder ID.

`name``string`

Optional

The name of the folder.

An organization the Brand Kit is shared with.

`type``string`

**Default value:** `ORGANIZATION`

**Available values:** The only valid value is `ORGANIZATION`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

A user the Brand Kit is shared with (within a team).

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`.

`user``AuditLogUser`

A Canva user.

Properties of **user**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A group the Brand Kit is shared with (within a team).

`type``string`

**Default value:** `GROUP`

**Available values:** The only valid value is `GROUP`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`new_shares``BrandKitShare[]`

Optional

The shares of the Brand Kit.

TEAMTEAM

FOLDERFOLDER

ORGANIZATIONORGANIZATION

USERUSER

GROUPGROUP

A team the Brand Kit is shared with.

`type``string`

**Default value:** `TEAM`

**Available values:** The only valid value is `TEAM`.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A folder the Brand Kit is shared with.

`type``string`

**Default value:** `FOLDER`

**Available values:** The only valid value is `FOLDER`.

`folder``AuditLogFolder`

A Canva folder.

Properties of **folder**

`id``string`

The folder ID.

`name``string`

Optional

The name of the folder.

An organization the Brand Kit is shared with.

`type``string`

**Default value:** `ORGANIZATION`

**Available values:** The only valid value is `ORGANIZATION`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

A user the Brand Kit is shared with (within a team).

`type``string`

**Default value:** `USER`

**Available values:** The only valid value is `USER`.

`user``AuditLogUser`

A Canva user.

Properties of **user**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

A group the Brand Kit is shared with (within a team).

`type``string`

**Default value:** `GROUP`

**Available values:** The only valid value is `GROUP`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`team``AuditLogTeam`

A Canva team.

Properties of **team**

`id``string`

The team ID.

`display_name``string`

Optional

The display name of the team.

For privacy reasons, this field is redacted for brands outside of your organization. Rarely, it may be unavailable for technical reasons.

`old_fonts``BrandKitFont[]`

Optional

The fonts of the Brand Kit.

Properties of **old_fonts**

`id``string`

The ID of the font family.

`font_family``string`

Optional

The name of the font family.

`font_style``string`

Optional

The style of the font.

`new_fonts``BrandKitFont[]`

Optional

The fonts of the Brand Kit.

Properties of **new_fonts**

`id``string`

The ID of the font family.

`font_family``string`

Optional

The name of the font family.

`font_style``string`

Optional

The style of the font.

`old_folder_links``BrandKitFolderLink[]`

Optional

The previous folder links to the Brand Kit.

Properties of **old_folder_links**

`folder``AuditLogFolder`

A Canva folder.

Properties of **folder**

`id``string`

The folder ID.

`name``string`

Optional

The name of the folder.

`type``string`

Optional

The type of the brand assets in the folder.

**Available values:**

  * `CHARTS`: A folder with Charts.
  * `GRAPHICS`: A folder with Graphics.
  * `ICONS`: A folder with Icons.
  * `LOGOS`: A folder with Logos.
  * `PHOTOS`: A folder with Photos.



`ingredient``BrandKitLinkedIngredient`

Optional

A linked ingredient of the Brand Kit.

Properties of **ingredient**

`id``string`

ID of the ingredient.

`name``string`

Optional

The name of the ingredient.

`new_folder_links``BrandKitFolderLink[]`

Optional

The new folder links to the Brand Kit.

Properties of **new_folder_links**

`folder``AuditLogFolder`

A Canva folder.

Properties of **folder**

`id``string`

The folder ID.

`name``string`

Optional

The name of the folder.

`type``string`

Optional

The type of the brand assets in the folder.

**Available values:**

  * `CHARTS`: A folder with Charts.
  * `GRAPHICS`: A folder with Graphics.
  * `ICONS`: A folder with Icons.
  * `LOGOS`: A folder with Logos.
  * `PHOTOS`: A folder with Photos.



`ingredient``BrandKitLinkedIngredient`

Optional

A linked ingredient of the Brand Kit.

Properties of **ingredient**

`id``string`

ID of the ingredient.

`name``string`

Optional

The name of the ingredient.

`old_ingredient``BrandKitIngredient`

Optional

An ingredient of the Brand Kit.

Properties of **old_ingredient**

`name``string`

Optional

A name of the ingredient.

`id``string`

Optional

ID of the ingredient.

`guidelines``string`

Optional

User-provided guidelines to help members of the team understand how, where, and when to use the ingredient.

`color_palettes``BrandKitColorPalette[]`

Optional

The color palettes of the Brand Kit.

Properties of **color_palettes**

`name``string`

Optional

The name of the color palette.

`colors``BrandKitColor[]`

Optional

The colors in the palette.

Properties of **colors**

`name``string`

Optional

The name of the color.

`hex``string`

Optional

The hex value of the color.

`cmyk``string`

Optional

The CMYK value of the color.

`gradient``BrandKitGradient`

Optional

A color gradient in the Brand Kit.

LINEARLINEAR

RADIALRADIAL

A linear gradient in the Brand Kit.

`type``string`

**Default value:** `LINEAR`

**Available values:** The only valid value is `LINEAR`.

`stops``BrandKitGradientStop[]`

The color stops in the gradient.

Properties of **stops**

`color``string`

The color of the stop.

`transparency``number`

The transparency of the stop.

`position``number`

The position of the stop as a percentage along the gradient line.

`rotation``number`

The rotation of the gradient in degrees.

A radial gradient in the Brand Kit.

`type``string`

**Default value:** `RADIAL`

**Available values:** The only valid value is `RADIAL`.

`stops``BrandKitGradientStop[]`

The color stops in the gradient.

Properties of **stops**

`color``string`

The color of the stop.

`transparency``number`

The transparency of the stop.

`position``number`

The position of the stop as a percentage along the gradient line.

`center``object`

The center of the radial gradient. If the `top` and `left` are both zero, the center is in the top-left of the gradient.

Properties of **center**

`top``number`

The top position of the center, as a percentage down from the top of the gradient.

`left``number`

The left position of the center, as a percentage from the left of the gradient.

`text_styles``BrandKitTextStylesGroup[]`

Optional

The text styles of the Brand Kit.

Properties of **text_styles**

`name``string`

The name of the text style group.

`text_styles``BrandKitTextStyle[]`

The formatting set for the text style.

Properties of **text_styles**

`font``BrandKitFont`

A font in the Brand Kit.

Properties of **font**

`id``string`

The ID of the font family.

`font_family``string`

Optional

The name of the font family.

`font_style``string`

Optional

The style of the font.

`size``integer`

The size of the text style in pixels.

`name``string`

Optional

The name of the text style.

`custom_name``string`

Optional

The user-defined text style name.

`voice``string`

Optional

The voice of the brand.

`assets``BrandKitAsset[]`

Optional

The assets in the ingredient.

Properties of **assets**

`id``string`

An ID of the asset.

`name``string`

Optional

A name of the asset.

`file_name``string`

Optional

A name of the asset file.

`dos_and_donts``BrandKitDosAndDonts`

Optional

The dos and donts for the ingredient

Properties of **dos_and_donts**

`dos``string[]`

Optional

The dos of the ingredient.

`donts``string[]`

Optional

The donts of the ingredient.

`new_ingredient``BrandKitIngredient`

Optional

An ingredient of the Brand Kit.

Properties of **new_ingredient**

`name``string`

Optional

A name of the ingredient.

`id``string`

Optional

ID of the ingredient.

`guidelines``string`

Optional

User-provided guidelines to help members of the team understand how, where, and when to use the ingredient.

`color_palettes``BrandKitColorPalette[]`

Optional

The color palettes of the Brand Kit.

Properties of **color_palettes**

`name``string`

Optional

The name of the color palette.

`colors``BrandKitColor[]`

Optional

The colors in the palette.

Properties of **colors**

`name``string`

Optional

The name of the color.

`hex``string`

Optional

The hex value of the color.

`cmyk``string`

Optional

The CMYK value of the color.

`gradient``BrandKitGradient`

Optional

A color gradient in the Brand Kit.

LINEARLINEAR

RADIALRADIAL

A linear gradient in the Brand Kit.

`type``string`

**Default value:** `LINEAR`

**Available values:** The only valid value is `LINEAR`.

`stops``BrandKitGradientStop[]`

The color stops in the gradient.

Properties of **stops**

`color``string`

The color of the stop.

`transparency``number`

The transparency of the stop.

`position``number`

The position of the stop as a percentage along the gradient line.

`rotation``number`

The rotation of the gradient in degrees.

A radial gradient in the Brand Kit.

`type``string`

**Default value:** `RADIAL`

**Available values:** The only valid value is `RADIAL`.

`stops``BrandKitGradientStop[]`

The color stops in the gradient.

Properties of **stops**

`color``string`

The color of the stop.

`transparency``number`

The transparency of the stop.

`position``number`

The position of the stop as a percentage along the gradient line.

`center``object`

The center of the radial gradient. If the `top` and `left` are both zero, the center is in the top-left of the gradient.

Properties of **center**

`top``number`

The top position of the center, as a percentage down from the top of the gradient.

`left``number`

The left position of the center, as a percentage from the left of the gradient.

`text_styles``BrandKitTextStylesGroup[]`

Optional

The text styles of the Brand Kit.

Properties of **text_styles**

`name``string`

The name of the text style group.

`text_styles``BrandKitTextStyle[]`

The formatting set for the text style.

Properties of **text_styles**

`font``BrandKitFont`

A font in the Brand Kit.

Properties of **font**

`id``string`

The ID of the font family.

`font_family``string`

Optional

The name of the font family.

`font_style``string`

Optional

The style of the font.

`size``integer`

The size of the text style in pixels.

`name``string`

Optional

The name of the text style.

`custom_name``string`

Optional

The user-defined text style name.

`voice``string`

Optional

The voice of the brand.

`assets``BrandKitAsset[]`

Optional

The assets in the ingredient.

Properties of **assets**

`id``string`

An ID of the asset.

`name``string`

Optional

A name of the asset.

`file_name``string`

Optional

A name of the asset file.

`dos_and_donts``BrandKitDosAndDonts`

Optional

The dos and donts for the ingredient

Properties of **dos_and_donts**

`dos``string[]`

Optional

The dos of the ingredient.

`donts``string[]`

Optional

The donts of the ingredient.

`old_icon``AuditLogImage`

Optional

A Canva image.

Properties of **old_icon**

`id``string`

The image ID.

`name``string`

Optional

The name of the image.

`new_icon``AuditLogImage`

Optional

A Canva image.

Properties of **new_icon**

`id``string`

The image ID.

`name``string`

Optional

The name of the image.

`old_guidelines``AuditLogDesign`

Optional

A Canva design.

Properties of **old_guidelines**

`id``string`

The design ID.

`name``string`

Optional

The name of the design.

`new_guidelines``AuditLogDesign`

Optional

A Canva design.

Properties of **new_guidelines**

`id``string`

The design ID.

`name``string`

Optional

The name of the design.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_BRAND_KIT",
    
        "changed_fields": [
    
          "NAME",
    
          "SHARES",
    
          "FONTS",
    
          "FOLDER_LINKS",
    
          "INGREDIENT",
    
          "ICON",
    
          "GUIDELINES"
    
        ],
    
        "old_name": "Marketing Brand Kit",
    
        "new_name": "Growth Brand Kit",
    
        "old_shares": [
    
          {
    
            "type": "TEAM",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "FOLDER",
    
            "folder": {
    
              "id": "FXeFatjDhdR",
    
              "name": "Marketing Folder"
    
            }
    
          },
    
          {
    
            "type": "ORGANIZATION",
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "USER",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "GROUP",
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          }
    
        ],
    
        "new_shares": [
    
          {
    
            "type": "TEAM",
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "FOLDER",
    
            "folder": {
    
              "id": "FXeFatjDhdR",
    
              "name": "Marketing Folder"
    
            }
    
          },
    
          {
    
            "type": "ORGANIZATION",
    
            "organization": {
    
              "id": "OXtgecafZvh",
    
              "display_name": "Acme Corporation"
    
            }
    
          },
    
          {
    
            "type": "USER",
    
            "user": {
    
              "id": "UXoqDbwwSbQ",
    
              "display_name": "Jane Doe",
    
              "email": "jane.doe@example.com"
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          },
    
          {
    
            "type": "GROUP",
    
            "group": {
    
              "id": "GJViWaMsqhL",
    
              "display_name": "Marketing Group"
    
            },
    
            "team": {
    
              "id": "BXeFatjDhdR",
    
              "display_name": "Acme Team"
    
            }
    
          }
    
        ],
    
        "old_fonts": [
    
          "Roboto Thin",
    
          "Mona Sans"
    
        ],
    
        "new_fonts": [
    
          "Roboto Thin",
    
          "Mona Sans"
    
        ],
    
        "old_folder_links": [
    
          {
    
            "folder": {
    
              "id": "FXeFatjDhdR",
    
              "name": "Marketing Folder"
    
            },
    
            "type": "CHARTS",
    
            "ingredient": {
    
              "name": "Logos",
    
              "id": "IG-123456789000"
    
            }
    
          }
    
        ],
    
        "new_folder_links": [
    
          {
    
            "folder": {
    
              "id": "FXeFatjDhdR",
    
              "name": "Marketing Folder"
    
            },
    
            "type": "CHARTS",
    
            "ingredient": {
    
              "name": "Logos",
    
              "id": "IG-123456789000"
    
            }
    
          }
    
        ],
    
        "old_ingredient": {
    
          "name": "Colors",
    
          "id": "IG-123456789000",
    
          "guidelines": "Use these colors for all marketing materials.",
    
          "color_palettes": [
    
            {
    
              "name": "Main brand colors",
    
              "colors": [
    
                {
    
                  "name": "Primary",
    
                  "hex": "#FF0000",
    
                  "cmyk": "cmyk(0, 100, 100, 0)",
    
                  "gradient": {
    
                    "type": "LINEAR",
    
                    "stops": [
    
                      {
    
                        "color": "#FF0000",
    
                        "transparency": 0.5,
    
                        "position": 50
    
                      }
    
                    ],
    
                    "rotation": 90
    
                  }
    
                }
    
              ]
    
            }
    
          ],
    
          "text_styles": [
    
            {
    
              "name": "Title",
    
              "text_styles": [
    
                {
    
                  "name": "Title",
    
                  "font": {
    
                    "id": "YXeFatjDhdR",
    
                    "font_family": "Roboto",
    
                    "font_style": "Bold"
    
                  },
    
                  "custom_name": "Main Title",
    
                  "size": 12
    
                }
    
              ]
    
            }
    
          ],
    
          "voice": "Our voice is professional and formal.",
    
          "assets": [
    
            {
    
              "id": "M1234567890",
    
              "name": "Our primary logo",
    
              "file_name": "main-logo.png"
    
            }
    
          ],
    
          "dos_and_donts": {
    
            "dos": [
    
              "Use these colors for all marketing materials."
    
            ],
    
            "donts": [
    
              "Do not use these colors for all marketing materials."
    
            ]
    
          }
    
        },
    
        "new_ingredient": {
    
          "name": "Colors",
    
          "id": "IG-123456789000",
    
          "guidelines": "Use these colors for all marketing materials.",
    
          "color_palettes": [
    
            {
    
              "name": "Main brand colors",
    
              "colors": [
    
                {
    
                  "name": "Primary",
    
                  "hex": "#FF0000",
    
                  "cmyk": "cmyk(0, 100, 100, 0)",
    
                  "gradient": {
    
                    "type": "LINEAR",
    
                    "stops": [
    
                      {
    
                        "color": "#FF0000",
    
                        "transparency": 0.5,
    
                        "position": 50
    
                      }
    
                    ],
    
                    "rotation": 90
    
                  }
    
                }
    
              ]
    
            }
    
          ],
    
          "text_styles": [
    
            {
    
              "name": "Title",
    
              "text_styles": [
    
                {
    
                  "name": "Title",
    
                  "font": {
    
                    "id": "YXeFatjDhdR",
    
                    "font_family": "Roboto",
    
                    "font_style": "Bold"
    
                  },
    
                  "custom_name": "Main Title",
    
                  "size": 12
    
                }
    
              ]
    
            }
    
          ],
    
          "voice": "Our voice is professional and formal.",
    
          "assets": [
    
            {
    
              "id": "M1234567890",
    
              "name": "Our primary logo",
    
              "file_name": "main-logo.png"
    
            }
    
          ],
    
          "dos_and_donts": {
    
            "dos": [
    
              "Use these colors for all marketing materials."
    
            ],
    
            "donts": [
    
              "Do not use these colors for all marketing materials."
    
            ]
    
          }
    
        },
    
        "old_icon": {
    
          "id": "MAGx4jow4mz",
    
          "name": "Logo.png"
    
        },
    
        "new_icon": {
    
          "id": "MAGx4jow4mz",
    
          "name": "Logo.png"
    
        },
    
        "old_guidelines": {
    
          "id": "DAGx5FEzu38",
    
          "name": "My awesome design"
    
        },
    
        "new_guidelines": {
    
          "id": "DAGx5FEzu38",
    
          "name": "My awesome design"
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Delete a Brand Kit

An `actor` triggers this event when they delete a Brand Kit. For details, see [Canva Help: Setting up Brand Kits⁠(opens in a new tab or window)](https://www.canva.com/help/brand-kit/).

`type``string`

**Default value:** `DELETE_BRAND_KIT`

**Available values:** The only valid value is `DELETE_BRAND_KIT`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "DELETE_BRAND_KIT"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Send a brand template share notification

An `actor` triggers this event when they share a brand template. Canva will attempt to send an email and an in-app notification to the user the brand template is shared with (`recipient`).

`type``string`

**Default value:** `SEND_BRAND_TEMPLATE_SHARE_NOTIFICATION`

**Available values:** The only valid value is `SEND_BRAND_TEMPLATE_SHARE_NOTIFICATION`.

`recipient``ShareNotificationRecipient`

The recipient of the share notification.

The recipient can be a user, a group, an organization, or an email address.

USER_RECIPIENTUSER_RECIPIENT

GROUP_RECIPIENTGROUP_RECIPIENT

ORGANIZATION_RECIPIENTORGANIZATION_RECIPIENT

EMAIL_RECIPIENTEMAIL_RECIPIENT

`type``string`

**Default value:** `USER_RECIPIENT`

**Available values:** The only valid value is `USER_RECIPIENT`.

`user``AuditLogUser`

A Canva user.

Properties of **user**

`id``string`

The user ID.

`display_name``string`

Optional

The display name of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`email``string`

Optional

The email address of the user.

For privacy reasons, this field is redacted for users outside of your organization. Rarely, it may also be unavailable for technical reasons.

`type``string`

**Default value:** `GROUP_RECIPIENT`

**Available values:** The only valid value is `GROUP_RECIPIENT`.

`group``AuditLogGroup`

A Canva group.

Properties of **group**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`type``string`

**Default value:** `ORGANIZATION_RECIPIENT`

**Available values:** The only valid value is `ORGANIZATION_RECIPIENT`.

`organization``AuditLogOrganization`

A Canva organization.

Properties of **organization**

`id``string`

The organization ID.

`display_name``string`

Optional

The display name of the organization.

For privacy reasons, this field is redacted for organizations other than your organization. Rarely, it may be unavailable for technical reasons.

`type``string`

**Default value:** `EMAIL_RECIPIENT`

**Available values:** The only valid value is `EMAIL_RECIPIENT`.

`email``string`

The email address the design invite was sent to.

`message``string`

Optional

An optional message from the `actor` to the `recipient`.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "SEND_BRAND_TEMPLATE_SHARE_NOTIFICATION",
    
        "message": "Check out my brand template!",
    
        "recipient": {
    
          "type": "USER_RECIPIENT",
    
          "user": {
    
            "id": "UXoqDbwwSbQ",
    
            "display_name": "Jane Doe",
    
            "email": "jane.doe@example.com"
    
          }
    
        }
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
