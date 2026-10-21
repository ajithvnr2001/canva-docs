---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/
title: Bind sports data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:11.722757+00:00
---

# Bind sports data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind sports data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_sports_data(
    
        self,
    
        info: Union[list, str] = None,
    
        color: str = None,
    
        size: str = None,
    
        squad_number: str = None,
    
        position_x: str = None,
    
        position_y: str = None,
    
        filter: str = None,
    
        photo: str = None,
    
        metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_sports_data(
    
        .,
    
        info = NULL,
    
        color = NULL,
    
        size = NULL,
    
        squad_number = NULL,
    
        position_x = NULL,
    
        position_y = NULL,
    
        filter = NULL,
    
        photo = NULL,
    
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
`info`| `Union[list, str]`, optional| Name. A name to include on a label and/or popup. Suggested data type hints: string, number. Flourish type hint: columns  
`color`| `str`, optional| Color by. An optional category column to color the dots by. For example if you have two different teams. Suggested data type hints: string. Flourish type hint: column  
`size`| `str`, optional| Size by. An optional numeric column to size the dots. Suggested data type hints: number. Flourish type hint: column  
`squad_number`| `str`, optional| Squad numbers. An optional squad number to appear within the dot. Suggested data type hints: number, string. Flourish type hint: column  
`position_x`| `str`, optional| X position. Use this to column to set the X position of a dot on the pitch when creating shot charts. This column is ignored when the setting Position points by is set to FormationSuggested data type hints: number. Flourish type hint: column  
`position_y`| `str`, optional| Y position. Use this to column to set the Y position of a dot on the pitch when creating shot charts. This column is ignored when the setting Position points by is set to FormationSuggested data type hints: number. Flourish type hint: column  
`filter`| `str`, optional| Filter by. Setting a column here will add a control to the visualization to filter the dots. For example you could filter by team. Suggested data type hints: string, number. Flourish type hint: column  
`photo`| `str`, optional| Image. Add an image to appear in the circles. To add an image, right click on a cell and click upload file Its also possible to add a image URL. Suggested data type hints: string. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panels Suggested data type hints: string, number, datetime. Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`info`| Name. A name to include on a label and/or popup. Suggested data type hints: string, number. Flourish type hint: columns  
`color`| Color by. An optional category column to color the dots by. For example if you have two different teams. Suggested data type hints: string. Flourish type hint: column  
`size`| Size by. An optional numeric column to size the dots. Suggested data type hints: number. Flourish type hint: column  
`squad_number`| Squad numbers. An optional squad number to appear within the dot. Suggested data type hints: number, string. Flourish type hint: column  
`position_x`| X position. Use this to column to set the X position of a dot on the pitch when creating shot charts. This column is ignored when the setting Position points by is set to FormationSuggested data type hints: number. Flourish type hint: column  
`position_y`| Y position. Use this to column to set the Y position of a dot on the pitch when creating shot charts. This column is ignored when the setting Position points by is set to FormationSuggested data type hints: number. Flourish type hint: column  
`filter`| Filter by. Setting a column here will add a control to the visualization to filter the dots. For example you could filter by team. Suggested data type hints: string, number. Flourish type hint: column  
`photo`| Image. Add an image to appear in the circles. To add an image, right click on a cell and click upload file Its also possible to add a image URL. Suggested data type hints: string. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panels Suggested data type hints: string, number, datetime. Flourish type hint: columns
