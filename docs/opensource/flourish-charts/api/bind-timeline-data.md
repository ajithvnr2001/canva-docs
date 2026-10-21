---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/
title: Bind timeline data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:12.054727+00:00
---

# Bind timeline data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind timeline data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_timeline_data(
    
        self,
    
        time_start: str = None,
    
        time_end: str = None,
    
        category: str = None,
    
        title: str = None,
    
        subtitle: str = None,
    
        text: str = None,
    
        image: str = None,
    
        background: str = None
    
        )

PYTHON

Copy
    
    
    bind_timeline_data(
    
        .,
    
        time_start = NULL,
    
        time_end = NULL,
    
        category = NULL,
    
        title = NULL,
    
        subtitle = NULL,
    
        text = NULL,
    
        image = NULL,
    
        background = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`time_start`| `str`, optional| Time start  
`time_end`| `str`, optional| End time. Sets the duration of the event in time scale mode. Flourish type hint: column  
`category`| `str`, optional| Category  
`title`| `str`, optional| Title. Title of the content. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`subtitle`| `str`, optional| Subtitle. Subtitle of the content. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`text`| `str`, optional| Text. Text to display inside the data point. Flourish type hint: column  
`image`| `str`, optional| Image. Main image for the event. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column  
`background`| `str`, optional| Background image. Background image for the event. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`time_start`| Time start  
`time_end`| End time. Sets the duration of the event in time scale mode. Flourish type hint: column  
`category`| Category  
`title`| Title. Title of the content. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`subtitle`| Subtitle. Subtitle of the content. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`text`| Text. Text to display inside the data point. Flourish type hint: column  
`image`| Image. Main image for the event. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column  
`background`| Background image. Background image for the event. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column
