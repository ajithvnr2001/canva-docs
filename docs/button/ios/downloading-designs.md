---
url: https://www.canva.dev/docs/button/ios/downloading-designs/
title: Downloading designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.946183+00:00
---

# Downloading designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/ios/downloading-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/ios/getting-started/)[Creating designs](https://www.canva.dev/docs/button/ios/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/ios/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/ios/editing-designs/)

# Downloading designs

Download a published design with the iOS SDK.

Copy page

The Canva editor has a **Publish** button. When a user clicks this button, the iOS SDK provides your app with:

  * a URL for downloading the user's design as a PNG file
  * the ID of the user's design



This part of the tutorial series explains how to download and render the user's published design.

![](https://www.canva.dev/_next/static/media/download-design.0d555d26.png)

## Step 1: Set up the UI

For the sake of simplicity, this tutorial uses Storyboards to define the UI of the app. This is not required to use the Canva Button.

  1. Open the `Main.storyboard` file.

  2. Add a **Image View** to the UI.

  3. Create an outlet for the **Image View** :
         
         @IBOutlet weak var publishedImageView: UIImageView!

SWIFT

Copy




## Step 2: Download (and render) the image

The `didPublishDesignWithDesignID` method runs when a user publishes their design via the Canva editor. It receives a `url` argument, which your app can use to download the published design.

The URL is in the form `https://export-download.canva.com/<export_file>`. If you're using the China version of the SDK, the TLD is `.cn` instead of `.com`. You can take the necessary security measures to protect the URL from any malicious attacks.

The following snippet demonstrates how to download a user's design and render it in an **Image View** :
    
    
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
    
    }

SWIFT

Copy

## Example

### ViewController.swift
    
    
    import UIKit
    
    import CanvaButton
    
    
    
    
    class ViewController: UIViewController {
    
    
    
    
        @IBOutlet weak var publishedImageView: UIImageView!
    
    
    
    
        override func viewDidLoad() {
    
            super.viewDidLoad()
    
        }
    
    
    
    
        @IBAction func createDesign(_ sender: Any) {
    
           do {
    
              let configuration = CanvaViewController.Configuration(apiKey: "API KEY GOES HERE")
    
              let canvaViewController = try CanvaViewController(deisgnType: "BookCover", configuration: configuration)
    
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
