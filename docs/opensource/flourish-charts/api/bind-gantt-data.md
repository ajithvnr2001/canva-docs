---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/
title: Bind gantt chart data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:10.080717+00:00
---

# Bind gantt chart data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind gantt chart data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_gantt_data(
    
        self,
    
        start_date: str = None,
    
        end_date: str = None,
    
        task: str = None,
    
        grouping: str = None,
    
        color: str = None,
    
        progress: str = None,
    
        filter: str = None,
    
        metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_gantt_data(
    
        .,
    
        start_date = NULL,
    
        end_date = NULL,
    
        task = NULL,
    
        grouping = NULL,
    
        color = NULL,
    
        progress = NULL,
    
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
`start_date`| `str`, optional| Start date  
`end_date`| `str`, optional| End date. The end date or time of the event. If working with days, the end date should be the first day after the end date. So if your event stretches from 1/1. and ends on the 5/1. your end date should be 6/1. This will mean your Gantt bar will stretch across the last day of your project or task. Flourish type hint: column  
`task`| `str`, optional| Task  
`grouping`| `str`, optional| Group. Select a categorical column to combine bars into groups on the Y axis. Flourish type hint: column  
`color`| `str`, optional| Color category. Select a categorical column; each unique value in the column will become a color. Flourish type hint: column  
`progress`| `str`, optional| Progress. Requires a number column with values between 0 and 1, representing the progress from 0 to 100%. Flourish type hint: column  
`filter`| `str`, optional| Filter. If set, creates a filter menu or time slider. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panelsFlourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`start_date`| Start date  
`end_date`| End date. The end date or time of the event. If working with days, the end date should be the first day after the end date. So if your event stretches from 1/1. and ends on the 5/1. your end date should be 6/1. This will mean your Gantt bar will stretch across the last day of your project or task. Flourish type hint: column  
`task`| Task  
`grouping`| Group. Select a categorical column to combine bars into groups on the Y axis. Flourish type hint: column  
`color`| Color category. Select a categorical column; each unique value in the column will become a color. Flourish type hint: column  
`progress`| Progress. Requires a number column with values between 0 and 1, representing the progress from 0 to 100%. Flourish type hint: column  
`filter`| Filter. If set, creates a filter menu or time slider. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panelsFlourish type hint: columns
