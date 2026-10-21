---
url: https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/
title: Set bubble chart chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:15.023215+00:00
---

# Set bubble chart chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set bubble chart chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_bubble_chart_details(
    
        self,
    
        bubble_alignment: str = None,
    
        margin_bubbles: float = None,
    
        animation_duration: float = None,
    
        height_mode: str = None,
    
        aspect_ratio: float = None,
    
        aspect_ratio_mobile: float = None,
    
        aspect_ratio_breakpoint: float = None,
    
        circle_background_color: str = None,
    
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
    
        circle_background_border: float = None,
    
        image_opacity: float = None,
    
        label_font_weight: str = None,
    
        label_font_style: str = None,
    
        label_font_case: str = None,
    
        label_font_color: str = None,
    
        label_shadow: bool = None,
    
        enable_highlighting: bool = None,
    
        selected_bubbles: Union[list, str] = None,
    
        opacity_highlighted: float = None,
    
        opacity_not_highlighted: float = None,
    
        highlight_pictures: bool = None,
    
        chart_legend_container_alignment: str = None,
    
        chart_legend_container_orientation: str = None,
    
        chart_legend_container_title_weight: str = None,
    
        chart_legend_container_text_weight: str = None,
    
        chart_legend_container_text_color: str = None,
    
        chart_legend_container_text_size: float = None,
    
        show_legend_axis: bool = None,
    
        axis_legend_title_mode: str = None,
    
        axis_legend_title: str = None,
    
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
    
        chart_size_legend_show_legend: bool = None,
    
        chart_size_legend_title_mode: str = None,
    
        chart_size_legend_title: str = None,
    
        chart_size_legend_shape_fill: str = None,
    
        chart_size_legend_shape_stroke: str = None,
    
        chart_size_legend_clip_height: float = None,
    
        chart_size_legend_small_symbol_size: float = None,
    
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
    
    
    set_bubble_chart_details(
    
        .,
    
        bubble_alignment = NULL,
    
        margin_bubbles = NULL,
    
        animation_duration = NULL,
    
        height_mode = NULL,
    
        aspect_ratio = NULL,
    
        aspect_ratio_mobile = NULL,
    
        aspect_ratio_breakpoint = NULL,
    
        circle_background_color = NULL,
    
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
    
        circle_background_border = NULL,
    
        image_opacity = NULL,
    
        label_font_weight = NULL,
    
        label_font_style = NULL,
    
        label_font_case = NULL,
    
        label_font_color = NULL,
    
        label_shadow = NULL,
    
        enable_highlighting = NULL,
    
        selected_bubbles = NULL,
    
        opacity_highlighted = NULL,
    
        opacity_not_highlighted = NULL,
    
        highlight_pictures = NULL,
    
        chart_legend_container_alignment = NULL,
    
        chart_legend_container_orientation = NULL,
    
        chart_legend_container_title_weight = NULL,
    
        chart_legend_container_text_weight = NULL,
    
        chart_legend_container_text_color = NULL,
    
        chart_legend_container_text_size = NULL,
    
        show_legend_axis = NULL,
    
        axis_legend_title_mode = NULL,
    
        axis_legend_title = NULL,
    
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
    
        chart_size_legend_show_legend = NULL,
    
        chart_size_legend_title_mode = NULL,
    
        chart_size_legend_title = NULL,
    
        chart_size_legend_shape_fill = NULL,
    
        chart_size_legend_shape_stroke = NULL,
    
        chart_size_legend_clip_height = NULL,
    
        chart_size_legend_small_symbol_size = NULL,
    
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
`bubble_alignment`| `str`, optional| Alignment of bubbles. Choices: center, axis. Flourish type hint: string, defaults to None  
`margin_bubbles`| `float`, optional| Space between bubbles. Flourish type hint: number, defaults to None  
`animation_duration`| `float`, optional| Animation duration. in seconds. Flourish type hint: number, defaults to None  
`height_mode`| `str`, optional| Height mode. Choices: fill_space, aspect. Fill space: the graphic will fill the container (which by default will be the the standard Flourish responsive chart size) Aspect ratio: sets the aspect of the chart. This setting is ignored when embedded in a fixed-height context, such as a simple iframe embedFlourish type hint: string, defaults to None  
`aspect_ratio`| `float`, optional| Aspect (desktop). Height of the plot as a proportion of its width, between 0 and 1. Flourish type hint: number, defaults to None  
`aspect_ratio_mobile`| `float`, optional| Aspect (mobile). Height of the plot as a proportion of its width, between 0 and 1. Flourish type hint: number, defaults to None  
`aspect_ratio_breakpoint`| `float`, optional| Breakpoint. The width at which mobile mode ends and desktop begins. Flourish type hint: number, defaults to None  
`circle_background_color`| `str`, optional| Color. Default color. Flourish type hint: color, defaults to None  
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
`circle_background_border`| `float`, optional| Border. Flourish type hint: number, defaults to None  
`image_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`label_font_weight`| `str`, optional| Weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`label_font_style`| `str`, optional| Style. Choices: normal, italic. Flourish type hint: string, defaults to None  
`label_font_case`| `str`, optional| Case. Choices:, uppercase. Flourish type hint: string, defaults to None  
`label_font_color`| `str`, optional| Color. Defaults to contrast coloring when no image is set. Flourish type hint: color, defaults to None  
`label_shadow`| `bool`, optional| Text shadow. Flourish type hint: boolean, defaults to None  
`enable_highlighting`| `bool`, optional| Enable highlighting. Flourish type hint: boolean, defaults to None  
`selected_bubbles`| `Union[list, str]`, optional| Highlight bubbles. To highlight bubbles, write the name of each bubble on a new line. You can also create a story and highlight/unhighlight by clicking. Flourish type hint: text, defaults to None  
`opacity_highlighted`| `float`, optional| Opacity of highlighted bubble. Flourish type hint: number, defaults to None  
`opacity_not_highlighted`| `float`, optional| Opacity of all other bubbles. Flourish type hint: number, defaults to None  
`highlight_pictures`| `bool`, optional| Show pictures only on highlighted bubbles. Flourish type hint: boolean, defaults to None  
`chart_legend_container_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`chart_legend_container_orientation`| `str`, optional| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to None  
`chart_legend_container_title_weight`| `str`, optional| Title weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_legend_container_text_weight`| `str`, optional| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to None  
`chart_legend_container_text_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`chart_legend_container_text_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`show_legend_axis`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`axis_legend_title_mode`| `str`, optional| Title mode. Choices: auto, custom. Flourish type hint: string, defaults to None  
`axis_legend_title`| `str`, optional| Title. Flourish type hint: string, defaults to None  
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
`chart_size_legend_show_legend`| `bool`, optional| Choices: True, False. Flourish type hint: boolean, defaults to None  
`chart_size_legend_title_mode`| `str`, optional| Title mode. Choices: auto, custom. Flourish type hint: string, defaults to None  
`chart_size_legend_title`| `str`, optional| Title. Flourish type hint: string, defaults to None  
`chart_size_legend_shape_fill`| `str`, optional| Shape fill. Flourish type hint: color, defaults to None  
`chart_size_legend_shape_stroke`| `str`, optional| Shape stroke. Hint: set to same value as fill for no stroke. Flourish type hint: color, defaults to None  
`chart_size_legend_clip_height`| `float`, optional| Max height. Maximum height of shape ( relative to root font size ). Flourish type hint: number, defaults to None  
`chart_size_legend_small_symbol_size`| `float`, optional| Small/large proportion. Proportion of the smallest symbols value compared to the biggest symbols value. 0.5 means its half the value of the big symbol. Flourish type hint: number, defaults to None  
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
`bubble_alignment`| Alignment of bubbles. Choices: center, axis. Flourish type hint: string, defaults to `NULL`  
`margin_bubbles`| Space between bubbles. Flourish type hint: number, defaults to `NULL`  
`animation_duration`| Animation duration. in seconds. Flourish type hint: number, defaults to `NULL`  
`height_mode`| Height mode. Choices: fill_space, aspect. Fill space: the graphic will fill the container (which by default will be the the standard Flourish responsive chart size) Aspect ratio: sets the aspect of the chart. This setting is ignored when embedded in a fixed-height context, such as a simple iframe embedFlourish type hint: string, defaults to `NULL`  
`aspect_ratio`| Aspect (desktop). Height of the plot as a proportion of its width, between 0 and 1. Flourish type hint: number, defaults to `NULL`  
`aspect_ratio_mobile`| Aspect (mobile). Height of the plot as a proportion of its width, between 0 and 1. Flourish type hint: number, defaults to `NULL`  
`aspect_ratio_breakpoint`| Breakpoint. The width at which mobile mode ends and desktop begins. Flourish type hint: number, defaults to `NULL`  
`circle_background_color`| Color. Default color. Flourish type hint: color, defaults to `NULL`  
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
`circle_background_border`| Border. Flourish type hint: number, defaults to `NULL`  
`image_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`label_font_weight`| Weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`label_font_style`| Style. Choices: normal, italic. Flourish type hint: string, defaults to `NULL`  
`label_font_case`| Case. Choices:, uppercase. Flourish type hint: string, defaults to `NULL`  
`label_font_color`| Color. Defaults to contrast coloring when no image is set. Flourish type hint: color, defaults to `NULL`  
`label_shadow`| Text shadow. Flourish type hint: boolean, defaults to `NULL`  
`enable_highlighting`| Enable highlighting. Flourish type hint: boolean, defaults to `NULL`  
`selected_bubbles`| Highlight bubbles. To highlight bubbles, write the name of each bubble on a new line. You can also create a story and highlight/unhighlight by clicking. Flourish type hint: text, defaults to `NULL`  
`opacity_highlighted`| Opacity of highlighted bubble. Flourish type hint: number, defaults to `NULL`  
`opacity_not_highlighted`| Opacity of all other bubbles. Flourish type hint: number, defaults to `NULL`  
`highlight_pictures`| Show pictures only on highlighted bubbles. Flourish type hint: boolean, defaults to `NULL`  
`chart_legend_container_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_orientation`| Orientation. Choices: horizontal, vertical. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_title_weight`| Title weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_text_weight`| Text weight. Choices: bold, normal. Flourish type hint: string, defaults to `NULL`  
`chart_legend_container_text_color`| Color. Flourish type hint: color, defaults to `NULL`  
`chart_legend_container_text_size`| Size. Flourish type hint: number, defaults to `NULL`  
`show_legend_axis`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`axis_legend_title_mode`| Title mode. Choices: auto, custom. Flourish type hint: string, defaults to `NULL`  
`axis_legend_title`| Title. Flourish type hint: string, defaults to `NULL`  
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
`chart_size_legend_show_legend`| Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_size_legend_title_mode`| Title mode. Choices: auto, custom. Flourish type hint: string, defaults to `NULL`  
`chart_size_legend_title`| Title. Flourish type hint: string, defaults to `NULL`  
`chart_size_legend_shape_fill`| Shape fill. Flourish type hint: color, defaults to `NULL`  
`chart_size_legend_shape_stroke`| Shape stroke. Hint: set to same value as fill for no stroke. Flourish type hint: color, defaults to `NULL`  
`chart_size_legend_clip_height`| Max height. Maximum height of shape ( relative to root font size ). Flourish type hint: number, defaults to `NULL`  
`chart_size_legend_small_symbol_size`| Small/large proportion. Proportion of the smallest symbols value compared to the biggest symbols value. 0.5 means its half the value of the big symbol. Flourish type hint: number, defaults to `NULL`  
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
