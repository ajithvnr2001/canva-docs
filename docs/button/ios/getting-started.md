---
url: https://www.canva.dev/docs/button/ios/getting-started/
title: Getting started - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:58.622248+00:00
---

# Getting started - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/ios/getting-started/

How-to guides

[Getting started](https://www.canva.dev/docs/button/ios/getting-started/)[Creating designs](https://www.canva.dev/docs/button/ios/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/ios/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/ios/editing-designs/)

# Getting started

Add the Canva Button to an iOS app with the iOS SDK.

Copy page

Canva provides an SDK to adding the Canva Button to iOS apps. You can use this SDK to launch the Canva editor from within your app.

Here's how it works:

Your app can open the Canva editor in a browser window. The user then creates or edits a design. When the user clicks the **Publish** button, your app downloads the user's design as an image file.

![](https://www.canva.dev/_next/static/media/app-flow.6deae955.png)

This tutorial series explains how to add the Canva Button to an empty iOS app. Once you understand the workflow, adapt the steps to add the Canva Button to your existing app

## Prerequisites

This tutorial assumes you have an API key to use the Canva Button. If you don't have one, [sign up for an API key](https://www.canva.dev/docs/button/quickstart/#step-1-sign-up-for-an-api-key).

## Step 1: Create an Xcode project

You can skip this step if you're adding the Canva Button to an existing app.

For the sake of simplicity, this tutorial uses Storyboards to define the UI of the app. This is not required to use the Canva Button.

  1. Open Xcode.
  2. Select **File > New > Project**.
  3. Select **iOS > App**.
  4. Select **Next**.
  5. Select **Interface > Storyboard**.
  6. Select **Life Cycle > UIKit App Delegate**.
  7. Select **Language > Swift**.
  8. Select **Next**.
  9. Choose a location for the project.



## Step 2: Install the Canva Button SDK

### Carthage

Coming soon.

### Cocoapods

  1. Copy the following code snippet into the project's `Podfile`:
         
         use_frameworks!
         
         
         
         
         target 'YourApp' do
         
           pod 'Canva.DesignButton'
         
         end

BASH

Copy

  2. Run `pod update`.




If you're using the `china` version of the SDK, replace `Canva.DesignButton` with `Canva-cn.DesignButton`.

### Manual

#### Add the framework to the project

  1. Download and extract the `CanvaButton.tar.gz` file. You should have received this file from Canva. The archive contains a `CanvaButton.framework` file, along with `.bcsymbolmap` and `.dSYM` files.
  2. Drag the `CanvaButton.framework` file into the Xcode project.
  3. In the **Navigator** , select the project.
  4. Under the **Targets** heading, select the target.
  5. Switch to the **General** tab.
  6. In the **Frameworks, Libraries and Embedded content** section, add the `CanvaButton.framework` file.
  7. Set the **Embed** option to **Embed & Sign**.



![](https://www.canva.dev/_next/static/media/embed-sign.b395d9fc.png)

#### Copy files at build time

  1. Switch to the **Build Phases** tab.
  2. Click the **+** button.
  3. Select **New Copy Files Phase**.
  4. Expand the **Copy Files** panel.
  5. Set the **Destination** to **Products Directory**.
  6. Add the `.bcsymbolmap` and `.dSYM` files to the list of copied files.



#### Run a script at build time

  1. Click the **+** button.

  2. Select **New Run Script Phase**.

  3. Expand the **Run Script** panel.

  4. Copy the following command into the script editor:
         
         bash "${BUILT_PRODUCTS_DIR}/${FRAMEWORKS_FOLDER_PATH}/CanvaButton.framework/strip.sh" "${BUILT_PRODUCTS_DIR}"

BASH

Copy

  5. Enable **For install builds only**.




## Step 3: Set up custom URL schemes

Canva uses [custom URL schemes⁠(opens in a new tab or window)](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app) to send information from the Canva editor to your app. URL schemes are unique values that are tied to your Canva Button API key. Canva should have already provided you with this scheme.

To set up the custom URL schemes for your app:

  1. Open the `Info.plist` file.
  2. Create a **String** property with a **Key** of `CanvaButtonScheme`.
  3. Set the URL scheme as the value of the following properties: 
     * **CanvaButtonScheme**
     * **URL Types > Item 0 > URL Schemes > Item 0**



![](https://www.canva.dev/_next/static/media/info-plist.8123974a.png)

The iOS and Android SDKs each have their own, distinct URL schemes.

## Step 4: Handle custom URL schemes

The iOS SDK provides two functions for handling custom URL schemes:

  * `isInternalURL`
  * `handleInternalURL`



You can use these functions to execute behavior in response to the information that Canva sends to your app. The exact implementation on whether or not your app uses [scenes⁠(opens in a new tab or window)](https://developer.apple.com/documentation/uikit/app_and_environment/scenes).

### With scenes

If your app uses scenes, import the `CanvaButton` module into the `SceneDelegate.swift` file:
    
    
    import CanvaButton

SWIFT

Copy

Then copy the following code into the `SceneDelegate` class:
    
    
    func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    
        for context in URLContexts {
    
            if CanvaButton.isInternalURL(context.url) {
    
                CanvaButton.handleInternalURL(context.url)
    
            }
    
        }
    
    }

SWIFT

Copy

### Without scenes

If your app doesn't use scenes, import the `CanvaButton` module into the `AppDelegate.swift` file:
    
    
    import CanvaButton

SWIFT

Copy

Then copy the following code into the `AppDelegate` class:
    
    
    func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    
        if CanvaButton.isInternalURL(url) {
    
            CanvaButton.handleInternalURL(url)
    
        }
    
    
    
    
        return true
    
    }

SWIFT

Copy

## Step 5: Implement the `CanvaViewControllerDelegate` protocol

When a user opens and interacts with the Canva editor, the SDK sends information to your app. To receive this information, import the `CanvaButton` module into the `ViewController.swift` file:
    
    
    import CanvaButton

SWIFT

Copy

Then copy the following code into the `ViewController.swift` file:
    
    
    extension ViewController: CanvaViewControllerDelegate {
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didFailToLoadWithError error: Error) {
    
            print("Unable to load Canva editor.")
    
            print(error)
    
        }
    
    
    
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didTerminateLoadingForDesignID designID: String?) {
    
            print("Unable to open design with an ID of \(designID ?? "nil").")
    
        }
    
    
    
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didPublishDesignWithDesignID designID: String?, url: URL?) {
    
            print("Published a design with an ID of \(designID ?? "nil").")
    
        }
    
    
    
    
        func canvaViewDidFailPublish(forDesignID designID: String?, withError error: Error) {
    
            print("Unable to publish design with an ID of \(designID ?? "nil").")
    
            print(error)
    
        }
    
    
    
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didFinishLoadingWithDesignID designID: String) {
    
            print("Opened a design with an ID of \(designID).")
    
        }
    
    }

