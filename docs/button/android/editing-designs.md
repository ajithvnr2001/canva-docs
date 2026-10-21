---
url: https://www.canva.dev/docs/button/android/editing-designs/
title: Editing designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.568742+00:00
---

# Editing designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/android/editing-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/android/getting-started/)[Creating designs](https://www.canva.dev/docs/button/android/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/android/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/android/editing-designs/)

# Editing designs

Edit an existing design with the Android SDK.

Copy page

After a user [creates a design](https://www.canva.dev/docs/button/html/creating-designs/), they may want to edit that design at a later point in time. To enable this, Canva provides your app with the ID of the user's design. You can use this ID to re-open the design in the Canva editor.

![](https://www.canva.dev/_next/static/media/edit-design-ux.74bd841e.png)

This part of the tutorial series explains how to open an existing design with the Android SDK.

## Step 1: Set up the UI

  1. Open the `activity_main.xml` file.

  2. Switch to the **Code** or **Split** view.

  3. Add a `Button` widget beneath the existing `Button` widget:
         
         <Button
         
             android:id="@+id/edit_design_button"
         
             android:layout_width="fill_parent"
         
             android:layout_height="wrap_content"
         
             android:enabled="false"
         
             android:layout_marginBottom="32dp"
         
             android:text="Edit design" />

MARKUP

Copy

This button should be disabled by default.




## Step 2: Open the Canva editor

In the `MainActivity` class, create a property for the **Edit design** button:
    
    
    private lateinit var editDesignButton: Button

KOTLIN

Copy

Then, in the `onCreate` function, create an on-click listener that opens the user's design in the Canva editor:
    
    
    editDesignButton = findViewById<Button>(R.id.edit_design_button)
    
    editDesignButton.setOnClickListener {
    
       val launcher = CanvaEditor.Launcher
    
                         .builder("API KEY GOES HERE")
    
                         .setDesignId(publishData.designId)
    
    
    
    
       disposable = launcher.launchActivityForResult(this, 132)
    
    }

KOTLIN

Copy

This listener is almost identical to the listener for the **Create design** button. The only difference is that it uses the `setDesignId` method instead of `setDesignType`. This method accepts the ID of a design. Canva uses this ID to open the existing design in the editor.

The `setDesignId` and `setDesignType` methods are mutually exclusive.

## Step 3: Enable the "Edit design" button

In the `onActivityResult` function, enable the button after the user publishes their design:
    
    
    if (requestCode == 132 && resultCode == RESULT_OK) {
    
        publishData = data.getParcelableExtra<PublishData>(CanvaEditor.KEY_PUBLISH_DATA)
    
    
    
    
        if (publishData == null) {
    
            return
    
        }
    
    
    
    
        val publishedImageView = findViewById<ImageView>(R.id.published_image_view)
    
        Picasso.get().load(publishData?.publishUrl).into(publishedImageView)
    
    
    
    
        editDesignButton.isEnabled = true
    
    }

KOTLIN

Copy

## Example

### activity_main.xml
    
    
    <?xml version="1.0" encoding="utf-8"?>
    
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    
        xmlns:app="http://schemas.android.com/apk/res-auto"
    
        xmlns:tools="http://schemas.android.com/tools"
    
        android:layout_width="match_parent"
    
        android:layout_height="match_parent"
    
        tools:context=".MainActivity">
    
    
    
    
        <LinearLayout
    
            xmlns:android="http://schemas.android.com/apk/res/android"
    
            android:layout_width="match_parent"
    
            android:layout_height="match_parent"
    
            android:padding="32dp"
    
            android:orientation="vertical" >
    
            <Button
    
                android:id="@+id/create_design_button"
    
                android:layout_width="fill_parent"
    
                android:layout_height="wrap_content"
    
                android:text="Create design" />
    
            <Button
    
                android:id="@+id/edit_design_button"
    
                android:layout_width="fill_parent"
    
                android:layout_height="wrap_content"
    
                android:enabled="false"
    
                android:layout_marginBottom="32dp"
    
                android:text="Edit design" />
    
            <ImageView
    
                android:id="@+id/published_image_view"
    
                android:layout_width="fill_parent"
    
                android:layout_height="fill_parent"
    
                android:layout_marginBottom="16dp" />
    
        </LinearLayout>
    
    
    
    
    </androidx.constraintlayout.widget.ConstraintLayout>

MARKUP

Copy

#### MainActivity.kt
    
    
    package com.example.myapplication
    
    
    
    
    import android.content.Intent
    
    import android.os.Bundle
    
    import android.widget.Button
    
    import android.widget.ImageView
    
    import androidx.appcompat.app.AppCompatActivity
    
    import com.canva.button.builder.CanvaEditor
    
    import com.canva.button.callbacks.Disposable
    
    import com.canva.button.callbacks.PublishData
    
    import com.squareup.picasso.Picasso
    
    
    
    
    class MainActivity : AppCompatActivity() {
    
        private var disposable: Disposable? = null
    
        private var publishData: PublishData? = null
    
        private lateinit var editDesignButton: Button
    
    
    
    
        override fun onCreate(savedInstanceState: Bundle?) {
    
            super.onCreate(savedInstanceState)
    
            setContentView(R.layout.activity_main)
    
    
    
    
            val createDesignButton = findViewById<Button>(R.id.create_design_button)
    
            createDesignButton.setOnClickListener {
    
                val launcher = CanvaEditor.Launcher
    
                    .builder("API KEY GOES HERE")
    
                    .setDesignType("Banner")
    
    
    
    
                disposable = launcher.launchActivityForResult(this, 132)
    
            }
    
    
    
    
            editDesignButton = findViewById<Button>(R.id.edit_design_button)
    
            editDesignButton.setOnClickListener {
    
                val launcher = CanvaEditor.Launcher
    
                    .builder("API KEY GOES HERE")
    
                    .setDesignId(publishData?.designId)
    
    
    
    
                disposable = launcher.launchActivityForResult(this, 132)
    
            }
    
        }
    
    
    
    
        override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    
            super.onActivityResult(requestCode, resultCode, data)
    
    
    
    
            if (data == null) {
    
                return
    
            }
    
    
    
    
            if (requestCode == 132 && resultCode == RESULT_OK) {
    
                publishData = data.getParcelableExtra<PublishData>(CanvaEditor.KEY_PUBLISH_DATA)
    
    
    
    
                if (publishData == null) {
    
                    return
    
                }
    
    
    
    
                val publishedImageView = findViewById<ImageView>(R.id.published_image_view)
    
                Picasso.get().load(publishData?.publishUrl).into(publishedImageView)
    
    
    
    
                editDesignButton.isEnabled = true
    
            }
    
        }
    
    
    
    
        override fun onDestroy() {
    
            super.onDestroy()
    
            disposable?.dispose()
    
        }
    
    }

KOTLIN

Copy
