---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/
title: Bind network graph data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:10.487878+00:00
---

# Bind network graph data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind network graph data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_network_graph_data(
    
        self,
    
        links_source: str = None,
    
        links_target: str = None,
    
        links_value: str = None,
    
        nodes_id: str = None,
    
        nodes_group: str = None,
    
        nodes_size: str = None,
    
        nodes_image: str = None,
    
        nodes_metadata: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_network_graph_data(
    
        .,
    
        links_source = NULL,
    
        links_target = NULL,
    
        links_value = NULL,
    
        nodes_id = NULL,
    
        nodes_group = NULL,
    
        nodes_size = NULL,
    
        nodes_image = NULL,
    
        nodes_metadata = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`links_source`| `str`, optional| Links source  
`links_target`| `str`, optional| Links target  
`links_value`| `str`, optional| Size by. A numerical value used to set the thickness of the links. Flourish type hint: column  
`nodes_id`| `str`, optional| ID. A unique identifier for each point in the network. If not specified, point information will be extracted from the links sheet. Flourish type hint: column  
`nodes_group`| `str`, optional| Color by. A group to which the point belongs. If set, can be used to color the points. Ignored if ID not set. Flourish type hint: column  
`nodes_size`| `str`, optional| Size by. A numerical value used to size the points. Ignored if ID not set. Flourish type hint: column  
`nodes_image`| `str`, optional| Image. An image to go into the circle. Flourish type hint: column  
`nodes_metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs , embedded charts etc) to include in popups and panels Ignored if ID not set. Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`links_source`| Links source  
`links_target`| Links target  
`links_value`| Size by. A numerical value used to set the thickness of the links. Flourish type hint: column  
`nodes_id`| ID. A unique identifier for each point in the network. If not specified, point information will be extracted from the links sheet. Flourish type hint: column  
`nodes_group`| Color by. A group to which the point belongs. If set, can be used to color the points. Ignored if ID not set. Flourish type hint: column  
`nodes_size`| Size by. A numerical value used to size the points. Ignored if ID not set. Flourish type hint: column  
`nodes_image`| Image. An image to go into the circle. Flourish type hint: column  
`nodes_metadata`| Info for popups. One or more columns of information (text, image URLs , embedded charts etc) to include in popups and panels Ignored if ID not set. Flourish type hint: columns
