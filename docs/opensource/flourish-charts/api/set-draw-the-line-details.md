---
url: https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/
title: Set draw the line chart chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:23.592403+00:00
---

# Set draw the line chart chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set draw the line chart chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_draw_the_line_details(
    
        self,
    
        guess_lines_start: float = None,
    
        guess_lines_width: float = None,
    
        guess_lines_dot_radius: float = None,
    
        guess_lines_dash: float = None,
    
        fixed_lines_width: float = None,
    
        fixed_lines_dot_radius: float = None,
    
        line_curve: str = None,
    
        guess_lines_panel_position: str = None,
    
        message_styling: bool = None,
    
        message_background: str = None,
    
        message_opacity: float = None,
    
        message_color: str = None,
    
        message_font_size: float = None,
    
        message_border: str = None,
    
        message_border_width: float = None,
    
        message_border_radius: float = None,
    
        message_shadow: bool = None,
    
        guess_lines_message_text: str = None,
    
        scores_3_min: float = None,
    
        scores_3_text: str = None,
    
        scores_2_min: float = None,
    
        scores_2_text: str = None,
    
        scores_1_min: float = None,
    
        scores_1_text: str = None,
    
        scores_0_text: str = None,
    
        guess_lines_submit_text: str = None,
    
        submit_styling: bool = None,
    
        submit_background: str = None,
    
        submit_opacity: float = None,
    
        submit_color: str = None,
    
        submit_font_size: float = None,
    
        submit_border: str = None,
    
        submit_border_width: float = None,
    
        submit_border_radius: float = None,
    
        submit_shadow: bool = None,
    
        chart_color_scale_categorical_palette: Union[list, str] = None,
    
        chart_color_scale_categorical_extend: bool = None,
    
        chart_color_scale_categorical_custom_palette: Union[list, str] = None,
    
        chart_color_scale_numeric_type: str = None,
    
        chart_color_scale_binning: bool = None,
    
        chart_color_scale_bin_mode: str = None,
    
        chart_color_scale_bin_count: float = None,
    
        chart_color_scale_bin_thresholds: str = None,
    
        chart_color_scale_sequential_palette: str = None,
    
        chart_color_scale_sequential_reverse: bool = None,
    
        chart_color_scale_sequential_custom_min: str = None,
    
        chart_color_scale_sequential_custom_max: str = None,
    
        chart_color_scale_sequential_color_space: str = None,
    
        chart_color_scale_sequential_custom_domain: bool = None,
    
        chart_color_scale_sequential_domain_min: float = None,
    
        chart_color_scale_sequential_domain_max: float = None,
    
        chart_color_scale_diverging_palette: str = None,
    
        chart_color_scale_diverging_reverse: bool = None,
    
        chart_color_scale_diverging_custom_min: str = None,
    
        chart_color_scale_diverging_custom_mid: str = None,
    
        chart_color_scale_diverging_custom_max: str = None,
    
        chart_color_scale_diverging_color_space: str = None,
    
        chart_color_scale_diverging_custom_domain: bool = None,
    
        chart_color_scale_diverging_domain_min: float = None,
    
        chart_color_scale_diverging_domain_mid: float = None,
    
        chart_color_scale_diverging_domain_max: float = None,
    
        chart_categorical_legend_show_legend: bool = None,
    
        chart_categorical_legend_title_mode: str = None,
    
        chart_categorical_legend_title: str = None,
    
        chart_categorical_legend_swatch_width: float = None,
    
        chart_categorical_legend_swatch_height: float = None,
    
        chart_categorical_legend_swatch_radius: float = None,
    
        chart_categorical_legend_legend_items_padding: float = None,
    
        chart_categorical_legend_swatch_outline: bool = None,
    
        chart_categorical_legend_swatch_outline_color: str = None,
    
        chart_categorical_legend_order_override: Union[list, str] = None,
    
        chart_categorical_legend_icon_height: float = None,
    
        chart_categorical_legend_icon_color: str = None,
    
        chart_categorical_legend_max_width: float = None,
    
        chart_categorical_legend_orientation: str = None,
    
        chart_legend_container_alignment: str = None,
    
        chart_legend_container_orientation: str = None,
    
        chart_legend_container_title_weight: str = None,
    
        chart_legend_container_text_weight: str = None,
    
        chart_legend_container_text_color: str = None,
    
        chart_legend_container_text_size: float = None,
    
        chart_x_axis_axis_position: str = None,
    
        chart_x_axis_y_axis_position: str = None,
    
        chart_x_axis_numeric_scale_type: str = None,
    
        chart_x_axis_linear_min: float = None,
    
        chart_x_axis_linear_max: float = None,
    
        chart_x_axis_log_min: float = None,
    
        chart_x_axis_log_max: float = None,
    
        chart_x_axis_datetime_min: str = None,
    
        chart_x_axis_datetime_max: str = None,
    
        chart_x_axis_flip: bool = None,
    
        chart_x_axis_show_scale_settings: bool = None,
    
        chart_x_axis_nice: bool = None,
    
        chart_x_axis_zero_axis: str = None,
    
        chart_x_axis_title_mode: str = None,
    
        chart_x_axis_title: str = None,
    
        chart_x_axis_title_styling: bool = None,
    
        chart_x_axis_title_weight: str = None,
    
        chart_x_axis_title_color: str = None,
    
        chart_x_axis_title_size: float = None,
    
        chart_x_axis_title_padding: float = None,
    
        chart_x_axis_tick_label_position: str = None,
    
        chart_x_axis_tick_label_styling: bool = None,
    
        chart_x_axis_tick_label_size: float = None,
    
        chart_x_axis_tick_label_color: str = None,
    
        chart_x_axis_tick_padding: float = None,
    
        chart_x_axis_tick_label_angle: str = None,
    
        chart_x_axis_tick_label_weight: str = None,
    
        chart_x_axis_tick_label_max_lines: float = None,
    
        chart_x_axis_tick_label_line_height: float = None,
    
        chart_x_axis_tick_label_space_mode: str = None,
    
        chart_x_axis_tick_label_space: float = None,
    
        chart_x_axis_tick_mode: str = None,
    
        chart_x_axis_tick_number: float = None,
    
        chart_x_axis_tick_custom: Union[list, str] = None,
    
        chart_x_axis_line_and_tick_color: str = None,
    
        chart_x_axis_line_and_tick_width: float = None,
    
        chart_x_axis_tick_length: float = None,
    
        chart_x_axis_tick_side: str = None,
    
        chart_x_axis_line_visible: bool = None,
    
        chart_x_axis_edge_padding: float = None,
    
        chart_x_axis_gridlines_visible: bool = None,
    
        chart_x_axis_gridlines_styling: bool = None,
    
        chart_x_axis_gridline_color: str = None,
    
        chart_x_axis_gridline_style: str = None,
    
        chart_x_axis_gridline_width: float = None,
    
        chart_x_axis_gridline_category_dividers: bool = None,
    
        chart_x_axis_gridline_category_dividers_extend: bool = None,
    
        chart_y_axis_axis_visible: bool = None,
    
        chart_y_axis_numeric_scale_type: str = None,
    
        chart_y_axis_linear_min: float = None,
    
        chart_y_axis_linear_max: float = None,
    
        chart_y_axis_log_min: float = None,
    
        chart_y_axis_log_max: float = None,
    
        chart_y_axis_datetime_min: str = None,
    
        chart_y_axis_datetime_max: str = None,
    
        chart_y_axis_flip: bool = None,
    
        chart_y_axis_show_scale_settings: bool = None,
    
        chart_y_axis_nice: bool = None,
    
        chart_y_axis_zero_axis: str = None,
    
        chart_y_axis_title_mode: str = None,
    
        chart_y_axis_title: str = None,
    
        chart_y_axis_title_styling: bool = None,
    
        chart_y_axis_title_position: str = None,
    
        chart_y_axis_title_weight: str = None,
    
        chart_y_axis_title_color: str = None,
    
        chart_y_axis_title_size: float = None,
    
        chart_y_axis_title_padding: float = None,
    
        chart_y_axis_tick_label_position: str = None,
    
        chart_y_axis_tick_label_styling: bool = None,
    
        chart_y_axis_tick_label_size: float = None,
    
        chart_y_axis_tick_label_color: str = None,
    
        chart_y_axis_tick_padding: float = None,
    
        chart_y_axis_tick_label_angle: str = None,
    
        chart_y_axis_tick_label_weight: str = None,
    
        chart_y_axis_tick_label_max_lines: float = None,
    
        chart_y_axis_tick_label_line_height: float = None,
    
        chart_y_axis_tick_label_space_mode: str = None,
    
        chart_y_axis_tick_label_space: float = None,
    
        chart_y_axis_tick_mode: str = None,
    
        chart_y_axis_tick_number: float = None,
    
        chart_y_axis_tick_custom: Union[list, str] = None,
    
        chart_y_axis_line_and_tick_color: str = None,
    
        chart_y_axis_line_and_tick_width: float = None,
    
        chart_y_axis_tick_length: float = None,
    
        chart_y_axis_tick_side: str = None,
    
        chart_y_axis_line_visible: bool = None,
    
        chart_y_axis_edge_padding: float = None,
    
        chart_y_axis_gridlines_visible: bool = None,
    
        chart_y_axis_gridlines_styling: bool = None,
    
        chart_y_axis_gridline_color: str = None,
    
        chart_y_axis_gridline_style: str = None,
    
        chart_y_axis_gridline_width: float = None,
    
        chart_y_axis_gridline_category_dividers: bool = None,
    
        chart_y_axis_gridline_category_dividers_extend: bool = None,
    
        chart_background_background_color_enabled: bool = None,
    
        chart_background_background_image_enabled: bool = None,
    
        chart_background_background_color: str = None,
    
        chart_background_background_image_src: str = None,
    
        chart_background_background_image_size: str = None,
    
        chart_background_background_image_position: str = None,
    
        datetime_input_format: str = None,
    
        date_format: str = None,
    
        chart_number_localization_input_decimal_separator: str = None,
    
        chart_number_localization_output_separators: str = None,
    
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
    
    
    set_draw_the_line_details(
    
        .,
    
        guess_lines_start = NULL,
    
        guess_lines_width = NULL,
    
        guess_lines_dot_radius = NULL,
    
        guess_lines_dash = NULL,
    
        fixed_lines_width = NULL,
    
        fixed_lines_dot_radius = NULL,
    
        line_curve = NULL,
    
        guess_lines_panel_position = NULL,
    
        message_styling = NULL,
    
        message_background = NULL,
    
        message_opacity = NULL,
    
        message_color = NULL,
    
        message_font_size = NULL,
    
        message_border = NULL,
    
        message_border_width = NULL,
    
        message_border_radius = NULL,
    
        message_shadow = NULL,
    
        guess_lines_message_text = NULL,
    
        scores_3_min = NULL,
    
        scores_3_text = NULL,
    
        scores_2_min = NULL,
    
        scores_2_text = NULL,
    
        scores_1_min = NULL,
    
        scores_1_text = NULL,
    
        scores_0_text = NULL,
    
        guess_lines_submit_text = NULL,
    
        submit_styling = NULL,
    
        submit_background = NULL,
    
        submit_opacity = NULL,
    
        submit_color = NULL,
    
        submit_font_size = NULL,
    
        submit_border = NULL,
    
        submit_border_width = NULL,
    
        submit_border_radius = NULL,
    
        submit_shadow = NULL,
    
        chart_color_scale_categorical_palette = NULL,
    
        chart_color_scale_categorical_extend = NULL,
    
        chart_color_scale_categorical_custom_palette = NULL,
    
        chart_color_scale_numeric_type = NULL,
    
        chart_color_scale_binning = NULL,
    
        chart_color_scale_bin_mode = NULL,
    
        chart_color_scale_bin_count = NULL,
    
        chart_color_scale_bin_thresholds = NULL,
    
        chart_color_scale_sequential_palette = NULL,
    
        chart_color_scale_sequential_reverse = NULL,
    
        chart_color_scale_sequential_custom_min = NULL,
    
        chart_color_scale_sequential_custom_max = NULL,
    
        chart_color_scale_sequential_color_space = NULL,
    
        chart_color_scale_sequential_custom_domain = NULL,
    
        chart_color_scale_sequential_domain_min = NULL,
    
        chart_color_scale_sequential_domain_max = NULL,
    
        chart_color_scale_diverging_palette = NULL,
    
        chart_color_scale_diverging_reverse = NULL,
    
        chart_color_scale_diverging_custom_min = NULL,
    
        chart_color_scale_diverging_custom_mid = NULL,
    
        chart_color_scale_diverging_custom_max = NULL,
    
        chart_color_scale_diverging_color_space = NULL,
    
        chart_color_scale_diverging_custom_domain = NULL,
    
        chart_color_scale_diverging_domain_min = NULL,
    
        chart_color_scale_diverging_domain_mid = NULL,
    
        chart_color_scale_diverging_domain_max = NULL,
    
        chart_categorical_legend_show_legend = NULL,
    
        chart_categorical_legend_title_mode = NULL,
    
        chart_categorical_legend_title = NULL,
    
        chart_categorical_legend_swatch_width = NULL,
    
        chart_categorical_legend_swatch_height = NULL,
    
        chart_categorical_legend_swatch_radius = NULL,
    
        chart_categorical_legend_legend_items_padding = NULL,
    
        chart_categorical_legend_swatch_outline = NULL,
    
        chart_categorical_legend_swatch_outline_color = NULL,
    
        chart_categorical_legend_order_override = NULL,
    
        chart_categorical_legend_icon_height = NULL,
    
        chart_categorical_legend_icon_color = NULL,
    
        chart_categorical_legend_max_width = NULL,
    
        chart_categorical_legend_orientation = NULL,
    
        chart_legend_container_alignment = NULL,
    
        chart_legend_container_orientation = NULL,
    
        chart_legend_container_title_weight = NULL,
    
        chart_legend_container_text_weight = NULL,
    
        chart_legend_container_text_color = NULL,
    
        chart_legend_container_text_size = NULL,
    
        chart_x_axis_axis_position = NULL,
    
        chart_x_axis_y_axis_position = NULL,
    
        chart_x_axis_numeric_scale_type = NULL,
    
        chart_x_axis_linear_min = NULL,
    
        chart_x_axis_linear_max = NULL,
    
        chart_x_axis_log_min = NULL,
    
        chart_x_axis_log_max = NULL,
    
        chart_x_axis_datetime_min = NULL,
    
        chart_x_axis_datetime_max = NULL,
    
        chart_x_axis_flip = NULL,
    
        chart_x_axis_show_scale_settings = NULL,
    
        chart_x_axis_nice = NULL,
    
        chart_x_axis_zero_axis = NULL,
    
        chart_x_axis_title_mode = NULL,
    
        chart_x_axis_title = NULL,
    
        chart_x_axis_title_styling = NULL,
    
        chart_x_axis_title_weight = NULL,
    
        chart_x_axis_title_color = NULL,
    
        chart_x_axis_title_size = NULL,
    
        chart_x_axis_title_padding = NULL,
    
        chart_x_axis_tick_label_position = NULL,
    
        chart_x_axis_tick_label_styling = NULL,
    
        chart_x_axis_tick_label_size = NULL,
    
        chart_x_axis_tick_label_color = NULL,
    
        chart_x_axis_tick_padding = NULL,
    
        chart_x_axis_tick_label_angle = NULL,
    
        chart_x_axis_tick_label_weight = NULL,
    
        chart_x_axis_tick_label_max_lines = NULL,
    
        chart_x_axis_tick_label_line_height = NULL,
    
        chart_x_axis_tick_label_space_mode = NULL,
    
        chart_x_axis_tick_label_space = NULL,
    
        chart_x_axis_tick_mode = NULL,
    
        chart_x_axis_tick_number = NULL,
    
        chart_x_axis_tick_custom = NULL,
    
        chart_x_axis_line_and_tick_color = NULL,
    
        chart_x_axis_line_and_tick_width = NULL,
    
        chart_x_axis_tick_length = NULL,
    
        chart_x_axis_tick_side = NULL,
    
        chart_x_axis_line_visible = NULL,
    
        chart_x_axis_edge_padding = NULL,
    
        chart_x_axis_gridlines_visible = NULL,
    
        chart_x_axis_gridlines_styling = NULL,
    
        chart_x_axis_gridline_color = NULL,
    
        chart_x_axis_gridline_style = NULL,
    
        chart_x_axis_gridline_width = NULL,
    
        chart_x_axis_gridline_category_dividers = NULL,
    
        chart_x_axis_gridline_category_dividers_extend = NULL,
    
        chart_y_axis_axis_visible = NULL,
    
        chart_y_axis_numeric_scale_type = NULL,
    
        chart_y_axis_linear_min = NULL,
    
        chart_y_axis_linear_max = NULL,
    
        chart_y_axis_log_min = NULL,
    
        chart_y_axis_log_max = NULL,
    
        chart_y_axis_datetime_min = NULL,
    
        chart_y_axis_datetime_max = NULL,
    
        chart_y_axis_flip = NULL,
    
        chart_y_axis_show_scale_settings = NULL,
    
        chart_y_axis_nice = NULL,
    
        chart_y_axis_zero_axis = NULL,
    
        chart_y_axis_title_mode = NULL,
    
        chart_y_axis_title = NULL,
    
        chart_y_axis_title_styling = NULL,
    
        chart_y_axis_title_position = NULL,
    
        chart_y_axis_title_weight = NULL,
    
        chart_y_axis_title_color = NULL,
    
        chart_y_axis_title_size = NULL,
    
        chart_y_axis_title_padding = NULL,
    
        chart_y_axis_tick_label_position = NULL,
    
        chart_y_axis_tick_label_styling = NULL,
    
        chart_y_axis_tick_label_size = NULL,
    
        chart_y_axis_tick_label_color = NULL,
    
        chart_y_axis_tick_padding = NULL,
    
        chart_y_axis_tick_label_angle = NULL,
    
        chart_y_axis_tick_label_weight = NULL,
    
        chart_y_axis_tick_label_max_lines = NULL,
    
        chart_y_axis_tick_label_line_height = NULL,
    
        chart_y_axis_tick_label_space_mode = NULL,
    
        chart_y_axis_tick_label_space = NULL,
    
        chart_y_axis_tick_mode = NULL,
    
        chart_y_axis_tick_number = NULL,
    
        chart_y_axis_tick_custom = NULL,
    
        chart_y_axis_line_and_tick_color = NULL,
    
        chart_y_axis_line_and_tick_width = NULL,
    
        chart_y_axis_tick_length = NULL,
    
        chart_y_axis_tick_side = NULL,
    
        chart_y_axis_line_visible = NULL,
    
        chart_y_axis_edge_padding = NULL,
    
        chart_y_axis_gridlines_visible = NULL,
    
        chart_y_axis_gridlines_styling = NULL,
    
        chart_y_axis_gridline_color = NULL,
    
        chart_y_axis_gridline_style = NULL,
    
        chart_y_axis_gridline_width = NULL,
    
        chart_y_axis_gridline_category_dividers = NULL,
    
        chart_y_axis_gridline_category_dividers_extend = NULL,
    
        chart_background_background_color_enabled = NULL,
    
        chart_background_background_image_enabled = NULL,
    
        chart_background_background_color = NULL,
    
        chart_background_background_image_src = NULL,
    
        chart_background_background_image_size = NULL,
    
        chart_background_background_image_position = NULL,
    
        datetime_input_format = NULL,
    
        date_format = NULL,
    
        chart_number_localization_input_decimal_separator = NULL,
    
        chart_number_localization_output_separators = NULL,
    
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
`guess_lines_start`| `float`, optional| Percent to reveal. What percentage of the line to show before a user starts drawing. Flourish type hint: number, defaults to None  
`guess_lines_width`| `float`, optional| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`guess_lines_dot_radius`| `float`, optional| Dot radius. Flourish type hint: number, defaults to None  
`guess_lines_dash`| `float`, optional| Drawing dash size. Only applies to the drawn section of the line. Set to zero for a solid line. Flourish type hint: number, defaults to None  
`fixed_lines_width`| `float`, optional| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`fixed_lines_dot_radius`| `float`, optional| Dot radius. Flourish type hint: number, defaults to None  
`line_curve`| `str`, optional| Live curve. Choices: linear, step, curve. Flourish type hint: string, defaults to None  
`guess_lines_panel_position`| `str`, optional| Position. Choices: top, middle, bottom. Flourish type hint: string, defaults to None  
`message_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`message_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`message_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`message_color`| `str`, optional| Font color. Flourish type hint: color, defaults to None  
`message_font_size`| `float`, optional| Font size. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`message_border`| `str`, optional| Border color. Flourish type hint: color, defaults to None  
`message_border_width`| `float`, optional| Border width. In pixels. Flourish type hint: number, defaults to None  
`message_border_radius`| `float`, optional| Border radius. In rems, a multiple of the panels font size. Flourish type hint: number, defaults to None  
`message_shadow`| `bool`, optional| Drop shadow. Flourish type hint: boolean, defaults to None  
`guess_lines_message_text`| `str`, optional| Text. Include `{{LINE}}` to show the lines name, in color. Flourish type hint: string, defaults to None  
`scores_3_min`| `float`, optional| % error. Specified as the maximum percentage error allowed, relative to the total Y axis. Flourish type hint: number, defaults to None  
`scores_3_text`| `str`, optional| Text. Use `{{DIFF}}` to show the average gap from the users guess to the real data point. Flourish type hint: string, defaults to None  
`scores_2_min`| `float`, optional| % error. Specified as the maximum percentage error allowed, relative to the total Y axis. Flourish type hint: number, defaults to None  
`scores_2_text`| `str`, optional| Text. Flourish type hint: string, defaults to None  
`scores_1_min`| `float`, optional| % error. Specified as the maximum percentage error allowed, relative to the total Y axis. Flourish type hint: number, defaults to None  
`scores_1_text`| `str`, optional| Text. Flourish type hint: string, defaults to None  
`scores_0_text`| `str`, optional| Text. Flourish type hint: string, defaults to None  
`guess_lines_submit_text`| `str`, optional| Text. In rems, a multiple of the pages base font size. Flourish type hint: string, defaults to None  
`submit_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`submit_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`submit_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`submit_color`| `str`, optional| Font color. Flourish type hint: color, defaults to None  
`submit_font_size`| `float`, optional| Font size. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`submit_border`| `str`, optional| Border colour. Flourish type hint: color, defaults to None  
`submit_border_width`| `float`, optional| Border width. In pixels. Flourish type hint: number, defaults to None  
`submit_border_radius`| `float`, optional| Border radius. In ems a multiple of the panels font size. Flourish type hint: number, defaults to None  
`submit_shadow`| `bool`, optional| Drop shadow. Flourish type hint: boolean, defaults to None  
`chart_color_scale_categorical_palette`| `Union[list, str]`, optional| Palette. Flourish type hint: colors, defaults to None  
`chart_color_scale_categorical_extend`| `bool`, optional| Extend. Automatically generate additional colours when needed to avoid the palette colours being used more than once. Flourish type hint: boolean, defaults to None  
`chart_color_scale_categorical_custom_palette`| `Union[list, str]`, optional| Custom overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to None  
`chart_color_scale_numeric_type`| `str`, optional| Scale type. Choices: sequential, diverging. Flourish type hint: string, defaults to None  
`chart_color_scale_binning`| `bool`, optional| Choices: False, True. In linear mode, the color scale will run as a smooth gradient between 2 colors. In binned mode, the gradient will be divided in smaller blocks. Flourish type hint: boolean, defaults to None  
`chart_color_scale_bin_mode`| `str`, optional| Binning mode. Choices: fixed, quantile, custom. Flourish type hint: string, defaults to None  
`chart_color_scale_bin_count`| `float`, optional| Number of bins. Flourish type hint: number, defaults to None  
`chart_color_scale_bin_thresholds`| `str`, optional| Custom thresholds. Enter your desired thresholds, separating them with a ";". For instance, "5;10;15". Bins form as follows: From the datas minimum value (domain minimum) up to the first threshold. Between consecutive thresholds. From the last threshold to the datas maximum value (domain maximum). For "5;10;15", youll get four bins based on your datas range. Flourish type hint: string, defaults to None  
`chart_color_scale_sequential_palette`| `str`, optional| Palette. Flourish type hint: string, defaults to None  
`chart_color_scale_sequential_reverse`| `bool`, optional| Reverse. Flourish type hint: boolean, defaults to None  
`chart_color_scale_sequential_custom_min`| `str`, optional| Minimum color. Flourish type hint: color, defaults to None  
`chart_color_scale_sequential_custom_max`| `str`, optional| Maximum color. Flourish type hint: color, defaults to None  
`chart_color_scale_sequential_color_space`| `str`, optional| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to None  
`chart_color_scale_sequential_custom_domain`| `bool`, optional| Domain. Choices: False, True. Flourish type hint: boolean, defaults to None  
`chart_color_scale_sequential_domain_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_color_scale_sequential_domain_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_color_scale_diverging_palette`| `str`, optional| Palette. Flourish type hint: string, defaults to None  
`chart_color_scale_diverging_reverse`| `bool`, optional| Reverse. Flourish type hint: boolean, defaults to None  
`chart_color_scale_diverging_custom_min`| `str`, optional| Minimum color. Flourish type hint: color, defaults to None  
`chart_color_scale_diverging_custom_mid`| `str`, optional| Midpoint color. Flourish type hint: color, defaults to None  
`chart_color_scale_diverging_custom_max`| `str`, optional| Maximum color. Flourish type hint: color, defaults to None  
`chart_color_scale_diverging_color_space`| `str`, optional| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to None  
`chart_color_scale_diverging_custom_domain`| `bool`, optional| Domain. Choices: False, True. Flourish type hint: boolean, defaults to None  
`chart_color_scale_diverging_domain_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_color_scale_diverging_domain_mid`| `float`, optional| Mid. Flourish type hint: number, defaults to None  
`chart_color_scale_diverging_domain_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_categorical_legend_show_legend`| `bool`, optional| Legend mode. Choices: True, False. A legend will not show with a single entry. Flourish type hint: boolean, defaults to None  
`chart_categorical_legend_title_mode`| `str`, optional| Title mode. Choices: auto, custom. Flourish type hint: string, defaults to None  
`chart_categorical_legend_title`| `str`, optional| Title. Flourish type hint: string, defaults to None  
`chart_categorical_legend_swatch_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_categorical_legend_swatch_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`chart_categorical_legend_swatch_radius`| `float`, optional| Roundness. The radius of the corners of the swatch (in pixels). Flourish type hint: number, defaults to None  
`chart_categorical_legend_legend_items_padding`| `float`, optional| Padding. Padding between legend items ( in rems ). Flourish type hint: number, defaults to None  
`chart_categorical_legend_swatch_outline`| `bool`, optional| Outline. An optional outline for the swatch in the legend. Flourish type hint: boolean, defaults to None  
`chart_categorical_legend_swatch_outline_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_categorical_legend_order_override`| `Union[list, str]`, optional| Custom order override. Manually specify the order of legend entries (one entry per line). Flourish type hint: text, defaults to None  
`chart_categorical_legend_icon_height`| `float`, optional| Height. Height of icon ( in rems ). Flourish type hint: number, defaults to None  
`chart_categorical_legend_icon_color`| `str`, optional| Color. Fallback color (icon color if not determined by template). Flourish type hint: color, defaults to None  
`chart_categorical_legend_max_width`| `float`, optional| Max width. Flourish type hint: number, defaults to None  
`chart_categorical_legend_orientation`| `str`, optional| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to None  
`chart_legend_container_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`chart_legend_container_orientation`| `str`, optional| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to None  
`chart_legend_container_title_weight`| `str`, optional| Title weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_legend_container_text_weight`| `str`, optional| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_legend_container_text_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_legend_container_text_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_x_axis_axis_position`| `str`, optional| Position. Choices: bottom, float-below, float-above, top, off. Flourish type hint: string, defaults to None  
`chart_x_axis_y_axis_position`| `str`, optional| Y value. Vertical position of the X axis on the Y scale. Flourish type hint: string, defaults to None  
`chart_x_axis_numeric_scale_type`| `str`, optional| Type. Choices: linear, log. Flourish type hint: string, defaults to None  
`chart_x_axis_linear_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_x_axis_linear_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_x_axis_log_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_x_axis_log_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_x_axis_datetime_min`| `str`, optional| Min (date). Flourish type hint: string, defaults to None  
`chart_x_axis_datetime_max`| `str`, optional| Max (date). Flourish type hint: string, defaults to None  
`chart_x_axis_flip`| `bool`, optional| Flip axis. Flourish type hint: boolean, defaults to None  
`chart_x_axis_show_scale_settings`| `bool`, optional| Configure default min/max. Flourish type hint: boolean, defaults to None  
`chart_x_axis_nice`| `bool`, optional| Round min/max. Choices: True, False. Enabling this option rounds the X axis start and end values to tidy numbers, such as 0, 50, 100 or whole years. Specified min and max values will override this feature. Flourish type hint: boolean, defaults to None  
`chart_x_axis_zero_axis`| `str`, optional| Include zero. Choices: auto, on, off. Enable to extend the axis to include zero, even when data is all positive or all negative. This is ignored if you set specific min and max scale values. Flourish type hint: string, defaults to None  
`chart_x_axis_title_mode`| `str`, optional| Type. Choices: auto, custom. Flourish type hint: string, defaults to None  
`chart_x_axis_title`| `str`, optional| Text. Flourish type hint: string, defaults to None  
`chart_x_axis_title_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_x_axis_title_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_x_axis_title_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_x_axis_title_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_x_axis_title_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_label_position`| `str`, optional| Position. Choices: default, left, right. Flourish type hint: string, defaults to None  
`chart_x_axis_tick_label_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_x_axis_tick_label_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_label_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_x_axis_tick_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_label_angle`| `str`, optional| Angle. Choices: 0, 30, 45, 60, 90. Flourish type hint: string, defaults to None  
`chart_x_axis_tick_label_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_x_axis_tick_label_max_lines`| `float`, optional| Max lines. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_label_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_label_space_mode`| `str`, optional| Space mode. Choices: auto, max, fixed. Flourish type hint: string, defaults to None  
`chart_x_axis_tick_label_space`| `float`, optional| Space. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_mode`| `str`, optional| Mode. Choices: auto, number, custom. Sets the method for selecting tick values on the axis: Auto automatically selects the ticks Number allows you to choose the number of ticks to display. Custom lets you select specific ticks to show. Note: If the axis is categorical, Number mode is ignored. Flourish type hint: string, defaults to None  
`chart_x_axis_tick_number`| `float`, optional| Number. Approximate number of ticks or gridlines. The actual number will depend on the range of values, chart size, etc. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_custom`| `Union[list, str]`, optional| One tick label per line. Specify the ticks to show, one per line. For dates, use the input format as specified in the datasheet. You can also use `{{FIRST}}` and `{{LAST}}` to add ticks at the minimum and maximum of the axis. For example: `{{FIRST}}` 25000 50000 75000 `{{LAST}}`. Flourish type hint: text, defaults to None  
`chart_x_axis_line_and_tick_color`| `str`, optional| Line color. Flourish type hint: color, defaults to None  
`chart_x_axis_line_and_tick_width`| `float`, optional| Line width. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_length`| `float`, optional| Tick length. Flourish type hint: number, defaults to None  
`chart_x_axis_tick_side`| `str`, optional| Tick side. Choices: out, in. Flourish type hint: string, defaults to None  
`chart_x_axis_line_visible`| `bool`, optional| Axis line. Flourish type hint: boolean, defaults to None  
`chart_x_axis_edge_padding`| `float`, optional| Edge padding (%). Space between start/end of axis line and first/last category tick as a percentage of the spacing between ticks. Flourish type hint: number, defaults to None  
`chart_x_axis_gridlines_visible`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_x_axis_gridlines_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_x_axis_gridline_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_x_axis_gridline_style`| `str`, optional| Style. Choices: solid, dash, dot, dot_dash. Flourish type hint: string, defaults to None  
`chart_x_axis_gridline_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_x_axis_gridline_category_dividers`| `bool`, optional| Put lines between categories. On a categorical axis, this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Flourish type hint: boolean, defaults to None  
`chart_x_axis_gridline_category_dividers_extend`| `bool`, optional| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to None  
`chart_y_axis_axis_visible`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_y_axis_numeric_scale_type`| `str`, optional| Type. Choices: linear, log. Flourish type hint: string, defaults to None  
`chart_y_axis_linear_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_y_axis_linear_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_y_axis_log_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_y_axis_log_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_y_axis_datetime_min`| `str`, optional| Min (date). Flourish type hint: string, defaults to None  
`chart_y_axis_datetime_max`| `str`, optional| Max (date). Flourish type hint: string, defaults to None  
`chart_y_axis_flip`| `bool`, optional| Flip axis. Flourish type hint: boolean, defaults to None  
`chart_y_axis_show_scale_settings`| `bool`, optional| Configure default min/max. Flourish type hint: boolean, defaults to None  
`chart_y_axis_nice`| `bool`, optional| Round min/max. Choices: True, False. When enabled, scales automatically extend to "nice" rounded start/end values, such as hundreds or whole years. Flourish type hint: boolean, defaults to None  
`chart_y_axis_zero_axis`| `str`, optional| Include zero. Choices: auto, on, off. Whether to extend the axis to include zero if the data values are all positive or all negative. Flourish type hint: string, defaults to None  
`chart_y_axis_title_mode`| `str`, optional| Type. Choices: auto, custom. Flourish type hint: string, defaults to None  
`chart_y_axis_title`| `str`, optional| Text. Flourish type hint: string, defaults to None  
`chart_y_axis_title_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_y_axis_title_position`| `str`, optional| Position. Choices: side, end. Flourish type hint: string, defaults to None  
`chart_y_axis_title_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_y_axis_title_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_y_axis_title_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_y_axis_title_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_label_position`| `str`, optional| Position. Choices: default, above, below. Flourish type hint: string, defaults to None  
`chart_y_axis_tick_label_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_y_axis_tick_label_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_label_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_y_axis_tick_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_label_angle`| `str`, optional| Angle. Choices: 0, 30, 45, 60, 90. Flourish type hint: string, defaults to None  
`chart_y_axis_tick_label_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_y_axis_tick_label_max_lines`| `float`, optional| Max lines. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_label_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_label_space_mode`| `str`, optional| Space mode. Choices: auto, max, fixed. Flourish type hint: string, defaults to None  
`chart_y_axis_tick_label_space`| `float`, optional| Space. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_mode`| `str`, optional| Mode. Choices: auto, number, custom. Sets the method for selecting tick values on the axis: Auto automatically selects the ticks Number allows you to choose the number of ticks to display. Custom lets you select specific ticks to show. Note: If the axis is categorical, Number mode is ignored. Flourish type hint: string, defaults to None  
`chart_y_axis_tick_number`| `float`, optional| Number. Approximate number of ticks or gridlines. The actual number will depend on the range of values, chart size, etc. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_custom`| `Union[list, str]`, optional| One tick label per line. Specify the ticks to show, one per line. For dates, use the input format as specified in the datasheet. You can also use `{{FIRST}}` and `{{LAST}}` to add ticks at the minimum and maximum of the axis. For example: `{{FIRST}}` 25000 50000 75000 `{{LAST}}`. Flourish type hint: text, defaults to None  
`chart_y_axis_line_and_tick_color`| `str`, optional| Line color. Flourish type hint: color, defaults to None  
`chart_y_axis_line_and_tick_width`| `float`, optional| Line width. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_length`| `float`, optional| Tick length. Flourish type hint: number, defaults to None  
`chart_y_axis_tick_side`| `str`, optional| Side. Choices: out, in. Flourish type hint: string, defaults to None  
`chart_y_axis_line_visible`| `bool`, optional| Axis line. Flourish type hint: boolean, defaults to None  
`chart_y_axis_edge_padding`| `float`, optional| Edge padding (%). Space between start/end of axis line and first/last category tick as a percentage of the spacing between ticks. Flourish type hint: number, defaults to None  
`chart_y_axis_gridlines_visible`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_y_axis_gridlines_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_y_axis_gridline_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_y_axis_gridline_style`| `str`, optional| Style. Choices: solid, dash, dot, dot_dash. Flourish type hint: string, defaults to None  
`chart_y_axis_gridline_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_y_axis_gridline_category_dividers`| `bool`, optional| Put lines between categories. On a categorical axis, this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Ignored for date and numeric axes. Flourish type hint: boolean, defaults to None  
`chart_y_axis_gridline_category_dividers_extend`| `bool`, optional| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to None  
`chart_background_background_color_enabled`| `bool`, optional| Color. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_background_background_image_enabled`| `bool`, optional| Image. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_background_background_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_background_background_image_src`| `str`, optional| Image URL. Flourish type hint: url, defaults to None  
`chart_background_background_image_size`| `str`, optional| Size. Choices: stretch, slice, meet. Flourish type hint: string, defaults to None  
`chart_background_background_image_position`| `str`, optional| Position. Choices: x_min_y_min, x_mid_y_min, x_max_y_min, x_max_y_mid, x_mid_y_mid, x_min_y_max, x_mid_y_max, x_max_y_max. Flourish type hint: string, defaults to None  
`datetime_input_format`| `str`, optional| Format in data sheet. Choices: auto, %Y-%m-%dT%H:%M:%S.%LZ, %Y-%m-%d, %m/%d/%Y, %d/%m/%Y, %d-%b-%y, %m/%Y, %m/%y, %b %Y, %b %y, %B %d, %d %b, %Y, %y, %B, %b, %H:%M:%S, %I:%M %p, %H:%M. The date/time format in the datasheet. Leave as Auto for Flourish to make a best guess. If it isnt in the list, you can enter a custom format using d3-time-format syntax. See NPM d3-data-format for details. Flourish type hint: string, defaults to None  
`date_format`| `str`, optional| Display format. Choices: auto, %Y-%m-%dT%H:%M:%S.%LZ, %Y-%m-%d, %m/%d/%Y, %d/%m/%Y, %d-%b-%y, %m/%Y, %m/%y, %b %Y, %b %y, %B %d, %d %b, %Y, %y, %B, %b, %A, %a, %H:%M:%S, %I:%M %p, %H:%M. The date/time format to show in the graphic. If it isnt in the list, you can enter a custom format using d3-time-format syntax. See NPM d3-data-format for details. Flourish type hint: string, defaults to None  
`chart_number_localization_input_decimal_separator`| `str`, optional| Decimal separator in data sheet. Choices: ., ,. Used for interpreting your data. Only change if data is not displaying on the chart as expected. Flourish type hint: string, defaults to None  
`chart_number_localization_output_separators`| `str`, optional| Number format to display. Choices: ,., .,, ., ,, ., ,. How the numbers should appear on chart labels. Flourish type hint: string, defaults to None  
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
`guess_lines_start`| Percent to reveal. What percentage of the line to show before a user starts drawing. Flourish type hint: number, defaults to `NULL`  
`guess_lines_width`| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`guess_lines_dot_radius`| Dot radius. Flourish type hint: number, defaults to `NULL`  
`guess_lines_dash`| Drawing dash size. Only applies to the drawn section of the line. Set to zero for a solid line. Flourish type hint: number, defaults to `NULL`  
`fixed_lines_width`| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`fixed_lines_dot_radius`| Dot radius. Flourish type hint: number, defaults to `NULL`  
`line_curve`| Live curve. Choices: linear, step, curve. Flourish type hint: string, defaults to `NULL`  
`guess_lines_panel_position`| Position. Choices: top, middle, bottom. Flourish type hint: string, defaults to `NULL`  
`message_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`message_background`| Background. Flourish type hint: color, defaults to `NULL`  
`message_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`message_color`| Font color. Flourish type hint: color, defaults to `NULL`  
`message_font_size`| Font size. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`message_border`| Border color. Flourish type hint: color, defaults to `NULL`  
`message_border_width`| Border width. In pixels. Flourish type hint: number, defaults to `NULL`  
`message_border_radius`| Border radius. In rems, a multiple of the panels font size. Flourish type hint: number, defaults to `NULL`  
`message_shadow`| Drop shadow. Flourish type hint: boolean, defaults to `NULL`  
`guess_lines_message_text`| Text. Include `{{LINE}}` to show the lines name, in color. Flourish type hint: string, defaults to `NULL`  
`scores_3_min`| % error. Specified as the maximum percentage error allowed, relative to the total Y axis. Flourish type hint: number, defaults to `NULL`  
`scores_3_text`| Text. Use `{{DIFF}}` to show the average gap from the users guess to the real data point. Flourish type hint: string, defaults to `NULL`  
`scores_2_min`| % error. Specified as the maximum percentage error allowed, relative to the total Y axis. Flourish type hint: number, defaults to `NULL`  
`scores_2_text`| Text. Flourish type hint: string, defaults to `NULL`  
`scores_1_min`| % error. Specified as the maximum percentage error allowed, relative to the total Y axis. Flourish type hint: number, defaults to `NULL`  
`scores_1_text`| Text. Flourish type hint: string, defaults to `NULL`  
`scores_0_text`| Text. Flourish type hint: string, defaults to `NULL`  
`guess_lines_submit_text`| Text. In rems, a multiple of the pages base font size. Flourish type hint: string, defaults to `NULL`  
`submit_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`submit_background`| Background. Flourish type hint: color, defaults to `NULL`  
`submit_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`submit_color`| Font color. Flourish type hint: color, defaults to `NULL`  
`submit_font_size`| Font size. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`submit_border`| Border colour. Flourish type hint: color, defaults to `NULL`  
`submit_border_width`| Border width. In pixels. Flourish type hint: number, defaults to `NULL`  
`submit_border_radius`| Border radius. In ems a multiple of the panels font size. Flourish type hint: number, defaults to `NULL`  
`submit_shadow`| Drop shadow. Flourish type hint: boolean, defaults to `NULL`  
`chart_color_scale_categorical_palette`| Palette. Flourish type hint: colors, defaults to `NULL`  
`chart_color_scale_categorical_extend`| Extend. Automatically generate additional colours when needed to avoid the palette colours being used more than once. Flourish type hint: boolean, defaults to `NULL`  
`chart_color_scale_categorical_custom_palette`| Custom overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to `NULL`  
`chart_color_scale_numeric_type`| Scale type. Choices: sequential, diverging. Flourish type hint: string, defaults to `NULL`  
`chart_color_scale_binning`| Choices: `FALSE`, `TRUE`. In linear mode, the color scale will run as a smooth gradient between 2 colors. In binned mode, the gradient will be divided in smaller blocks. Flourish type hint: boolean, defaults to `NULL`  
`chart_color_scale_bin_mode`| Binning mode. Choices: fixed, quantile, custom. Flourish type hint: string, defaults to `NULL`  
`chart_color_scale_bin_count`| Number of bins. Flourish type hint: number, defaults to `NULL`  
`chart_color_scale_bin_thresholds`| Custom thresholds. Enter your desired thresholds, separating them with a ";". For instance, "5;10;15". Bins form as follows: From the datas minimum value (domain minimum) up to the first threshold. Between consecutive thresholds. From the last threshold to the datas maximum value (domain maximum). For "5;10;15", youll get four bins based on your datas range. Flourish type hint: string, defaults to `NULL`  
`chart_color_scale_sequential_palette`| Palette. Flourish type hint: string, defaults to `NULL`  
`chart_color_scale_sequential_reverse`| Reverse. Flourish type hint: boolean, defaults to `NULL`  
`chart_color_scale_sequential_custom_min`| Minimum color. Flourish type hint: color, defaults to `NULL`  
`chart_color_scale_sequential_custom_max`| Maximum color. Flourish type hint: color, defaults to `NULL`  
`chart_color_scale_sequential_color_space`| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to `NULL`  
`chart_color_scale_sequential_custom_domain`| Domain. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_color_scale_sequential_domain_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_color_scale_sequential_domain_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_color_scale_diverging_palette`| Palette. Flourish type hint: string, defaults to `NULL`  
`chart_color_scale_diverging_reverse`| Reverse. Flourish type hint: boolean, defaults to `NULL`  
`chart_color_scale_diverging_custom_min`| Minimum color. Flourish type hint: color, defaults to `NULL`  
`chart_color_scale_diverging_custom_mid`| Midpoint color. Flourish type hint: color, defaults to `NULL`  
`chart_color_scale_diverging_custom_max`| Maximum color. Flourish type hint: color, defaults to `NULL`  
`chart_color_scale_diverging_color_space`| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to `NULL`  
`chart_color_scale_diverging_custom_domain`| Domain. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_color_scale_diverging_domain_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_color_scale_diverging_domain_mid`| Mid. Flourish type hint: number, defaults to `NULL`  
`chart_color_scale_diverging_domain_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_categorical_legend_show_legend`| Legend mode. Choices: `TRUE`, `FALSE`. A legend will not show with a single entry. Flourish type hint: boolean, defaults to `NULL`  
`chart_categorical_legend_title_mode`| Title mode. Choices: auto, custom. Flourish type hint: string, defaults to `NULL`  
`chart_categorical_legend_title`| Title. Flourish type hint: string, defaults to `NULL`  
`chart_categorical_legend_swatch_width`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_categorical_legend_swatch_height`| Height. Flourish type hint: number, defaults to `NULL`  
`chart_categorical_legend_swatch_radius`| Roundness. The radius of the corners of the swatch (in pixels). Flourish type hint: number, defaults to `NULL`  
`chart_categorical_legend_legend_items_padding`| Padding. Padding between legend items ( in rems ). Flourish type hint: number, defaults to `NULL`  
`chart_categorical_legend_swatch_outline`| Outline. An optional outline for the swatch in the legend. Flourish type hint: boolean, defaults to `NULL`  
`chart_categorical_legend_swatch_outline_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_categorical_legend_order_override`| Custom order override. Manually specify the order of legend entries (one entry per line). Flourish type hint: text, defaults to `NULL`  
`chart_categorical_legend_icon_height`| Height. Height of icon ( in rems ). Flourish type hint: number, defaults to `NULL`  
`chart_categorical_legend_icon_color`| Color. Fallback color (icon color if not determined by template). Flourish type hint: color, defaults to `NULL`  
`chart_categorical_legend_max_width`| Max width. Flourish type hint: number, defaults to `NULL`  
`chart_categorical_legend_orientation`| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_orientation`| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_title_weight`| Title weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_text_weight`| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_text_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_legend_container_text_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_axis_position`| Position. Choices: bottom, float-below, float-above, top, off. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_y_axis_position`| Y value. Vertical position of the X axis on the Y scale. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_numeric_scale_type`| Type. Choices: linear, log. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_linear_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_linear_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_log_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_log_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_datetime_min`| Min (date). Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_datetime_max`| Max (date). Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_flip`| Flip axis. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_show_scale_settings`| Configure default min/max. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_nice`| Round min/max. Choices: `TRUE`, `FALSE`. Enabling this option rounds the X axis start and end values to tidy numbers, such as 0, 50, 100 or whole years. Specified min and max values will override this feature. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_zero_axis`| Include zero. Choices: auto, on, off. Enable to extend the axis to include zero, even when data is all positive or all negative. This is ignored if you set specific min and max scale values. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_title_mode`| Type. Choices: auto, custom. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_title`| Text. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_title_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_title_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_title_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_x_axis_title_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_title_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_label_position`| Position. Choices: default, left, right. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_tick_label_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_tick_label_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_label_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_x_axis_tick_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_label_angle`| Angle. Choices: 0, 30, 45, 60, 90. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_tick_label_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_tick_label_max_lines`| Max lines. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_label_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_label_space_mode`| Space mode. Choices: auto, max, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_tick_label_space`| Space. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_mode`| Mode. Choices: auto, number, custom. Sets the method for selecting tick values on the axis: Auto automatically selects the ticks Number allows you to choose the number of ticks to display. Custom lets you select specific ticks to show. Note: If the axis is categorical, Number mode is ignored. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_tick_number`| Number. Approximate number of ticks or gridlines. The actual number will depend on the range of values, chart size, etc. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_custom`| One tick label per line. Specify the ticks to show, one per line. For dates, use the input format as specified in the datasheet. You can also use `{{FIRST}}` and `{{LAST}}` to add ticks at the minimum and maximum of the axis. For example: `{{FIRST}}` 25000 50000 75000 `{{LAST}}`. Flourish type hint: text, defaults to `NULL`  
`chart_x_axis_line_and_tick_color`| Line color. Flourish type hint: color, defaults to `NULL`  
`chart_x_axis_line_and_tick_width`| Line width. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_length`| Tick length. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_side`| Tick side. Choices: out, in. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_line_visible`| Axis line. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_edge_padding`| Edge padding (%). Space between start/end of axis line and first/last category tick as a percentage of the spacing between ticks. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_gridlines_visible`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_gridlines_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_gridline_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_x_axis_gridline_style`| Style. Choices: solid, dash, dot, dot_dash. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_gridline_width`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_gridline_category_dividers`| Put lines between categories. On a categorical axis, this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_gridline_category_dividers_extend`| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_axis_visible`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_numeric_scale_type`| Type. Choices: linear, log. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_linear_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_linear_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_log_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_log_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_datetime_min`| Min (date). Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_datetime_max`| Max (date). Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_flip`| Flip axis. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_show_scale_settings`| Configure default min/max. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_nice`| Round min/max. Choices: `TRUE`, `FALSE`. When enabled, scales automatically extend to "nice" rounded start/end values, such as hundreds or whole years. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_zero_axis`| Include zero. Choices: auto, on, off. Whether to extend the axis to include zero if the data values are all positive or all negative. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_title_mode`| Type. Choices: auto, custom. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_title`| Text. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_title_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_title_position`| Position. Choices: side, end. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_title_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_title_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_y_axis_title_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_title_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_label_position`| Position. Choices: default, above, below. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_tick_label_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_tick_label_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_label_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_y_axis_tick_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_label_angle`| Angle. Choices: 0, 30, 45, 60, 90. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_tick_label_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_tick_label_max_lines`| Max lines. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_label_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_label_space_mode`| Space mode. Choices: auto, max, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_tick_label_space`| Space. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_mode`| Mode. Choices: auto, number, custom. Sets the method for selecting tick values on the axis: Auto automatically selects the ticks Number allows you to choose the number of ticks to display. Custom lets you select specific ticks to show. Note: If the axis is categorical, Number mode is ignored. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_tick_number`| Number. Approximate number of ticks or gridlines. The actual number will depend on the range of values, chart size, etc. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_custom`| One tick label per line. Specify the ticks to show, one per line. For dates, use the input format as specified in the datasheet. You can also use `{{FIRST}}` and `{{LAST}}` to add ticks at the minimum and maximum of the axis. For example: `{{FIRST}}` 25000 50000 75000 `{{LAST}}`. Flourish type hint: text, defaults to `NULL`  
`chart_y_axis_line_and_tick_color`| Line color. Flourish type hint: color, defaults to `NULL`  
`chart_y_axis_line_and_tick_width`| Line width. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_length`| Tick length. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_side`| Side. Choices: out, in. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_line_visible`| Axis line. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_edge_padding`| Edge padding (%). Space between start/end of axis line and first/last category tick as a percentage of the spacing between ticks. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_gridlines_visible`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_gridlines_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_gridline_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_y_axis_gridline_style`| Style. Choices: solid, dash, dot, dot_dash. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_gridline_width`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_gridline_category_dividers`| Put lines between categories. On a categorical axis, this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Ignored for date and numeric axes. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_gridline_category_dividers_extend`| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to `NULL`  
`chart_background_background_color_enabled`| Color. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_background_background_image_enabled`| Image. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_background_background_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_background_background_image_src`| Image URL. Flourish type hint: url, defaults to `NULL`  
`chart_background_background_image_size`| Size. Choices: stretch, slice, meet. Flourish type hint: string, defaults to `NULL`  
`chart_background_background_image_position`| Position. Choices: x_min_y_min, x_mid_y_min, x_max_y_min, x_max_y_mid, x_mid_y_mid, x_min_y_max, x_mid_y_max, x_max_y_max. Flourish type hint: string, defaults to `NULL`  
`datetime_input_format`| Format in data sheet. Choices: auto, %Y-%m-%dT%H:%M:%S.%LZ, %Y-%m-%d, %m/%d/%Y, %d/%m/%Y, %d-%b-%y, %m/%Y, %m/%y, %b %Y, %b %y, %B %d, %d %b, %Y, %y, %B, %b, %H:%M:%S, %I:%M %p, %H:%M. The date/time format in the datasheet. Leave as Auto for Flourish to make a best guess. If it isnt in the list, you can enter a custom format using d3-time-format syntax. See NPM d3-data-format for details. Flourish type hint: string, defaults to `NULL`  
`date_format`| Display format. Choices: auto, %Y-%m-%dT%H:%M:%S.%LZ, %Y-%m-%d, %m/%d/%Y, %d/%m/%Y, %d-%b-%y, %m/%Y, %m/%y, %b %Y, %b %y, %B %d, %d %b, %Y, %y, %B, %b, %A, %a, %H:%M:%S, %I:%M %p, %H:%M. The date/time format to show in the graphic. If it isnt in the list, you can enter a custom format using d3-time-format syntax. See NPM d3-data-format for details. Flourish type hint: string, defaults to `NULL`  
`chart_number_localization_input_decimal_separator`| Decimal separator in data sheet. Choices: ., ,. Used for interpreting your data. Only change if data is not displaying on the chart as expected. Flourish type hint: string, defaults to `NULL`  
`chart_number_localization_output_separators`| Number format to display. Choices: ,., .,, ., ,, ., ,. How the numbers should appear on chart labels. Flourish type hint: string, defaults to `NULL`  
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
