---
url: https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/
title: Set scatter chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:46.340138+00:00
---

# Set scatter chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set scatter chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_scatter_details(
    
        self,
    
        default_color: str = None,
    
        fill_opacity: float = None,
    
        default_shape: str = None,
    
        data_point_default_size: float = None,
    
        data_point_min_size: float = None,
    
        data_point_max_size: float = None,
    
        responsive_dots: bool = None,
    
        stroke_opacity: float = None,
    
        stroke_width: float = None,
    
        stroke_mode: str = None,
    
        stroke_color: str = None,
    
        render_mode: str = None,
    
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
    
        labels_show: bool = None,
    
        labels_selective: bool = None,
    
        label_color_type: str = None,
    
        label_color: str = None,
    
        labels_responsive: str = None,
    
        label_font_size: float = None,
    
        label_font_size_min: float = None,
    
        label_font_size_max: float = None,
    
        label_bg_size: float = None,
    
        label_max_width: float = None,
    
        label_align: str = None,
    
        label_x_offset: str = None,
    
        label_y_offset: str = None,
    
        height_mode: str = None,
    
        facet_aspect: float = None,
    
        facet_aspect_mobile: float = None,
    
        chart_background_background_color_enabled: bool = None,
    
        chart_background_background_image_enabled: bool = None,
    
        chart_background_background_color: str = None,
    
        chart_background_background_image_src: str = None,
    
        chart_background_background_image_size: str = None,
    
        chart_background_background_image_position: str = None,
    
        margin_top: float = None,
    
        margin_right: float = None,
    
        margin_bottom: float = None,
    
        margin_left: float = None,
    
        facet_fixed_cols: bool = None,
    
        facet_min_w: float = None,
    
        facet_cols: float = None,
    
        facet_gutter_w: float = None,
    
        facet_gutter_h: float = None,
    
        facet_header_font_size: float = None,
    
        facet_title_align: str = None,
    
        facet_header_color: str = None,
    
        lines_show: bool = None,
    
        line_width: float = None,
    
        line_curve: str = None,
    
        line_opacity: float = None,
    
        line_color_mode: str = None,
    
        line_per_facet: bool = None,
    
        line_color: str = None,
    
        line_arrows: bool = None,
    
        line_arrow_size: float = None,
    
        line_arrow_color_mode: str = None,
    
        line_arrow_color: str = None,
    
        x_matching: bool = None,
    
        x_single_row: bool = None,
    
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
    
        chart_x_axis_number_date_format_prefix: str = None,
    
        chart_x_axis_number_date_format_suffix: str = None,
    
        chart_x_axis_number_date_format_n_dec: float = None,
    
        chart_x_axis_number_date_format_advanced: bool = None,
    
        chart_x_axis_number_date_format_negative_sign: str = None,
    
        chart_x_axis_number_date_format_strip_zeros: bool = None,
    
        chart_x_axis_number_date_format_strip_separator: bool = None,
    
        chart_x_axis_number_date_format_transform_labels: bool = None,
    
        chart_x_axis_number_date_format_transform: str = None,
    
        chart_x_axis_number_date_format_multiply_divide_constant: float = None,
    
        chart_x_axis_number_date_format_exponentiate_constant: float = None,
    
        y_matching: bool = None,
    
        y_single_col: bool = None,
    
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
    
        chart_y_axis_number_date_format_prefix: str = None,
    
        chart_y_axis_number_date_format_suffix: str = None,
    
        chart_y_axis_number_date_format_n_dec: float = None,
    
        chart_y_axis_number_date_format_advanced: bool = None,
    
        chart_y_axis_number_date_format_negative_sign: str = None,
    
        chart_y_axis_number_date_format_strip_zeros: bool = None,
    
        chart_y_axis_number_date_format_strip_separator: bool = None,
    
        chart_y_axis_number_date_format_transform_labels: bool = None,
    
        chart_y_axis_number_date_format_transform: str = None,
    
        chart_y_axis_number_date_format_multiply_divide_constant: float = None,
    
        chart_y_axis_number_date_format_exponentiate_constant: float = None,
    
        legend_position: str = None,
    
        legend_filtering_mode: str = None,
    
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
    
        chart_continous_legend_show_legend: bool = None,
    
        chart_continous_legend_title_mode: str = None,
    
        chart_continous_legend_title: str = None,
    
        chart_continous_legend_color_band_width: float = None,
    
        chart_continous_legend_color_band_height: float = None,
    
        chart_continous_legend_color_band_radius: float = None,
    
        chart_continous_legend_binned_label_mode: str = None,
    
        chart_continous_legend_binned_label_custom: str = None,
    
        chart_continous_legend_legend_min: float = None,
    
        chart_continous_legend_additional_min_label: str = None,
    
        chart_continous_legend_legend_max: float = None,
    
        chart_continous_legend_additional_max_label: str = None,
    
        text_legend: str = None,
    
        text_legend_title: bool = None,
    
        text_legend_subtitle: bool = None,
    
        text_legend_bold: bool = None,
    
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
    
        chart_filter_controls_control_type: str = None,
    
        chart_filter_controls_control_styles: bool = None,
    
        chart_filter_controls_control_title: str = None,
    
        chart_filter_controls_button_group: bool = None,
    
        chart_filter_controls_button_group_width_mode: str = None,
    
        chart_filter_controls_button_group_width_fixed: float = None,
    
        chart_filter_controls_dropdown_width_mode: str = None,
    
        chart_filter_controls_dropdown_width_fixed: float = None,
    
        chart_filter_controls_slider_width: float = None,
    
        chart_filter_controls_slider_max_label_width: float = None,
    
        chart_filter_controls_slider_step_time: float = None,
    
        chart_filter_controls_slider_loop: bool = None,
    
        chart_filter_controls_slider_restart_pause: float = None,
    
        chart_filter_controls_sort: bool = None,
    
        filter_show_all: bool = None,
    
        filter_show_all_text: str = None,
    
        filter_updates_axes: str = None,
    
        slider_updates_axes: str = None,
    
        time_label_show: bool = None,
    
        time_label_color: str = None,
    
        time_label_opacity: float = None,
    
        time_label_font_size: float = None,
    
        chart_slider_filter_controls_control_type: str = None,
    
        chart_slider_filter_controls_control_styles: bool = None,
    
        chart_slider_filter_controls_control_title: str = None,
    
        chart_slider_filter_controls_button_group: bool = None,
    
        chart_slider_filter_controls_button_group_width_mode: str = None,
    
        chart_slider_filter_controls_button_group_width_fixed: float = None,
    
        chart_slider_filter_controls_dropdown_width_mode: str = None,
    
        chart_slider_filter_controls_dropdown_width_fixed: float = None,
    
        chart_slider_filter_controls_slider_width: float = None,
    
        chart_slider_filter_controls_slider_max_label_width: float = None,
    
        chart_slider_filter_controls_slider_step_time: float = None,
    
        chart_slider_filter_controls_slider_loop: bool = None,
    
        chart_slider_filter_controls_slider_restart_pause: float = None,
    
        chart_slider_filter_controls_sort: bool = None,
    
        chart_filter_controls_container_alignment: str = None,
    
        chart_filter_controls_container_controls_spacing: float = None,
    
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
    
        chart_slider_control_style_track_color: str = None,
    
        chart_slider_control_style_font_color: str = None,
    
        chart_slider_control_style_handle_color: str = None,
    
        chart_slider_control_style_play_color: str = None,
    
        chart_slider_control_style_track_height: float = None,
    
        chart_slider_control_style_handle_height: float = None,
    
        chart_slider_control_style_play_button: bool = None,
    
        fit_type: str = None,
    
        fit_force_origin: bool = None,
    
        fit_line_width: float = None,
    
        fit_line_dash: float = None,
    
        fit_line_color: str = None,
    
        beeswarm_plot: bool = None,
    
        box_plot: bool = None,
    
        box_color: str = None,
    
        box_opacity: float = None,
    
        box_line_color: str = None,
    
        box_line_width: float = None,
    
        box_whisker_type: str = None,
    
        box_whisker_multiplier: float = None,
    
        use_box_popup: bool = None,
    
        box_first_quartile_text: str = None,
    
        box_median_text: str = None,
    
        box_third_quartile_text: str = None,
    
        violin_plot: bool = None,
    
        violin_bandwidth: float = None,
    
        violin_samples: float = None,
    
        violin_color: str = None,
    
        violin_opacity: float = None,
    
        violin_sizing: str = None,
    
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
    
        annotations_styling: bool = None,
    
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
    
        animation_duration: float = None,
    
        animation_stagger: float = None,
    
        line_animate_in: bool = None,
    
        line_animate_out: bool = None,
    
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
    
    
    set_scatter_details(
    
        .,
    
        default_color = NULL,
    
        fill_opacity = NULL,
    
        default_shape = NULL,
    
        data_point_default_size = NULL,
    
        data_point_min_size = NULL,
    
        data_point_max_size = NULL,
    
        responsive_dots = NULL,
    
        stroke_opacity = NULL,
    
        stroke_width = NULL,
    
        stroke_mode = NULL,
    
        stroke_color = NULL,
    
        render_mode = NULL,
    
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
    
        labels_show = NULL,
    
        labels_selective = NULL,
    
        label_color_type = NULL,
    
        label_color = NULL,
    
        labels_responsive = NULL,
    
        label_font_size = NULL,
    
        label_font_size_min = NULL,
    
        label_font_size_max = NULL,
    
        label_bg_size = NULL,
    
        label_max_width = NULL,
    
        label_align = NULL,
    
        label_x_offset = NULL,
    
        label_y_offset = NULL,
    
        height_mode = NULL,
    
        facet_aspect = NULL,
    
        facet_aspect_mobile = NULL,
    
        chart_background_background_color_enabled = NULL,
    
        chart_background_background_image_enabled = NULL,
    
        chart_background_background_color = NULL,
    
        chart_background_background_image_src = NULL,
    
        chart_background_background_image_size = NULL,
    
        chart_background_background_image_position = NULL,
    
        margin_top = NULL,
    
        margin_right = NULL,
    
        margin_bottom = NULL,
    
        margin_left = NULL,
    
        facet_fixed_cols = NULL,
    
        facet_min_w = NULL,
    
        facet_cols = NULL,
    
        facet_gutter_w = NULL,
    
        facet_gutter_h = NULL,
    
        facet_header_font_size = NULL,
    
        facet_title_align = NULL,
    
        facet_header_color = NULL,
    
        lines_show = NULL,
    
        line_width = NULL,
    
        line_curve = NULL,
    
        line_opacity = NULL,
    
        line_color_mode = NULL,
    
        line_per_facet = NULL,
    
        line_color = NULL,
    
        line_arrows = NULL,
    
        line_arrow_size = NULL,
    
        line_arrow_color_mode = NULL,
    
        line_arrow_color = NULL,
    
        x_matching = NULL,
    
        x_single_row = NULL,
    
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
    
        chart_x_axis_number_date_format_prefix = NULL,
    
        chart_x_axis_number_date_format_suffix = NULL,
    
        chart_x_axis_number_date_format_n_dec = NULL,
    
        chart_x_axis_number_date_format_advanced = NULL,
    
        chart_x_axis_number_date_format_negative_sign = NULL,
    
        chart_x_axis_number_date_format_strip_zeros = NULL,
    
        chart_x_axis_number_date_format_strip_separator = NULL,
    
        chart_x_axis_number_date_format_transform_labels = NULL,
    
        chart_x_axis_number_date_format_transform = NULL,
    
        chart_x_axis_number_date_format_multiply_divide_constant = NULL,
    
        chart_x_axis_number_date_format_exponentiate_constant = NULL,
    
        y_matching = NULL,
    
        y_single_col = NULL,
    
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
    
        chart_y_axis_number_date_format_prefix = NULL,
    
        chart_y_axis_number_date_format_suffix = NULL,
    
        chart_y_axis_number_date_format_n_dec = NULL,
    
        chart_y_axis_number_date_format_advanced = NULL,
    
        chart_y_axis_number_date_format_negative_sign = NULL,
    
        chart_y_axis_number_date_format_strip_zeros = NULL,
    
        chart_y_axis_number_date_format_strip_separator = NULL,
    
        chart_y_axis_number_date_format_transform_labels = NULL,
    
        chart_y_axis_number_date_format_transform = NULL,
    
        chart_y_axis_number_date_format_multiply_divide_constant = NULL,
    
        chart_y_axis_number_date_format_exponentiate_constant = NULL,
    
        legend_position = NULL,
    
        legend_filtering_mode = NULL,
    
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
    
        chart_continous_legend_show_legend = NULL,
    
        chart_continous_legend_title_mode = NULL,
    
        chart_continous_legend_title = NULL,
    
        chart_continous_legend_color_band_width = NULL,
    
        chart_continous_legend_color_band_height = NULL,
    
        chart_continous_legend_color_band_radius = NULL,
    
        chart_continous_legend_binned_label_mode = NULL,
    
        chart_continous_legend_binned_label_custom = NULL,
    
        chart_continous_legend_legend_min = NULL,
    
        chart_continous_legend_additional_min_label = NULL,
    
        chart_continous_legend_legend_max = NULL,
    
        chart_continous_legend_additional_max_label = NULL,
    
        text_legend = NULL,
    
        text_legend_title = NULL,
    
        text_legend_subtitle = NULL,
    
        text_legend_bold = NULL,
    
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
    
        chart_filter_controls_control_type = NULL,
    
        chart_filter_controls_control_styles = NULL,
    
        chart_filter_controls_control_title = NULL,
    
        chart_filter_controls_button_group = NULL,
    
        chart_filter_controls_button_group_width_mode = NULL,
    
        chart_filter_controls_button_group_width_fixed = NULL,
    
        chart_filter_controls_dropdown_width_mode = NULL,
    
        chart_filter_controls_dropdown_width_fixed = NULL,
    
        chart_filter_controls_slider_width = NULL,
    
        chart_filter_controls_slider_max_label_width = NULL,
    
        chart_filter_controls_slider_step_time = NULL,
    
        chart_filter_controls_slider_loop = NULL,
    
        chart_filter_controls_slider_restart_pause = NULL,
    
        chart_filter_controls_sort = NULL,
    
        filter_show_all = NULL,
    
        filter_show_all_text = NULL,
    
        filter_updates_axes = NULL,
    
        slider_updates_axes = NULL,
    
        time_label_show = NULL,
    
        time_label_color = NULL,
    
        time_label_opacity = NULL,
    
        time_label_font_size = NULL,
    
        chart_slider_filter_controls_control_type = NULL,
    
        chart_slider_filter_controls_control_styles = NULL,
    
        chart_slider_filter_controls_control_title = NULL,
    
        chart_slider_filter_controls_button_group = NULL,
    
        chart_slider_filter_controls_button_group_width_mode = NULL,
    
        chart_slider_filter_controls_button_group_width_fixed = NULL,
    
        chart_slider_filter_controls_dropdown_width_mode = NULL,
    
        chart_slider_filter_controls_dropdown_width_fixed = NULL,
    
        chart_slider_filter_controls_slider_width = NULL,
    
        chart_slider_filter_controls_slider_max_label_width = NULL,
    
        chart_slider_filter_controls_slider_step_time = NULL,
    
        chart_slider_filter_controls_slider_loop = NULL,
    
        chart_slider_filter_controls_slider_restart_pause = NULL,
    
        chart_slider_filter_controls_sort = NULL,
    
        chart_filter_controls_container_alignment = NULL,
    
        chart_filter_controls_container_controls_spacing = NULL,
    
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
    
        chart_slider_control_style_track_color = NULL,
    
        chart_slider_control_style_font_color = NULL,
    
        chart_slider_control_style_handle_color = NULL,
    
        chart_slider_control_style_play_color = NULL,
    
        chart_slider_control_style_track_height = NULL,
    
        chart_slider_control_style_handle_height = NULL,
    
        chart_slider_control_style_play_button = NULL,
    
        fit_type = NULL,
    
        fit_force_origin = NULL,
    
        fit_line_width = NULL,
    
        fit_line_dash = NULL,
    
        fit_line_color = NULL,
    
        beeswarm_plot = NULL,
    
        box_plot = NULL,
    
        box_color = NULL,
    
        box_opacity = NULL,
    
        box_line_color = NULL,
    
        box_line_width = NULL,
    
        box_whisker_type = NULL,
    
        box_whisker_multiplier = NULL,
    
        use_box_popup = NULL,
    
        box_first_quartile_text = NULL,
    
        box_median_text = NULL,
    
        box_third_quartile_text = NULL,
    
        violin_plot = NULL,
    
        violin_bandwidth = NULL,
    
        violin_samples = NULL,
    
        violin_color = NULL,
    
        violin_opacity = NULL,
    
        violin_sizing = NULL,
    
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
    
        annotations_styling = NULL,
    
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
    
        animation_duration = NULL,
    
        animation_stagger = NULL,
    
        line_animate_in = NULL,
    
        line_animate_out = NULL,
    
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
`default_color`| `str`, optional| Default color. Used when Color column is unspecified. Flourish type hint: color, defaults to None  
`fill_opacity`| `float`, optional| Dot opacity. Flourish type hint: number, defaults to None  
`default_shape`| `str`, optional| Default shape. Choices: circle, cross, diamond, square, star, triangle, wye. Used when Shape column is unspecified or empty. Flourish type hint: string, defaults to None  
`data_point_default_size`| `float`, optional| Size. In pixel area. Only used when Size column is unspecified or empty. Subject to scaling with the chart size (see setting below). Flourish type hint: number, defaults to None  
`data_point_min_size`| `float`, optional| Min size. In pixel area. Used when you have a Size column selected. Subject to scaling with the chart size. Flourish type hint: number, defaults to None  
`data_point_max_size`| `float`, optional| Max size. In pixel area. Used when you have a Size column selected. Subject to scaling with the chart size. Flourish type hint: number, defaults to None  
`responsive_dots`| `bool`, optional| Scale dots based on chart size. Makes the dots get bigger or smaller relative to the chart size. Turn off to specify a fixed size regardless of chart size. Flourish type hint: boolean, defaults to None  
`stroke_opacity`| `float`, optional| Outline opacity. Flourish type hint: number, defaults to None  
`stroke_width`| `float`, optional| Outline width. Flourish type hint: number, defaults to None  
`stroke_mode`| `str`, optional| Outline mode. Choices: auto, fixed. Choose Auto for outline color to match dot color. Choose Fixed to give all dots a uniform outline color. Flourish type hint: string, defaults to None  
`stroke_color`| `str`, optional| Outline color. Flourish type hint: color, defaults to None  
`render_mode`| `str`, optional| Renderer. Choices: svg, webgl. In most cases you should only need SVG, but you may want to choose WebGL if you have a lot of data or you notice your chart is running slowly on your device. Flourish type hint: string, defaults to None  
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
`labels_show`| `bool`, optional| Show labels on points. Labels only show up if you have designated a Name column in the data tab. Flourish type hint: boolean, defaults to None  
`labels_selective`| `bool`, optional| Labels to show. Choices: False, True. To show labels selectively, turn on this option and then make a story In the story editor, click on dots to hide/show the labels. Flourish type hint: boolean, defaults to None  
`label_color_type`| `str`, optional| Label color. Choices: auto, match, fixed. Flourish type hint: string, defaults to None  
`label_color`| `str`, optional| Fixed. Flourish type hint: color, defaults to None  
`labels_responsive`| `str`, optional| Scale label. Choices: chart, data, none. Choose between no scale, scale by chart size, or try to fit the label in the data point. Flourish type hint: string, defaults to None  
`label_font_size`| `float`, optional| Font size. Flourish type hint: number, defaults to None  
`label_font_size_min`| `float`, optional| Min font size. Flourish type hint: number, defaults to None  
`label_font_size_max`| `float`, optional| Max font size. Flourish type hint: number, defaults to None  
`label_bg_size`| `float`, optional| Shadow size. As percent of font size. Flourish type hint: number, defaults to None  
`label_max_width`| `float`, optional| Max width. Flourish type hint: number, defaults to None  
`label_align`| `str`, optional| Alignment. Choices: auto, start, middle, end. Align the text at the start, middle or end of the data point. Flourish type hint: string, defaults to None  
`label_x_offset`| `str`, optional| Offset. Choices: top, next. Place labels on top of or next to the data point. Flourish type hint: string, defaults to None  
`label_y_offset`| `str`, optional| Offset. Choices: top, above, below. Place labels on top of or next to the data point. Flourish type hint: string, defaults to None  
`height_mode`| `str`, optional| Sizing mode. Choices: auto, fill_space, aspect. In Fill space mode the graphic will fill the container (which by default will be the the standard Flourish responsive chart size). In Aspect ratio mode, you set the aspect ratio of the plot, and the container will be updated to accommodate it (not supported when embedded in a simple fixed-height iframe ). Flourish type hint: string, defaults to None  
`facet_aspect`| `float`, optional| Aspect (desktop). Aspect ratio of each plot in desktop mode, where 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to None  
`facet_aspect_mobile`| `float`, optional| Aspect (mobile). Aspect of each plot in mobile mode, where 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to None  
`chart_background_background_color_enabled`| `bool`, optional| Color. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_background_background_image_enabled`| `bool`, optional| Image. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_background_background_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_background_background_image_src`| `str`, optional| Image URL. Flourish type hint: url, defaults to None  
`chart_background_background_image_size`| `str`, optional| Size. Choices: stretch, slice, meet. Flourish type hint: string, defaults to None  
`chart_background_background_image_position`| `str`, optional| Position. Choices: x_min_y_min, x_mid_y_min, x_max_y_min, x_max_y_mid, x_mid_y_mid, x_min_y_max, x_mid_y_max, x_max_y_max. Flourish type hint: string, defaults to None  
`margin_top`| `float`, optional| Top. Flourish type hint: number, defaults to None  
`margin_right`| `float`, optional| Right. Flourish type hint: number, defaults to None  
`margin_bottom`| `float`, optional| Bottom. Flourish type hint: number, defaults to None  
`margin_left`| `float`, optional| Left. Flourish type hint: number, defaults to None  
`facet_fixed_cols`| `bool`, optional| Fixed number of columns in grid. Flourish type hint: boolean, defaults to None  
`facet_min_w`| `float`, optional| Min chart width. Determines how many columns of charts there should be in the grid. Ignored if you specify a fixed number of columns. Flourish type hint: number, defaults to None  
`facet_cols`| `float`, optional| Number of columns in grid. Flourish type hint: number, defaults to None  
`facet_gutter_w`| `float`, optional| Horizontal. In rems. Flourish type hint: number, defaults to None  
`facet_gutter_h`| `float`, optional| Vertical. In rems. Flourish type hint: number, defaults to None  
`facet_header_font_size`| `float`, optional| Text size. In rems. Flourish type hint: number, defaults to None  
`facet_title_align`| `str`, optional| Alignment. Choices: auto, left, center. Flourish type hint: string, defaults to None  
`facet_header_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`lines_show`| `bool`, optional| Shows lines. Flourish type hint: boolean, defaults to None  
`line_width`| `float`, optional| Line width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`line_curve`| `str`, optional| Line style. Choices: curve_linear, curve_natural. Flourish type hint: string, defaults to None  
`line_opacity`| `float`, optional| Line opacity. Flourish type hint: number, defaults to None  
`line_color_mode`| `str`, optional| Line color. Choices: by_dot, fixed. When set to Match dots the lines will be the same as the first dot in the line. Flourish type hint: string, defaults to None  
`line_per_facet`| `bool`, optional| Lock lines to axes. Disable to allow lines to run between or animate between facets. Flourish type hint: boolean, defaults to None  
`line_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`line_arrows`| `bool`, optional| Arrow heads on lines. Flourish type hint: boolean, defaults to None  
`line_arrow_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`line_arrow_color_mode`| `str`, optional| Color mode. Choices: auto, fixed. Flourish type hint: string, defaults to None  
`line_arrow_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`x_matching`| `bool`, optional| Matching x axis across grid of charts. Flourish type hint: boolean, defaults to None  
`x_single_row`| `bool`, optional| Only show x axis on first column of grid. Flourish type hint: boolean, defaults to None  
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
`chart_x_axis_number_date_format_prefix`| `str`, optional| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to None  
`chart_x_axis_number_date_format_suffix`| `str`, optional| Suffix. Text to place after a number. Flourish type hint: string, defaults to None  
`chart_x_axis_number_date_format_n_dec`| `float`, optional| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to None  
`chart_x_axis_number_date_format_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_x_axis_number_date_format_negative_sign`| `str`, optional| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to None  
`chart_x_axis_number_date_format_strip_zeros`| `bool`, optional| Remove trailing zeros. Flourish type hint: boolean, defaults to None  
`chart_x_axis_number_date_format_strip_separator`| `bool`, optional| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to None  
`chart_x_axis_number_date_format_transform_labels`| `bool`, optional| Multiply/divide values. Flourish type hint: boolean, defaults to None  
`chart_x_axis_number_date_format_transform`| `str`, optional| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to None  
`chart_x_axis_number_date_format_multiply_divide_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_x_axis_number_date_format_exponentiate_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`y_matching`| `bool`, optional| Matching y axis across grid of charts. Flourish type hint: boolean, defaults to None  
`y_single_col`| `bool`, optional| Only show Y axis on first column of grid. Flourish type hint: boolean, defaults to None  
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
`chart_y_axis_number_date_format_prefix`| `str`, optional| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to None  
`chart_y_axis_number_date_format_suffix`| `str`, optional| Suffix. Text to place after a number. Flourish type hint: string, defaults to None  
`chart_y_axis_number_date_format_n_dec`| `float`, optional| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to None  
`chart_y_axis_number_date_format_advanced`| `bool`, optional| Advanced. Flourish type hint: boolean, defaults to None  
`chart_y_axis_number_date_format_negative_sign`| `str`, optional| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to None  
`chart_y_axis_number_date_format_strip_zeros`| `bool`, optional| Remove trailing zeros. Flourish type hint: boolean, defaults to None  
`chart_y_axis_number_date_format_strip_separator`| `bool`, optional| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to None  
`chart_y_axis_number_date_format_transform_labels`| `bool`, optional| Multiply/divide values. Flourish type hint: boolean, defaults to None  
`chart_y_axis_number_date_format_transform`| `str`, optional| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to None  
`chart_y_axis_number_date_format_multiply_divide_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`chart_y_axis_number_date_format_exponentiate_constant`| `float`, optional| Flourish type hint: number, defaults to None  
`legend_position`| `str`, optional| Legend position. Choices: above, below, off. The legend position relative to the chart. A legend will not show with a single entry. Flourish type hint: string, defaults to None  
`legend_filtering_mode`| `str`, optional| Clickable legend. Choices: filter_out, filter_in, off. When a legend item is clicked on, the corresponding dots can either be hidden or shown. This option can also be turned off. Flourish type hint: string, defaults to None  
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
`chart_continous_legend_show_legend`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_continous_legend_title_mode`| `str`, optional| Title mode. Choices: auto, custom. Flourish type hint: string, defaults to None  
`chart_continous_legend_title`| `str`, optional| Title. Flourish type hint: string, defaults to None  
`chart_continous_legend_color_band_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_continous_legend_color_band_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`chart_continous_legend_color_band_radius`| `float`, optional| Roundness. The radius of the corners of the color band (in pixels). Flourish type hint: number, defaults to None  
`chart_continous_legend_binned_label_mode`| `str`, optional| Binned label mode. Choices: thresholds, centers, custom. Flourish type hint: string, defaults to None  
`chart_continous_legend_binned_label_custom`| `str`, optional| Custom bin labels. List numeric values, separated by semi-colons. Flourish type hint: string, defaults to None  
`chart_continous_legend_legend_min`| `float`, optional| Legend min. Flourish type hint: number, defaults to None  
`chart_continous_legend_additional_min_label`| `str`, optional| Custom min label. Flourish type hint: string, defaults to None  
`chart_continous_legend_legend_max`| `float`, optional| Legend max. Flourish type hint: number, defaults to None  
`chart_continous_legend_additional_max_label`| `str`, optional| Custom max label. Flourish type hint: string, defaults to None  
`text_legend`| `str`, optional| Choices: auto, custom, off. Flourish type hint: string, defaults to None  
`text_legend_title`| `bool`, optional| Title. Flourish type hint: boolean, defaults to None  
`text_legend_subtitle`| `bool`, optional| Subtitle. Flourish type hint: boolean, defaults to None  
`text_legend_bold`| `bool`, optional| Bold. If checked, always use bold for colored items. Flourish type hint: boolean, defaults to None  
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
`chart_popup_mode`| `str`, optional| Choices: none, popup, panel, both. Flourish type hint: string, defaults to None  
`chart_popup_popup_is_custom`| `bool`, optional| Popup content. Choices: False, True. Flourish type hint: boolean, defaults to None  
`chart_popup_show_popup_styles`| `bool`, optional| Show popup styles. Flourish type hint: boolean, defaults to None  
`chart_popup_popup_custom_header`| `Union[list, str]`, optional| Popup custom header. Use `{{column_name}}` to add a value from your data Ensure the column is selected, or add it to Info for popups for popup use. Advanced users can add HTML styling or add category colors to popup headers. To hide parts of the popup when a column is empty using `{{#if column_name}}Content for non-empty column_name{{/if}}`. For example: `{{#if Capital name}}Capital:{{/if}} {{Capital name}}`. Here, the word "Capital:" will only show if the corresponding cell in the "Capital name" column is not empty. Flourish type hint: html, defaults to None  
`chart_popup_popup_custom_main`| `Union[list, str]`, optional| Popup custom main content. Use `{{column_name}}` to add a value from your data Ensure the column is selected, or add it to Info for popups for popup use. Advanced users can add HTML for designs, styles, and images. To hide parts of the popup when a column is empty use the syntax `{{#if column_name}}Content for non-empty column_name{{/if}}`. For example: `{{#if Capital name}}Capital:{{/if}} {{Capital name}}`. Here, the word "Capital:" will only show if the corresponding cell in the "Capital name" column is not empty. Flourish type hint: html, defaults to None  
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
`chart_popup_panel_custom_header`| `Union[list, str]`, optional| Panel custom header. Use `{{column_name}}` to add a value from your data Ensure the column is selected, or add it to Info for popups for panel use. Advanced users can add HTML for styling or add category colors to panel headers. To hide parts of the panel when a column is empty using `{{#if column_name}}Content for non-empty column_name{{/if}}`. For example: `{{#if Capital name}}Capital:{{/if}} {{Capital name}}`. Here, the word "Capital:" will only show if the corresponding cell in the "Capital name" column is not empty. Flourish type hint: html, defaults to None  
`chart_popup_panel_custom_main`| `Union[list, str]`, optional| Panel custom main content. Use `{{column_name}}` to add a value from your data Ensure the column is selected, or add it to Info for popups for panel use. Advanced users can add HTML for designs, styles, images, videos and embedded Flourish charts, To hide parts of the panel when a column is empty using `{{#if column_name}}Content for non-empty column_name{{/if}}`. For example: `{{#if Capital name}}Capital:{{/if}} {{Capital name}}`. Here, the word "Capital:" will only show if the corresponding cell in the "Capital name" column is not empty. Flourish type hint: html, defaults to None  
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
`chart_filter_controls_control_type`| `str`, optional| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to None  
`chart_filter_controls_control_styles`| `bool`, optional| Adv. Flourish type hint: boolean, defaults to None  
`chart_filter_controls_control_title`| `str`, optional| Control title. Flourish type hint: string, defaults to None  
`chart_filter_controls_button_group`| `bool`, optional| Grouped. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_filter_controls_button_group_width_mode`| `str`, optional| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_filter_controls_button_group_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_filter_controls_dropdown_width_mode`| `str`, optional| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_filter_controls_dropdown_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_filter_controls_slider_width`| `float`, optional| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to None  
`chart_filter_controls_slider_max_label_width`| `float`, optional| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to None  
`chart_filter_controls_slider_step_time`| `float`, optional| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to None  
`chart_filter_controls_slider_loop`| `bool`, optional| Loop. Flourish type hint: boolean, defaults to None  
`chart_filter_controls_slider_restart_pause`| `float`, optional| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to None  
`chart_filter_controls_sort`| `bool`, optional| Sorting. Choices: True, False. Flourish type hint: boolean, defaults to None  
`filter_show_all`| `bool`, optional| Include "All". Flourish type hint: boolean, defaults to None  
`filter_show_all_text`| `str`, optional| “All” label. Flourish type hint: string, defaults to None  
`filter_updates_axes`| `str`, optional| Update axes when filtering. Choices: off, x, y, both. Flourish type hint: string, defaults to None  
`slider_updates_axes`| `str`, optional| Update axes when using slider. Choices: off, x, y, both. Flourish type hint: string, defaults to None  
`time_label_show`| `bool`, optional| Show time label. Flourish type hint: boolean, defaults to None  
`time_label_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`time_label_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`time_label_font_size`| `float`, optional| Size. As a percent of the default size; the actual size scales with the chart. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_control_type`| `str`, optional| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to None  
`chart_slider_filter_controls_control_styles`| `bool`, optional| Adv. Flourish type hint: boolean, defaults to None  
`chart_slider_filter_controls_control_title`| `str`, optional| Control title. Flourish type hint: string, defaults to None  
`chart_slider_filter_controls_button_group`| `bool`, optional| Grouped. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_slider_filter_controls_button_group_width_mode`| `str`, optional| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_slider_filter_controls_button_group_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_dropdown_width_mode`| `str`, optional| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to None  
`chart_slider_filter_controls_dropdown_width_fixed`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_slider_width`| `float`, optional| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_slider_max_label_width`| `float`, optional| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_slider_step_time`| `float`, optional| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_slider_loop`| `bool`, optional| Loop. Flourish type hint: boolean, defaults to None  
`chart_slider_filter_controls_slider_restart_pause`| `float`, optional| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to None  
`chart_slider_filter_controls_sort`| `bool`, optional| Sorting. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_filter_controls_container_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`chart_filter_controls_container_controls_spacing`| `float`, optional| Spacing. The space between controls, like dropdowns and adjacent button sets, in em units. Flourish type hint: number, defaults to None  
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
`chart_slider_control_style_track_color`| `str`, optional| Track. Flourish type hint: color, defaults to None  
`chart_slider_control_style_font_color`| `str`, optional| Text. Flourish type hint: color, defaults to None  
`chart_slider_control_style_handle_color`| `str`, optional| Handle. Flourish type hint: color, defaults to None  
`chart_slider_control_style_play_color`| `str`, optional| Play/pause. Flourish type hint: color, defaults to None  
`chart_slider_control_style_track_height`| `float`, optional| Track height. Flourish type hint: number, defaults to None  
`chart_slider_control_style_handle_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`chart_slider_control_style_play_button`| `bool`, optional| Play button. Flourish type hint: boolean, defaults to None  
`fit_type`| `str`, optional| Lines to show. Choices: none, both, color, chart, all. Flourish type hint: string, defaults to None  
`fit_force_origin`| `bool`, optional| Force line through origin. Flourish type hint: boolean, defaults to None  
`fit_line_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`fit_line_dash`| `float`, optional| Dash. Flourish type hint: number, defaults to None  
`fit_line_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`beeswarm_plot`| `bool`, optional| Show beeswarm when plotting one numerical and one categorical axis. Choices: True, False. Auto mode will make a beeswarm unless there are more than 5000 points in the dataset. Note: Performance will be reduced with thousands of rows due to the nature of how beeswarm positions are computed. Flourish type hint: boolean, defaults to None  
`box_plot`| `bool`, optional| Show box plot when plotting one numerical and one categorical axis. Choices: True, False. To learn more about box plots [see here](https://helpcenter.flourish.studio/hc/en-us/articles/9859136207759-How-to-make-box-violin-and-beeswarm-scatter-plots). Flourish type hint: boolean, defaults to None  
`box_color`| `str`, optional| Box color. Flourish type hint: color, defaults to None  
`box_opacity`| `float`, optional| Box opacity. Flourish type hint: number, defaults to None  
`box_line_color`| `str`, optional| Line color. Flourish type hint: color, defaults to None  
`box_line_width`| `float`, optional| Line width. Flourish type hint: number, defaults to None  
`box_whisker_type`| `str`, optional| Whisker type. Choices: tukey, all. Flourish type hint: string, defaults to None  
`box_whisker_multiplier`| `float`, optional| Max whisker length (number of IQRs). Maximum distance whiskers should extend out from the box as a multiple of the interquartile range. 1.5 is John Tukeys classsic value. Flourish type hint: number, defaults to None  
`use_box_popup`| `bool`, optional| Box popup. If enabled, shows a popup for the box describing the first quartile, median, and third quartile. The user will not be able to access the popups for the points underneath the box. Flourish type hint: boolean, defaults to None  
`box_first_quartile_text`| `str`, optional| First quartile. Flourish type hint: string, defaults to None  
`box_median_text`| `str`, optional| Median. Flourish type hint: string, defaults to None  
`box_third_quartile_text`| `str`, optional| Third quartile. Flourish type hint: string, defaults to None  
`violin_plot`| `bool`, optional| Show violin plot when plotting one numerical and one categorical axis. Choices: True, False. To learn more about violin plots [see here](https://helpcenter.flourish.studio/hc/en-us/articles/9859136207759-How-to-make-box-violin-and-beeswarm-scatter-plots). Flourish type hint: boolean, defaults to None  
`violin_bandwidth`| `float`, optional| Bandwidth. The bandwidth in a violin plot determines the degree of smoothing applied to the probability density function estimating the shape of the plot. Generally, larger bandwidth values create a smoother plot with less detail, while smaller values create a more precise plot with more detail. Flourish type hint: number, defaults to None  
`violin_samples`| `float`, optional| No. of samples. Number of points at which to calculate a violins distribution. More points means a more accurate curve but can also harm performance. Flourish type hint: number, defaults to None  
`violin_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`violin_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`violin_sizing`| `str`, optional| Sizing mode. Choices: area, width. Flourish type hint: string, defaults to None  
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
`annotations_styling`| `bool`, optional| Show annotations styling. Flourish type hint: boolean, defaults to None  
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
`animation_duration`| `float`, optional| Animation duration. The duration of the animation for each dot or axis, in seconds. The animation can be seen between slides in a Flourish story. Flourish type hint: number, defaults to None  
`animation_stagger`| `float`, optional| Animation stagger. The delay between each dot starting to move, in seconds; set to 0 to have all dots move simultaneously. Flourish type hint: number, defaults to None  
`line_animate_in`| `bool`, optional| Animate new lines in. Whether new lines should appear whole or be animated into view. Flourish type hint: boolean, defaults to None  
`line_animate_out`| `bool`, optional| Animate exiting lines. Whether filtered/removed lines should be removed whole or animated out of view. Flourish type hint: boolean, defaults to None  
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
`default_color`| Default color. Used when Color column is unspecified. Flourish type hint: color, defaults to `NULL`  
`fill_opacity`| Dot opacity. Flourish type hint: number, defaults to `NULL`  
`default_shape`| Default shape. Choices: circle, cross, diamond, square, star, triangle, wye. Used when Shape column is unspecified or empty. Flourish type hint: string, defaults to `NULL`  
`data_point_default_size`| Size. In pixel area. Only used when Size column is unspecified or empty. Subject to scaling with the chart size (see setting below). Flourish type hint: number, defaults to `NULL`  
`data_point_min_size`| Min size. In pixel area. Used when you have a Size column selected. Subject to scaling with the chart size. Flourish type hint: number, defaults to `NULL`  
`data_point_max_size`| Max size. In pixel area. Used when you have a Size column selected. Subject to scaling with the chart size. Flourish type hint: number, defaults to `NULL`  
`responsive_dots`| Scale dots based on chart size. Makes the dots get bigger or smaller relative to the chart size. Turn off to specify a fixed size regardless of chart size. Flourish type hint: boolean, defaults to `NULL`  
`stroke_opacity`| Outline opacity. Flourish type hint: number, defaults to `NULL`  
`stroke_width`| Outline width. Flourish type hint: number, defaults to `NULL`  
`stroke_mode`| Outline mode. Choices: auto, fixed. Choose Auto for outline color to match dot color. Choose Fixed to give all dots a uniform outline color. Flourish type hint: string, defaults to `NULL`  
`stroke_color`| Outline color. Flourish type hint: color, defaults to `NULL`  
`render_mode`| Renderer. Choices: svg, webgl. In most cases you should only need SVG, but you may want to choose WebGL if you have a lot of data or you notice your chart is running slowly on your device. Flourish type hint: string, defaults to `NULL`  
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
`labels_show`| Show labels on points. Labels only show up if you have designated a Name column in the data tab. Flourish type hint: boolean, defaults to `NULL`  
`labels_selective`| Labels to show. Choices: `FALSE`, `TRUE`. To show labels selectively, turn on this option and then make a story In the story editor, click on dots to hide/show the labels. Flourish type hint: boolean, defaults to `NULL`  
`label_color_type`| Label color. Choices: auto, match, fixed. Flourish type hint: string, defaults to `NULL`  
`label_color`| Fixed. Flourish type hint: color, defaults to `NULL`  
`labels_responsive`| Scale label. Choices: chart, data, none. Choose between no scale, scale by chart size, or try to fit the label in the data point. Flourish type hint: string, defaults to `NULL`  
`label_font_size`| Font size. Flourish type hint: number, defaults to `NULL`  
`label_font_size_min`| Min font size. Flourish type hint: number, defaults to `NULL`  
`label_font_size_max`| Max font size. Flourish type hint: number, defaults to `NULL`  
`label_bg_size`| Shadow size. As percent of font size. Flourish type hint: number, defaults to `NULL`  
`label_max_width`| Max width. Flourish type hint: number, defaults to `NULL`  
`label_align`| Alignment. Choices: auto, start, middle, end. Align the text at the start, middle or end of the data point. Flourish type hint: string, defaults to `NULL`  
`label_x_offset`| Offset. Choices: top, next. Place labels on top of or next to the data point. Flourish type hint: string, defaults to `NULL`  
`label_y_offset`| Offset. Choices: top, above, below. Place labels on top of or next to the data point. Flourish type hint: string, defaults to `NULL`  
`height_mode`| Sizing mode. Choices: auto, fill_space, aspect. In Fill space mode the graphic will fill the container (which by default will be the the standard Flourish responsive chart size). In Aspect ratio mode, you set the aspect ratio of the plot, and the container will be updated to accommodate it (not supported when embedded in a simple fixed-height iframe ). Flourish type hint: string, defaults to `NULL`  
`facet_aspect`| Aspect (desktop). Aspect ratio of each plot in desktop mode, where 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to `NULL`  
`facet_aspect_mobile`| Aspect (mobile). Aspect of each plot in mobile mode, where 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to `NULL`  
`chart_background_background_color_enabled`| Color. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_background_background_image_enabled`| Image. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_background_background_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_background_background_image_src`| Image URL. Flourish type hint: url, defaults to `NULL`  
`chart_background_background_image_size`| Size. Choices: stretch, slice, meet. Flourish type hint: string, defaults to `NULL`  
`chart_background_background_image_position`| Position. Choices: x_min_y_min, x_mid_y_min, x_max_y_min, x_max_y_mid, x_mid_y_mid, x_min_y_max, x_mid_y_max, x_max_y_max. Flourish type hint: string, defaults to `NULL`  
`margin_top`| Top. Flourish type hint: number, defaults to `NULL`  
`margin_right`| Right. Flourish type hint: number, defaults to `NULL`  
`margin_bottom`| Bottom. Flourish type hint: number, defaults to `NULL`  
`margin_left`| Left. Flourish type hint: number, defaults to `NULL`  
`facet_fixed_cols`| Fixed number of columns in grid. Flourish type hint: boolean, defaults to `NULL`  
`facet_min_w`| Min chart width. Determines how many columns of charts there should be in the grid. Ignored if you specify a fixed number of columns. Flourish type hint: number, defaults to `NULL`  
`facet_cols`| Number of columns in grid. Flourish type hint: number, defaults to `NULL`  
`facet_gutter_w`| Horizontal. In rems. Flourish type hint: number, defaults to `NULL`  
`facet_gutter_h`| Vertical. In rems. Flourish type hint: number, defaults to `NULL`  
`facet_header_font_size`| Text size. In rems. Flourish type hint: number, defaults to `NULL`  
`facet_title_align`| Alignment. Choices: auto, left, center. Flourish type hint: string, defaults to `NULL`  
`facet_header_color`| Color. Flourish type hint: color, defaults to `NULL`  
`lines_show`| Shows lines. Flourish type hint: boolean, defaults to `NULL`  
`line_width`| Line width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`line_curve`| Line style. Choices: curve_linear, curve_natural. Flourish type hint: string, defaults to `NULL`  
`line_opacity`| Line opacity. Flourish type hint: number, defaults to `NULL`  
`line_color_mode`| Line color. Choices: by_dot, fixed. When set to Match dots the lines will be the same as the first dot in the line. Flourish type hint: string, defaults to `NULL`  
`line_per_facet`| Lock lines to axes. Disable to allow lines to run between or animate between facets. Flourish type hint: boolean, defaults to `NULL`  
`line_color`| Color. Flourish type hint: color, defaults to `NULL`  
`line_arrows`| Arrow heads on lines. Flourish type hint: boolean, defaults to `NULL`  
`line_arrow_size`| Size. Flourish type hint: number, defaults to `NULL`  
`line_arrow_color_mode`| Color mode. Choices: auto, fixed. Flourish type hint: string, defaults to `NULL`  
`line_arrow_color`| Color. Flourish type hint: color, defaults to `NULL`  
`x_matching`| Matching x axis across grid of charts. Flourish type hint: boolean, defaults to `NULL`  
`x_single_row`| Only show x axis on first column of grid. Flourish type hint: boolean, defaults to `NULL`  
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
`chart_x_axis_number_date_format_prefix`| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_number_date_format_suffix`| Suffix. Text to place after a number. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_number_date_format_n_dec`| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_number_date_format_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_number_date_format_negative_sign`| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_number_date_format_strip_zeros`| Remove trailing zeros. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_number_date_format_strip_separator`| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_number_date_format_transform_labels`| Multiply/divide values. Flourish type hint: boolean, defaults to `NULL`  
`chart_x_axis_number_date_format_transform`| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to `NULL`  
`chart_x_axis_number_date_format_multiply_divide_constant`| Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_number_date_format_exponentiate_constant`| Flourish type hint: number, defaults to `NULL`  
`y_matching`| Matching y axis across grid of charts. Flourish type hint: boolean, defaults to `NULL`  
`y_single_col`| Only show Y axis on first column of grid. Flourish type hint: boolean, defaults to `NULL`  
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
`chart_y_axis_number_date_format_prefix`| Prefix. Text to place in front of a number. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_number_date_format_suffix`| Suffix. Text to place after a number. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_number_date_format_n_dec`| Decimal places. Decimal places. You can also enter a negative integer to round to a whole number with that many zeros. For example, -2 will round to the nearest hundred. Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_number_date_format_advanced`| Advanced. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_number_date_format_negative_sign`| Styling of negative numbers. Choices: -$nk, $-nk, ($nk), $(n)k, none. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_number_date_format_strip_zeros`| Remove trailing zeros. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_number_date_format_strip_separator`| Hide thousands separator below 10,000. Turn off if you want four-digit numbers to include a separator, e.g. 1,234 rather than 1234. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_number_date_format_transform_labels`| Multiply/divide values. Flourish type hint: boolean, defaults to `NULL`  
`chart_y_axis_number_date_format_transform`| Choices: multiply, divide, exponentiate. Flourish type hint: string, defaults to `NULL`  
`chart_y_axis_number_date_format_multiply_divide_constant`| Flourish type hint: number, defaults to `NULL`  
`chart_y_axis_number_date_format_exponentiate_constant`| Flourish type hint: number, defaults to `NULL`  
`legend_position`| Legend position. Choices: above, below, off. The legend position relative to the chart. A legend will not show with a single entry. Flourish type hint: string, defaults to `NULL`  
`legend_filtering_mode`| Clickable legend. Choices: filter_out, filter_in, off. When a legend item is clicked on, the corresponding dots can either be hidden or shown. This option can also be turned off. Flourish type hint: string, defaults to `NULL`  
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
`chart_continous_legend_show_legend`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_continous_legend_title_mode`| Title mode. Choices: auto, custom. Flourish type hint: string, defaults to `NULL`  
`chart_continous_legend_title`| Title. Flourish type hint: string, defaults to `NULL`  
`chart_continous_legend_color_band_width`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_continous_legend_color_band_height`| Height. Flourish type hint: number, defaults to `NULL`  
`chart_continous_legend_color_band_radius`| Roundness. The radius of the corners of the color band (in pixels). Flourish type hint: number, defaults to `NULL`  
`chart_continous_legend_binned_label_mode`| Binned label mode. Choices: thresholds, centers, custom. Flourish type hint: string, defaults to `NULL`  
`chart_continous_legend_binned_label_custom`| Custom bin labels. List numeric values, separated by semi-colons. Flourish type hint: string, defaults to `NULL`  
`chart_continous_legend_legend_min`| Legend min. Flourish type hint: number, defaults to `NULL`  
`chart_continous_legend_additional_min_label`| Custom min label. Flourish type hint: string, defaults to `NULL`  
`chart_continous_legend_legend_max`| Legend max. Flourish type hint: number, defaults to `NULL`  
`chart_continous_legend_additional_max_label`| Custom max label. Flourish type hint: string, defaults to `NULL`  
`text_legend`| Choices: auto, custom, off. Flourish type hint: string, defaults to `NULL`  
`text_legend_title`| Title. Flourish type hint: boolean, defaults to `NULL`  
`text_legend_subtitle`| Subtitle. Flourish type hint: boolean, defaults to `NULL`  
`text_legend_bold`| Bold. If checked, always use bold for colored items. Flourish type hint: boolean, defaults to `NULL`  
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
`chart_popup_mode`| Choices: none, popup, panel, both. Flourish type hint: string, defaults to `NULL`  
`chart_popup_popup_is_custom`| Popup content. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_show_popup_styles`| Show popup styles. Flourish type hint: boolean, defaults to `NULL`  
`chart_popup_popup_custom_header`| Popup custom header. Use `{{column_name}}` to add a value from your data Ensure the column is selected, or add it to Info for popups for popup use. Advanced users can add HTML styling or add category colors to popup headers. To hide parts of the popup when a column is empty using `{{#if column_name}}Content for non-empty column_name{{/if}}`. For example: `{{#if Capital name}}Capital:{{/if}} {{Capital name}}`. Here, the word "Capital:" will only show if the corresponding cell in the "Capital name" column is not empty. Flourish type hint: html, defaults to `NULL`  
`chart_popup_popup_custom_main`| Popup custom main content. Use `{{column_name}}` to add a value from your data Ensure the column is selected, or add it to Info for popups for popup use. Advanced users can add HTML for designs, styles, and images. To hide parts of the popup when a column is empty use the syntax `{{#if column_name}}Content for non-empty column_name{{/if}}`. For example: `{{#if Capital name}}Capital:{{/if}} {{Capital name}}`. Here, the word "Capital:" will only show if the corresponding cell in the "Capital name" column is not empty. Flourish type hint: html, defaults to `NULL`  
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
`chart_popup_panel_custom_header`| Panel custom header. Use `{{column_name}}` to add a value from your data Ensure the column is selected, or add it to Info for popups for panel use. Advanced users can add HTML for styling or add category colors to panel headers. To hide parts of the panel when a column is empty using `{{#if column_name}}Content for non-empty column_name{{/if}}`. For example: `{{#if Capital name}}Capital:{{/if}} {{Capital name}}`. Here, the word "Capital:" will only show if the corresponding cell in the "Capital name" column is not empty. Flourish type hint: html, defaults to `NULL`  
`chart_popup_panel_custom_main`| Panel custom main content. Use `{{column_name}}` to add a value from your data Ensure the column is selected, or add it to Info for popups for panel use. Advanced users can add HTML for designs, styles, images, videos and embedded Flourish charts, To hide parts of the panel when a column is empty using `{{#if column_name}}Content for non-empty column_name{{/if}}`. For example: `{{#if Capital name}}Capital:{{/if}} {{Capital name}}`. Here, the word "Capital:" will only show if the corresponding cell in the "Capital name" column is not empty. Flourish type hint: html, defaults to `NULL`  
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
`chart_filter_controls_control_type`| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to `NULL`  
`chart_filter_controls_control_styles`| Adv. Flourish type hint: boolean, defaults to `NULL`  
`chart_filter_controls_control_title`| Control title. Flourish type hint: string, defaults to `NULL`  
`chart_filter_controls_button_group`| Grouped. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_filter_controls_button_group_width_mode`| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_filter_controls_button_group_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_filter_controls_dropdown_width_mode`| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_filter_controls_dropdown_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_filter_controls_slider_width`| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to `NULL`  
`chart_filter_controls_slider_max_label_width`| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to `NULL`  
`chart_filter_controls_slider_step_time`| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to `NULL`  
`chart_filter_controls_slider_loop`| Loop. Flourish type hint: boolean, defaults to `NULL`  
`chart_filter_controls_slider_restart_pause`| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to `NULL`  
`chart_filter_controls_sort`| Sorting. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`filter_show_all`| Include "All". Flourish type hint: boolean, defaults to `NULL`  
`filter_show_all_text`| “All” label. Flourish type hint: string, defaults to `NULL`  
`filter_updates_axes`| Update axes when filtering. Choices: off, x, y, both. Flourish type hint: string, defaults to `NULL`  
`slider_updates_axes`| Update axes when using slider. Choices: off, x, y, both. Flourish type hint: string, defaults to `NULL`  
`time_label_show`| Show time label. Flourish type hint: boolean, defaults to `NULL`  
`time_label_color`| Color. Flourish type hint: color, defaults to `NULL`  
`time_label_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`time_label_font_size`| Size. As a percent of the default size; the actual size scales with the chart. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_control_type`| Control type. Choices: dropdown, buttons, slider. Choose between a dropdown, buttons or a time slider Flourish type hint: string, defaults to `NULL`  
`chart_slider_filter_controls_control_styles`| Adv. Flourish type hint: boolean, defaults to `NULL`  
`chart_slider_filter_controls_control_title`| Control title. Flourish type hint: string, defaults to `NULL`  
`chart_slider_filter_controls_button_group`| Grouped. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_slider_filter_controls_button_group_width_mode`| Button group width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_slider_filter_controls_button_group_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_dropdown_width_mode`| Dropdown width. Choices: auto, full, fixed. Flourish type hint: string, defaults to `NULL`  
`chart_slider_filter_controls_dropdown_width_fixed`| Width. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_slider_width`| Slider width. Width of the slider track in rems Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_slider_max_label_width`| Max label width. In rems, multiples of base font size. If larger than the longest label, only the space required to fit labels will be used. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_slider_step_time`| Time between steps. Measured in seconds, positive values move the slider left to right, negative values move the slider right to left. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_slider_loop`| Loop. Flourish type hint: boolean, defaults to `NULL`  
`chart_slider_filter_controls_slider_restart_pause`| Pause before loop. Measured in seconds and in addition to the regular step time displayed above. Flourish type hint: number, defaults to `NULL`  
`chart_slider_filter_controls_sort`| Sorting. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_filter_controls_container_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_filter_controls_container_controls_spacing`| Spacing. The space between controls, like dropdowns and adjacent button sets, in em units. Flourish type hint: number, defaults to `NULL`  
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
`chart_slider_control_style_track_color`| Track. Flourish type hint: color, defaults to `NULL`  
`chart_slider_control_style_font_color`| Text. Flourish type hint: color, defaults to `NULL`  
`chart_slider_control_style_handle_color`| Handle. Flourish type hint: color, defaults to `NULL`  
`chart_slider_control_style_play_color`| Play/pause. Flourish type hint: color, defaults to `NULL`  
`chart_slider_control_style_track_height`| Track height. Flourish type hint: number, defaults to `NULL`  
`chart_slider_control_style_handle_height`| Height. Flourish type hint: number, defaults to `NULL`  
`chart_slider_control_style_play_button`| Play button. Flourish type hint: boolean, defaults to `NULL`  
`fit_type`| Lines to show. Choices: none, both, color, chart, all. Flourish type hint: string, defaults to `NULL`  
`fit_force_origin`| Force line through origin. Flourish type hint: boolean, defaults to `NULL`  
`fit_line_width`| Width. Flourish type hint: number, defaults to `NULL`  
`fit_line_dash`| Dash. Flourish type hint: number, defaults to `NULL`  
`fit_line_color`| Color. Flourish type hint: color, defaults to `NULL`  
`beeswarm_plot`| Show beeswarm when plotting one numerical and one categorical axis. Choices: `TRUE`, `FALSE`. Auto mode will make a beeswarm unless there are more than 5000 points in the dataset. Note: Performance will be reduced with thousands of rows due to the nature of how beeswarm positions are computed. Flourish type hint: boolean, defaults to `NULL`  
`box_plot`| Show box plot when plotting one numerical and one categorical axis. Choices: `TRUE`, `FALSE`. To learn more about box plots [see here](https://helpcenter.flourish.studio/hc/en-us/articles/9859136207759-How-to-make-box-violin-and-beeswarm-scatter-plots). Flourish type hint: boolean, defaults to `NULL`  
`box_color`| Box color. Flourish type hint: color, defaults to `NULL`  
`box_opacity`| Box opacity. Flourish type hint: number, defaults to `NULL`  
`box_line_color`| Line color. Flourish type hint: color, defaults to `NULL`  
`box_line_width`| Line width. Flourish type hint: number, defaults to `NULL`  
`box_whisker_type`| Whisker type. Choices: tukey, all. Flourish type hint: string, defaults to `NULL`  
`box_whisker_multiplier`| Max whisker length (number of IQRs). Maximum distance whiskers should extend out from the box as a multiple of the interquartile range. 1.5 is John Tukeys classsic value. Flourish type hint: number, defaults to `NULL`  
`use_box_popup`| Box popup. If enabled, shows a popup for the box describing the first quartile, median, and third quartile. The user will not be able to access the popups for the points underneath the box. Flourish type hint: boolean, defaults to `NULL`  
`box_first_quartile_text`| First quartile. Flourish type hint: string, defaults to `NULL`  
`box_median_text`| Median. Flourish type hint: string, defaults to `NULL`  
`box_third_quartile_text`| Third quartile. Flourish type hint: string, defaults to `NULL`  
`violin_plot`| Show violin plot when plotting one numerical and one categorical axis. Choices: `TRUE`, `FALSE`. To learn more about violin plots [see here](https://helpcenter.flourish.studio/hc/en-us/articles/9859136207759-How-to-make-box-violin-and-beeswarm-scatter-plots). Flourish type hint: boolean, defaults to `NULL`  
`violin_bandwidth`| Bandwidth. The bandwidth in a violin plot determines the degree of smoothing applied to the probability density function estimating the shape of the plot. Generally, larger bandwidth values create a smoother plot with less detail, while smaller values create a more precise plot with more detail. Flourish type hint: number, defaults to `NULL`  
`violin_samples`| No. of samples. Number of points at which to calculate a violins distribution. More points means a more accurate curve but can also harm performance. Flourish type hint: number, defaults to `NULL`  
`violin_color`| Color. Flourish type hint: color, defaults to `NULL`  
`violin_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`violin_sizing`| Sizing mode. Choices: area, width. Flourish type hint: string, defaults to `NULL`  
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
`annotations_styling`| Show annotations styling. Flourish type hint: boolean, defaults to `NULL`  
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
`animation_duration`| Animation duration. The duration of the animation for each dot or axis, in seconds. The animation can be seen between slides in a Flourish story. Flourish type hint: number, defaults to `NULL`  
`animation_stagger`| Animation stagger. The delay between each dot starting to move, in seconds; set to 0 to have all dots move simultaneously. Flourish type hint: number, defaults to `NULL`  
`line_animate_in`| Animate new lines in. Whether new lines should appear whole or be animated into view. Flourish type hint: boolean, defaults to `NULL`  
`line_animate_out`| Animate exiting lines. Whether filtered/removed lines should be removed whole or animated out of view. Flourish type hint: boolean, defaults to `NULL`  
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
