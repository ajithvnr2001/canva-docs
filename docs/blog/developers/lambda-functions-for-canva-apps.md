---
url: https://www.canva.dev/blog/developers/lambda-functions-for-canva-apps/
title: Getting Started with Lambda Functions for Canva Apps - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:06.574505+00:00
---

# Getting Started with Lambda Functions for Canva Apps - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/lambda-functions-for-canva-apps/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

lambda

# Getting Started with Lambda Functions for Canva Apps

Learn how to use Lambda functions

![](https://www.canva.dev/_next/static/media/thumbnail.f388d5fa.jpg)

* * *

  * 


[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Oct 4, 2023

* * *

With UI Web Apps, it is important to remove heavy load activities and resource intensive operations from the frontend of your application, because not doing so can create a slower user experience. A slow or lagging UI can cause user churn and lead to your app seeing low usage. Offloading these expensive operations to backend resources, like AWS, can help you ensure a great experience for your users. We’ll take a look at how to set up your Lambda functions and Canva app to be able to communicate with each other.

![An app on Canva that we'll use as an example](https://www.canva.dev/_next/static/media/finished-product.2a56597d.jpg)

## Why Lambda

Lambda Functions are a convenient service available in the AWS landscape. Lambda functions allow you to easily scale up to match demand without having to worry about managing the physical or virtual resources (like servers or containers) yourself. They will scale up and down based on need — saving you time, money, and resources — while allowing you to focus on the core value add, the code only you can write. As you are developing new apps, you can start to understand user needs, patterns, and adoption before investing in developing your own backend. While Lambda functions do have some drawbacks, such as not being able to control your compute resources and having cold start delays, the benefits of seamless scaling and low costs are great for getting started and exploratory development.

## Set up your first function

First thing is to get a Lambda function created in your AWS Console. If you are new to creating Lambda functions, their Getting Started template is enough to follow along with this example. If you already have a Lambda function created, go ahead and skip to the Creating the Function URL section.

  1. Start by searching for Lambda.

![Searching for Lambda on amazon](https://www.canva.dev/_next/static/media/search-for-lambda.875ddfc4.jpg)

  2. Click Create function.

![Click create](https://www.canva.dev/_next/static/media/click-create.0385da98.jpg)

  3. Select Use a Blueprint.

![Selecting use a blueprint](https://www.canva.dev/_next/static/media/use-blueprint.f92ee774.jpg)

  4. Pick a blueprint. The Hello World examples are easiest to follow along with.

  5. Give the blueprint a name like `myCanvaFunction`.

![Giving the blueprint a name](https://www.canva.dev/_next/static/media/blueprint-name.1cbac7bc.jpg)

  6. For this example, you can leave all the other settings as is, but if this is a production service, you would want to configure roles and permissions.

  7. Create the function.

![Creating the function](https://www.canva.dev/_next/static/media/create-function.c3825905.jpg)




## Creating the Function URL

To enable your Lambda function to be called outside of the AWS test environment, you’ll need to create a Function URL. If your function already has a URL, you can see it in the Function overview. If you already have one, go ahead and skip to the section on Configuring CORS.

![An overview of the function](https://www.canva.dev/_next/static/media/function-overview.6ea114af.jpg)

  1. Go to the Configuration tab.

  2. Click the Create function URL button.

![Clicking create function URL](https://www.canva.dev/_next/static/media/create-function-url.c09ff09f.jpg)

  3. For this example, you’ll want to create a Public URL, so select NONE under Auth type. If this is sensitive data being accessed, you would want to make sure to configure user roles and permissions.

![Click create](https://www.canva.dev/_next/static/media/select-none-auth.c33dca16.jpg)

  4. Under Function URL on your Function overview, you should now see a URL. If you click it, it should take you to a new window where you can see the response from your Lambda function. The Hello World function expects an input to be able to output the Key1 value. The result on Node will be “null” and on Python will be a 502 error.

![Seeing the response](https://www.canva.dev/_next/static/media/function-url-click.be1ba91d.jpg)




For ease of testing, you may want to update your code to simply return Hello World. To do so, just change the Return statements to “Hello World”.

## Configure CORS

In order for your Canva app to be able to communicate with AWS, you’ll need to add it to the allowed list for resource sharing, also known as CORS. This protects against malicious calls to resources by confirming they are from a trusted entity. There are two ways to do CORS.

  * The simple way is to just allow everything. You would control access using roles and permissions. This would be `Access-Control-Allow-Origin: *`, which would allow any request from any origin though.
  * A more secure way is to limit access to just your Canva app(s). The Canva App URL is formed in combination with your APP_ID. You would need to add each APP URL to the allow list if this function is used in multiple apps. Alternatively you could set up a static middleware service to forward requests from Canva to your Lambda function.


  1. To enable CORS on your Function URL, go to the Configurations tab and click Edit on the Function URL.

![Configurations tab](https://www.canva.dev/_next/static/media/cors-function.4687519b.jpg)

  2. Under Additional Settings, you’ll find a checkbox to Configure cross-origin resource sharing (CORS). Check it.

![Check the CORS checkbox](https://www.canva.dev/_next/static/media/configure-cross-origin.3094af45.jpg)

  3. Once it’s checked, you can add Origins to the allow list. For testing purposes, you can leave it as *. Otherwise, add to your Canva App URL or middleware service.

![Add Canva app URL](https://www.canva.dev/_next/static/media/add-origin.547017d7.jpg)

  4. Make sure to Save.

![Click save](https://www.canva.dev/_next/static/media/make-save.f71d88ac.jpg)




## Call your function from Canva

You’re now ready to use your Lambda function in Canva! You’ll need your Canva App code. If you haven’t built a Canva App yet, you can [clone the Starter Kit from Github⁠(opens in a new tab or window)](https://github.com/canva-sdks/canva-apps-sdk-starter-kit) to make it easier to jump into building. Once you have it cloned, edit the `app.tsx` file under `src`.

You’re going to make a Fetch call to the Function URL. In order to keep your app dynamic, it’s recommended to use state management for any data displayed to the end user.

  1. You can start by setting up state management for the response in your App. Inside of your App definition, add in a current state variable and setter function, and use these for the returned values from `React.useState`. Since you can’t guarantee the responses format, we recommend using `unknown` and `undefined` states. Set the initial state to `undefined`.
         
         const [responseBody, setResponseBody] = React.useState<unknown | undefined>(
         
         undefined
         
         );

JS

Copy

  2. Next, create a function to handle the GET request, named `sendGetRequest`. Since in this example you are simply getting data from your Lambda function, you don’t need to worry about passing data. However, Fetch can be a resource hog, so make sure to make it async.
         
         const sendGetRequest = async () => {}

JS

Copy

  3. Inside your new send function, you can send the fetch request to your Function URL. Make sure to assign the response to a variable.
         
         const res = await fetch(LAMBDA_URL);

JS

Copy

  4. Once the fetch request returns, parse out the JSON from the response and assign it to a new variable.
         
         const body = await res.json();

JS

Copy

  5. Use the body JSON object to set the state of the response body.
         
         setResponseBody(body);

JS

Copy

  6. You’ll use the response to add a new element to the design. Make sure you’ve imported the `addNativeElement` method from `@canva/design`.
         
         import { addNativeElement } from "@canva/design";

JS

Copy

  7. To add a text element, you’ll need to add the props of type as TEXT and children as an array of strings. Since the example function is returning a string of “Hello World”, you can wrap it as an array [ ].
         
         addNativeElement({
         
         type: "TEXT",
         
         children: [body],
         
         });

JS

Copy

  8. Last thing to do is to actually call your send function. You can do this from an onClick handler for a button. Your App UI can be found in the return statement for your App code. In your app UI, make sure there is a Button UI element. You can use the UI kit Button to keep it aligned to Canva Brand.
         
         <Button variant="primary" onClick={onClick} stretch>
         
         Send to Lambda Function
         
         </Button>

JSX

Copy

  9. Back in your app code, make sure to have the event handler defined. Inside the event handler, call your send request function.
         
         const onClick = () => {
         
         sendGetRequest()
         
         };

JS

Copy




## Test your App

Now that your app is built and your Lambda function created, you are ready to test your app. You’ll need to get your app running locally and preview it inside the Canva Editor. The following steps are in reference to the Starter Kit, so make sure to adjust depending on your app folder structure.

  1. At the top level of the app in your preferred CLI tool — for the Starter Kit, this is the Starter Kit top folder — you need to run an install to make sure you have all your packages.
         
         npm install

SH

Copy

  2. Once you have successfully installed your app, you can start your app. In the Starter Kit, the keyword `start` is configured to run your app.tsx src file.
         
         npm start

SH

Copy

  3. This will provide you with a development URL. You will need this for configuring your app in the Canva Dev Portal. Switch over to the [Developer Portal⁠(opens in a new tab or window)](https://www.canva.com/developers/apps).

![Click create](https://www.canva.dev/_next/static/media/dev-portal.caf06e4a.jpg)

  4. You can either Create an app if you don’t have a test app to use, or use an existing test app. It’s recommended to create a Public app.

![Click create](https://www.canva.dev/_next/static/media/create-public-app.8ba8e843.jpg)

  5. In the **Code upload** tab, under App Source, paste in your Development URL from your running app.

![Click create](https://www.canva.dev/_next/static/media/dev-url.9a931246.jpg)

  6. Click Preview to see your app running in a new blank Canva design.

![Click create](https://www.canva.dev/_next/static/media/click-preview.e080c50a.jpg)

  7. Here we’ll have a button to Send to Lambda Function.

![Click create](https://www.canva.dev/_next/static/media/send-lambda-function.dce7ecf1.jpg)

  8. When you click it, you should see a Text element added to your design saying Hello World!

![Click create](https://www.canva.dev/_next/static/media/hello-world.f014da71.jpg)




And that’s the basics of getting started using Lambda functions in your Canva App. It’s simple to bring in functionality from 3rd-party sources to take your app to the next level.

In our next Blog Post, you can learn about how to pass data from User Inputs in your Canva App to your Lambda Function.

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.02a1ad94.jpg)](https://www.canva.dev/blog/developers/building-with-content-publisher-part3/)

[Content Publisher IntentMeet the Content Publisher Intent - Part 3Complete implementation, Preview UIs, and publishing](https://www.canva.dev/blog/developers/building-with-content-publisher-part3/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)May 8, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.d9204a0c.jpg)](https://www.canva.dev/blog/developers/canva-and-coding-agents-platforms/)

[Connect APIUsing Canva with your coding agentGuidance for using Canva with coding assistants, Dev MCP, remote MCP, and the Connect APIs.](https://www.canva.dev/blog/developers/canva-and-coding-agents-platforms/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Jun 9, 2026

[![](https://www.canva.dev/_next/static/media/thumbnail.f9835b74.jpg)](https://www.canva.dev/blog/developers/welcome-to-the-brand-new-era/)

[Canva CreateWelcome to the Brand New Era of Being a Developer on CanvaExplore some of the apps we shared as part of Canva Create.](https://www.canva.dev/blog/developers/welcome-to-the-brand-new-era/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Mar 20, 2023
