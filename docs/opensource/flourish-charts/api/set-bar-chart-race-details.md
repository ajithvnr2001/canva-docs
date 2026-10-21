---
url: https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/
title: Set bar chart race chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:17.862803+00:00
---

# Set bar chart race chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set bar chart race chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_bar_chart_race_details(
    
        self,
    
        column_chart: bool = None,
    
        number_of_bars: float = None,
    
        bar_margin: float = None,
    
        sort_enabled: bool = None,
    
        sort_ascending: bool = None,
    
        bars_advanced: bool = None,
    
        height_mode: str = None,
    
        bar_height: float = None,
    
        bar_min_value: float = None,
    
        bar_empty_spaces: bool = None,
    
        color_mode: str = None,
    
        color_single: str = None,
    
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
    
        color_single_overrides: Union[list, str] = None,
    
        bar_opacity: float = None,
    
        label_max_size: float = None,
    
        label_mode: str = None,
    
        label_color_in: str = None,
    
        label_axis_width: float = None,
    
        show_value: bool = None,
    
        label_color_out: str = None,
    
        padding_right: float = None,
    
        image_height: float = None,
    
        image_width: float = None,
    
        image_margin_right: float = None,
    
        image_scale: str = None,
    
        image_circle: bool = None,
    
        counter: bool = None,
    
        counter_font_size: float = None,
    
        counter_color: str = None,
    
        counter_line_height: float = None,
    
        totaliser: bool = None,
    
        totaliser_font_size: float = None,
    
        totaliser_color: str = None,
    
        totaliser_label: str = None,
    
        caption_background_color: str = None,
    
        caption_border_color: str = None,
    
        caption_opacity: float = None,
    
        caption_padding: float = None,
    
        caption_text_align: str = None,
    
        caption_position: str = None,
    
        caption_font_size: float = None,
    
        caption_text_color: str = None,
    
        caption_mode: str = None,
    
        caption_image_width: float = None,
    
        caption_image_position: str = None,
    
        caption_space_between: float = None,
    
        sort_control: bool = None,
    
        sort_descending_text: str = None,
    
        sort_ascending_text: str = None,
    
        chart_controls_style_font_size: float = None,
    
        chart_controls_style_font_weight: str = None,
    
        chart_controls_style_height: float = None,
    
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
    
        text_legend: str = None,
    
        text_legend_title: bool = None,
    
        text_legend_subtitle: bool = None,
    
        text_legend_caption: bool = None,
    
        text_legend_bold: bool = None,
    
        axis_text_color: str = None,
    
        axis_font_size: float = None,
    
        axis_color: str = None,
    
        axis_gridline_dash: float = None,
    
        scale_type: str = None,
    
        scale_min: float = None,
    
        scale_max: float = None,
    
        annotations_enabled: bool = None,
    
        annotations_content: Union[list, str] = None,
    
        annotations_text_color: str = None,
    
        annotations_text_size: float = None,
    
        annotations_text_weight: str = None,
    
        annotations_line_color: str = None,
    
        annotations_line_opacity: float = None,
    
        annotations_line_width: float = None,
    
        annotations_line_dash: float = None,
    
        annotations_align: str = None,
    
        annotations_offset: str = None,
    
        chart_timeline_controls_enabled: bool = None,
    
        chart_timeline_controls_style: str = None,
    
        chart_timeline_controls_graph: bool = None,
    
        chart_timeline_controls_play_on_load: bool = None,
    
        chart_timeline_controls_loop: bool = None,
    
        chart_timeline_controls_duration: float = None,
    
        chart_timeline_controls_duration_tween: float = None,
    
        chart_timeline_controls_duration_wait_at_end: float = None,
    
        chart_timeline_controls_axes_custom_enabled: bool = None,
    
        chart_timeline_controls_color_axes: str = None,
    
        chart_timeline_controls_axis_font_size: float = None,
    
        chart_timeline_controls_date_format_display: str = None,
    
        chart_timeline_controls_axis_nice_x: bool = None,
    
        chart_timeline_controls_axis_nice_y: bool = None,
    
        chart_timeline_controls_scrubber_snap: bool = None,
    
        chart_timeline_controls_scrubber_snap_paused: bool = None,
    
        chart_timeline_controls_layout_settings: bool = None,
    
        chart_timeline_controls_margin_top: float = None,
    
        chart_timeline_controls_margin_left: float = None,
    
        chart_timeline_controls_margin_bottom: float = None,
    
        chart_timeline_controls_margin_right: float = None,
    
        chart_timeline_controls_playback_button_margin_right: float = None,
    
        chart_timeline_controls_scrubber_height: float = None,
    
        chart_timeline_controls_playback_button_margin_right_button: float = None,
    
        chart_timeline_controls_graph_settings: bool = None,
    
        chart_timeline_controls_color_background: str = None,
    
        chart_timeline_controls_graph_height: float = None,
    
        chart_timeline_controls_curve: bool = None,
    
        chart_timeline_controls_playback_styling: bool = None,
    
        chart_timeline_controls_playback_button_button_color: str = None,
    
        chart_timeline_controls_playback_button_button_size: float = None,
    
        chart_timeline_controls_playback_button_icon_color: str = None,
    
        chart_timeline_controls_playback_button_icon_size: float = None,
    
        chart_timeline_controls_playback_button_label_size: float = None,
    
        animation_duration: float = None,
    
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
    
        blank_cells: str = None,
    
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
    
    
    set_bar_chart_race_details(
    
        .,
    
        column_chart = NULL,
    
        number_of_bars = NULL,
    
        bar_margin = NULL,
    
        sort_enabled = NULL,
    
        sort_ascending = NULL,
    
        bars_advanced = NULL,
    
        height_mode = NULL,
    
        bar_height = NULL,
    
        bar_min_value = NULL,
    
        bar_empty_spaces = NULL,
    
        color_mode = NULL,
    
        color_single = NULL,
    
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
    
        color_single_overrides = NULL,
    
        bar_opacity = NULL,
    
        label_max_size = NULL,
    
        label_mode = NULL,
    
        label_color_in = NULL,
    
        label_axis_width = NULL,
    
        show_value = NULL,
    
        label_color_out = NULL,
    
        padding_right = NULL,
    
        image_height = NULL,
    
        image_width = NULL,
    
        image_margin_right = NULL,
    
        image_scale = NULL,
    
        image_circle = NULL,
    
        counter = NULL,
    
        counter_font_size = NULL,
    
        counter_color = NULL,
    
        counter_line_height = NULL,
    
        totaliser = NULL,
    
        totaliser_font_size = NULL,
    
        totaliser_color = NULL,
    
        totaliser_label = NULL,
    
        caption_background_color = NULL,
    
        caption_border_color = NULL,
    
        caption_opacity = NULL,
    
        caption_padding = NULL,
    
        caption_text_align = NULL,
    
        caption_position = NULL,
    
        caption_font_size = NULL,
    
        caption_text_color = NULL,
    
        caption_mode = NULL,
    
        caption_image_width = NULL,
    
        caption_image_position = NULL,
    
        caption_space_between = NULL,
    
        sort_control = NULL,
    
        sort_descending_text = NULL,
    
        sort_ascending_text = NULL,
    
        chart_controls_style_font_size = NULL,
    
        chart_controls_style_font_weight = NULL,
    
        chart_controls_style_height = NULL,
    
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
    
        text_legend = NULL,
    
        text_legend_title = NULL,
    
        text_legend_subtitle = NULL,
    
        text_legend_caption = NULL,
    
        text_legend_bold = NULL,
    
        axis_text_color = NULL,
    
        axis_font_size = NULL,
    
        axis_color = NULL,
    
        axis_gridline_dash = NULL,
    
        scale_type = NULL,
    
        scale_min = NULL,
    
        scale_max = NULL,
    
        annotations_enabled = NULL,
    
        annotations_content = NULL,
    
        annotations_text_color = NULL,
    
        annotations_text_size = NULL,
    
        annotations_text_weight = NULL,
    
        annotations_line_color = NULL,
    
        annotations_line_opacity = NULL,
    
        annotations_line_width = NULL,
    
        annotations_line_dash = NULL,
    
        annotations_align = NULL,
    
        annotations_offset = NULL,
    
        chart_timeline_controls_enabled = NULL,
    
        chart_timeline_controls_style = NULL,
    
        chart_timeline_controls_graph = NULL,
    
        chart_timeline_controls_play_on_load = NULL,
    
        chart_timeline_controls_loop = NULL,
    
        chart_timeline_controls_duration = NULL,
    
        chart_timeline_controls_duration_tween = NULL,
    
        chart_timeline_controls_duration_wait_at_end = NULL,
    
        chart_timeline_controls_axes_custom_enabled = NULL,
    
        chart_timeline_controls_color_axes = NULL,
    
        chart_timeline_controls_axis_font_size = NULL,
    
        chart_timeline_controls_date_format_display = NULL,
    
        chart_timeline_controls_axis_nice_x = NULL,
    
        chart_timeline_controls_axis_nice_y = NULL,
    
        chart_timeline_controls_scrubber_snap = NULL,
    
        chart_timeline_controls_scrubber_snap_paused = NULL,
    
        chart_timeline_controls_layout_settings = NULL,
    
        chart_timeline_controls_margin_top = NULL,
    
        chart_timeline_controls_margin_left = NULL,
    
        chart_timeline_controls_margin_bottom = NULL,
    
        chart_timeline_controls_margin_right = NULL,
    
        chart_timeline_controls_playback_button_margin_right = NULL,
    
        chart_timeline_controls_scrubber_height = NULL,
    
        chart_timeline_controls_playback_button_margin_right_button = NULL,
    
        chart_timeline_controls_graph_settings = NULL,
    
        chart_timeline_controls_color_background = NULL,
    
        chart_timeline_controls_graph_height = NULL,
    
        chart_timeline_controls_curve = NULL,
    
        chart_timeline_controls_playback_styling = NULL,
    
        chart_timeline_controls_playback_button_button_color = NULL,
    
        chart_timeline_controls_playback_button_button_size = NULL,
    
        chart_timeline_controls_playback_button_icon_color = NULL,
    
        chart_timeline_controls_playback_button_icon_size = NULL,
    
        chart_timeline_controls_playback_button_label_size = NULL,
    
        animation_duration = NULL,
    
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
    
        blank_cells = NULL,
    
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
`column_chart`| `bool`, optional| Chart style. Choices: False, True. Flourish type hint: boolean, defaults to None  
`number_of_bars`| `float`, optional| No. bars. Flourish type hint: number, defaults to None  
`bar_margin`| `float`, optional| Spacing (Percentage). Spacing as a percentage of bar width. For example at "50" the bar height will equal bar spacing. Flourish type hint: number, defaults to None  
`sort_enabled`| `bool`, optional| Sorting. Choices: True, False. Flourish type hint: boolean, defaults to None  
`sort_ascending`| `bool`, optional| Sort mode. Choices: False, True. Flourish type hint: boolean, defaults to None  
`bars_advanced`| `bool`, optional| Show advanced. Flourish type hint: boolean, defaults to None  
`height_mode`| `str`, optional| Bar height. Choices: fill_space, specified. Flourish type hint: string, defaults to None  
`bar_height`| `float`, optional| Height. Height of the bar; expressed as a multiple of the base font size to make it responsive. Flourish type hint: number, defaults to None  
`bar_min_value`| `float`, optional| Hide bars below value. This will hide all bars that have a value below the number specified in this setting. Flourish type hint: number, defaults to None  
`bar_empty_spaces`| `bool`, optional| When not enough bars. Choices: True, False. If enabled, the chart and bars will remain the same size as more bars enter the race. Flourish type hint: boolean, defaults to None  
`color_mode`| `str`, optional| Color mode. Choices: category, bar, single. Whether to color by category (if you have a category column set in the datasheet), by each individual bar, or give every bar the same color. Flourish type hint: string, defaults to None  
`color_single`| `str`, optional| Single color. Flourish type hint: color, defaults to None  
`chart_color_scale_categorical_palette`| `Union[list, str]`, optional| Palette. Flourish type hint: colors, defaults to None  
`chart_color_scale_categorical_extend`| `bool`, optional| Extend. Automatically generate additional colours when needed to avoid the palette colours being used more than once. Flourish type hint: boolean, defaults to None  
`chart_color_scale_categorical_custom_palette`| `Union[list, str]`, optional| Color overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to None  
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
`color_single_overrides`| `Union[list, str]`, optional| Color overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to None  
`bar_opacity`| `float`, optional| Bar opacity. Flourish type hint: number, defaults to None  
`label_max_size`| `float`, optional| Max size. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`label_mode`| `str`, optional| Labels mode. Choices: bars, axis. Flourish type hint: string, defaults to None  
`label_color_in`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`label_axis_width`| `float`, optional| Space. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`show_value`| `bool`, optional| Show values. Flourish type hint: boolean, defaults to None  
`label_color_out`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`padding_right`| `float`, optional| Space. Flourish type hint: number, defaults to None  
`image_height`| `float`, optional| Height. As a percentage of bar height. Flourish type hint: number, defaults to None  
`image_width`| `float`, optional| Width. As a percentage of bar height. Flourish type hint: number, defaults to None  
`image_margin_right`| `float`, optional| Margin right. As a percentage of bar height. Use a negative value to get images to show to the right of the barFlourish type hint: number, defaults to None  
`image_scale`| `str`, optional| Image sizing. Choices: fill, fit, stretch. Flourish type hint: string, defaults to None  
`image_circle`| `bool`, optional| Shape. Choices: False, True. Flourish type hint: boolean, defaults to None  
`counter`| `bool`, optional| Show current time. Flourish type hint: boolean, defaults to None  
`counter_font_size`| `float`, optional| Size (percentage of screen). Flourish type hint: number, defaults to None  
`counter_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`counter_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`totaliser`| `bool`, optional| Show total. Shows the sum of all the values in the datasheet for the current time, including any bars not currently visible in the chart. Flourish type hint: boolean, defaults to None  
`totaliser_font_size`| `float`, optional| Size (percentage of screen). Flourish type hint: number, defaults to None  
`totaliser_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`totaliser_label`| `str`, optional| Label. Flourish type hint: string, defaults to None  
`caption_background_color`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`caption_border_color`| `str`, optional| Border. Flourish type hint: color, defaults to None  
`caption_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`caption_padding`| `float`, optional| Padding. In rems multiples of the base font size. Flourish type hint: number, defaults to None  
`caption_text_align`| `str`, optional| Align. Choices: flex-start, center, flex-end. Flourish type hint: string, defaults to None  
`caption_position`| `str`, optional| Position. Choices: top-left, center-left, bottom-left, top-right, center-right, bottom-right, top-center, center-center, bottom-center. Flourish type hint: string, defaults to None  
`caption_font_size`| `float`, optional| Font size. In rems multiples of the base font size. Flourish type hint: number, defaults to None  
`caption_text_color`| `str`, optional| Text. Flourish type hint: color, defaults to None  
`caption_mode`| `str`, optional| Content mode. Choices: text_legend, html. In Text with colors mode, any phrases matching category names will be automatically colored. In HTML mode, no colors will be applied, but you can include any HTML in the datasheet to add images, etc. Flourish type hint: string, defaults to None  
`caption_image_width`| `float`, optional| Width. As a percentage of the caption container width. Flourish type hint: number, defaults to None  
`caption_image_position`| `str`, optional| Position. Choices: column, column-reverse, row, row-reverse. Flourish type hint: string, defaults to None  
`caption_space_between`| `float`, optional| Space between. Space between the image and text in rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`sort_control`| `bool`, optional| Show sort control. Flourish type hint: boolean, defaults to None  
`sort_descending_text`| `str`, optional| “Highest” label. Flourish type hint: string, defaults to None  
`sort_ascending_text`| `str`, optional| “Lowest” label. Flourish type hint: string, defaults to None  
`chart_controls_style_font_size`| `float`, optional| Text size. Flourish type hint: number, defaults to None  
`chart_controls_style_font_weight`| `str`, optional| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_controls_style_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
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
`text_legend`| `str`, optional| Choices: auto, custom, off. Flourish type hint: string, defaults to None  
`text_legend_title`| `bool`, optional| Title. Flourish type hint: boolean, defaults to None  
`text_legend_subtitle`| `bool`, optional| Subtitle. Flourish type hint: boolean, defaults to None  
`text_legend_caption`| `bool`, optional| Captions. Flourish type hint: boolean, defaults to None  
`text_legend_bold`| `bool`, optional| Bold. If checked, always use bold for colored items. Flourish type hint: boolean, defaults to None  
`axis_text_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`axis_font_size`| `float`, optional| Text size. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`axis_color`| `str`, optional| Line color. Flourish type hint: color, defaults to None  
`axis_gridline_dash`| `float`, optional| Line dash. Flourish type hint: number, defaults to None  
`scale_type`| `str`, optional| Type. Choices: auto, auto_fixed, manual. The dynamic scale type sets a dynamix X axis that will animate with the chart. The fixed or custom scale type sets a fixed maximum value on the X axis. Flourish type hint: string, defaults to None  
`scale_min`| `float`, optional| Min range. The axis will go from zero to this value, then be dynamic. Flourish type hint: number, defaults to None  
`scale_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`annotations_enabled`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`annotations_content`| `Union[list, str]`, optional| Annotations. One line per annotation. Syntax Annotation text :: Value on X axis Example Winner :: 250 Majority :: 200. Flourish type hint: text, defaults to None  
`annotations_text_color`| `str`, optional| Text color. Flourish type hint: color, defaults to None  
`annotations_text_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`annotations_text_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`annotations_line_color`| `str`, optional| Line color. Flourish type hint: color, defaults to None  
`annotations_line_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`annotations_line_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`annotations_line_dash`| `float`, optional| Dash. Flourish type hint: number, defaults to None  
`annotations_align`| `str`, optional| Align. Choices: start, middle, end. Flourish type hint: string, defaults to None  
`annotations_offset`| `str`, optional| Offset. Choices: above, on, below. Offset text mode. Flourish type hint: string, defaults to None  
`chart_timeline_controls_enabled`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_style`| `str`, optional| Style. Choices: timeline, button. Flourish type hint: string, defaults to None  
`chart_timeline_controls_graph`| `bool`, optional| Show chart. Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_play_on_load`| `bool`, optional| Play on load. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_loop`| `bool`, optional| Loop timeline. When turned on, the timeline will return to the beginning once complete. Otherwise, it will stop when it reaches the end. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_duration`| `float`, optional| Timeline duration. Total duration of the timeline during normal playback in seconds. Flourish type hint: number, defaults to None  
`chart_timeline_controls_duration_tween`| `float`, optional| Time jump duration. Duration of transitions between different points in time on the timeline. This is the transition you see in the story player when switching between slides with a different time on the timeline (in seconds). Flourish type hint: number, defaults to None  
`chart_timeline_controls_duration_wait_at_end`| `float`, optional| Pause before loop. Flourish type hint: number, defaults to None  
`chart_timeline_controls_axes_custom_enabled`| `bool`, optional| Axis settings. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_color_axes`| `str`, optional| Axes color. Flourish type hint: color, defaults to None  
`chart_timeline_controls_axis_font_size`| `float`, optional| Font size. Flourish type hint: number, defaults to None  
`chart_timeline_controls_date_format_display`| `str`, optional| X axis date format. Choices:, %Y-%m-%dT%H:%M:%S.%LZ, %Y-%m-%d, %m/%d/%Y, %d/%m/%Y, %d-%b-%y, %m/%Y, %b %Y, %b %y, %B %d, %d %b, %Y, %B, %b, %A, %a, %H:%M:%S, %I:%M %p, %H:%M. Flourish type hint: string, defaults to None  
`chart_timeline_controls_axis_nice_x`| `bool`, optional| Clean X axis. Rounds out the X axis so that its start and end values are nice, round dates. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_axis_nice_y`| `bool`, optional| Clean Y axis. Rounds out the Y axis so that its start and end values are nice, round numbers. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_scrubber_snap`| `bool`, optional| Snap when scrubbing. When turned on, you can only jump to values that are supplied in the dataset and nothing in between. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_scrubber_snap_paused`| `bool`, optional| Snap when paused. Activate to snap the timeline to the closest interval when non animating. This is useful for ensuring the data visible in the visualization always reflects the data you have supplied. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_layout_settings`| `bool`, optional| Layout settings. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_margin_top`| `float`, optional| Top. Flourish type hint: number, defaults to None  
`chart_timeline_controls_margin_left`| `float`, optional| Left. Flourish type hint: number, defaults to None  
`chart_timeline_controls_margin_bottom`| `float`, optional| Bottom. Flourish type hint: number, defaults to None  
`chart_timeline_controls_margin_right`| `float`, optional| Right. Flourish type hint: number, defaults to None  
`chart_timeline_controls_playback_button_margin_right`| `float`, optional| Space between button and timeline. Flourish type hint: number, defaults to None  
`chart_timeline_controls_scrubber_height`| `float`, optional| Scrubber height. Flourish type hint: number, defaults to None  
`chart_timeline_controls_playback_button_margin_right_button`| `float`, optional| Space between button and text. Flourish type hint: number, defaults to None  
`chart_timeline_controls_graph_settings`| `bool`, optional| Chart settings. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_color_background`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`chart_timeline_controls_graph_height`| `float`, optional| Height. Flourish type hint: number, defaults to None  
`chart_timeline_controls_curve`| `bool`, optional| Curved lines. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_playback_styling`| `bool`, optional| Play button settings. Flourish type hint: boolean, defaults to None  
`chart_timeline_controls_playback_button_button_color`| `str`, optional| Button color. Flourish type hint: color, defaults to None  
`chart_timeline_controls_playback_button_button_size`| `float`, optional| Button size. Flourish type hint: number, defaults to None  
`chart_timeline_controls_playback_button_icon_color`| `str`, optional| Icon color. Flourish type hint: color, defaults to None  
`chart_timeline_controls_playback_button_icon_size`| `float`, optional| Icon size. Flourish type hint: number, defaults to None  
`chart_timeline_controls_playback_button_label_size`| `float`, optional| Label size. Flourish type hint: number, defaults to None  
`animation_duration`| `float`, optional| Bar swap duration. Animation duration of the bars swapping, in seconds. Flourish type hint: number, defaults to None  
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
`blank_cells`| `str`, optional| How to handle blank/invalid cells. Choices: interpolate, last_valid, zero, remove. Interpolate fills the gaps between the last and next valid values. Use last valid will use the last number for the bar. Treat as zero will set the value of the blank cell to zero. Remove bar will remove the bar for any blank/invalid cells. Flourish type hint: string, defaults to None  
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
`column_chart`| Chart style. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`number_of_bars`| No. bars. Flourish type hint: number, defaults to `NULL`  
`bar_margin`| Spacing (Percentage). Spacing as a percentage of bar width. For example at "50" the bar height will equal bar spacing. Flourish type hint: number, defaults to `NULL`  
`sort_enabled`| Sorting. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`sort_ascending`| Sort mode. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`bars_advanced`| Show advanced. Flourish type hint: boolean, defaults to `NULL`  
`height_mode`| Bar height. Choices: fill_space, specified. Flourish type hint: string, defaults to `NULL`  
`bar_height`| Height. Height of the bar; expressed as a multiple of the base font size to make it responsive. Flourish type hint: number, defaults to `NULL`  
`bar_min_value`| Hide bars below value. This will hide all bars that have a value below the number specified in this setting. Flourish type hint: number, defaults to `NULL`  
`bar_empty_spaces`| When not enough bars. Choices: `TRUE`, `FALSE`. If enabled, the chart and bars will remain the same size as more bars enter the race. Flourish type hint: boolean, defaults to `NULL`  
`color_mode`| Color mode. Choices: category, bar, single. Whether to color by category (if you have a category column set in the datasheet), by each individual bar, or give every bar the same color. Flourish type hint: string, defaults to `NULL`  
`color_single`| Single color. Flourish type hint: color, defaults to `NULL`  
`chart_color_scale_categorical_palette`| Palette. Flourish type hint: colors, defaults to `NULL`  
`chart_color_scale_categorical_extend`| Extend. Automatically generate additional colours when needed to avoid the palette colours being used more than once. Flourish type hint: boolean, defaults to `NULL`  
`chart_color_scale_categorical_custom_palette`| Color overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to `NULL`  
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
`color_single_overrides`| Color overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to `NULL`  
`bar_opacity`| Bar opacity. Flourish type hint: number, defaults to `NULL`  
`label_max_size`| Max size. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`label_mode`| Labels mode. Choices: bars, axis. Flourish type hint: string, defaults to `NULL`  
`label_color_in`| Color. Flourish type hint: color, defaults to `NULL`  
`label_axis_width`| Space. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`show_value`| Show values. Flourish type hint: boolean, defaults to `NULL`  
`label_color_out`| Color. Flourish type hint: color, defaults to `NULL`  
`padding_right`| Space. Flourish type hint: number, defaults to `NULL`  
`image_height`| Height. As a percentage of bar height. Flourish type hint: number, defaults to `NULL`  
`image_width`| Width. As a percentage of bar height. Flourish type hint: number, defaults to `NULL`  
`image_margin_right`| Margin right. As a percentage of bar height. Use a negative value to get images to show to the right of the barFlourish type hint: number, defaults to `NULL`  
`image_scale`| Image sizing. Choices: fill, fit, stretch. Flourish type hint: string, defaults to `NULL`  
`image_circle`| Shape. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`counter`| Show current time. Flourish type hint: boolean, defaults to `NULL`  
`counter_font_size`| Size (percentage of screen). Flourish type hint: number, defaults to `NULL`  
`counter_color`| Color. Flourish type hint: color, defaults to `NULL`  
`counter_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`totaliser`| Show total. Shows the sum of all the values in the datasheet for the current time, including any bars not currently visible in the chart. Flourish type hint: boolean, defaults to `NULL`  
`totaliser_font_size`| Size (percentage of screen). Flourish type hint: number, defaults to `NULL`  
`totaliser_color`| Color. Flourish type hint: color, defaults to `NULL`  
`totaliser_label`| Label. Flourish type hint: string, defaults to `NULL`  
`caption_background_color`| Background. Flourish type hint: color, defaults to `NULL`  
`caption_border_color`| Border. Flourish type hint: color, defaults to `NULL`  
`caption_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`caption_padding`| Padding. In rems multiples of the base font size. Flourish type hint: number, defaults to `NULL`  
`caption_text_align`| Align. Choices: flex-start, center, flex-end. Flourish type hint: string, defaults to `NULL`  
`caption_position`| Position. Choices: top-left, center-left, bottom-left, top-right, center-right, bottom-right, top-center, center-center, bottom-center. Flourish type hint: string, defaults to `NULL`  
`caption_font_size`| Font size. In rems multiples of the base font size. Flourish type hint: number, defaults to `NULL`  
`caption_text_color`| Text. Flourish type hint: color, defaults to `NULL`  
`caption_mode`| Content mode. Choices: text_legend, html. In Text with colors mode, any phrases matching category names will be automatically colored. In HTML mode, no colors will be applied, but you can include any HTML in the datasheet to add images, etc. Flourish type hint: string, defaults to `NULL`  
`caption_image_width`| Width. As a percentage of the caption container width. Flourish type hint: number, defaults to `NULL`  
`caption_image_position`| Position. Choices: column, column-reverse, row, row-reverse. Flourish type hint: string, defaults to `NULL`  
`caption_space_between`| Space between. Space between the image and text in rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`sort_control`| Show sort control. Flourish type hint: boolean, defaults to `NULL`  
`sort_descending_text`| “Highest” label. Flourish type hint: string, defaults to `NULL`  
`sort_ascending_text`| “Lowest” label. Flourish type hint: string, defaults to `NULL`  
`chart_controls_style_font_size`| Text size. Flourish type hint: number, defaults to `NULL`  
`chart_controls_style_font_weight`| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_controls_style_height`| Height. Flourish type hint: number, defaults to `NULL`  
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
`text_legend`| Choices: auto, custom, off. Flourish type hint: string, defaults to `NULL`  
`text_legend_title`| Title. Flourish type hint: boolean, defaults to `NULL`  
`text_legend_subtitle`| Subtitle. Flourish type hint: boolean, defaults to `NULL`  
`text_legend_caption`| Captions. Flourish type hint: boolean, defaults to `NULL`  
`text_legend_bold`| Bold. If checked, always use bold for colored items. Flourish type hint: boolean, defaults to `NULL`  
`axis_text_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`axis_font_size`| Text size. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`axis_color`| Line color. Flourish type hint: color, defaults to `NULL`  
`axis_gridline_dash`| Line dash. Flourish type hint: number, defaults to `NULL`  
`scale_type`| Type. Choices: auto, auto_fixed, manual. The dynamic scale type sets a dynamix X axis that will animate with the chart. The fixed or custom scale type sets a fixed maximum value on the X axis. Flourish type hint: string, defaults to `NULL`  
`scale_min`| Min range. The axis will go from zero to this value, then be dynamic. Flourish type hint: number, defaults to `NULL`  
`scale_max`| Max. Flourish type hint: number, defaults to `NULL`  
`annotations_enabled`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`annotations_content`| Annotations. One line per annotation. Syntax Annotation text :: Value on X axis Example Winner :: 250 Majority :: 200. Flourish type hint: text, defaults to `NULL`  
`annotations_text_color`| Text color. Flourish type hint: color, defaults to `NULL`  
`annotations_text_size`| Size. Flourish type hint: number, defaults to `NULL`  
`annotations_text_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`annotations_line_color`| Line color. Flourish type hint: color, defaults to `NULL`  
`annotations_line_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`annotations_line_width`| Width. Flourish type hint: number, defaults to `NULL`  
`annotations_line_dash`| Dash. Flourish type hint: number, defaults to `NULL`  
`annotations_align`| Align. Choices: start, middle, end. Flourish type hint: string, defaults to `NULL`  
`annotations_offset`| Offset. Choices: above, on, below. Offset text mode. Flourish type hint: string, defaults to `NULL`  
`chart_timeline_controls_enabled`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_style`| Style. Choices: timeline, button. Flourish type hint: string, defaults to `NULL`  
`chart_timeline_controls_graph`| Show chart. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_play_on_load`| Play on load. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_loop`| Loop timeline. When turned on, the timeline will return to the beginning once complete. Otherwise, it will stop when it reaches the end. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_duration`| Timeline duration. Total duration of the timeline during normal playback in seconds. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_duration_tween`| Time jump duration. Duration of transitions between different points in time on the timeline. This is the transition you see in the story player when switching between slides with a different time on the timeline (in seconds). Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_duration_wait_at_end`| Pause before loop. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_axes_custom_enabled`| Axis settings. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_color_axes`| Axes color. Flourish type hint: color, defaults to `NULL`  
`chart_timeline_controls_axis_font_size`| Font size. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_date_format_display`| X axis date format. Choices:, %Y-%m-%dT%H:%M:%S.%LZ, %Y-%m-%d, %m/%d/%Y, %d/%m/%Y, %d-%b-%y, %m/%Y, %b %Y, %b %y, %B %d, %d %b, %Y, %B, %b, %A, %a, %H:%M:%S, %I:%M %p, %H:%M. Flourish type hint: string, defaults to `NULL`  
`chart_timeline_controls_axis_nice_x`| Clean X axis. Rounds out the X axis so that its start and end values are nice, round dates. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_axis_nice_y`| Clean Y axis. Rounds out the Y axis so that its start and end values are nice, round numbers. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_scrubber_snap`| Snap when scrubbing. When turned on, you can only jump to values that are supplied in the dataset and nothing in between. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_scrubber_snap_paused`| Snap when paused. Activate to snap the timeline to the closest interval when non animating. This is useful for ensuring the data visible in the visualization always reflects the data you have supplied. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_layout_settings`| Layout settings. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_margin_top`| Top. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_margin_left`| Left. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_margin_bottom`| Bottom. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_margin_right`| Right. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_playback_button_margin_right`| Space between button and timeline. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_scrubber_height`| Scrubber height. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_playback_button_margin_right_button`| Space between button and text. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_graph_settings`| Chart settings. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_color_background`| Background. Flourish type hint: color, defaults to `NULL`  
`chart_timeline_controls_graph_height`| Height. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_curve`| Curved lines. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_playback_styling`| Play button settings. Flourish type hint: boolean, defaults to `NULL`  
`chart_timeline_controls_playback_button_button_color`| Button color. Flourish type hint: color, defaults to `NULL`  
`chart_timeline_controls_playback_button_button_size`| Button size. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_playback_button_icon_color`| Icon color. Flourish type hint: color, defaults to `NULL`  
`chart_timeline_controls_playback_button_icon_size`| Icon size. Flourish type hint: number, defaults to `NULL`  
`chart_timeline_controls_playback_button_label_size`| Label size. Flourish type hint: number, defaults to `NULL`  
`animation_duration`| Bar swap duration. Animation duration of the bars swapping, in seconds. Flourish type hint: number, defaults to `NULL`  
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
`blank_cells`| How to handle blank/invalid cells. Choices: interpolate, last_valid, zero, remove. Interpolate fills the gaps between the last and next valid values. Use last valid will use the last number for the bar. Treat as zero will set the value of the blank cell to zero. Remove bar will remove the bar for any blank/invalid cells. Flourish type hint: string, defaults to `NULL`  
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
