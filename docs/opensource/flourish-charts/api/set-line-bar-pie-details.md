---
url: https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/
title: Set line, bar and pie charts chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:33.286008+00:00
---

# Set line, bar and pie charts chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set line, bar and pie charts chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_line_bar_pie_details(
    
        self,
    
        dual_axis: bool = None,
    
        secondary_series: float = None,
    
        stack_sort: str = None,
    
        facet_layout: str = None,
    
        height_mode: str = None,
    
        facet_aspect: float = None,
    
        facet_aspect_mobile: float = None,
    
        facet_aspect_breakpoint: float = None,
    
        sort_mode: str = None,
    
        chart_facet_columns_fixed: bool = None,
    
        chart_facet_min_width: float = None,
    
        chart_facet_max_width: float = None,
    
        chart_facet_columns: float = None,
    
        chart_facet_gutter_w: float = None,
    
        chart_facet_gutter_h: float = None,
    
        chart_facet_animation: str = None,
    
        chart_facet_titles: bool = None,
    
        chart_facet_title_align: str = None,
    
        chart_facet_title_size: float = None,
    
        chart_facet_title_unit: str = None,
    
        chart_facet_title_color: str = None,
    
        chart_facet_title_padding_top: float = None,
    
        chart_facet_title_padding_bottom: float = None,
    
        chart_facet_title_bg: str = None,
    
        chart_facet_title_bg_color: str = None,
    
        chart_facet_title_bg_padding: float = None,
    
        x_axis_matching: bool = None,
    
        x_axis_last_row_only: bool = None,
    
        y_axis_matching: bool = None,
    
        y_axis_first_col_only: bool = None,
    
        y2_axis_matching: bool = None,
    
        y2_axis_last_col_only: bool = None,
    
        series_filter_mode: str = None,
    
        series_control_multi_text: str = None,
    
        series_control_multi_none_text: str = None,
    
        series_control_select_text: str = None,
    
        max_series: float = None,
    
        series_control_background: str = None,
    
        series_control_text: str = None,
    
        series_control_border: str = None,
    
        series_control_pill_background: str = None,
    
        series_control_pill_text: str = None,
    
        series_control_pill_radius: float = None,
    
        series_control_single_all: bool = None,
    
        series_control_single_all_text: str = None,
    
        filter_rows_with_no_data: bool = None,
    
        chart_series_filter_controls_control_type: str = None,
    
        chart_series_filter_controls_control_styles: bool = None,
    
        chart_series_filter_controls_control_title: str = None,
    
        chart_series_filter_controls_button_group: bool = None,
    
        chart_series_filter_controls_button_group_width_mode: str = None,
    
        chart_series_filter_controls_button_group_width_fixed: float = None,
    
        chart_series_filter_controls_dropdown_width_mode: str = None,
    
        chart_series_filter_controls_dropdown_width_fixed: float = None,
    
        chart_series_filter_controls_slider_width: float = None,
    
        chart_series_filter_controls_slider_max_label_width: float = None,
    
        chart_series_filter_controls_slider_step_time: float = None,
    
        chart_series_filter_controls_slider_loop: bool = None,
    
        chart_series_filter_controls_slider_restart_pause: float = None,
    
        chart_series_filter_controls_sort: bool = None,
    
        row_filter_control_all: bool = None,
    
        row_filter_control_all_text: str = None,
    
        chart_row_filter_controls_control_type: str = None,
    
        chart_row_filter_controls_control_styles: bool = None,
    
        chart_row_filter_controls_control_title: str = None,
    
        chart_row_filter_controls_button_group: bool = None,
    
        chart_row_filter_controls_button_group_width_mode: str = None,
    
        chart_row_filter_controls_button_group_width_fixed: float = None,
    
        chart_row_filter_controls_dropdown_width_mode: str = None,
    
        chart_row_filter_controls_dropdown_width_fixed: float = None,
    
        chart_row_filter_controls_slider_width: float = None,
    
        chart_row_filter_controls_slider_max_label_width: float = None,
    
        chart_row_filter_controls_slider_step_time: float = None,
    
        chart_row_filter_controls_slider_loop: bool = None,
    
        chart_row_filter_controls_slider_restart_pause: float = None,
    
        chart_row_filter_controls_sort: bool = None,
    
        log_control_y_visible: bool = None,
    
        chart_log_control_y_filter_controls_control_type: str = None,
    
        chart_log_control_y_filter_controls_control_styles: bool = None,
    
        chart_log_control_y_filter_controls_control_title: str = None,
    
        chart_log_control_y_filter_controls_button_group: bool = None,
    
        chart_log_control_y_filter_controls_button_group_width_mode: str = None,
    
        chart_log_control_y_filter_controls_button_group_width_fixed: float = None,
    
        chart_log_control_y_filter_controls_dropdown_width_mode: str = None,
    
        chart_log_control_y_filter_controls_dropdown_width_fixed: float = None,
    
        chart_log_control_y_filter_controls_slider_width: float = None,
    
        chart_log_control_y_filter_controls_slider_max_label_width: float = None,
    
        chart_log_control_y_filter_controls_slider_step_time: float = None,
    
        chart_log_control_y_filter_controls_slider_loop: bool = None,
    
        chart_log_control_y_filter_controls_slider_restart_pause: float = None,
    
        chart_log_control_y_filter_controls_sort: bool = None,
    
        log_control_y_text_linear: str = None,
    
        log_control_y_text_log: str = None,
    
        chart_controls_style_font_size: float = None,
    
        chart_controls_style_font_weight: str = None,
    
        chart_controls_style_height: float = None,
    
        chart_dropdown_control_style_background: str = None,
    
        chart_dropdown_control_style_font_color: str = None,
    
        chart_dropdown_control_style_border_styles_advanced: bool = None,
    
        chart_dropdown_control_style_border_style: str = None,
    
        chart_dropdown_control_style_border_width: float = None,
    
        chart_dropdown_control_style_border_color: str = None,
    
        chart_dropdown_control_style_border_transparency: float = None,
    
        chart_dropdown_control_style_border_radius: float = None,
    
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
    
        chart_filter_controls_container_alignment: str = None,
    
        chart_filter_controls_container_controls_spacing: float = None,
    
        controls_position: str = None,
    
        color_mode: str = None,
    
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
    
        line_width: float = None,
    
        line_opacity: float = None,
    
        line_stroke: bool = None,
    
        line_curve: str = None,
    
        line_dash_items: Union[list, str] = None,
    
        line_dash_width: float = None,
    
        line_dash_space_width: float = None,
    
        line_interpolate: bool = None,
    
        shade_between_lines: bool = None,
    
        shade_between_lines_config: Union[list, str] = None,
    
        shade_between_lines_color: str = None,
    
        shade_between_lines_opacity: float = None,
    
        area_opacity: float = None,
    
        dot_mode: str = None,
    
        dot_opacity: float = None,
    
        dot_radius: float = None,
    
        dot_radius_last: float = None,
    
        dot_hollow: bool = None,
    
        bar_height: float = None,
    
        column_opacity: float = None,
    
        uniform_column_width: bool = None,
    
        uniform_bar_height: bool = None,
    
        column_padding_inner: float = None,
    
        column_padding_in_group: float = None,
    
        column_padding_stack: float = None,
    
        column_stroke: bool = None,
    
        column_stroke_opacity: float = None,
    
        column_stroke_color: str = None,
    
        donut_inner_radius: float = None,
    
        donut_corner_radius: float = None,
    
        donut_pad_angle: float = None,
    
        donut_auto_scale: bool = None,
    
        bar_labels_above: bool = None,
    
        bar_labels_color: str = None,
    
        bar_labels_font_size: float = None,
    
        bar_labels_weight: str = None,
    
        line_end_labels: bool = None,
    
        chart_line_labels_max_width: float = None,
    
        chart_line_labels_overlap_mode: str = None,
    
        chart_line_labels_spreading_margin: float = None,
    
        chart_line_labels_data_point_margin: float = None,
    
        chart_line_labels_show_only_labels: Union[list, str] = None,
    
        chart_line_labels_text_color: str = None,
    
        chart_line_labels_text_size: float = None,
    
        chart_line_labels_text_bg_color: str = None,
    
        chart_line_labels_text_bg_size: float = None,
    
        chart_line_labels_text_line_height: float = None,
    
        chart_line_labels_text_max_lines: float = None,
    
        chart_line_labels_text_weight: str = None,
    
        chart_line_labels_lines: str = None,
    
        chart_line_labels_line_style: str = None,
    
        chart_line_labels_line_color: str = None,
    
        chart_line_labels_line_width: float = None,
    
        chart_line_labels_line_range: float = None,
    
        chart_line_labels_line_padding: float = None,
    
        labels: bool = None,
    
        labels_hide_overlaps: bool = None,
    
        labels_dot_center: bool = None,
    
        labels_column_align: str = None,
    
        labels_column_padding: float = None,
    
        labels_bar_align: str = None,
    
        labels_bar_autohide: bool = None,
    
        labels_color_mode: str = None,
    
        labels_fixed_color: str = None,
    
        labels_font_weight: str = None,
    
        labels_font_size_mode: str = None,
    
        labels_font_size: float = None,
    
        labels_bg_mode: str = None,
    
        labels_bg_size: float = None,
    
        labels_content: str = None,
    
        stack_labels: bool = None,
    
        stack_labels_color: str = None,
    
        stack_labels_font_size: float = None,
    
        stack_labels_weight: str = None,
    
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
    
        chart_secondary_y_axis_axis_visible: bool = None,
    
        chart_secondary_y_axis_numeric_scale_type: str = None,
    
        chart_secondary_y_axis_linear_min: float = None,
    
        chart_secondary_y_axis_linear_max: float = None,
    
        chart_secondary_y_axis_log_min: float = None,
    
        chart_secondary_y_axis_log_max: float = None,
    
        chart_secondary_y_axis_datetime_min: str = None,
    
        chart_secondary_y_axis_datetime_max: str = None,
    
        chart_secondary_y_axis_flip: bool = None,
    
        chart_secondary_y_axis_show_scale_settings: bool = None,
    
        chart_secondary_y_axis_nice: bool = None,
    
        chart_secondary_y_axis_zero_axis: str = None,
    
        chart_secondary_y_axis_title_mode: str = None,
    
        chart_secondary_y_axis_title: str = None,
    
        chart_secondary_y_axis_title_styling: bool = None,
    
        chart_secondary_y_axis_title_position: str = None,
    
        chart_secondary_y_axis_title_weight: str = None,
    
        chart_secondary_y_axis_title_color: str = None,
    
        chart_secondary_y_axis_title_size: float = None,
    
        chart_secondary_y_axis_title_padding: float = None,
    
        chart_secondary_y_axis_tick_label_position: str = None,
    
        chart_secondary_y_axis_tick_label_styling: bool = None,
    
        chart_secondary_y_axis_tick_label_size: float = None,
    
        chart_secondary_y_axis_tick_label_color: str = None,
    
        chart_secondary_y_axis_tick_padding: float = None,
    
        chart_secondary_y_axis_tick_label_angle: str = None,
    
        chart_secondary_y_axis_tick_label_weight: str = None,
    
        chart_secondary_y_axis_tick_label_max_lines: float = None,
    
        chart_secondary_y_axis_tick_label_line_height: float = None,
    
        chart_secondary_y_axis_tick_label_space_mode: str = None,
    
        chart_secondary_y_axis_tick_label_space: float = None,
    
        chart_secondary_y_axis_tick_mode: str = None,
    
        chart_secondary_y_axis_tick_number: float = None,
    
        chart_secondary_y_axis_tick_custom: Union[list, str] = None,
    
        chart_secondary_y_axis_line_and_tick_color: str = None,
    
        chart_secondary_y_axis_line_and_tick_width: float = None,
    
        chart_secondary_y_axis_tick_length: float = None,
    
        chart_secondary_y_axis_tick_side: str = None,
    
        chart_secondary_y_axis_line_visible: bool = None,
    
        chart_secondary_y_axis_edge_padding: float = None,
    
        chart_secondary_y_axis_gridlines_visible: bool = None,
    
        chart_secondary_y_axis_gridlines_styling: bool = None,
    
        chart_secondary_y_axis_gridline_color: str = None,
    
        chart_secondary_y_axis_gridline_style: str = None,
    
        chart_secondary_y_axis_gridline_width: float = None,
    
        chart_secondary_y_axis_gridline_category_dividers: bool = None,
    
        chart_secondary_y_axis_gridline_category_dividers_extend: bool = None,
    
        chart_background_background_color_enabled: bool = None,
    
        chart_background_background_image_enabled: bool = None,
    
        chart_background_background_color: str = None,
    
        chart_background_background_image_src: str = None,
    
        chart_background_background_image_size: str = None,
    
        chart_background_background_image_position: str = None,
    
        number_format_labels_prefix: str = None,
    
        number_format_labels_suffix: str = None,
    
        number_format_labels_n_dec: float = None,
    
        number_format_labels_advanced: bool = None,
    
        number_format_labels_negative_sign: str = None,
    
        number_format_labels_strip_zeros: bool = None,
    
        number_format_labels_strip_separator: bool = None,
    
        number_format_labels_transform_labels: bool = None,
    
        number_format_labels_transform: str = None,
    
        number_format_labels_multiply_divide_constant: float = None,
    
        number_format_labels_exponentiate_constant: float = None,
    
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
    
        number_format_prop: bool = None,
    
        chart_secondary_number_date_format_prefix: str = None,
    
        chart_secondary_number_date_format_suffix: str = None,
    
        chart_secondary_number_date_format_n_dec: float = None,
    
        chart_secondary_number_date_format_advanced: bool = None,
    
        chart_secondary_number_date_format_negative_sign: str = None,
    
        chart_secondary_number_date_format_strip_zeros: bool = None,
    
        chart_secondary_number_date_format_strip_separator: bool = None,
    
        chart_secondary_number_date_format_transform_labels: bool = None,
    
        chart_secondary_number_date_format_transform: str = None,
    
        chart_secondary_number_date_format_multiply_divide_constant: float = None,
    
        chart_secondary_number_date_format_exponentiate_constant: float = None,
    
        legend_mode: str = None,
    
        legend_filter_mode: str = None,
    
        chart_legend_container_alignment: str = None,
    
        chart_legend_container_orientation: str = None,
    
        chart_legend_container_title_weight: str = None,
    
        chart_legend_container_text_weight: str = None,
    
        chart_legend_container_text_color: str = None,
    
        chart_legend_container_text_size: float = None,
    
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
    
        legend_position: str = None,
    
        text_legend: str = None,
    
        text_legend_title: bool = None,
    
        text_legend_subtitle: bool = None,
    
        text_legend_bold: bool = None,
    
        chart_popup_mode: str = None,
    
        chart_popup_popup_is_custom: bool = None,
    
        chart_popup_show_popup_styles: bool = None,
    
        chart_popup_popup_custom_header: Union[list, str] = None,
    
        chart_popup_popup_custom_main: Union[list, str] = None,
    
        chart_popup_popup_custom_accessible: Union[list, str] = None,
    
        chart_popup_popup_width: float = None,
    
        chart_popup_popup_font_size: float = None,
    
        chart_popup_popup_text_color: str = None,
    
        chart_popup_popup_align: str = None,
    
        chart_popup_popup_background: str = None,
    
        chart_popup_popup_background_opacity: float = None,
    
        chart_popup_popup_padding: float = None,
    
        chart_popup_popup_radius: float = None,
    
        chart_popup_popup_header_type: str = None,
    
        chart_popup_popup_header_background: str = None,
    
        chart_popup_popup_header_text_color: str = None,
    
        chart_popup_popup_list_type: str = None,
    
        chart_popup_popup_list_label_weight: str = None,
    
        chart_popup_popup_list_separator: str = None,
    
        chart_popup_popup_shadow: bool = None,
    
        chart_popup_popup_pointer: bool = None,
    
        chart_popup_panel_position: str = None,
    
        chart_popup_panel_open_duration: float = None,
    
        chart_popup_panel_side_fixed: bool = None,
    
        chart_popup_panel_side_default_content: Union[list, str] = None,
    
        chart_popup_panel_is_custom: bool = None,
    
        chart_popup_show_panel_styles: bool = None,
    
        chart_popup_panel_custom_header: Union[list, str] = None,
    
        chart_popup_panel_custom_main: Union[list, str] = None,
    
        chart_popup_panel_width_overlay: float = None,
    
        chart_popup_panel_height_overlay: float = None,
    
        chart_popup_panel_width_side: float = None,
    
        chart_popup_panel_height_side: float = None,
    
        chart_popup_panel_max_width: float = None,
    
        chart_popup_panel_max_height: float = None,
    
        chart_popup_panel_vertical_position: str = None,
    
        chart_popup_panel_text_color: str = None,
    
        chart_popup_panel_font_size: float = None,
    
        chart_popup_panel_align: str = None,
    
        chart_popup_panel_background: str = None,
    
        chart_popup_panel_background_opacity: float = None,
    
        chart_popup_panel_padding: float = None,
    
        chart_popup_panel_radius: float = None,
    
        chart_popup_panel_list_type: str = None,
    
        chart_popup_panel_list_label_weight: str = None,
    
        chart_popup_panel_list_separator: str = None,
    
        chart_popup_panel_shadow: bool = None,
    
        popup_color_headers: bool = None,
    
        show_series_text: bool = None,
    
        popup_series_text: Union[list, str] = None,
    
        chart_axes_highlights_placement: str = None,
    
        chart_axes_highlights_x_enabled: bool = None,
    
        chart_axes_highlights_x_lines: Union[list, str] = None,
    
        chart_axes_highlights_x_line_color: str = None,
    
        chart_axes_highlights_x_line_width: float = None,
    
        chart_axes_highlights_x_line_dash: float = None,
    
        chart_axes_highlights_x_areas: Union[list, str] = None,
    
        chart_axes_highlights_x_area_color: str = None,
    
        chart_axes_highlights_x_area_opacity: float = None,
    
        chart_axes_highlights_x_area_texture: str = None,
    
        chart_axes_highlights_x_label_vertical: bool = None,
    
        chart_axes_highlights_x_label_y_position: str = None,
    
        chart_axes_highlights_x_label_x_position: str = None,
    
        chart_axes_highlights_x_label_max_width: float = None,
    
        chart_axes_highlights_x_font_size: float = None,
    
        chart_axes_highlights_x_font_weight: str = None,
    
        chart_axes_highlights_x_label_color: str = None,
    
        chart_axes_highlights_x_shadow_color: str = None,
    
        chart_axes_highlights_x_shadow_enabled: bool = None,
    
        chart_axes_highlights_y_enabled: bool = None,
    
        chart_axes_highlights_y_lines: Union[list, str] = None,
    
        chart_axes_highlights_y_line_color: str = None,
    
        chart_axes_highlights_y_line_width: float = None,
    
        chart_axes_highlights_y_line_dash: float = None,
    
        chart_axes_highlights_y_areas: Union[list, str] = None,
    
        chart_axes_highlights_y_area_color: str = None,
    
        chart_axes_highlights_y_area_opacity: float = None,
    
        chart_axes_highlights_y_area_texture: str = None,
    
        chart_axes_highlights_y_label_x_position: str = None,
    
        chart_axes_highlights_y_label_y_position: str = None,
    
        chart_axes_highlights_y_label_max_width: float = None,
    
        chart_axes_highlights_y_font_size: float = None,
    
        chart_axes_highlights_y_font_weight: str = None,
    
        chart_axes_highlights_y_label_color: str = None,
    
        chart_axes_highlights_y_shadow_color: str = None,
    
        chart_axes_highlights_y_shadow_enabled: bool = None,
    
        annotations_styles: bool = None,
    
        chart_annotations_defaults_text_weight: str = None,
    
        chart_annotations_defaults_text_size: float = None,
    
        chart_annotations_defaults_text_color: str = None,
    
        chart_annotations_defaults_label_width: float = None,
    
        chart_annotations_defaults_text_background_mode: str = None,
    
        chart_annotations_defaults_text_bg: str = None,
    
        chart_annotations_defaults_label_bg: str = None,
    
        chart_annotations_defaults_text_alignment: str = None,
    
        chart_annotations_defaults_popup_position: str = None,
    
        chart_annotations_defaults_line_marker: str = None,
    
        chart_annotations_defaults_stroke_width: float = None,
    
        chart_annotations_defaults_stroke_color: str = None,
    
        chart_annotations_defaults_connector_extend_line: str = None,
    
        data_trans_duration: float = None,
    
        animate_on_load: bool = None,
    
        data_trans_bind_series: bool = None,
    
        data_trans_bind_data_points: bool = None,
    
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
    
        chart_layout_screenreader_hide_primary: bool = None,
    
        chart_url_settings_enabled: bool = None,
    
        chart_url_settings_whitelist: Union[list, str] = None
    
        )

