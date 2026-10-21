---
url: https://www.canva.dev/docs/button/ios/creating-designs/
title: Creating designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.802617+00:00
---

# Creating designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/ios/creating-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/ios/getting-started/)[Creating designs](https://www.canva.dev/docs/button/ios/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/ios/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/ios/editing-designs/)

# Creating designs

Create a new design with the iOS SDK.

Copy page

After [setting up the iOS SDK](https://www.canva.dev/docs/button/html/getting-started/), the next step is to allow users to create a design with the Canva editor. This part of the tutorial series explains how to launch the Canva editor from your app.

![](https://www.canva.dev/_next/static/media/create-design.b8bbad52.png)

## Step 1: Set up the UI

For the sake of simplicity, this tutorial uses Storyboards to define the UI of the app. This is not required to use the Canva Button.

  1. Open the `Main.storyboard` file.

  2. Add a **Button** to the app.

  3. Choose a **Label** for the **Button**.

  4. Create an action for the **Button** :
         
         @IBAction func createDesign(_ sender: Any) {
         
            // code goes here
         
         }

SWIFT

Copy

In this case, the action is called `createDesign`.




## Step 2: Create a `Configuration` object

In the `createDesign` action, create a `CanvaViewController.Configuration` object:
    
    
    @IBAction func createDesign(_ sender: Any) {
    
       let configuration = CanvaViewController.Configuration(apiKey: "API KEY GOES HERE")
    
    }

SWIFT

Copy

You must instantiate this object with your Canva Button API key.

## Step 3: Create a `CanvaViewController`

In the `createDesign` action, create an instance of the `CanvaViewController` class and wrap this code in a do/catch block:
    
    
    @IBAction func createDesign(_ sender: Any) {
    
       do {
    
          let configuration = CanvaViewController.Configuration(apiKey: "API KEY GOES HERE")
    
          let canvaViewController = try CanvaViewController(designType: "BookCover", configuration: configuration)
    
       } catch {
    
          print("Something went wrong. Unable to create a new design.")
    
          print(error)
    
       }
    
    }

SWIFT

Copy

You must instantiate this class with two arguments:

  * `designType` \- This value determines the default dimensions of the user's design and the templates that Canva shows to the user. It's sometimes referred to as the _design type_. For a complete list of design types, refer to [Design types](https://www.canva.dev/docs/button/reference/design-types/).
  * `configuration` \- This value is the `CanvaViewController.Configuration` object.



Next, set the delegate of the `CanvaViewController` to `self` and call the `present` method:
    
    
    @IBAction func createDesign(_ sender: Any) {
    
       do {
    
          let configuration = CanvaViewController.Configuration(apiKey: "API KEY GOES HERE")
    
          let canvaViewController = try CanvaViewController(designType: "BookCover", configuration: configuration)
    
          canvaViewController.delegate = self
    
          self.present(canvaViewController, animated: true)
    
       } catch {
    
          print("Something went wrong. Unable to create a new design.")
    
          print(error)
    
       }
    
    }

SWIFT

Copy

Then build and run the app.

If you click the **Create design** button, Canva opens in a web view. You need to log into Canva to access the editor. Some interactions with the editor, such as opening or publishing a design, log messages to the console.

## Example

### ViewController.swift
    
    
    import UIKit
    
    import CanvaButton
    
    
    
    
    class ViewController: UIViewController {
    
    
    
    
        override func viewDidLoad() {
    
            super.viewDidLoad()
    
        }
    
    
    
    
        @IBAction func createDesign(_ sender: Any) {
    
           do {
    
              let configuration = CanvaViewController.Configuration(apiKey: "API KEY GOES HERE")
    
              let canvaViewController = try CanvaViewController(designType: "BookCover", configuration: configuration)
    
              canvaViewController.delegate = self
    
              self.present(canvaViewController, animated: true)
    
           } catch {
    
              print("Something went wrong. Unable to create a new design.")
    
              print(error)
    
           }
    
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
