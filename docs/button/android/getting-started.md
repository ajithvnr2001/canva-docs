---
url: https://www.canva.dev/docs/button/android/getting-started/
title: Getting started - How-to guides - Canva Button Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:57.066031+00:00
---

# Getting started - How-to guides - Canva Button Documentation

> Source: https://www.canva.dev/docs/button/android/getting-started/

How-to guides

[Getting started](https://www.canva.dev/docs/button/android/getting-started/)[Creating designs](https://www.canva.dev/docs/button/android/creating-designs/)[Downloading designs](https://www.canva.dev/docs/button/android/downloading-designs/)[Editing designs](https://www.canva.dev/docs/button/android/editing-designs/)

# Getting started

Add the Canva Button to an Android app with the Android SDK.

Copy page

Canva provides an SDK for adding the Canva Button to Android apps. You can use this SDK to launch the Canva editor from within your app.

Here's how it works:

Your app opens the Canva editor in a [Custom Tab⁠(opens in a new tab or window)](https://developers.google.com/web/android/custom-tabs). The user then creates or edits a design. When the user clicks the **Publish** button, your app downloads the user's design as an image file.

![](https://www.canva.dev/_next/static/media/android-ux.ca4a94f5.png)

This tutorial series explains how to add the Canva Button to an empty Android app. Once you understand the workflow, adapt the steps to add the Canva Button to your existing app.

## Prerequisites

This tutorial assumes you have an API key to use the Canva Button. If you don't have one, [sign up for an API key](https://www.canva.dev/docs/button/quickstart/#step-1-sign-up-for-an-api-key).

## Step 1: Create a project in Android Studio

You can skip this step if you're adding the Canva Button to an existing app.

  1. Open **Android Studio**.
  2. Select **Create New Project**.
  3. Select **Empty Activity**.
  4. Select **Next**.
  5. (Optional) Choose a **Name** for the application.
  6. (Optional) Choose a **Package name** for the application.
  7. Select **Language > Kotlin**.
  8. Select **Minimum SDK > API 16**.
  9. Select **Finish**.



This is the default `MainActivity.kt` file:
    
    
    package com.example.myapplication
    
    
    
    
    import androidx.appcompat.app.AppCompatActivity
    
    import android.os.Bundle
    
    
    
    
    class MainActivity : AppCompatActivity() {
    
        override fun onCreate(savedInstanceState: Bundle?) {
    
            super.onCreate(savedInstanceState)
    
            setContentView(R.layout.activity_main)
    
        }
    
    }

KOTLIN

Copy

## Step 2: Add the Android SDK to the project

### Maven

  1. Add the repository source to the root's `build.gradle` file:
         
         allprojects {
         
           repositories {
         
           // ...
         
           maven { url "https://sdk.canva.com/nativebutton/android" }
         
           }
         
         }

GRADLE

Copy

  2. Copy the following statement into the `dependencies` section of the app's `build.gradle` file:
         
         implementation 'com.canva:design-button:1.3.0'

GRADLE

Copy




If you're using the `china` version of the SDK, replace `https://sdk.canva.com/nativebutton/android` with `https://sdk.canva.cn/nativebutton/android` and `com.canva:design-button:1.3.0` with `cn.canva:design-button:1.3.0`.

### Manual

  1. Download the the Android SDK. You should have received the SDK from Canva as a `.aar` file. There are two versions of the SDK: `global` and `china`. The `global` version of the SDK connects to canva.com, while the `china` version of the SDK connects to canva.cn. These websites are separate environments, so user's accounts and designs are not shared between them.
  2. Select **File > New > New Module...**.
  3. Select **Import .JAR/.AAR Package**.
  4. Select **Next**.
  5. In the **File name** field, enter the path of the `.aar` file.
  6. Select **Finish**.



The SDK appears in the **Project** pane.

![](https://www.canva.dev/_next/static/media/imported-sdk.188def42.png)

  1. Copy the following statement into the `dependencies` section of the app's `build.gradle` file:


    
    
    implementation project(path: ":canva-button-global-release")

GRADLE

Copy

If you're using the `china` version of the SDK, replace `:canva-button-global-release` with `:canva-button-china-release`.

## Step 3: Install the dependencies

  1. Open the app's `build.gradle` file.

  2. Copy the following lines into the `dependencies` section:
         
         implementation "androidx.appcompat:appcompat:1.2.0"
         
         implementation "androidx.browser:browser:1.0.0"

GRADLE

Copy

  3. Select **Sync now**.




## Step 4: Set up a URL scheme

The Android SDK uses [deep links⁠(opens in a new tab or window)](https://developer.android.com/training/app-links/deep-linking) to send information from the Canva editor to the Android SDK. For the SDK to handle deep links, you need a _URL scheme_. This is a unique value that's tied to your Canva Button API key. Canva should have already provided you with this scheme.

Once you have a URL scheme:

  1. Add the following [`manifestPlaceholders`⁠(opens in a new tab or window)](https://developer.android.com/studio/build/manifest-build-variables) property to the `defaultConfig` section of the app's `build.gradle` file:
         
         manifestPlaceholders = [deeplinkScheme: "URL SCHEME GOES HERE"]

GRADLE

Copy

  2. Replace `URL SCHEME GOES HERE` with the Canva-provided URL scheme.




Refer to the [Example](https://www.canva.dev/docs/button/html/getting-started/#example) for a complete code sample.

The Android and iOS SDKs each have their own, distinct URL schemes.

## Step 5: Configure the manifest

In the `AndroidManifest.xml` file:

  1. Add the following property to the `manifest` element:
         
         xmlns:tools="http://schemas.android.com/tools"

XML

Copy

  2. Add an `android:allowBackup` property to the `application` element:
         
         tools:replace="android:allowBackup"

XML

Copy




## Example

### AndroidManifest.xml
    
    
    <?xml version="1.0" encoding="utf-8"?>
    
    <manifest
    
        xmlns:android="http://schemas.android.com/apk/res/android"
    
        xmlns:tools="http://schemas.android.com/tools"
    
        package="com.example.myapplication">
    
    
    
    
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
    
    
    
    
    import androidx.appcompat.app.AppCompatActivity
    
    import android.os.Bundle
    
    
    
    
    class MainActivity : AppCompatActivity() {
    
        override fun onCreate(savedInstanceState: Bundle?) {
    
            super.onCreate(savedInstanceState)
    
            setContentView(R.layout.activity_main)
    
        }
    
    }

KOTLIN

Copy
