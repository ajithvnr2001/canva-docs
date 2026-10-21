---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/
title: Bind calculator data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:09.362399+00:00
---

# Bind calculator data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind calculator data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_calculator_data(
    
        self,
    
        question_text: str = None,
    
        question_type: str = None,
    
        context_text: str = None,
    
        image: str = None,
    
        answers_raw: str = None,
    
        fallback_value: str = None
    
        )

PYTHON

Copy
    
    
    bind_calculator_data(
    
        .,
    
        question_text = NULL,
    
        question_type = NULL,
    
        context_text = NULL,
    
        image = NULL,
    
        answers_raw = NULL,
    
        fallback_value = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`question_text`| `str`, optional| Question text. The question text. Flourish type hint: column  
`question_type`| `str`, optional| Question type. The type of question. Choose from number input, text input, single response buttons, multi response buttons, dropdown, single date picker, range date picker, multi date picker, rating, single slider or range slider. Leave empty to just display text. Flourish type hint: column  
`context_text`| `str`, optional| Question context. Additional information. Flourish type hint: column  
`image`| `str`, optional| Image. Question background image. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column  
`answers_raw`| `str`, optional| Answers. Answer values separated by "::". Required for single and multi-response buttons, dropdown and rating questions. Rating answers can take optional labels per value noted as "Value >> Label" - for example, "1 >> Bad :: 2 :: 3 >> Good". Number inputs can take range specifications in the format "min: 0 :: max: 50 :: step: 2". Slider inputs can take slider specifications in the format "min: 0 :: max: 100 :: value: 10". Use two comma separated values for range sliders, eg.: "value: 1, 100". See the templates documentation for additional info. Flourish type hint: column  
`fallback_value`| `str`, optional| Fallback value. Fallback value to fill the answer input if left empty by the user. Works for all question types but sliders, which will always show the initial value. Flourish type hint: column  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`question_text`| Question text. The question text. Flourish type hint: column  
`question_type`| Question type. The type of question. Choose from number input, text input, single response buttons, multi response buttons, dropdown, single date picker, range date picker, multi date picker, rating, single slider or range slider. Leave empty to just display text. Flourish type hint: column  
`context_text`| Question context. Additional information. Flourish type hint: column  
`image`| Image. Question background image. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column  
`answers_raw`| Answers. Answer values separated by "::". Required for single and multi-response buttons, dropdown and rating questions. Rating answers can take optional labels per value noted as "Value >> Label" - for example, "1 >> Bad :: 2 :: 3 >> Good". Number inputs can take range specifications in the format "min: 0 :: max: 50 :: step: 2". Slider inputs can take slider specifications in the format "min: 0 :: max: 100 :: value: 10". Use two comma separated values for range sliders, eg.: "value: 1, 100". See the templates documentation for additional info. Flourish type hint: column  
`fallback_value`| Fallback value. Fallback value to fill the answer input if left empty by the user. Works for all question types but sliders, which will always show the initial value. Flourish type hint: column
