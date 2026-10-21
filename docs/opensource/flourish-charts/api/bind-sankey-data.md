---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/
title: Bind sankey diagram data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:11.299283+00:00
---

# Bind sankey diagram data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind sankey diagram data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_sankey_data(
    
        self,
    
        source: str = None,
    
        target: str = None,
    
        value: str = None,
    
        filter: str = None,
    
        facet: str = None,
    
        step_from: str = None,
    
        step_to: str = None,
    
        metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_sankey_data(
    
        .,
    
        source = NULL,
    
        target = NULL,
    
        value = NULL,
    
        filter = NULL,
    
        facet = NULL,
    
        step_from = NULL,
    
        step_to = NULL,
    
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
`source`| `str`, optional| Source. Suggested data type hints: string. Flourish type hint: column  
`target`| `str`, optional| Target. Suggested data type hints: string. Flourish type hint: column  
`value`| `str`, optional| Value of link. A numerical value used to set the thickness of the links. Suggested data type hints: number. Flourish type hint: column  
`filter`| `str`, optional| Filter. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`facet`| `str`, optional| Grid of charts. Suggested data type hints: string. Flourish type hint: column  
`step_from`| `str`, optional| Step from. An integer(whole number) used to indicate where a link starts from (used only in Alluvial mode). Suggested data type hints: number. Flourish type hint: column  
`step_to`| `str`, optional| Step to. An integer(whole number) used to indicate where a link goes to (used only in Alluvial mode). Suggested data type hints: number. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panels Suggested data type hints: number, datetime, string. Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`source`| Source. Suggested data type hints: string. Flourish type hint: column  
`target`| Target. Suggested data type hints: string. Flourish type hint: column  
`value`| Value of link. A numerical value used to set the thickness of the links. Suggested data type hints: number. Flourish type hint: column  
`filter`| Filter. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`facet`| Grid of charts. Suggested data type hints: string. Flourish type hint: column  
`step_from`| Step from. An integer(whole number) used to indicate where a link starts from (used only in Alluvial mode). Suggested data type hints: number. Flourish type hint: column  
`step_to`| Step to. An integer(whole number) used to indicate where a link goes to (used only in Alluvial mode). Suggested data type hints: number. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panels Suggested data type hints: number, datetime, string. Flourish type hint: columns
