---
url: https://www.canva.dev/docs/button/android/downloading-designs/
title: Downloading designs - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:56.926029+00:00
---

# Downloading designs - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/android/downloading-designs/

How-to guides

[Getting started](https://www.canva.dev/docs/button/android/getting-started/)[Creating designs](https://www.canva.dev/docs/button/android/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/android/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/android/editing-designs/)

# Downloading designs

Download a published design with the Android SDK.

Copy page

The Canva editor has a **Publish** button. When a user clicks this button, the Android SDK provides your app with:

  * a URL for downloading the user's design as a PNG file
  * the ID of the user's design



This part of the tutorial series explains how to download and render the user's published design.

![](https://www.canva.dev/_next/static/media/publish-ux.6163abc3.png)

## Step 1: Set up the UI

  1. Open the `activity_main.xml` file.

  2. Switch to the **Code** or **Split** view.

  3. Add an `ImageView` element beneath the `Button` element:
         
         <ImageView
         
              android:id="@+id/published_image_view"
         
              android:layout_width="fill_parent"
         
              android:layout_height="fill_parent"
         
              android:layout_marginBottom="16dp" />

MARKUP

Copy

  4. Import the `ImageView` widget into the `MainActivity.kt` file:
         
         import android.widget.ImageView

KOTLIN

Copy




## Step 2: Get the URL of the published design

When a user clicks the **Publish** button in the Canva editor, the app can receive a `PublishData` object.

The `PublishData` object contains:

  * the ID of the user's design
  * a URL for downloading the design as an image file



The URL is in the form `https://export-download.canva.com/<export_file>`. If you're using the China version of the SDK, the TLD is `.cn` instead of `.com`. You can take the necessary security measures to protect the URL from any malicious attacks.

To receive the `PublishData`object:

  1. Add a `publishData` property to the `MainActivity` class:
         
         private var publishData: PublishData? = null

KOTLIN

Copy

  2. Add an `onActivityResult` function to the `MainActivity` class:
         
         override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
         
             super.onActivityResult(requestCode, resultCode, data)
         
         }

KOTLIN

Copy

  3. Use conditionals to detect when the activity is receiving an intent:
         
         override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
         
             super.onActivityResult(requestCode, resultCode, data)
         
         
         
         
             if (data == null) {
         
                 return
         
             }
         
         
         
         
             if (requestCode == 132 && resultCode == RESULT_OK) {
         
                 // The user has published their design...
         
             }
         
         }

KOTLIN

Copy

The value of the `requestCode` variable is based on the integer passed into the `launchActivityForResult` method.

  4. Use the intent's `getParcelableExtra` function to set the value of the `publishData` property:
         
         if (requestCode == 132 && resultCode == RESULT_OK) {
         
             publishData = data.getParcelableExtra<PublishData>(CanvaEditor.KEY_PUBLISH_DATA)
         
         }

KOTLIN

Copy

The object returned by the `getParcelableExtra` function has two properties: `designId` and `publishUrl`.




## Step 3: Render the published design

When a user is taken back to your app, it usually makes sense to download and render the published version of their design. This step explores one way to accomplish this.

### Install Picasso

Picasso is "a powerful image downloading and caching library for Android." It significantly streamlines the process of downloading and rendering an image into an `ImageView` widget. You don't _have_ to use this library, but it can save you from writing some otherwise tedious code.

To install Picasso:

  1. Open the app's `build.gradle` file.

  2. Copy the following statement into the `dependencies` section:
         
         implementation 'com.squareup.picasso:picasso:2.8'

Copy

  3. Click **Sync now**.

  4. Import Picasso into the `MainActivity.kt` file:
         
         import com.squareup.picasso.Picasso

KOTLIN

Copy




