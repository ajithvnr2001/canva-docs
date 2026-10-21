---
url: https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/
title: Set calculator chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:20.986464+00:00
---

# Set calculator chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set calculator chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_calculator_details(
    
        self,
    
        question_flow: str = None,
    
        design_border_type: str = None,
    
        design_border_color: str = None,
    
        design_background: str = None,
    
        design_advanced: bool = None,
    
        design_align_horizontal: str = None,
    
        design_align_vertical: str = None,
    
        design_max_width: float = None,
    
        design_margin_vertical: float = None,
    
        design_padding_vertical: float = None,
    
        design_padding_horizontal: float = None,
    
        design_border_width: float = None,
    
        design_border_style: str = None,
    
        design_border_radius: float = None,
    
        design_shadow: bool = None,
    
        design_shadow_color: str = None,
    
        result_variables: Union[list, str] = None,
    
        result_input: Union[list, str] = None,
    
        result_advanced: bool = None,
    
        result_font_size: str = None,
    
        result_font_size_custom: float = None,
    
        result_font_color: str = None,
    
        result_font_weight: str = None,
    
        result_font_style: str = None,
    
        result_border_type: str = None,
    
        result_border_width: float = None,
    
        result_border_style: str = None,
    
        result_border_color: str = None,
    
        result_bg_type: str = None,
    
        result_bg_color: str = None,
    
        result_bg_image_src: str = None,
    
        result_bg_image_size: str = None,
    
        design_question_font_size: str = None,
    
        design_question_font_size_custom: float = None,
    
        design_question_font_color: str = None,
    
        design_question_font_weight: str = None,
    
        design_question_font_style: str = None,
    
        design_question_margin_vertical: float = None,
    
        design_question_margin_horizontal: float = None,
    
        design_question_padding: float = None,
    
        design_context_font_size: str = None,
    
        design_context_font_size_custom: float = None,
    
        design_context_font_color: str = None,
    
        design_context_font_weight: str = None,
    
        design_context_font_style: str = None,
    
        design_context_margin_vertical: float = None,
    
        design_context_margin_horizontal: float = None,
    
        design_question_bg_color: str = None,
    
        design_question_bg_opacity: float = None,
    
        design_question_border_radius: float = None,
    
        design_answer_margin_vertical: float = None,
    
        design_answer_margin_horizontal: float = None,
    
        input_color: str = None,
    
        input_background_color: str = None,
    
        input_width: float = None,
    
        number_input_placeholder: str = None,
    
        text_input_placeholder: str = None,
    
        input_input_advanced: bool = None,
    
        input_border_color: str = None,
    
        input_border_radius: float = None,
    
        input_border_width: float = None,
    
        input_border_style: str = None,
    
        input_align: str = None,
    
        input_margin: float = None,
    
        input_padding: float = None,
    
        button_font_size: str = None,
    
        button_font_size_custom: float = None,
    
        chart_button_control_style_background: str = None,
    
        chart_button_control_style_background_selected: str = None,
    
        chart_button_control_style_background_hover: str = None,
    
        chart_button_control_style_font_color: str = None,
    
        chart_button_control_style_font_color_selected: str = None,
    
        chart_button_control_style_font_color_hover: str = None,
    
        chart_button_control_style_button_styles_advanced: bool = None,
    
        chart_button_control_style_border_width: float = None,
    
        chart_button_control_style_border_color: str = None,
    
        chart_button_control_style_border_transparency: float = None,
    
        chart_button_control_style_border_radius: float = None,
    
        button_border_style: str = None,
    
        button_container_width: float = None,
    
        button_justify_content: str = None,
    
        button_margin: float = None,
    
        button_padding_factor: float = None,
    
        dropdown_font_size: str = None,
    
        dropdown_font_size_custom: float = None,
    
        dropdown_placeholder: str = None,
    
        chart_dropdown_control_style_background: str = None,
    
        chart_dropdown_control_style_font_color: str = None,
    
        chart_dropdown_control_style_border_styles_advanced: bool = None,
    
        chart_dropdown_control_style_border_style: str = None,
    
        chart_dropdown_control_style_border_width: float = None,
    
        chart_dropdown_control_style_border_color: str = None,
    
        chart_dropdown_control_style_border_transparency: float = None,
    
        chart_dropdown_control_style_border_radius: float = None,
    
        dropdown_padding_factor: float = None,
    
        dropdown_border_style: str = None,
    
        dropdown_font_weight: str = None,
    
        dropdown_font_style: str = None,
    
        dropdown_shadow: bool = None,
    
        dropdown_shadow_color: str = None,
    
        date_format: str = None,
    
        date_input_placeholder: str = None,
    
        date_advanced: bool = None,
    
        date_width: float = None,
    
        date_margin: float = None,
    
        date_padding: float = None,
    
        date_border_width: float = None,
    
        date_border_style: str = None,
    
        date_border_color: str = None,
    
        date_border_radius: float = None,
    
        date_align: str = None,
    
        date_calendar_position_vertical: str = None,
    
        date_calendar_position_horizontal: str = None,
    
        rating_icon_type: str = None,
    
        rating_icon_fill_base: str = None,
    
        rating_icon_stroke_base: str = None,
    
        rating_icon_fill_active: str = None,
    
        rating_icon_stroke_active: str = None,
    
        rating_advanced: bool = None,
    
        rating_icon_width: float = None,
    
        rating_icon_height: float = None,
    
        rating_icon_margin: float = None,
    
        rating_icon_stroke_width: float = None,
    
        rating_container_width: float = None,
    
        rating_wrap_margin_vertical: float = None,
    
        rating_wrap_margin_horizontal: float = None,
    
        rating_wrap_padding_vertical: float = None,
    
        rating_wrap_padding_horizontal: float = None,
    
        rating_label_width: float = None,
    
        rating_label_color: str = None,
    
        rating_label_position: str = None,
    
        chart_slider_filter_controls_handle_color: str = None,
    
        chart_slider_filter_controls_track_active_color: str = None,
    
        chart_slider_filter_controls_track_base_color: str = None,
    
        chart_slider_filter_controls_handle_size: float = None,
    
        chart_slider_filter_controls_ticks: bool = None,
    
        chart_slider_filter_controls_advanced: bool = None,
    
        chart_slider_filter_controls_container_width: float = None,
    
        chart_slider_filter_controls_wrap_margin_vertical: float = None,
    
        chart_slider_filter_controls_wrap_margin_horizontal: float = None,
    
        chart_slider_filter_controls_track_height: float = None,
    
        chart_slider_filter_controls_track_border_radius: float = None,
    
        chart_slider_filter_controls_track_border_color: str = None,
    
        chart_slider_filter_controls_track_border_width: float = None,
    
        chart_slider_filter_controls_handle_shape: str = None,
    
        chart_slider_filter_controls_handle_width: float = None,
    
        chart_slider_filter_controls_handle_border_color: str = None,
    
        chart_slider_filter_controls_handle_border_width: float = None,
    
        chart_slider_filter_controls_handle_border_radius: float = None,
    
        chart_slider_filter_controls_handle_box_shadow: bool = None,
    
        chart_slider_filter_controls_tooltips: bool = None,
    
        chart_slider_filter_controls_tooltip_background: bool = None,
    
        chart_slider_filter_controls_tick_color: str = None,
    
        chart_slider_filter_controls_tick_padding: float = None,
    
        chart_slider_filter_controls_tick_number_padding: float = None,
    
        submit_comment_text: Union[list, str] = None,
    
        submit_button_text: str = None,
    
        submit_bg_type: str = None,
    
        submit_bg_color: str = None,
    
        submit_bg_image_src: str = None,
    
        submit_border: bool = None,
    
        submit_bg_image_size: str = None,
    
        submit_advanced: bool = None,
    
        submit_comment_font_size: str = None,
    
        submit_comment_font_size_custom: float = None,
    
        submit_comment_font_weight: str = None,
    
        submit_comment_font_style: str = None,
    
        submit_flex_direction: str = None,
    
        submit_comment_font_color: str = None,
    
        submit_comment_margin: float = None,
    
        submit_button_font_size: str = None,
    
        submit_button_font_size_custom: float = None,
    
        submit_button_font_weight: str = None,
    
        submit_button_font_style: str = None,
    
        submit_button_margin: float = None,
    
        submit_button_padding_factor: float = None,
    
        submit_button_box_shadow: bool = None,
    
        submit_button_use_default_styles: bool = None,
    
        submit_button_bg_color: str = None,
    
        submit_button_bg_color_hover: str = None,
    
        submit_button_font_color: str = None,
    
        submit_button_font_color_hover: str = None,
    
        submit_button_border_style: str = None,
    
        submit_button_border_color: str = None,
    
        submit_button_border_width: float = None,
    
        submit_button_border_transparency: float = None,
    
        submit_button_border_radius: float = None,
    
        design_controls_position: str = None,
    
        design_controls_button_symbol_back: str = None,
    
        design_controls_button_symbol_forward: str = None,
    
        design_controls_button_font_color: str = None,
    
        design_controls_button_font_size: float = None,
    
        design_controls_advanced: bool = None,
    
        design_controls_button_margin: float = None,
    
        design_controls_button_padding_factor: float = None,
    
        design_controls_button_bg_color: str = None,
    
        design_controls_button_bg_opacity: float = None,
    
        design_controls_button_font_weight: str = None,
    
        design_controls_button_font_style: str = None,
    
        design_controls_button_border_width: float = None,
    
        design_controls_button_border_style: str = None,
    
        design_controls_button_border_color: str = None,
    
        design_controls_button_border_radius: float = None,
    
        design_progress_show: bool = None,
    
        design_progress_position: str = None,
    
        design_progress_height: float = None,
    
        design_progress_margin: float = None,
    
        design_progress_bg_color: str = None,
    
        design_progress_bg_opacity: float = None,
    
        chart_number_date_format_prefix: str = None,
    
        chart_number_date_format_suffix: str = None,
    
        chart_number_date_format_n_dec: float = None,
    
        chart_number_date_format_advanced: bool = None,
    
        chart_number_date_format_negative_sign: str = None,
    
        chart_number_date_format_strip_zeros: bool = None,
    
        chart_number_date_format_strip_separator: bool = None,
    
        chart_number_date_format_transform_labels: bool = None,
    
        chart_number_date_format_transform: str = None,
    
        chart_number_date_format_multiply_divide_constant: float = None,
    
        chart_number_date_format_exponentiate_constant: float = None,
    
        chart_number_localization_input_decimal_separator: str = None,
    
        chart_number_localization_output_separators: str = None,
    
        external_write_enabled: bool = None,
    
        external_write_endpoint: str = None,
    
        chart_layout_body_font: str = None,
    
        chart_layout_font_color: str = None,
    
        chart_layout_background_color_enabled: bool = None,
    
        chart_layout_background_image_enabled: bool = None,
    
        chart_layout_background_color: str = None,
    
        chart_layout_background_image_src: str = None,
    
        chart_layout_background_image_size: str = None,
    
        chart_layout_background_image_position: str = None,
    
        chart_layout_max_width_target: str = None,
    
        chart_layout_max_width: float = None,
    
        chart_layout_max_width_align: str = None,
    
        chart_layout_layout_order: str = None,
    
        chart_layout_space_between_sections: str = None,
    
        chart_layout_space_between_sections_custom: float = None,
    
        chart_layout_margin_top: float = None,
    
        chart_layout_margin_right: float = None,
    
        chart_layout_margin_bottom: float = None,
    
        chart_layout_margin_left: float = None,
    
        chart_layout_border_enabled: bool = None,
    
        chart_layout_border_top_width: float = None,
    
        chart_layout_border_top_style: str = None,
    
        chart_layout_border_top_color: str = None,
    
        chart_layout_border_right_width: float = None,
    
        chart_layout_border_right_style: str = None,
    
        chart_layout_border_right_color: str = None,
    
        chart_layout_border_bottom_width: float = None,
    
        chart_layout_border_bottom_style: str = None,
    
        chart_layout_border_bottom_color: str = None,
    
        chart_layout_border_left_width: float = None,
    
        chart_layout_border_left_style: str = None,
    
        chart_layout_border_left_color: str = None,
    
        chart_layout_read_direction: str = None,
    
        chart_layout_font_size_mobile_small: float = None,
    
        chart_layout_font_size_mobile_big: float = None,
    
        chart_layout_font_size_tablet: float = None,
    
        chart_layout_font_size_desktop: float = None,
    
        chart_layout_font_size_big_screen: float = None,
    
        chart_layout_breakpoint_mobile_small: float = None,
    
        chart_layout_breakpoint_mobile_big: float = None,
    
        chart_layout_breakpoint_tablet: float = None,
    
        chart_layout_breakpoint_desktop: float = None,
    
        chart_layout_breakpoint_big_screen: float = None,
    
        chart_layout_header_align: str = None,
    
        chart_layout_title: Union[list, str] = None,
    
        chart_layout_title_styling: bool = None,
    
        chart_layout_title_font: str = None,
    
        chart_layout_title_size: str = None,
    
        chart_layout_title_size_custom: float = None,
    
        chart_layout_title_weight: str = None,
    
        chart_layout_title_color: str = None,
    
        chart_layout_title_line_height: float = None,
    
        chart_layout_title_space_above: str = None,
    
        chart_layout_title_space_above_custom: float = None,
    
        chart_layout_subtitle: Union[list, str] = None,
    
        chart_layout_subtitle_styling: bool = None,
    
        chart_layout_subtitle_font: str = None,
    
        chart_layout_subtitle_size: str = None,
    
        chart_layout_subtitle_size_custom: float = None,
    
        chart_layout_subtitle_weight: str = None,
    
        chart_layout_subtitle_color: str = None,
    
        chart_layout_subtitle_line_height: float = None,
    
        chart_layout_subtitle_space_above: str = None,
    
        chart_layout_subtitle_space_above_custom: float = None,
    
        chart_layout_header_text: Union[list, str] = None,
    
        chart_layout_header_text_styling: bool = None,
    
        chart_layout_header_text_size: str = None,
    
        chart_layout_header_text_size_custom: float = None,
    
        chart_layout_header_text_weight: str = None,
    
        chart_layout_header_text_color: str = None,
    
        chart_layout_header_text_line_height: float = None,
    
        chart_layout_header_text_space_above: str = None,
    
        chart_layout_header_text_space_above_custom: float = None,
    
        chart_layout_header_border: str = None,
    
        chart_layout_header_border_width: float = None,
    
        chart_layout_header_border_color: str = None,
    
        chart_layout_header_border_style: str = None,
    
        chart_layout_header_border_space: float = None,
    
        chart_layout_header_logo_enabled: bool = None,
    
        chart_layout_header_logo_src: str = None,
    
        chart_layout_header_logo_alt: str = None,
    
        chart_layout_header_logo_link_url: str = None,
    
        chart_layout_header_logo_height: float = None,
    
        chart_layout_header_logo_align: str = None,
    
        chart_layout_header_logo_position_inside: str = None,
    
        chart_layout_header_logo_position_outside: str = None,
    
        chart_layout_header_logo_margin_top: float = None,
    
        chart_layout_header_logo_margin_right: float = None,
    
        chart_layout_header_logo_margin_bottom: float = None,
    
        chart_layout_header_logo_margin_left: float = None,
    
        chart_layout_footer_align: str = None,
    
        chart_layout_footer_text_size: float = None,
    
        chart_layout_footer_text_color: str = None,
    
        chart_layout_footer_styling: bool = None,
    
        chart_layout_footer_font: str = None,
    
        chart_layout_footer_text_weight: str = None,
    
        chart_layout_source_name: str = None,
    
        chart_layout_source_url: str = None,
    
        chart_layout_multiple_sources: bool = None,
    
        chart_layout_source_name_2: str = None,
    
        chart_layout_source_url_2: str = None,
    
        chart_layout_source_name_3: str = None,
    
        chart_layout_source_url_3: str = None,
    
        chart_layout_source_label: str = None,
    
        chart_layout_footer_note: Union[list, str] = None,
    
        chart_layout_footer_note_secondary: Union[list, str] = None,
    
        chart_layout_advanced_note_styling: bool = None,
    
        chart_layout_footer_timestamp_format: str = None,
    
        chart_layout_footer_logo_enabled: bool = None,
    
        chart_layout_footer_logo_src: str = None,
    
        chart_layout_footer_logo_src_light: str = None,
    
        chart_layout_footer_logo_alt: str = None,
    
        chart_layout_footer_logo_link_url: str = None,
    
        chart_layout_footer_logo_height: float = None,
    
        chart_layout_footer_logo_margin: float = None,
    
        chart_layout_footer_logo_order: str = None,
    
        chart_layout_footer_align_vertical: str = None,
    
        chart_layout_footer_border: str = None,
    
        chart_layout_footer_border_width: float = None,
    
        chart_layout_footer_border_color: str = None,
    
        chart_layout_footer_border_style: str = None,
    
        chart_layout_footer_border_space: float = None,
    
        chart_layout_screenreader_text_primary: Union[list, str] = None,
    
        chart_layout_screenreader_label: str = None,
    
        chart_layout_screenreader_hide_primary: bool = None
    
        )

