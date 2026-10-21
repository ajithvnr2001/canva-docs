---
url: https://www.canva.dev/blog/developers/passing-user-input-from-canva-ui-to-your-lambda-function/
title: Passing User Input from Canva UI to your Lambda Function - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:07.610377+00:00
---

# Passing User Input from Canva UI to your Lambda Function - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/passing-user-input-from-canva-ui-to-your-lambda-function/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

lambda

# Passing User Input from Canva UI to your Lambda Function

Learn how to pass Canva user inputs with Lambda Functions.

![](https://www.canva.dev/_next/static/media/thumbnail.832cdac2.png)

* * *

  * 


[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Oct 20, 2023

* * *

In our [previous guide](https://www.canva.dev/blog/developers/lambda-functions-for-canva-apps/), you learned how to interact with Lambda Functions from your Canva App. Most apps require user input to complete their task, so in this part, we show you how to retrieve a user value and pass it to your third-party service. Then, you can use the new response to display custom content based on the user’s input. Working with services like Lambda Functions to handle user input reduces load on your app’s frontend, keeping it performant. Let’s take a look at how to use user input.

## Accept user input

First, let users enter a text value to send to your Lambda Function. The Canva UI Kit provides prebuilt UI components for user input, including text input. To accept user input, you need to create a new field in the App UI and allow your app to be able read and set the value.

  1. Edit your `app.tsx` file to make these changes to your app’s frontend.

  2. Import the TextInput component from the App UI Kit.
         
         import { ..., TextInput } from "@canva/app-ui-kit";

JSX

Copy

  3. Using a setter, add a state variable to manage the input value. This needs to be inside your app definition, but outside any methods or the return statement.
         
         const [input, setInput] = React.useState<string>("Canva");

JSX

Copy

  4. In your App UI definition, add the new TextInput component above the Send button and inside your return statement.
         
         <TextInput value onChange />

JSX

Copy

  5. Set the value of the text input to your input state variable.
         
         <TextInput value={input} onChange />

JSX

Copy

  6. Add an `onChange` event handler that sets the input state to the value the user enters the field.
         
         onChange={(value) => {
         
           setInput(() => {
         
             return value;
         
           });
         
         }}

JSX

Copy




## Create a POST request

Now that you have access to the user’s input, you can create a request body with the input’s value. Your app sends this to your Lambda Function as a POST request since you're including data. The Fetch method accepts a second parameter allowing you to send a request header with details such as the request method and body data.

  1. Create a data object to hold the information sent to the Lambda Function and make sure you stringify the user’s input.
         
         let data = JSON.stringify({
         
           passedValue: input,
         
         });

JSX

Copy

  2. Create a new JSON object to store the headers data.
         
         const headers = {
         
           method: "POST",
         
           body: data,
         
         };

JSX

Copy

  3. Pass the headers object into the existing fetch request to your Lambda function’s URL.
         
         const res = await fetch(LAMBDA_URL, headers);

JSX

Copy




## Accept data in Lambda Functions

Accessing data sent to Lambda Functions is straightforward if you have worked with API requests before. Data passed to an endpoint using a POST request is available in the body of the request payload. You can easily retrieve the JSON in your Lambda Function and add the user’s data to a Canva design. This is an example of changing the text value sent and returning the new value.

  1. In the Lambda Functions Console, open your function’s code.

  2. Parse out the body from the request, or event as it’s called in your lambda skeleton.
         
         let data = JSON.parse(event.body);

JSX

Copy

  3. You can then access the user’s input in the data object’s `passedValue` property.
         
         console.log(data.passedValue);

JSX

Copy

  4. Now you can do something with the user’s input. For this example, let’s add a Hello message to the text.
         
         let newValue = “Hello “ + data.passedValue;

JSX

Copy

  5. Next, you need to return the message with the value to Canva so you can use it in your app’s frontend. To do this, create a response object.
         
         const response = {};

JSX

Copy

  6. In the response, add a success HTTP status code.
         
         const response = {
         
           statusCode: 200,
         
         };

JSX

Copy

  7. Return the new value in the response body, and make sure you stringify the body text.
         
         const response = {
         
           statusCode: 200,
         
           body: JSON.stringify(newValue),
         
         };

JSX

Copy

  8. Change your return value to the response.
         
         return response;

JSX

Copy

  9. Save and deploy your changes!




## Use the returned data in your app

Once you get a response back from the Lambda Function, you can share it in your app. For images, you might want to display a few options and let the user select one before uploading the image. With text, consider if your user might want to edit it before adding it to a design, or if you want to add it straight to the design since Native Elements are editable on the canvas.

  1. In your code editor, open your Canva app’s frontend found in the app.tsx file.

  2. In our previous walkthrough, we already set up the Add Native Element method to handle changes from our response. So, no new changes are needed here 😀

  3. A handy tip is to show an element in the UI Side Panel with information about the response. Conditionally rendered elements can display the returned values if you create state variables to handle them.
         
         type State = "idle" | "loading" | "success" | "error";
         
         ...
         
         export const App = () = {
         
         ...
         
         const [state, setState] = React.useState<State>("idle");

JSX

Copy

  4. Use these state variables to set the state as _idle_ while doing nothing, _loading_ when the request is sent, and either _success_ or _error_ when the response returns. You can determine the response state from the status code.
         
         setState("loading");

JSX

Copy

  5. These state values allow you to conditionally show success or error fields in the UI. In your app’s UI, add a state check for success and wrap it in curly braces.
         
         {state === "success"}

JSX

Copy

  6. Next, add a logical AND operator (`&&`) to check for a response body.
         
         {state === "success" && responseBody}

JSX

Copy

  7. Then, add a second AND operator to show a new Text UI component with the response body value, if the first two conditions are true.
         
         {state === "success" && responseBody && <Text>{responseBody}</Text>}

JSX

Copy

  8. Finally, you can pass the returned response data to a custom text element on the canvas and display the value in a Text UI component in the app’s side panel.

![Screenshot of the content from the lambda function rendered in the Canva editor](https://www.canva.dev/_next/static/media/lambda-content-in-the-editor.17d7abc4.png)




You’ve successfully passed data provided by a user to your Lambda function and handled the response in your app’s UI. This basic workflow establishes a framework you can apply to any app you build with Canva. We can’t wait to see what you build!

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.9247b03d.png)](https://www.canva.dev/blog/developers/best-app-ideas/)

[Apps SDK15 ideas for buzz-worthy apps that Canva users wantThe best ideas for apps based on Canva's latest research.](https://www.canva.dev/blog/developers/best-app-ideas/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Feb 9, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.2a37fda3.jpg)](https://www.canva.dev/blog/developers/canva-developers-wrapped-2024/)

[2024Canva Developers 2024 WrappedAnother exciting year for Canva Developers is coming to a close. Learn about all the amazing growth our ecosystem has seen this year.](https://www.canva.dev/blog/developers/canva-developers-wrapped-2024/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Dec 20, 2024

[![](https://www.canva.dev/_next/static/media/thumbnail.088a2bca.png)](https://www.canva.dev/blog/developers/canva-dev-mcp-server/)

[AIIntroducing the Canva Dev MCP ServerHarness the full power of AI coding agents with the Canva Dev MCP Server.](https://www.canva.dev/blog/developers/canva-dev-mcp-server/)

[Anto Lepejian⁠(opens in a new tab or window)](https://www.linkedin.com/in/anto-lepejian/)Apr 16, 2025
