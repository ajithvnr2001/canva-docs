---
url: https://www.canva.dev/docs/apps/app-ui-kit-v5-migration/
title: App UI Kit v4 to v5 Migration Guide - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:58:21.883197+00:00
---

# App UI Kit v4 to v5 Migration Guide - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/app-ui-kit-v5-migration/

App lifecycle

[App versioning](https://www.canva.dev/docs/apps/versioning-apps/)[Canva REST API versioning](https://www.canva.dev/docs/apps/rest-apis/manage-versions/)[Disabled apps](https://www.canva.dev/docs/apps/handling-disabled-apps/)[Deep linking](https://www.canva.dev/docs/apps/deep-linking/)

Growth and performance

[Analytics](https://www.canva.dev/docs/apps/analytics/)[Getting featured](https://www.canva.dev/docs/apps/getting-featured/)

Monetization

[Overview](https://www.canva.dev/docs/apps/monetization/)[External payment links](https://www.canva.dev/docs/apps/accepting-payments/)

Premium Apps Program

[Overview](https://www.canva.dev/docs/apps/premium-apps/)[Implementing monetization](https://www.canva.dev/docs/apps/premium-apps/implementing-monetization/)[Set up payout details](https://www.canva.dev/docs/apps/payout-details/)[Design guidelines](https://www.canva.dev/docs/apps/design-guidelines/premium-apps/)[Learn more⁠(opens in a new tab or window)](https://www.canva.com/developers/premium-apps-program/)

Team and access

[App collaborators](https://www.canva.dev/docs/apps/app-configuration/collaboration/)

Upgrades and migrations

[Overview](https://www.canva.dev/docs/apps/upgrades-and-migrations/)[Apps SDK v2 Upgrade guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/v2-migration-guide/)[Apps SDK v2 Upgrade FAQ](https://www.canva.dev/docs/apps/upgrades-and-migrations/v2-migration-faq/)[Design Editor Intent Upgrade guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/design-editor-migration-guide/)[App UI Kit v5 Upgrade guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/app-ui-kit-v5-migration/)[App Scripts Upgrade guide](https://www.canva.dev/docs/apps/upgrades-and-migrations/app-scripts-migration-guide/)

# App UI Kit v4 to v5 Migration Guide

Upgrade your app from App UI Kit v4 to v5.

Copy page

Version 5 of the App UI Kit includes new design tokens that replace the v4 tokens with a new naming system and improved semantic structure.

This page provides the complete mapping from v4 to v5 design tokens to help you upgrade your app.

For more information about design tokens and when to use them, see the [design tokens overview](https://www.canva.dev/docs/apps/app-ui-kit/design-tokens/).

There are also some breaking changes in the component library. For the full list of changes, see the [changelog](https://www.canva.dev/docs/apps/app-ui-kit/changelog/#501-2025-09-30) .

## What's changing?

The App UI Kit v5 introduces a new design token system with:

  * **Improved semantic naming** : Tokens now have clearer, more descriptive names.
  * **Better organization** : Tokens are grouped by purpose (action, content, feedback, and so on).
  * **Enhanced consistency** : More consistent naming patterns across all token types.



There are also some breaking changes to the properties of the `Link`, `Pill`, `InputPill`, `Columns`, and `ColorSelector` components.

Finally, we have upgraded from React 18 to 19 so you may have other dependencies that need to change, or breaking changes in React to accommodate. For more information about upgrading to React 19, see the [react.dev upgrade guide⁠(opens in a new tab or window)](https://react.dev/blog/2024/04/25/react-19-upgrade-guide).

## How to automatically migrate

Run the `app-ui-kit-v5` Canva CLI apps migrate command in your app's project directory to use the Canva CLI to automatically migrate your app to use App UI Kit v5:
    
    
    npx @canva/cli@latest apps migrate app-ui-kit-v5

BASH

Copy

It automatically runs through the code changes required to install the updated dependencies, migrates design tokens, and changes component properties.

## How to manually migrate

  1. **Update your dependencies** : Upgrade to the latest version of `@canva/app-ui-kit`.
  2. **Find and replace tokens** : Use the tables below to map your v4 tokens to v5 tokens.
  3. **Update components** : There are some small breaking changes to component properties in v5.
  4. **Test your app** : Verify that your app still looks and works correctly.



### Migration example

Here's an example of migrating a CSS class from v4 to v5 tokens:

**Before (v4 tokens):**
    
    
    .my-component {
    
      background-color: var(--ui-kit-color-primary);
    
      color: var(--ui-kit-color-typography-primary);
    
      padding: var(--ui-kit-space-2);
    
    }

CSS

Copy

**After (v5 tokens):**
    
    
    .my-component {
    
      background-color: var(--ui-kit-color-action-primary-bg);
    
      color: var(--ui-kit-color-content-fg);
    
      padding: var(--ui-kit-space-200);
    
    }

CSS

Copy

### Do I need to migrate the design tokens?

  * **If you only use App UI Kit components** : You don't need to do anything. The components will automatically use the new v5 tokens.

  * **If you use design tokens directly in your CSS or TypeScript** : You'll need to update your code to use the new v5 token names.




## Migration mappings

The tables below show the complete mapping from v4 to v5 design tokens.

### Color tokens

CSS VariablesCSS Variables

JS VariablesJS Variables

Removed V4 variable| Replacement V5 variable  
---|---  
`--ui-kit-color-typography-primary`| `--ui-kit-color-content-fg`  
`--ui-kit-color-typography-secondary`| `--ui-kit-color-content-subtle-fg`  
`--ui-kit-color-typography-tertiary`| `--ui-kit-color-content-subtlest-fg`  
`--ui-kit-color-typography-quaternary`| `--ui-kit-color-content-placeholder-fg`  
`--ui-kit-color-typography-placeholder`| `--ui-kit-color-content-placeholder-fg`  
`--ui-kit-color-typography-positive`| `--ui-kit-color-content-positive-fg`  
`--ui-kit-color-typography-info`| `--ui-kit-color-content-info-fg`  
`--ui-kit-color-typography-warn`| `--ui-kit-color-content-warn-fg`  
`--ui-kit-color-typography-critical`| `--ui-kit-color-content-critical-fg`  
`--ui-kit-color-typography-critical-hover`| `--ui-kit-color-content-critical-fg`  
`--ui-kit-color-typography-critical-active`| `--ui-kit-color-content-critical-fg`  
`--ui-kit-color-typography-link`| `--ui-kit-color-link-fg`  
`--ui-kit-color-typography-link-hover`| `--ui-kit-color-link-fg-hovered`  
`--ui-kit-color-typography-link-active`| `--ui-kit-color-link-fg-pressed`  
`--ui-kit-color-contrast`| `--ui-kit-color-feedback-overlay-bg`  
`--ui-kit-color-contrast-fore`| `--ui-kit-color-feedback-overlay-fg`  
`--ui-kit-color-neutral-fore-disabled`| `--ui-kit-color-handle-bg-disabled`  
`--ui-kit-color-neutral-fore-low`| `--ui-kit-color-content-fg`  
`--ui-kit-color-positive-hover`| `--ui-kit-color-action-secondary-bg-hovered`  
`--ui-kit-color-positive-active`| `--ui-kit-color-action-secondary-bg-pressed`  
`--ui-kit-color-positive-disabled`| `--ui-kit-color-action-bg-disabled`  
`--ui-kit-color-info-hover`| `--ui-kit-color-action-secondary-bg-hovered`  
`--ui-kit-color-info-active`| `--ui-kit-color-action-secondary-bg-pressed`  
`--ui-kit-color-info-disabled`| `--ui-kit-color-action-bg-disabled`  
`--ui-kit-color-info-fore-disabled`| `--ui-kit-color-action-fg-disabled`  
`--ui-kit-color-warn-hover`| `--ui-kit-color-action-secondary-bg-hovered`  
`--ui-kit-color-warn-active`| `--ui-kit-color-action-secondary-bg-pressed`  
`--ui-kit-color-warn-disabled`| `--ui-kit-color-action-bg-disabled`  
`--ui-kit-color-critical`| `--ui-kit-color-feedback-critical-bg`  
`--ui-kit-color-critical-fore`| `--ui-kit-color-feedback-critical-fg`  
`--ui-kit-color-border-active`| `--ui-kit-color-action-selected-border`  
`--ui-kit-color-primary`| `--ui-kit-color-action-primary-bg`  
`--ui-kit-color-primary-hover`| `--ui-kit-color-action-primary-bg-hovered`  
`--ui-kit-color-primary-active`| `--ui-kit-color-action-primary-bg-pressed`  
`--ui-kit-color-primary-disabled`| `--ui-kit-color-action-bg-disabled`  
`--ui-kit-color-primary-fore`| `--ui-kit-color-action-primary-fg`  
`--ui-kit-color-primary-fore-disabled`| `--ui-kit-color-action-fg-disabled`  
`--ui-kit-color-secondary`| `--ui-kit-color-action-secondary-bg`  
`--ui-kit-color-secondary-hover`| `--ui-kit-color-action-secondary-bg-hovered`  
`--ui-kit-color-secondary-active`| `--ui-kit-color-action-secondary-bg-pressed`  
`--ui-kit-color-secondary-disabled`| `--ui-kit-color-action-bg-disabled`  
`--ui-kit-color-secondary-fore`| `--ui-kit-color-action-secondary-fg`  
`--ui-kit-color-secondary-fore-disabled`| `--ui-kit-color-action-fg-disabled`  
`--ui-kit-color-tertiary`| `--ui-kit-color-action-tertiary-bg`  
`--ui-kit-color-tertiary-hover`| `--ui-kit-color-action-tertiary-bg-hovered`  
`--ui-kit-color-tertiary-active`| `--ui-kit-color-action-tertiary-bg-pressed`  
`--ui-kit-color-tertiary-disabled`| `--ui-kit-color-action-subtle-bg-disabled`  
`--ui-kit-color-tertiary-fore`| `--ui-kit-color-action-tertiary-fg`  
`--ui-kit-color-tertiary-fore-disabled`| `--ui-kit-color-action-subtle-fg-disabled`  
`--ui-kit-color-contrast-hover`| `--ui-kit-color-action-overlay-bg-hovered`  
`--ui-kit-color-contrast-active`| `--ui-kit-color-action-overlay-bg-pressed`  
`--ui-kit-color-contrast-disabled`| `--ui-kit-color-action-overlay-bg-disabled`  
`--ui-kit-color-contrast-fore-disabled`| `--ui-kit-color-action-overlay-fg-disabled`  
`--ui-kit-color-neutral`| `--ui-kit-color-ui-neutral-bg`  
`--ui-kit-color-neutral-hover`| `--ui-kit-color-ui-neutral-strong-bg`  
`--ui-kit-color-neutral-active`| `--ui-kit-color-ui-neutral-bg`  
`--ui-kit-color-neutral-disabled`| `--ui-kit-color-ui-neutral-bg`  
`--ui-kit-color-neutral-fore`| `--ui-kit-color-content-fg`  
`--ui-kit-color-neutral-low`| `--ui-kit-color-ui-neutral-subtle-bg`  
`--ui-kit-color-positive`| `--ui-kit-color-feedback-positive-bg`  
`--ui-kit-color-positive-low`| `--ui-kit-color-feedback-positive-subtle-bg`  
`--ui-kit-color-positive-fore`| `--ui-kit-color-feedback-positive-fg`  
`--ui-kit-color-positive-fore-low`| `--ui-kit-color-feedback-positive-subtle-fg`  
`--ui-kit-color-positive-fore-disabled`| `--ui-kit-color-action-fg-disabled`  
`--ui-kit-color-info`| `--ui-kit-color-feedback-info-bg`  
`--ui-kit-color-info-low`| `--ui-kit-color-feedback-info-subtle-bg`  
`--ui-kit-color-info-fore`| `--ui-kit-color-feedback-info-fg`  
`--ui-kit-color-info-fore-low`| `--ui-kit-color-feedback-info-subtle-fg`  
`--ui-kit-color-warn`| `--ui-kit-color-feedback-warn-bg`  
`--ui-kit-color-warn-low`| `--ui-kit-color-feedback-warn-subtle-bg`  
`--ui-kit-color-warn-fore`| `--ui-kit-color-feedback-warn-fg`  
`--ui-kit-color-warn-fore-low`| `--ui-kit-color-feedback-warn-subtle-fg`  
`--ui-kit-color-warn-fore-disabled`| `--ui-kit-color-action-fg-disabled`  
`--ui-kit-color-critical-hover`| `--ui-kit-color-content-critical-fg`  
`--ui-kit-color-critical-active`| `--ui-kit-color-content-critical-fg`  
`--ui-kit-color-critical-disabled`| `--ui-kit-color-action-bg-disabled`  
`--ui-kit-color-critical-low`| `--ui-kit-color-feedback-critical-subtle-bg`  
`--ui-kit-color-critical-fore-low`| `--ui-kit-color-feedback-critical-subtle-fg`  
`--ui-kit-color-critical-fore-disabled`| `--ui-kit-color-action-fg-disabled`  
`--ui-kit-color-border`| `--ui-kit-color-control-border`  
`--ui-kit-color-border-hover`| `--ui-kit-color-control-border-hovered`  
`--ui-kit-color-border-disabled`| `--ui-kit-color-control-border-disabled`  
`--ui-kit-color-border-critical`| `--ui-kit-color-control-critical-border`  
`--ui-kit-color-border-low`| `--ui-kit-color-ui-border`  
`--ui-kit-color-border-strong`| `--ui-kit-color-control-strong-border`  
`--ui-kit-color-overlay`| `--ui-kit-color-ui-overlay-bg`  
  
Removed V4 variable| Replacement V5 variable  
---|---  
`colorTypographyPrimary`| `colorContentFg`  
`colorTypographySecondary`| `colorContentSubtleFg`  
`colorTypographyTertiary`| `colorContentSubtlestFg`  
`colorTypographyQuaternary`| `colorContentPlaceholderFg`  
`colorTypographyPlaceholder`| `colorContentPlaceholderFg`  
`colorTypographyPositive`| `colorContentPositiveFg`  
`colorTypographyInfo`| `colorContentInfoFg`  
`colorTypographyWarn`| `colorContentWarnFg`  
`colorTypographyCritical`| `colorContentCriticalFg`  
`colorTypographyCriticalHover`| `colorContentCriticalFg`  
`colorTypographyCriticalActive`| `colorContentCriticalFg`  
`colorTypographyLink`| `colorLinkFg`  
`colorTypographyLinkHover`| `colorLinkFgHovered`  
`colorTypographyLinkActive`| `colorLinkFgPressed`  
`colorContrast`| `colorFeedbackOverlayBg`  
`colorContrastFore`| `colorFeedbackOverlayFg`  
`colorNeutralForeDisabled`| `colorHandleBgDisabled`  
`colorNeutralForeLow`| `colorContentFg`  
`colorPositiveHover`| `colorActionSecondaryBgHovered`  
`colorPositiveActive`| `colorActionSecondaryBgPressed`  
`colorPositiveDisabled`| `colorActionBgDisabled`  
`colorInfoHover`| `colorActionSecondaryBgHovered`  
`colorInfoActive`| `colorActionSecondaryBgPressed`  
`colorInfoDisabled`| `colorActionBgDisabled`  
`colorInfoForeDisabled`| `colorActionFgDisabled`  
`colorWarnHover`| `colorActionSecondaryBgHovered`  
`colorWarnActive`| `colorActionSecondaryBgPressed`  
`colorWarnDisabled`| `colorActionBgDisabled`  
`colorCritical`| `colorFeedbackCriticalBg`  
`colorCriticalFore`| `colorFeedbackCriticalFg`  
`colorBorderActive`| `colorActionSelectedBorder`  
`colorPrimary`| `colorActionPrimaryBg`  
`colorPrimaryHover`| `colorActionPrimaryBgHovered`  
`colorPrimaryActive`| `colorActionPrimaryBgPressed`  
`colorPrimaryDisabled`| `colorActionBgDisabled`  
`colorPrimaryFore`| `colorActionPrimaryFg`  
`colorPrimaryForeDisabled`| `colorActionFgDisabled`  
`colorSecondary`| `colorActionSecondaryBg`  
`colorSecondaryHover`| `colorActionSecondaryBgHovered`  
`colorSecondaryActive`| `colorActionSecondaryBgPressed`  
`colorSecondaryDisabled`| `colorActionBgDisabled`  
`colorSecondaryFore`| `colorActionSecondaryFg`  
`colorSecondaryForeDisabled`| `colorActionFgDisabled`  
`colorTertiary`| `colorActionTertiaryBg`  
`colorTertiaryHover`| `colorActionTertiaryBgHovered`  
`colorTertiaryActive`| `colorActionTertiaryBgPressed`  
`colorTertiaryDisabled`| `colorActionSubtleBgDisabled`  
`colorTertiaryFore`| `colorActionTertiaryFg`  
`colorTertiaryForeDisabled`| `colorActionSubtleFgDisabled`  
`colorContrastHover`| `colorActionOverlayBgHovered`  
`colorContrastActive`| `colorActionOverlayBgPressed`  
`colorContrastDisabled`| `colorActionOverlayBgDisabled`  
`colorContrastForeDisabled`| `colorActionOverlayFgDisabled`  
`colorNeutral`| `colorUiNeutralBg`  
`colorNeutralHover`| `colorUiNeutralStrongBg`  
`colorNeutralActive`| `colorUiNeutralBg`  
`colorNeutralDisabled`| `colorUiNeutralBg`  
`colorNeutralFore`| `colorContentFg`  
`colorNeutralLow`| `colorUiNeutralSubtleBg`  
`colorPositive`| `colorFeedbackPositiveBg`  
`colorPositiveLow`| `colorFeedbackPositiveSubtleBg`  
`colorPositiveFore`| `colorFeedbackPositiveFg`  
`colorPositiveForeLow`| `colorFeedbackPositiveSubtleFg`  
`colorPositiveForeDisabled`| `colorActionFgDisabled`  
`colorInfo`| `colorFeedbackInfoBg`  
`colorInfoLow`| `colorFeedbackInfoSubtleBg`  
`colorInfoFore`| `colorFeedbackInfoFg`  
`colorInfoForeLow`| `colorFeedbackInfoSubtleFg`  
`colorWarn`| `colorFeedbackWarnBg`  
`colorWarnLow`| `colorFeedbackWarnSubtleBg`  
`colorWarnFore`| `colorFeedbackWarnFg`  
`colorWarnForeLow`| `colorFeedbackWarnSubtleFg`  
`colorWarnForeDisabled`| `colorActionFgDisabled`  
`colorCriticalHover`| `colorContentCriticalFg`  
`colorCriticalActive`| `colorContentCriticalFg`  
`colorCriticalDisabled`| `colorActionBgDisabled`  
`colorCriticalLow`| `colorFeedbackCriticalSubtleBg`  
`colorCriticalForeLow`| `colorFeedbackCriticalSubtleFg`  
`colorCriticalForeDisabled`| `colorActionFgDisabled`  
`colorBorder`| `colorControlBorder`  
`colorBorderHover`| `colorControlBorderHovered`  
`colorBorderDisabled`| `colorControlBorderDisabled`  
`colorBorderCritical`| `colorControlCriticalBorder`  
`colorBorderLow`| `colorUiBorder`  
`colorBorderStrong`| `colorControlStrongBorder`  
`colorOverlay`| `colorUiOverlayBg`  
  
### Shadow and surface tokens

CSS VariablesCSS Variables

JS VariablesJS Variables

Removed V4 variable| Replacement V5 variable  
---|---  
`--ui-kit-box-shadow-faint`| `--ui-kit-elevation-surface-raised-shadow`  
`--ui-kit-box-shadow-medium`| `--ui-kit-elevation-surface-raised-shadow`  
`--ui-kit-box-shadow-heavy`| `--ui-kit-elevation-surface-floating-shadow`  
`--ui-kit-color-surface`| `--ui-kit-elevation-surface-floating-bg`  
`--ui-kit-color-canvas`| `--ui-kit-elevation-surface-sunken-bg`  
`--ui-kit-color-tabdock`| `--ui-kit-elevation-surface-sunken-bg`  
`--ui-kit-color-page`| `--ui-kit-elevation-surface-bg`  
`--ui-kit-shadow-surface`| `--ui-kit-elevation-surface-raised-shadow`  
`--ui-kit-box-shadow-faint`| `--ui-kit-elevation-surface-raised-shadow`  
`--ui-kit-box-shadow-medium`| `--ui-kit-elevation-surface-raised-shadow`  
`--ui-kit-shadow-surface-high`| `--ui-kit-elevation-surface-floating-shadow`  
`--ui-kit-box-shadow-heavy`| `--ui-kit-elevation-surface-floating-shadow`  
  
Removed V4 variable| Replacement V5 variable  
---|---  
`boxShadowFaint`| `elevationSurfaceRaisedShadow`  
`boxShadowMedium`| `elevationSurfaceRaisedShadow`  
`boxShadowHeavy`| `elevationSurfaceFloatingShadow`  
`colorSurface`| `elevationSurfaceFloatingBg`  
`colorCanvas`| `elevationSurfaceSunkenBg`  
`colorTabdock`| `elevationSurfaceSunkenBg`  
`colorPage`| `elevationSurfaceBg`  
`shadowSurface`| `elevationSurfaceRaisedShadow`  
`shadowSurface`| `elevationSurfaceRaisedShadow`  
`shadowSurface`| `elevationSurfaceRaisedShadow`  
`shadowSurfaceHigh`| `elevationSurfaceFloatingShadow`  
`shadowSurfaceHigh`| `elevationSurfaceFloatingShadow`  
  
### Spacing tokens

CSS VariablesCSS Variables

JS VariablesJS Variables

Removed V4 variable| Replacement V5 variable  
---|---  
`--ui-kit-space-1`| `--ui-kit-space-100`  
`--ui-kit-space-2`| `--ui-kit-space-200`  
`--ui-kit-space-3`| `--ui-kit-space-300`  
`--ui-kit-space-4`| `--ui-kit-space-400`  
`--ui-kit-space-6`| `--ui-kit-space-600`  
`--ui-kit-space-8`| `--ui-kit-space-800`  
`--ui-kit-space-12`| `--ui-kit-space-1200`  
`--ui-kit-border-radius`| `--ui-kit-radius-element-standard`  
  
Removed V4 variable| Replacement V5 variable  
---|---  
`space1`| `space100`  
`space2`| `space200`  
`space3`| `space300`  
`space4`| `space400`  
`space6`| `space600`  
`space8`| `space800`  
`space12`| `space1200`  
`borderRadius`| `radiusElementStandard`  
  
### Component changes

In addition to design token changes, App UI Kit v5 includes several component updates:

#### React version requirement

  * **Breaking** : React 19 is now required and React 18 support was removed.

**Migration** : Update your project to use React v19.




#### Link component

  * **Breaking** : Removed deprecated `title` prop.

**Migration** : Use `tooltipLabel` instead of `title`.



    
    
    // Before (v4)
    
    <Link title="Click here" href="/example">Link text</Link>
    
    
    
    
    // After (v5)
    
    <Link tooltipLabel="Click here" href="/example">Link text</Link>

TSX

Copy

#### ColorSelector component

  * **Breaking** : The `source` parameter in `onChange` callback is now optional.

**Migration** : Check for `undefined` values in your callback handler.



    
    
    // Before (v4)
    
    <ColorSelector onChange={(color, source) => {
    
      // source was always defined
    
      console.log(source);
    
    }} />
    
    
    
    
    // After (v5)
    
    <ColorSelector onChange={(color, source) => {
    
      // source might be undefined
    
      if (source) {
    
        console.log(source);
    
      }
    
    }} />

TSX

Copy

#### Column component

  * **Breaking** : Default `alignY` property changed from implicit to `stretch`.

**Migration** : To use the old behavior, explicitly set `alignY="start"`.



    
    
    // Before (v4) - implicit start alignment
    
    <Column>Content</Column>
    
    
    
    
    // After (v5) - explicit start alignment needed
    
    <Column alignY="start">Content</Column>

TSX

Copy

#### Pill and InputPill components

  * **Breaking** : Replaced `truncateText` prop with `maxWidth` prop.
  * **Breaking** : Changed `size` values: `"small"` is now `"xsmall"`.
  * **Breaking** : Pill has a rounder appearance for consistency with other Canva elements.
  * **Breaking** : Removed `tone` property.


    
    
    // Before (v4)
    
    <Pill size="small" truncateText>Text</Pill>
    
    <InputPill truncateText={false}>Text</InputPill>
    
    
    
    
    // After (v5)
    
    <Pill size="xsmall" maxWidth='25u'>Text</Pill>
    
    <InputPill maxWidth='100%'>Text</InputPill>

TSX

Copy

#### Global styling

  * **Breaking** : Removed the default `colorSurface` background color from the `html` tag.

A migration isn't be required, the Canva environment has changed to accommodate this.




#### New components

  * **Added** : `LinkButton` component for in-app actions that don't open URLs.

Use `LinkButton` instead of `Button` when you need link-style interactions without navigation



