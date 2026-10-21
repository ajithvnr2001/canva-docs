---
url: https://www.canva.dev/blog/developers/building-with-content-publisher-part1/
title: Meet the Content Publisher Intent - Part 1 - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:04.098051+00:00
---

# Meet the Content Publisher Intent - Part 1 - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/building-with-content-publisher-part1/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Content Publisher Intent

# Meet the Content Publisher Intent - Part 1

Understanding data flow and structure for publishing

![](https://www.canva.dev/_next/static/media/thumbnail.c59330ae.jpg)

* * *

  * 


[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Feb 19, 2026

* * *

Meet our new way to Publish from Canva - the Content Publisher Intent. It's a powerful, updated foundation for integrating Canva with external content systems, from social media to asset management. Whether you're connecting to a digital asset management (DAM) platform, a brand portal, or an enterprise content repository, the Content Publisher intent provides the infrastructure to streamline exporting Canva designs.

This is Part 1 of a 3-part series on building asset management integrations with Content Publisher. In this post, we'll explore how data flows through the publishing process and how to design the custom settings structure that powers your asset organization.

* * *

> Series Overview:
> 
> Part 1 (this post): Understanding data flow and structure for publishing
> 
> [Part 2: Building Settings UIs and UI patterns for asset organization](https://www.canva.dev/blog/developers/building-with-content-publisher-part2/)
> 
> [Part 3: Complete implementation, Preview UIs, and publishing](https://www.canva.dev/blog/developers/building-with-content-publisher-part3/)

* * *

## Understanding the Content Publisher Flow

The Content Publisher intent follows a four-step flow, with data passing between Canva and your app at each stage:

  1. getPublishConfiguration → Define what content types you accept
  2. renderSettingsUi → Collect custom metadata from the user
  3. renderPreviewUi → Show a preview before publishing
  4. publishContent → Send files + metadata to your DAM



Let's explore what data flows through each step.

### Step 1: getPublishConfiguration

**What happens:** Canva asks your app what output types you support.

**Data flow:** You → Canva

You define the output types (file formats, aspect ratios, etc.) that your DAM accepts:
    
    
    async function getPublishConfiguration() {
    
      return {
    
        status: 'completed',
    
        outputTypes: [
    
          {
    
            id: 'image_asset',
    
            displayName: 'Image Asset',
    
            mediaSlots: [{
    
              id: 'media',
    
              displayName: 'Media',
    
              fileCount: { min: 1, max: 10 },
    
              accepts: {
    
                image: { format: 'png' }
    
              }
    
            }]
    
          }
    
        ]
    
      };
    
    }

TSX

Copy

`fileCount` max is rate limited to 10. You can't export more than 10 files at a time.

### Step 2: renderSettingsUi - Collecting custom metadata

**What happens:** User provides metadata for organizing the asset in your DAM.

**Data flow:** User → Your UI → `publishRef` (stored by Canva)

This is where you collect whatever information your DAM needs. You store it in `publishRef`:
    
    
    function SettingsUI({ updatePublishSettings }) {
    
      const [settings, setSettings] = useState<PublishSettings>({
    
        destinationFolder: '',
    
        category: '',
    
        tags: [],
    
        description: ''
    
      });
    
    
    
    
      const setAndPropagateSettings = useCallback(
    
        (updatedSettings: PublishSettings) => {
    
          setSettings(updatedSettings);
    
          updatePublishSettings({
    
            publishRef: JSON.stringify(updatedSettings),
    
            validityState: validatePublishRef(updatedSettings),
    
          });
    
        },
    
        [updatePublishSettings],
    
      );
    
      
    
      return (
    
        <Rows spacing="2u">
    
          <FormField
    
            label="Folder to save to"
    
            control={(props) => (
    
              <Select
    
                {...props}
    
                options={[
    
                  //populate from folder structure
    
                ]}
    
                searchable
    
                stretch
    
              />
    
            )}
    
          />
    
          {/* More fields... */}
    
        </Rows>
    
      );
    
    }

TSX

Copy

**Key concept:** `publishRef` is a string (max 32KB) where you store any data structure you want. Design it based on your DAM's requirements.

### Step 3: `renderPreviewUi` \- Showing What Will Be Published

**What happens:** User confirms settings before publishing.

**Data flow:** Canva → Your Preview UI

You receive preview media and the `publishRef` you saved:
    
    
    function PreviewUI({ invocationContext, registerOnPreviewChange }) {
    
      const [previewData, setPreviewData] = useState<{
    
        previewMedia: PreviewMedia[];
    
        outputType: OutputType;
    
        publishRef?: string;
    
      } | null>(null);
    
      
    
      useEffect(() => {
    
        const dispose = registerOnPreviewChange((data) => {
    
          setPreviewData(data);
    
        });
    
        return dispose;
    
      }, [registerOnPreviewChange]);
    
    
    
    
      const { previewMedia, publishRef, outputType } = previewData ?? {};
    
      const publishSettings = parsePublishSettings(publishRef);
    
      
    
      return (
    
        <Box spacing="2u">
    
          <Text>Publishing to: {publishSettings.destinationFolder}</Text>
    
          {previewMedia.map(preview => <ImageCard thumbnailUrl={preview.url} />)}
    
        </Box>
    
      );
    
    }

TSX

Copy

### Step 4: publishContent - Sending to Your DAM

**What happens:** Files are exported and sent to your backend with metadata.

**Data flow:** Canva → Your backend

You receive two sources of metadata:

**Your Custom Settings:`publishRef`**

This contains the settings you collected in Step 2:
    
    
    async function publishContent(request: PublishContentRequest) {
    
      // Parse YOUR custom settings
    
      const settings = request.publishRef 
    
        ? JSON.parse(request.publishRef)
    
        : {};
    
      
    
      console.log(settings.destinationFolder); // "/Marketing/Q1-2024"
    
      console.log(settings.category);          // "social"
    
      console.log(settings.tags);              // ["campaign", "instagram"]
    
    }

TSX

Copy

**Canva's Design Metadata:`contentMetadata`**

Canva automatically provides metadata about the source design on each file:
    
    
    async function publishContent(request: PublishContentRequest) {
    
      const file = request.outputMedia[0].files[0];
    
      
    
      // Canva provides this automatically
    
      const canvaMetadata = file.contentMetadata;
    
      
    
      console.log(canvaMetadata.title);        // "Product Launch Hero"
    
      console.log(canvaMetadata.designToken);  // "eyJhbGc..."
    
      console.log(canvaMetadata.pages);        // [{ pageId, pageNumber }]
    
    }

TSX

Copy

Design `title` is not available until the Publish action has been taken by the user. You can use the `designToken` on your platform with a Canva Connect Integration to reopen the design with your app.

**Using Both Together**

Combine your custom settings with Canva's metadata when uploading to your DAM:
    
    
    async function publishContent(request: PublishContentRequest) {
    
      // YOUR custom settings
    
      const customSettings = request.publishRef 
    
        ? JSON.parse(request.publishRef) 
    
        : {};
    
      
    
      const files = request.outputMedia[0]?.files ?? [];
    
      
    
      for (const file of files) {
    
        // CANVA's design metadata
    
        const designMetadata = file.contentMetadata;
    
        
    
        // Upload to your DAM with both
    
        await uploadToDAM({
    
          // Download URL for the exported file
    
          downloadUrl: file.url,
    
          
    
          // From YOUR settings (publishRef)
    
          destinationFolder: customSettings.destinationFolder,
    
          category: customSettings.category,
    
          tags: customSettings.tags,
    
          description: customSettings.description,
    
          
    
          // From CANVA (contentMetadata)
    
          originalDesignTitle: designMetadata.title,
    
          designToken: designMetadata.designToken,
    
          pageNumber: designMetadata.pages[0]?.pageNumber,
    
          
    
          // From the file itself
    
          width: file.widthPx,
    
          height: file.heightPx,
    
          format: file.format
    
        });
    
      }
    
      
    
      return {
    
        status: 'completed',
    
        externalUrl: `https://yourdam.com/assets/${customSettings.destinationFolder}`
    
      };
    
    }

TSX

Copy

**Key Distinctions:`publishRef` vs `contentMetadata`**

Aspect| `publishRef`| `contentMetadata`  
---|---|---  
Controlled by| You (the developer)| Canva (automatic)  
Structure| Whatever you design| Fixed by Canva  
Purpose| Store custom publish settings| Provide content context  
Created in| `renderSettingsUi()`| Automatically by Canva  
Received in| `publishContent(request.publishRef)`| `publishContent(request.outputMedia[].files[].contentMetadata)`  
Contains| Folder, tags, category, custom fields| Design title, token, pages  
Max size| 32KB| N/A  
  
## Designing Your publishRef Structure

The structure of `publishRef` is entirely up to you - design it based on your DAM system's requirements. Here is an example pattern:
    
    
    interface ContentSettings {
    
      folder: string;
    
      tags: string[];
    
      description: string;
    
    }

TSX

Copy

### Best Practices for `publishRef` Design

  1. Start Simple, Grow As Needed

Begin with the minimum viable structure:
         
         interface MinimalSettings {
         
           folder: string;
         
           tags: string[];
         
         }
         
         
         
         
         updatePublishSettings({
         
           publishRef: JSON.stringify({ folder: '/Marketing', tags: ['campaign'] }),
         
           validityState: 'valid'
         
         });

TSX

Copy

Add fields only when you have clear use cases:
         
         interface ExpandedSettings {
         
           folder: string;
         
           tags: string[];
         
           // Added after user feedback
         
           projectId?: string;
         
           // Added for compliance
         
           expiryDate?: string;
         
         }

TSX

Copy

  2. Make Required Fields Obvious
         
         interface WellDesignedSettings {
         
           // Required fields (no ? suffix)
         
           destinationFolder: string;
         
           category: string;
         
           
         
           // Optional fields (? suffix)
         
           tags?: string[];
         
           projectId?: string;
         
           description?: string;
         
         }
         
         
         
         
         // Validate before allowing publish
         
         const isValid = settings.destinationFolder && settings.category;
         
         updatePublishSettings({
         
           publishRef: JSON.stringify(settings),
         
           validityState: isValid ? 'valid' : 'invalid_missing_required_fields'
         
         });

TSX

Copy

  3. Use TypeScript Types for Controlled Vocabularies

Instead of free-text:
         
         category: string; // ❌ User can enter anything

TSX

Copy

Use union types:
         
         category: 'marketing' | 'brand' | 'product' | 'social'; // ✅ Controlled values

TSX

Copy

  4. Consider Your Backend's Needs

Your `publishRef` structure should make it easy for your backend to:

     * Store assets in the right location
     * Apply the correct permissions
     * Enable search and filtering
     * Track assets over time
    
    interface BackendFriendlySettings {
    
      // Easy to map to storage path
    
      folderPath: string; // "/clients/acme/2024/campaign"
    
      
    
      // Easy to index for search
    
      tags: string[];
    
      
    
      // Easy to apply permissions
    
      department: string;
    
      visibility: 'public' | 'internal' | 'restricted';
    
    }
    
    
    
    
    // In publishContent
    
    const settings = JSON.parse(request.publishRef) as BackendFriendlySettings;
    
    const storagePath = settings.folderPath;
    
    const searchIndex = { tags: settings.tags, department: settings.department };

TSX

Copy

  5. Plan for Custom Fields

Different teams often need different metadata. Build flexibility in:
         
         interface FlexibleSettings {
         
           // Standard fields all assets need
         
           folder: string;
         
           category: string;
         
           tags: string[];
         
           
         
           // Custom fields specific to your use case
         
           customFields?: {
         
             [key: string]: string | number | boolean | string[];
         
           };
         
         }
         
         
         
         
         // Example usage in Settings UI
         
         const settings: FlexibleSettings = {
         
           folder: "/marketing",
         
           category: "social",
         
           tags: ["campaign"],
         
           customFields: {
         
             targetAudience: "enterprise",
         
             performanceGoal: "awareness",
         
             estimatedReach: 50000
         
           }
         
         };
         
         
         
         
         updatePublishSettings({
         
           publishRef: JSON.stringify(settings),
         
           validityState: 'valid'
         
         });

TSX

Copy

  6. Remember the 32KB Limit

`publishRef` has a maximum size of 32KB. Keep it reasonable:
         
         // ❌ Too much data
         
         const bloatedSettings = {
         
           folder: '/path',
         
           // Don't include large data
         
           fullDesignData: '...',  // Too large!
         
           allUserHistory: [...],   // Too large!
         
           base64Image: '...'       // Too large!
         
         };
         
         
         
         
         // ✅ Just the essentials
         
         const efficientSettings = {
         
           folder: '/Marketing/Q1',
         
           category: 'social',
         
           tags: ['campaign', 'instagram'],
         
           projectId: 'PROJ-2024-001'
         
         };

TSX

Copy




## Validating Your Structure

Before implementing, validate your `publishRef` design.

Questions to Ask:

  1. Can users easily provide this information? 
     * Is it obvious where to find each value?
     * Are there too many required fields?
  2. Does it match how users think? 
     * Use their terminology, not technical jargon
     * Organize fields in logical groups
  3. Will it scale? 
     * What happens when you have 10,000 assets?
     * Can you add new fields without breaking existing integrations?
  4. Is it maintainable? 
     * Can you update controlled vocabularies (like categories)?
     * How do you handle structure changes?
  5. Does it fit in 32KB? 
     * Even with lots of tags and custom fields?
     * Have you tested with realistic data?



### Validation Example
    
    
    interface AssetSettings {
    
      folder: string;
    
      category: string;
    
      tags: string[];
    
      description?: string;
    
    }
    
    
    
    
    // Validation function for your Settings UI
    
    function validateSettings(settings: Partial<AssetSettings>): {
    
      isValid: boolean;
    
      errors: string[];
    
    } {
    
      const errors: string[] = [];
    
      
    
      if (!settings.folder) {
    
        errors.push('Destination folder is required');
    
      }
    
      
    
      if (!settings.category) {
    
        errors.push('Category is required');
    
      }
    
      
    
      if (settings.tags && settings.tags.length > 10) {
    
        errors.push('Maximum 10 tags allowed');
    
      }
    
      
    
      if (settings.description && settings.description.length > 500) {
    
        errors.push('Description must be less than 500 characters');
    
      }
    
      
    
      // Check serialized size
    
      const serialized = JSON.stringify(settings);
    
      if (serialized.length > 32000) { // 32KB
    
        errors.push('Settings exceed 32KB limit');
    
      }
    
      
    
      return {
    
        isValid: errors.length === 0,
    
        errors
    
      };
    
    }
    
    
    
    
    // Use in Settings UI
    
    function SettingsUI({ updatePublishSettings }) {
    
      const [settings, setSettings] = useState<AssetSettings>({
    
        folder: '',
    
        category: '',
    
        tags: [],
    
        description: ''
    
      });
    
      
    
      const setAndPropagateSettings = useCallback(
    
        (updatedSettings: PublishSettings) => {
    
          const settingsValidationResult = validateSettings(updatedSettings)
    
          setSettings(updatedSettings);
    
          updatePublishSettings({
    
            publishRef: JSON.stringify(updatedSettings),
    
            validityState: settingsValidationResult.isValid ? 'valid' : 'invalid_missing_required_fields',
    
          });
    
        },
    
        [updatePublishSettings],
    
      );
    
    }

TSX

Copy

## What's Next

Now that you understand how data flows through the Content Publisher intent and how to design a publishRef structure for your DAM system, the next step is building the UI to collect this information from users.

In Part 2, we'll cover:

  * Building Settings UIs that collect your custom settings
  * Advanced UI patterns (hierarchical folders, tag suggestions, context-aware defaults)
  * Multi-page asset organization patterns
  * How to properly use updatePublishSettings to save your data



We'll take the `publishRef` structures from this post and turn them into intuitive user interfaces within Canva.

## Key Takeaways

  1. **Data flows through four stages:** `getPublishConfiguration` → `renderSettingsUi` → `renderPreviewUi` → `publishContent`
  2. **You control`publishRef`:** This is where you store custom settings collected in your Settings UI (folder, tags, category, etc.)
  3. **Canva provides`contentMetadata`:** Automatically included on each exported file with design title, token, and page info
  4. **Design for your DAM:** Structure `publishRef` based on how your DAM organizes and discovers assets
  5. **Keep it under 32KB:** The `publishRef` string has a size limit, so keep it focused on essential metadata



## Resources

  * [Content Publisher Intent Overview](https://www.canva.dev/docs/apps/intents/content-publisher/)
  * [App UI Kit Documentation⁠(opens in a new tab or window)](https://www.canva.dev/docs/apps/app-ui-kit/)
  * [Content Publisher Example App⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-apps-sdk-starter-kit/tree/main/examples/intents/content_publisher_intent)



## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.eab8445b.png)](https://www.canva.dev/blog/developers/spotlight-on-the-background/)

[BackgroundSpotlight on the background](https://www.canva.dev/blog/developers/spotlight-on-the-background/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Jan 22, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.050298fa.jpg)](https://www.canva.dev/blog/developers/launching-new-ways-to-build/)

[Apps SDKUnlock new ways to build for Canva Apps MarketplaceLaunching Data Connectors and Design Editing to enable more complex app use cases.](https://www.canva.dev/blog/developers/launching-new-ways-to-build/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Jun 25, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.dbaf156a.jpg)](https://www.canva.dev/blog/developers/getting-started-guide/)

[Canva ExtendGetting Started GuideGet ready for Canva Extend by following our tips to get started.](https://www.canva.dev/blog/developers/getting-started-guide/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Jun 14, 2023
