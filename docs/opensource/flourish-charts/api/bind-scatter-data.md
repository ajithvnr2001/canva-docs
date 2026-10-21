---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/
title: Bind scatter data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:11.180456+00:00
---

# Bind scatter data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind scatter data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_scatter_data(
    
        self,
    
        x: str = None,
    
        y: str = None,
    
        name: Union[list, str] = None,
    
        color: str = None,
    
        size: str = None,
    
        shape: str = None,
    
        facet: str = None,
    
        slider: str = None,
    
        series: str = None,
    
        filter: str = None,
    
        metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_scatter_data(
    
        .,
    
        x = NULL,
    
        y = NULL,
    
        name = NULL,
    
        color = NULL,
    
        size = NULL,
    
        shape = NULL,
    
        facet = NULL,
    
        slider = NULL,
    
        series = NULL,
    
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
`x`| `str`, optional| X values. Suggested data type hints: number, string, datetime. Flourish type hint: column  
`y`| `str`, optional| Y values. Suggested data type hints: number, string, datetime. Flourish type hint: column  
`name`| `Union[list, str]`, optional| Name. Select multiple columns if required to make a unique name. Suggested data type hints: string. Flourish type hint: columns  
`color`| `str`, optional| Color. Colors the dots based on numbers or categories. Suggested data type hints: string, number. Flourish type hint: column  
`size`| `str`, optional| Size. Sizes the dots based on the numbers. Suggested data type hints: number, string. Flourish type hint: column  
`shape`| `str`, optional| Shape. Sets the shape of the dots based on numbers or categories. Suggested data type hints: string. Flourish type hint: column  
`facet`| `str`, optional| Grid of charts (facet). Creates a mini chart for each value in the selected column. Suggested data type hints: string. Flourish type hint: column  
`slider`| `str`, optional| Time. Creates a time slider and connects/animates dots with the same name. Suggested data type hints: datetime, string, number. Flourish type hint: column  
`series`| `str`, optional| Series (connect with line). Group dots into series based on the contents of a column. Suggested data type hints: string. Flourish type hint: column  
`filter`| `str`, optional| Filter control. Creates a control based on the contents of any column. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panelsSuggested data type hints: string, number, datetime. Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`x`| X values. Suggested data type hints: number, string, datetime. Flourish type hint: column  
`y`| Y values. Suggested data type hints: number, string, datetime. Flourish type hint: column  
`name`| Name. Select multiple columns if required to make a unique name. Suggested data type hints: string. Flourish type hint: columns  
`color`| Color. Colors the dots based on numbers or categories. Suggested data type hints: string, number. Flourish type hint: column  
`size`| Size. Sizes the dots based on the numbers. Suggested data type hints: number, string. Flourish type hint: column  
`shape`| Shape. Sets the shape of the dots based on numbers or categories. Suggested data type hints: string. Flourish type hint: column  
`facet`| Grid of charts (facet). Creates a mini chart for each value in the selected column. Suggested data type hints: string. Flourish type hint: column  
`slider`| Time. Creates a time slider and connects/animates dots with the same name. Suggested data type hints: datetime, string, number. Flourish type hint: column  
`series`| Series (connect with line). Group dots into series based on the contents of a column. Suggested data type hints: string. Flourish type hint: column  
`filter`| Filter control. Creates a control based on the contents of any column. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panelsSuggested data type hints: string, number, datetime. Flourish type hint: columns
