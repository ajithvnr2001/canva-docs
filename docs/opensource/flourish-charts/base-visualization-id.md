---
url: https://www.canva.dev/opensource/flourish-charts/base-visualization-id/
title: Extending the Flourish base visualization ID - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:58.205609+00:00
---

# Extending the Flourish base visualization ID - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/base-visualization-id/

Getting started

[Overview](https://www.canva.dev/opensource/flourish-charts/)[Set up Flourish Charts](https://www.canva.dev/opensource/flourish-charts/prerequisites/)[Creating Flourish graphs](https://www.canva.dev/opensource/flourish-charts/quickstart/)[Extending the Flourish base visualization ID](https://www.canva.dev/opensource/flourish-charts/base-visualization-id/)[Changelog](https://www.canva.dev/opensource/flourish-charts/changelog/)

API reference

[Flourish](https://www.canva.dev/opensource/flourish-charts/api/flourish/)[flourish-api-documentation](https://www.canva.dev/opensource/flourish-charts/api/flourish-api-documentation/)[gapminder](https://www.canva.dev/opensource/flourish-charts/api/gapminder/)

Binding additional data sources

Add extra details to charts

# Extending the Flourish base visualization ID

Copy page

PythonPython

RR
    
    
    from flourishcharts import Flourish
    
    from flourishcharts.datasets import gapminder

PYTHON

Copy
    
    
    library(flourishcharts)

R

Copy

Flourish allows users to extend visualizations created in the app online via the API. This feature uses a base visualization ID to call the original chart.

The original chart must be published via the app. Every Flourish URL pointing to a chart made in the editor cotains a unique ID - this is the base visualization ID. As an example, we published this chart using the default data source that Flourish provides: <https://public.flourish.studio/visualisation/17833871/>[⁠(opens in a new tab or window)](https://public.flourish.studio/visualisation/17833871/).

The base visualization ID is 17833871.

We are able to recreate this graph inside R or Python by passing the base visualization ID to the `flourish()` function in R or the `Flourish()` class in Python.

PythonPython

RR
    
    
    graph = Flourish(base_visualisation_id = 17833871)

PYTHON

Copy
    
    
    graph <- flourish(base_visualisation_id = 17833871)

R

Copy

In addition to _recreating_ it, we can also _extend_ the graph by writing over data, data bindings, or chart settings.

PythonPython

RR
    
    
    df = (
    
        gapminder[gapminder['year'] == gapminder['year'].max()]
    
            .assign(lifeExp=lambda x: x['lifeExp'].round())
    
            .sort_values(by='lifeExp')
    
            .head(10)
    
    )
    
    
    
    
    Flourish(
    
        base_visualisation_id = 17833871
    
    ).bind_line_bar_pie_data(
    
        data = df,
    
        label = "country",
    
        value = "lifeExp"
    
    ).set_line_bar_pie_details(
    
        chart_y_axis_title = "Bottom 10 Life Expectancy in 2007"
    
    )

PYTHON

Copy
    
    
    df <- gapminder |>
    
      filter(year == max(year)) |>
    
      mutate(lifeExp = round(lifeExp)) |>
    
      arrange(lifeExp) |>
    
      slice_head(n = 10)
    
    
    
    
    graph |>
    
      bind_line_bar_pie_data(
    
        data = df,
    
        label = "country",
    
        value = "lifeExp"
    
      ) |>
    
      set_line_bar_pie_details(
    
      chart_y_axis_title = "Bottom 10 Life Expectancy in 2007"
    
      )

R

Copy

This is a powerful notion because we can publish graphs with dummy data and write over them with _real_ data locally. This is important for conserving the privacy of enterprise data.

Additionally, as the Flourish team note in their documentation - the base visualization ID enables non-technical stakeholders to build and style graphs to which technical stakeholders can then add data. Moreover, if a non-technical stakeholder were to update the graph inside the website, the changes will flow down into the API.
