---
url: https://www.canva.dev/opensource/flourish-charts/api/flourish-api-documentation/
title: flourish-api-documentation - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:12.262496+00:00
---

# flourish-api-documentation - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/flourish-api-documentation/

Getting started

[Overview](https://www.canva.dev/opensource/flourish-charts/)[Set up Flourish Charts](https://www.canva.dev/opensource/flourish-charts/prerequisites/)[Creating Flourish graphs](https://www.canva.dev/opensource/flourish-charts/quickstart/)[Extending the Flourish base visualization ID](https://www.canva.dev/opensource/flourish-charts/base-visualization-id/)[Changelog](https://www.canva.dev/opensource/flourish-charts/changelog/)

API reference

[Flourish](https://www.canva.dev/opensource/flourish-charts/api/flourish/)[flourish-api-documentation](https://www.canva.dev/opensource/flourish-charts/api/flourish-api-documentation/)[gapminder](https://www.canva.dev/opensource/flourish-charts/api/gapminder/)

Binding additional data sources

Add extra details to charts

# flourish-api-documentation

Get a list of chart types.

Copy page

A dataset containing list of all the available chart types for Flourish charts.

PythonPython

RR

## Usage
    
    
    from flourishcharts.flourish_api_docs import reference
    
    reference

PYTHON

Copy

## Columns

  * **template_name** : Template name as provided by Flourish.
  * **chart_type** : Chart type string. This must match a `chart_type` value in the `flourish()`/`Flourish()` function.
  * **url** : URL linking to the Flourish API documentation for the template.



## Module Source

`python_package/data/flourish_api_documentation.csv`

## Usage
    
    
    library(flourishcharts)
    
    flourish_api_documentation

R

Copy

## Columns

  * **template_name** : Template name as provided by Flourish.
  * **chart_type** : Chart type string. This must match a `chart_type` value in the `flourish()`/`Flourish()` function.
  * **url** : URL linking to the Flourish API documentation for the template.



## Module Source

`R_package/R/data.R`
