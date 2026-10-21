---
url: https://www.canva.dev/docs/button/android/creating-designs/
title: Creating designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:56.669040+00:00
---

# Creating designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/android/creating-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/android/getting-started/)[Creating designs](https://www.canva.dev/docs/button/android/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/android/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/android/editing-designs/)

# Creating designs

Create a new design with the Android SDK.

Copy page

After [setting up the Android SDK](https://www.canva.dev/docs/button/html/getting-started/), the next step is to allow users to create a design with the Canva editor. This part of the tutorial series explains how to launch the Canva editor from your app.

![](https://www.canva.dev/_next/static/media/create-ux.d5d6936d.png)

## Step 1: Set up the UI

  1. Open the `activity_main.xml` file.

  2. Switch to the **Code** or **Split** view.

  3. Replace the `TextView` element with the following code:
         
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
         
         </LinearLayout>

MARKUP

Copy

This code adds a **Create design** button to the UI. The `LinearLayout` element ensures that additional elements are nicely stacked within the UI.




## Step 2: Open the Canva editor

  1. Copy the following statements into the `MainActivity.kt` file:
         
         import android.content.Intent
         
         import android.widget.Button
         
         import com.canva.button.builder.CanvaEditor
         
         import com.canva.button.callbacks.Disposable
         
         import com.canva.button.callbacks.PublishData

KOTLIN

Copy

  2. In the `onCreate` function, add an on-click listener to the **Create design** button:
         
         class MainActivity : AppCompatActivity() {
         
             override fun onCreate(savedInstanceState: Bundle?) {
         
                 super.onCreate(savedInstanceState)
         
                 setContentView(R.layout.activity_main)
         
         
         
         
                 // Set up the "Create design" button
         
                 val createDesignButton = findViewById<Button>(R.id.create_design_button)
         
                 createDesignButton.setOnClickListener {
         
                     // code goes here
         
                 }
         
             }
         
         }

KOTLIN

Copy

  3. In the on-click listener, use the `builder` method to create a `CanvaEditor.Builder` object:
         
         createDesignButton.setOnClickListener {
         
             val launcher = CanvaEditor.Launcher.builder("API KEY GOES HERE")
         
         }

KOTLIN

Copy

Be sure to replace `API KEY GOES HERE` with your API key.

  4. Use the `setDesignType` method to set the _design type_ of the design:
         
         createDesignButton.setOnClickListener {
         
             val launcher = CanvaEditor.Launcher
         
                                 .builder("API KEY GOES HERE")
         
                                 .setDesignType("Banner")
         
         }

KOTLIN

Copy

The design type determines the default dimensions of the user's design and the templates that Canva shows to the user. For a complete list of design types, refer to [Design types](https://www.canva.dev/docs/button/reference/design-types/).

  5. Launch the editor with the `launchActivityForResult` method:
         
         launcher.launchActivityForResult(this, 132)

KOTLIN

Copy

The first argument is the current activity. The second argument is a _request code_. This code is required to [get the result from an activity⁠(opens in a new tab or window)](https://developer.android.com/training/basics/intents/result). The request code must be a unique integer. The integer `132` has no special meaning.




Based on these changes, clicking the **Create design** button opens Canva in the browser. If you're already logged into Canva, the editor immediately loads. Otherwise, you need to to sign up for or log into an account.

If the Canva editor fails to load, verify that the API key is valid.

## Step 3: Clean-up the on-click listener

  1. Add a `disposable` property to the `MainActivity` class:
         
         private var disposable: Disposable? = null

KOTLIN

Copy

  2. In the on-click listener, set the `disposable` property to the value returned by the `launchActivityForResult` method:
         
         disposable = launcher.launchActivityForResult(this, 132)

KOTLIN

Copy

  3. Add an `onDestroy` method to the class and call the `dispose` method on the `disposable` property:
         
         override fun onDestroy() {
         
             super.onDestroy()
         
             disposable?.dispose()
         
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
    
        </LinearLayout>
    
    
    
    
    </androidx.constraintlayout.widget.ConstraintLayout>

MARKUP

Copy

### MainActivity.kt
    
    
    package com.example.myapplication
    
    
    
    
    import android.content.Intent
    
    import android.os.Bundle
    
    import android.widget.Button
    
    import androidx.appcompat.app.AppCompatActivity
    
    import com.canva.button.builder.CanvaEditor
    
    import com.canva.button.callbacks.Disposable
    
    import com.canva.button.callbacks.PublishData
    
    
    
    
    class MainActivity : AppCompatActivity() {
    
        private var disposable: Disposable? = null
    
    
    
    
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
    
        }
    
    
    
    
        override fun onDestroy() {
    
            super.onDestroy()
    
            disposable?.dispose()
    
        }
    
    }

KOTLIN

Copy
