---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/
title: Bind line chart race data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:10.254657+00:00
---

# Bind line chart race data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind line chart race data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_horserace_data(
    
        self,
    
        horserace_name: str = None,
    
        horserace_stages: Union[list, str] = None,
    
        horserace_category: str = None,
    
        horserace_pic: str = None,
    
        horserace_filter: str = None,
    
        captions_from: str = None,
    
        captions_to: str = None,
    
        captions_text: str = None,
    
        captions_image: str = None
    
        )

PYTHON

Copy
    
    
    bind_horserace_data(
    
        .,
    
        horserace_name = NULL,
    
        horserace_stages = NULL,
    
        horserace_category = NULL,
    
        horserace_pic = NULL,
    
        horserace_filter = NULL,
    
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
`horserace_name`| `str`, optional| Label. The name of each entrant. Suggested data type hints: string. Flourish type hint: column  
`horserace_stages`| `Union[list, str]`, optional| Values. Raw scores, which will be automatically converted to ranks. Column names will be used to populate the X axis of the chart. Suggested data type hints: number. Flourish type hint: columns  
`horserace_category`| `str`, optional| Color by. Select a column to color the lines by. If omitted, colors will be assigned per name. Suggested data type hints: string. Flourish type hint: column  
`horserace_pic`| `str`, optional| Image. Add an image URL or right-click on a cell to upload an image. Suggested data type hints: string. Flourish type hint: column  
`horserace_filter`| `str`, optional| Filter. Hide/show entrants based on the values in this column. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`captions_from`| `str`, optional| Stage to show. Must match the column headers in the main datasheet. Suggested data type hints: string. Flourish type hint: column  
`captions_to`| `str`, optional| Stage to hide. Must match the column headers in the main datasheet. Suggested data type hints: string. Flourish type hint: column  
`captions_text`| `str`, optional| Text. Text or HTML to show. Suggested data type hints: string. Flourish type hint: column  
`captions_image`| `str`, optional| Image. Image to show. Suggested data type hints: string. Flourish type hint: column  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`horserace_name`| Label. The name of each entrant. Suggested data type hints: string. Flourish type hint: column  
`horserace_stages`| Values. Raw scores, which will be automatically converted to ranks. Column names will be used to populate the X axis of the chart. Suggested data type hints: number. Flourish type hint: columns  
`horserace_category`| Color by. Select a column to color the lines by. If omitted, colors will be assigned per name. Suggested data type hints: string. Flourish type hint: column  
`horserace_pic`| Image. Add an image URL or right-click on a cell to upload an image. Suggested data type hints: string. Flourish type hint: column  
`horserace_filter`| Filter. Hide/show entrants based on the values in this column. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`captions_from`| Stage to show. Must match the column headers in the main datasheet. Suggested data type hints: string. Flourish type hint: column  
`captions_to`| Stage to hide. Must match the column headers in the main datasheet. Suggested data type hints: string. Flourish type hint: column  
`captions_text`| Text. Text or HTML to show. Suggested data type hints: string. Flourish type hint: column  
`captions_image`| Image. Image to show. Suggested data type hints: string. Flourish type hint: column
