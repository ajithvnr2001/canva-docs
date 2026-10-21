---
url: https://www.canva.dev/docs/apps/localization/icu-syntax/
title: ICU syntax - Canva Developers SDK Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:56:06.233945+00:00
---

# ICU syntax - Canva Developers SDK Documentation

> Source: https://www.canva.dev/docs/apps/localization/icu-syntax/

[Overview](https://www.canva.dev/docs/apps/reference/)

Apps inside Canva

API reference

[Permissions](https://www.canva.dev/docs/apps/configuring-intents-permissions/)[Error codes](https://www.canva.dev/docs/apps/intents-error-codes/)

App UI Kit reference

[Apps Scripts config reference](https://www.canva.dev/docs/apps/canva-app-scripts/configuration-reference/)[Localization syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/)

Canva for your platform

Canva REST API reference

[Keys](https://www.canva.dev/docs/apps/rest-apis/reference/webhooks/keys/)[Scopes](https://www.canva.dev/docs/apps/rest-apis/scopes/)[Error responses](https://www.canva.dev/docs/apps/rest-apis/error-responses/)

Webhooks notification reference

[Changelog](https://www.canva.dev/docs/apps/rest-apis/changelog/)

Canva for AI assistants

Tools

[Rate limits](https://www.canva.dev/docs/apps/mcp/tools/)[Usage policy](https://www.canva.dev/docs/apps/mcp/usage-policy/)[Prohibited use](https://www.canva.dev/docs/apps/mcp/prohibited-use/)

Security

Apps inside Canva

[Security guidelines](https://www.canva.dev/docs/apps/security-guidelines/)[Content Security Policy](https://www.canva.dev/docs/apps/content-security-policy/)[Shared responsibility model](https://www.canva.dev/docs/apps/shared-responsibility-intents/)

Canva for your platform

[Security recommendations](https://www.canva.dev/docs/apps/rest-apis/security-recommendations/)[Shared responsibility model](https://www.canva.dev/docs/apps/rest-apis/shared-responsibility/)

Canva CLI

[Overview](https://www.canva.dev/docs/apps/canva-cli/)[canva-app.json](https://www.canva.dev/docs/apps/app-configuration/canva-app-json/)[Making REST API requests](https://www.canva.dev/docs/apps/canva-cli/making-rest-api-requests/)

Policies

[Deprecation policy](https://www.canva.dev/docs/apps/deprecation-policy/)

# ICU syntax

Canva supports a subset of International Components for Unicode (ICU).

Copy page

The Canva translation process supports a subset of ICU `MessageFormat` syntax. For more information about ICU, see the official [FormatJS documentation⁠(opens in a new tab or window)](https://formatjs.github.io/docs/core-concepts/icu-syntax).

Canva's translation process doesn't support the entire ICU syntax, and uploaded files will be rejected if they contain any unsupported syntax. For more information, see [Unsupported syntax](https://www.canva.dev/docs/apps/localization/icu-syntax/#unsupported-syntax).

## ICU basics

This section describes the supported ICU syntax, with recommendations and examples.

Follow these examples and guidelines so that your app can be translated more accurately and efficiently.

### Basic messages

How to do basic message localization with React, using the `FormattedMessage` component from `react-intl`.

  * The `defaultMessage` string is the source for translation text. It's displayed to users that either have an English locale, or a locale with no translations available.
  * Use the `description` string to give as much context as possible to a human translator. For guidance on writing translator notes, see [Add notes for translators](https://www.canva.dev/docs/apps/localization/#add-notes-for-translators).



For example:
    
    
    <FormattedMessage
    
      defaultMessage="My internationalized app"
    
      description="The title the user sees when opening the app. Appears at top of page."
    
    />

TSX

Copy

Do  
---  
Ensure that `defaultMessage` is clear and written in US English.  
Include a detailed `description` that gives context to translators.  
  
### Interpolation

You can use dynamic values (like `firstName`) in the `defaultMessage` prop of `FormattedMessage`. This process is known as _interpolation_.

This section explains how to use interpolation for localized messages in React, using the `FormattedMessage` component from `react-intl`.

For example:
    
    
    const name = "John"
    
    // ...
    
    <FormattedMessage
    
      defaultMessage="Welcome to the world of AI creativity, {firstName}!"
    
      description="A greeting that welcomes the user to the AI image generation app"
    
      values={{
    
        firstName: name,
    
      }}
    
    />

TSX

Copy

This renders as: "Welcome to the world of AI creativity, John!"

Do  
---  
When inserting dynamic content (such as user-specific data), use placeholders like `{firstName}`.  
`"Hello {name}"`  
  
Don't  
---  
Don't manually combine strings and variables, using techniques like the `+` operator. This can lead to incorrect and confusing sentences when translations are combined. This is because languages will reorder words in various ways. For more information, see this [blog post⁠(opens in a new tab or window)](https://www.linkedin.com/pulse/internationalization-localization-tips-concatenation-daniel-neumann).  
`"Hello " + name`  
  
There are some cases where [select](https://www.canva.dev/docs/apps/localization/icu-syntax/#select) is preferable to interpolation. For more information, see [Using select or interpolation](https://www.canva.dev/docs/apps/localization/icu-syntax/#using-select-or-interpolation).

### Plurals

How to handle plurals in localized messages in React.

For example:
    
    
    export const CreditUsage = ({
    
      creditsCost,
    
      remainingCredits,
    
    }: {
    
      creditsCost: number;
    
      remainingCredits: number;
    
    }) => (
    
      <Text>
    
        <FormattedMessage
    
          defaultMessage={`Use {creditsCost, number} of {remainingCredits, plural,
    
            one {# credit}
    
            other {# credits}
    
          }`}
    
          description="Informs the user about the number of credits they will use for the image generation task. Appears below the image generation button."
    
          values={{
    
            creditsCost,
    
            remainingCredits,
    
          }}
    
        />
    
      </Text>
    
    );

TSX

Copy
    
    
    <CreditUsage creditsCost={5} remainingCredits={50} />
    
    <CreditUsage creditsCost={1} remainingCredits={1} />

TSX

Copy

This would render as:

  * "Use 5 of 50 credits"
  * "Use 1 of 1 credit"



Do  
---  
**Consider edge cases:** Ensure that pluralization handles various scenarios, such as zero, one, and other amounts.  
  
### Numbers

To localize numbers for the user's locale, ICU needs them to be formatted with a specific argument.

If you are only presenting a number by itself, you can use [`FormattedNumber`⁠(opens in a new tab or window)](https://formatjs.github.io/docs/react-intl/components/#formattednumber) from the `react-intl` library to localize the number. If you are presenting a number in a sentence with other words, you should use the ICU syntax, as shown below.

This example shows how to format numbers in localized messages in React, using the `FormattedMessage` component from `react-intl`.
    
    
    <FormattedMessage
    
      defaultMessage="Image generation is {progress, number, ::percent} complete."
    
      description="Displays the progress of the current image generation task that the user requested"
    
      values={{
    
        progress: 0.75,
    
      }}
    
    />

TSX

Copy

Assuming the locale uses this percentage format, this can render as: "Image generation is 75% complete."

Do  
---  
Use ICU number formatting for numbers, such as percentages.  
`Members ({(members, number, integer)})` \- `123456 members` displays as `Members (123,456)` in English, `Membres (123 456)` in French, and `Thành viên (123.456)` in Vietnamese.  
  
Don't  
---  
Avoid formatting numbers manually. Instead, you can use an ICU formatting library like `react-intl`.  
`Members ({members})` \- The number doesn't respect the user's locale and always displays 123456 as the number, without separators.  
  
#### Currency

Automatically adjusts currency symbols and formats based on the user's locale. This function does not convert currency into other denominations, and does not consider exchange rates at any point.

  * `::currency/CODE`: Specifies the currency code for number formatting (such as `USD`, `EUR`).



In this example, the number `1234.56` is formatted as currency in USD, displaying "$1,234.56" for locales using the dollar sign format. The `::currency/USD` syntax configures the number formatting for the specified currency.
    
    
    <FormattedMessage
    
      defaultMessage="The total amount is {amount, number, ::currency/USD}"
    
      description="Displays the total amount in USD currency"
    
      values={{
    
        amount: 1234.56,
    
      }}

TSX

Copy

Rendered result: `The total amount is $1,234.56`

#### Decimal

Automatically adjusts decimal number formats based on the user's locale.

  * `{temperature, number, .0}`: Formats the number as a decimal with one fractional digit.



This example shows how to display a temperature reading. The `{temperature, number, .0}` syntax formats the number `23.456` as "23.5", representing the temperature with one decimal place.
    
    
    <FormattedMessage
    
      defaultMessage="The current temperature is {temperature, number, .0} degrees."
    
      description="Displays the current temperature with one decimal place"
    
      values={{
    
        temperature: 23.456,
    
      }}
    
    />

TSX

Copy

Rendered result: `The current temperature is 23.5 degrees.`

#### Percentage

Automatically adjusts percentage formats based on the user's locale.

  * `{progress, number, ::percent}`: Formats a number as a percentage.



This example shows how to display task completion progress. The `{progress, number, ::percent}` syntax formats the number `0.71` as "71%", representing the progress in whole percentage terms.
    
    
    <FormattedMessage
    
      defaultMessage="Task completion is at {progress, number, ::percent}."
    
      description="Displays the task completion progress as a full percentage"
    
      values={{
    
        progress: 0.71,
    
      }}
    
    />

TSX

Copy

Rendered result: `Task completion is at 71%.`

### Dates

To localize date values for the user's locale, ICU needs them to be formatted with a specific argument.

If you are only presenting a date by itself, you can use [`FormattedDate`⁠(opens in a new tab or window)](https://formatjs.github.io/docs/react-intl/components/#formatteddate) from the `react-intl` library to localize the date. If you are presenting a date in a sentence with other words, you should use the ICU syntax, as shown below.

This example demonstrates how to format dates and times in localized messages in React, using the `FormattedMessage` component from `react-intl`.
    
    
    <FormattedMessage
    
      defaultMessage="Credits refresh on: {refreshDate, date, short} at {refreshTime, time, short}"
    
      description="Informs users when their credits for image generation will refresh, including the time"
    
      values={{
    
        refreshDate: new Date("2023-11-24T15:00:00"),
    
        refreshTime: new Date("2023-11-24T15:00:00"),
    
      }}
    
    />

TSX

Copy

Depending on the user's locale, this can render as: `Credits refresh on: 11/24/23 at 3:00 PM"`.

Do  
---  
`Expires {(expiryDate, date, short)}` \- When formatted with a date value (such as `new Date('2024-09-25')` in JavaScript), this will correctly display as:

  * `Expires 9/25/2024` for US English (en-US).
  * `Verfällt am 25.09.2024` for German (de-DE).

  
  
Don't  
---  
`Expires {expiryDate}` \- The number doesn't respect the user’s locale and always displays the date as 2024-09-25. For example: (`Verfällt am 2024-09-25`)  
  
### Time

To localize time values for the user's locale, ICU needs them to be formatted with a specific argument.

If you are only presenting a time by itself, you can use [`FormattedTime`⁠(opens in a new tab or window)](https://formatjs.github.io/docs/react-intl/components/#formattedtime) from the `react-intl` library to localize the time. If you are presenting a time in a sentence with other words, you should use the ICU syntax, as shown below.

Do  
---  
`Current time: {(currentTime, time, short)}` \- This displays as `Current time: 3:45 PM` in English.  
  
#### Relative time

This section provides guidelines for displaying relative time.
    
    
    const LastGeneratedMessage = ({
    
      lastGeneratedTime,
    
    }: {
    
      lastGeneratedTime: Date;
    
    }) => {
    
      const intl = useIntl();
    
    
    
    
      const [generatedTimeAgoInSeconds, setGeneratedTimeAgoInSeconds] = React.useState(0);
    
    
    
    
      // ...
    
    
    
    
      return (
    
        <Text>
    
          <FormattedMessage
    
            defaultMessage="Last image generated {timeAgo}"
    
            description="Tells the user how long ago they generated their last image. timeAgo is a relative time string. e.g. '5 seconds ago'"
    
            values={{
    
              timeAgo: intl.formatRelativeTime(
    
                -generatedTimeAgoInSeconds,
    
                "seconds",
    
              ),
    
            }}
    
          />
    
        </Text>
    
      );
    
    };

TSX

Copy

Do  
---  
Use functions or libraries that handle relative time calculations and formatting, such as `intl.formatRelativeTime` of `react-intl`, or [Intl.RelativeTimeFormat⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat)  
  
Don't  
---  
Avoid hardcoding custom logic for relative time calculations, as this might not adapt well across different locales.  
  
### Select

Do  
---  
`Hello, {role, select, admin {Administrator} user {User} guest {Guest} other {Visitor}}!`

  * If `role` is `'admin'`, it renders: `Hello, Administrator!`
  * If `role` is `'user'`, it renders: `Hello, User!`
  * If `role` is `'guest'`, it renders: `Hello, Guest!`
  * If `role` is anything else or missing, it renders: `Hello, Visitor!`

  
  
#### Using select or interpolation

If your message needs to adapt to a specific, categorical value (such as _status_ or _day_) and an obvious fallback value, then [select](https://www.canva.dev/docs/apps/localization/icu-syntax/#select) might be easier to implement than [interpolation](https://www.canva.dev/docs/apps/localization/icu-syntax/#interpolation). Select lets you define the various message strings directly within the message format, making your code more concise and easier to maintain. While select might appear simpler and preferable to implement at first, it can become more complex once you start nesting ICU elements.

Interpolation is more familiar to JavaScript and TypeScript developers and is a flexible and powerful option, especially when you need to handle multiple dynamic values.

The following table summarizes the use cases for select and interpolation.

Feature| Select| Interpolation  
---|---|---  
Purpose| Conditional selection based on predefined categories.| Dynamic value insertion.  
Example Input| "male", "female", "other".| "Jane", "123", "New York".  
Use case| Gender, user roles, statuses.| Names, numbers, locations, dynamic content.  
Fallback required?| Yes (other case).| No, just inserts the value.  
  
These examples compare how select and interpolation would handle a dynamic greeting:

**Select:**

When using select, you can create a message that changes based the document type:
    
    
    Here are your stats for the year. {doctype, select, presentation{Your slides are the talk of the town!} social {Your followers love your work!} other {Way to go!}}

JSON

Copy

**Interpolation:**

When using string interpolation instead of select, you need to define logic outside the message to choose the appropriate string for the doctype. Here's and example of how the interpolation code might look:
    
    
    import { defineMessages, useIntl } from 'react-intl';
    
    
    
    
    const messages = defineMessages({
    
      presentation: { 
    
        defaultMessage: "Your slides are the talk of the town!", 
    
        description: "Message for presentation documents" 
    
      },
    
      social: { 
    
        defaultMessage: "Your followers love your work!", 
    
        description: "Message for social media posts" 
    
      },
    
      other: { 
    
        defaultMessage: "Way to go!", 
    
        description: "Fallback message" 
    
      },
    
    });
    
    
    
    
    const interpolateSelect = (key, intl) => {
    
      return intl.formatMessage(messages[key] || messages.other);
    
    };
    
    
    
    
    const DocumentMessage = ({ doctype }) => {
    
      const intl = useIntl();
    
      const message = interpolateSelect(doctype, intl);
    
    
    
    
      return <p>{message}</p>;
    
    };
    
    
    
    
    // Usage example
    
    <DocumentMessage doctype="presentation" />

JAVASCRIPT

Copy

### Rich text

How to format rich text in localized messages in React, using the `FormattedMessage` component from `react-intl`.

For example:
    
    
    <FormattedMessage
    
      defaultMessage="Discover stunning AI-generated example images in our <link>gallery</link> and <callToAction>start exploring now!</callToAction>"
    
      description="A call to action directing the user to explore the AI image gallery"
    
      values={{
    
        link: (chunks) => (
    
          <Link
    
            href={DOCS_URL}
    
            requestOpenExternalUrl={() => openExternalUrl(DOCS_URL)}
    
          >
    
            {chunks}
    
          </Link>
    
        ),
    
        callToAction: (chunks) => <strong>{chunks}</strong>,
    
      }}
    
    >
    
      {(chunks) => <Text>{chunks}</Text>}
    
    </FormattedMessage>

TSX

Copy

This can render as: "Discover stunning AI-generated example images in our [gallery](https://www.canva.dev/docs/apps/localization/icu-syntax/#rich-text) and **start exploring now!** "

Do  
---  
**Use functions for rich text:** To ensure dynamic content is properly rendered, you can wrap parts of your message in React components by passing functions in the `values` prop.  
  
Don't  
---  
**Hardcode HTML Elements:** Avoid embedding raw HTML within your `defaultMessage`.  
  
### Message as string type

How to use localized strings as button labels in React, using `formatMessage` from `react-intl`.

For example:
    
    
    <Button variant="primary">
    
      {intl.formatMessage({
    
        defaultMessage: "Generate image",
    
        description: "A button label to generate an image from a prompt",
    
      })}
    
    </Button>

TSX

Copy

This renders a button with the label "Generate image", and the text is localized based on the user's locale.

Do  
---  
For consistency with the rest of the app's localization, use `formatMessage` to localize user-facing text that is required to be a string type (like button labels).  
  
Don't  
---  
Avoid hardcoding button text, since it will be left untranslated.  
  
### Non-visible text for accessibility

How to use non-visible text for accessibility purposes (such as screen reader descriptions) in React, using `ariaLabel` and `formatMessage` from `react-intl`.

For example:
    
    
    <Button
    
      variant="primary"
    
      icon={SortIcon}
    
      ariaLabel={intl.formatMessage({
    
        defaultMessage: "Sort images by creation date (Newest to Oldest)",
    
        description:
    
          "Screenreader text for a button. When pressed, the button will sort the generated images by creation date from newest to oldest.",
    
      })}
    
    />

TSX

Copy

The screen reader will read the aria label as: "Sort images by creation date (Newest to Oldest)".

Do  
---  
Use `formatMessage` for accessibility by providing localized `ariaLabel` text.  
  
### LTR and RTL languages

To support left-to-right (LTR) and right-to-left (RTL) languages, you can use CSS properties in UI components.

This example uses `paddingStart` instead of `paddingLeft` or `paddingRight`, which lets your UI automatically adapt to the language's text direction.
    
    
    <Box paddingStart="2u">
    
      <Slider min={0} max={100} />
    
    </Box>

TSX

Copy

Do  
---  
To help components adapt to LTR and RTL languages, use logical properties like `paddingStart` instead of directional properties like `paddingLeft`.  
  
### Lists

How to format lists in a way that is compatible with localization.

In this example, the `SelectedEffects` component defines a list of image effects, each formatted for localization.
    
    
    const SelectedEffects = () => {
    
      const intl = useIntl();
    
    
    
    
      // TODO: Make this list change based on user selection!
    
      const selectedEffects = [
    
        intl.formatMessage({
    
          defaultMessage: "black and white",
    
          description:
    
            "An option that when selected, will apply a black and white effect to the generated image",
    
        }),
    
        intl.formatMessage({
    
          defaultMessage: "high contrast",
    
          description:
    
            "An option that when selected, will apply a high contrast effect to the generated image",
    
        }),
    
        intl.formatMessage({
    
          defaultMessage: "cartoon",
    
          description:
    
            "An option that when selected, will apply a cartoon effect to the generated image",
    
        }),
    
      ];
    
    
    
    
      return (
    
        <Text>
    
          <FormattedMessage
    
            defaultMessage="You have selected the following image effects: {effects}"
    
            description="Informs the user about the image effects they have selected. effects is a list of effects that will be applied to the generated image."
    
            values={{
    
              effects: intl.formatList(selectedEffects, {
    
                type: "conjunction",
    
              }),
    
            }}
    
          />
    
        </Text>
    
      );
    
    };

TSX

Copy

This component renders based on the user's locale. For example, an English list uses an Oxford comma, but German does not:

  * **English (en-US):** "You have selected the following image effects: black and white, high contrast, and cartoon."
  * **German (de-DE):** "Sie haben die folgenden Bildeffekte ausgewählt: Schwarzweiß, hoher Kontrast und Cartoon."



Do  
---  
Ensure that lists are formatted using methods that adapt to locale-specific conventions, such as comma placement and conjunction usage. Use library functions like `intl.formatList` of `react-intl` to automatically handle these variations, or use built-in JS APIs like [Intl.ListFormat⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/ListFormat)  
  
Don't  
---  
Avoid concatenating list items by using separators like commas or "and," as this might not be appropriate for all languages and locales.  
Don't overlook variations in list formatting conventions between different languages.  
  
### Display name formatting

How to use display name formatting to inform users about the app's active language, using the `FormattedMessage` component with React.

For example:
    
    
    <FormattedMessage
    
      defaultMessage="You are currently viewing this app in {language}"
    
      description="Shows the user which language the app is currently using"
    
      values={{
    
        language: intl.formatDisplayName(intl.locale, {
    
          type: "language",
    
        }),
    
      }}
    
    />

TSX

Copy

Do  
---  
Use `intl.formatDisplayName` or [Intl.DisplayNames⁠(opens in a new tab or window)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames) to retrieve and display the name of the active language.  
  
Don't  
---  
Avoid hardcoding language names directly in the UI, as this limits flexibility and might not adapt to all locale-specific language names.  
  
## Unsupported syntax

Don't use strings with multiple `plural` arguments. For example:  
---  
`{like_count, plural, one {1 like} other {{like_count} likes}} and {subscriber_count, plural, one {1 sub} other {{subscriber_count} subs}}`  
  
Don't use strings with a `plural` argument and `offset` property. For example:  
---  
`{like_count, plural, offset:1 =0 {no likes} other {{like_count} likes}}`  
  
Don't use strings with a `selectordinal` argument. For example:  
---  
`{n, selectordinal, one {This is the #st item} two {This is the #nd item} few {This is the #rd item} other {This is the #th item}}`  
  
Don't use strings containing the `choice` argument. For example:  
---  
`{user_category, choice, ...`  
  
Don't use strings that result in over 20 combinations. For example:  
---  
      
    
    {firstChoice, select,  optionA {First A}  optionB {First B}  other {First C}} {secondChoice, select,  optionX {Second X}  optionY {Second Y}  other {Second Z}} {thirdChoice, select,  option1 {Third 1}  option2 {Third 2}  other {Third 3}}

TSCopy

  * This example contains a select with 3 choices, followed by another select with 3 choices, followed by another select with 3 choices. This would result in 3 x 3 x 3 = 27 possible string combinations.

  
  
Don't use nested selects/plurals/select-plural combinations, except when the nested argument is a simple placeholder. For example, this nesting is not supported:   
---  
      
    
    {gender, select,   male {    {count, plural,       one {He has one item}       other {He has # items}    }  }   other {    {count, plural,       one {They have one item}       other {They have # items}    }  }}

TSCopy  
  
This nesting is supported:   
---  
      
    
    {task_count, plural,  one {    You have {# task_count} task: {task_name}.  }  other {    You have {# task_count} tasks. Next task: {task_name}.  }}

TSCopy  
  
## More information

  * Overview of the localization process: [Localization overview](https://www.canva.dev/docs/apps/localization/)
  * How to use the recommended workflow: [Recommended workflow](https://www.canva.dev/docs/apps/localization/recommended-workflow/)
  * How to localize an existing app: [Migrate an existing app](https://www.canva.dev/docs/apps/localization/migrate-an-existing-app/)
  * Review the localization design guidelines: [Localization](https://www.canva.dev/docs/apps/design-guidelines/localization/)
  * See bad practices: [Bad practices](https://www.canva.dev/docs/apps/localization/bad-practices/)