PYTHON

Copy
    
    
    set_line_bar_pie_details(
    
        .,
    
        dual_axis = NULL,
    
        secondary_series = NULL,
    
        stack_sort = NULL,
    
        facet_layout = NULL,
    
        height_mode = NULL,
    
        facet_aspect = NULL,
    
        facet_aspect_mobile = NULL,
    
        facet_aspect_breakpoint = NULL,
    
        sort_mode = NULL,
    
        chart_facet_columns_fixed = NULL,
    
        chart_facet_min_width = NULL,
    
        chart_facet_max_width = NULL,
    
        chart_facet_columns = NULL,
    
        chart_facet_gutter_w = NULL,
    
        chart_facet_gutter_h = NULL,
    
        chart_facet_animation = NULL,
    
        chart_facet_titles = NULL,
    
        chart_facet_title_align = NULL,
    
        chart_facet_title_size = NULL,
    
        chart_facet_title_unit = NULL,
    
        chart_facet_title_color = NULL,
    
        chart_facet_title_padding_top = NULL,
    
        chart_facet_title_padding_bottom = NULL,
    
        chart_facet_title_bg = NULL,
    
        chart_facet_title_bg_color = NULL,
    
        chart_facet_title_bg_padding = NULL,
    
        x_axis_matching = NULL,
    
        x_axis_last_row_only = NULL,
    
        y_axis_matching = NULL,
    
        y_axis_first_col_only = NULL,
    
        y2_axis_matching = NULL,
    
        y2_axis_last_col_only = NULL,
    
        series_filter_mode = NULL,
    
        series_control_multi_text = NULL,
    
        series_control_multi_none_text = NULL,
    
        series_control_select_text = NULL,
    
        max_series = NULL,
    
        series_control_background = NULL,
    
        series_control_text = NULL,
    
        series_control_border = NULL,
    
        series_control_pill_background = NULL,
    
        series_control_pill_text = NULL,
    
        series_control_pill_radius = NULL,
    
        series_control_single_all = NULL,
    
        series_control_single_all_text = NULL,
    
        filter_rows_with_no_data = NULL,
    
        chart_series_filter_controls_control_type = NULL,
    
        chart_series_filter_controls_control_styles = NULL,
    
        chart_series_filter_controls_control_title = NULL,
    
        chart_series_filter_controls_button_group = NULL,
    
        chart_series_filter_controls_button_group_width_mode = NULL,
    
        chart_series_filter_controls_button_group_width_fixed = NULL,
    
        chart_series_filter_controls_dropdown_width_mode = NULL,
    
        chart_series_filter_controls_dropdown_width_fixed = NULL,
    
        chart_series_filter_controls_slider_width = NULL,
    
        chart_series_filter_controls_slider_max_label_width = NULL,
    
        chart_series_filter_controls_slider_step_time = NULL,
    
        chart_series_filter_controls_slider_loop = NULL,
    
        chart_series_filter_controls_slider_restart_pause = NULL,
    
        chart_series_filter_controls_sort = NULL,
    
        row_filter_control_all = NULL,
    
        row_filter_control_all_text = NULL,
    
        chart_row_filter_controls_control_type = NULL,
    
        chart_row_filter_controls_control_styles = NULL,
    
        chart_row_filter_controls_control_title = NULL,
    
        chart_row_filter_controls_button_group = NULL,
    
        chart_row_filter_controls_button_group_width_mode = NULL,
    
        chart_row_filter_controls_button_group_width_fixed = NULL,
    
        chart_row_filter_controls_dropdown_width_mode = NULL,
    
        chart_row_filter_controls_dropdown_width_fixed = NULL,
    
        chart_row_filter_controls_slider_width = NULL,
    
        chart_row_filter_controls_slider_max_label_width = NULL,
    
        chart_row_filter_controls_slider_step_time = NULL,
    
        chart_row_filter_controls_slider_loop = NULL,
    
        chart_row_filter_controls_slider_restart_pause = NULL,
    
        chart_row_filter_controls_sort = NULL,
    
        log_control_y_visible = NULL,
    
        chart_log_control_y_filter_controls_control_type = NULL,
    
        chart_log_control_y_filter_controls_control_styles = NULL,
    
        chart_log_control_y_filter_controls_control_title = NULL,
    
        chart_log_control_y_filter_controls_button_group = NULL,
    
        chart_log_control_y_filter_controls_button_group_width_mode = NULL,
    
        chart_log_control_y_filter_controls_button_group_width_fixed = NULL,
    
        chart_log_control_y_filter_controls_dropdown_width_mode = NULL,
    
        chart_log_control_y_filter_controls_dropdown_width_fixed = NULL,
    
        chart_log_control_y_filter_controls_slider_width = NULL,
    
        chart_log_control_y_filter_controls_slider_max_label_width = NULL,
    
        chart_log_control_y_filter_controls_slider_step_time = NULL,
    
        chart_log_control_y_filter_controls_slider_loop = NULL,
    
        chart_log_control_y_filter_controls_slider_restart_pause = NULL,
    
        chart_log_control_y_filter_controls_sort = NULL,
    
        log_control_y_text_linear = NULL,
    
        log_control_y_text_log = NULL,
    
        chart_controls_style_font_size = NULL,
    
        chart_controls_style_font_weight = NULL,
    
        chart_controls_style_height = NULL,
    
        chart_dropdown_control_style_background = NULL,
    
        chart_dropdown_control_style_font_color = NULL,
    
        chart_dropdown_control_style_border_styles_advanced = NULL,
    
        chart_dropdown_control_style_border_style = NULL,
    
        chart_dropdown_control_style_border_width = NULL,
    
        chart_dropdown_control_style_border_color = NULL,
    
        chart_dropdown_control_style_border_transparency = NULL,
    
        chart_dropdown_control_style_border_radius = NULL,
    
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
    
        chart_filter_controls_container_alignment = NULL,
    
        chart_filter_controls_container_controls_spacing = NULL,
    
        controls_position = NULL,
    
        color_mode = NULL,
    
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
    
        line_width = NULL,
    
        line_opacity = NULL,
    
        line_stroke = NULL,
    
        line_curve = NULL,
    
        line_dash_items = NULL,
    
        line_dash_width = NULL,
    
        line_dash_space_width = NULL,
    
        line_interpolate = NULL,
    
        shade_between_lines = NULL,
    
        shade_between_lines_config = NULL,
    
        shade_between_lines_color = NULL,
    
        shade_between_lines_opacity = NULL,
    
        area_opacity = NULL,
    
        dot_mode = NULL,
    
        dot_opacity = NULL,
    
        dot_radius = NULL,
    
        dot_radius_last = NULL,
    
        dot_hollow = NULL,
    
        bar_height = NULL,
    
        column_opacity = NULL,
    
        uniform_column_width = NULL,
    
        uniform_bar_height = NULL,
    
        column_padding_inner = NULL,
    
        column_padding_in_group = NULL,
    
        column_padding_stack = NULL,
    
        column_stroke = NULL,
    
        column_stroke_opacity = NULL,
    
        column_stroke_color = NULL,
    
        donut_inner_radius = NULL,
    
        donut_corner_radius = NULL,
    
        donut_pad_angle = NULL,
    
        donut_auto_scale = NULL,
    
        bar_labels_above = NULL,
    
        bar_labels_color = NULL,
    
        bar_labels_font_size = NULL,
    
        bar_labels_weight = NULL,
    
        line_end_labels = NULL,
    
        chart_line_labels_max_width = NULL,
    
        chart_line_labels_overlap_mode = NULL,
    
        chart_line_labels_spreading_margin = NULL,
    
        chart_line_labels_data_point_margin = NULL,
    
        chart_line_labels_show_only_labels = NULL,
    
        chart_line_labels_text_color = NULL,
    
        chart_line_labels_text_size = NULL,
    
        chart_line_labels_text_bg_color = NULL,
    
        chart_line_labels_text_bg_size = NULL,
    
        chart_line_labels_text_line_height = NULL,
    
        chart_line_labels_text_max_lines = NULL,
    
        chart_line_labels_text_weight = NULL,
    
        chart_line_labels_lines = NULL,
    
        chart_line_labels_line_style = NULL,
    
        chart_line_labels_line_color = NULL,
    
        chart_line_labels_line_width = NULL,
    
        chart_line_labels_line_range = NULL,
    
        chart_line_labels_line_padding = NULL,
    
        labels = NULL,
    
        labels_hide_overlaps = NULL,
    
        labels_dot_center = NULL,
    
        labels_column_align = NULL,
    
        labels_column_padding = NULL,
    
        labels_bar_align = NULL,
    
        labels_bar_autohide = NULL,
    
        labels_color_mode = NULL,
    
        labels_fixed_color = NULL,
    
        labels_font_weight = NULL,
    
        labels_font_size_mode = NULL,
    
        labels_font_size = NULL,
    
        labels_bg_mode = NULL,
    
        labels_bg_size = NULL,
    
        labels_content = NULL,
    
        stack_labels = NULL,
    
        stack_labels_color = NULL,
    
        stack_labels_font_size = NULL,
    
        stack_labels_weight = NULL,
    
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
    
        chart_secondary_y_axis_axis_visible = NULL,
    
        chart_secondary_y_axis_numeric_scale_type = NULL,
    
        chart_secondary_y_axis_linear_min = NULL,
    
        chart_secondary_y_axis_linear_max = NULL,
    
        chart_secondary_y_axis_log_min = NULL,
    
        chart_secondary_y_axis_log_max = NULL,
    
        chart_secondary_y_axis_datetime_min = NULL,
    
        chart_secondary_y_axis_datetime_max = NULL,
    
        chart_secondary_y_axis_flip = NULL,
    
        chart_secondary_y_axis_show_scale_settings = NULL,
    
        chart_secondary_y_axis_nice = NULL,
    
        chart_secondary_y_axis_zero_axis = NULL,
    
        chart_secondary_y_axis_title_mode = NULL,
    
        chart_secondary_y_axis_title = NULL,
    
        chart_secondary_y_axis_title_styling = NULL,
    
        chart_secondary_y_axis_title_position = NULL,
    
        chart_secondary_y_axis_title_weight = NULL,
    
        chart_secondary_y_axis_title_color = NULL,
    
        chart_secondary_y_axis_title_size = NULL,
    
        chart_secondary_y_axis_title_padding = NULL,
    
        chart_secondary_y_axis_tick_label_position = NULL,
    
        chart_secondary_y_axis_tick_label_styling = NULL,
    
        chart_secondary_y_axis_tick_label_size = NULL,
    
        chart_secondary_y_axis_tick_label_color = NULL,
    
        chart_secondary_y_axis_tick_padding = NULL,
    
        chart_secondary_y_axis_tick_label_angle = NULL,
    
        chart_secondary_y_axis_tick_label_weight = NULL,
    
        chart_secondary_y_axis_tick_label_max_lines = NULL,
    
        chart_secondary_y_axis_tick_label_line_height = NULL,
    
        chart_secondary_y_axis_tick_label_space_mode = NULL,
    
        chart_secondary_y_axis_tick_label_space = NULL,
    
        chart_secondary_y_axis_tick_mode = NULL,
    
        chart_secondary_y_axis_tick_number = NULL,
    
        chart_secondary_y_axis_tick_custom = NULL,
    
        chart_secondary_y_axis_line_and_tick_color = NULL,
    
        chart_secondary_y_axis_line_and_tick_width = NULL,
    
        chart_secondary_y_axis_tick_length = NULL,
    
        chart_secondary_y_axis_tick_side = NULL,
    
        chart_secondary_y_axis_line_visible = NULL,
    
        chart_secondary_y_axis_edge_padding = NULL,
    
        chart_secondary_y_axis_gridlines_visible = NULL,
    
        chart_secondary_y_axis_gridlines_styling = NULL,
    
        chart_secondary_y_axis_gridline_color = NULL,
    
        chart_secondary_y_axis_gridline_style = NULL,
    
        chart_secondary_y_axis_gridline_width = NULL,
    
        chart_secondary_y_axis_gridline_category_dividers = NULL,
    
        chart_secondary_y_axis_gridline_category_dividers_extend = NULL,
    
        chart_background_background_color_enabled = NULL,
    
        chart_background_background_image_enabled = NULL,
    
        chart_background_background_color = NULL,
    
        chart_background_background_image_src = NULL,
    
        chart_background_background_image_size = NULL,
    
        chart_background_background_image_position = NULL,
    
        number_format_labels_prefix = NULL,
    
        number_format_labels_suffix = NULL,
    
        number_format_labels_n_dec = NULL,
    
        number_format_labels_advanced = NULL,
    
        number_format_labels_negative_sign = NULL,
    
        number_format_labels_strip_zeros = NULL,
    
        number_format_labels_strip_separator = NULL,
    
        number_format_labels_transform_labels = NULL,
    
        number_format_labels_transform = NULL,
    
        number_format_labels_multiply_divide_constant = NULL,
    
        number_format_labels_exponentiate_constant = NULL,
    
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
    
        number_format_prop = NULL,
    
        chart_secondary_number_date_format_prefix = NULL,
    
        chart_secondary_number_date_format_suffix = NULL,
    
        chart_secondary_number_date_format_n_dec = NULL,
    
        chart_secondary_number_date_format_advanced = NULL,
    
        chart_secondary_number_date_format_negative_sign = NULL,
    
        chart_secondary_number_date_format_strip_zeros = NULL,
    
        chart_secondary_number_date_format_strip_separator = NULL,
    
        chart_secondary_number_date_format_transform_labels = NULL,
    
        chart_secondary_number_date_format_transform = NULL,
    
        chart_secondary_number_date_format_multiply_divide_constant = NULL,
    
        chart_secondary_number_date_format_exponentiate_constant = NULL,
    
        legend_mode = NULL,
    
        legend_filter_mode = NULL,
    
        chart_legend_container_alignment = NULL,
    
        chart_legend_container_orientation = NULL,
    
        chart_legend_container_title_weight = NULL,
    
        chart_legend_container_text_weight = NULL,
    
        chart_legend_container_text_color = NULL,
    
        chart_legend_container_text_size = NULL,
    
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
    
        legend_position = NULL,
    
        text_legend = NULL,
    
        text_legend_title = NULL,
    
        text_legend_subtitle = NULL,
    
        text_legend_bold = NULL,
    
        chart_popup_mode = NULL,
    
        chart_popup_popup_is_custom = NULL,
    
        chart_popup_show_popup_styles = NULL,
    
        chart_popup_popup_custom_header = NULL,
    
        chart_popup_popup_custom_main = NULL,
    
        chart_popup_popup_custom_accessible = NULL,
    
        chart_popup_popup_width = NULL,
    
        chart_popup_popup_font_size = NULL,
    
        chart_popup_popup_text_color = NULL,
    
        chart_popup_popup_align = NULL,
    
        chart_popup_popup_background = NULL,
    
        chart_popup_popup_background_opacity = NULL,
    
        chart_popup_popup_padding = NULL,
    
        chart_popup_popup_radius = NULL,
    
        chart_popup_popup_header_type = NULL,
    
        chart_popup_popup_header_background = NULL,
    
        chart_popup_popup_header_text_color = NULL,
    
        chart_popup_popup_list_type = NULL,
    
        chart_popup_popup_list_label_weight = NULL,
    
        chart_popup_popup_list_separator = NULL,
    
        chart_popup_popup_shadow = NULL,
    
        chart_popup_popup_pointer = NULL,
    
        chart_popup_panel_position = NULL,
    
        chart_popup_panel_open_duration = NULL,
    
        chart_popup_panel_side_fixed = NULL,
    
        chart_popup_panel_side_default_content = NULL,
    
        chart_popup_panel_is_custom = NULL,
    
        chart_popup_show_panel_styles = NULL,
    
        chart_popup_panel_custom_header = NULL,
    
        chart_popup_panel_custom_main = NULL,
    
        chart_popup_panel_width_overlay = NULL,
    
        chart_popup_panel_height_overlay = NULL,
    
        chart_popup_panel_width_side = NULL,
    
        chart_popup_panel_height_side = NULL,
    
        chart_popup_panel_max_width = NULL,
    
        chart_popup_panel_max_height = NULL,
    
        chart_popup_panel_vertical_position = NULL,
    
        chart_popup_panel_text_color = NULL,
    
        chart_popup_panel_font_size = NULL,
    
        chart_popup_panel_align = NULL,
    
        chart_popup_panel_background = NULL,
    
        chart_popup_panel_background_opacity = NULL,
    
        chart_popup_panel_padding = NULL,
    
        chart_popup_panel_radius = NULL,
    
        chart_popup_panel_list_type = NULL,
    
        chart_popup_panel_list_label_weight = NULL,
    
        chart_popup_panel_list_separator = NULL,
    
        chart_popup_panel_shadow = NULL,
    
        popup_color_headers = NULL,
    
        show_series_text = NULL,
    
        popup_series_text = NULL,
    
        chart_axes_highlights_placement = NULL,
    
        chart_axes_highlights_x_enabled = NULL,
    
        chart_axes_highlights_x_lines = NULL,
    
        chart_axes_highlights_x_line_color = NULL,
    
        chart_axes_highlights_x_line_width = NULL,
    
        chart_axes_highlights_x_line_dash = NULL,
    
        chart_axes_highlights_x_areas = NULL,
    
        chart_axes_highlights_x_area_color = NULL,
    
        chart_axes_highlights_x_area_opacity = NULL,
    
        chart_axes_highlights_x_area_texture = NULL,
    
        chart_axes_highlights_x_label_vertical = NULL,
    
        chart_axes_highlights_x_label_y_position = NULL,
    
        chart_axes_highlights_x_label_x_position = NULL,
    
        chart_axes_highlights_x_label_max_width = NULL,
    
        chart_axes_highlights_x_font_size = NULL,
    
        chart_axes_highlights_x_font_weight = NULL,
    
        chart_axes_highlights_x_label_color = NULL,
    
        chart_axes_highlights_x_shadow_color = NULL,
    
        chart_axes_highlights_x_shadow_enabled = NULL,
    
        chart_axes_highlights_y_enabled = NULL,
    
        chart_axes_highlights_y_lines = NULL,
    
        chart_axes_highlights_y_line_color = NULL,
    
        chart_axes_highlights_y_line_width = NULL,
    
        chart_axes_highlights_y_line_dash = NULL,
    
        chart_axes_highlights_y_areas = NULL,
    
        chart_axes_highlights_y_area_color = NULL,
    
        chart_axes_highlights_y_area_opacity = NULL,
    
        chart_axes_highlights_y_area_texture = NULL,
    
        chart_axes_highlights_y_label_x_position = NULL,
    
        chart_axes_highlights_y_label_y_position = NULL,
    
        chart_axes_highlights_y_label_max_width = NULL,
    
        chart_axes_highlights_y_font_size = NULL,
    
        chart_axes_highlights_y_font_weight = NULL,
    
        chart_axes_highlights_y_label_color = NULL,
    
        chart_axes_highlights_y_shadow_color = NULL,
    
        chart_axes_highlights_y_shadow_enabled = NULL,
    
        annotations_styles = NULL,
    
        chart_annotations_defaults_text_weight = NULL,
    
        chart_annotations_defaults_text_size = NULL,
    
        chart_annotations_defaults_text_color = NULL,
    
        chart_annotations_defaults_label_width = NULL,
    
        chart_annotations_defaults_text_background_mode = NULL,
    
        chart_annotations_defaults_text_bg = NULL,
    
        chart_annotations_defaults_label_bg = NULL,
    
        chart_annotations_defaults_text_alignment = NULL,
    
        chart_annotations_defaults_popup_position = NULL,
    
        chart_annotations_defaults_line_marker = NULL,
    
        chart_annotations_defaults_stroke_width = NULL,
    
        chart_annotations_defaults_stroke_color = NULL,
    
        chart_annotations_defaults_connector_extend_line = NULL,
    
        data_trans_duration = NULL,
    
        animate_on_load = NULL,
    
        data_trans_bind_series = NULL,
    
        data_trans_bind_data_points = NULL,
    
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
    
        chart_layout_screenreader_hide_primary = NULL,
    
        chart_url_settings_enabled = NULL,
    
        chart_url_settings_whitelist = NULL
    
        )

