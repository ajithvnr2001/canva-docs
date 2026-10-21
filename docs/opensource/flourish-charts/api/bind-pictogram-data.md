---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/
title: Bind pictogram data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:10.837971+00:00
---

# Bind pictogram data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind pictogram data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_pictogram_data(
    
        self,
    
        main_category: str = None,
    
        sub_category: str = None,
    
        values: Union[list, str] = None,
    
        icon_id: str = None,
    
        color: str = None,
    
        metadata: Union[list, str] = None,
    
        icons_id: str = None,
    
        icons_path_string: str = None,
    
        icons_width: str = None,
    
        icons_height: str = None
    
        )

PYTHON

Copy
    
    
    bind_pictogram_data(
    
        .,
    
        main_category = NULL,
    
        sub_category = NULL,
    
        values = NULL,
    
        icon_id = NULL,
    
        color = NULL,
    
        metadata = NULL,
    
        icons_id = NULL,
    
        icons_path_string = NULL,
    
        icons_width = NULL,
    
        icons_height = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`main_category`| `str`, optional| Main category. The (categorical) column that defines the categories along the main axis. Flourish type hint: column  
`sub_category`| `str`, optional| Subcategory. The (categorical) column that defines the categories within each bar. Flourish type hint: column  
`values`| `Union[list, str]`, optional| Values. (Optional) Choose the numeric columns to determine the size of each bar. If more than 1 is chosen, a dropdown will appear in the visualization, which lets the user choose. Flourish type hint: columns  
`icon_id`| `str`, optional| Icon ID. IDs for joining icons in the Icons datasheet. Must contain IDs that match Icon ID values in Icons Set to the same column as the Main category or Subcategory. Flourish type hint: column  
`color`| `str`, optional| Color. The (categorical) column which determines the icon color. Set to the same column as the Main category or Subcategory. Flourish type hint: column  
`metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panels Flourish type hint: columns  
`icons_id`| `str`, optional| Icon ID. Unique ID for joining icon path strings. Must contain IDs that match the Icon ID values in DataFlourish type hint: column  
`icons_path_string`| `str`, optional| Icon. Icon path string (e.g. "M10,10 l80,0 l0,80 l-80,0 z") or the name of a built-in icon (e.g. "female"). Flourish type hint: column  
`icons_width`| `str`, optional| Icon width. Icon width (in pixels). Flourish type hint: column  
`icons_height`| `str`, optional| Icon height. Icon height (in pixels). Flourish type hint: column  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`main_category`| Main category. The (categorical) column that defines the categories along the main axis. Flourish type hint: column  
`sub_category`| Subcategory. The (categorical) column that defines the categories within each bar. Flourish type hint: column  
`values`| Values. (Optional) Choose the numeric columns to determine the size of each bar. If more than 1 is chosen, a dropdown will appear in the visualization, which lets the user choose. Flourish type hint: columns  
`icon_id`| Icon ID. IDs for joining icons in the Icons datasheet. Must contain IDs that match Icon ID values in Icons Set to the same column as the Main category or Subcategory. Flourish type hint: column  
`color`| Color. The (categorical) column which determines the icon color. Set to the same column as the Main category or Subcategory. Flourish type hint: column  
`metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panels Flourish type hint: columns  
`icons_id`| Icon ID. Unique ID for joining icon path strings. Must contain IDs that match the Icon ID values in DataFlourish type hint: column  
`icons_path_string`| Icon. Icon path string (e.g. "M10,10 l80,0 l0,80 l-80,0 z") or the name of a built-in icon (e.g. "female"). Flourish type hint: column  
`icons_width`| Icon width. Icon width (in pixels). Flourish type hint: column  
`icons_height`| Icon height. Icon height (in pixels). Flourish type hint: column
