---
url: https://www.canva.dev/opensource/flourish-charts/api/flourish/
title: Flourish - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:12.431888+00:00
---

# Flourish - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/flourish/

Getting started

[Overview](https://www.canva.dev/opensource/flourish-charts/)[Set up Flourish Charts](https://www.canva.dev/opensource/flourish-charts/prerequisites/)[Creating Flourish graphs](https://www.canva.dev/opensource/flourish-charts/quickstart/)[Extending the Flourish base visualization ID](https://www.canva.dev/opensource/flourish-charts/base-visualization-id/)[Changelog](https://www.canva.dev/opensource/flourish-charts/changelog/)

API reference

[Flourish](https://www.canva.dev/opensource/flourish-charts/api/flourish/)[flourish-api-documentation](https://www.canva.dev/opensource/flourish-charts/api/flourish-api-documentation/)[gapminder](https://www.canva.dev/opensource/flourish-charts/api/gapminder/)

Binding additional data sources

Add extra details to charts

# Flourish

Create a graph using Flourish.

Copy page

PythonPython

RR

The `Flourish` class for generating Flourish graphs in Python.

## Usage
    
    
    class Flourish(
    
        anywidget.AnyWidget,
    
        details.DetailsMixin,
    
        bindings.DataBindingsMixin
    
    )

PYTHON

Copy

## Arguments

Argument| Type hint| Description  
---|---|---  
`chart_type`| `str`, optional| A chart type string for a graph in Flourish's library. Use `chart_type` instead of `template_id` and `template_version` where possible.  
`base_visualisation_id`| `str`, optional| Provide the numerical ID of an existing public Flourish visualization to reference it's configuration.  
`chart_description`| `str`, optional| A description of the chart contents for assistive technologies, such as screen-readers. For example “The line chart shows China consistently higher than the other countries since 1990”. Defaults to `None`.  
`template_id`| `str`, optional| A template ID, as set by Flourish, found at <https://app.flourish.studio/@flourish>[⁠(opens in a new tab or window)](https://app.flourish.studio/@flourish). Use if you can't use `chart_type` or `base_visualisation_id`. Defaults to `None`.  
`template_version_number`| `str`, optional| A template version number, as set by Flourish, found at <https://app.flourish.studio/@flourish>[⁠(opens in a new tab or window)](https://app.flourish.studio/@flourish). Use if you can't use `chart_type` or `base_visualisation_id`. Defaults to `None`.  
`width`| `int`, optional| Width of the graph. Defaults to `None`.  
`height`| `int`, optional| Height of the graph. Defaults to `None`.  
`api_key`| `str`, optional| A Flourish API key, which you can generate in your Flourish account. Defaults to `None`.  
  
## Class

`Flourish` Objects

## Module Source

Module `flourishcharts.flourish`

The `flourish` function for generating Flourish graphs in R.

## Usage
    
    
    flourish(
    
      chart_type = 'line',
    
      chart_description = 'Chart showing the number of households with internet increasing over 20 years',
    
      base_visualisation_id = NULL,
    
      template_id = '@flourish/line-bar-pie',
    
      template_version_number = 32.3.2,
    
      api_key = Sys.getenv("FLOURISH_API_KEY")
    
    )

R

Copy

## Arguments

Arguments| Description  
---|---  
`chart_type`| Required - a chart type string for each graph in Flourish's library. Preferred usage compared to `template_id` and `template_version`.  
`chart_description`| Optional - A description of the chart contents for assistive technologies, such as screen-readers. For example “The line chart shows China consistently higher than the other countries since 1990”.  
`base_visualisation_id`| Optional - provide the numerical ID of an existing public (published) Flourish visualization to reference it's configuration.  
`template_id`| Optional - the Flourish template ID, found at <https://app.flourish.studio/@flourish>[⁠(opens in a new tab or window)](https://app.flourish.studio/@flourish). Use if you can't use `chart_type`.  
`template_version_number`| Optional - the template's version number. Also found at <https://app.flourish.studio/@flourish>[⁠(opens in a new tab or window)](https://app.flourish.studio/@flourish). Use if you can't use `chart_type`.  
`api_key`| Required - a Flourish API key, which you can generate in your Flourish account. Defaults to `Sys.getenv("FLOURISH_API_KEY")`.  
  
## Module Source

`R/flourish.R`
