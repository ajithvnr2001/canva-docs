---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/
title: Bind cards data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:09.488235+00:00
---

# Bind cards data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind cards data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_cards_data(
    
        self,
    
        title: str = None,
    
        image: str = None,
    
        category: str = None,
    
        subtitle: str = None,
    
        text: Union[list, str] = None,
    
        audio: str = None,
    
        filter: str = None,
    
        metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_cards_data(
    
        .,
    
        title = NULL,
    
        image = NULL,
    
        category = NULL,
    
        subtitle = NULL,
    
        text = NULL,
    
        audio = NULL,
    
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
`title`| `str`, optional| Title. Suggested data type hints: string. Flourish type hint: column  
`image`| `str`, optional| Image. Suggested data type hints: string. Flourish type hint: column  
`category`| `str`, optional| Categories. Optional category column to color the cards. Suggested data type hints: string. Flourish type hint: column  
`subtitle`| `str`, optional| Subtitle. Suggested data type hints: string. Flourish type hint: column  
`text`| `Union[list, str]`, optional| Text. Suggested data type hints: string. Flourish type hint: columns  
`audio`| `str`, optional| Audio. Add an audio file to the card, which will play when the card is clicked. This will disable popup behavior. Suggested data type hints: string. Flourish type hint: column  
`filter`| `str`, optional| Filter. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in custom popups and panelsSuggested data type hints: string, number, datetime. Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`title`| Title. Suggested data type hints: string. Flourish type hint: column  
`image`| Image. Suggested data type hints: string. Flourish type hint: column  
`category`| Categories. Optional category column to color the cards. Suggested data type hints: string. Flourish type hint: column  
`subtitle`| Subtitle. Suggested data type hints: string. Flourish type hint: column  
`text`| Text. Suggested data type hints: string. Flourish type hint: columns  
`audio`| Audio. Add an audio file to the card, which will play when the card is clicked. This will disable popup behavior. Suggested data type hints: string. Flourish type hint: column  
`filter`| Filter. Suggested data type hints: string, number, datetime. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in custom popups and panelsSuggested data type hints: string, number, datetime. Flourish type hint: columns