To learn more about Picasso, refer to [the official documentation⁠(opens in a new tab or window)](https://square.github.io/picasso/).

### Configure the app's permissions

Add the following element to the `AndroidManifest.xml` file, as a child of the `manifest` element:
    
    
    <uses-permission android:name="android.permission.INTERNET" />

MARKUP

Copy

The presence of this element ensures that the app has permission to download the user's image from the internet. Without this permission, the app can't send HTTP requests.

### Render the image

Copy the following code into the `onActivityResult` function:
    
    
    val publishedImageView = findViewById<ImageView>(R.id.published_image_view)
    
    Picasso.get().load(publishData?.publishUrl).into(publishedImageView)

KOTLIN

Copy

This code uses Picasso to download the user's published design and render it in the `ImageView` widget.

After making these changes: create and publish a design. The published image appears in the app.

## Example

### android_main.xml
    
    
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
    
            <ImageView
    
                android:id="@+id/published_image_view"
    
                android:layout_width="fill_parent"
    
                android:layout_height="fill_parent"
    
                android:layout_marginBottom="16dp" />
    
        </LinearLayout>
    
    
    
    
    </androidx.constraintlayout.widget.ConstraintLayout>

MARKUP

Copy

### AndroidManifest.xml
    
    
    <?xml version="1.0" encoding="utf-8"?>
    
    <manifest
    
        xmlns:android="http://schemas.android.com/apk/res/android"
    
        xmlns:tools="http://schemas.android.com/tools"
    
        package="com.example.myapplication">
    
    
    
    
        <uses-permission android:name="android.permission.INTERNET" />
    
    
    
    
        <application
    
            android:allowBackup="true"
    
            android:icon="@mipmap/ic_launcher"
    
            android:label="@string/app_name"
    
            android:roundIcon="@mipmap/ic_launcher_round"
    
            android:supportsRtl="true"
    
            android:theme="@style/Theme.MyApplication"
    
            tools:replace="android:allowBackup">
    
            <activity android:name=".MainActivity">
    
                <intent-filter>
    
                    <action android:name="android.intent.action.MAIN" />
    
                    <category android:name="android.intent.category.LAUNCHER" />
    
                </intent-filter>
    
            </activity>
    
        </application>
    
    
    
    
    </manifest>

MARKUP

Copy

### build.gradle
    
    
    plugins {
    
        id 'com.android.application'
    
        id 'kotlin-android'
    
    }
    
    
    
    
    android {
    
        compileSdkVersion 30
    
        buildToolsVersion "30.0.2"
    
    
    
    
        defaultConfig {
    
            applicationId "com.example.myapplication"
    
            minSdkVersion 16
    
            targetSdkVersion 30
    
            versionCode 1
    
            versionName "1.0"
    
    
    
    
            testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    
    
    
    
            manifestPlaceholders = [deeplinkScheme: "URL SCHEME GOES HERE"]
    
        }
    
    
    
    
        buildTypes {
    
            release {
    
                minifyEnabled false
    
                proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
    
            }
    
        }
    
        compileOptions {
    
            sourceCompatibility JavaVersion.VERSION_1_8
    
            targetCompatibility JavaVersion.VERSION_1_8
    
        }
    
        kotlinOptions {
    
            jvmTarget = '1.8'
    
        }
    
    }
    
    
    
    
    dependencies {
    
        implementation project(path: ":canva-button-global-release")
    
        implementation 'com.squareup.picasso:picasso:2.8'
    
        implementation "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
    
        implementation 'androidx.core:core-ktx:1.3.2'
    
        implementation 'androidx.appcompat:appcompat:1.2.0'
    
        implementation "androidx.browser:browser:1.0.0"
    
        implementation 'com.google.android.material:material:1.2.1'
    
        implementation 'androidx.constraintlayout:constraintlayout:2.0.4'
    
        testImplementation 'junit:junit:4.+'
    
        androidTestImplementation 'androidx.test.ext:junit:1.1.2'
    
        androidTestImplementation 'androidx.test.espresso:espresso-core:3.3.0'
    
    }

Copy

### MainActivity.kt
    
    
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
    
            }
    
        }
    
    
    
    
        override fun onDestroy() {
    
            super.onDestroy()
    
            disposable?.dispose()
    
        }
    
    }

KOTLIN

Copy
