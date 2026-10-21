---
url: https://www.canva.dev/blog/developers/helping-you-migrate-to-native-fetch/
title: Helping you migrate to Native Fetch - Canva Developers Blog
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:06.867729+00:00
---

# Helping you migrate to Native Fetch - Canva Developers Blog

> Source: https://www.canva.dev/blog/developers/helping-you-migrate-to-native-fetch/

Developers Blog

[Overview](https://www.canva.dev/blog/developers/)

[About Canva⁠(opens in a new tab or window)](https://www.canva.com/about/)

Apps SDK

# Helping you migrate to Native Fetch

Learn how you can migrate your Canva apps to use Native Fetch API.

![](https://www.canva.dev/_next/static/media/thumbnail.761d69ec.png)

* * *

  * 


[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Feb 27, 2023

* * *

Native Fetch is here!

We’re happy to unblock the Native Browser Fetch API in your Canva app panel, opening up a world of new possibilities. This exciting change removes many limitations, such as the size of your request and response, making it easier to access larger data files, like high-res images and videos.

We want to take you through what this change means for you, how to make the necessary changes to your code, and the additional middleware services you’ll need to develop. This guide helps explain the Starter Kit Fetch example in more detail.

## What does this change mean?

In order to keep your apps secure with these changes, you should be signing all requests with JSON Web Tokens (or JWTs) to verify the source of the request. If you’re new to JWTs, [this⁠(opens in a new tab or window)](https://jwt.io/introduction) is a great introduction.

You can now start implementing the necessary changes in your code to sign all fetch requests with a JWT, create the middleware to decode and verify the tokens, and store your public keys. We’re continuing to develop the JWT service on our end, so until then, we’ve created a mock service to use. Note that in the interim, apps will only be able to be worked on in your local development environment. The method definitions on the mock service and live service are the same, so no additional changes will be needed when we go live.

Make sure to pull down the latest version of the Starter Kit to get the changes to the Canva SDK and the newest examples.
    
    
    git pull

SHELL

Copy

## Updating your frontend code

Let’s walk through how you can start building and testing with Native Fetch in your frontend. All requests will need an Authorization header using Bearer Token authentication.

  1. Start in your `app.ts` file (which is probably where you’ve created your app’s frontend). Remove your import statement for Canva Fetch, since Native Fetch is now available.
         
         import { Response, getFetch } from "@canva/fetch";

JS

Copy

  2. Also, remove any references to `getFetch()`, such as `const fetch = getFetch();`.

  3. Since Native Fetch is unblocked, any calls using the fetch keyword will now default to the Fetch API. Update all of your fetch requests to use the fetch method.

For example:
         
         const response = await fetch.post({
         
           endpoint,
         
         });

JS

Copy

becomes
         
         const res = await fetch(endpoint, {
         
           method: "POST",
         
         });

JS

Copy

  4. All your requests need Authorization headers, using the Bearer Authentication. Your token will be your JWT. Add your headers to your request.
         
         const res = await fetch(endpoint, {
         
           method: "POST",
         
           headers: {
         
             Authorization: `Bearer ${token}`,
         
           },
         
         });

JS

Copy

  5. To get your token, access the Authentication service from Canva. Import the Authentication library and the `getAuthentication` method.
         
         import { getAuthentication } from "@canva/authentication";

JS

Copy

  6. Inside your App function, initialize the authentication capability to generate your JWT.
         
         const auth = getAuthentication();

JS

Copy

  7. Before sending your fetch request, generate the token.
         
         const token = await auth.getCanvaUserToken();

JS

Copy




## About the Middleware you’ll need

In your backend, you’ll need the ability to decode and verify your token. We’ve created a sample of this middleware in the jwt_middleware.ts file. This will validate there’s an Authorization header in all requests to your backend, retrieve the JWT and decode it, then verify the token has the correct `userId`, `brandId`, and `aud`. You’ll use your public key to verify the token.

You’ll also need to store your public key that will help you decode your token. We’ve created a sample of how to cache your public key in the `public_key_cache.ts` file. Normally your public key store/cache would retrieve your public keys from Canva’s key store server, using your App ID to dynamically navigate the path. That server runs locally on your machine for now, but you’ll still need the App ID as part of the key store path. We have the local key server set up in our examples to run on Port 3002. When the service is ready from Canva, make sure you switch over the KEY_SERVER to the Server URL provided by us. This service should also be able to refresh expired public keys.

Make sure to create similar handlers on your backend server before you submit your app.

## Updating your Backend

Once the infrastructure to help decode and verify your JWT is set up (or you’re just using our samples provided), in your routing file (in our sample, it’s the `server.ts` file), you’ll need to verify every request.

  1. Start by creating and retrieving your public key. Create a new public key store and initialize it.
         
         const publicKeyCache = new PublicKeyStore(APP_ID);
         
         await publicKeyCache.init();

JS

Copy

  2. Once your public key is available, you can use your JWT middleware to verify the request. Remember, your JWT middleware service needs the public key to verify the JWT. Use Express’s router use method to call this middleware for each request.
         
         router.use(jwtMiddleware(publicKeyCache));

JS

Copy

  3. After you’ve verified the request JWT, you can handle your route calls the same as you did with Legacy Fetch.

For example:
         
         router.get("/your-route", async (req, res) => {});

JS

Copy

  4. When running your application locally, remember you’ll need to have two local servers running. If you are using the example, the start script we’ve provided starts both servers.
         
         npm start fetch

SHELL

Copy




## Wrap Up and Support

We’re excited about this change, and we do understand that some refactoring is required to use Native Fetch, so hopefully, our examples and this guide will help you speed up your development.

If you have any questions, feel free to post them in the [#beta⁠(opens in a new tab or window)](https://canvadev1.slack.com/archives/C040N8QKZKN) channel, and we’ll update this guide with any further clarifications. Happy coding!

_Dev note: For apps submitted for the Canva Create event, Legacy Fetch will continue to be supported for your app. All app submissions after the Canva Create deadline will need to use Native Fetch._

## More from the Developers Blog

[![](https://www.canva.dev/_next/static/media/thumbnail.3a2aa29c.jpg)](https://www.canva.dev/blog/developers/streamlining-real-estate/)

[Real EstateStreamlining Real Estate content creationLearn how to architect your Canva App to supercharge your real estate marketing content creation.](https://www.canva.dev/blog/developers/streamlining-real-estate/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)May 6, 2025

[![](https://www.canva.dev/_next/static/media/thumbnail.6c865963.jpg)](https://www.canva.dev/blog/developers/apps-to-win-big/)

[Apps SDKSimple apps to win big in the Canva Apps MarketplaceWhat kind of apps are we looking for for the Apps Marketplace?](https://www.canva.dev/blog/developers/apps-to-win-big/)

[Meredith Hassett⁠(opens in a new tab or window)](https://www.linkedin.com/in/meredith-hassett/)Sep 19, 2023

[![](https://www.canva.dev/_next/static/media/thumbnail.7611d581.jpg)](https://www.canva.dev/blog/developers/simplifying-dx/)

[Developer experienceSimplifying developer experiences at scaleHow Canva is bridging the gap between complex developer experience and the simplicity our users love](https://www.canva.dev/blog/developers/simplifying-dx/)

[Faria Anzum⁠(opens in a new tab or window)](https://www.linkedin.com/in/farianzum)May 20, 2025
