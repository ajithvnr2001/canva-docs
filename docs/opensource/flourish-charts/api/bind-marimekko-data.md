---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/
title: Bind marimekko data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:10.617956+00:00
---

# Bind marimekko data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind marimekko data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_marimekko_data(
    
        self,
    
        name: str = None,
    
        unstacked_value: str = None,
    
        stacked_values: Union[list, str] = None,
    
        facet: str = None,
    
        category: str = None,
    
        filter: str = None,
    
        metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_marimekko_data(
    
        .,
    
        name = NULL,
    
        unstacked_value = NULL,
    
        stacked_values = NULL,
    
        facet = NULL,
    
        category = NULL,
    
        filter = NULL,
    
        metadata = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`name`| `str`, optional| Name  
`unstacked_value`| `str`, optional| Unstacked value  
`stacked_values`| `Union[list, str]`, optional| Secondary metric. One or more numeric columns. Each column will form a segment of a stacked bar. Flourish type hint: columns  
`facet`| `str`, optional| Facet  
`category`| `str`, optional| Color category. Suggested data type hints: string. Flourish type hint: column  
`filter`| `str`, optional| Filter by. (Optional) Choose a categorical column to filter by. A dropdown will appear in the visualization. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panels Suggested data type hints: number, string, datetime. Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`name`| Name  
`unstacked_value`| Unstacked value  
`stacked_values`| Secondary metric. One or more numeric columns. Each column will form a segment of a stacked bar. Flourish type hint: columns  
`facet`| Facet  
`category`| Color category. Suggested data type hints: string. Flourish type hint: column  
`filter`| Filter by. (Optional) Choose a categorical column to filter by. A dropdown will appear in the visualization. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panels Suggested data type hints: number, string, datetime. Flourish type hint: columns