R

Copy

## Arguments

PythonPython

RR

Arguments| Type hint| Description  
---|---|---  
`self`| `Flourish`| Returns the Flourish object  
`dual_axis`| `bool`, optional| Axis type. Choices: False, True. Flourish type hint: boolean, defaults to None  
`secondary_series`| `float`, optional| Number of combo lines. In line-bar mode , sets how many of your value columns are treated as lines. In line-line mode , sets how many lines use the right axis. The order counts from the start, so if you want column B as a line and A as a column, set the order in the column bindings to "B, A". Flourish type hint: number, defaults to None  
`stack_sort`| `str`, optional| Stack sort mode. Choices: data, ascending, descending. Whether each stack is in the default order or sorted by value. Use ascending or descending with a stacked area chart to make a "bump" area chart. Flourish type hint: string, defaults to None  
`facet_layout`| `str`, optional| Grid mode. Choices: single, facets. By default, Grid of charts creates a mini chart for each series. If Grid of charts is set in your column bindings, a mini chart will be created for each unique value in your specified column. Flourish type hint: string, defaults to None  
`height_mode`| `str`, optional| Height mode. Choices: auto, fill_space, aspect. Auto: sets the height based on the chart type, data and width. Standard: uses the default Flourish responsive sizing. Aspect ratio: sets the aspect of each plot. This setting is ignored when embedded in a fixed-height context, such as a simple iframe embedFlourish type hint: string, defaults to None  
`facet_aspect`| `float`, optional| Aspect (desktop). Aspect ratio of each plot in desktop mode, where 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to None  
`facet_aspect_mobile`| `float`, optional| Aspect (mobile). Aspect of each plot in mobile mode, where 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to None  
`facet_aspect_breakpoint`| `float`, optional| Breakpoint. The width at which mobile mode ends and desktop begins. Flourish type hint: number, defaults to None  
`sort_mode`| `str`, optional| Sort mode. Choices: data, value, label. Flourish type hint: string, defaults to None  
`chart_facet_columns_fixed`| `bool`, optional| Number of columns. Choices: False, True. In Auto mode, the number of columns will change with screen size. Flourish type hint: boolean, defaults to None  
`chart_facet_min_width`| `float`, optional| Min chart width. Determines how many columns of charts are displayed in the grid. Ignored if you specify a fixed number of columns. Flourish type hint: number, defaults to None  
`chart_facet_max_width`| `float`, optional| Max chart width. Determines how many columns of charts are in the grid. Ignored if you specify a fixed number of columns. Flourish type hint: number, defaults to None  
`chart_facet_columns`| `float`, optional| Fixed number of columns. Flourish type hint: number, defaults to None  
`chart_facet_gutter_w`| `float`, optional| Horizontal margin. Flourish type hint: number, defaults to None  
`chart_facet_gutter_h`| `float`, optional| Vertical margin. Flourish type hint: number, defaults to None  
`chart_facet_animation`| `str`, optional| On data change. Choices: auto, name, reuse. If a chart in the grid is removed, that cell can either be animated out (with another cell moving to take its place) or reused for the new data in that cell. Auto decides for you based on the data. Flourish type hint: string, defaults to None  
`chart_facet_titles`| `bool`, optional| Show titles. Flourish type hint: boolean, defaults to None  
`chart_facet_title_align`| `str`, optional| Alignment. Choices: auto, left, center, right. Flourish type hint: string, defaults to None  
`chart_facet_title_size`| `float`, optional| Size. Relative to the width of the chart. Flourish type hint: number, defaults to None  
`chart_facet_title_unit`| `str`, optional| Scale with chart. Choices: rem, facet. Flourish type hint: string, defaults to None  
`chart_facet_title_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_facet_title_padding_top`| `float`, optional| Space above. Flourish type hint: number, defaults to None  
`chart_facet_title_padding_bottom`| `float`, optional| Space below. Flourish type hint: number, defaults to None  
`chart_facet_title_bg`| `str`, optional| Background. Choices: none, full, text. Flourish type hint: string, defaults to None  
`chart_facet_title_bg_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_facet_title_bg_padding`| `float`, optional| Padding. Horizontal space between text and background. Flourish type hint: number, defaults to None  
`x_axis_matching`| `bool`, optional| Same across grid. Ensure the X scale is the same across the grid. Flourish type hint: boolean, defaults to None  
`x_axis_last_row_only`| `bool`, optional| Last row only. Only show the X axis on the last row, where possible. Ignored if the X axis is not positioned at the bottom. Flourish type hint: boolean, defaults to None  
`y_axis_matching`| `bool`, optional| Same across grid. Ensure the Y scale is the same across the grid. Flourish type hint: boolean, defaults to None  
`y_axis_first_col_only`| `bool`, optional| First column only. Only show the Y axis on the first column of the grid, where possible. Flourish type hint: boolean, defaults to None  
`y2_axis_matching`| `bool`, optional| Same across grid. Ensure the secondary Y scale is the same across the grid. Flourish type hint: boolean, defaults to None  
`y2_axis_last_col_only`| `bool`, optional| Last column only. Only show the secondary Y axis on the last column of the grid, where possible. Flourish type hint: boolean, defaults to None  
`series_filter_mode`| `str`, optional| Series filter. Choices: none, single, multi. Filter control for series/columns. The user can also filter by clicking on the legend, except in single select mode. Use the animation settings panel to determine whether series animate when changing the filter. Flourish type hint: string, defaults to None  
`series_control_multi_text`| `str`, optional| Placeholder text. Flourish type hint: string, defaults to None  
`series_control_multi_none_text`| `str`, optional| No more results text. Flourish type hint: string, defaults to None  
`series_control_select_text`| `str`, optional| Select text. Flourish type hint: string, defaults to None  
`max_series`| `float`, optional| Max series to show. Limits the number of series/columns that will be visualized at once. Flourish type hint: number, defaults to None  
`series_control_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`series_control_text`| `str`, optional| Text. Flourish type hint: color, defaults to None  
`series_control_border`| `str`, optional| Border. Flourish type hint: color, defaults to None  
`series_control_pill_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`series_control_pill_text`| `str`, optional| Text. Flourish type hint: color, defaults to None  
`series_control_pill_radius`| `float`, optional| Border radius. Flourish type hint: number, defaults to None  
`series_control_single_all`| `bool`, optional| Include "All". Flourish type hint: boolean, defaults to None  
`series_control_single_all_text`| `str`, optional| Name for "All". Flourish type hint: string, defaults to None  
`filter_rows_with_no_data`| `bool`, optional| Filter rows that have no data. This setting filters rows that have no data, this is useful in combination with filters and datasets that have a lot of empty cells. Flourish type hint: boolean, defaults to None  
`chart_series_filter_controls_control_type`| `str`, optional| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to None  
`chart_series_filter_controls_control_styles`| `bool`, optional| Adv. Flourish type hint: boolean, defaults to None  
`chart_series_filter_controls_control_title`| `str`, optional| Control title. Flourish type hint: string, defaults to None  
`chart_series_filter_controls_button_group`| `bool`, optional| Grouped. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_series_filter_controls_button_group_width_mode`| `str`, optional| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_series_filter_controls_button_group_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_series_filter_controls_dropdown_width_mode`| `str`, optional| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_series_filter_controls_dropdown_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_series_filter_controls_slider_width`| `float`, optional| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to None  
`chart_series_filter_controls_slider_max_label_width`| `float`, optional| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to None  
`chart_series_filter_controls_slider_step_time`| `float`, optional| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to None  
`chart_series_filter_controls_slider_loop`| `bool`, optional| Loop. Flourish type hint: boolean, defaults to None  
`chart_series_filter_controls_slider_restart_pause`| `float`, optional| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to None  
`chart_series_filter_controls_sort`| `bool`, optional| Sorting. Choices: True, False. Flourish type hint: boolean, defaults to None  
`row_filter_control_all`| `bool`, optional| Include "All". Flourish type hint: boolean, defaults to None  
`row_filter_control_all_text`| `str`, optional| Name for "All". Flourish type hint: string, defaults to None  
`chart_row_filter_controls_control_type`| `str`, optional| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to None  
`chart_row_filter_controls_control_styles`| `bool`, optional| Adv. Flourish type hint: boolean, defaults to None  
`chart_row_filter_controls_control_title`| `str`, optional| Control title. Flourish type hint: string, defaults to None  
`chart_row_filter_controls_button_group`| `bool`, optional| Grouped. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_row_filter_controls_button_group_width_mode`| `str`, optional| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_row_filter_controls_button_group_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_row_filter_controls_dropdown_width_mode`| `str`, optional| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_row_filter_controls_dropdown_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_row_filter_controls_slider_width`| `float`, optional| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to None  
`chart_row_filter_controls_slider_max_label_width`| `float`, optional| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to None  
`chart_row_filter_controls_slider_step_time`| `float`, optional| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to None  
`chart_row_filter_controls_slider_loop`| `bool`, optional| Loop. Flourish type hint: boolean, defaults to None  
`chart_row_filter_controls_slider_restart_pause`| `float`, optional| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to None  
`chart_row_filter_controls_sort`| `bool`, optional| Sorting. Choices: True, False. Flourish type hint: boolean, defaults to None  
`log_control_y_visible`| `bool`, optional| Show log control for Y axis. Adds a tabbed control to allow users to switch between log and linear Y scales. Flourish type hint: boolean, defaults to None  
`chart_log_control_y_filter_controls_control_type`| `str`, optional| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to None  
`chart_log_control_y_filter_controls_control_styles`| `bool`, optional| Adv. Flourish type hint: boolean, defaults to None  
`chart_log_control_y_filter_controls_control_title`| `str`, optional| Control title. Flourish type hint: string, defaults to None  
`chart_log_control_y_filter_controls_button_group`| `bool`, optional| Grouped. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_log_control_y_filter_controls_button_group_width_mode`| `str`, optional| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_log_control_y_filter_controls_button_group_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_log_control_y_filter_controls_dropdown_width_mode`| `str`, optional| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_log_control_y_filter_controls_dropdown_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_log_control_y_filter_controls_slider_width`| `float`, optional| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to None  
`chart_log_control_y_filter_controls_slider_max_label_width`| `float`, optional| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to None  
`chart_log_control_y_filter_controls_slider_step_time`| `float`, optional| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to None  
`chart_log_control_y_filter_controls_slider_loop`| `bool`, optional| Loop. Flourish type hint: boolean, defaults to None  
`chart_log_control_y_filter_controls_slider_restart_pause`| `float`, optional| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to None  
`chart_log_control_y_filter_controls_sort`| `bool`, optional| Sorting. Choices: True, False. Flourish type hint: boolean, defaults to None  
`log_control_y_text_linear`| `str`, optional| Linear text. Flourish type hint: string, defaults to None  
`log_control_y_text_log`| `str`, optional| Log text. Flourish type hint: string, defaults to None  
`chart_controls_style_font_size`| `float`, optional| Text size. Flourish type hint: number, defaults to None  
`chart_controls_style_font_weight`| `str`, optional| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_controls_style_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`chart_dropdown_control_style_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`chart_dropdown_control_style_font_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`chart_dropdown_control_style_border_styles_advanced`| `bool`, optional| Dropdown border styles. Flourish type hint: boolean, defaults to None  
`chart_dropdown_control_style_border_style`| `str`, optional| Border style. Choices: all, bottom. Show border on all sides, or only at the bottom. Flourish type hint: string, defaults to None  
`chart_dropdown_control_style_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`chart_dropdown_control_style_border_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_dropdown_control_style_border_transparency`| `float`, optional| Transparency. Flourish type hint: number, defaults to None  
`chart_dropdown_control_style_border_radius`| `float`, optional| Radius. Flourish type hint: number, defaults to None  
`chart_button_control_style_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`chart_button_control_style_background_selected`| `str`, optional| Selected. Flourish type hint: color, defaults to None  
`chart_button_control_style_background_hover`| `str`, optional| Mouse over. Flourish type hint: color, defaults to None  
`chart_button_control_style_font_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`chart_button_control_style_font_color_selected`| `str`, optional| Selected. Flourish type hint: color, defaults to None  
`chart_button_control_style_font_color_hover`| `str`, optional| Mouse over. Flourish type hint: color, defaults to None  
`chart_button_control_style_button_styles_advanced`| `bool`, optional| Button border styles. Flourish type hint: boolean, defaults to None  
`chart_button_control_style_border_width`| `float`, optional| Border width. Flourish type hint: number, defaults to None  
`chart_button_control_style_border_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_button_control_style_border_transparency`| `float`, optional| Transparency. Flourish type hint: number, defaults to None  
`chart_button_control_style_border_radius`| `float`, optional| Radius. Flourish type hint: number, defaults to None  
`chart_filter_controls_container_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`chart_filter_controls_container_controls_spacing`| `float`, optional| Spacing. The space between controls, like dropdowns and adjacent button sets, in em units. Flourish type hint: number, defaults to None  
`controls_position`| `str`, optional| Control position. Choices: log_series_row, series_log_row, log_row_series, series_row_log, row_log_series, row_series_log. If you have two or more controls turned on for your chart, you can change the order the controls appear. Flourish type hint: string, defaults to None  
`color_mode`| `str`, optional| Color mode. Choices: column, row. By column will set the colors by series. Each column listed in the value column binding in the datasheet will have a different color. By row will instead set the color depending on the datas label/time column binding. Flourish type hint: string, defaults to None  
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
`line_width`| `float`, optional| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`line_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`line_stroke`| `bool`, optional| Outline. Add a stroke around your lines to enhance visibility when overlapping. Flourish type hint: boolean, defaults to None  
`line_curve`| `str`, optional| Line curve. Choices: curve_linear, curve_monotone_x, curve_natural, curve_step, curve_step_before, curve_step_after. Flourish type hint: string, defaults to None  
`line_dash_items`| `Union[list, str]`, optional| Dashed lines. Specify the series that you would like to display with a dashed line. Multiple dashed lines can be set using multiple lines. For example: Party 1 Party 2 Party 3. Flourish type hint: text, defaults to None  
`line_dash_width`| `float`, optional| Dash width. Flourish type hint: number, defaults to None  
`line_dash_space_width`| `float`, optional| Space width. Flourish type hint: number, defaults to None  
`line_interpolate`| `bool`, optional| Missing data points. Choices: True, False. Flourish type hint: boolean, defaults to None  
`shade_between_lines`| `bool`, optional| Shade areas between lines. Shade the gap between any two lines on your chart. Flourish type hint: boolean, defaults to None  
`shade_between_lines_config`| `Union[list, str]`, optional| Which lines to shade between. Specify each area as a pair of line names separated by `::`. For example: Series A :: Series B Series C :: Series D You can optionally add a specific color and opacity for each area, e.g. `Series A :: Series B :: red :: 0.1`. Flourish type hint: text, defaults to None  
`shade_between_lines_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`shade_between_lines_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`area_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`dot_mode`| `str`, optional| Choices: auto, on, off. " Auto will automatically show dots on lines if fewer than 250 data points. Note: avoid showing dots for large datasets since it can lead to poor performance issues and poor-looking charts". Flourish type hint: string, defaults to None  
`dot_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`dot_radius`| `float`, optional| Radius. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`dot_radius_last`| `float`, optional| Final dot scale (%). Making the last point on a line larger can help emphasise the final value. This will usually be the dot furthest right on the axis. Flourish type hint: number, defaults to None  
`dot_hollow`| `bool`, optional| Hollow. Flourish type hint: boolean, defaults to None  
`bar_height`| `float`, optional| Bar height. The approximate height of the bar, the exact height depends on padding and label style. Specified in rems Ignored if the chart is embedded at a fixed height. Flourish type hint: number, defaults to None  
`column_opacity`| `float`, optional| Bar opacity. Flourish type hint: number, defaults to None  
`uniform_column_width`| `bool`, optional| Uniform column width. Flourish type hint: boolean, defaults to None  
`uniform_bar_height`| `bool`, optional| Uniform bar height. Flourish type hint: boolean, defaults to None  
`column_padding_inner`| `float`, optional| Spacing (main). Space between bar stacks or groups, as a % of the width of a whole bar stack or group. Flourish type hint: number, defaults to None  
`column_padding_in_group`| `float`, optional| Spacing (in group). Space between bars in groups, as a % of the width of a single bar in the group. Ignored if only a single series is selected. Flourish type hint: number, defaults to None  
`column_padding_stack`| `float`, optional| Spacing (in stack). Space each bar in the stack, in tenths of a rem Flourish type hint: number, defaults to None  
`column_stroke`| `bool`, optional| Outline. Add a stroke around your columns or bars (same color as text). Flourish type hint: boolean, defaults to None  
`column_stroke_opacity`| `float`, optional| Outline opacity. Flourish type hint: number, defaults to None  
`column_stroke_color`| `str`, optional| Outline color. Flourish type hint: color, defaults to None  
`donut_inner_radius`| `float`, optional| Doughnut hole (%). Flourish type hint: number, defaults to None  
`donut_corner_radius`| `float`, optional| Corner curve (pixels). Flourish type hint: number, defaults to None  
`donut_pad_angle`| `float`, optional| Segment padding (degrees). Flourish type hint: number, defaults to None  
`donut_auto_scale`| `bool`, optional| Scale pies based on data. Scale each pie chart in the grid so that the area of each pie/donut reflect its value. Flourish type hint: boolean, defaults to None  
`bar_labels_above`| `bool`, optional| Label style. Choices: True, False. Flourish type hint: boolean, defaults to None  
`bar_labels_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`bar_labels_font_size`| `float`, optional| Size. When in Standard or Aspect ratio height mode, the font size of the labels will be limited to the space available. In remsFlourish type hint: number, defaults to None  
`bar_labels_weight`| `str`, optional| Choices: 600, 400. Flourish type hint: string, defaults to None  
`line_end_labels`| `bool`, optional| Show labels on lines. Show series labels on the end of lines if theres enough space. Flourish type hint: boolean, defaults to None  
`chart_line_labels_max_width`| `float`, optional| Max label width. The maximum allowed label width. Flourish type hint: number, defaults to None  
`chart_line_labels_overlap_mode`| `str`, optional| Overlaps. Choices: spread, hide, none. What to do with overlaps. Flourish type hint: string, defaults to None  
`chart_line_labels_spreading_margin`| `float`, optional| Space between labels. The space left between labels when spreading them out to avoid overlaps. Flourish type hint: number, defaults to None  
`chart_line_labels_data_point_margin`| `float`, optional| Distance. The space between the data point and the label in rems (a multiple of base font size). Flourish type hint: number, defaults to None  
`chart_line_labels_show_only_labels`| `Union[list, str]`, optional| Show only certain labels. Manually specify which labels youd like to display (one entry per line that should match headers from the Values columns). Flourish type hint: text, defaults to None  
`chart_line_labels_text_color`| `str`, optional| Color. If cleared, uses the main text color from the Layout settings panel. Flourish type hint: color, defaults to None  
`chart_line_labels_text_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_line_labels_text_bg_color`| `str`, optional| Outline. If cleared, uses the main background color from the Layout settings panel. Flourish type hint: color, defaults to None  
`chart_line_labels_text_bg_size`| `float`, optional| Outline width. As a % of the font size. Flourish type hint: number, defaults to None  
`chart_line_labels_text_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`chart_line_labels_text_max_lines`| `float`, optional| Max lines. The max number of lines for each label. Flourish type hint: number, defaults to None  
`chart_line_labels_text_weight`| `str`, optional| Weight. Choices: 400, 700. Flourish type hint: string, defaults to None  
`chart_line_labels_lines`| `str`, optional| Connector lines. Choices: auto, on, off. Flourish type hint: string, defaults to None  
`chart_line_labels_line_style`| `str`, optional| Line style. Choices: straight, step. Flourish type hint: string, defaults to None  
`chart_line_labels_line_color`| `str`, optional| Color. If cleared, uses the main text color from the Layout settings panel. Flourish type hint: color, defaults to None  
`chart_line_labels_line_width`| `float`, optional| Width. In rems (a multiple of base font size). Flourish type hint: number, defaults to None  
`chart_line_labels_line_range`| `float`, optional| Length. The width of the space given over to lines; in rems, a multiple of base font size. Flourish type hint: number, defaults to None  
`chart_line_labels_line_padding`| `float`, optional| Padding. The padding to the left and right of the line; in rems, a multiple of base font size. Flourish type hint: number, defaults to None  
`labels`| `bool`, optional| Show labels on data points. Flourish type hint: boolean, defaults to None  
`labels_hide_overlaps`| `bool`, optional| Hide overlapping labels. Flourish type hint: boolean, defaults to None  
`labels_dot_center`| `bool`, optional| Position labels on center of dot. Flourish type hint: boolean, defaults to None  
`labels_column_align`| `str`, optional| Bar label alignment. Choices: bottom, middle, top, above. The final above option puts the labels above the bars in standard column charts. In stacked charts, where the space above the stack is reserved for stack total the labels falls back to top alignment. Flourish type hint: string, defaults to None  
`labels_column_padding`| `float`, optional| Padding. Space above or below, as a proportion of the font size in rems Flourish type hint: number, defaults to None  
`labels_bar_align`| `str`, optional| Label alignment. Choices: left, center, right, out. In stacked bar charts the final out (outside of bar) option falls back to right alignment, since the space after the stack is reserved for stack total labels (see below). Flourish type hint: string, defaults to None  
`labels_bar_autohide`| `bool`, optional| Hide if too big. Turn off to force labels to show, even if they will overflow the bars. Ignored when labels are not inside the bars. Flourish type hint: boolean, defaults to None  
`labels_color_mode`| `str`, optional| Text color. Choices: auto, data, contrast, fixed. Contrast mode is black or white depending on the color of the data point (or the background color for labels positioned over the background). Flourish type hint: string, defaults to None  
`labels_fixed_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`labels_font_weight`| `str`, optional| Weight. Choices: 600, 400. Flourish type hint: string, defaults to None  
`labels_font_size_mode`| `str`, optional| Size. Choices: auto, fixed. Flourish type hint: string, defaults to None  
`labels_font_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`labels_bg_mode`| `str`, optional| Outline. Choices: on, off. A text outline/background can make the text more readable by increasing contrast. Flourish type hint: string, defaults to None  
`labels_bg_size`| `float`, optional| Size. Size of the background, as % of text size. Flourish type hint: number, defaults to None  
`labels_content`| `str`, optional| Label content. Choices: auto, value, label, both. Flourish type hint: string, defaults to None  
`stack_labels`| `bool`, optional| Show labels for stack totals. Flourish type hint: boolean, defaults to None  
`stack_labels_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`stack_labels_font_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`stack_labels_weight`| `str`, optional| Weight. Choices: 600, 400. Flourish type hint: string, defaults to None  
`chart_x_axis_axis_position`| `str`, optional| Position. Choices: bottom, float-below, float-above, top, off. Flourish type hint: string, defaults to None  
`chart_x_axis_y_axis_position`| `str`, optional| Y value. Vertical position of the x axis on the y scale. Flourish type hint: string, defaults to None  
`chart_x_axis_numeric_scale_type`| `str`, optional| Type. Choices: linear, log. Flourish type hint: string, defaults to None  
`chart_x_axis_linear_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_x_axis_linear_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_x_axis_log_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_x_axis_log_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_x_axis_datetime_min`| `str`, optional| Min (date). Use the input date format as specified in the datasheet. Flourish type hint: string, defaults to None  
`chart_x_axis_datetime_max`| `str`, optional| Max (date). Use the input date format as specified in the datasheet. Flourish type hint: string, defaults to None  
`chart_x_axis_flip`| `bool`, optional| Flip axis. Flourish type hint: boolean, defaults to None  
`chart_x_axis_show_scale_settings`| `bool`, optional| Configure default min/max. Flourish type hint: boolean, defaults to None  
`chart_x_axis_nice`| `bool`, optional| Round min/max. Choices: True, False. When enabled, scales automatically extend to "nice" rounded start/end values, such as hundreds or whole years. Overridden by any explicitly specified scale min and max. Flourish type hint: boolean, defaults to None  
`chart_x_axis_zero_axis`| `str`, optional| Include zero. Choices: auto, on, off. Whether to extend the axis to include zero if the data values are all positive or all negative. Overridden by any explicitly specified scale min and max. Flourish type hint: string, defaults to None  
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
`chart_x_axis_tick_label_space_mode`| `str`, optional| Space mode. Choices: auto, max, fixed. How the vertical space available for tick labels is determined. "Auto" means that the space is automatically determined. "Max" lets you specify the maximum vertical space tick labels may occupy. "Fixed" lets you specify a fixed amount of vertical space for tick labels. Tick labels will be truncated to fit within the allocated horizontal space. Flourish type hint: string, defaults to None  
`chart_x_axis_tick_label_space`| `float`, optional| Space. The space allocated for tick labels (relative to the root font size). Flourish type hint: number, defaults to None  
`chart_x_axis_tick_mode`| `str`, optional| Mode. Choices: auto, number, custom. Determines how the tick values are chosen. "Auto" mode chooses the ticks automatically. "Number" mode lets you specify how many ticks are drawn. "Custom" mode lets you specify which ticks are drawn. If the axis is categorical, "Number" mode is ignored. Flourish type hint: string, defaults to None  
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
`chart_x_axis_gridline_category_dividers`| `bool`, optional| Put lines between categories. On a categorical axis this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Flourish type hint: boolean, defaults to None  
`chart_x_axis_gridline_category_dividers_extend`| `bool`, optional| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to None  
`chart_y_axis_axis_visible`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_y_axis_numeric_scale_type`| `str`, optional| Type. Choices: linear, log. Flourish type hint: string, defaults to None  
`chart_y_axis_linear_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_y_axis_linear_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_y_axis_log_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_y_axis_log_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_y_axis_datetime_min`| `str`, optional| Min (date). Use the same format as displayed in the axis. Flourish type hint: string, defaults to None  
`chart_y_axis_datetime_max`| `str`, optional| Max (date). Use the same format as displayed in the axis. Flourish type hint: string, defaults to None  
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
`chart_y_axis_tick_label_space_mode`| `str`, optional| Space mode. Choices: auto, max, fixed. Sets how the horizontal space available for tick labels is determined. "Auto" means that the space is automatically determined. "Max" lets you specify the maximum horizontal space tick labels may occupy. "Fixed" lets you specify a fixed amount of horizontal space for tick labels. Tick labels will be truncated to fit within the allocated horizontal space. Flourish type hint: string, defaults to None  
`chart_y_axis_tick_label_space`| `float`, optional| Space. The space allocated for tick labels (relative to the root font size). Flourish type hint: number, defaults to None  
`chart_y_axis_tick_mode`| `str`, optional| Mode. Choices: auto, number, custom. Determines how the tick values are chosen. "Auto" mode chooses the ticks automatically. "Number" mode lets you specify how many ticks are drawn. "Custom" mode lets you specify which ticks are drawn. If the axis is categorical, "Number" mode is ignored. Flourish type hint: string, defaults to None  
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
`chart_y_axis_gridline_category_dividers`| `bool`, optional| Put lines between categories. On a categorical axis this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Ignored for date and numeric axes. Flourish type hint: boolean, defaults to None  
`chart_y_axis_gridline_category_dividers_extend`| `bool`, optional| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_axis_visible`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_numeric_scale_type`| `str`, optional| Type. Choices: linear, log. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_linear_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_linear_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_log_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_log_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_datetime_min`| `str`, optional| Min (date). Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_datetime_max`| `str`, optional| Max (date). Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_flip`| `bool`, optional| Flip axis. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_show_scale_settings`| `bool`, optional| Configure default min/max. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_nice`| `bool`, optional| Round min/max. Choices: True, False. When enabled, scales automatically extend to "nice" rounded start/end values, such as hundreds or whole years. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_zero_axis`| `str`, optional| Include zero. Choices: auto, on, off. Whether to extend the axis to include zero if the data values are all positive or all negative. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_title_mode`| `str`, optional| Type. Choices: auto, custom. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_title`| `str`, optional| Text. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_title_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_title_position`| `str`, optional| Position. Choices: side, end. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_title_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_title_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_secondary_y_axis_title_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_title_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_label_position`| `str`, optional| Position. Choices: default, above, below. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_tick_label_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_tick_label_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_label_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_secondary_y_axis_tick_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_label_angle`| `str`, optional| Angle. Choices: 0, 30, 45, 60, 90. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_tick_label_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_tick_label_max_lines`| `float`, optional| Max lines. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_label_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_label_space_mode`| `str`, optional| Space mode. Choices: auto, max, fixed. Sets how the horizontal space available for tick labels is determined. "Auto" means that the space is automatically determined. "Max" lets you specify the maximum horizontal space tick labels may occupy. "Fixed" lets you specify a fixed amount of horizontal space for tick labels. Tick labels will be truncated to fit within the allocated horizontal space. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_tick_label_space`| `float`, optional| Space. The space allocated for tick labels (relative to the root font size). Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_mode`| `str`, optional| Mode. Choices: auto, number, custom. Determines how the tick values are chosen. "Auto" mode chooses the ticks automatically. "Number" mode lets you specify how many ticks are drawn. "Custom" mode lets you specify which ticks are drawn. If the axis is categorical, "Number" mode is ignored. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_tick_number`| `float`, optional| Number. Approximate number of ticks or gridlines. The actual number will depend on the range of values, chart size, etc. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_custom`| `Union[list, str]`, optional| One tick label per line. Specify the ticks to show, one per line. For dates, use the input format as specified in the datasheet. You can also use `{{FIRST}}` and `{{LAST}}` to add ticks at the minimum and maximum of the axis. For example: `{{FIRST}}` 25000 50000 75000 `{{LAST}}`. Flourish type hint: text, defaults to None  
`chart_secondary_y_axis_line_and_tick_color`| `str`, optional| Line color. Flourish type hint: color, defaults to None  
`chart_secondary_y_axis_line_and_tick_width`| `float`, optional| Line width. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_length`| `float`, optional| Tick length. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_tick_side`| `str`, optional| Side. Choices: out, in. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_line_visible`| `bool`, optional| Axis line. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_edge_padding`| `float`, optional| Edge padding (%). Space between start/end of axis line and first/last category tick as a percentage of the spacing between ticks. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_gridlines_visible`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_gridlines_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_gridline_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_secondary_y_axis_gridline_style`| `str`, optional| Style. Choices: solid, dash, dot, dot_dash. Flourish type hint: string, defaults to None  
`chart_secondary_y_axis_gridline_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_secondary_y_axis_gridline_category_dividers`| `bool`, optional| Put lines between categories. On a categorical axis this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Ignored for date and numeric axes. Flourish type hint: boolean, defaults to None  
`chart_secondary_y_axis_gridline_category_dividers_extend`| `bool`, optional| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to None  
`chart_background_background_color_enabled`| `bool`, optional| Color. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_background_background_image_enabled`| `bool`, optional| Image. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_background_background_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_background_background_image_src`| `str`, optional| Image URL. Flourish type hint: url, defaults to None  
`chart_background_background_image_size`| `str`, optional| Size. Choices: stretch, slice, meet. Flourish type hint: string, defaults to None  
`chart_background_background_image_position`| `str`, optional| Position. Choices: x_min_y_min, x_mid_y_min, x_max_y_min, x_max_y_mid, x_mid_y_mid, x_min_y_max, x_mid_y_max, x_max_y_max. Flourish type hint: string, defaults to None  
`number_format_labels_prefix`| `str`, optional| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to None  
`number_format_labels_suffix`| `str`, optional| Suffix. Text to place after a number. Flourish type hint: string, defaults to None  
`number_format_labels_n_dec`| `float`, optional| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to None  
`number_format_labels_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`number_format_labels_negative_sign`| `str`, optional| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to None  
`number_format_labels_strip_zeros`| `bool`, optional| Remove trailing zeros. Flourish type hint: boolean, defaults to None  
`number_format_labels_strip_separator`| `bool`, optional| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to None  
`number_format_labels_transform_labels`| `bool`, optional| Multiply/divide values. Flourish type hint: boolean, defaults to None  
`number_format_labels_transform`| `str`, optional| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to None  
`number_format_labels_multiply_divide_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`number_format_labels_exponentiate_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_number_date_format_prefix`| `str`, optional| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to None  
`chart_number_date_format_suffix`| `str`, optional| Suffix. Text to place after a number. Flourish type hint: string, defaults to None  
`chart_number_date_format_n_dec`| `float`, optional| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to None  
`chart_number_date_format_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_number_date_format_negative_sign`| `str`, optional| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to None  
`chart_number_date_format_strip_zeros`| `bool`, optional| Remove trailing zeros. Flourish type hint: boolean, defaults to None  
`chart_number_date_format_strip_separator`| `bool`, optional| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to None  
`chart_number_date_format_transform_labels`| `bool`, optional| Multiply/divide values. Flourish type hint: boolean, defaults to None  
`chart_number_date_format_transform`| `str`, optional| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to None  
`chart_number_date_format_multiply_divide_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_number_date_format_exponentiate_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`number_format_prop`| `bool`, optional| Show % values. Toggles between showing the raw values from the datasheet and the computed percent values for the row in popups/panels. Flourish type hint: boolean, defaults to None  
`chart_secondary_number_date_format_prefix`| `str`, optional| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to None  
`chart_secondary_number_date_format_suffix`| `str`, optional| Suffix. Text to place after a number. Flourish type hint: string, defaults to None  
`chart_secondary_number_date_format_n_dec`| `float`, optional| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to None  
`chart_secondary_number_date_format_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_secondary_number_date_format_negative_sign`| `str`, optional| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to None  
`chart_secondary_number_date_format_strip_zeros`| `bool`, optional| Remove trailing zeros. Flourish type hint: boolean, defaults to None  
`chart_secondary_number_date_format_strip_separator`| `bool`, optional| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to None  
`chart_secondary_number_date_format_transform_labels`| `bool`, optional| Multiply/divide values. Flourish type hint: boolean, defaults to None  
`chart_secondary_number_date_format_transform`| `str`, optional| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to None  
`chart_secondary_number_date_format_multiply_divide_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_secondary_number_date_format_exponentiate_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`legend_mode`| `str`, optional| Legend mode. Choices: auto, on, off. Auto mode hides the legend in certain situations, such as when each color is already explained by the chart titles in a grid of charts A legend will not show with a single entry. Flourish type hint: string, defaults to None  
`legend_filter_mode`| `str`, optional| Click legend to filter data. Choices: none, filter-in, filter-out. Single select : When clicked only shows the series selected Multi select : When clicked, hides series selected. Multiple series can be hidden Filterable legends are ignored in certain situations, such as when shading by series and using a series filter Flourish type hint: string, defaults to None  
`chart_legend_container_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`chart_legend_container_orientation`| `str`, optional| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to None  
`chart_legend_container_title_weight`| `str`, optional| Title weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_legend_container_text_weight`| `str`, optional| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_legend_container_text_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_legend_container_text_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
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
`legend_position`| `str`, optional| Legend position. Choices: above, below. Flourish type hint: string, defaults to None  
`text_legend`| `str`, optional| Add data colors to header text. Choices: auto, custom, off. When selected, this will change the color of any text in your header which matches the name of a series in your data. This feature can be used instead of a legend when there are a small number of series, or it can be used to highlight a particular series. Note using optional HTML in the header is disabled if using this feature. Flourish type hint: string, defaults to None  
`text_legend_title`| `bool`, optional| Title. Flourish type hint: boolean, defaults to None  
`text_legend_subtitle`| `bool`, optional| Subtitle. Flourish type hint: boolean, defaults to None  
`text_legend_bold`| `bool`, optional| Bold. If checked, always use bold for colored items. Flourish type hint: boolean, defaults to None  
`chart_popup_mode`| `str`, optional| Choices: none, popup, panel, both. Flourish type hint: string, defaults to None  
`chart_popup_popup_is_custom`| `bool`, optional| Popup content. Choices: False, True. Flourish type hint: boolean, defaults to None  
`chart_popup_show_popup_styles`| `bool`, optional| Show popup styles. Flourish type hint: boolean, defaults to None  
`chart_popup_popup_custom_header`| `Union[list, str]`, optional| Popup custom header. Use `{{VALUE}}` to include the numerical value of the current data point, or `{{SERIES}}` to display its series name. For any other selected columns use `{{column_name}}`. Advanced users can include HTML to apply layouts, formatting, images, etc. You can also hide content based on a column name being empty using `{{#if column_name}} Text to display when column_name is not empty {{/if}}`. For example, `{{Country}}` `{{#if Capital}}(Capital: {{Capital}}){{/if}}` Flourish type hint: html, defaults to None  
`chart_popup_popup_custom_main`| `Union[list, str]`, optional| Popup custom main content. Use `{{VALUE}}` to include the numerical value of the current data point, or `{{SERIES}}` to display its series name. For any other selected columns use `{{column_name}}`. Advanced users can include HTML to apply layouts, formatting, images, etc. You can also hide content based on a column name being empty using `{{#if column_name}} Text to display when column_name is not empty {{/if}}`. For example, `{{Country}}` `{{#if Capital}}(Capital: {{Capital}}){{/if}}` Flourish type hint: html, defaults to None  
`chart_popup_popup_custom_accessible`| `Union[list, str]`, optional| Popup custom accessible content. A text alternative to visual custom popup content that will be read out by screenreaders. This content is added as an aria-label attribute to data point elements. You can still use `{{column_name}}` to add values from your data, but do not use HTML. For example: `{{Name}}, Population: {{Population}}, GDP: {{GDP}}`. If left empty, accessible content will fallback to the default popup content. Flourish type hint: text, defaults to None  
`chart_popup_popup_width`| `float`, optional| Max width. In rems, multiples of base font size. Leave blank to let the width adjust based on the contents. Flourish type hint: number, defaults to None  
`chart_popup_popup_font_size`| `float`, optional| Text size. Flourish type hint: number, defaults to None  
`chart_popup_popup_text_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`chart_popup_popup_align`| `str`, optional| Align. Choices: start, center, end. Flourish type hint: string, defaults to None  
`chart_popup_popup_background`| `str`, optional| Fill color. Flourish type hint: color, defaults to None  
`chart_popup_popup_background_opacity`| `float`, optional| Fill opacity. Flourish type hint: number, defaults to None  
`chart_popup_popup_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`chart_popup_popup_radius`| `float`, optional| Radius. Corner radius of popup. Flourish type hint: number, defaults to None  
`chart_popup_popup_header_type`| `str`, optional| Header style. Choices: block, inline. Flourish type hint: string, defaults to None  
`chart_popup_popup_header_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`chart_popup_popup_header_text_color`| `str`, optional| Text. Flourish type hint: color, defaults to None  
`chart_popup_popup_list_type`| `str`, optional| List type. Choices: table, ul. Flourish type hint: string, defaults to None  
`chart_popup_popup_list_label_weight`| `str`, optional| Label weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`chart_popup_popup_list_separator`| `str`, optional| List separator. Choices: :, , , `<br />`. Flourish type hint: string, defaults to None  
`chart_popup_popup_shadow`| `bool`, optional| Shadow. Flourish type hint: boolean, defaults to None  
`chart_popup_popup_pointer`| `bool`, optional| Pointer. Flourish type hint: boolean, defaults to None  
`chart_popup_panel_position`| `str`, optional| Choices: overlay, left, right, top, bottom. Flourish type hint: string, defaults to None  
`chart_popup_panel_open_duration`| `float`, optional| Open duration. Flourish type hint: number, defaults to None  
`chart_popup_panel_side_fixed`| `bool`, optional| Always show. Flourish type hint: boolean, defaults to None  
`chart_popup_panel_side_default_content`| `Union[list, str]`, optional| Placeholder content. Flourish type hint: text, defaults to None  
`chart_popup_panel_is_custom`| `bool`, optional| Panel content. Choices: False, True. Flourish type hint: boolean, defaults to None  
`chart_popup_show_panel_styles`| `bool`, optional| Show panel styles. Flourish type hint: boolean, defaults to None  
`chart_popup_panel_custom_header`| `Union[list, str]`, optional| Panel custom header. Use `{{VALUE}}` to include the numerical value of the current data point, or `{{SERIES}}` to display its series name. For any other selected columns use `{{column_name}}`. Advanced users can include HTML to apply layouts, formatting, images, etc. You can also hide content based on a column name being empty using `{{#if column_name}} Text to display when column_name is not empty {{/if}}`. For example, `{{Country}}` `{{#if Capital}}(Capital: {{Capital}}){{/if}}` Flourish type hint: html, defaults to None  
`chart_popup_panel_custom_main`| `Union[list, str]`, optional| Panel custom main content. Use `{{VALUE}}` to include the numerical value of the current data point, or `{{SERIES}}` to display its series name. For any other selected columns use `{{column_name}}`. Advanced users can include HTML to apply layouts, formatting, images, etc. You can also hide content based on a column name being empty using `{{#if column_name}} Text to display when column_name is not empty {{/if}}`. For example, `{{Country}}` `{{#if Capital}}(Capital: {{Capital}}){{/if}}` Flourish type hint: html, defaults to None  
`chart_popup_panel_width_overlay`| `float`, optional| Width (%). Flourish type hint: number, defaults to None  
`chart_popup_panel_height_overlay`| `float`, optional| Height (%). Flourish type hint: number, defaults to None  
`chart_popup_panel_width_side`| `float`, optional| Width (%). Flourish type hint: number, defaults to None  
`chart_popup_panel_height_side`| `float`, optional| Height (%). Flourish type hint: number, defaults to None  
`chart_popup_panel_max_width`| `float`, optional| Max width (px). Flourish type hint: number, defaults to None  
`chart_popup_panel_max_height`| `float`, optional| Max height (px). Flourish type hint: number, defaults to None  
`chart_popup_panel_vertical_position`| `str`, optional| Vertical position. Choices: click, center. Choosing Click position is especially useful when your visualization is really tall, this will make sure the panel content is always on top of the element youve clicked on. Flourish type hint: string, defaults to None  
`chart_popup_panel_text_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`chart_popup_panel_font_size`| `float`, optional| Text size. Flourish type hint: number, defaults to None  
`chart_popup_panel_align`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`chart_popup_panel_background`| `str`, optional| Fill color. Flourish type hint: color, defaults to None  
`chart_popup_panel_background_opacity`| `float`, optional| Fill opacity. Flourish type hint: number, defaults to None  
`chart_popup_panel_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`chart_popup_panel_radius`| `float`, optional| Radius. Corner radius of panel. Flourish type hint: number, defaults to None  
`chart_popup_panel_list_type`| `str`, optional| List type. Choices: table, ul. Flourish type hint: string, defaults to None  
`chart_popup_panel_list_label_weight`| `str`, optional| Label weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`chart_popup_panel_list_separator`| `str`, optional| List separator. Choices: :, , , `<br />`. Flourish type hint: string, defaults to None  
`chart_popup_panel_shadow`| `bool`, optional| Shadow. Flourish type hint: boolean, defaults to None  
`popup_color_headers`| `bool`, optional| Color headers to match data. Flourish type hint: boolean, defaults to None  
`show_series_text`| `bool`, optional| Set series info in popups. Allows you to add information about each series/column (e.g. each line) to the popups. Note: This is incompatible with custom popup content. Flourish type hint: boolean, defaults to None  
`popup_series_text`| `Union[list, str]`, optional| Popup content for series. Adds content to the popup about the series. Separate column name and text with a double colon. For example: Series 1 :: Comment about Series 1 Series 2 :: Comment about series 2. Flourish type hint: text, defaults to None  
`chart_axes_highlights_placement`| `str`, optional| Placement of axis highlights. Choices: above, below. Flourish type hint: string, defaults to None  
`chart_axes_highlights_x_enabled`| `bool`, optional| Show highlights on the x axis. Flourish type hint: boolean, defaults to None  
`chart_axes_highlights_x_lines`| `Union[list, str]`, optional| One per line, in format “My label :: 2012”. One per line, using the format : My label :: 2012 For dates, use the input format as specified in the datasheet. You can optionally specify a line color and a text color For visualizations using a grid of charts , you can apply the annotation only on a specific chart. Use the format: `My label :: 2012 :: line_color / text_color :: facet_name`. For example, `My label :: 2012 :: #eb0000 / #0084bd :: Category 1`. If you want to add an annotation to just one specific chart but do not want to color the line/text, you can leave that part blank. For example: My label :: 2012 :: :: Category 1 Flourish type hint: text, defaults to None  
`chart_axes_highlights_x_line_color`| `str`, optional| Line color. Flourish type hint: color, defaults to None  
`chart_axes_highlights_x_line_width`| `float`, optional| Line width. Flourish type hint: number, defaults to None  
`chart_axes_highlights_x_line_dash`| `float`, optional| Dash. Flourish type hint: number, defaults to None  
`chart_axes_highlights_x_areas`| `Union[list, str]`, optional| One per line, in format “My label :: 2013 >> 2015”. One per line, using the format : My label :: date >> date For dates, use the input format as specified in the datasheet. You can optionally specify a line color and a text color For visualizations using a grid of charts , you can apply the annotation only on a specific chart Use the format: My label :: 2012 :: area_color / text_color :: facet_name For example, `My label :: 2012 >> 2015 :: #eb0000 / #0084bd :: Category 1`. Flourish type hint: text, defaults to None  
`chart_axes_highlights_x_area_color`| `str`, optional| Area. Flourish type hint: color, defaults to None  
`chart_axes_highlights_x_area_opacity`| `float`, optional| Area opacity. Flourish type hint: number, defaults to None  
`chart_axes_highlights_x_area_texture`| `str`, optional| Area texture. Choices: none, pattern-diagonal, pattern-grid, pattern-dots. Flourish type hint: string, defaults to None  
`chart_axes_highlights_x_label_vertical`| `bool`, optional| Vertical. Flourish type hint: boolean, defaults to None  
`chart_axes_highlights_x_label_y_position`| `str`, optional| Y position. Choices: bottom, middle, top. Vertically position the label at the top, bottom or in the middle of the line. This setting will be ignored if there is not enough space for the selected position. Flourish type hint: string, defaults to None  
`chart_axes_highlights_x_label_x_position`| `str`, optional| X position. Choices: left, middle, right. Horizontally position the label on the left, the right or in the middle of the line. This setting will be ignored if there is not enough space for the selected position. Flourish type hint: string, defaults to None  
`chart_axes_highlights_x_label_max_width`| `float`, optional| Max width. Flourish type hint: number, defaults to None  
`chart_axes_highlights_x_font_size`| `float`, optional| Font size. Flourish type hint: number, defaults to None  
`chart_axes_highlights_x_font_weight`| `str`, optional| Font weight. Choices: regular, bold. Flourish type hint: string, defaults to None  
`chart_axes_highlights_x_label_color`| `str`, optional| Text. Flourish type hint: color, defaults to None  
`chart_axes_highlights_x_shadow_color`| `str`, optional| Shadow. Flourish type hint: color, defaults to None  
`chart_axes_highlights_x_shadow_enabled`| `bool`, optional| Shadow. Flourish type hint: boolean, defaults to None  
`chart_axes_highlights_y_enabled`| `bool`, optional| Show highlights on the y axis. Flourish type hint: boolean, defaults to None  
`chart_axes_highlights_y_lines`| `Union[list, str]`, optional| One per line, in format “My label :: 5000”. One per line, using the format : My label :: 2012 For dates, use the input format as specified in the datasheet. You can optionally specify a line color and a text color For visualizations using a grid of charts , you can apply the annotation only on a specific chart Use the format: `My label :: 2012 :: line_color / text_color :: facet_name`. For example: `My label :: 2012 :: #eb0000 / #0084bd :: Category 1`. If you want to add an annotation to just one specific chart but do not want to color the line/text, you can leave that part blank. For example: My label :: 2012 :: :: Category 1 Flourish type hint: text, defaults to None  
`chart_axes_highlights_y_line_color`| `str`, optional| Line color. Flourish type hint: color, defaults to None  
`chart_axes_highlights_y_line_width`| `float`, optional| line width. Flourish type hint: number, defaults to None  
`chart_axes_highlights_y_line_dash`| `float`, optional| Dash. Flourish type hint: number, defaults to None  
`chart_axes_highlights_y_areas`| `Union[list, str]`, optional| One per line, in format “My label :: 2000 >> 8000”. One per line, using the format : My label :: date >> date For dates, use the input format as specified in the datasheet. You can optionally specify a line color and a text color For visualizations using a grid of charts , you can apply the annotation only on a specific chart Use the format: My label :: 2012 :: area_color / text_color :: facet_name For example: `My label :: 2012 >> 2015 :: #eb0000 / #0084bd :: Category 1`. Flourish type hint: text, defaults to None  
`chart_axes_highlights_y_area_color`| `str`, optional| Area. Flourish type hint: color, defaults to None  
`chart_axes_highlights_y_area_opacity`| `float`, optional| Area opacity. Flourish type hint: number, defaults to None  
`chart_axes_highlights_y_area_texture`| `str`, optional| Area texture. Choices: none, pattern-diagonal, pattern-grid, pattern-dots. Flourish type hint: string, defaults to None  
`chart_axes_highlights_y_label_x_position`| `str`, optional| X position. Choices: left, middle, right. Horizontally position label on the left, the middle or the right end of the line. This setting will be ignored if there is not enough space for the selected position. Flourish type hint: string, defaults to None  
`chart_axes_highlights_y_label_y_position`| `str`, optional| Y position. Choices: above, middle, below. Vertically position the label above, below or in the middle of the line. This setting will be ignored if there is not enough space for the selected position. Flourish type hint: string, defaults to None  
`chart_axes_highlights_y_label_max_width`| `float`, optional| Max width. Flourish type hint: number, defaults to None  
`chart_axes_highlights_y_font_size`| `float`, optional| Font size. Flourish type hint: number, defaults to None  
`chart_axes_highlights_y_font_weight`| `str`, optional| Font weight. Choices: regular, bold. Flourish type hint: string, defaults to None  
`chart_axes_highlights_y_label_color`| `str`, optional| Text. Flourish type hint: color, defaults to None  
`chart_axes_highlights_y_shadow_color`| `str`, optional| Shadow. Flourish type hint: color, defaults to None  
`chart_axes_highlights_y_shadow_enabled`| `bool`, optional| Shadow. Flourish type hint: boolean, defaults to None  
`annotations_styles`| `bool`, optional| Show styling options. Flourish type hint: boolean, defaults to None  
`chart_annotations_defaults_text_weight`| `str`, optional| Weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`chart_annotations_defaults_text_size`| `float`, optional| Text size. Flourish type hint: number, defaults to None  
`chart_annotations_defaults_text_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`chart_annotations_defaults_label_width`| `float`, optional| Max width. Flourish type hint: number, defaults to None  
`chart_annotations_defaults_text_background_mode`| `str`, optional| Text background. Choices: none, outline, background. Flourish type hint: string, defaults to None  
`chart_annotations_defaults_text_bg`| `str`, optional| Outline. Flourish type hint: color, defaults to None  
`chart_annotations_defaults_label_bg`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`chart_annotations_defaults_text_alignment`| `str`, optional| Alignment. Choices: auto, start, center, end. Flourish type hint: string, defaults to None  
`chart_annotations_defaults_popup_position`| `str`, optional| Popup position. Choices: center, left, right, top, bottom. Flourish type hint: string, defaults to None  
`chart_annotations_defaults_line_marker`| `str`, optional| Marker. Choices: none, arrowhead_open, arrowhead. Flourish type hint: string, defaults to None  
`chart_annotations_defaults_stroke_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_annotations_defaults_stroke_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_annotations_defaults_connector_extend_line`| `str`, optional| Extend line. Choices: enabled, disabled. Flourish type hint: string, defaults to None  
`data_trans_duration`| `float`, optional| Animation duration. The duration of transitions in milliseconds, for example between two slides in a story. Flourish type hint: number, defaults to None  
`animate_on_load`| `bool`, optional| Animate on load. Flourish type hint: boolean, defaults to None  
`data_trans_bind_series`| `bool`, optional| Only animate series with same name. Determines how animations work when the data changes (e.g. between slides in a story ). When this is on, series (e.g. lines) will attempt to animate to become another line only if they have the same name (i.e. the same column header). Flourish type hint: boolean, defaults to None  
`data_trans_bind_data_points`| `bool`, optional| Only animate points with same label. Determines how animations work when the data changes (e.g. between slides in a story ). When this is on, data points (e.g. dots or bars) will attempt to animate to become other data points if they have the same label (e.g. date or category). Flourish type hint: boolean, defaults to None  
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
`chart_url_settings_enabled`| `bool`, optional| Update project from URL. Make it possible to change the visualizations settings/state from the URL hash, for example when embedding in an iframe or popup panel. Flourish type hint: boolean, defaults to None  
`chart_url_settings_whitelist`| `Union[list, str]`, optional| Allowed state properties. List each state property you want to make changeable with the URL hash See the template page for a full list of state properties. Add one property name per line. Use dot format for nested properties, e.g. `layout.background_color`. Flourish type hint: text, defaults to None  
  
Arguments| Description  
---|---  
`.`| Returns the Flourish object  
`dual_axis`| Axis type. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`secondary_series`| Number of combo lines. In line-bar mode , sets how many of your value columns are treated as lines. In line-line mode , sets how many lines use the right axis. The order counts from the start, so if you want column B as a line and A as a column, set the order in the column bindings to "B, A". Flourish type hint: number, defaults to `NULL`  
`stack_sort`| Stack sort mode. Choices: data, ascending, descending. Whether each stack is in the default order or sorted by value. Use ascending or descending with a stacked area chart to make a "bump" area chart. Flourish type hint: string, defaults to `NULL`  
`facet_layout`| Grid mode. Choices: single, facets. By default, Grid of charts creates a mini chart for each series. If Grid of charts is set in your column bindings, a mini chart will be created for each unique value in your specified column. Flourish type hint: string, defaults to `NULL`  
`height_mode`| Height mode. Choices: auto, fill_space, aspect. Auto: sets the height based on the chart type, data and width. Standard: uses the default Flourish responsive sizing. Aspect ratio: sets the aspect of each plot. This setting is ignored when embedded in a fixed-height context, such as a simple iframe embedFlourish type hint: string, defaults to `NULL`  
`facet_aspect`| Aspect (desktop). Aspect ratio of each plot in desktop mode, where 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to `NULL`  
`facet_aspect_mobile`| Aspect (mobile). Aspect of each plot in mobile mode, where 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to `NULL`  
`facet_aspect_breakpoint`| Breakpoint. The width at which mobile mode ends and desktop begins. Flourish type hint: number, defaults to `NULL`  
`sort_mode`| Sort mode. Choices: data, value, label. Flourish type hint: string, defaults to `NULL`  
`chart_facet_columns_fixed`| Number of columns. Choices: `FALSE`, `TRUE`. In Auto mode, the number of columns will change with screen size. Flourish type hint: boolean, defaults to `NULL`  
`chart_facet_min_width`| Min chart width. Determines how many columns of charts are displayed in the grid. Ignored if you specify a fixed number of columns. Flourish type hint: number, defaults to `NULL`  
`chart_facet_max_width`| Max chart width. Determines how many columns of charts are in the grid. Ignored if you specify a fixed number of columns. Flourish type hint: number, defaults to `NULL`  
`chart_facet_columns`| Fixed number of columns. Flourish type hint: number, defaults to `NULL`  
`chart_facet_gutter_w`| Horizontal margin. Flourish type hint: number, defaults to `NULL`  
`chart_facet_gutter_h`| Vertical margin. Flourish type hint: number, defaults to `NULL`  
`chart_facet_animation`| On data change. Choices: auto, name, reuse. If a chart in the grid is removed, that cell can either be animated out (with another cell moving to take its place) or reused for the new data in that cell. Auto decides for you based on the data. Flourish type hint: string, defaults to `NULL`  
`chart_facet_titles`| Show titles. Flourish type hint: boolean, defaults to `NULL`  
`chart_facet_title_align`| Alignment. Choices: auto, left, center, right. Flourish type hint: string, defaults to `NULL`  
`chart_facet_title_size`| Size. Relative to the width of the chart. Flourish type hint: number, defaults to `NULL`  
`chart_facet_title_unit`| Scale with chart. Choices: rem, facet. Flourish type hint: string, defaults to `NULL`  
`chart_facet_title_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_facet_title_padding_top`| Space above. Flourish type hint: number, defaults to `NULL`  
`chart_facet_title_padding_bottom`| Space below. Flourish type hint: number, defaults to `NULL`  
`chart_facet_title_bg`| Background. Choices: none, full, text. Flourish type hint: string, defaults to `NULL`  
`chart_facet_title_bg_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_facet_title_bg_padding`| Padding. Horizontal space between text and background. Flourish type hint: number, defaults to `NULL`  
`x_axis_matching`| Same across grid. Ensure the X scale is the same across the grid. Flourish type hint: boolean, defaults to `NULL`  
`x_axis_last_row_only`| Last row only. Only show the X axis on the last row, where possible. Ignored if the X axis is not positioned at the bottom. Flourish type hint: boolean, defaults to `NULL`  
`y_axis_matching`| Same across grid. Ensure the Y scale is the same across the grid. Flourish type hint: boolean, defaults to `NULL`  
`y_axis_first_col_only`| First column only. Only show the Y axis on the first column of the grid, where possible. Flourish type hint: boolean, defaults to `NULL`  
`y2_axis_matching`| Same across grid. Ensure the secondary Y scale is the same across the grid. Flourish type hint: boolean, defaults to `NULL`  
`y2_axis_last_col_only`| Last column only. Only show the secondary Y axis on the last column of the grid, where possible. Flourish type hint: boolean, defaults to `NULL`  
`series_filter_mode`| Series filter. Choices: none, single, multi. Filter control for series/columns. The user can also filter by clicking on the legend, except in single select mode. Use the animation settings panel to determine whether series animate when changing the filter. Flourish type hint: string, defaults to `NULL`  
`series_control_multi_text`| Placeholder text. Flourish type hint: string, defaults to `NULL`  
`series_control_multi_none_text`| No more results text. Flourish type hint: string, defaults to `NULL`  
`series_control_select_text`| Select text. Flourish type hint: string, defaults to `NULL`  
`max_series`| Max series to show. Limits the number of series/columns that will be visualized at once. Flourish type hint: number, defaults to `NULL`  
`series_control_background`| Background. Flourish type hint: color, defaults to `NULL`  
`series_control_text`| Text. Flourish type hint: color, defaults to `NULL`  
`series_control_border`| Border. Flourish type hint: color, defaults to `NULL`  
`series_control_pill_background`| Background. Flourish type hint: color, defaults to `NULL`  
`series_control_pill_text`| Text. Flourish type hint: color, defaults to `NULL`  
`series_control_pill_radius`| Border radius. Flourish type hint: number, defaults to `NULL`  
`series_control_single_all`| Include "All". Flourish type hint: boolean, defaults to `NULL`  
`series_control_single_all_text`| Name for "All". Flourish type hint: string, defaults to `NULL`  
`filter_rows_with_no_data`| Filter rows that have no data. This setting filters rows that have no data, this is useful in combination with filters and datasets that have a lot of empty cells. Flourish type hint: boolean, defaults to `NULL`  
`chart_series_filter_controls_control_type`| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to `NULL`  
`chart_series_filter_controls_control_styles`| Adv. Flourish type hint: boolean, defaults to `NULL`  
`chart_series_filter_controls_control_title`| Control title. Flourish type hint: string, defaults to `NULL`  
`chart_series_filter_controls_button_group`| Grouped. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_series_filter_controls_button_group_width_mode`| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_series_filter_controls_button_group_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_series_filter_controls_dropdown_width_mode`| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_series_filter_controls_dropdown_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_series_filter_controls_slider_width`| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to `NULL`  
`chart_series_filter_controls_slider_max_label_width`| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to `NULL`  
`chart_series_filter_controls_slider_step_time`| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to `NULL`  
`chart_series_filter_controls_slider_loop`| Loop. Flourish type hint: boolean, defaults to `NULL`  
`chart_series_filter_controls_slider_restart_pause`| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to `NULL`  
`chart_series_filter_controls_sort`| Sorting. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`row_filter_control_all`| Include "All". Flourish type hint: boolean, defaults to `NULL`  
`row_filter_control_all_text`| Name for "All". Flourish type hint: string, defaults to `NULL`  
`chart_row_filter_controls_control_type`| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to `NULL`  
`chart_row_filter_controls_control_styles`| Adv. Flourish type hint: boolean, defaults to `NULL`  
`chart_row_filter_controls_control_title`| Control title. Flourish type hint: string, defaults to `NULL`  
`chart_row_filter_controls_button_group`| Grouped. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_row_filter_controls_button_group_width_mode`| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_row_filter_controls_button_group_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_row_filter_controls_dropdown_width_mode`| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_row_filter_controls_dropdown_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_row_filter_controls_slider_width`| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to `NULL`  
`chart_row_filter_controls_slider_max_label_width`| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to `NULL`  
`chart_row_filter_controls_slider_step_time`| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to `NULL`  
`chart_row_filter_controls_slider_loop`| Loop. Flourish type hint: boolean, defaults to `NULL`  
`chart_row_filter_controls_slider_restart_pause`| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to `NULL`  
`chart_row_filter_controls_sort`| Sorting. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`log_control_y_visible`| Show log control for Y axis. Adds a tabbed control to allow users to switch between log and linear Y scales. Flourish type hint: boolean, defaults to `NULL`  
`chart_log_control_y_filter_controls_control_type`| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to `NULL`  
`chart_log_control_y_filter_controls_control_styles`| Adv. Flourish type hint: boolean, defaults to `NULL`  
`chart_log_control_y_filter_controls_control_title`| Control title. Flourish type hint: string, defaults to `NULL`  
`chart_log_control_y_filter_controls_button_group`| Grouped. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_log_control_y_filter_controls_button_group_width_mode`| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_log_control_y_filter_controls_button_group_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_log_control_y_filter_controls_dropdown_width_mode`| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_log_control_y_filter_controls_dropdown_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_log_control_y_filter_controls_slider_width`| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to `NULL`  
`chart_log_control_y_filter_controls_slider_max_label_width`| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to `NULL`  
`chart_log_control_y_filter_controls_slider_step_time`| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to `NULL`  
`chart_log_control_y_filter_controls_slider_loop`| Loop. Flourish type hint: boolean, defaults to `NULL`  
`chart_log_control_y_filter_controls_slider_restart_pause`| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to `NULL`  
`chart_log_control_y_filter_controls_sort`| Sorting. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`log_control_y_text_linear`| Linear text. Flourish type hint: string, defaults to `NULL`  
`log_control_y_text_log`| Log text. Flourish type hint: string, defaults to `NULL`  
`chart_controls_style_font_size`| Text size. Flourish type hint: number, defaults to `NULL`  
`chart_controls_style_font_weight`| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_controls_style_height`| Height. Flourish type hint: number, defaults to `NULL`  
`chart_dropdown_control_style_background`| Background. Flourish type hint: color, defaults to `NULL`  
`chart_dropdown_control_style_font_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`chart_dropdown_control_style_border_styles_advanced`| Dropdown border styles. Flourish type hint: boolean, defaults to `NULL`  
`chart_dropdown_control_style_border_style`| Border style. Choices: all, bottom. Show border on all sides, or only at the bottom. Flourish type hint: string, defaults to `NULL`  
`chart_dropdown_control_style_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`chart_dropdown_control_style_border_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_dropdown_control_style_border_transparency`| Transparency. Flourish type hint: number, defaults to `NULL`  
`chart_dropdown_control_style_border_radius`| Radius. Flourish type hint: number, defaults to `NULL`  
`chart_button_control_style_background`| Background. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_background_selected`| Selected. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_background_hover`| Mouse over. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_font_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_font_color_selected`| Selected. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_font_color_hover`| Mouse over. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_button_styles_advanced`| Button border styles. Flourish type hint: boolean, defaults to `NULL`  
`chart_button_control_style_border_width`| Border width. Flourish type hint: number, defaults to `NULL`  
`chart_button_control_style_border_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_button_control_style_border_transparency`| Transparency. Flourish type hint: number, defaults to `NULL`  
`chart_button_control_style_border_radius`| Radius. Flourish type hint: number, defaults to `NULL`  
`chart_filter_controls_container_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_filter_controls_container_controls_spacing`| Spacing. The space between controls, like dropdowns and adjacent button sets, in em units. Flourish type hint: number, defaults to `NULL`  
`controls_position`| Control position. Choices: log_series_row, series_log_row, log_row_series, series_row_log, row_log_series, row_series_log. If you have two or more controls turned on for your chart, you can change the order the controls appear. Flourish type hint: string, defaults to `NULL`  
`color_mode`| Color mode. Choices: column, row. By column will set the colors by series. Each column listed in the value column binding in the datasheet will have a different color. By row will instead set the color depending on the datas label/time column binding. Flourish type hint: string, defaults to `NULL`  
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
`line_width`| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`line_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`line_stroke`| Outline. Add a stroke around your lines to enhance visibility when overlapping. Flourish type hint: boolean, defaults to `NULL`  
`line_curve`| Line curve. Choices: curve_linear, curve_monotone_x, curve_natural, curve_step, curve_step_before, curve_step_after. Flourish type hint: string, defaults to `NULL`  
`line_dash_items`| Dashed lines. Specify the series that you would like to display with a dashed line. Multiple dashed lines can be set using multiple lines. For example: Party 1 Party 2 Party 3. Flourish type hint: text, defaults to `NULL`  
`line_dash_width`| Dash width. Flourish type hint: number, defaults to `NULL`  
`line_dash_space_width`| Space width. Flourish type hint: number, defaults to `NULL`  
`line_interpolate`| Missing data points. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`shade_between_lines`| Shade areas between lines. Shade the gap between any two lines on your chart. Flourish type hint: boolean, defaults to `NULL`  
`shade_between_lines_config`| Which lines to shade between. Specify each area as a pair of line names separated by `::`. For example: Series A :: Series B Series C :: Series D You can optionally add a specific color and opacity for each area, e.g. `Series A :: Series B :: red :: 0.1`. Flourish type hint: text, defaults to `NULL`  
`shade_between_lines_color`| Color. Flourish type hint: color, defaults to `NULL`  
`shade_between_lines_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`area_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`dot_mode`| Choices: auto, on, off. " Auto will automatically show dots on lines if fewer than 250 data points. Note: avoid showing dots for large datasets since it can lead to poor performance issues and poor-looking charts". Flourish type hint: string, defaults to `NULL`  
`dot_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`dot_radius`| Radius. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`dot_radius_last`| Final dot scale (%). Making the last point on a line larger can help emphasise the final value. This will usually be the dot furthest right on the axis. Flourish type hint: number, defaults to `NULL`  
`dot_hollow`| Hollow. Flourish type hint: boolean, defaults to `NULL`  
`bar_height`| Bar height. The approximate height of the bar, the exact height depends on padding and label style. Specified in rems Ignored if the chart is embedded at a fixed height. Flourish type hint: number, defaults to `NULL`  
`column_opacity`| Bar opacity. Flourish type hint: number, defaults to `NULL`  
`uniform_column_width`| Uniform column width. Flourish type hint: boolean, defaults to `NULL`  
`uniform_bar_height`| Uniform bar height. Flourish type hint: boolean, defaults to `NULL`  
`column_padding_inner`| Spacing (main). Space between bar stacks or groups, as a % of the width of a whole bar stack or group. Flourish type hint: number, defaults to `NULL`  
`column_padding_in_group`| Spacing (in group). Space between bars in groups, as a % of the width of a single bar in the group. Ignored if only a single series is selected. Flourish type hint: number, defaults to `NULL`  
`column_padding_stack`| Spacing (in stack). Space each bar in the stack, in tenths of a rem Flourish type hint: number, defaults to `NULL`  
`column_stroke`| Outline. Add a stroke around your columns or bars (same color as text). Flourish type hint: boolean, defaults to `NULL`  
`column_stroke_opacity`| Outline opacity. Flourish type hint: number, defaults to `NULL`  
`column_stroke_color`| Outline color. Flourish type hint: color, defaults to `NULL`  
`donut_inner_radius`| Doughnut hole (%). Flourish type hint: number, defaults to `NULL`  
`donut_corner_radius`| Corner curve (pixels). Flourish type hint: number, defaults to `NULL`  
`donut_pad_angle`| Segment padding (degrees). Flourish type hint: number, defaults to `NULL`  
`donut_auto_scale`| Scale pies based on data. Scale each pie chart in the grid so that the area of each pie/donut reflect its value. Flourish type hint: boolean, defaults to `NULL`  
`bar_labels_above`| Label style. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`bar_labels_color`| Color. Flourish type hint: color, defaults to `NULL`  
`bar_labels_font_size`| Size. When in Standard or Aspect ratio height mode, the font size of the labels will be limited to the space available. In remsFlourish type hint: number, defaults to `NULL`  
`bar_labels_weight`| Choices: 600, 400. Flourish type hint: string, defaults to `NULL`  
`line_end_labels`| Show labels on lines. Show series labels on the end of lines if theres enough space. Flourish type hint: boolean, defaults to `NULL`  
`chart_line_labels_max_width`| Max label width. The maximum allowed label width. Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_overlap_mode`| Overlaps. Choices: spread, hide, none. What to do with overlaps. Flourish type hint: string, defaults to `NULL`  
`chart_line_labels_spreading_margin`| Space between labels. The space left between labels when spreading them out to avoid overlaps. Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_data_point_margin`| Distance. The space between the data point and the label in rems (a multiple of base font size). Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_show_only_labels`| Show only certain labels. Manually specify which labels youd like to display (one entry per line that should match headers from the Values columns). Flourish type hint: text, defaults to `NULL`  
`chart_line_labels_text_color`| Color. If cleared, uses the main text color from the Layout settings panel. Flourish type hint: color, defaults to `NULL`  
`chart_line_labels_text_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_text_bg_color`| Outline. If cleared, uses the main background color from the Layout settings panel. Flourish type hint: color, defaults to `NULL`  
`chart_line_labels_text_bg_size`| Outline width. As a % of the font size. Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_text_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_text_max_lines`| Max lines. The max number of lines for each label. Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_text_weight`| Weight. Choices: 400, 700. Flourish type hint: string, defaults to `NULL`  
`chart_line_labels_lines`| Connector lines. Choices: auto, on, off. Flourish type hint: string, defaults to `NULL`  
`chart_line_labels_line_style`| Line style. Choices: straight, step. Flourish type hint: string, defaults to `NULL`  
`chart_line_labels_line_color`| Color. If cleared, uses the main text color from the Layout settings panel. Flourish type hint: color, defaults to `NULL`  
`chart_line_labels_line_width`| Width. In rems (a multiple of base font size). Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_line_range`| Length. The width of the space given over to lines; in rems, a multiple of base font size. Flourish type hint: number, defaults to `NULL`  
`chart_line_labels_line_padding`| Padding. The padding to the left and right of the line; in rems, a multiple of base font size. Flourish type hint: number, defaults to `NULL`  
`labels`| Show labels on data points. Flourish type hint: boolean, defaults to `NULL`  
`labels_hide_overlaps`| Hide overlapping labels. Flourish type hint: boolean, defaults to `NULL`  
`labels_dot_center`| Position labels on center of dot. Flourish type hint: boolean, defaults to `NULL`  
`labels_column_align`| Bar label alignment. Choices: bottom, middle, top, above. The final above option puts the labels above the bars in standard column charts. In stacked charts, where the space above the stack is reserved for stack total the labels falls back to top alignment. Flourish type hint: string, defaults to `NULL`  
`labels_column_padding`| Padding. Space above or below, as a proportion of the font size in rems Flourish type hint: number, defaults to `NULL`  
`labels_bar_align`| Label alignment. Choices: left, center, right, out. In stacked bar charts the final out (outside of bar) option falls back to right alignment, since the space after the stack is reserved for stack total labels (see below). Flourish type hint: string, defaults to `NULL`  
`labels_bar_autohide`| Hide if too big. Turn off to force labels to show, even if they will overflow the bars. Ignored when labels are not inside the bars. Flourish type hint: boolean, defaults to `NULL`  
`labels_color_mode`| Text color. Choices: auto, data, contrast, fixed. Contrast mode is black or white depending on the color of the data point (or the background color for labels positioned over the background). Flourish type hint: string, defaults to `NULL`  
`labels_fixed_color`| Color. Flourish type hint: color, defaults to `NULL`  
`labels_font_weight`| Weight. Choices: 600, 400. Flourish type hint: string, defaults to `NULL`  
`labels_font_size_mode`| Size. Choices: auto, fixed. Flourish type hint: string, defaults to `NULL`  
`labels_font_size`| Size. Flourish type hint: number, defaults to `NULL`  
`labels_bg_mode`| Outline. Choices: on, off. A text outline/background can make the text more readable by increasing contrast. Flourish type hint: string, defaults to `NULL`  
`labels_bg_size`| Size. Size of the background, as % of text size. Flourish type hint: number, defaults to `NULL`  
`labels_content`| Label content. Choices: auto, value, label, both. Flourish type hint: string, defaults to `NULL`  
`stack_labels`| Show labels for stack totals. Flourish type hint: boolean, defaults to `NULL`  
`stack_labels_color`| Color. Flourish type hint: color, defaults to `NULL`  
`stack_labels_font_size`| Size. Flourish type hint: number, defaults to `NULL`  
`stack_labels_weight`| Weight. Choices: 600, 400. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_axis_position`| Position. Choices: bottom, float-below, float-above, top, off. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_y_axis_position`| Y value. Vertical position of the x axis on the y scale. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_numeric_scale_type`| Type. Choices: linear, log. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_linear_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_linear_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_log_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_log_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_datetime_min`| Min (date). Use the input date format as specified in the datasheet. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_datetime_max`| Max (date). Use the input date format as specified in the datasheet. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_flip`| Flip axis. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_show_scale_settings`| Configure default min/max. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_nice`| Round min/max. Choices: `TRUE`, `FALSE`. When enabled, scales automatically extend to "nice" rounded start/end values, such as hundreds or whole years. Overridden by any explicitly specified scale min and max. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_zero_axis`| Include zero. Choices: auto, on, off. Whether to extend the axis to include zero if the data values are all positive or all negative. Overridden by any explicitly specified scale min and max. Flourish type hint: string, defaults to `NULL`  
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
`chart_x_axis_tick_label_space_mode`| Space mode. Choices: auto, max, fixed. How the vertical space available for tick labels is determined. "Auto" means that the space is automatically determined. "Max" lets you specify the maximum vertical space tick labels may occupy. "Fixed" lets you specify a fixed amount of vertical space for tick labels. Tick labels will be truncated to fit within the allocated horizontal space. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_tick_label_space`| Space. The space allocated for tick labels (relative to the root font size). Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_tick_mode`| Mode. Choices: auto, number, custom. Determines how the tick values are chosen. "Auto" mode chooses the ticks automatically. "Number" mode lets you specify how many ticks are drawn. "Custom" mode lets you specify which ticks are drawn. If the axis is categorical, "Number" mode is ignored. Flourish type hint: string, defaults to `NULL`  
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
`chart_x_axis_gridline_category_dividers`| Put lines between categories. On a categorical axis this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_gridline_category_dividers_extend`| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_axis_visible`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_numeric_scale_type`| Type. Choices: linear, log. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_linear_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_linear_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_log_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_log_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_datetime_min`| Min (date). Use the same format as displayed in the axis. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_datetime_max`| Max (date). Use the same format as displayed in the axis. Flourish type hint: string, defaults to `NULL`  
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
`chart_y_axis_tick_label_space_mode`| Space mode. Choices: auto, max, fixed. Sets how the horizontal space available for tick labels is determined. "Auto" means that the space is automatically determined. "Max" lets you specify the maximum horizontal space tick labels may occupy. "Fixed" lets you specify a fixed amount of horizontal space for tick labels. Tick labels will be truncated to fit within the allocated horizontal space. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_tick_label_space`| Space. The space allocated for tick labels (relative to the root font size). Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_tick_mode`| Mode. Choices: auto, number, custom. Determines how the tick values are chosen. "Auto" mode chooses the ticks automatically. "Number" mode lets you specify how many ticks are drawn. "Custom" mode lets you specify which ticks are drawn. If the axis is categorical, "Number" mode is ignored. Flourish type hint: string, defaults to `NULL`  
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
`chart_y_axis_gridline_category_dividers`| Put lines between categories. On a categorical axis this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Ignored for date and numeric axes. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_gridline_category_dividers_extend`| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_axis_visible`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_numeric_scale_type`| Type. Choices: linear, log. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_linear_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_linear_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_log_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_log_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_datetime_min`| Min (date). Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_datetime_max`| Max (date). Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_flip`| Flip axis. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_show_scale_settings`| Configure default min/max. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_nice`| Round min/max. Choices: `TRUE`, `FALSE`. When enabled, scales automatically extend to "nice" rounded start/end values, such as hundreds or whole years. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_zero_axis`| Include zero. Choices: auto, on, off. Whether to extend the axis to include zero if the data values are all positive or all negative. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_title_mode`| Type. Choices: auto, custom. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_title`| Text. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_title_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_title_position`| Position. Choices: side, end. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_title_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_title_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_secondary_y_axis_title_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_title_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_position`| Position. Choices: default, above, below. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_size`| Size. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_secondary_y_axis_tick_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_angle`| Angle. Choices: 0, 30, 45, 60, 90. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_max_lines`| Max lines. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_space_mode`| Space mode. Choices: auto, max, fixed. Sets how the horizontal space available for tick labels is determined. "Auto" means that the space is automatically determined. "Max" lets you specify the maximum horizontal space tick labels may occupy. "Fixed" lets you specify a fixed amount of horizontal space for tick labels. Tick labels will be truncated to fit within the allocated horizontal space. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_tick_label_space`| Space. The space allocated for tick labels (relative to the root font size). Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_mode`| Mode. Choices: auto, number, custom. Determines how the tick values are chosen. "Auto" mode chooses the ticks automatically. "Number" mode lets you specify how many ticks are drawn. "Custom" mode lets you specify which ticks are drawn. If the axis is categorical, "Number" mode is ignored. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_tick_number`| Number. Approximate number of ticks or gridlines. The actual number will depend on the range of values, chart size, etc. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_custom`| One tick label per line. Specify the ticks to show, one per line. For dates, use the input format as specified in the datasheet. You can also use `{{FIRST}}` and `{{LAST}}` to add ticks at the minimum and maximum of the axis. For example: `{{FIRST}}` 25000 50000 75000 `{{LAST}}`. Flourish type hint: text, defaults to `NULL`  
`chart_secondary_y_axis_line_and_tick_color`| Line color. Flourish type hint: color, defaults to `NULL`  
`chart_secondary_y_axis_line_and_tick_width`| Line width. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_length`| Tick length. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_tick_side`| Side. Choices: out, in. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_line_visible`| Axis line. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_edge_padding`| Edge padding (%). Space between start/end of axis line and first/last category tick as a percentage of the spacing between ticks. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_gridlines_visible`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_gridlines_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_gridline_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_secondary_y_axis_gridline_style`| Style. Choices: solid, dash, dot, dot_dash. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_y_axis_gridline_width`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_y_axis_gridline_category_dividers`| Put lines between categories. On a categorical axis this option disables the gridline on each tick and instead adds rules between each category to give a table-like design. Ignored for date and numeric axes. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_y_axis_gridline_category_dividers_extend`| Extend. Extends the dividers into the axis margins. Flourish type hint: boolean, defaults to `NULL`  
`chart_background_background_color_enabled`| Color. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_background_background_image_enabled`| Image. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_background_background_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_background_background_image_src`| Image URL. Flourish type hint: url, defaults to `NULL`  
`chart_background_background_image_size`| Size. Choices: stretch, slice, meet. Flourish type hint: string, defaults to `NULL`  
`chart_background_background_image_position`| Position. Choices: x_min_y_min, x_mid_y_min, x_max_y_min, x_max_y_mid, x_mid_y_mid, x_min_y_max, x_mid_y_max, x_max_y_max. Flourish type hint: string, defaults to `NULL`  
`number_format_labels_prefix`| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to `NULL`  
`number_format_labels_suffix`| Suffix. Text to place after a number. Flourish type hint: string, defaults to `NULL`  
`number_format_labels_n_dec`| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to `NULL`  
`number_format_labels_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`number_format_labels_negative_sign`| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to `NULL`  
`number_format_labels_strip_zeros`| Remove trailing zeros. Flourish type hint: boolean, defaults to `NULL`  
`number_format_labels_strip_separator`| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to `NULL`  
`number_format_labels_transform_labels`| Multiply/divide values. Flourish type hint: boolean, defaults to `NULL`  
`number_format_labels_transform`| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to `NULL`  
`number_format_labels_multiply_divide_constant`| Flourish type hint: number, defaults to `NULL`  
`number_format_labels_exponentiate_constant`| Flourish type hint: number, defaults to `NULL`  
`chart_number_date_format_prefix`| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to `NULL`  
`chart_number_date_format_suffix`| Suffix. Text to place after a number. Flourish type hint: string, defaults to `NULL`  
`chart_number_date_format_n_dec`| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to `NULL`  
`chart_number_date_format_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_number_date_format_negative_sign`| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to `NULL`  
`chart_number_date_format_strip_zeros`| Remove trailing zeros. Flourish type hint: boolean, defaults to `NULL`  
`chart_number_date_format_strip_separator`| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to `NULL`  
`chart_number_date_format_transform_labels`| Multiply/divide values. Flourish type hint: boolean, defaults to `NULL`  
`chart_number_date_format_transform`| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to `NULL`  
`chart_number_date_format_multiply_divide_constant`| Flourish type hint: number, defaults to `NULL`  
`chart_number_date_format_exponentiate_constant`| Flourish type hint: number, defaults to `NULL`  
`number_format_prop`| Show % values. Toggles between showing the raw values from the datasheet and the computed percent values for the row in popups/panels. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_number_date_format_prefix`| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_number_date_format_suffix`| Suffix. Text to place after a number. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_number_date_format_n_dec`| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to `NULL`  
`chart_secondary_number_date_format_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_number_date_format_negative_sign`| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_number_date_format_strip_zeros`| Remove trailing zeros. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_number_date_format_strip_separator`| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_number_date_format_transform_labels`| Multiply/divide values. Flourish type hint: boolean, defaults to `NULL`  
`chart_secondary_number_date_format_transform`| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to `NULL`  
`chart_secondary_number_date_format_multiply_divide_constant`| Flourish type hint: number, defaults to `NULL`  
`chart_secondary_number_date_format_exponentiate_constant`| Flourish type hint: number, defaults to `NULL`  
`legend_mode`| Legend mode. Choices: auto, on, off. Auto mode hides the legend in certain situations, such as when each color is already explained by the chart titles in a grid of charts A legend will not show with a single entry. Flourish type hint: string, defaults to `NULL`  
`legend_filter_mode`| Click legend to filter data. Choices: none, filter-in, filter-out. Single select : When clicked only shows the series selected Multi select : When clicked, hides series selected. Multiple series can be hidden Filterable legends are ignored in certain situations, such as when shading by series and using a series filter Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_orientation`| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_title_weight`| Title weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_text_weight`| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_text_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_legend_container_text_size`| Size. Flourish type hint: number, defaults to `NULL`  
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
`legend_position`| Legend position. Choices: above, below. Flourish type hint: string, defaults to `NULL`  
`text_legend`| Add data colors to header text. Choices: auto, custom, off. When selected, this will change the color of any text in your header which matches the name of a series in your data. This feature can be used instead of a legend when there are a small number of series, or it can be used to highlight a particular series. Note using optional HTML in the header is disabled if using this feature. Flourish type hint: string, defaults to `NULL`  
`text_legend_title`| Title. Flourish type hint: boolean, defaults to `NULL`  
`text_legend_subtitle`| Subtitle. Flourish type hint: boolean, defaults to `NULL`  
`text_legend_bold`| Bold. If checked, always use bold for colored items. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_mode`| Choices: none, popup, panel, both. Flourish type hint: string, defaults to `NULL`  
`chart_popup_popup_is_custom`| Popup content. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_show_popup_styles`| Show popup styles. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_popup_custom_header`| Popup custom header. Use `{{VALUE}}` to include the numerical value of the current data point, or `{{SERIES}}` to display its series name. For any other selected columns use `{{column_name}}`. Advanced users can include HTML to apply layouts, formatting, images, etc. You can also hide content based on a column name being empty using `{{#if column_name}} Text to display when column_name is not empty {{/if}}`. For example, `{{Country}}` `{{#if Capital}}(Capital: {{Capital}}){{/if}}` Flourish type hint: html, defaults to `NULL`  
`chart_popup_popup_custom_main`| Popup custom main content. Use `{{VALUE}}` to include the numerical value of the current data point, or `{{SERIES}}` to display its series name. For any other selected columns use `{{column_name}}`. Advanced users can include HTML to apply layouts, formatting, images, etc. You can also hide content based on a column name being empty using `{{#if column_name}} Text to display when column_name is not empty {{/if}}`. For example, `{{Country}}` `{{#if Capital}}(Capital: {{Capital}}){{/if}}` Flourish type hint: html, defaults to `NULL`  
`chart_popup_popup_custom_accessible`| Popup custom accessible content. A text alternative to visual custom popup content that will be read out by screenreaders. This content is added as an aria-label attribute to data point elements. You can still use `{{column_name}}` to add values from your data, but do not use HTML. For example: `{{Name}}, Population: {{Population}}, GDP: {{GDP}}`. If left empty, accessible content will fallback to the default popup content. Flourish type hint: text, defaults to `NULL`  
`chart_popup_popup_width`| Max width. In rems, multiples of base font size. Leave blank to let the width adjust based on the contents. Flourish type hint: number, defaults to `NULL`  
`chart_popup_popup_font_size`| Text size. Flourish type hint: number, defaults to `NULL`  
`chart_popup_popup_text_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`chart_popup_popup_align`| Align. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_popup_popup_background`| Fill color. Flourish type hint: color, defaults to `NULL`  
`chart_popup_popup_background_opacity`| Fill opacity. Flourish type hint: number, defaults to `NULL`  
`chart_popup_popup_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`chart_popup_popup_radius`| Radius. Corner radius of popup. Flourish type hint: number, defaults to `NULL`  
`chart_popup_popup_header_type`| Header style. Choices: block, inline. Flourish type hint: string, defaults to `NULL`  
`chart_popup_popup_header_background`| Background. Flourish type hint: color, defaults to `NULL`  
`chart_popup_popup_header_text_color`| Text. Flourish type hint: color, defaults to `NULL`  
`chart_popup_popup_list_type`| List type. Choices: table, ul. Flourish type hint: string, defaults to `NULL`  
`chart_popup_popup_list_label_weight`| Label weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`chart_popup_popup_list_separator`| List separator. Choices: :, , , `<br />`. Flourish type hint: string, defaults to `NULL`  
`chart_popup_popup_shadow`| Shadow. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_popup_pointer`| Pointer. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_panel_position`| Choices: overlay, left, right, top, bottom. Flourish type hint: string, defaults to `NULL`  
`chart_popup_panel_open_duration`| Open duration. Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_side_fixed`| Always show. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_panel_side_default_content`| Placeholder content. Flourish type hint: text, defaults to `NULL`  
`chart_popup_panel_is_custom`| Panel content. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_show_panel_styles`| Show panel styles. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_panel_custom_header`| Panel custom header. Use `{{VALUE}}` to include the numerical value of the current data point, or `{{SERIES}}` to display its series name. For any other selected columns use `{{column_name}}`. Advanced users can include HTML to apply layouts, formatting, images, etc. You can also hide content based on a column name being empty using `{{#if column_name}} Text to display when column_name is not empty {{/if}}`. For example, `{{Country}}` `{{#if Capital}}(Capital: {{Capital}}){{/if}}` Flourish type hint: html, defaults to `NULL`  
`chart_popup_panel_custom_main`| Panel custom main content. Use `{{VALUE}}` to include the numerical value of the current data point, or `{{SERIES}}` to display its series name. For any other selected columns use `{{column_name}}`. Advanced users can include HTML to apply layouts, formatting, images, etc. You can also hide content based on a column name being empty using `{{#if column_name}} Text to display when column_name is not empty {{/if}}`. For example, `{{Country}}` `{{#if Capital}}(Capital: {{Capital}}){{/if}}` Flourish type hint: html, defaults to `NULL`  
`chart_popup_panel_width_overlay`| Width (%). Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_height_overlay`| Height (%). Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_width_side`| Width (%). Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_height_side`| Height (%). Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_max_width`| Max width (px). Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_max_height`| Max height (px). Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_vertical_position`| Vertical position. Choices: click, center. Choosing Click position is especially useful when your visualization is really tall, this will make sure the panel content is always on top of the element youve clicked on. Flourish type hint: string, defaults to `NULL`  
`chart_popup_panel_text_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`chart_popup_panel_font_size`| Text size. Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_align`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_popup_panel_background`| Fill color. Flourish type hint: color, defaults to `NULL`  
`chart_popup_panel_background_opacity`| Fill opacity. Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_radius`| Radius. Corner radius of panel. Flourish type hint: number, defaults to `NULL`  
`chart_popup_panel_list_type`| List type. Choices: table, ul. Flourish type hint: string, defaults to `NULL`  
`chart_popup_panel_list_label_weight`| Label weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`chart_popup_panel_list_separator`| List separator. Choices: :, , , `<br />`. Flourish type hint: string, defaults to `NULL`  
`chart_popup_panel_shadow`| Shadow. Flourish type hint: boolean, defaults to `NULL`  
`popup_color_headers`| Color headers to match data. Flourish type hint: boolean, defaults to `NULL`  
`show_series_text`| Set series info in popups. Allows you to add information about each series/column (e.g. each line) to the popups. Note: This is incompatible with custom popup content. Flourish type hint: boolean, defaults to `NULL`  
`popup_series_text`| Popup content for series. Adds content to the popup about the series. Separate column name and text with a double colon. For example: Series 1 :: Comment about Series 1 Series 2 :: Comment about series 2. Flourish type hint: text, defaults to `NULL`  
`chart_axes_highlights_placement`| Placement of axis highlights. Choices: above, below. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_x_enabled`| Show highlights on the x axis. Flourish type hint: boolean, defaults to `NULL`  
`chart_axes_highlights_x_lines`| One per line, in format “My label :: 2012”. One per line, using the format : My label :: 2012 For dates, use the input format as specified in the datasheet. You can optionally specify a line color and a text color For visualizations using a grid of charts , you can apply the annotation only on a specific chart. Use the format: `My label :: 2012 :: line_color / text_color :: facet_name`. For example, `My label :: 2012 :: #eb0000 / #0084bd :: Category 1`. If you want to add an annotation to just one specific chart but do not want to color the line/text, you can leave that part blank. For example: My label :: 2012 :: :: Category 1 Flourish type hint: text, defaults to `NULL`  
`chart_axes_highlights_x_line_color`| Line color. Flourish type hint: color, defaults to `NULL`  
`chart_axes_highlights_x_line_width`| Line width. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_x_line_dash`| Dash. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_x_areas`| One per line, in format “My label :: 2013 >> 2015”. One per line, using the format : My label :: date >> date For dates, use the input format as specified in the datasheet. You can optionally specify a line color and a text color For visualizations using a grid of charts , you can apply the annotation only on a specific chart Use the format: My label :: 2012 :: area_color / text_color :: facet_name For example, `My label :: 2012 >> 2015 :: #eb0000 / #0084bd :: Category 1`. Flourish type hint: text, defaults to `NULL`  
`chart_axes_highlights_x_area_color`| Area. Flourish type hint: color, defaults to `NULL`  
`chart_axes_highlights_x_area_opacity`| Area opacity. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_x_area_texture`| Area texture. Choices: none, pattern-diagonal, pattern-grid, pattern-dots. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_x_label_vertical`| Vertical. Flourish type hint: boolean, defaults to `NULL`  
`chart_axes_highlights_x_label_y_position`| Y position. Choices: bottom, middle, top. Vertically position the label at the top, bottom or in the middle of the line. This setting will be ignored if there is not enough space for the selected position. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_x_label_x_position`| X position. Choices: left, middle, right. Horizontally position the label on the left, the right or in the middle of the line. This setting will be ignored if there is not enough space for the selected position. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_x_label_max_width`| Max width. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_x_font_size`| Font size. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_x_font_weight`| Font weight. Choices: regular, bold. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_x_label_color`| Text. Flourish type hint: color, defaults to `NULL`  
`chart_axes_highlights_x_shadow_color`| Shadow. Flourish type hint: color, defaults to `NULL`  
`chart_axes_highlights_x_shadow_enabled`| Shadow. Flourish type hint: boolean, defaults to `NULL`  
`chart_axes_highlights_y_enabled`| Show highlights on the y axis. Flourish type hint: boolean, defaults to `NULL`  
`chart_axes_highlights_y_lines`| One per line, in format “My label :: 5000”. One per line, using the format : My label :: 2012 For dates, use the input format as specified in the datasheet. You can optionally specify a line color and a text color For visualizations using a grid of charts , you can apply the annotation only on a specific chart Use the format: `My label :: 2012 :: line_color / text_color :: facet_name`. For example: `My label :: 2012 :: #eb0000 / #0084bd :: Category 1`. If you want to add an annotation to just one specific chart but do not want to color the line/text, you can leave that part blank. For example: My label :: 2012 :: :: Category 1 Flourish type hint: text, defaults to `NULL`  
`chart_axes_highlights_y_line_color`| Line color. Flourish type hint: color, defaults to `NULL`  
`chart_axes_highlights_y_line_width`| line width. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_y_line_dash`| Dash. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_y_areas`| One per line, in format “My label :: 2000 >> 8000”. One per line, using the format : My label :: date >> date For dates, use the input format as specified in the datasheet. You can optionally specify a line color and a text color For visualizations using a grid of charts , you can apply the annotation only on a specific chart Use the format: My label :: 2012 :: area_color / text_color :: facet_name For example: `My label :: 2012 >> 2015 :: #eb0000 / #0084bd :: Category 1`. Flourish type hint: text, defaults to `NULL`  
`chart_axes_highlights_y_area_color`| Area. Flourish type hint: color, defaults to `NULL`  
`chart_axes_highlights_y_area_opacity`| Area opacity. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_y_area_texture`| Area texture. Choices: none, pattern-diagonal, pattern-grid, pattern-dots. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_y_label_x_position`| X position. Choices: left, middle, right. Horizontally position label on the left, the middle or the right end of the line. This setting will be ignored if there is not enough space for the selected position. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_y_label_y_position`| Y position. Choices: above, middle, below. Vertically position the label above, below or in the middle of the line. This setting will be ignored if there is not enough space for the selected position. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_y_label_max_width`| Max width. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_y_font_size`| Font size. Flourish type hint: number, defaults to `NULL`  
`chart_axes_highlights_y_font_weight`| Font weight. Choices: regular, bold. Flourish type hint: string, defaults to `NULL`  
`chart_axes_highlights_y_label_color`| Text. Flourish type hint: color, defaults to `NULL`  
`chart_axes_highlights_y_shadow_color`| Shadow. Flourish type hint: color, defaults to `NULL`  
`chart_axes_highlights_y_shadow_enabled`| Shadow. Flourish type hint: boolean, defaults to `NULL`  
`annotations_styles`| Show styling options. Flourish type hint: boolean, defaults to `NULL`  
`chart_annotations_defaults_text_weight`| Weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`chart_annotations_defaults_text_size`| Text size. Flourish type hint: number, defaults to `NULL`  
`chart_annotations_defaults_text_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`chart_annotations_defaults_label_width`| Max width. Flourish type hint: number, defaults to `NULL`  
`chart_annotations_defaults_text_background_mode`| Text background. Choices: none, outline, background. Flourish type hint: string, defaults to `NULL`  
`chart_annotations_defaults_text_bg`| Outline. Flourish type hint: color, defaults to `NULL`  
`chart_annotations_defaults_label_bg`| Background. Flourish type hint: color, defaults to `NULL`  
`chart_annotations_defaults_text_alignment`| Alignment. Choices: auto, start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_annotations_defaults_popup_position`| Popup position. Choices: center, left, right, top, bottom. Flourish type hint: string, defaults to `NULL`  
`chart_annotations_defaults_line_marker`| Marker. Choices: none, arrowhead_open, arrowhead. Flourish type hint: string, defaults to `NULL`  
`chart_annotations_defaults_stroke_width`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_annotations_defaults_stroke_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_annotations_defaults_connector_extend_line`| Extend line. Choices: enabled, disabled. Flourish type hint: string, defaults to `NULL`  
`data_trans_duration`| Animation duration. The duration of transitions in milliseconds, for example between two slides in a story. Flourish type hint: number, defaults to `NULL`  
`animate_on_load`| Animate on load. Flourish type hint: boolean, defaults to `NULL`  
`data_trans_bind_series`| Only animate series with same name. Determines how animations work when the data changes (e.g. between slides in a story ). When this is on, series (e.g. lines) will attempt to animate to become another line only if they have the same name (i.e. the same column header). Flourish type hint: boolean, defaults to `NULL`  
`data_trans_bind_data_points`| Only animate points with same label. Determines how animations work when the data changes (e.g. between slides in a story ). When this is on, data points (e.g. dots or bars) will attempt to animate to become other data points if they have the same label (e.g. date or category). Flourish type hint: boolean, defaults to `NULL`  
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
`chart_url_settings_enabled`| Update project from URL. Make it possible to change the visualizations settings/state from the URL hash, for example when embedding in an iframe or popup panel. Flourish type hint: boolean, defaults to `NULL`  
`chart_url_settings_whitelist`| Allowed state properties. List each state property you want to make changeable with the URL hash See the template page for a full list of state properties. Add one property name per line. Use dot format for nested properties, e.g. `layout.background_color`. Flourish type hint: text, defaults to `NULL`
