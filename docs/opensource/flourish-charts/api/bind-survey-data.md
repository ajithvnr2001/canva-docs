---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/
title: Bind survey data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:11.595734+00:00
---

# Bind survey data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind survey data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_survey_data(
    
        self,
    
        questions_categorical: Union[list, str] = None,
    
        questions_continuous: Union[list, str] = None,
    
        questions_geo: Union[list, str] = None,
    
        questions_label: str = None,
    
        questions_column_filter: str = None,
    
        questions_id: str = None,
    
        questions_metadata: Union[list, str] = None,
    
        order_categories: Union[list, str] = None,
    
        labels_label: str = None,
    
        labels_replacement: str = None,
    
        colors_question: str = None,
    
        colors_answer: str = None,
    
        colors_color: str = None,
    
        places_latitude: str = None,
    
        places_longitude: str = None,
    
        places_names: Union[list, str] = None,
    
        answer_groups_group: str = None,
    
        answer_groups_question: str = None,
    
        answer_groups_display_as: str = None,
    
        answer_groups_affirmative_answers: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    bind_survey_data(
    
        .,
    
        questions_categorical = NULL,
    
        questions_continuous = NULL,
    
        questions_geo = NULL,
    
        questions_label = NULL,
    
        questions_column_filter = NULL,
    
        questions_id = NULL,
    
        questions_metadata = NULL,
    
        order_categories = NULL,
    
        labels_label = NULL,
    
        labels_replacement = NULL,
    
        colors_question = NULL,
    
        colors_answer = NULL,
    
        colors_color = NULL,
    
        places_latitude = NULL,
    
        places_longitude = NULL,
    
        places_names = NULL,
    
        answer_groups_group = NULL,
    
        answer_groups_question = NULL,
    
        answer_groups_display_as = NULL,
    
        answer_groups_affirmative_answers = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`questions_categorical`| `Union[list, str]`, optional| Categorical columns. Each of these columns appears in the Group by, Shade by and Compare dropdowns. Flourish type hint: columns  
`questions_continuous`| `Union[list, str]`, optional| Continuous columns. Must contain numbers. Each of these columns appears in the Size by dropdown. Flourish type hint: columns  
`questions_geo`| `Union[list, str]`, optional| Geographic columns. Must contain place names matching those specified in the Places sheet. Set to blank to disable the map mode. Flourish type hint: columns  
`questions_label`| `str`, optional| Label. A column containing text (e.g. names or emoji) to write on the dots. Not recommended for datasets with more than a few hundred dots. Flourish type hint: column  
`questions_column_filter`| `str`, optional| Slider or menu. Add a time slider or menu to filter the data based on the contents of a single column. Flourish type hint: column  
`questions_id`| `str`, optional| Unique name/ID. Specify to allow animations between multiple occurrences of the same person or thing e.g. when using a time slider. Flourish type hint: column  
`questions_metadata`| `Union[list, str]`, optional| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panelsFlourish type hint: columns  
`order_categories`| `Union[list, str]`, optional| Order of answers. Use one column for each question or metric. Put the column header from the main data sheet at the top (e.g. "Do you agree?"), followed by the answers in the order you want (e.g. "disagree", "neutral", "agree"). Flourish type hint: columns  
`labels_label`| `str`, optional| Label. A column containing phrases from the main data sheet. Flourish type hint: column  
`labels_replacement`| `str`, optional| Replacement. A column containing the phrase to display. Flourish type hint: column  
`colors_question`| `str`, optional| Question. The column header (e.g. a survey question) exactly as it appears in the main data sheet. Flourish type hint: column  
`colors_answer`| `str`, optional| Answer. Use one column for each question or metric. Put the column header from the main datasheet at the top (e.g. "Do you agree?"), followed by the answers in the order you want (e.g. "disagree", "neutral", "agree"). Flourish type hint: column  
`colors_color`| `str`, optional| Color. A color name (e.g. orange, red) or code (e.g. #ff3300, #ff0000). Flourish type hint: column  
`places_latitude`| `str`, optional| Latitude. A column of latitude values. Flourish type hint: column  
`places_longitude`| `str`, optional| Longitude. A column of longitude values. Flourish type hint: column  
`places_names`| `Union[list, str]`, optional| Names. One or more columns of place names matching those in the main data sheet. Flourish type hint: columns  
`answer_groups_group`| `str`, optional| Group name. This column will contain the name of the grouped question Flourish type hint: column  
`answer_groups_question`| `str`, optional| Question. A question that matches exactly one of the questions in the datasheet. Flourish type hint: column  
`answer_groups_display_as`| `str`, optional| Display answer as. This will be the new text for the question. Flourish type hint: column  
`answer_groups_affirmative_answers`| `Union[list, str]`, optional| Answers to include. The respondent is included in the group if their answer to the question is one of the answers listed in these columns. Flourish type hint: columns  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`questions_categorical`| Categorical columns. Each of these columns appears in the Group by, Shade by and Compare dropdowns. Flourish type hint: columns  
`questions_continuous`| Continuous columns. Must contain numbers. Each of these columns appears in the Size by dropdown. Flourish type hint: columns  
`questions_geo`| Geographic columns. Must contain place names matching those specified in the Places sheet. Set to blank to disable the map mode. Flourish type hint: columns  
`questions_label`| Label. A column containing text (e.g. names or emoji) to write on the dots. Not recommended for datasets with more than a few hundred dots. Flourish type hint: column  
`questions_column_filter`| Slider or menu. Add a time slider or menu to filter the data based on the contents of a single column. Flourish type hint: column  
`questions_id`| Unique name/ID. Specify to allow animations between multiple occurrences of the same person or thing e.g. when using a time slider. Flourish type hint: column  
`questions_metadata`| Info for popups. One or more columns of information (text, image URLs, embedded charts etc) to include in popups and panelsFlourish type hint: columns  
`order_categories`| Order of answers. Use one column for each question or metric. Put the column header from the main data sheet at the top (e.g. "Do you agree?"), followed by the answers in the order you want (e.g. "disagree", "neutral", "agree"). Flourish type hint: columns  
`labels_label`| Label. A column containing phrases from the main data sheet. Flourish type hint: column  
`labels_replacement`| Replacement. A column containing the phrase to display. Flourish type hint: column  
`colors_question`| Question. The column header (e.g. a survey question) exactly as it appears in the main data sheet. Flourish type hint: column  
`colors_answer`| Answer. Use one column for each question or metric. Put the column header from the main datasheet at the top (e.g. "Do you agree?"), followed by the answers in the order you want (e.g. "disagree", "neutral", "agree"). Flourish type hint: column  
`colors_color`| Color. A color name (e.g. orange, red) or code (e.g. #ff3300, #ff0000). Flourish type hint: column  
`places_latitude`| Latitude. A column of latitude values. Flourish type hint: column  
`places_longitude`| Longitude. A column of longitude values. Flourish type hint: column  
`places_names`| Names. One or more columns of place names matching those in the main data sheet. Flourish type hint: columns  
`answer_groups_group`| Group name. This column will contain the name of the grouped question Flourish type hint: column  
`answer_groups_question`| Question. A question that matches exactly one of the questions in the datasheet. Flourish type hint: column  
`answer_groups_display_as`| Display answer as. This will be the new text for the question. Flourish type hint: column  
`answer_groups_affirmative_answers`| Answers to include. The respondent is included in the group if their answer to the question is one of the answers listed in these columns. Flourish type hint: columns