PYTHON

Copy
    
    
    set_calculator_details(
    
        .,
    
        question_flow = NULL,
    
        design_border_type = NULL,
    
        design_border_color = NULL,
    
        design_background = NULL,
    
        design_advanced = NULL,
    
        design_align_horizontal = NULL,
    
        design_align_vertical = NULL,
    
        design_max_width = NULL,
    
        design_margin_vertical = NULL,
    
        design_padding_vertical = NULL,
    
        design_padding_horizontal = NULL,
    
        design_border_width = NULL,
    
        design_border_style = NULL,
    
        design_border_radius = NULL,
    
        design_shadow = NULL,
    
        design_shadow_color = NULL,
    
        result_variables = NULL,
    
        result_input = NULL,
    
        result_advanced = NULL,
    
        result_font_size = NULL,
    
        result_font_size_custom = NULL,
    
        result_font_color = NULL,
    
        result_font_weight = NULL,
    
        result_font_style = NULL,
    
        result_border_type = NULL,
    
        result_border_width = NULL,
    
        result_border_style = NULL,
    
        result_border_color = NULL,
    
        result_bg_type = NULL,
    
        result_bg_color = NULL,
    
        result_bg_image_src = NULL,
    
        result_bg_image_size = NULL,
    
        design_question_font_size = NULL,
    
        design_question_font_size_custom = NULL,
    
        design_question_font_color = NULL,
    
        design_question_font_weight = NULL,
    
        design_question_font_style = NULL,
    
        design_question_margin_vertical = NULL,
    
        design_question_margin_horizontal = NULL,
    
        design_question_padding = NULL,
    
        design_context_font_size = NULL,
    
        design_context_font_size_custom = NULL,
    
        design_context_font_color = NULL,
    
        design_context_font_weight = NULL,
    
        design_context_font_style = NULL,
    
        design_context_margin_vertical = NULL,
    
        design_context_margin_horizontal = NULL,
    
        design_question_bg_color = NULL,
    
        design_question_bg_opacity = NULL,
    
        design_question_border_radius = NULL,
    
        design_answer_margin_vertical = NULL,
    
        design_answer_margin_horizontal = NULL,
    
        input_color = NULL,
    
        input_background_color = NULL,
    
        input_width = NULL,
    
        number_input_placeholder = NULL,
    
        text_input_placeholder = NULL,
    
        input_input_advanced = NULL,
    
        input_border_color = NULL,
    
        input_border_radius = NULL,
    
        input_border_width = NULL,
    
        input_border_style = NULL,
    
        input_align = NULL,
    
        input_margin = NULL,
    
        input_padding = NULL,
    
        button_font_size = NULL,
    
        button_font_size_custom = NULL,
    
        chart_button_control_style_background = NULL,
    
        chart_button_control_style_background_selected = NULL,
    
        chart_button_control_style_background_hover = NULL,
    
        chart_button_control_style_font_color = NULL,
    
        chart_button_control_style_font_color_selected = NULL,
    
        chart_button_control_style_font_color_hover = NULL,
    
        chart_button_control_style_button_styles_advanced = NULL,
    
        chart_button_control_style_border_width = NULL,
    
        chart_button_control_style_border_color = NULL,
    
        chart_button_control_style_border_transparency = NULL,
    
        chart_button_control_style_border_radius = NULL,
    
        button_border_style = NULL,
    
        button_container_width = NULL,
    
        button_justify_content = NULL,
    
        button_margin = NULL,
    
        button_padding_factor = NULL,
    
        dropdown_font_size = NULL,
    
        dropdown_font_size_custom = NULL,
    
        dropdown_placeholder = NULL,
    
        chart_dropdown_control_style_background = NULL,
    
        chart_dropdown_control_style_font_color = NULL,
    
        chart_dropdown_control_style_border_styles_advanced = NULL,
    
        chart_dropdown_control_style_border_style = NULL,
    
        chart_dropdown_control_style_border_width = NULL,
    
        chart_dropdown_control_style_border_color = NULL,
    
        chart_dropdown_control_style_border_transparency = NULL,
    
        chart_dropdown_control_style_border_radius = NULL,
    
        dropdown_padding_factor = NULL,
    
        dropdown_border_style = NULL,
    
        dropdown_font_weight = NULL,
    
        dropdown_font_style = NULL,
    
        dropdown_shadow = NULL,
    
        dropdown_shadow_color = NULL,
    
        date_format = NULL,
    
        date_input_placeholder = NULL,
    
        date_advanced = NULL,
    
        date_width = NULL,
    
        date_margin = NULL,
    
        date_padding = NULL,
    
        date_border_width = NULL,
    
        date_border_style = NULL,
    
        date_border_color = NULL,
    
        date_border_radius = NULL,
    
        date_align = NULL,
    
        date_calendar_position_vertical = NULL,
    
        date_calendar_position_horizontal = NULL,
    
        rating_icon_type = NULL,
    
        rating_icon_fill_base = NULL,
    
        rating_icon_stroke_base = NULL,
    
        rating_icon_fill_active = NULL,
    
        rating_icon_stroke_active = NULL,
    
        rating_advanced = NULL,
    
        rating_icon_width = NULL,
    
        rating_icon_height = NULL,
    
        rating_icon_margin = NULL,
    
        rating_icon_stroke_width = NULL,
    
        rating_container_width = NULL,
    
        rating_wrap_margin_vertical = NULL,
    
        rating_wrap_margin_horizontal = NULL,
    
        rating_wrap_padding_vertical = NULL,
    
        rating_wrap_padding_horizontal = NULL,
    
        rating_label_width = NULL,
    
        rating_label_color = NULL,
    
        rating_label_position = NULL,
    
        chart_slider_filter_controls_handle_color = NULL,
    
        chart_slider_filter_controls_track_active_color = NULL,
    
        chart_slider_filter_controls_track_base_color = NULL,
    
        chart_slider_filter_controls_handle_size = NULL,
    
        chart_slider_filter_controls_ticks = NULL,
    
        chart_slider_filter_controls_advanced = NULL,
    
        chart_slider_filter_controls_container_width = NULL,
    
        chart_slider_filter_controls_wrap_margin_vertical = NULL,
    
        chart_slider_filter_controls_wrap_margin_horizontal = NULL,
    
        chart_slider_filter_controls_track_height = NULL,
    
        chart_slider_filter_controls_track_border_radius = NULL,
    
        chart_slider_filter_controls_track_border_color = NULL,
    
        chart_slider_filter_controls_track_border_width = NULL,
    
        chart_slider_filter_controls_handle_shape = NULL,
    
        chart_slider_filter_controls_handle_width = NULL,
    
        chart_slider_filter_controls_handle_border_color = NULL,
    
        chart_slider_filter_controls_handle_border_width = NULL,
    
        chart_slider_filter_controls_handle_border_radius = NULL,
    
        chart_slider_filter_controls_handle_box_shadow = NULL,
    
        chart_slider_filter_controls_tooltips = NULL,
    
        chart_slider_filter_controls_tooltip_background = NULL,
    
        chart_slider_filter_controls_tick_color = NULL,
    
        chart_slider_filter_controls_tick_padding = NULL,
    
        chart_slider_filter_controls_tick_number_padding = NULL,
    
        submit_comment_text = NULL,
    
        submit_button_text = NULL,
    
        submit_bg_type = NULL,
    
        submit_bg_color = NULL,
    
        submit_bg_image_src = NULL,
    
        submit_border = NULL,
    
        submit_bg_image_size = NULL,
    
        submit_advanced = NULL,
    
        submit_comment_font_size = NULL,
    
        submit_comment_font_size_custom = NULL,
    
        submit_comment_font_weight = NULL,
    
        submit_comment_font_style = NULL,
    
        submit_flex_direction = NULL,
    
        submit_comment_font_color = NULL,
    
        submit_comment_margin = NULL,
    
        submit_button_font_size = NULL,
    
        submit_button_font_size_custom = NULL,
    
        submit_button_font_weight = NULL,
    
        submit_button_font_style = NULL,
    
        submit_button_margin = NULL,
    
        submit_button_padding_factor = NULL,
    
        submit_button_box_shadow = NULL,
    
        submit_button_use_default_styles = NULL,
    
        submit_button_bg_color = NULL,
    
        submit_button_bg_color_hover = NULL,
    
        submit_button_font_color = NULL,
    
        submit_button_font_color_hover = NULL,
    
        submit_button_border_style = NULL,
    
        submit_button_border_color = NULL,
    
        submit_button_border_width = NULL,
    
        submit_button_border_transparency = NULL,
    
        submit_button_border_radius = NULL,
    
        design_controls_position = NULL,
    
        design_controls_button_symbol_back = NULL,
    
        design_controls_button_symbol_forward = NULL,
    
        design_controls_button_font_color = NULL,
    
        design_controls_button_font_size = NULL,
    
        design_controls_advanced = NULL,
    
        design_controls_button_margin = NULL,
    
        design_controls_button_padding_factor = NULL,
    
        design_controls_button_bg_color = NULL,
    
        design_controls_button_bg_opacity = NULL,
    
        design_controls_button_font_weight = NULL,
    
        design_controls_button_font_style = NULL,
    
        design_controls_button_border_width = NULL,
    
        design_controls_button_border_style = NULL,
    
        design_controls_button_border_color = NULL,
    
        design_controls_button_border_radius = NULL,
    
        design_progress_show = NULL,
    
        design_progress_position = NULL,
    
        design_progress_height = NULL,
    
        design_progress_margin = NULL,
    
        design_progress_bg_color = NULL,
    
        design_progress_bg_opacity = NULL,
    
        chart_number_date_format_prefix = NULL,
    
        chart_number_date_format_suffix = NULL,
    
        chart_number_date_format_n_dec = NULL,
    
        chart_number_date_format_advanced = NULL,
    
        chart_number_date_format_negative_sign = NULL,
    
        chart_number_date_format_strip_zeros = NULL,
    
        chart_number_date_format_strip_separator = NULL,
    
        chart_number_date_format_transform_labels = NULL,
    
        chart_number_date_format_transform = NULL,
    
        chart_number_date_format_multiply_divide_constant = NULL,
    
        chart_number_date_format_exponentiate_constant = NULL,
    
        chart_number_localization_input_decimal_separator = NULL,
    
        chart_number_localization_output_separators = NULL,
    
        external_write_enabled = NULL,
    
        external_write_endpoint = NULL,
    
        chart_layout_body_font = NULL,
    
        chart_layout_font_color = NULL,
    
        chart_layout_background_color_enabled = NULL,
    
        chart_layout_background_image_enabled = NULL,
    
        chart_layout_background_color = NULL,
    
        chart_layout_background_image_src = NULL,
    
        chart_layout_background_image_size = NULL,
    
        chart_layout_background_image_position = NULL,
    
        chart_layout_max_width_target = NULL,
    
        chart_layout_max_width = NULL,
    
        chart_layout_max_width_align = NULL,
    
        chart_layout_layout_order = NULL,
    
        chart_layout_space_between_sections = NULL,
    
        chart_layout_space_between_sections_custom = NULL,
    
        chart_layout_margin_top = NULL,
    
        chart_layout_margin_right = NULL,
    
        chart_layout_margin_bottom = NULL,
    
        chart_layout_margin_left = NULL,
    
        chart_layout_border_enabled = NULL,
    
        chart_layout_border_top_width = NULL,
    
        chart_layout_border_top_style = NULL,
    
        chart_layout_border_top_color = NULL,
    
        chart_layout_border_right_width = NULL,
    
        chart_layout_border_right_style = NULL,
    
        chart_layout_border_right_color = NULL,
    
        chart_layout_border_bottom_width = NULL,
    
        chart_layout_border_bottom_style = NULL,
    
        chart_layout_border_bottom_color = NULL,
    
        chart_layout_border_left_width = NULL,
    
        chart_layout_border_left_style = NULL,
    
        chart_layout_border_left_color = NULL,
    
        chart_layout_read_direction = NULL,
    
        chart_layout_font_size_mobile_small = NULL,
    
        chart_layout_font_size_mobile_big = NULL,
    
        chart_layout_font_size_tablet = NULL,
    
        chart_layout_font_size_desktop = NULL,
    
        chart_layout_font_size_big_screen = NULL,
    
        chart_layout_breakpoint_mobile_small = NULL,
    
        chart_layout_breakpoint_mobile_big = NULL,
    
        chart_layout_breakpoint_tablet = NULL,
    
        chart_layout_breakpoint_desktop = NULL,
    
        chart_layout_breakpoint_big_screen = NULL,
    
        chart_layout_header_align = NULL,
    
        chart_layout_title = NULL,
    
        chart_layout_title_styling = NULL,
    
        chart_layout_title_font = NULL,
    
        chart_layout_title_size = NULL,
    
        chart_layout_title_size_custom = NULL,
    
        chart_layout_title_weight = NULL,
    
        chart_layout_title_color = NULL,
    
        chart_layout_title_line_height = NULL,
    
        chart_layout_title_space_above = NULL,
    
        chart_layout_title_space_above_custom = NULL,
    
        chart_layout_subtitle = NULL,
    
        chart_layout_subtitle_styling = NULL,
    
        chart_layout_subtitle_font = NULL,
    
        chart_layout_subtitle_size = NULL,
    
        chart_layout_subtitle_size_custom = NULL,
    
        chart_layout_subtitle_weight = NULL,
    
        chart_layout_subtitle_color = NULL,
    
        chart_layout_subtitle_line_height = NULL,
    
        chart_layout_subtitle_space_above = NULL,
    
        chart_layout_subtitle_space_above_custom = NULL,
    
        chart_layout_header_text = NULL,
    
        chart_layout_header_text_styling = NULL,
    
        chart_layout_header_text_size = NULL,
    
        chart_layout_header_text_size_custom = NULL,
    
        chart_layout_header_text_weight = NULL,
    
        chart_layout_header_text_color = NULL,
    
        chart_layout_header_text_line_height = NULL,
    
        chart_layout_header_text_space_above = NULL,
    
        chart_layout_header_text_space_above_custom = NULL,
    
        chart_layout_header_border = NULL,
    
        chart_layout_header_border_width = NULL,
    
        chart_layout_header_border_color = NULL,
    
        chart_layout_header_border_style = NULL,
    
        chart_layout_header_border_space = NULL,
    
        chart_layout_header_logo_enabled = NULL,
    
        chart_layout_header_logo_src = NULL,
    
        chart_layout_header_logo_alt = NULL,
    
        chart_layout_header_logo_link_url = NULL,
    
        chart_layout_header_logo_height = NULL,
    
        chart_layout_header_logo_align = NULL,
    
        chart_layout_header_logo_position_inside = NULL,
    
        chart_layout_header_logo_position_outside = NULL,
    
        chart_layout_header_logo_margin_top = NULL,
    
        chart_layout_header_logo_margin_right = NULL,
    
        chart_layout_header_logo_margin_bottom = NULL,
    
        chart_layout_header_logo_margin_left = NULL,
    
        chart_layout_footer_align = NULL,
    
        chart_layout_footer_text_size = NULL,
    
        chart_layout_footer_text_color = NULL,
    
        chart_layout_footer_styling = NULL,
    
        chart_layout_footer_font = NULL,
    
        chart_layout_footer_text_weight = NULL,
    
        chart_layout_source_name = NULL,
    
        chart_layout_source_url = NULL,
    
        chart_layout_multiple_sources = NULL,
    
        chart_layout_source_name_2 = NULL,
    
        chart_layout_source_url_2 = NULL,
    
        chart_layout_source_name_3 = NULL,
    
        chart_layout_source_url_3 = NULL,
    
        chart_layout_source_label = NULL,
    
        chart_layout_footer_note = NULL,
    
        chart_layout_footer_note_secondary = NULL,
    
        chart_layout_advanced_note_styling = NULL,
    
        chart_layout_footer_timestamp_format = NULL,
    
        chart_layout_footer_logo_enabled = NULL,
    
        chart_layout_footer_logo_src = NULL,
    
        chart_layout_footer_logo_src_light = NULL,
    
        chart_layout_footer_logo_alt = NULL,
    
        chart_layout_footer_logo_link_url = NULL,
    
        chart_layout_footer_logo_height = NULL,
    
        chart_layout_footer_logo_margin = NULL,
    
        chart_layout_footer_logo_order = NULL,
    
        chart_layout_footer_align_vertical = NULL,
    
        chart_layout_footer_border = NULL,
    
        chart_layout_footer_border_width = NULL,
    
        chart_layout_footer_border_color = NULL,
    
        chart_layout_footer_border_style = NULL,
    
        chart_layout_footer_border_space = NULL,
    
        chart_layout_screenreader_text_primary = NULL,
    
        chart_layout_screenreader_label = NULL,
    
        chart_layout_screenreader_hide_primary = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`question_flow`| `str`, optional| Question flow. Choices: vertical, horizontal. Flourish type hint: string, defaults to None  
`design_border_type`| `str`, optional| Border. Choices: border-bottom, border. Flourish type hint: string, defaults to None  
`design_border_color`| `str`, optional| Border color. Flourish type hint: color, defaults to None  
`design_background`| `str`, optional| Background. The background color of the cards. If not set, the background color in Layout is used. Flourish type hint: color, defaults to None  
`design_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`design_align_horizontal`| `str`, optional| Align. Choices: start, center, end. Flourish type hint: string, defaults to None  
`design_align_vertical`| `str`, optional| Position. Choices: start, center, flex-end. Set the vertical text position if the window height is fixed and the text doesnt stretch across the full vertical card space. Flourish type hint: string, defaults to None  
`design_max_width`| `float`, optional| Max width (%). Flourish type hint: number, defaults to None  
`design_margin_vertical`| `float`, optional| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_padding_vertical`| `float`, optional| Vertical padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_padding_horizontal`| `float`, optional| Horizontal padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`design_border_style`| `str`, optional| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`design_border_radius`| `float`, optional| Roundness. Flourish type hint: number, defaults to None  
`design_shadow`| `bool`, optional| Shadow. Flourish type hint: boolean, defaults to None  
`design_shadow_color`| `str`, optional| Shadow color. Shadow color as an RGBA value (red, green, blue, alpha). The alpha parameter is a number between 0.0 (fully transparent) and 1.0 (fully opaque). Flourish type hint: string, defaults to None  
`result_variables`| `Union[list, str]`, optional| Variables. Define variables to use in the Result field below. Set one variable per line in the format name = value Values can be: Numbers Text (single quotes for spaces) Question references like q_2 with the number representing the row number of each question in the Questions datasheet Previously defined variables (if wrapped into square brackets ) which will resolve to the answered value Excel functions, e.g., a = SUM(q_2, q_3) Flourish type hint: text, defaults to None  
`result_input`| `Union[list, str]`, optional| Result. Here you can compose your result view You have access to all variables you created above as well as all "q_" variables by referencing them in double curly braces like for example: `{{ my_variable }}` or `{{ q_6 }}` Flourish type hint: html, defaults to None  
`result_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`result_font_size`| `str`, optional| Text size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to None  
`result_font_size_custom`| `float`, optional| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`result_font_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`result_font_weight`| `str`, optional| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`result_font_style`| `str`, optional| Text style. Choices: normal, italic. Flourish type hint: string, defaults to None  
`result_border_type`| `str`, optional| Border. Choices: border-bottom, border. Flourish type hint: string, defaults to None  
`result_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`result_border_style`| `str`, optional| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`result_border_color`| `str`, optional| Border color. Flourish type hint: color, defaults to None  
`result_bg_type`| `str`, optional| Background. Choices: color, image. Flourish type hint: string, defaults to None  
`result_bg_color`| `str`, optional| Background color. Flourish type hint: color, defaults to None  
`result_bg_image_src`| `str`, optional| Image URL. Flourish type hint: url, defaults to None  
`result_bg_image_size`| `str`, optional| Image size. Choices: auto, cover, contain. Flourish type hint: string, defaults to None  
`design_question_font_size`| `str`, optional| Text size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to None  
`design_question_font_size_custom`| `float`, optional| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`design_question_font_color`| `str`, optional| Color. The text color used for your questions. If not set, the text color in Layout is used. Flourish type hint: color, defaults to None  
`design_question_font_weight`| `str`, optional| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`design_question_font_style`| `str`, optional| Text style. Choices: normal, italic. Flourish type hint: string, defaults to None  
`design_question_margin_vertical`| `float`, optional| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_question_margin_horizontal`| `float`, optional| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_question_padding`| `float`, optional| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_context_font_size`| `str`, optional| Text size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to None  
`design_context_font_size_custom`| `float`, optional| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`design_context_font_color`| `str`, optional| Color. The text color used for your question context. If not set, the text color in Layout is used. Flourish type hint: color, defaults to None  
`design_context_font_weight`| `str`, optional| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`design_context_font_style`| `str`, optional| Text style. Choices: normal, italic. Flourish type hint: string, defaults to None  
`design_context_margin_vertical`| `float`, optional| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_context_margin_horizontal`| `float`, optional| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_question_bg_color`| `str`, optional| Background color. The background color for your questions and context. To change the background color of the whole question card, go to the General design settings. Flourish type hint: color, defaults to None  
`design_question_bg_opacity`| `float`, optional| Background opacity. The opacity of the question background color. Flourish type hint: number, defaults to None  
`design_question_border_radius`| `float`, optional| Roundness. The roundness of the question background container. Flourish type hint: number, defaults to None  
`design_answer_margin_vertical`| `float`, optional| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_answer_margin_horizontal`| `float`, optional| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`input_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`input_background_color`| `str`, optional| Background color. Flourish type hint: color, defaults to None  
`input_width`| `float`, optional| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`number_input_placeholder`| `str`, optional| Number input placeholder. Flourish type hint: string, defaults to None  
`text_input_placeholder`| `str`, optional| Text input placeholder. Flourish type hint: string, defaults to None  
`input_input_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`input_border_color`| `str`, optional| Border color. Flourish type hint: color, defaults to None  
`input_border_radius`| `float`, optional| Roundness. Flourish type hint: number, defaults to None  
`input_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`input_border_style`| `str`, optional| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`input_align`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`input_margin`| `float`, optional| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`input_padding`| `float`, optional| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`button_font_size`| `str`, optional| Text size. Choices: 1, 1.2, 1.6, custom. Flourish type hint: string, defaults to None  
`button_font_size_custom`| `float`, optional| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`chart_button_control_style_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`chart_button_control_style_background_selected`| `str`, optional| Selected. Flourish type hint: color, defaults to None  
`chart_button_control_style_background_hover`| `str`, optional| Mouse over. Flourish type hint: color, defaults to None  
`chart_button_control_style_font_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`chart_button_control_style_font_color_selected`| `str`, optional| Selected. Flourish type hint: color, defaults to None  
`chart_button_control_style_font_color_hover`| `str`, optional| Mouse over. Flourish type hint: color, defaults to None  
`chart_button_control_style_button_styles_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_button_control_style_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`chart_button_control_style_border_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_button_control_style_border_transparency`| `float`, optional| Transparency. Flourish type hint: number, defaults to None  
`chart_button_control_style_border_radius`| `float`, optional| Radius. Flourish type hint: number, defaults to None  
`button_border_style`| `str`, optional| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`button_container_width`| `float`, optional| Button group width (%). The width of the button group as a percentage of the card width. Flourish type hint: number, defaults to None  
`button_justify_content`| `str`, optional| Align. Choices: flex-start, center, flex-end. Flourish type hint: string, defaults to None  
`button_margin`| `float`, optional| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`button_padding_factor`| `float`, optional| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`dropdown_font_size`| `str`, optional| Text size. Choices: 1, 1.2, 1.6, custom. Flourish type hint: string, defaults to None  
`dropdown_font_size_custom`| `float`, optional| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`dropdown_placeholder`| `str`, optional| Placeholder. Flourish type hint: string, defaults to None  
`chart_dropdown_control_style_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`chart_dropdown_control_style_font_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`chart_dropdown_control_style_border_styles_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_dropdown_control_style_border_style`| `str`, optional| Border style. Choices: all, bottom. Show border on all sides, or only at the bottom. Flourish type hint: string, defaults to None  
`chart_dropdown_control_style_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`chart_dropdown_control_style_border_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_dropdown_control_style_border_transparency`| `float`, optional| Transparency. Flourish type hint: number, defaults to None  
`chart_dropdown_control_style_border_radius`| `float`, optional| Radius. Flourish type hint: number, defaults to None  
`dropdown_padding_factor`| `float`, optional| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`dropdown_border_style`| `str`, optional| Border look. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`dropdown_font_weight`| `str`, optional| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`dropdown_font_style`| `str`, optional| Text style. Choices: normal, italic. Flourish type hint: string, defaults to None  
`dropdown_shadow`| `bool`, optional| Shadow. Flourish type hint: boolean, defaults to None  
`dropdown_shadow_color`| `str`, optional| Shadow color. Flourish type hint: string, defaults to None  
`date_format`| `str`, optional| Format. Choices: y-m-d, d/m/_y, d/m/y, j/n/_y, j/n/y, d-m-_y, d-m-y, j-n-_y, j-n-y, d.m._y, d.m.y, j.n._y, j.n.y, m/d/_y, m/d/y, n/j/_y, n/j/y, m-d-_y, m-d-y, n-j-_y, n-j-y, m j, _y, f j, _y. Flourish type hint: string, defaults to None  
`date_input_placeholder`| `str`, optional| Placeholder. Flourish type hint: string, defaults to None  
`date_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`date_width`| `float`, optional| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`date_margin`| `float`, optional| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`date_padding`| `float`, optional| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`date_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`date_border_style`| `str`, optional| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`date_border_color`| `str`, optional| Border color. Flourish type hint: color, defaults to None  
`date_border_radius`| `float`, optional| Roundness. Flourish type hint: number, defaults to None  
`date_align`| `str`, optional| Text alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`date_calendar_position_vertical`| `str`, optional| Calendar vertical position. Choices: auto, above, below. Flourish type hint: string, defaults to None  
`date_calendar_position_horizontal`| `str`, optional| Calendar horizontal position. Choices: left, center, right. Flourish type hint: string, defaults to None  
`rating_icon_type`| `str`, optional| Choices: star, circle, check. Flourish type hint: string, defaults to None  
`rating_icon_fill_base`| `str`, optional| Base fill color. Flourish type hint: color, defaults to None  
`rating_icon_stroke_base`| `str`, optional| Base stroke color. Flourish type hint: color, defaults to None  
`rating_icon_fill_active`| `str`, optional| Active fill color. Flourish type hint: color, defaults to None  
`rating_icon_stroke_active`| `str`, optional| Active stroke color. Flourish type hint: color, defaults to None  
`rating_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`rating_icon_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`rating_icon_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`rating_icon_margin`| `float`, optional| Vertical margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`rating_icon_stroke_width`| `float`, optional| Stroke width (px). Flourish type hint: number, defaults to None  
`rating_container_width`| `float`, optional| Rating group width (%). The width of the rating group as a percentage of the card width. Flourish type hint: number, defaults to None  
`rating_wrap_margin_vertical`| `float`, optional| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`rating_wrap_margin_horizontal`| `float`, optional| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`rating_wrap_padding_vertical`| `float`, optional| Vertical padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`rating_wrap_padding_horizontal`| `float`, optional| Horizontal padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`rating_label_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`rating_label_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`rating_label_position`| `str`, optional| Position. Choices: above, below. Flourish type hint: string, defaults to None  
`chart_slider_filter_controls_handle_color`| `str`, optional| Handle color. Flourish type hint: color, defaults to None  
`chart_slider_filter_controls_track_active_color`| `str`, optional| Track active color. Flourish type hint: color, defaults to None  
`chart_slider_filter_controls_track_base_color`| `str`, optional| Track background color. Flourish type hint: color, defaults to None  
`chart_slider_filter_controls_handle_size`| `float`, optional| Handle size. percentage of track height. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_ticks`| `bool`, optional| Range ticks. Display the minimum and the maximum of the range at the left and right. Flourish type hint: boolean, defaults to None  
`chart_slider_filter_controls_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_slider_filter_controls_container_width`| `float`, optional| Track width (%). The width of the track as a percentage of the card width. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_wrap_margin_vertical`| `float`, optional| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_wrap_margin_horizontal`| `float`, optional| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_track_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_track_border_radius`| `float`, optional| Roundness. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_track_border_color`| `str`, optional| Border color. Flourish type hint: color, defaults to None  
`chart_slider_filter_controls_track_border_width`| `float`, optional| Border width. The width of the border around the card, in rems Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_handle_shape`| `str`, optional| Shape. Choices: rectangle, circle. Flourish type hint: string, defaults to None  
`chart_slider_filter_controls_handle_width`| `float`, optional| Width. % of Size (the handle height). Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_handle_border_color`| `str`, optional| Stroke color. Flourish type hint: color, defaults to None  
`chart_slider_filter_controls_handle_border_width`| `float`, optional| Stroke width. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_handle_border_radius`| `float`, optional| Roundness. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_handle_box_shadow`| `bool`, optional| Box shadow. Flourish type hint: boolean, defaults to None  
`chart_slider_filter_controls_tooltips`| `bool`, optional| Tooltip. Flourish type hint: boolean, defaults to None  
`chart_slider_filter_controls_tooltip_background`| `bool`, optional| Tooltip background. Flourish type hint: boolean, defaults to None  
`chart_slider_filter_controls_tick_color`| `str`, optional| Tick color. Flourish type hint: color, defaults to None  
`chart_slider_filter_controls_tick_padding`| `float`, optional| Tick padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_tick_number_padding`| `float`, optional| Number padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`submit_comment_text`| `Union[list, str]`, optional| Submit label. Flourish type hint: text, defaults to None  
`submit_button_text`| `str`, optional| Submit button text. Flourish type hint: string, defaults to None  
`submit_bg_type`| `str`, optional| Background. Choices: color, image. Flourish type hint: string, defaults to None  
`submit_bg_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`submit_bg_image_src`| `str`, optional| Image URL. Flourish type hint: url, defaults to None  
`submit_border`| `bool`, optional| Border. Flourish type hint: boolean, defaults to None  
`submit_bg_image_size`| `str`, optional| Image size. Choices: auto, cover, contain. Flourish type hint: string, defaults to None  
`submit_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`submit_comment_font_size`| `str`, optional| Label size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to None  
`submit_comment_font_size_custom`| `float`, optional| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`submit_comment_font_weight`| `str`, optional| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`submit_comment_font_style`| `str`, optional| Text style. Choices: normal, italic. Flourish type hint: string, defaults to None  
`submit_flex_direction`| `str`, optional| Label position. Choices: column, column-reverse. Flourish type hint: string, defaults to None  
`submit_comment_font_color`| `str`, optional| Label color. Flourish type hint: color, defaults to None  
`submit_comment_margin`| `float`, optional| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`submit_button_font_size`| `str`, optional| Button text size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to None  
`submit_button_font_size_custom`| `float`, optional| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`submit_button_font_weight`| `str`, optional| Button text weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`submit_button_font_style`| `str`, optional| Text style. Choices: normal, italic. Flourish type hint: string, defaults to None  
`submit_button_margin`| `float`, optional| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`submit_button_padding_factor`| `float`, optional| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`submit_button_box_shadow`| `bool`, optional| Hover shadow. Flourish type hint: boolean, defaults to None  
`submit_button_use_default_styles`| `bool`, optional| Use answer button styles. Flourish type hint: boolean, defaults to None  
`submit_button_bg_color`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`submit_button_bg_color_hover`| `str`, optional| Mouse over. Flourish type hint: color, defaults to None  
`submit_button_font_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`submit_button_font_color_hover`| `str`, optional| Mouse over. Flourish type hint: color, defaults to None  
`submit_button_border_style`| `str`, optional| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`submit_button_border_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`submit_button_border_width`| `float`, optional| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`submit_button_border_transparency`| `float`, optional| Transparency. Flourish type hint: number, defaults to None  
`submit_button_border_radius`| `float`, optional| Roundness. Flourish type hint: number, defaults to None  
`design_controls_position`| `str`, optional| Position. Choices: top_left, top_centre, top_right, bottom_left, bottom_centre, bottom_right. Flourish type hint: string, defaults to None  
`design_controls_button_symbol_back`| `str`, optional| Back button. Flourish type hint: string, defaults to None  
`design_controls_button_symbol_forward`| `str`, optional| Forward button. Flourish type hint: string, defaults to None  
`design_controls_button_font_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`design_controls_button_font_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`design_controls_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`design_controls_button_margin`| `float`, optional| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_controls_button_padding_factor`| `float`, optional| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_controls_button_bg_color`| `str`, optional| Background color. Flourish type hint: color, defaults to None  
`design_controls_button_bg_opacity`| `float`, optional| Background opacity. Flourish type hint: number, defaults to None  
`design_controls_button_font_weight`| `str`, optional| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`design_controls_button_font_style`| `str`, optional| Text style. Choices: normal, italic. Flourish type hint: string, defaults to None  
`design_controls_button_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`design_controls_button_border_style`| `str`, optional| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`design_controls_button_border_color`| `str`, optional| Border color. Flourish type hint: color, defaults to None  
`design_controls_button_border_radius`| `float`, optional| Roundness. Flourish type hint: number, defaults to None  
`design_progress_show`| `bool`, optional| Show progress bar. Flourish type hint: boolean, defaults to None  
`design_progress_position`| `str`, optional| Position. Choices: top, bottom. Flourish type hint: string, defaults to None  
`design_progress_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`design_progress_margin`| `float`, optional| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`design_progress_bg_color`| `str`, optional| Background color. Flourish type hint: color, defaults to None  
`design_progress_bg_opacity`| `float`, optional| Background opacity. Flourish type hint: number, defaults to None  
`chart_number_date_format_prefix`| `str`, optional| Prefix. Text to place in front of number. Flourish type hint: string, defaults to None  
`chart_number_date_format_suffix`| `str`, optional| Suffix. Text to place after number. Flourish type hint: string, defaults to None  
`chart_number_date_format_n_dec`| `float`, optional| Decimal places. Enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to None  
`chart_number_date_format_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_number_date_format_negative_sign`| `str`, optional| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to None  
`chart_number_date_format_strip_zeros`| `bool`, optional| Remove trailing zeros. Flourish type hint: boolean, defaults to None  
`chart_number_date_format_strip_separator`| `bool`, optional| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to None  
`chart_number_date_format_transform_labels`| `bool`, optional| Multiply/divide values. Flourish type hint: boolean, defaults to None  
`chart_number_date_format_transform`| `str`, optional| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to None  
`chart_number_date_format_multiply_divide_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_number_date_format_exponentiate_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_number_localization_input_decimal_separator`| `str`, optional| Decimal separator in data sheet. Choices: ., ,. Used for interpreting your data. Only change if data is not displaying on the chart as expected. Flourish type hint: string, defaults to None  
`chart_number_localization_output_separators`| `str`, optional| Number format to display. Choices: ,., .,, ., ,, ., ,. How the numbers should appear on chart labels. Flourish type hint: string, defaults to None  
`external_write_enabled`| `bool`, optional| Store result data externally. Flourish type hint: boolean, defaults to None  
`external_write_endpoint`| `str`, optional| Storage endpoint. Your external database, store, API or web app endpoint to post data to. If you were to use Google Sheets to store your data, please check the External write docs for integration help. Flourish type hint: string, defaults to None  
`chart_layout_body_font`| `str`, optional| Main font. This font will apply to the whole graphic by default. You can optionally change the font for the title, subtitle, footer, etc in the Header and Footer settings panels. Flourish type hint: font, defaults to None  
`chart_layout_font_color`| `str`, optional| Text color. This color will apply to the whole graphic by default, You can optionally change the color for individual text elements, in other settings panels. Flourish type hint: color, defaults to None  
`chart_layout_background_color_enabled`| `bool`, optional| Color. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_layout_background_image_enabled`| `bool`, optional| Image. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_layout_background_color`| `str`, optional| Background color. Flourish type hint: color, defaults to None  
`chart_layout_background_image_src`| `str`, optional| Image URL. Flourish type hint: url, defaults to None  
`chart_layout_background_image_size`| `str`, optional| Size. Choices: cover, contain, auto, 100% 100%. Flourish type hint: string, defaults to None  
`chart_layout_background_image_position`| `str`, optional| Position. Choices: top left, top center, top right, center left, center center, center right, bottom left, bottom center, bottom right. Flourish type hint: string, defaults to None  
`chart_layout_max_width_target`| `str`, optional| Maximum width. Choices: none, wrapper, primary. Apply a maximum width to just the main graphic or everything (main graphic plus header, footer, etc). Flourish type hint: string, defaults to None  
`chart_layout_max_width`| `float`, optional| Maximum width. Leave blank to stretch to container width. Flourish type hint: number, defaults to None  
`chart_layout_max_width_align`| `str`, optional| Align. Choices: left, center, right. Flourish type hint: string, defaults to None  
`chart_layout_layout_order`| `str`, optional| Layout order. Flourish type hint: string, defaults to None  
`chart_layout_space_between_sections`| `str`, optional| Space between sections. Choices: 0.5, 1, 1.5, custom. Flourish type hint: string, defaults to None  
`chart_layout_space_between_sections_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`chart_layout_margin_top`| `float`, optional| Top. Flourish type hint: number, defaults to None  
`chart_layout_margin_right`| `float`, optional| Right. Flourish type hint: number, defaults to None  
`chart_layout_margin_bottom`| `float`, optional| Bottom. Flourish type hint: number, defaults to None  
`chart_layout_margin_left`| `float`, optional| Left. Flourish type hint: number, defaults to None  
`chart_layout_border_enabled`| `bool`, optional| Show borders around visualisation. Flourish type hint: boolean, defaults to None  
`chart_layout_border_top_width`| `float`, optional| Top. Flourish type hint: number, defaults to None  
`chart_layout_border_top_style`| `str`, optional| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`chart_layout_border_top_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_border_right_width`| `float`, optional| Right. Flourish type hint: number, defaults to None  
`chart_layout_border_right_style`| `str`, optional| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`chart_layout_border_right_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_border_bottom_width`| `float`, optional| Bottom. Flourish type hint: number, defaults to None  
`chart_layout_border_bottom_style`| `str`, optional| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`chart_layout_border_bottom_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_border_left_width`| `float`, optional| Left. Flourish type hint: number, defaults to None  
`chart_layout_border_left_style`| `str`, optional| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`chart_layout_border_left_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_read_direction`| `str`, optional| Read direction. Choices: ltr, rtl. This will change the reading direction of the main text elements on the page. Its not possible to adjust this on all elements, such as axes. Note that when direction is set to right to left any alignment icons will be reversed. Flourish type hint: string, defaults to None  
`chart_layout_font_size_mobile_small`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_font_size_mobile_big`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_font_size_tablet`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_font_size_desktop`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_font_size_big_screen`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_breakpoint_mobile_small`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_breakpoint_mobile_big`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_breakpoint_tablet`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_breakpoint_desktop`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_breakpoint_big_screen`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_layout_header_align`| `str`, optional| Alignment. Choices: left, center, right. Flourish type hint: string, defaults to None  
`chart_layout_title`| `Union[list, str]`, optional| Flourish type hint: html, defaults to None  
`chart_layout_title_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_layout_title_font`| `str`, optional| Title Font. Flourish type hint: font, defaults to None  
`chart_layout_title_size`| `str`, optional| Size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to None  
`chart_layout_title_size_custom`| `float`, optional| Custom. Specify a custom responsive font size in rems The best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`chart_layout_title_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_layout_title_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_title_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`chart_layout_title_space_above`| `str`, optional| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to None  
`chart_layout_title_space_above_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`chart_layout_subtitle`| `Union[list, str]`, optional| Flourish type hint: html, defaults to None  
`chart_layout_subtitle_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_layout_subtitle_font`| `str`, optional| Subtitle Font. Flourish type hint: font, defaults to None  
`chart_layout_subtitle_size`| `str`, optional| Size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to None  
`chart_layout_subtitle_size_custom`| `float`, optional| Custom. Specify a custom responsive font size in rems The best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`chart_layout_subtitle_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_layout_subtitle_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_subtitle_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`chart_layout_subtitle_space_above`| `str`, optional| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to None  
`chart_layout_subtitle_space_above_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`chart_layout_header_text`| `Union[list, str]`, optional| Flourish type hint: html, defaults to None  
`chart_layout_header_text_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_layout_header_text_size`| `str`, optional| Size. Choices: 1.2, 1.4, 1.6, custom. Flourish type hint: string, defaults to None  
`chart_layout_header_text_size_custom`| `float`, optional| Custom. Specify a custom responsive font size in rems The best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`chart_layout_header_text_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_layout_header_text_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_header_text_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`chart_layout_header_text_space_above`| `str`, optional| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to None  
`chart_layout_header_text_space_above_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`chart_layout_header_border`| `str`, optional| Choices: top, bottom, top_and_bottom, none. Flourish type hint: string, defaults to None  
`chart_layout_header_border_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_layout_header_border_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_header_border_style`| `str`, optional| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`chart_layout_header_border_space`| `float`, optional| Space. Space between border and header text. Flourish type hint: number, defaults to None  
`chart_layout_header_logo_enabled`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_layout_header_logo_src`| `str`, optional| Image. Flourish type hint: url, defaults to None  
`chart_layout_header_logo_alt`| `str`, optional| Alt text. Flourish type hint: string, defaults to None  
`chart_layout_header_logo_link_url`| `str`, optional| Link. Flourish type hint: string, defaults to None  
`chart_layout_header_logo_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`chart_layout_header_logo_align`| `str`, optional| Align. Choices: inside, outside. Align logo inside either the header or the main visualization container. Flourish type hint: string, defaults to None  
`chart_layout_header_logo_position_inside`| `str`, optional| Position. Choices: top, left, right. Flourish type hint: string, defaults to None  
`chart_layout_header_logo_position_outside`| `str`, optional| Position. Choices: left, right. Flourish type hint: string, defaults to None  
`chart_layout_header_logo_margin_top`| `float`, optional| Top. Flourish type hint: number, defaults to None  
`chart_layout_header_logo_margin_right`| `float`, optional| Right. Flourish type hint: number, defaults to None  
`chart_layout_header_logo_margin_bottom`| `float`, optional| Bottom. Flourish type hint: number, defaults to None  
`chart_layout_header_logo_margin_left`| `float`, optional| Left. Flourish type hint: number, defaults to None  
`chart_layout_footer_align`| `str`, optional| Alignment. Choices: left, center, right, justify. Flourish type hint: string, defaults to None  
`chart_layout_footer_text_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_layout_footer_text_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_footer_styling`| `bool`, optional| Advanced footer styles. Flourish type hint: boolean, defaults to None  
`chart_layout_footer_font`| `str`, optional| Font. Flourish type hint: font, defaults to None  
`chart_layout_footer_text_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_layout_source_name`| `str`, optional| Source name. Flourish type hint: string, defaults to None  
`chart_layout_source_url`| `str`, optional| Source url. Flourish type hint: string, defaults to None  
`chart_layout_multiple_sources`| `bool`, optional| Multiple sources. Flourish type hint: boolean, defaults to None  
`chart_layout_source_name_2`| `str`, optional| Source name. Flourish type hint: string, defaults to None  
`chart_layout_source_url_2`| `str`, optional| Source url. Flourish type hint: string, defaults to None  
`chart_layout_source_name_3`| `str`, optional| Source name. Flourish type hint: string, defaults to None  
`chart_layout_source_url_3`| `str`, optional| Source url. Flourish type hint: string, defaults to None  
`chart_layout_source_label`| `str`, optional| Source label. Flourish type hint: string, defaults to None  
`chart_layout_footer_note`| `Union[list, str]`, optional| Note. To add the time/date stamp of when the data was last updated add `{{data_last_updated}}`. For example, "Last updated at `{{data_last_updated}}`". To customize the format, use the advanced options below. Flourish type hint: html, defaults to None  
`chart_layout_footer_note_secondary`| `Union[list, str]`, optional| Note (secondary). The secondary note is placed below the source and primary note. To add the time/date stamp of when the data was last updated add `{{data_last_updated}}`. For example, "Last updated at `{{data_last_updated}}`". To customize the format, use the advanced options below. Flourish type hint: html, defaults to None  
`chart_layout_advanced_note_styling`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_layout_footer_timestamp_format`| `str`, optional| Time/date stamp formatting. Choices: %H:%M:%S, %I:%M %p, %H:%M, %H:%M %p, %H:%M:%S, %d %b %Y, %H:%M, %d %b %Y, %H:%M, %d/%m/%Y, %H:%M, %m/%d/%Y, %H:%M, %d-%m-%Y, %H:%M, %m-%d-%Y, %d %b %Y, %m/%d/%Y, %d/%m/%Y, %m-%d-%Y, %d-%m-%Y, %Y-%m-%d, %Y-%m-%d %H:%M:%S. Flourish type hint: string, defaults to None  
`chart_layout_footer_logo_enabled`| `bool`, optional| Image. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_layout_footer_logo_src`| `str`, optional| Image. Flourish type hint: url, defaults to None  
`chart_layout_footer_logo_src_light`| `str`, optional| Image (light version). If provided this version will be used whenever the background color is dark. Flourish type hint: hidden, defaults to None  
`chart_layout_footer_logo_alt`| `str`, optional| Alt text. Flourish type hint: string, defaults to None  
`chart_layout_footer_logo_link_url`| `str`, optional| Link. Flourish type hint: string, defaults to None  
`chart_layout_footer_logo_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`chart_layout_footer_logo_margin`| `float`, optional| Margin. Flourish type hint: number, defaults to None  
`chart_layout_footer_logo_order`| `str`, optional| Position. Choices: left, right. Flourish type hint: string, defaults to None  
`chart_layout_footer_align_vertical`| `str`, optional| V. align. Choices: flex-start, center, flex-end. Flourish type hint: string, defaults to None  
`chart_layout_footer_border`| `str`, optional| Choices: top, bottom, top_and_bottom, none. Flourish type hint: string, defaults to None  
`chart_layout_footer_border_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_layout_footer_border_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_layout_footer_border_style`| `str`, optional| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to None  
`chart_layout_footer_border_space`| `float`, optional| Space. Space between border and footer text. Flourish type hint: number, defaults to None  
`chart_layout_screenreader_text_primary`| `Union[list, str]`, optional| Screenreader description. A text alternative to the visual content that will only be visible to screenreaders, e.g. The line chart shows China consistently higher than the other countries since 1990. Do not replicate your title, since that will also be read by screenreaders. Flourish type hint: text, defaults to None  
`chart_layout_screenreader_label`| `str`, optional| Screenreader label. A short text label given to the main Flourish embed wrapper to provide an accessible name that is only visible to screenreaders Added in the form of an "aria-label". Flourish type hint: string, defaults to None  
`chart_layout_screenreader_hide_primary`| `bool`, optional| Screenreader mode for main visual container. Choices: True, False. Whether the main visual container is visible to screenreaders (Text in the header and footer are always available to screenreaders.). Flourish type hint: boolean, defaults to None  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`question_flow`| Question flow. Choices: vertical, horizontal. Flourish type hint: string, defaults to `NULL`  
`design_border_type`| Border. Choices: border-bottom, border. Flourish type hint: string, defaults to `NULL`  
`design_border_color`| Border color. Flourish type hint: color, defaults to `NULL`  
`design_background`| Background. The background color of the cards. If not set, the background color in Layout is used. Flourish type hint: color, defaults to `NULL`  
`design_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`design_align_horizontal`| Align. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`design_align_vertical`| Position. Choices: start, center, flex-end. Set the vertical text position if the window height is fixed and the text doesnt stretch across the full vertical card space. Flourish type hint: string, defaults to `NULL`  
`design_max_width`| Max width (%). Flourish type hint: number, defaults to `NULL`  
`design_margin_vertical`| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_padding_vertical`| Vertical padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_padding_horizontal`| Horizontal padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`design_border_style`| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`design_border_radius`| Roundness. Flourish type hint: number, defaults to `NULL`  
`design_shadow`| Shadow. Flourish type hint: boolean, defaults to `NULL`  
`design_shadow_color`| Shadow color. Shadow color as an RGBA value (red, green, blue, alpha). The alpha parameter is a number between 0.0 (fully transparent) and 1.0 (fully opaque). Flourish type hint: string, defaults to `NULL`  
`result_variables`| Variables. Define variables to use in the Result field below. Set one variable per line in the format name = value Values can be: Numbers Text (single quotes for spaces) Question references like q_2 with the number representing the row number of each question in the Questions datasheet Previously defined variables (if wrapped into square brackets ) which will resolve to the answered value Excel functions, e.g., a = SUM(q_2, q_3) Flourish type hint: text, defaults to `NULL`  
`result_input`| Result. Here you can compose your result view You have access to all variables you created above as well as all "q_" variables by referencing them in double curly braces like for example: `{{ my_variable }}` or `{{ q_6 }}` Flourish type hint: html, defaults to `NULL`  
`result_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`result_font_size`| Text size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to `NULL`  
`result_font_size_custom`| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`result_font_color`| Color. Flourish type hint: color, defaults to `NULL`  
`result_font_weight`| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`result_font_style`| Text style. Choices: normal, italic. Flourish type hint: string, defaults to `NULL`  
`result_border_type`| Border. Choices: border-bottom, border. Flourish type hint: string, defaults to `NULL`  
`result_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`result_border_style`| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`result_border_color`| Border color. Flourish type hint: color, defaults to `NULL`  
`result_bg_type`| Background. Choices: color, image. Flourish type hint: string, defaults to `NULL`  
`result_bg_color`| Background color. Flourish type hint: color, defaults to `NULL`  
`result_bg_image_src`| Image URL. Flourish type hint: url, defaults to `NULL`  
`result_bg_image_size`| Image size. Choices: auto, cover, contain. Flourish type hint: string, defaults to `NULL`  
`design_question_font_size`| Text size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to `NULL`  
`design_question_font_size_custom`| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`design_question_font_color`| Color. The text color used for your questions. If not set, the text color in Layout is used. Flourish type hint: color, defaults to `NULL`  
`design_question_font_weight`| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`design_question_font_style`| Text style. Choices: normal, italic. Flourish type hint: string, defaults to `NULL`  
`design_question_margin_vertical`| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_question_margin_horizontal`| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_question_padding`| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_context_font_size`| Text size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to `NULL`  
`design_context_font_size_custom`| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`design_context_font_color`| Color. The text color used for your question context. If not set, the text color in Layout is used. Flourish type hint: color, defaults to `NULL`  
`design_context_font_weight`| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`design_context_font_style`| Text style. Choices: normal, italic. Flourish type hint: string, defaults to `NULL`  
`design_context_margin_vertical`| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_context_margin_horizontal`| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_question_bg_color`| Background color. The background color for your questions and context. To change the background color of the whole question card, go to the General design settings. Flourish type hint: color, defaults to `NULL`  
`design_question_bg_opacity`| Background opacity. The opacity of the question background color. Flourish type hint: number, defaults to `NULL`  
`design_question_border_radius`| Roundness. The roundness of the question background container. Flourish type hint: number, defaults to `NULL`  
`design_answer_margin_vertical`| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_answer_margin_horizontal`| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`input_color`| Color. Flourish type hint: color, defaults to `NULL`  
`input_background_color`| Background color. Flourish type hint: color, defaults to `NULL`  
`input_width`| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`number_input_placeholder`| Number input placeholder. Flourish type hint: string, defaults to `NULL`  
`text_input_placeholder`| Text input placeholder. Flourish type hint: string, defaults to `NULL`  
`input_input_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`input_border_color`| Border color. Flourish type hint: color, defaults to `NULL`  
`input_border_radius`| Roundness. Flourish type hint: number, defaults to `NULL`  
`input_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`input_border_style`| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`input_align`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`input_margin`| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`input_padding`| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`button_font_size`| Text size. Choices: 1, 1.2, 1.6, custom. Flourish type hint: string, defaults to `NULL`  
`button_font_size_custom`| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`chart_button_control_style_background`| Background. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_background_selected`| Selected. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_background_hover`| Mouse over. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_font_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_font_color_selected`| Selected. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_font_color_hover`| Mouse over. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_button_styles_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_button_control_style_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`chart_button_control_style_border_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_border_transparency`| Transparency. Flourish type hint: number, defaults to `NULL`  
`chart_button_control_style_border_radius`| Radius. Flourish type hint: number, defaults to `NULL`  
`button_border_style`| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`button_container_width`| Button group width (%). The width of the button group as a percentage of the card width. Flourish type hint: number, defaults to `NULL`  
`button_justify_content`| Align. Choices: flex-start, center, flex-end. Flourish type hint: string, defaults to `NULL`  
`button_margin`| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`button_padding_factor`| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`dropdown_font_size`| Text size. Choices: 1, 1.2, 1.6, custom. Flourish type hint: string, defaults to `NULL`  
`dropdown_font_size_custom`| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`dropdown_placeholder`| Placeholder. Flourish type hint: string, defaults to `NULL`  
`chart_dropdown_control_style_background`| Background. Flourish type hint: color, defaults to `NULL`  
`chart_dropdown_control_style_font_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`chart_dropdown_control_style_border_styles_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_dropdown_control_style_border_style`| Border style. Choices: all, bottom. Show border on all sides, or only at the bottom. Flourish type hint: string, defaults to `NULL`  
`chart_dropdown_control_style_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`chart_dropdown_control_style_border_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_dropdown_control_style_border_transparency`| Transparency. Flourish type hint: number, defaults to `NULL`  
`chart_dropdown_control_style_border_radius`| Radius. Flourish type hint: number, defaults to `NULL`  
`dropdown_padding_factor`| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`dropdown_border_style`| Border look. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`dropdown_font_weight`| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`dropdown_font_style`| Text style. Choices: normal, italic. Flourish type hint: string, defaults to `NULL`  
`dropdown_shadow`| Shadow. Flourish type hint: boolean, defaults to `NULL`  
`dropdown_shadow_color`| Shadow color. Flourish type hint: string, defaults to `NULL`  
`date_format`| Format. Choices: y-m-d, d/m/_y, d/m/y, j/n/_y, j/n/y, d-m-_y, d-m-y, j-n-_y, j-n-y, d.m._y, d.m.y, j.n._y, j.n.y, m/d/_y, m/d/y, n/j/_y, n/j/y, m-d-_y, m-d-y, n-j-_y, n-j-y, m j, _y, f j, _y. Flourish type hint: string, defaults to `NULL`  
`date_input_placeholder`| Placeholder. Flourish type hint: string, defaults to `NULL`  
`date_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`date_width`| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`date_margin`| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`date_padding`| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`date_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`date_border_style`| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`date_border_color`| Border color. Flourish type hint: color, defaults to `NULL`  
`date_border_radius`| Roundness. Flourish type hint: number, defaults to `NULL`  
`date_align`| Text alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`date_calendar_position_vertical`| Calendar vertical position. Choices: auto, above, below. Flourish type hint: string, defaults to `NULL`  
`date_calendar_position_horizontal`| Calendar horizontal position. Choices: left, center, right. Flourish type hint: string, defaults to `NULL`  
`rating_icon_type`| Choices: star, circle, check. Flourish type hint: string, defaults to `NULL`  
`rating_icon_fill_base`| Base fill color. Flourish type hint: color, defaults to `NULL`  
`rating_icon_stroke_base`| Base stroke color. Flourish type hint: color, defaults to `NULL`  
`rating_icon_fill_active`| Active fill color. Flourish type hint: color, defaults to `NULL`  
`rating_icon_stroke_active`| Active stroke color. Flourish type hint: color, defaults to `NULL`  
`rating_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`rating_icon_width`| Width. Flourish type hint: number, defaults to `NULL`  
`rating_icon_height`| Height. Flourish type hint: number, defaults to `NULL`  
`rating_icon_margin`| Vertical margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`rating_icon_stroke_width`| Stroke width (px). Flourish type hint: number, defaults to `NULL`  
`rating_container_width`| Rating group width (%). The width of the rating group as a percentage of the card width. Flourish type hint: number, defaults to `NULL`  
`rating_wrap_margin_vertical`| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`rating_wrap_margin_horizontal`| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`rating_wrap_padding_vertical`| Vertical padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`rating_wrap_padding_horizontal`| Horizontal padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`rating_label_width`| Width. Flourish type hint: number, defaults to `NULL`  
`rating_label_color`| Color. Flourish type hint: color, defaults to `NULL`  
`rating_label_position`| Position. Choices: above, below. Flourish type hint: string, defaults to `NULL`  
`chart_slider_filter_controls_handle_color`| Handle color. Flourish type hint: color, defaults to `NULL`  
`chart_slider_filter_controls_track_active_color`| Track active color. Flourish type hint: color, defaults to `NULL`  
`chart_slider_filter_controls_track_base_color`| Track background color. Flourish type hint: color, defaults to `NULL`  
`chart_slider_filter_controls_handle_size`| Handle size. percentage of track height. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_ticks`| Range ticks. Display the minimum and the maximum of the range at the left and right. Flourish type hint: boolean, defaults to `NULL`  
`chart_slider_filter_controls_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_slider_filter_controls_container_width`| Track width (%). The width of the track as a percentage of the card width. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_wrap_margin_vertical`| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_wrap_margin_horizontal`| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_track_height`| Height. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_track_border_radius`| Roundness. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_track_border_color`| Border color. Flourish type hint: color, defaults to `NULL`  
`chart_slider_filter_controls_track_border_width`| Border width. The width of the border around the card, in rems Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_handle_shape`| Shape. Choices: rectangle, circle. Flourish type hint: string, defaults to `NULL`  
`chart_slider_filter_controls_handle_width`| Width. % of Size (the handle height). Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_handle_border_color`| Stroke color. Flourish type hint: color, defaults to `NULL`  
`chart_slider_filter_controls_handle_border_width`| Stroke width. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_handle_border_radius`| Roundness. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_handle_box_shadow`| Box shadow. Flourish type hint: boolean, defaults to `NULL`  
`chart_slider_filter_controls_tooltips`| Tooltip. Flourish type hint: boolean, defaults to `NULL`  
`chart_slider_filter_controls_tooltip_background`| Tooltip background. Flourish type hint: boolean, defaults to `NULL`  
`chart_slider_filter_controls_tick_color`| Tick color. Flourish type hint: color, defaults to `NULL`  
`chart_slider_filter_controls_tick_padding`| Tick padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_tick_number_padding`| Number padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`submit_comment_text`| Submit label. Flourish type hint: text, defaults to `NULL`  
`submit_button_text`| Submit button text. Flourish type hint: string, defaults to `NULL`  
`submit_bg_type`| Background. Choices: color, image. Flourish type hint: string, defaults to `NULL`  
`submit_bg_color`| Color. Flourish type hint: color, defaults to `NULL`  
`submit_bg_image_src`| Image URL. Flourish type hint: url, defaults to `NULL`  
`submit_border`| Border. Flourish type hint: boolean, defaults to `NULL`  
`submit_bg_image_size`| Image size. Choices: auto, cover, contain. Flourish type hint: string, defaults to `NULL`  
`submit_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`submit_comment_font_size`| Label size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to `NULL`  
`submit_comment_font_size_custom`| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`submit_comment_font_weight`| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`submit_comment_font_style`| Text style. Choices: normal, italic. Flourish type hint: string, defaults to `NULL`  
`submit_flex_direction`| Label position. Choices: column, column-reverse. Flourish type hint: string, defaults to `NULL`  
`submit_comment_font_color`| Label color. Flourish type hint: color, defaults to `NULL`  
`submit_comment_margin`| Vertical margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`submit_button_font_size`| Button text size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to `NULL`  
`submit_button_font_size_custom`| Custom. Specify a custom responsive text size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`submit_button_font_weight`| Button text weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`submit_button_font_style`| Text style. Choices: normal, italic. Flourish type hint: string, defaults to `NULL`  
`submit_button_margin`| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`submit_button_padding_factor`| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`submit_button_box_shadow`| Hover shadow. Flourish type hint: boolean, defaults to `NULL`  
`submit_button_use_default_styles`| Use answer button styles. Flourish type hint: boolean, defaults to `NULL`  
`submit_button_bg_color`| Background. Flourish type hint: color, defaults to `NULL`  
`submit_button_bg_color_hover`| Mouse over. Flourish type hint: color, defaults to `NULL`  
`submit_button_font_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`submit_button_font_color_hover`| Mouse over. Flourish type hint: color, defaults to `NULL`  
`submit_button_border_style`| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`submit_button_border_color`| Color. Flourish type hint: color, defaults to `NULL`  
`submit_button_border_width`| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`submit_button_border_transparency`| Transparency. Flourish type hint: number, defaults to `NULL`  
`submit_button_border_radius`| Roundness. Flourish type hint: number, defaults to `NULL`  
`design_controls_position`| Position. Choices: top_left, top_centre, top_right, bottom_left, bottom_centre, bottom_right. Flourish type hint: string, defaults to `NULL`  
`design_controls_button_symbol_back`| Back button. Flourish type hint: string, defaults to `NULL`  
`design_controls_button_symbol_forward`| Forward button. Flourish type hint: string, defaults to `NULL`  
`design_controls_button_font_color`| Color. Flourish type hint: color, defaults to `NULL`  
`design_controls_button_font_size`| Size. Flourish type hint: number, defaults to `NULL`  
`design_controls_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`design_controls_button_margin`| Margin. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_controls_button_padding_factor`| Padding. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_controls_button_bg_color`| Background color. Flourish type hint: color, defaults to `NULL`  
`design_controls_button_bg_opacity`| Background opacity. Flourish type hint: number, defaults to `NULL`  
`design_controls_button_font_weight`| Text weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`design_controls_button_font_style`| Text style. Choices: normal, italic. Flourish type hint: string, defaults to `NULL`  
`design_controls_button_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`design_controls_button_border_style`| Border style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`design_controls_button_border_color`| Border color. Flourish type hint: color, defaults to `NULL`  
`design_controls_button_border_radius`| Roundness. Flourish type hint: number, defaults to `NULL`  
`design_progress_show`| Show progress bar. Flourish type hint: boolean, defaults to `NULL`  
`design_progress_position`| Position. Choices: top, bottom. Flourish type hint: string, defaults to `NULL`  
`design_progress_height`| Height. Flourish type hint: number, defaults to `NULL`  
`design_progress_margin`| Horizontal margins. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`design_progress_bg_color`| Background color. Flourish type hint: color, defaults to `NULL`  
`design_progress_bg_opacity`| Background opacity. Flourish type hint: number, defaults to `NULL`  
`chart_number_date_format_prefix`| Prefix. Text to place in front of number. Flourish type hint: string, defaults to `NULL`  
`chart_number_date_format_suffix`| Suffix. Text to place after number. Flourish type hint: string, defaults to `NULL`  
`chart_number_date_format_n_dec`| Decimal places. Enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to `NULL`  
`chart_number_date_format_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_number_date_format_negative_sign`| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to `NULL`  
`chart_number_date_format_strip_zeros`| Remove trailing zeros. Flourish type hint: boolean, defaults to `NULL`  
`chart_number_date_format_strip_separator`| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to `NULL`  
`chart_number_date_format_transform_labels`| Multiply/divide values. Flourish type hint: boolean, defaults to `NULL`  
`chart_number_date_format_transform`| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to `NULL`  
`chart_number_date_format_multiply_divide_constant`| Flourish type hint: number, defaults to `NULL`  
`chart_number_date_format_exponentiate_constant`| Flourish type hint: number, defaults to `NULL`  
`chart_number_localization_input_decimal_separator`| Decimal separator in data sheet. Choices: ., ,. Used for interpreting your data. Only change if data is not displaying on the chart as expected. Flourish type hint: string, defaults to `NULL`  
`chart_number_localization_output_separators`| Number format to display. Choices: ,., .,, ., ,, ., ,. How the numbers should appear on chart labels. Flourish type hint: string, defaults to `NULL`  
`external_write_enabled`| Store result data externally. Flourish type hint: boolean, defaults to `NULL`  
`external_write_endpoint`| Storage endpoint. Your external database, store, API or web app endpoint to post data to. If you were to use Google Sheets to store your data, please check the External write docs for integration help. Flourish type hint: string, defaults to `NULL`  
`chart_layout_body_font`| Main font. This font will apply to the whole graphic by default. You can optionally change the font for the title, subtitle, footer, etc in the Header and Footer settings panels. Flourish type hint: font, defaults to `NULL`  
`chart_layout_font_color`| Text color. This color will apply to the whole graphic by default, You can optionally change the color for individual text elements, in other settings panels. Flourish type hint: color, defaults to `NULL`  
`chart_layout_background_color_enabled`| Color. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_background_image_enabled`| Image. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_background_color`| Background color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_background_image_src`| Image URL. Flourish type hint: url, defaults to `NULL`  
`chart_layout_background_image_size`| Size. Choices: cover, contain, auto, 100% 100%. Flourish type hint: string, defaults to `NULL`  
`chart_layout_background_image_position`| Position. Choices: top left, top center, top right, center left, center center, center right, bottom left, bottom center, bottom right. Flourish type hint: string, defaults to `NULL`  
`chart_layout_max_width_target`| Maximum width. Choices: none, wrapper, primary. Apply a maximum width to just the main graphic or everything (main graphic plus header, footer, etc). Flourish type hint: string, defaults to `NULL`  
`chart_layout_max_width`| Maximum width. Leave blank to stretch to container width. Flourish type hint: number, defaults to `NULL`  
`chart_layout_max_width_align`| Align. Choices: left, center, right. Flourish type hint: string, defaults to `NULL`  
`chart_layout_layout_order`| Layout order. Flourish type hint: string, defaults to `NULL`  
`chart_layout_space_between_sections`| Space between sections. Choices: 0.5, 1, 1.5, custom. Flourish type hint: string, defaults to `NULL`  
`chart_layout_space_between_sections_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`chart_layout_margin_top`| Top. Flourish type hint: number, defaults to `NULL`  
`chart_layout_margin_right`| Right. Flourish type hint: number, defaults to `NULL`  
`chart_layout_margin_bottom`| Bottom. Flourish type hint: number, defaults to `NULL`  
`chart_layout_margin_left`| Left. Flourish type hint: number, defaults to `NULL`  
`chart_layout_border_enabled`| Show borders around visualisation. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_border_top_width`| Top. Flourish type hint: number, defaults to `NULL`  
`chart_layout_border_top_style`| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`chart_layout_border_top_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_border_right_width`| Right. Flourish type hint: number, defaults to `NULL`  
`chart_layout_border_right_style`| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`chart_layout_border_right_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_border_bottom_width`| Bottom. Flourish type hint: number, defaults to `NULL`  
`chart_layout_border_bottom_style`| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`chart_layout_border_bottom_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_border_left_width`| Left. Flourish type hint: number, defaults to `NULL`  
`chart_layout_border_left_style`| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`chart_layout_border_left_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_read_direction`| Read direction. Choices: ltr, rtl. This will change the reading direction of the main text elements on the page. Its not possible to adjust this on all elements, such as axes. Note that when direction is set to right to left any alignment icons will be reversed. Flourish type hint: string, defaults to `NULL`  
`chart_layout_font_size_mobile_small`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_font_size_mobile_big`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_font_size_tablet`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_font_size_desktop`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_font_size_big_screen`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_breakpoint_mobile_small`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_breakpoint_mobile_big`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_breakpoint_tablet`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_breakpoint_desktop`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_breakpoint_big_screen`| Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_align`| Alignment. Choices: left, center, right. Flourish type hint: string, defaults to `NULL`  
`chart_layout_title`| Flourish type hint: html, defaults to `NULL`  
`chart_layout_title_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_title_font`| Title Font. Flourish type hint: font, defaults to `NULL`  
`chart_layout_title_size`| Size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to `NULL`  
`chart_layout_title_size_custom`| Custom. Specify a custom responsive font size in rems The best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`chart_layout_title_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_layout_title_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_title_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`chart_layout_title_space_above`| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to `NULL`  
`chart_layout_title_space_above_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`chart_layout_subtitle`| Flourish type hint: html, defaults to `NULL`  
`chart_layout_subtitle_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_subtitle_font`| Subtitle Font. Flourish type hint: font, defaults to `NULL`  
`chart_layout_subtitle_size`| Size. Choices: 1.4, 1.6, 2, custom. Flourish type hint: string, defaults to `NULL`  
`chart_layout_subtitle_size_custom`| Custom. Specify a custom responsive font size in rems The best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`chart_layout_subtitle_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_layout_subtitle_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_subtitle_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`chart_layout_subtitle_space_above`| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to `NULL`  
`chart_layout_subtitle_space_above_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_text`| Flourish type hint: html, defaults to `NULL`  
`chart_layout_header_text_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_header_text_size`| Size. Choices: 1.2, 1.4, 1.6, custom. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_text_size_custom`| Custom. Specify a custom responsive font size in rems The best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_text_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_text_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_header_text_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_text_space_above`| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_text_space_above_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_border`| Choices: top, bottom, top_and_bottom, none. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_border_width`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_border_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_header_border_style`| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_border_space`| Space. Space between border and header text. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_logo_enabled`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_header_logo_src`| Image. Flourish type hint: url, defaults to `NULL`  
`chart_layout_header_logo_alt`| Alt text. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_logo_link_url`| Link. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_logo_height`| Height. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_logo_align`| Align. Choices: inside, outside. Align logo inside either the header or the main visualization container. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_logo_position_inside`| Position. Choices: top, left, right. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_logo_position_outside`| Position. Choices: left, right. Flourish type hint: string, defaults to `NULL`  
`chart_layout_header_logo_margin_top`| Top. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_logo_margin_right`| Right. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_logo_margin_bottom`| Bottom. Flourish type hint: number, defaults to `NULL`  
`chart_layout_header_logo_margin_left`| Left. Flourish type hint: number, defaults to `NULL`  
`chart_layout_footer_align`| Alignment. Choices: left, center, right, justify. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_text_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_layout_footer_text_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_footer_styling`| Advanced footer styles. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_footer_font`| Font. Flourish type hint: font, defaults to `NULL`  
`chart_layout_footer_text_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_layout_source_name`| Source name. Flourish type hint: string, defaults to `NULL`  
`chart_layout_source_url`| Source url. Flourish type hint: string, defaults to `NULL`  
`chart_layout_multiple_sources`| Multiple sources. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_source_name_2`| Source name. Flourish type hint: string, defaults to `NULL`  
`chart_layout_source_url_2`| Source url. Flourish type hint: string, defaults to `NULL`  
`chart_layout_source_name_3`| Source name. Flourish type hint: string, defaults to `NULL`  
`chart_layout_source_url_3`| Source url. Flourish type hint: string, defaults to `NULL`  
`chart_layout_source_label`| Source label. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_note`| Note. To add the time/date stamp of when the data was last updated add `{{data_last_updated}}`. For example, "Last updated at `{{data_last_updated}}`". To customize the format, use the advanced options below. Flourish type hint: html, defaults to `NULL`  
`chart_layout_footer_note_secondary`| Note (secondary). The secondary note is placed below the source and primary note. To add the time/date stamp of when the data was last updated add `{{data_last_updated}}`. For example, "Last updated at `{{data_last_updated}}`". To customize the format, use the advanced options below. Flourish type hint: html, defaults to `NULL`  
`chart_layout_advanced_note_styling`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_footer_timestamp_format`| Time/date stamp formatting. Choices: %H:%M:%S, %I:%M %p, %H:%M, %H:%M %p, %H:%M:%S, %d %b %Y, %H:%M, %d %b %Y, %H:%M, %d/%m/%Y, %H:%M, %m/%d/%Y, %H:%M, %d-%m-%Y, %H:%M, %m-%d-%Y, %d %b %Y, %m/%d/%Y, %d/%m/%Y, %m-%d-%Y, %d-%m-%Y, %Y-%m-%d, %Y-%m-%d %H:%M:%S. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_logo_enabled`| Image. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_layout_footer_logo_src`| Image. Flourish type hint: url, defaults to `NULL`  
`chart_layout_footer_logo_src_light`| Image (light version). If provided this version will be used whenever the background color is dark. Flourish type hint: hidden, defaults to `NULL`  
`chart_layout_footer_logo_alt`| Alt text. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_logo_link_url`| Link. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_logo_height`| Height. Flourish type hint: number, defaults to `NULL`  
`chart_layout_footer_logo_margin`| Margin. Flourish type hint: number, defaults to `NULL`  
`chart_layout_footer_logo_order`| Position. Choices: left, right. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_align_vertical`| V. align. Choices: flex-start, center, flex-end. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_border`| Choices: top, bottom, top_and_bottom, none. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_border_width`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_layout_footer_border_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_layout_footer_border_style`| Style. Choices: solid, dashed, dotted. Flourish type hint: string, defaults to `NULL`  
`chart_layout_footer_border_space`| Space. Space between border and footer text. Flourish type hint: number, defaults to `NULL`  
`chart_layout_screenreader_text_primary`| Screenreader description. A text alternative to the visual content that will only be visible to screenreaders, e.g. The line chart shows China consistently higher than the other countries since 1990. Do not replicate your title, since that will also be read by screenreaders. Flourish type hint: text, defaults to `NULL`  
`chart_layout_screenreader_label`| Screenreader label. A short text label given to the main Flourish embed wrapper to provide an accessible name that is only visible to screenreaders Added in the form of an "aria-label". Flourish type hint: string, defaults to `NULL`  
`chart_layout_screenreader_hide_primary`| Screenreader mode for main visual container. Choices: `TRUE`, `FALSE`. Whether the main visual container is visible to screenreaders (Text in the header and footer are always available to screenreaders.). Flourish type hint: boolean, defaults to `NULL`
