---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/
title: Bind interactive svg data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:10.339949+00:00
---

# Bind interactive svg data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind interactive svg data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_interactive_svg_data(
    
        self,
    
        id: str = None,
    
        reveal_id: str = None,
    
        h3: str = None,
    
        h4: str = None,
    
        content: str = None,
    
        link: str = None,
    
        metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_interactive_svg_data(
    
        .,
    
        id = NULL,
    
        reveal_id = NULL,
    
        h3 = NULL,
    
        h4 = NULL,
    
        content = NULL,
    
        link = NULL,
    
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
`id`| `str`, optional| ID. A column of IDs of elements in the uploaded SVG file. Flourish type hint: column  
`reveal_id`| `str`, optional| Reveal layer. A column to reveal when layer is clicked. Flourish type hint: column  
`h3`| `str`, optional| Heading 1. A column containing the main header. Flourish type hint: column  
`h4`| `str`, optional| Heading 2. A column containing a secondary header. Flourish type hint: column  
`content`| `str`, optional| Content. A column containing text or HTML to display. Flourish type hint: column  
`link`| `str`, optional| Link. A URL that can be opened when a layer is clicked. Any reveal layers or popups will be overridden. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in custom popups and panels Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`id`| ID. A column of IDs of elements in the uploaded SVG file. Flourish type hint: column  
`reveal_id`| Reveal layer. A column to reveal when layer is clicked. Flourish type hint: column  
`h3`| Heading 1. A column containing the main header. Flourish type hint: column  
`h4`| Heading 2. A column containing a secondary header. Flourish type hint: column  
`content`| Content. A column containing text or HTML to display. Flourish type hint: column  
`link`| Link. A URL that can be opened when a layer is clicked. Any reveal layers or popups will be overridden. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in custom popups and panels Flourish type hint: columns
