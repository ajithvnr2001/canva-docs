---
url: https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/
title: Bind quiz data - Binding additional data sources - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:10.968159+00:00
---

# Bind quiz data - Binding additional data sources - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/

Binding additional data sources

[Bind functions](https://www.canva.dev/opensource/flourish-charts/api/bind/)[Bind audio data](https://www.canva.dev/opensource/flourish-charts/api/bind-audio-data/)[Bind bar chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-bar-chart-race-data/)[Bind bubble chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-bubble-chart-data/)[Bind calculator data](https://www.canva.dev/opensource/flourish-charts/api/bind-calculator-data/)[Bind cards data](https://www.canva.dev/opensource/flourish-charts/api/bind-cards-data/)[Bind chord diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-chord-diagram-data/)[Bind draw the line chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-draw-the-line-data/)[Bind election results chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-election-results-chart-data/)[Bind gantt chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-gantt-data/)[Bind gauge data](https://www.canva.dev/opensource/flourish-charts/api/bind-gauge-data/)[Bind hierarchy data](https://www.canva.dev/opensource/flourish-charts/api/bind-hierarchy-data/)[Bind line chart race data](https://www.canva.dev/opensource/flourish-charts/api/bind-horserace-data/)[Bind interactive svg data](https://www.canva.dev/opensource/flourish-charts/api/bind-interactive-svg-data/)[Bind line, bar and pie charts data](https://www.canva.dev/opensource/flourish-charts/api/bind-line-bar-pie-data/)[Bind marimekko data](https://www.canva.dev/opensource/flourish-charts/api/bind-marimekko-data/)[Bind network graph data](https://www.canva.dev/opensource/flourish-charts/api/bind-network-graph-data/)[Bind parliament chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-parliament-chart-data/)[Bind pictogram data](https://www.canva.dev/opensource/flourish-charts/api/bind-pictogram-data/)[Bind quiz data](https://www.canva.dev/opensource/flourish-charts/api/bind-quiz-data/)[Bind radar chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-radar-data/)[Bind sankey diagram data](https://www.canva.dev/opensource/flourish-charts/api/bind-sankey-data/)[Bind scatter data](https://www.canva.dev/opensource/flourish-charts/api/bind-scatter-data/)[Bind slope chart data](https://www.canva.dev/opensource/flourish-charts/api/bind-slope-chart-data/)[Bind sports data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-data/)[Bind sports race data](https://www.canva.dev/opensource/flourish-charts/api/bind-sports-race-data/)[Bind survey data](https://www.canva.dev/opensource/flourish-charts/api/bind-survey-data/)[Bind svg annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-svg-annotator-data/)[Bind table data](https://www.canva.dev/opensource/flourish-charts/api/bind-table-data/)[Bind text annotator data](https://www.canva.dev/opensource/flourish-charts/api/bind-text-annotator-data/)[Bind timeline data](https://www.canva.dev/opensource/flourish-charts/api/bind-timeline-data/)[Bind tournament data](https://www.canva.dev/opensource/flourish-charts/api/bind-tournament-data/)[Bind word cloud data](https://www.canva.dev/opensource/flourish-charts/api/bind-word-cloud-data/)

# Bind quiz data

Copy page

## Usage

PythonPython

RR
    
    
    def bind_quiz_data(
    
        self,
    
        questions_text: str = None,
    
        questions_explanation: str = None,
    
        questions_input_type: str = None,
    
        questions_answers: Union[list, str] = None,
    
        questions_suffix: str = None,
    
        questions_choices: str = None,
    
        scores_question: str = None,
    
        scores_range: str = None,
    
        scores_explanation: str = None,
    
        scores_media: str = None,
    
        results_range: str = None,
    
        results_text: str = None,
    
        results_media: str = None
    
        )

PYTHON

Copy
    
    
    bind_quiz_data(
    
        .,
    
        questions_text = NULL,
    
        questions_explanation = NULL,
    
        questions_input_type = NULL,
    
        questions_answers = NULL,
    
        questions_suffix = NULL,
    
        questions_choices = NULL,
    
        scores_question = NULL,
    
        scores_range = NULL,
    
        scores_explanation = NULL,
    
        scores_media = NULL,
    
        results_range = NULL,
    
        results_text = NULL,
    
        results_media = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`questions_text`| `str`, optional| Text. Question text. Flourish type hint: column  
`questions_explanation`| `str`, optional| Explanation. A short text explanation accompanying the question. Flourish type hint: column  
`questions_input_type`| `str`, optional| Input type. Type of answer input, choose between slider or multiple choice Flourish type hint: column  
`questions_answers`| `Union[list, str]`, optional| Answers. The correct answer to the question. The score will be decided by the difference between this answer and your input. Its possible to select multiple columns with answers; this will create a dropdown list above the quiz where you can select which answer to compare to. Flourish type hint: columns  
`questions_suffix`| `str`, optional| Slider input suffix. Add a suffix after the value, eg. "%" or "people" (only for slider input type). Flourish type hint: column  
`questions_choices`| `str`, optional| Multiple choice options. Options to show in multiple choice questions. Divide using "::" (eg. "Cat :: Dog :: Sheep :: Badger"). Flourish type hint: column  
`scores_question`| `str`, optional| Question. Question that the answer belongs to. Flourish type hint: column  
`scores_range`| `str`, optional| Answer. The answer to the question. This can be text for multiple choice questions. For slider answers, you can use numbers or number ranges, values could be "0-10" or "4" or "_" to select all answers. You can also add multiple rows with score ranges per question; the more specific scores will take priority (e.g. it will choose "4" over "0-10" over "_ "). Flourish type hint: column  
`scores_explanation`| `str`, optional| Text. Text to show after answering question. Flourish type hint: column  
`scores_media`| `str`, optional| Media. Picture to show after answering question. Flourish type hint: column  
`results_range`| `str`, optional| Points range. A range of points youre targeting. You can use numbers or number ranges, values could be "0-10" or "4" or "_" to select all answers. You can also add multiple rows with score ranges per question; the more specific scores will take priority (e.g. it will choose "4" over "0-10" over "_ "). Flourish type hint: column  
`results_text`| `str`, optional| Results text  
`results_media`| `str`, optional| Media. An image to show with the result. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`questions_text`| Text. Question text. Flourish type hint: column  
`questions_explanation`| Explanation. A short text explanation accompanying the question. Flourish type hint: column  
`questions_input_type`| Input type. Type of answer input, choose between slider or multiple choice Flourish type hint: column  
`questions_answers`| Answers. The correct answer to the question. The score will be decided by the difference between this answer and your input. Its possible to select multiple columns with answers; this will create a dropdown list above the quiz where you can select which answer to compare to. Flourish type hint: columns  
`questions_suffix`| Slider input suffix. Add a suffix after the value, eg. "%" or "people" (only for slider input type). Flourish type hint: column  
`questions_choices`| Multiple choice options. Options to show in multiple choice questions. Divide using "::" (eg. "Cat :: Dog :: Sheep :: Badger"). Flourish type hint: column  
`scores_question`| Question. Question that the answer belongs to. Flourish type hint: column  
`scores_range`| Answer. The answer to the question. This can be text for multiple choice questions. For slider answers, you can use numbers or number ranges, values could be "0-10" or "4" or "_" to select all answers. You can also add multiple rows with score ranges per question; the more specific scores will take priority (e.g. it will choose "4" over "0-10" over "_ "). Flourish type hint: column  
`scores_explanation`| Text. Text to show after answering question. Flourish type hint: column  
`scores_media`| Media. Picture to show after answering question. Flourish type hint: column  
`results_range`| Points range. A range of points youre targeting. You can use numbers or number ranges, values could be "0-10" or "4" or "_" to select all answers. You can also add multiple rows with score ranges per question; the more specific scores will take priority (e.g. it will choose "4" over "0-10" over "_ "). Flourish type hint: column  
`results_text`| Results text  
`results_media`| Media. An image to show with the result. Add an image URL or right-click on a cell to upload an image. Flourish type hint: column
