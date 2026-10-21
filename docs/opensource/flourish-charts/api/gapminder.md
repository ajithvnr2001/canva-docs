---
url: https://www.canva.dev/opensource/flourish-charts/api/gapminder/
title: gapminder - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:12.485817+00:00
---

# gapminder - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/gapminder/

Getting started

[Overview](https://www.canva.dev/opensource/flourish-charts/)[Set up Flourish Charts](https://www.canva.dev/opensource/flourish-charts/prerequisites/)[Creating Flourish graphs](https://www.canva.dev/opensource/flourish-charts/quickstart/)[Extending the Flourish base visualization ID](https://www.canva.dev/opensource/flourish-charts/base-visualization-id/)[Changelog](https://www.canva.dev/opensource/flourish-charts/changelog/)

API reference

[Flourish](https://www.canva.dev/opensource/flourish-charts/api/flourish/)[flourish-api-documentation](https://www.canva.dev/opensource/flourish-charts/api/flourish-api-documentation/)[gapminder](https://www.canva.dev/opensource/flourish-charts/api/gapminder/)

Binding additional data sources

Add extra details to charts

# gapminder

Example dataset from Gapminder.

Copy page

Flourish charts comes with some example data from Gapminder ([gapminder.org⁠(opens in a new tab or window)](https://www.gapminder.org/)) that you can use for experimenting with the Flourish charts libraries.

## Usage

PythonPython

RR
    
    
    from flourishcharts.datasets import gapminder
    
    gapminder

PYTHON

Copy
    
    
    library(flourishcharts)
    
    gapminder

R

Copy

## Columns

  * **country** : Country name, listed in alphabetical order starting with Afghanistan. 142 countries are listed in the data.
  * **continent** : Continent name.
  * **year** : Year the data was collected.
  * **lifeExp** : Life expectancy of people in that country in the given year.
  * **pop** : Population of country
  * **gdpPercap** : GDP per capita



## Module Source

  * **R** : `R_package/R/data.R`
  * **Python** : `python_package/flourishcharts/data/gapminder.csv`