SWIFT

Copy

This code extends the `ViewController` class and implements the `CanvaViewControllerDelegate` protocol.

Based on this change, the following methods run throughout the lifecycle of the app:

  * `didFailToLoadWithError`
  * `didTerminateLoadingForDesignID`
  * `didPublishDesignWithDesignID`
  * `canvaViewDidFailPublish`
  * `didFinishLoadingWithDesignID`



The behavior of these methods is explained throughout this tutorial.

## Example

### AppDelegate.swift
    
    
    import UIKit
    
    import CanvaButton
    
    
    
    
    @main
    
    class AppDelegate: UIResponder, UIApplicationDelegate {
    
    
    
    
        func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    
            if CanvaButton.isInternalURL(url) {
    
                CanvaButton.handleInternalURL(url)
    
            }
    
    
    
    
            return true
    
        }
    
    
    
    
        func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    
            return true
    
        }
    
    
    
    
        func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration {
    
            return UISceneConfiguration(name: "Default Configuration", sessionRole: connectingSceneSession.role)
    
        }
    
    
    
    
    }

SWIFT

Copy

### SceneDelegate.swift
    
    
    import UIKit
    
    import CanvaButton
    
    
    
    
    class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    
    
    
    
        var window: UIWindow?
    
    
    
    
        func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    
            for context in URLContexts {
    
                if CanvaButton.isInternalURL(context.url) {
    
                    CanvaButton.handleInternalURL(context.url)
    
                }
    
            }
    
        }
    
    
    
    
        func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
    
            guard let _ = (scene as? UIWindowScene) else { return }
    
        }
    
    
    
    
    }

SWIFT

Copy

### ViewController.swift
    
    
    import UIKit
    
    import CanvaButton
    
    
    
    
    class ViewController: UIViewController {
    
    
    
    
        override func viewDidLoad() {
    
            super.viewDidLoad()
    
        }
    
    
    
    
    }
    
    
    
    
    extension ViewController: CanvaViewControllerDelegate {
    
    
    
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didFailToLoadWithError error: Error) {
    
            print("Unable to load Canva editor.")
    
            print(error)
    
        }
    
    
    
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didTerminateLoadingForDesignID designID: String?) {
    
            print("Unable to open design with an ID of \(designID ?? "nil").")
    
        }
    
    
    
    
    
    
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didPublishDesignWithDesignID designID: String?, url: URL?) {
    
            print("Published a design with an ID of \(designID ?? "nil").")
    
        }
    
    
    
    
        func canvaViewDidFailPublish(forDesignID designID: String?, withError error: Error) {
    
            print("Unable to publish design with an ID of \(designID ?? "nil").")
    
            print(error)
    
        }
    
    
    
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didFinishLoadingWithDesignID designID: String) {
    
            print("Opened a design with an ID of \(designID).")
    
        }
    
    
    
    
    }

SWIFT

Copy
