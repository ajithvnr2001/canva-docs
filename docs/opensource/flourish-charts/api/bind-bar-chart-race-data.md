---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/
title: Bind bar chart race data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:09.183049+00:00
---

# Bind bar chart race data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind bar chart race data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_bar_chart_race_data(
    
        self,
    
        label: str = None,
    
        values: Union[list, str] = None,
    
        category: str = None,
    
        image: str = None,
    
        captions_from: str = None,
    
        captions_to: str = None,
    
        captions_text: str = None,
    
        captions_image: str = None
    
        )

PYTHON

Copy
    
    
    bind_bar_chart_race_data(
    
        .,
    
        label = NULL,
    
        values = NULL,
    
        category = NULL,
    
        image = NULL,
    
        captions_from = NULL,
    
        captions_to = NULL,
    
        captions_text = NULL,
    
        captions_image = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`label`| `str`, optional| Label. A column containing the names of the bars, e.g. countries or people. Suggested data type hints: string. Flourish type hint: column  
`values`| `Union[list, str]`, optional| Values. Multiple columns of numbers, each column representing a point in time Suggested data type hints: number. Flourish type hint: columns  
`category`| `str`, optional| Categories. Optional category column to color the bars Make sure the Color mode setting is set to By Category in the Bar colors settings panel. Suggested data type hints: string. Flourish type hint: column  
`image`| `str`, optional| Image. Optional column with URLs of images. Suggested data type hints: string. Flourish type hint: column  
`captions_from`| `str`, optional| Time to show. Must match the column headers in the main data sheet. Suggested data type hints: string, datetime. Flourish type hint: column  
`captions_to`| `str`, optional| Time to hide. Must match the column headers in the main data sheet. Suggested data type hints: string, datetime. Flourish type hint: column  
`captions_text`| `str`, optional| Text. Text or HTML to show. Suggested data type hints: string. Flourish type hint: column  
`captions_image`| `str`, optional| Image. Image to show. Add an image URL or right-click on a cell to upload an image. Suggested data type hints: string. Flourish type hint: column  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`label`| Label. A column containing the names of the bars, e.g. countries or people. Suggested data type hints: string. Flourish type hint: column  
`values`| Values. Multiple columns of numbers, each column representing a point in time Suggested data type hints: number. Flourish type hint: columns  
`category`| Categories. Optional category column to color the bars Make sure the Color mode setting is set to By Category in the Bar colors settings panel. Suggested data type hints: string. Flourish type hint: column  
`image`| Image. Optional column with URLs of images. Suggested data type hints: string. Flourish type hint: column  
`captions_from`| Time to show. Must match the column headers in the main data sheet. Suggested data type hints: string, datetime. Flourish type hint: column  
`captions_to`| Time to hide. Must match the column headers in the main data sheet. Suggested data type hints: string, datetime. Flourish type hint: column  
`captions_text`| Text. Text or HTML to show. Suggested data type hints: string. Flourish type hint: column  
`captions_image`| Image. Image to show. Add an image URL or right-click on a cell to upload an image. Suggested data type hints: string. Flourish type hint: column
