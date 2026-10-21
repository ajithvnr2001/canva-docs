---
url: https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/
title: Set timeline chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:56.226514+00:00
---

# Set timeline chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set timeline chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_timeline_details(
    
        self,
    
        widescreen_orientation: str = None,
    
        height_mode: str = None,
    
        facet_aspect: str = None,
    
        facet_aspect_custom: float = None,
    
        facet_aspect_breakpoint: float = None,
    
        facet_aspect_mobile: str = None,
    
        facet_aspect_mobile_custom: float = None,
    
        line_color: str = None,
    
        line_width: float = None,
    
        line_cap: str = None,
    
        events_scale_type: str = None,
    
        background_opacity: float = None,
    
        background_sizing: str = None,
    
        background_zoom: float = None,
    
        background_gradient_size: float = None,
    
        background_gradient_opacity: float = None,
    
        background_gradient_blur: float = None,
    
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
    
        marker_size: float = None,
    
        marker_background_color: str = None,
    
        marker_background_color_custom: str = None,
    
        marker_border_width: float = None,
    
        marker_border_color: str = None,
    
        marker_border_color_custom: str = None,
    
        connector_size: float = None,
    
        connector_space: float = None,
    
        connector_color: str = None,
    
        connector_opacity: float = None,
    
        content_background_color: str = None,
    
        content_padding: float = None,
    
        content_space_between: float = None,
    
        content_consistent_size: bool = None,
    
        content_border_radius: float = None,
    
        individual_borders: bool = None,
    
        content_border_width: float = None,
    
        content_border_opacity: float = None,
    
        content_border_color: str = None,
    
        content_border_color_custom: str = None,
    
        content_border_top_width: float = None,
    
        content_border_top_opacity: float = None,
    
        content_border_top_color: str = None,
    
        content_border_top_color_custom: str = None,
    
        content_border_right_width: float = None,
    
        content_border_right_opacity: float = None,
    
        content_border_right_color: str = None,
    
        content_border_right_color_custom: str = None,
    
        content_border_bottom_width: float = None,
    
        content_border_bottom_opacity: float = None,
    
        content_border_bottom_color: str = None,
    
        content_border_bottom_color_custom: str = None,
    
        content_border_left_width: float = None,
    
        content_border_left_opacity: float = None,
    
        content_border_left_color: str = None,
    
        content_border_left_color_custom: str = None,
    
        content_title_alignment: str = None,
    
        content_title_styling: bool = None,
    
        content_title_line_height: float = None,
    
        content_title_size: str = None,
    
        content_title_size_custom: float = None,
    
        content_title_weight: str = None,
    
        content_title_color: str = None,
    
        content_title_color_custom: str = None,
    
        content_title_space_above: str = None,
    
        content_title_space_above_custom: float = None,
    
        content_subtitle_alignment: str = None,
    
        content_subtitle_styling: bool = None,
    
        content_subtitle_line_height: float = None,
    
        content_subtitle_size: str = None,
    
        content_subtitle_size_custom: float = None,
    
        content_subtitle_weight: str = None,
    
        content_subtitle_color: str = None,
    
        content_subtitle_color_custom: str = None,
    
        content_subtitle_space_above: str = None,
    
        content_subtitle_space_above_custom: float = None,
    
        content_text_alignment: str = None,
    
        content_text_styling: bool = None,
    
        content_text_line_height: float = None,
    
        content_text_size: str = None,
    
        content_text_size_custom: float = None,
    
        content_text_weight: str = None,
    
        content_text_color: str = None,
    
        content_text_color_custom: str = None,
    
        content_text_space_above: str = None,
    
        content_text_space_above_custom: float = None,
    
        link_weight: str = None,
    
        link_color: str = None,
    
        link_underline: bool = None,
    
        image_location: str = None,
    
        image_opacity: float = None,
    
        image_display: str = None,
    
        image_sizing: str = None,
    
        image_zoom: float = None,
    
        image_content_sizing: str = None,
    
        image_content_zoom: float = None,
    
        image_float_position: str = None,
    
        image_inline_position: str = None,
    
        image_alignment: str = None,
    
        content_banner_depth: str = None,
    
        content_banner_depth_custom: float = None,
    
        image_width: float = None,
    
        image_margin: float = None,
    
        image_aspect: float = None,
    
        navigation_step_type: str = None,
    
        navigation_screen_proportion: float = None,
    
        navigation_event_number: float = None,
    
        navigation_icon_type: str = None,
    
        navigation_icon_size: float = None,
    
        navigation_icon_opacity: float = None,
    
        navigation_icon_custom: str = None,
    
        navigation_icon_color: str = None,
    
        navigation_gradient_color: str = None,
    
        navigation_gradient_width: float = None,
    
        navigation_gradient_opacity: float = None,
    
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
    
    
    set_timeline_details(
    
        .,
    
        widescreen_orientation = NULL,
    
        height_mode = NULL,
    
        facet_aspect = NULL,
    
        facet_aspect_custom = NULL,
    
        facet_aspect_breakpoint = NULL,
    
        facet_aspect_mobile = NULL,
    
        facet_aspect_mobile_custom = NULL,
    
        line_color = NULL,
    
        line_width = NULL,
    
        line_cap = NULL,
    
        events_scale_type = NULL,
    
        background_opacity = NULL,
    
        background_sizing = NULL,
    
        background_zoom = NULL,
    
        background_gradient_size = NULL,
    
        background_gradient_opacity = NULL,
    
        background_gradient_blur = NULL,
    
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
    
        marker_size = NULL,
    
        marker_background_color = NULL,
    
        marker_background_color_custom = NULL,
    
        marker_border_width = NULL,
    
        marker_border_color = NULL,
    
        marker_border_color_custom = NULL,
    
        connector_size = NULL,
    
        connector_space = NULL,
    
        connector_color = NULL,
    
        connector_opacity = NULL,
    
        content_background_color = NULL,
    
        content_padding = NULL,
    
        content_space_between = NULL,
    
        content_consistent_size = NULL,
    
        content_border_radius = NULL,
    
        individual_borders = NULL,
    
        content_border_width = NULL,
    
        content_border_opacity = NULL,
    
        content_border_color = NULL,
    
        content_border_color_custom = NULL,
    
        content_border_top_width = NULL,
    
        content_border_top_opacity = NULL,
    
        content_border_top_color = NULL,
    
        content_border_top_color_custom = NULL,
    
        content_border_right_width = NULL,
    
        content_border_right_opacity = NULL,
    
        content_border_right_color = NULL,
    
        content_border_right_color_custom = NULL,
    
        content_border_bottom_width = NULL,
    
        content_border_bottom_opacity = NULL,
    
        content_border_bottom_color = NULL,
    
        content_border_bottom_color_custom = NULL,
    
        content_border_left_width = NULL,
    
        content_border_left_opacity = NULL,
    
        content_border_left_color = NULL,
    
        content_border_left_color_custom = NULL,
    
        content_title_alignment = NULL,
    
        content_title_styling = NULL,
    
        content_title_line_height = NULL,
    
        content_title_size = NULL,
    
        content_title_size_custom = NULL,
    
        content_title_weight = NULL,
    
        content_title_color = NULL,
    
        content_title_color_custom = NULL,
    
        content_title_space_above = NULL,
    
        content_title_space_above_custom = NULL,
    
        content_subtitle_alignment = NULL,
    
        content_subtitle_styling = NULL,
    
        content_subtitle_line_height = NULL,
    
        content_subtitle_size = NULL,
    
        content_subtitle_size_custom = NULL,
    
        content_subtitle_weight = NULL,
    
        content_subtitle_color = NULL,
    
        content_subtitle_color_custom = NULL,
    
        content_subtitle_space_above = NULL,
    
        content_subtitle_space_above_custom = NULL,
    
        content_text_alignment = NULL,
    
        content_text_styling = NULL,
    
        content_text_line_height = NULL,
    
        content_text_size = NULL,
    
        content_text_size_custom = NULL,
    
        content_text_weight = NULL,
    
        content_text_color = NULL,
    
        content_text_color_custom = NULL,
    
        content_text_space_above = NULL,
    
        content_text_space_above_custom = NULL,
    
        link_weight = NULL,
    
        link_color = NULL,
    
        link_underline = NULL,
    
        image_location = NULL,
    
        image_opacity = NULL,
    
        image_display = NULL,
    
        image_sizing = NULL,
    
        image_zoom = NULL,
    
        image_content_sizing = NULL,
    
        image_content_zoom = NULL,
    
        image_float_position = NULL,
    
        image_inline_position = NULL,
    
        image_alignment = NULL,
    
        content_banner_depth = NULL,
    
        content_banner_depth_custom = NULL,
    
        image_width = NULL,
    
        image_margin = NULL,
    
        image_aspect = NULL,
    
        navigation_step_type = NULL,
    
        navigation_screen_proportion = NULL,
    
        navigation_event_number = NULL,
    
        navigation_icon_type = NULL,
    
        navigation_icon_size = NULL,
    
        navigation_icon_opacity = NULL,
    
        navigation_icon_custom = NULL,
    
        navigation_icon_color = NULL,
    
        navigation_gradient_color = NULL,
    
        navigation_gradient_width = NULL,
    
        navigation_gradient_opacity = NULL,
    
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
`widescreen_orientation`| `str`, optional| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to None  
`height_mode`| `str`, optional| Height mode. Choices: auto, standard, aspect. Auto: sets the height based on the chart type, data and width. Standard: uses the default Flourish responsive sizing. Aspect ratio: sets the aspect of each plot. This setting is ignored when embedded in a fixed-height context, such as a simple iframe embedFlourish type hint: string, defaults to None  
`facet_aspect`| `str`, optional| Desktop aspect. Choices: 0.75, 1, 1.5, custom. Aspect ratio of the visualization in desktop mode. Flourish type hint: string, defaults to None  
`facet_aspect_custom`| `float`, optional| Custom. 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to None  
`facet_aspect_breakpoint`| `float`, optional| Breakpoint. The width at which mobile mode ends and desktop begins. Flourish type hint: number, defaults to None  
`facet_aspect_mobile`| `str`, optional| Mobile aspect. Choices: 0.75, 1, 1.5, custom. Flourish type hint: string, defaults to None  
`facet_aspect_mobile_custom`| `float`, optional| Custom. 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to None  
`line_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`line_width`| `float`, optional| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`line_cap`| `str`, optional| Cap. Choices: butt, round, square. The shape used to draw the end points. Flourish type hint: string, defaults to None  
`events_scale_type`| `str`, optional| Choices: linear, timescale. Flourish type hint: string, defaults to None  
`background_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`background_sizing`| `str`, optional| Sizing. Choices: contain, cover, zoom. Flourish type hint: string, defaults to None  
`background_zoom`| `float`, optional| Zoom. Sets what size the image should fill the container as a percentage of the container size. Flourish type hint: number, defaults to None  
`background_gradient_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`background_gradient_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`background_gradient_blur`| `float`, optional| Blur. Flourish type hint: number, defaults to None  
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
`marker_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`marker_background_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`marker_background_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`marker_border_width`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`marker_border_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`marker_border_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`connector_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`connector_space`| `float`, optional| Space. Sets the area around the markers to keep clear of content containers. Flourish type hint: number, defaults to None  
`connector_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`connector_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`content_background_color`| `str`, optional| Background. Flourish type hint: color, defaults to None  
`content_padding`| `float`, optional| Padding. Flourish type hint: number, defaults to None  
`content_space_between`| `float`, optional| Space between. Defines the minimum amount of space between each content container. Flourish type hint: number, defaults to None  
`content_consistent_size`| `bool`, optional| Keep sizes consistent. Flourish type hint: boolean, defaults to None  
`content_border_radius`| `float`, optional| Radius. Flourish type hint: number, defaults to None  
`individual_borders`| `bool`, optional| Style borders individually. Flourish type hint: boolean, defaults to None  
`content_border_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`content_border_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`content_border_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`content_border_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`content_border_top_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`content_border_top_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`content_border_top_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`content_border_top_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`content_border_right_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`content_border_right_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`content_border_right_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`content_border_right_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`content_border_bottom_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`content_border_bottom_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`content_border_bottom_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`content_border_bottom_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`content_border_left_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`content_border_left_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`content_border_left_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`content_border_left_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`content_title_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`content_title_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`content_title_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`content_title_size`| `str`, optional| Size. Choices: 1.0, 1.2, custom. Flourish type hint: string, defaults to None  
`content_title_size_custom`| `float`, optional| Custom. Specify a custom responsive font size. Best results will be with values between 0.8 and 3. Flourish type hint: number, defaults to None  
`content_title_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`content_title_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`content_title_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`content_title_space_above`| `str`, optional| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to None  
`content_title_space_above_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`content_subtitle_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`content_subtitle_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`content_subtitle_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`content_subtitle_size`| `str`, optional| Size. Choices: 1.0, 1.2, custom. Flourish type hint: string, defaults to None  
`content_subtitle_size_custom`| `float`, optional| Custom. Specify a custom responsive font size. Best results will be with values between 0.8 and 3. Flourish type hint: number, defaults to None  
`content_subtitle_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`content_subtitle_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`content_subtitle_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`content_subtitle_space_above`| `str`, optional| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to None  
`content_subtitle_space_above_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`content_text_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`content_text_styling`| `bool`, optional| Styling. Flourish type hint: boolean, defaults to None  
`content_text_line_height`| `float`, optional| Line height. Flourish type hint: number, defaults to None  
`content_text_size`| `str`, optional| Size. Choices: 1.0, 1.2, custom. Flourish type hint: string, defaults to None  
`content_text_size_custom`| `float`, optional| Custom. Specify a custom responsive font size. Best results will be with values between 0.8 and 3. Flourish type hint: number, defaults to None  
`content_text_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`content_text_color`| `str`, optional| Color. Choices: data, custom. Flourish type hint: string, defaults to None  
`content_text_color_custom`| `str`, optional| Flourish type hint: color, defaults to None  
`content_text_space_above`| `str`, optional| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to None  
`content_text_space_above_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`link_weight`| `str`, optional| Weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`link_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`link_underline`| `bool`, optional| Underline. Flourish type hint: boolean, defaults to None  
`image_location`| `str`, optional| Location. Choices: none, marker, content. Flourish type hint: string, defaults to None  
`image_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`image_display`| `str`, optional| Content display. Choices: float, inline, banner, background. Flourish type hint: string, defaults to None  
`image_sizing`| `str`, optional| Sizing. Choices: contain, cover, zoom. Flourish type hint: string, defaults to None  
`image_zoom`| `float`, optional| Zoom. Sets what size the image should fill the container as a percentage of the container size. Flourish type hint: number, defaults to None  
`image_content_sizing`| `str`, optional| Sizing. Choices: contain, cover, zoom. Flourish type hint: string, defaults to None  
`image_content_zoom`| `float`, optional| Zoom. Sets what size the image should fill the container as a percentage of the container size. Flourish type hint: number, defaults to None  
`image_float_position`| `str`, optional| Position. Choices: 1, 2. Flourish type hint: string, defaults to None  
`image_inline_position`| `str`, optional| Position. Choices: 1, 2, 3. Flourish type hint: string, defaults to None  
`image_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`content_banner_depth`| `str`, optional| Banner depth. Choices: 2, 4, 6, custom. Flourish type hint: string, defaults to None  
`content_banner_depth_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`image_width`| `float`, optional| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to None  
`image_margin`| `float`, optional| Margin. Flourish type hint: number, defaults to None  
`image_aspect`| `float`, optional| Aspect ratio. As a multiplier of the images width. For example: a value of 2, means the image height is 2 times the image width. Flourish type hint: number, defaults to None  
`navigation_step_type`| `str`, optional| Step by. Choices: screen, event. Determines by which measure the timeline is approximately moved each time the navigation buttons are clicked. Flourish type hint: string, defaults to None  
`navigation_screen_proportion`| `float`, optional| Proportion. Flourish type hint: number, defaults to None  
`navigation_event_number`| `float`, optional| Number. Flourish type hint: number, defaults to None  
`navigation_icon_type`| `str`, optional| Icon. Choices: default, custom. Flourish type hint: string, defaults to None  
`navigation_icon_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`navigation_icon_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`navigation_icon_custom`| `str`, optional| Custom icon. Flourish type hint: url, defaults to None  
`navigation_icon_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`navigation_gradient_color`| `str`, optional| Color. If undefined the color will default to the background of the visualization. Flourish type hint: color, defaults to None  
`navigation_gradient_width`| `float`, optional| Width. Flourish type hint: number, defaults to None  
`navigation_gradient_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`chart_x_axis_axis_position`| `str`, optional| Position. Choices: bottom, top, hidden. Flourish type hint: string, defaults to None  
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
`widescreen_orientation`| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to `NULL`  
`height_mode`| Height mode. Choices: auto, standard, aspect. Auto: sets the height based on the chart type, data and width. Standard: uses the default Flourish responsive sizing. Aspect ratio: sets the aspect of each plot. This setting is ignored when embedded in a fixed-height context, such as a simple iframe embedFlourish type hint: string, defaults to `NULL`  
`facet_aspect`| Desktop aspect. Choices: 0.75, 1, 1.5, custom. Aspect ratio of the visualization in desktop mode. Flourish type hint: string, defaults to `NULL`  
`facet_aspect_custom`| Custom. 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to `NULL`  
`facet_aspect_breakpoint`| Breakpoint. The width at which mobile mode ends and desktop begins. Flourish type hint: number, defaults to `NULL`  
`facet_aspect_mobile`| Mobile aspect. Choices: 0.75, 1, 1.5, custom. Flourish type hint: string, defaults to `NULL`  
`facet_aspect_mobile_custom`| Custom. 1 is square, above 1 is wider, and below 1 is taller. Flourish type hint: number, defaults to `NULL`  
`line_color`| Color. Flourish type hint: color, defaults to `NULL`  
`line_width`| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`line_cap`| Cap. Choices: butt, round, square. The shape used to draw the end points. Flourish type hint: string, defaults to `NULL`  
`events_scale_type`| Choices: linear, timescale. Flourish type hint: string, defaults to `NULL`  
`background_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`background_sizing`| Sizing. Choices: contain, cover, zoom. Flourish type hint: string, defaults to `NULL`  
`background_zoom`| Zoom. Sets what size the image should fill the container as a percentage of the container size. Flourish type hint: number, defaults to `NULL`  
`background_gradient_size`| Size. Flourish type hint: number, defaults to `NULL`  
`background_gradient_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`background_gradient_blur`| Blur. Flourish type hint: number, defaults to `NULL`  
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
`marker_size`| Size. Flourish type hint: number, defaults to `NULL`  
`marker_background_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`marker_background_color_custom`| Flourish type hint: color, defaults to `NULL`  
`marker_border_width`| Size. Flourish type hint: number, defaults to `NULL`  
`marker_border_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`marker_border_color_custom`| Flourish type hint: color, defaults to `NULL`  
`connector_size`| Size. Flourish type hint: number, defaults to `NULL`  
`connector_space`| Space. Sets the area around the markers to keep clear of content containers. Flourish type hint: number, defaults to `NULL`  
`connector_color`| Color. Flourish type hint: color, defaults to `NULL`  
`connector_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`content_background_color`| Background. Flourish type hint: color, defaults to `NULL`  
`content_padding`| Padding. Flourish type hint: number, defaults to `NULL`  
`content_space_between`| Space between. Defines the minimum amount of space between each content container. Flourish type hint: number, defaults to `NULL`  
`content_consistent_size`| Keep sizes consistent. Flourish type hint: boolean, defaults to `NULL`  
`content_border_radius`| Radius. Flourish type hint: number, defaults to `NULL`  
`individual_borders`| Style borders individually. Flourish type hint: boolean, defaults to `NULL`  
`content_border_width`| Width. Flourish type hint: number, defaults to `NULL`  
`content_border_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`content_border_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`content_border_color_custom`| Flourish type hint: color, defaults to `NULL`  
`content_border_top_width`| Width. Flourish type hint: number, defaults to `NULL`  
`content_border_top_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`content_border_top_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`content_border_top_color_custom`| Flourish type hint: color, defaults to `NULL`  
`content_border_right_width`| Width. Flourish type hint: number, defaults to `NULL`  
`content_border_right_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`content_border_right_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`content_border_right_color_custom`| Flourish type hint: color, defaults to `NULL`  
`content_border_bottom_width`| Width. Flourish type hint: number, defaults to `NULL`  
`content_border_bottom_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`content_border_bottom_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`content_border_bottom_color_custom`| Flourish type hint: color, defaults to `NULL`  
`content_border_left_width`| Width. Flourish type hint: number, defaults to `NULL`  
`content_border_left_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`content_border_left_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`content_border_left_color_custom`| Flourish type hint: color, defaults to `NULL`  
`content_title_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`content_title_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`content_title_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`content_title_size`| Size. Choices: 1.0, 1.2, custom. Flourish type hint: string, defaults to `NULL`  
`content_title_size_custom`| Custom. Specify a custom responsive font size. Best results will be with values between 0.8 and 3. Flourish type hint: number, defaults to `NULL`  
`content_title_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`content_title_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`content_title_color_custom`| Flourish type hint: color, defaults to `NULL`  
`content_title_space_above`| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to `NULL`  
`content_title_space_above_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`content_subtitle_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`content_subtitle_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`content_subtitle_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`content_subtitle_size`| Size. Choices: 1.0, 1.2, custom. Flourish type hint: string, defaults to `NULL`  
`content_subtitle_size_custom`| Custom. Specify a custom responsive font size. Best results will be with values between 0.8 and 3. Flourish type hint: number, defaults to `NULL`  
`content_subtitle_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`content_subtitle_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`content_subtitle_color_custom`| Flourish type hint: color, defaults to `NULL`  
`content_subtitle_space_above`| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to `NULL`  
`content_subtitle_space_above_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`content_text_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`content_text_styling`| Styling. Flourish type hint: boolean, defaults to `NULL`  
`content_text_line_height`| Line height. Flourish type hint: number, defaults to `NULL`  
`content_text_size`| Size. Choices: 1.0, 1.2, custom. Flourish type hint: string, defaults to `NULL`  
`content_text_size_custom`| Custom. Specify a custom responsive font size. Best results will be with values between 0.8 and 3. Flourish type hint: number, defaults to `NULL`  
`content_text_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`content_text_color`| Color. Choices: data, custom. Flourish type hint: string, defaults to `NULL`  
`content_text_color_custom`| Flourish type hint: color, defaults to `NULL`  
`content_text_space_above`| Space above. Choices: 0, 0.5, 1, custom. Flourish type hint: string, defaults to `NULL`  
`content_text_space_above_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`link_weight`| Weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`link_color`| Color. Flourish type hint: color, defaults to `NULL`  
`link_underline`| Underline. Flourish type hint: boolean, defaults to `NULL`  
`image_location`| Location. Choices: none, marker, content. Flourish type hint: string, defaults to `NULL`  
`image_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`image_display`| Content display. Choices: float, inline, banner, background. Flourish type hint: string, defaults to `NULL`  
`image_sizing`| Sizing. Choices: contain, cover, zoom. Flourish type hint: string, defaults to `NULL`  
`image_zoom`| Zoom. Sets what size the image should fill the container as a percentage of the container size. Flourish type hint: number, defaults to `NULL`  
`image_content_sizing`| Sizing. Choices: contain, cover, zoom. Flourish type hint: string, defaults to `NULL`  
`image_content_zoom`| Zoom. Sets what size the image should fill the container as a percentage of the container size. Flourish type hint: number, defaults to `NULL`  
`image_float_position`| Position. Choices: 1, 2. Flourish type hint: string, defaults to `NULL`  
`image_inline_position`| Position. Choices: 1, 2, 3. Flourish type hint: string, defaults to `NULL`  
`image_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`content_banner_depth`| Banner depth. Choices: 2, 4, 6, custom. Flourish type hint: string, defaults to `NULL`  
`content_banner_depth_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`image_width`| Width. In rems, a multiple of the pages base font size. Flourish type hint: number, defaults to `NULL`  
`image_margin`| Margin. Flourish type hint: number, defaults to `NULL`  
`image_aspect`| Aspect ratio. As a multiplier of the images width. For example: a value of 2, means the image height is 2 times the image width. Flourish type hint: number, defaults to `NULL`  
`navigation_step_type`| Step by. Choices: screen, event. Determines by which measure the timeline is approximately moved each time the navigation buttons are clicked. Flourish type hint: string, defaults to `NULL`  
`navigation_screen_proportion`| Proportion. Flourish type hint: number, defaults to `NULL`  
`navigation_event_number`| Number. Flourish type hint: number, defaults to `NULL`  
`navigation_icon_type`| Icon. Choices: default, custom. Flourish type hint: string, defaults to `NULL`  
`navigation_icon_size`| Size. Flourish type hint: number, defaults to `NULL`  
`navigation_icon_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`navigation_icon_custom`| Custom icon. Flourish type hint: url, defaults to `NULL`  
`navigation_icon_color`| Color. Flourish type hint: color, defaults to `NULL`  
`navigation_gradient_color`| Color. If undefined the color will default to the background of the visualization. Flourish type hint: color, defaults to `NULL`  
`navigation_gradient_width`| Width. Flourish type hint: number, defaults to `NULL`  
`navigation_gradient_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`chart_x_axis_axis_position`| Position. Choices: bottom, top, hidden. Flourish type hint: string, defaults to `NULL`  
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
