---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/
title: Bind hierarchy data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:10.154626+00:00
---

# Bind hierarchy data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind hierarchy data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_hierarchy_data(
    
        self,
    
        nest_columns: Union[list, str] = None,
    
        size_columns: Union[list, str] = None,
    
        filter: str = None,
    
        popup_metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_hierarchy_data(
    
        .,
    
        nest_columns = NULL,
    
        size_columns = NULL,
    
        filter = NULL,
    
        popup_metadata = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`nest_columns`| `Union[list, str]`, optional| Categories/nesting. Choose one or more categorical columns to nest by. The data is nested in the same order as the chosen columns (e.g. C, B is different from B, C). Suggested data type hints: string. Flourish type hint: columns  
`size_columns`| `Union[list, str]`, optional| Size by. Optionally choose one or more numeric columns to size by. If more than one is chosen, a dropdown will appear in the visualization which lets the user choose. Rows with negative values are excluded. Suggested data type hints: number. Flourish type hint: columns  
`filter`| `str`, optional| Filter. Optionally choose a categorical column to filter by. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`popup_metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs , embedded charts etc) to include in popups and panels Suggested data type hints: string, number, datetime. Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`nest_columns`| Categories/nesting. Choose one or more categorical columns to nest by. The data is nested in the same order as the chosen columns (e.g. C, B is different from B, C). Suggested data type hints: string. Flourish type hint: columns  
`size_columns`| Size by. Optionally choose one or more numeric columns to size by. If more than one is chosen, a dropdown will appear in the visualization which lets the user choose. Rows with negative values are excluded. Suggested data type hints: number. Flourish type hint: columns  
`filter`| Filter. Optionally choose a categorical column to filter by. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`popup_metadata`| Info for popups. One or more columns of information (text, image URLs , embedded charts etc) to include in popups and panels Suggested data type hints: string, number, datetime. Flourish type hint: columns
