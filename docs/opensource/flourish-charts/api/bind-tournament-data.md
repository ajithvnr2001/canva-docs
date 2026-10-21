---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/
title: Bind tournament data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:12.372722+00:00
---

# Bind tournament data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind tournament data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_tournament_data(
    
        self,
    
        round: str = None,
    
        team_a: str = None,
    
        team_b: str = None,
    
        winner: str = None,
    
        score_a: str = None,
    
        score_b: str = None,
    
        metadata: Union[list, str] = None,
    
        id: str = None,
    
        image: str = None
    
        )

PYTHON

Copy
    
    
    bind_tournament_data(
    
        .,
    
        round = NULL,
    
        team_a = NULL,
    
        team_b = NULL,
    
        winner = NULL,
    
        score_a = NULL,
    
        score_b = NULL,
    
        metadata = NULL,
    
        id = NULL,
    
        image = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`round`| `str`, optional| Stage. The stage of the tournament, for example "Round of 16" or "Semifinals". Flourish type hint: column  
`team_a`| `str`, optional| Participant A. The first participant or team in this match. Flourish type hint: column  
`team_b`| `str`, optional| Participant B. The second participant or team in this match. Flourish type hint: column  
`winner`| `str`, optional| Winner. The winning participant or team in this match. Must match the name of either Participant A or Participant B. If left blank, the template will assume that the match is upcoming. Flourish type hint: column  
`score_a`| `str`, optional| Participant A score. The score of Participant A in this match. Will appear along with the participants name in the box. Suggested data type hints: string, number. Flourish type hint: column  
`score_b`| `str`, optional| Participant B score. The score of Participant B in this match. Will appear along with the participants name in the box. Suggested data type hints: string, number. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs , embedded charts etc) to include in popups and panels Suggested data type hints: string, number, datetime. Flourish type hint: columns  
`id`| `str`, optional| ID. Participant ID. Should match a participants name from the Matches sheet. Flourish type hint: column  
`image`| `str`, optional| Image. Image to render in the participant box. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`round`| Stage. The stage of the tournament, for example "Round of 16" or "Semifinals". Flourish type hint: column  
`team_a`| Participant A. The first participant or team in this match. Flourish type hint: column  
`team_b`| Participant B. The second participant or team in this match. Flourish type hint: column  
`winner`| Winner. The winning participant or team in this match. Must match the name of either Participant A or Participant B. If left blank, the template will assume that the match is upcoming. Flourish type hint: column  
`score_a`| Participant A score. The score of Participant A in this match. Will appear along with the participants name in the box. Suggested data type hints: string, number. Flourish type hint: column  
`score_b`| Participant B score. The score of Participant B in this match. Will appear along with the participants name in the box. Suggested data type hints: string, number. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs , embedded charts etc) to include in popups and panels Suggested data type hints: string, number, datetime. Flourish type hint: columns  
`id`| ID. Participant ID. Should match a participants name from the Matches sheet. Flourish type hint: column  
`image`| Image. Image to render in the participant box. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column
