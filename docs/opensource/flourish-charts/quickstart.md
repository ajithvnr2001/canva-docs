---
url: https://www.canva.dev/opensource/flourish-charts/quickstart/
title: Creating Flourish graphs in R and Python - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:58.712224+00:00
---

# Creating Flourish graphs in R and Python - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/quickstart/

Getting started

[Overview](https://www.canva.dev/opensource/flourish-charts/)[Set up Flourish Charts](https://www.canva.dev/opensource/flourish-charts/prerequisites/)[Creating Flourish graphs](https://www.canva.dev/opensource/flourish-charts/quickstart/)[Extending the Flourish base visualization ID](https://www.canva.dev/opensource/flourish-charts/base-visualization-id/)[Changelog](https://www.canva.dev/opensource/flourish-charts/changelog/)

API reference

[Flourish](https://www.canva.dev/opensource/flourish-charts/api/flourish/)[flourish-api-documentation](https://www.canva.dev/opensource/flourish-charts/api/flourish-api-documentation/)[gapminder](https://www.canva.dev/opensource/flourish-charts/api/gapminder/)

Binding additional data sources

Add extra details to charts

# Creating Flourish graphs in R and Python

Copy page

Flourish primarily depends on two main functions in R and Python.

  * **Python users:** `Flourish()` and a `bind_..._data()` function.
  * **R users:** `flourish()` and a `bind_..._data()` function.



The `...` depends on the chart type. A list of chart types can be found `flourish_api_documentation['chart_type']` in R or `reference['chart_type']` in Python.

In Python you can wrap the function in `help()` to see the docstrings and also shift tab to view the docstrings dynamically while coding. In R, you can find a list of Flourish functions by running `flourishcharts::`, typing `?flourishcharts` in your console, or heading over to the references page in this site.

The following chunks show some example charts using Gapminder data, with accompanying notes.

## Get started

The Flourish Charts package provides a data frame (`flourish_api_documentation` in R or `reference` in Python) with metadata about each graph (template ID, version, a simplified chart name for end users, and a URL to Flourish's API documentation).

PythonPython

RR
    
    
    from flourishcharts import Flourish
    
    from flourishcharts.datasets import gapminder
    
    from flourishcharts.flourish_docs import reference
    
    import pandas as pd

PYTHON

Copy
    
    
    library(flourishcharts)
    
    library(tidyr)
    
    library(dplyr)

R

Copy

## Add additional information

PythonPython

RR
    
    
    reference[['template_name', 'chart_type', 'url']].head()

PYTHON

Copy
    
    
    head(flourish_api_documentation)

R

Copy

Flourish Charts requires the following functions to plot Flourish graphs:

  * Mandatory arguments in `flourish()` in R or `Flourish()` in Python: 
    * `chart_type`: A string that must match a value in `flourish_api_documentation["chart_type"]`. This tells Flourish the chart template you want to use to visualize your data.
    * The API key. This can be set in two ways: 
      * As per the setup steps in [Flourish API key](https://www.canva.dev/opensource/flourish-charts/prerequisites/#flourish-api-key) which will point to the default value.
      * or by passing a string to `api_key`.
  * `bind_..._data()`: A data bindings function that allows users to upload data to the graph and tell Flourish which column, or data binding, should go where on the chart. For more information on the information required, see the [Flourish API documentation for each graph type⁠(opens in a new tab or window)](https://app.flourish.studio/@flourish).
  * Add additional details by running `set_..._details()` — for example, `set_scatter_details()`. This is where you can change the chart color palette, axes labels, and so on.



Every function can be piped or chained into another. For example, R users can use the base pipe `|>` to chain together the main `flourish()` function and a data bindings function, like `bind_scatter_data` : `flourish() |> bind_scatter_data()`. Python users are able to chain the functions together by appending each function prefixed with a period: `Flourish().bind_scatter_data()`.

## Examples

### Scatterplot

PythonPython

RR
    
    
    scatterplot = Flourish(
    
        chart_type = "scatter"
    
    ).bind_scatter_data(
    
        data = gapminder,
    
        x = "gdpPercap",
    
        y = "lifeExp",
    
        slider = "year",
    
        metadata = ["country", "year"],
    
        size = "pop",
    
        color = "continent"
    
    )
    
    scatterplot

PYTHON

Copy
    
    
    scatterplot <- flourish(
    
      chart_type = "scatter"
    
    ) |>
    
    bind_scatter_data(
    
      data = gapminder,
    
      x = "gdpPercap",
    
      y = "lifeExp",
    
      slider = "year",
    
      size = "pop",
    
      color = "continent",
    
      metadata = c("country", "year")
    
    )
    
    scatterplot

R

Copy

### Bar chart race

Please note that some Flourish graphs require wide datasets. We convert the `gapminder` dataframe from long to wide below.

PythonPython

RR
    
    
    # Define the subset of countries
    
    subset_countries = [
    
        "Australia", "New Zealand", "United States",
    
        "Rwanda", "Sierra Leone", "Indonesia", "Brazil"
    
    ]
    
    # Filter the DataFrame and select relevant columns
    
    subset_countries_bcr_df = (
    
        gapminder[gapminder['country'].isin(subset_countries)]
    
        [["year", "lifeExp", "country", "continent"]]
    
    )
    
    # Pivot the DataFrame to a wide format
    
    countries_wide_bcr = subset_countries_bcr_df.pivot(
    
        index=["country", "continent"],
    
        columns="year",
    
        values="lifeExp"
    
    )
    
    # Convert the pivot table to a DataFrame
    
    countries_wide_bcr_df = countries_wide_bcr.reset_index()
    
    
    
    
    bcr = Flourish(
    
        "bar_race"
    
    ).bind_bar_chart_race_data(
    
        data = countries_wide_bcr_df,
    
        label = "country",
    
        values = ["1952", "1957",
    
        "1962", "1967", "1972", "1977",
    
        "1982", "1987", "1992", "1997",
    
        "2002", "2007"],
    
        category = "continent"
    
    ).set_bar_chart_race_details(
    
        chart_layout_title = "Life expectancy from the 1950s to 2007",
    
        chart_layout_subtitle = "Selected countries include Australia, New Zealand, the US, Rwanda, Indonesia, Sierra Leone, and Brazil.",
    
        totaliser = False
    
    )
    
    bcr

PYTHON

Copy
    
    
    bcr_data <- gapminder |>
    
      filter(country %in% c(
    
        "Australia",
    
        "New Zealand",
    
        "United States",
    
        "Rwanda",
    
        "Sierra Leone",
    
        "Indonesia",
    
        "Brazil"
    
      )) |>
    
      select(c("country", "continent", "year", "lifeExp")) |>
    
      pivot_wider(
    
        id_cols = c("country", "continent"),
    
        names_from = "year",
    
        values_from = "lifeExp"
    
    )
    
    
    
    
    bcr <- flourish("bar_race") |>
    
      bind_bar_chart_race_data(
    
        data = bcr_data,
    
        label = "country",
    
        values = colnames(bcr_data[, c(3:14)]),
    
        category = "continent"
    
      ) |>
    
      set_bar_chart_race_details(
    
        chart_layout_title = "Life expectancy from the 1950s to 2007",
    
        chart_layout_subtitle = "Selected countries include Australia, New Zealand, the US, Rwanda, Indonesia, Sierra Leone, and Brazil.",
    
        totaliser = FALSE
    
      )
    
    bcr

R

Copy

### Alluvial Diagram

PythonPython

RR
    
    
    from io import StringIO
    
    
    
    
    d = '''before,after,seat_flow
    
    Radicals,Radicals,27
    
    Moderates,Moderates,18
    
    Green,Green,4
    
    Progressives,Progressives,15
    
    Radicals,Moderates,28
    
    Progressives,Radicals,12
    
    Libertarians,Libertarians,8
    
    Moderates,Radicals,10
    
    Progressives,Moderates,6
    
    Radicals,Independents,5
    
    Independents,Independents,4
    
    Progressives,Independents,3
    
    Progressives,Libertarians,7
    
    Independents,Moderates,2
    
    Loonies,Green,2
    
    Independents,Radicals,1
    
    Loonies,Libertarians,10
    
    Independents,Independents,1'''
    
    
    
    
    
    
    
    df = pd.read_csv(StringIO(d), sep=',')
    
    
    
    
    alluvial_graph = Flourish(
    
        chart_type = "sankey"
    
    ).bind_sankey_data(
    
        data = df,
    
        source = "before",
    
        target = "after",
    
        value = "seat_flow"
    
    )
    
    alluvial_graph

PYTHON

Copy
    
    
    alluvial_data <- tibble::tribble(
    
        ~before,~after,~seat_flow,
    
        "Radicals","Radicals" , 27,
    
        "Moderates","Moderates",1,
    
        "Green","Green",4,
    
        "Progressives","Progressives",15,
    
        "Radicals","Moderates",28,
    
        "Progressives","Radicals",12,
    
        "Libertarians","Libertarians",8,
    
        "Moderates","Radicals",10,
    
        "Progressives","Moderates",6,
    
        "Radicals","Independents",5,
    
        "Independents","Independents",4,
    
        "Progressives","Independents",3,
    
        "Progressives","Libertarians",7,
    
        "Independents","Moderates",2,
    
        "Loonies","Green",2,
    
        "Independents","Radicals",1,
    
        "Loonies","Libertarians",10,
    
        "Independents","Independents",1
    
    )
    
    
    
    
    alluvial_graph <- flourish(chart_type = "sankey") |>
    
      bind_sankey_data(data = alluvial_data,
    
      source = "before",
    
      target = "after",
    
      value = "seat_flow"
    
    )
    
    alluvial_graph

R

Copy
