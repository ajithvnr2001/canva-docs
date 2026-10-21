---
url: https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/
title: Permissions & Settings - Canva Audit Logs Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:53.070509+00:00
---

# Permissions & Settings - Canva Audit Logs Documentation

> Source: https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/

Audit Logs

[Overview](https://www.canva.dev/docs/audit-logs/)[Setup](https://www.canva.dev/docs/audit-logs/setup/)[Audit events](https://www.canva.dev/docs/audit-logs/audit-events/)

Concepts

[Designs, folders, and assets](https://www.canva.dev/docs/audit-logs/what-are-designs-folders-and-assets/)[Teams, groups, and users](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/)[Canva Apps and Integrations](https://www.canva.dev/docs/audit-logs/what-are-canva-apps-and-integrations/)

Actions reference

[3Ds](https://www.canva.dev/docs/audit-logs/actions/3ds/)[Admin API](https://www.canva.dev/docs/audit-logs/actions/admin-api/)[Apps](https://www.canva.dev/docs/audit-logs/actions/apps/)[Audio](https://www.canva.dev/docs/audit-logs/actions/audio/)[Audit Logs](https://www.canva.dev/docs/audit-logs/actions/audit-logs/)[Brands](https://www.canva.dev/docs/audit-logs/actions/brands/)[Content](https://www.canva.dev/docs/audit-logs/actions/content/)[Designs](https://www.canva.dev/docs/audit-logs/actions/designs/)[Exports](https://www.canva.dev/docs/audit-logs/actions/exports/)[Folders](https://www.canva.dev/docs/audit-logs/actions/folders/)[Groups](https://www.canva.dev/docs/audit-logs/actions/groups/)[Investigations](https://www.canva.dev/docs/audit-logs/actions/investigations/)[Organizations](https://www.canva.dev/docs/audit-logs/actions/organizations/)[Permissions & Settings](https://www.canva.dev/docs/audit-logs/actions/permissions-and-settings/)[Teams](https://www.canva.dev/docs/audit-logs/actions/teams/)[Templates](https://www.canva.dev/docs/audit-logs/actions/templates/)[Users](https://www.canva.dev/docs/audit-logs/actions/users/)[Videos](https://www.canva.dev/docs/audit-logs/actions/videos/)[Websites](https://www.canva.dev/docs/audit-logs/actions/websites/)

# Permissions & Settings

Copy page

## Update a Team's Permissions

An `actor` triggers this event when they update a team permission for a feature. For example, when a user sets `MAGIC WRITE` to `TEAM_ADMINS`, users with the `TEAM ADMIN` team role can access `MAGIC WRITE`. If an a user adds a group to a feature's team permission, all members of this group will get access to the feature regardless of the members team role.

`type``string`

**Default value:** `UPDATE_TEAM_PERMISSION`

**Available values:** The only valid value is `UPDATE_TEAM_PERMISSION`.

`team_permission``string`

The feature which the permission controls access too.

**Available values:**

  * `DREAM_STUDIO`: Use Dream studio.
  * `OFFLINE_DESIGNS`: Use Offline Designs.
  * `CANVA_AI`: Use Canva AI (conversational AI) to brainstorm, write, and create designs.
  * `MAGIC_DESIGN`: Use Magic Design.
  * `MAGIC_EDIT`: Use Magic Edit.
  * `MAGIC_MEDIA`: Use Magic Media.
  * `TRANSFORM_INTO_DOC`: Use Transform into Doc.
  * `MAGIC_WRITE`: Use Magic Write.
  * `TEMPLATE_LIBRARY`: Access the templates library.
  * `ASK_CANVA`: Ask Canva for AI-generated design advice.
  * `NON_INDEMNIFIED_CONTENT`: Access elements and fonts not covered by Canva’s IP indemnity.
  * `MAGIC_INSIGHTS`: Use Magic Insights.
  * `CANVA_CODE`: Use Canva Code.
  * `ACCEPT_COPIED_CONTENT_FROM_ANOTHER_TEAM`: Accept copied content from another team.
  * `SHARE_DESIGNS_EXTERNALLY_VIA_LINKS`: Share designs via [public view links⁠(opens in a new tab or window)](https://www.canva.com/help/sharing-your-design-as-a-public-view-link/), [public embeds⁠(opens in a new tab or window)](https://www.canva.com/help/embed-designs/), [websites⁠(opens in a new tab or window)](https://www.canva.com/help/canva-websites/), and [collaboration links⁠(opens in a new tab or window)](https://www.canva.com/help/share-via-link-or-email/) that can be shared externally.
  * `SHARE_DESIGNS_TO_EXTERNAL_EMAILS`: Share designs to external emails by design access invitation or directly granting access.
  * `SCHEDULE_POSTS_WITH_CONTENT_PLANNER`: Schedule posts with the Content Planner.
  * `CANVA_PRINT`: Use Canva Print.
  * `DOWNLOAD_DESIGNS`: Download designs or selected elements.
  * `COPY_CONTENT_TO_ANOTHER_TEAM`: Send copies of their content outside the team.
  * `PHOTO_ELEMENTS`: Use photo elements.
  * `AUDIO_ELEMENTS`: Use audio elements.
  * `VIDEO_ELEMENTS`: Use video elements.
  * `GRAPHIC_ELEMENTS`: Use graphic elements.
  * `STICKER_ELEMENTS`: Use sticker elements.
  * `CHART_ELEMENTS`: Use chart elements.
  * `TABLE_ELEMENTS`: Use table elements.
  * `FRAME_ELEMENTS`: Use frame elements.
  * `GRID_ELEMENTS`: Use grid elements.
  * `SHAPE_ELEMENTS`: Use shape elements.
  * `OTHER_ELEMENTS`: Use any other elements.
  * `VIEW_EMAILS`: See other members email addresses.
  * `CREATE_GROUPS`: Create [groups⁠(opens in a new tab or window)](https://www.canva.com/help/groups/).
  * `LEAVE_TEAM`: Leave a team.
  * `REFERENCE_TEAM_CONTENT_FOR_AI_GENERATED_RESPONSES`: Reference team documents when using AI to generate content.
  * `MAGIC_ACTIVITIES`: Use Magic Activities.
  * `GROW_CREATE`: Use Canva Grow Create
  * `GROW_INSIGHTS`: Use Canva Grow Insights
  * `CONNECT_AD_ACCOUNTS`: Connect Ad Accounts to Canva Grow
  * `MAGIC_BACKGROUND`: Use Magic Background.
  * `CREATE_PERSONAL_BRAND_KIT`: Create a personal Brand Kit.
  * `AI_CHART_GENERATION`: Use AI to generate charts.
  * `PUBLISH_TO_WEBSITE_DOMAIN`: Publish to a website domain.
  * `AI_AUDIO_GENERATION`: Use AI to generate audio.
  * `AI_3D_ELEMENT_GENERATION`: Use AI to generate 3D elements.
  * `MAGIC_DECORATIONS`: Use Magic Decorations.
  * `BEAUTIFY`: Use Beautify.
  * `MAGIC_LAYERS`: Use Magic Layers.
  * `BULK_CREATE_AUTO_MATCH_FIELDS`: Use auto-match fields in bulk create.
  * `ADD_COMMENTS_ON_DESIGNS`: Comment on designs.
  * `EDIT_AND_DELETE_COMMENTS_ON_DESIGNS`: Edit and delete comments on designs.
  * `IMAGE_TO_VIDEO`: Use Image to Video.
  * `VIEW_EXTERNAL_DESIGNS`: Access designs shared from outside this team.
  * `PUBLISH_ADS`: Publish ads and edit ad budgets on platforms.
  * `AFFINITY_CANVA_AI`: Use Canva AI in Affinity.



`old_team_permission_role``string`

Optional

The team role for a feature. Users who are assigned this team role will access to the feature controlled by the Permission.

**Available values:**

  * `NO_ONE`: No team members can use the feature.
  * `TEAM_ADMINS`: Team admins can use the feature.
  * `TEAM_BRAND_DESIGNERS_AND_TEAM_ADMINS`: Team designers and admins can use the feature.
  * `EVERYONE`: All team members can use the feature.



`new_team_permission_role``string`

Optional

The team role for a feature. Users who are assigned this team role will access to the feature controlled by the Permission.

**Available values:**

  * `NO_ONE`: No team members can use the feature.
  * `TEAM_ADMINS`: Team admins can use the feature.
  * `TEAM_BRAND_DESIGNERS_AND_TEAM_ADMINS`: Team designers and admins can use the feature.
  * `EVERYONE`: All team members can use the feature.



`old_groups``AuditLogGroup[]`

Optional

The [Groups](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/) associated with this Permission Setting. Members of a Group included will have access to the feature regardless of the Team Role.

Properties of **old_groups**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

`new_groups``AuditLogGroup[]`

Optional

The [Groups](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/) associated with this Permission Setting. Members of a Group included will have access to the feature regardless of the Team Role.

Properties of **new_groups**

`id``string`

The group ID.

`display_name``string`

Optional

The display name of the group.

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_TEAM_PERMISSION",
    
        "team_permission": "DREAM_STUDIO",
    
        "old_team_permission_role": "NO_ONE",
    
        "new_team_permission_role": "NO_ONE",
    
        "old_groups": [
    
          {
    
            "id": "GJViWaMsqhL",
    
            "display_name": "Marketing Group"
    
          }
    
        ],
    
        "new_groups": [
    
          {
    
            "id": "GJViWaMsqhL",
    
            "display_name": "Marketing Group"
    
          }
    
        ]
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an Organization's Permissions

An `actor` triggers this event when they update an organization's default permission for a feature. For example, when an organization admin sets `MAGIC WRITE` to `TEAM_ADMINS`, all users in the organization with the `TEAM ADMIN` team role can access `MAGIC WRITE`. An organization admin is able to specify whether this default permission value is overrideable by team level admins.

`type``string`

**Default value:** `UPDATE_ORGANIZATION_PERMISSION`

**Available values:** The only valid value is `UPDATE_ORGANIZATION_PERMISSION`.

`team_permission``string`

The feature which the permission controls access too.

**Available values:**

  * `DREAM_STUDIO`: Use Dream studio.
  * `OFFLINE_DESIGNS`: Use Offline Designs.
  * `CANVA_AI`: Use Canva AI (conversational AI) to brainstorm, write, and create designs.
  * `MAGIC_DESIGN`: Use Magic Design.
  * `MAGIC_EDIT`: Use Magic Edit.
  * `MAGIC_MEDIA`: Use Magic Media.
  * `TRANSFORM_INTO_DOC`: Use Transform into Doc.
  * `MAGIC_WRITE`: Use Magic Write.
  * `TEMPLATE_LIBRARY`: Access the templates library.
  * `ASK_CANVA`: Ask Canva for AI-generated design advice.
  * `NON_INDEMNIFIED_CONTENT`: Access elements and fonts not covered by Canva’s IP indemnity.
  * `MAGIC_INSIGHTS`: Use Magic Insights.
  * `CANVA_CODE`: Use Canva Code.
  * `ACCEPT_COPIED_CONTENT_FROM_ANOTHER_TEAM`: Accept copied content from another team.
  * `SHARE_DESIGNS_EXTERNALLY_VIA_LINKS`: Share designs via [public view links⁠(opens in a new tab or window)](https://www.canva.com/help/sharing-your-design-as-a-public-view-link/), [public embeds⁠(opens in a new tab or window)](https://www.canva.com/help/embed-designs/), [websites⁠(opens in a new tab or window)](https://www.canva.com/help/canva-websites/), and [collaboration links⁠(opens in a new tab or window)](https://www.canva.com/help/share-via-link-or-email/) that can be shared externally.
  * `SHARE_DESIGNS_TO_EXTERNAL_EMAILS`: Share designs to external emails by design access invitation or directly granting access.
  * `SCHEDULE_POSTS_WITH_CONTENT_PLANNER`: Schedule posts with the Content Planner.
  * `CANVA_PRINT`: Use Canva Print.
  * `DOWNLOAD_DESIGNS`: Download designs or selected elements.
  * `COPY_CONTENT_TO_ANOTHER_TEAM`: Send copies of their content outside the team.
  * `PHOTO_ELEMENTS`: Use photo elements.
  * `AUDIO_ELEMENTS`: Use audio elements.
  * `VIDEO_ELEMENTS`: Use video elements.
  * `GRAPHIC_ELEMENTS`: Use graphic elements.
  * `STICKER_ELEMENTS`: Use sticker elements.
  * `CHART_ELEMENTS`: Use chart elements.
  * `TABLE_ELEMENTS`: Use table elements.
  * `FRAME_ELEMENTS`: Use frame elements.
  * `GRID_ELEMENTS`: Use grid elements.
  * `SHAPE_ELEMENTS`: Use shape elements.
  * `OTHER_ELEMENTS`: Use any other elements.
  * `VIEW_EMAILS`: See other members email addresses.
  * `CREATE_GROUPS`: Create [groups⁠(opens in a new tab or window)](https://www.canva.com/help/groups/).
  * `LEAVE_TEAM`: Leave a team.
  * `REFERENCE_TEAM_CONTENT_FOR_AI_GENERATED_RESPONSES`: Reference team documents when using AI to generate content.
  * `MAGIC_ACTIVITIES`: Use Magic Activities.
  * `GROW_CREATE`: Use Canva Grow Create
  * `GROW_INSIGHTS`: Use Canva Grow Insights
  * `CONNECT_AD_ACCOUNTS`: Connect Ad Accounts to Canva Grow
  * `MAGIC_BACKGROUND`: Use Magic Background.
  * `CREATE_PERSONAL_BRAND_KIT`: Create a personal Brand Kit.
  * `AI_CHART_GENERATION`: Use AI to generate charts.
  * `PUBLISH_TO_WEBSITE_DOMAIN`: Publish to a website domain.
  * `AI_AUDIO_GENERATION`: Use AI to generate audio.
  * `AI_3D_ELEMENT_GENERATION`: Use AI to generate 3D elements.
  * `MAGIC_DECORATIONS`: Use Magic Decorations.
  * `BEAUTIFY`: Use Beautify.
  * `MAGIC_LAYERS`: Use Magic Layers.
  * `BULK_CREATE_AUTO_MATCH_FIELDS`: Use auto-match fields in bulk create.
  * `ADD_COMMENTS_ON_DESIGNS`: Comment on designs.
  * `EDIT_AND_DELETE_COMMENTS_ON_DESIGNS`: Edit and delete comments on designs.
  * `IMAGE_TO_VIDEO`: Use Image to Video.
  * `VIEW_EXTERNAL_DESIGNS`: Access designs shared from outside this team.
  * `PUBLISH_ADS`: Publish ads and edit ad budgets on platforms.
  * `AFFINITY_CANVA_AI`: Use Canva AI in Affinity.



`old_team_overrides_enabled``boolean`

Optional

Whether or not the team permission was overrideable by team admins previously.

`new_team_overrides_enabled``boolean`

Optional

Whether or not the team permission is overrideable by team admins currently.

`old_team_permission_role_default``string`

Optional

The team role for a feature. Users who are assigned this team role will access to the feature controlled by the Permission.

**Available values:**

  * `NO_ONE`: No team members can use the feature.
  * `TEAM_ADMINS`: Team admins can use the feature.
  * `TEAM_BRAND_DESIGNERS_AND_TEAM_ADMINS`: Team designers and admins can use the feature.
  * `EVERYONE`: All team members can use the feature.



`new_team_permission_role_default``string`

Optional

The team role for a feature. Users who are assigned this team role will access to the feature controlled by the Permission.

**Available values:**

  * `NO_ONE`: No team members can use the feature.
  * `TEAM_ADMINS`: Team admins can use the feature.
  * `TEAM_BRAND_DESIGNERS_AND_TEAM_ADMINS`: Team designers and admins can use the feature.
  * `EVERYONE`: All team members can use the feature.



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_ORGANIZATION_PERMISSION",
    
        "team_permission": "DREAM_STUDIO",
    
        "old_team_overrides_enabled": true,
    
        "new_team_overrides_enabled": true,
    
        "old_team_permission_role_default": "NO_ONE",
    
        "new_team_permission_role_default": "NO_ONE"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update an Organization's settings

An `actor` triggers this event when they update an organization setting.

`type``string`

**Default value:** `UPDATE_ORGANIZATION_SETTING`

**Available values:** The only valid value is `UPDATE_ORGANIZATION_SETTING`.

`setting``string`

The name of the setting that was updated.

**Available values:**

  * `PERSONAL_TEAM_ARCHIVING_ENABLED`: Automatically [archive any personal teams⁠(opens in a new tab or window)](https://www.canva.com/help/enable-content-consolidation-enterprise/) that your managed members may have.
  * `SHARE_DESIGNS_WITH_CANVA_SUPPORT_ENABLED`: Allows or prevents members of a [Canva organization](https://www.canva.dev/docs/audit-logs/how-are-teams-structured/) from temporarily sharing affected designs with Canva Support during support requests.
  * `INVESTIGATIONS_ENABLED`: Allows organisation admins to access private content that hasn’t been shared with them. This access is for security and compliance investigations only and is always audit logged.
  * `DESIGN_ACTIVITY_REPORT_ENABLED`: When turned on, admins can access the design activity report which shows insights about team designs.
  * `TEAM_ARCHIVAL_ENABLED`: When turned on, affiliated users will have brands they own archived. See [Archive personal teams in Canva⁠(opens in a new tab or window)](https://www.canva.com/help/enable-content-consolidation-enterprise/) for more details.



`new_value``boolean`

`old_value``boolean`

Optional

### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_ORGANIZATION_SETTING",
    
        "setting": "PERSONAL_TEAM_ARCHIVING_ENABLED",
    
        "old_value": true,
    
        "new_value": true
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy

## Update data residency region

An `actor` triggers this event when they update the data residency region.

`type``string`

**Default value:** `UPDATE_DATA_RESIDENCY_REGION_SETTING`

**Available values:** The only valid value is `UPDATE_DATA_RESIDENCY_REGION_SETTING`.

`new_region``string`

The data residency region.

**Available values:**

  * `US`: United States
  * `EU`: Europe
  * `AU`: Australia
  * `JP`: Japan
  * `ANY`: No preference



`old_region``string`

Optional

The data residency region.

**Available values:**

  * `US`: United States
  * `EU`: Europe
  * `AU`: Australia
  * `JP`: Japan
  * `ANY`: No preference



### Example
    
    
    {
    
      "id": ...,
    
      "timestamp": ...,
    
      "actor": ...,
    
      "target": ...,
    
      "action": {
    
        "type": "UPDATE_DATA_RESIDENCY_REGION_SETTING",
    
        "old_region": "US",
    
        "new_region": "US"
    
      },
    
      "outcome": ...,
    
      "context": ...
    
    }

JSON

Copy
