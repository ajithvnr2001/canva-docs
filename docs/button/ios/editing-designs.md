---
url: https://www.canva.dev/docs/button/ios/editing-designs/
title: Editing designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:58.129172+00:00
---

# Editing designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/ios/editing-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/ios/getting-started/)[Creating designs](https://www.canva.dev/docs/button/ios/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/ios/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/ios/editing-designs/)

# Editing designs

Edit an existing design with the iOS SDK.

Copy page

After a user [creates a design](https://www.canva.dev/docs/button/html/creating-designs/), they may want to edit that design at a later point in time. To enable this, Canva provides your app with the ID of the user's design. You can use this ID to re-open the design in the Canva editor.

![](https://www.canva.dev/_next/static/media/edit-design.5ba32f07.png)

This part of the tutorial series explains how to open an existing design with the iOS SDK.

## Step 1: Set up the UI

For the sake of simplicity, this tutorial uses Storyboards to define the UI of the app. This is not required to use the Canva Button.

  1. Open the `Main.storyboard` file.

  2. Add a **Button** to the app.

  3. Open the **Attributes Inspector** for the **Button**.

  4. Uncheck the **State > Enabled** option.

  5. Choose a **Label** for the **Button**.

  6. Create an outlet for the **Button** :
         
         @IBOutlet weak var editDesignButton: UIButton!

SWIFT

Copy

In this case, the outlet is called `editDesignButton`.

  7. Create an action for the **Button** :
         
         @IBAction func editDesign(_ sender: Any) {
         
             // code goes here
         
         }

SWIFT

Copy

In this case, the action is called `editDesign`.




## Step 2: Get the ID of the user's design

In the `ViewController` class, create a property to store the ID of the user's most recent design:
    
    
    var previousDesignId: String?

SWIFT

Copy

Then, when a user creates or publishes a design:

  * Update the value of the `previousDesignId` variable.
  * Enable the `editDesign` button.



The following snippet demonstrates how to do this with the `didPublishDesignWithDesignID` and `didFinishLoadingWithDesignID` methods:
    
    
    func canvaViewController(_ canvaViewController: CanvaViewController, didPublishDesignWithDesignID designID: String?, url: URL?) {
    
        print("Published a design with an ID of \(designID ?? "nil").")
    
    
    
    
        // Download and render the user's image
    
        guard let url = url else { return }
    
        let task = URLSession.shared.dataTask(with: url) { data, urlResponse, error in
    
            guard let downloadedImage = data,
    
            let imageData = Data(base64Encoded: downloadedImage.base64EncodedString())
    
            else { return }
    
                DispatchQueue.main.async {
    
                    self.publishedImageView.image = UIImage(data: imageData)
    
            }
    
        }
    
    
    
    
        task.resume()
    
    
    
    
        // Save the ID of the user's design
    
        previousDesignId = designID
    
    
    
    
        // Enable the "Edit design" button
    
        editDesignButton.isEnabled = true
    
    }
    
    
    
    
    // ...
    
    
    
    
    func canvaViewController(_ canvaViewController: CanvaViewController, didFinishLoadingWithDesignID designID: String) {
    
       // Save the ID of the user's design
    
       previousDesignId = designID
    
    
    
    
       // Enable the "Edit design" button
    
       editDesignButton.isEnabled = true
    
    }

SWIFT

Copy

## Step 3: Create a `CanvaViewController`

Copy the following code into the `editDesign` action:
    
    
    guard let previousDesignId = previousDesignId else  { return }
    
    do {
    
       let configuration = CanvaViewController.Configuration(apiKey: "API KEY GOES HERE")
    
       let canvaViewController = try CanvaViewController(designID: previousDesignId, configuration: configuration)
    
       canvaViewController.delegate = self
    
       canvaViewController.preferredControlTintColor = UIColor(named: "canvaColor")
    
       self.present(canvaViewController, animated: true)
    
    } catch {
    
       print("Something went wrong. Unable to edit design with ID of \(previousDesignId).")
    
       print(error)
    
    }

SWIFT

Copy

The `editDesign` action is almost identical to the code in the `createDesign` action. There's only two differences:

  * The function returns early if `previousDesignId` isn't defined.
  * A `designID` argument is passed into the `CanvaViewController` instead of a `designType`. Canva uses this ID to open the existing design in the editor.



After making these changes: run the app, create a new design, and close the web view. You should be able to re-open the design by clicking the **Edit design** button.

## Example

### ViewController.swift
    
    
    import UIKit
    
    import CanvaButton
    
    
    
    
    class ViewController: UIViewController {
    
    
    
    
        var previousDesignId: String?
    
    
    
    
        @IBOutlet weak var publishedImageView: UIImageView!
    
        @IBOutlet weak var editDesignButton: UIButton!
    
    
    
    
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
    
    
    
    
        @IBAction func editDesign(_ sender: Any) {
    
            guard let previousDesignId = previousDesignId else  { return }
    
            do {
    
               let configuration = CanvaViewController.Configuration(apiKey: "API KEY GOES HERE")
    
               let canvaViewController = try CanvaViewController(designID: previousDesignId!, configuration: configuration)
    
               canvaViewController.delegate = self
    
               canvaViewController.preferredControlTintColor = UIColor(named: "canvaColor")
    
               self.present(canvaViewController, animated: true)
    
            } catch {
    
               print("Something went wrong. Unable to edit design with ID of \(previousDesignId).")
    
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
    
    
    
    
            // Download and render the user's image
    
            guard let url = url else { return }
    
            let task = URLSession.shared.dataTask(with: url) { data, urlResponse, error in
    
                guard let downloadedImage = data,
    
                let imageData = Data(base64Encoded: downloadedImage.base64EncodedString())
    
                else { return }
    
                    DispatchQueue.main.async {
    
                        self.publishedImageView.image = UIImage(data: imageData)
    
                }
    
            }
    
    
    
    
            task.resume()
    
    
    
    
            // Save the ID of the user's design
    
            previousDesignId = designID
    
    
    
    
            // Enable the "Edit design" button
    
            editDesignButton.isEnabled = true
    
        }
    
    
    
    
        func canvaViewDidFailPublish(forDesignID designID: String?, withError error: Error) {
    
            print("Unable to publish design with an ID of \(designID ?? "nil").")
    
            print(error)
    
        }
    
    
    
    
        func canvaViewController(_ canvaViewController: CanvaViewController, didFinishLoadingWithDesignID designID: String) {
    
            print("Opened a design with an ID of \(designID).")
    
            previousDesignId = designID
    
        }
    
    }

SWIFT

Copy
