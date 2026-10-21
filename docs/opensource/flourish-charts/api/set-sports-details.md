---
url: https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/
title: Set sports chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:49.287117+00:00
---

# Set sports chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set sports chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_sports_details(
    
        self,
    
        positions_type: str = None,
    
        positions_scale_custom: str = None,
    
        positions_x_min: float = None,
    
        positions_x_max: float = None,
    
        positions_y_min: float = None,
    
        positions_y_max: float = None,
    
        formation_type: str = None,
    
        formation: str = None,
    
        formation_custom: Union[list, str] = None,
    
        pitch_margin_top: float = None,
    
        pitch_margin_bottom: float = None,
    
        pitch_type: str = None,
    
        pitch_type_custom: str = None,
    
        pitch_type_upload: str = None,
    
        pitch_type_svg: Union[list, str] = None,
    
        pitch_line_color: str = None,
    
        pitch_line_opacity: float = None,
    
        pitch_line_width: float = None,
    
        pitch_height: float = None,
    
        pitch_background: str = None,
    
        pitch_opacity: float = None,
    
        pitch_orientation: str = None,
    
        pitch_crop: str = None,
    
        pitch_crop_custom: float = None,
    
        pitch_flip_dots: bool = None,
    
        pitch_flip_pitch: bool = None,
    
        colors_categorical_palette: Union[list, str] = None,
    
        colors_categorical_extend: bool = None,
    
        colors_categorical_custom_palette: Union[list, str] = None,
    
        colors_numeric_type: str = None,
    
        colors_binning: bool = None,
    
        colors_bin_mode: str = None,
    
        colors_bin_count: float = None,
    
        colors_bin_thresholds: str = None,
    
        colors_sequential_palette: str = None,
    
        colors_sequential_reverse: bool = None,
    
        colors_sequential_custom_min: str = None,
    
        colors_sequential_custom_max: str = None,
    
        colors_sequential_color_space: str = None,
    
        colors_sequential_custom_domain: bool = None,
    
        colors_sequential_domain_min: float = None,
    
        colors_sequential_domain_max: float = None,
    
        colors_diverging_palette: str = None,
    
        colors_diverging_reverse: bool = None,
    
        colors_diverging_custom_min: str = None,
    
        colors_diverging_custom_mid: str = None,
    
        colors_diverging_custom_max: str = None,
    
        colors_diverging_color_space: str = None,
    
        colors_diverging_custom_domain: bool = None,
    
        colors_diverging_domain_min: float = None,
    
        colors_diverging_domain_mid: float = None,
    
        colors_diverging_domain_max: float = None,
    
        dot_opacity: float = None,
    
        dot_size: str = None,
    
        dot_size_custom: float = None,
    
        dot_border: str = None,
    
        dot_border_custom: float = None,
    
        dot_border_color: str = None,
    
        label_mode: bool = None,
    
        label_color: str = None,
    
        label_weight: str = None,
    
        label_size: str = None,
    
        label_size_custom: float = None,
    
        show_squad_numbers: bool = None,
    
        squad_number_size: str = None,
    
        squad_number_size_custom: float = None,
    
        squad_number_weight: str = None,
    
        squad_number_color: str = None,
    
        squad_number_vertical_adjust: float = None,
    
        image_contrast: float = None,
    
        image_brightness: float = None,
    
        image_saturation: float = None,
    
        image_blend_mode: str = None,
    
        animation_target: str = None,
    
        animation_duration: float = None,
    
        trail: bool = None,
    
        trail_color: str = None,
    
        trail_opacity: float = None,
    
        trail_size: str = None,
    
        trail_size_custom: float = None,
    
        trail_style: str = None,
    
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
    
        chart_filter_controls_container_alignment: str = None,
    
        chart_filter_controls_container_controls_spacing: float = None,
    
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
    
        filter_include_all: bool = None,
    
        filter_all_label: str = None,
    
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
    
    
    set_sports_details(
    
        .,
    
        positions_type = NULL,
    
        positions_scale_custom = NULL,
    
        positions_x_min = NULL,
    
        positions_x_max = NULL,
    
        positions_y_min = NULL,
    
        positions_y_max = NULL,
    
        formation_type = NULL,
    
        formation = NULL,
    
        formation_custom = NULL,
    
        pitch_margin_top = NULL,
    
        pitch_margin_bottom = NULL,
    
        pitch_type = NULL,
    
        pitch_type_custom = NULL,
    
        pitch_type_upload = NULL,
    
        pitch_type_svg = NULL,
    
        pitch_line_color = NULL,
    
        pitch_line_opacity = NULL,
    
        pitch_line_width = NULL,
    
        pitch_height = NULL,
    
        pitch_background = NULL,
    
        pitch_opacity = NULL,
    
        pitch_orientation = NULL,
    
        pitch_crop = NULL,
    
        pitch_crop_custom = NULL,
    
        pitch_flip_dots = NULL,
    
        pitch_flip_pitch = NULL,
    
        colors_categorical_palette = NULL,
    
        colors_categorical_extend = NULL,
    
        colors_categorical_custom_palette = NULL,
    
        colors_numeric_type = NULL,
    
        colors_binning = NULL,
    
        colors_bin_mode = NULL,
    
        colors_bin_count = NULL,
    
        colors_bin_thresholds = NULL,
    
        colors_sequential_palette = NULL,
    
        colors_sequential_reverse = NULL,
    
        colors_sequential_custom_min = NULL,
    
        colors_sequential_custom_max = NULL,
    
        colors_sequential_color_space = NULL,
    
        colors_sequential_custom_domain = NULL,
    
        colors_sequential_domain_min = NULL,
    
        colors_sequential_domain_max = NULL,
    
        colors_diverging_palette = NULL,
    
        colors_diverging_reverse = NULL,
    
        colors_diverging_custom_min = NULL,
    
        colors_diverging_custom_mid = NULL,
    
        colors_diverging_custom_max = NULL,
    
        colors_diverging_color_space = NULL,
    
        colors_diverging_custom_domain = NULL,
    
        colors_diverging_domain_min = NULL,
    
        colors_diverging_domain_mid = NULL,
    
        colors_diverging_domain_max = NULL,
    
        dot_opacity = NULL,
    
        dot_size = NULL,
    
        dot_size_custom = NULL,
    
        dot_border = NULL,
    
        dot_border_custom = NULL,
    
        dot_border_color = NULL,
    
        label_mode = NULL,
    
        label_color = NULL,
    
        label_weight = NULL,
    
        label_size = NULL,
    
        label_size_custom = NULL,
    
        show_squad_numbers = NULL,
    
        squad_number_size = NULL,
    
        squad_number_size_custom = NULL,
    
        squad_number_weight = NULL,
    
        squad_number_color = NULL,
    
        squad_number_vertical_adjust = NULL,
    
        image_contrast = NULL,
    
        image_brightness = NULL,
    
        image_saturation = NULL,
    
        image_blend_mode = NULL,
    
        animation_target = NULL,
    
        animation_duration = NULL,
    
        trail = NULL,
    
        trail_color = NULL,
    
        trail_opacity = NULL,
    
        trail_size = NULL,
    
        trail_size_custom = NULL,
    
        trail_style = NULL,
    
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
    
        chart_filter_controls_container_alignment = NULL,
    
        chart_filter_controls_container_controls_spacing = NULL,
    
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
    
        filter_include_all = NULL,
    
        filter_all_label = NULL,
    
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
`positions_type`| `str`, optional| Position points by. Choices: auto, formation, data. Position points automatically based on your data, on a specific formation, or use X and Y coordinates. Flourish type hint: string, defaults to None  
`positions_scale_custom`| `str`, optional| Position scale. Choices: auto, custom. "Auto" will set the position scale based on the minimum and maximum values in your data. "Custom" allows you to set a custom minimum and maximum. Flourish type hint: string, defaults to None  
`positions_x_min`| `float`, optional| X min. Flourish type hint: number, defaults to None  
`positions_x_max`| `float`, optional| X max. Flourish type hint: number, defaults to None  
`positions_y_min`| `float`, optional| Y min. Flourish type hint: number, defaults to None  
`positions_y_max`| `float`, optional| Y max. Flourish type hint: number, defaults to None  
`formation_type`| `str`, optional| Formation type. Choices: preset, custom. Flourish type hint: string, defaults to None  
`formation`| `str`, optional| Formation. Choices: 3-5-2, 4-3-3, 4-3-2-1, 4-4-2, 3-4-3, 4-2-3-1. Flourish type hint: string, defaults to None  
`formation_custom`| `Union[list, str]`, optional| Custom formation. Use a "*"" for every player and a "-" for every space on the pitch. Flourish type hint: code, defaults to None  
`pitch_margin_top`| `float`, optional| Top. Increases the gap between the top of the pitch and the first dot. Flourish type hint: number, defaults to None  
`pitch_margin_bottom`| `float`, optional| Bottom. Increases the gap between the bottom of the pitch and the last dot. Flourish type hint: number, defaults to None  
`pitch_type`| `str`, optional| Sport. Choices: football, basketball, tennis, custom. Flourish type hint: string, defaults to None  
`pitch_type_custom`| `str`, optional| Choices: upload, svg. Flourish type hint: string, defaults to None  
`pitch_type_upload`| `str`, optional| Upload. Flourish type hint: url, defaults to None  
`pitch_type_svg`| `Union[list, str]`, optional| SVG. Flourish type hint: text, defaults to None  
`pitch_line_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`pitch_line_opacity`| `float`, optional| Opacity. Opacity of the pitch marking lines. Flourish type hint: number, defaults to None  
`pitch_line_width`| `float`, optional| Line width. Line width of the pitch markings in pixels. Flourish type hint: number, defaults to None  
`pitch_height`| `float`, optional| Pitch height. As a percentage of the width. Flourish type hint: number, defaults to None  
`pitch_background`| `str`, optional| Background color. Background color of the pitch. To change the color of the background outside of the pitch, instead slect Background color in the layout section. Flourish type hint: color, defaults to None  
`pitch_opacity`| `float`, optional| Background opacity. Opacity of the pitch background. Flourish type hint: number, defaults to None  
`pitch_orientation`| `str`, optional| Orientation. Choices: vertical, horizontal. Flourish type hint: string, defaults to None  
`pitch_crop`| `str`, optional| Crop pitch. Choices: 1, custom. Show the full pitch, or only show a portion. Flourish type hint: string, defaults to None  
`pitch_crop_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`pitch_flip_dots`| `bool`, optional| Flip dots. Choices: True, False. Flourish type hint: boolean, defaults to None  
`pitch_flip_pitch`| `bool`, optional| Flip pitch. Choices: True, False. Flourish type hint: boolean, defaults to None  
`colors_categorical_palette`| `Union[list, str]`, optional| Palette. Flourish type hint: colors, defaults to None  
`colors_categorical_extend`| `bool`, optional| Extend. Automatically generate additional colours when needed to avoid the palette colours being used more than once. Flourish type hint: boolean, defaults to None  
`colors_categorical_custom_palette`| `Union[list, str]`, optional| Custom overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to None  
`colors_numeric_type`| `str`, optional| Scale type. Choices: sequential, diverging. Flourish type hint: string, defaults to None  
`colors_binning`| `bool`, optional| Choices: False, True. In linear mode, the color scale will run as a smooth gradient between 2 colors. In binned mode, the gradient will be divided in smaller blocks. Flourish type hint: boolean, defaults to None  
`colors_bin_mode`| `str`, optional| Binning mode. Choices: fixed, quantile, custom. Flourish type hint: string, defaults to None  
`colors_bin_count`| `float`, optional| Number of bins. Flourish type hint: number, defaults to None  
`colors_bin_thresholds`| `str`, optional| Custom thresholds. Enter your desired thresholds, separating them with a ";". For instance, "5;10;15". Bins form as follows: From the datas minimum value (domain minimum) up to the first threshold. Between consecutive thresholds. From the last threshold to the datas maximum value (domain maximum). For "5;10;15", youll get four bins based on your datas range. Flourish type hint: string, defaults to None  
`colors_sequential_palette`| `str`, optional| Palette. Flourish type hint: string, defaults to None  
`colors_sequential_reverse`| `bool`, optional| Reverse. Flourish type hint: boolean, defaults to None  
`colors_sequential_custom_min`| `str`, optional| Minimum color. Flourish type hint: color, defaults to None  
`colors_sequential_custom_max`| `str`, optional| Maximum color. Flourish type hint: color, defaults to None  
`colors_sequential_color_space`| `str`, optional| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to None  
`colors_sequential_custom_domain`| `bool`, optional| Domain. Choices: False, True. Flourish type hint: boolean, defaults to None  
`colors_sequential_domain_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`colors_sequential_domain_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`colors_diverging_palette`| `str`, optional| Palette. Flourish type hint: string, defaults to None  
`colors_diverging_reverse`| `bool`, optional| Reverse. Flourish type hint: boolean, defaults to None  
`colors_diverging_custom_min`| `str`, optional| Minimum color. Flourish type hint: color, defaults to None  
`colors_diverging_custom_mid`| `str`, optional| Midpoint color. Flourish type hint: color, defaults to None  
`colors_diverging_custom_max`| `str`, optional| Maximum color. Flourish type hint: color, defaults to None  
`colors_diverging_color_space`| `str`, optional| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to None  
`colors_diverging_custom_domain`| `bool`, optional| Domain. Choices: False, True. Flourish type hint: boolean, defaults to None  
`colors_diverging_domain_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`colors_diverging_domain_mid`| `float`, optional| Mid. Flourish type hint: number, defaults to None  
`colors_diverging_domain_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`dot_opacity`| `float`, optional| Opacity. Opacity of the dots. Flourish type hint: number, defaults to None  
`dot_size`| `str`, optional| Size. Choices: 1.3, 2.5, 6, custom. Flourish type hint: string, defaults to None  
`dot_size_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`dot_border`| `str`, optional| Border size. Choices: 0, 0.2, 0.5, custom. Flourish type hint: string, defaults to None  
`dot_border_custom`| `float`, optional| Custom. Flourish type hint: number, defaults to None  
`dot_border_color`| `str`, optional| Color. Outline color of the dots. Flourish type hint: color, defaults to None  
`label_mode`| `bool`, optional| Labels. Choices: True, False. Labels will always be hidden if there are more than 200 data points. Flourish type hint: boolean, defaults to None  
`label_color`| `str`, optional| Color. Label color. Defaults to layout font color settings if not set. Flourish type hint: color, defaults to None  
`label_weight`| `str`, optional| Weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`label_size`| `str`, optional| Size. Choices: 0.8, 1, 1.2, custom. Sizing unit is relative to root font size. Flourish type hint: string, defaults to None  
`label_size_custom`| `float`, optional| Custom. Specify a custom responsive font size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to None  
`show_squad_numbers`| `bool`, optional| Show Squad Numbers. Optional squad number to appear within dot. Flourish type hint: boolean, defaults to None  
`squad_number_size`| `str`, optional| Size Mode. Choices: 1.1, 1.4, 1.7, custom. Resizes the font size as a proportion of the dots radius. Flourish type hint: string, defaults to None  
`squad_number_size_custom`| `float`, optional| Custom. Specify a custom responsive font size. Best results are betwen 0.8 and 2. Flourish type hint: number, defaults to None  
`squad_number_weight`| `str`, optional| Weight. Choices: normal, bold. Flourish type hint: string, defaults to None  
`squad_number_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`squad_number_vertical_adjust`| `float`, optional| Adjust vertical spacing. Adjust vertical centering for custom fonts. Flourish type hint: number, defaults to None  
`image_contrast`| `float`, optional| Contrast. Flourish type hint: number, defaults to None  
`image_brightness`| `float`, optional| Brightness. Flourish type hint: number, defaults to None  
`image_saturation`| `float`, optional| Saturation. Flourish type hint: number, defaults to None  
`image_blend_mode`| `str`, optional| Blend mode. Choices: normal, multiply, screen, overlay, darken, lighten. Flourish type hint: string, defaults to None  
`animation_target`| `str`, optional| Animate. Choices: position, opacity, both. Choose whether you want to animate the animate the positions or fade, for example when changing the filter, or drag players positions in the story editor. Flourish type hint: string, defaults to None  
`animation_duration`| `float`, optional| Duration. Specified in seconds. Flourish type hint: number, defaults to None  
`trail`| `bool`, optional| Trail lines. Choices: False, True. Show trail lines when a point is dragged to a new position. Only visible in the story editor. Flourish type hint: boolean, defaults to None  
`trail_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`trail_opacity`| `float`, optional| Opacity. Flourish type hint: number, defaults to None  
`trail_size`| `str`, optional| Size. Choices: 0.2, 0.5, custom. Flourish type hint: string, defaults to None  
`trail_size_custom`| `float`, optional| Custom. Proportional to the smallest point size. Flourish type hint: number, defaults to None  
`trail_style`| `str`, optional| Style. Choices: solid, dotted. Flourish type hint: string, defaults to None  
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
`chart_filter_controls_container_alignment`| `str`, optional| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to None  
`chart_filter_controls_container_controls_spacing`| `float`, optional| Spacing. The space between controls, like dropdowns and adjacent button sets, in em units. Flourish type hint: number, defaults to None  
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
`filter_include_all`| `bool`, optional| Include "all". Include "All" in the filter dropdown. Flourish type hint: boolean, defaults to None  
`filter_all_label`| `str`, optional| All label. Flourish type hint: string, defaults to None  
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
`positions_type`| Position points by. Choices: auto, formation, data. Position points automatically based on your data, on a specific formation, or use X and Y coordinates. Flourish type hint: string, defaults to `NULL`  
`positions_scale_custom`| Position scale. Choices: auto, custom. "Auto" will set the position scale based on the minimum and maximum values in your data. "Custom" allows you to set a custom minimum and maximum. Flourish type hint: string, defaults to `NULL`  
`positions_x_min`| X min. Flourish type hint: number, defaults to `NULL`  
`positions_x_max`| X max. Flourish type hint: number, defaults to `NULL`  
`positions_y_min`| Y min. Flourish type hint: number, defaults to `NULL`  
`positions_y_max`| Y max. Flourish type hint: number, defaults to `NULL`  
`formation_type`| Formation type. Choices: preset, custom. Flourish type hint: string, defaults to `NULL`  
`formation`| Formation. Choices: 3-5-2, 4-3-3, 4-3-2-1, 4-4-2, 3-4-3, 4-2-3-1. Flourish type hint: string, defaults to `NULL`  
`formation_custom`| Custom formation. Use a "*"" for every player and a "-" for every space on the pitch. Flourish type hint: code, defaults to `NULL`  
`pitch_margin_top`| Top. Increases the gap between the top of the pitch and the first dot. Flourish type hint: number, defaults to `NULL`  
`pitch_margin_bottom`| Bottom. Increases the gap between the bottom of the pitch and the last dot. Flourish type hint: number, defaults to `NULL`  
`pitch_type`| Sport. Choices: football, basketball, tennis, custom. Flourish type hint: string, defaults to `NULL`  
`pitch_type_custom`| Choices: upload, svg. Flourish type hint: string, defaults to `NULL`  
`pitch_type_upload`| Upload. Flourish type hint: url, defaults to `NULL`  
`pitch_type_svg`| SVG. Flourish type hint: text, defaults to `NULL`  
`pitch_line_color`| Color. Flourish type hint: color, defaults to `NULL`  
`pitch_line_opacity`| Opacity. Opacity of the pitch marking lines. Flourish type hint: number, defaults to `NULL`  
`pitch_line_width`| Line width. Line width of the pitch markings in pixels. Flourish type hint: number, defaults to `NULL`  
`pitch_height`| Pitch height. As a percentage of the width. Flourish type hint: number, defaults to `NULL`  
`pitch_background`| Background color. Background color of the pitch. To change the color of the background outside of the pitch, instead slect Background color in the layout section. Flourish type hint: color, defaults to `NULL`  
`pitch_opacity`| Background opacity. Opacity of the pitch background. Flourish type hint: number, defaults to `NULL`  
`pitch_orientation`| Orientation. Choices: vertical, horizontal. Flourish type hint: string, defaults to `NULL`  
`pitch_crop`| Crop pitch. Choices: 1, custom. Show the full pitch, or only show a portion. Flourish type hint: string, defaults to `NULL`  
`pitch_crop_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`pitch_flip_dots`| Flip dots. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`pitch_flip_pitch`| Flip pitch. Choices: `TRUE`, `FALSE`. Flourish type hint: boolean, defaults to `NULL`  
`colors_categorical_palette`| Palette. Flourish type hint: colors, defaults to `NULL`  
`colors_categorical_extend`| Extend. Automatically generate additional colours when needed to avoid the palette colours being used more than once. Flourish type hint: boolean, defaults to `NULL`  
`colors_categorical_custom_palette`| Custom overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to `NULL`  
`colors_numeric_type`| Scale type. Choices: sequential, diverging. Flourish type hint: string, defaults to `NULL`  
`colors_binning`| Choices: `FALSE`, `TRUE`. In linear mode, the color scale will run as a smooth gradient between 2 colors. In binned mode, the gradient will be divided in smaller blocks. Flourish type hint: boolean, defaults to `NULL`  
`colors_bin_mode`| Binning mode. Choices: fixed, quantile, custom. Flourish type hint: string, defaults to `NULL`  
`colors_bin_count`| Number of bins. Flourish type hint: number, defaults to `NULL`  
`colors_bin_thresholds`| Custom thresholds. Enter your desired thresholds, separating them with a ";". For instance, "5;10;15". Bins form as follows: From the datas minimum value (domain minimum) up to the first threshold. Between consecutive thresholds. From the last threshold to the datas maximum value (domain maximum). For "5;10;15", youll get four bins based on your datas range. Flourish type hint: string, defaults to `NULL`  
`colors_sequential_palette`| Palette. Flourish type hint: string, defaults to `NULL`  
`colors_sequential_reverse`| Reverse. Flourish type hint: boolean, defaults to `NULL`  
`colors_sequential_custom_min`| Minimum color. Flourish type hint: color, defaults to `NULL`  
`colors_sequential_custom_max`| Maximum color. Flourish type hint: color, defaults to `NULL`  
`colors_sequential_color_space`| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to `NULL`  
`colors_sequential_custom_domain`| Domain. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`colors_sequential_domain_min`| Min. Flourish type hint: number, defaults to `NULL`  
`colors_sequential_domain_max`| Max. Flourish type hint: number, defaults to `NULL`  
`colors_diverging_palette`| Palette. Flourish type hint: string, defaults to `NULL`  
`colors_diverging_reverse`| Reverse. Flourish type hint: boolean, defaults to `NULL`  
`colors_diverging_custom_min`| Minimum color. Flourish type hint: color, defaults to `NULL`  
`colors_diverging_custom_mid`| Midpoint color. Flourish type hint: color, defaults to `NULL`  
`colors_diverging_custom_max`| Maximum color. Flourish type hint: color, defaults to `NULL`  
`colors_diverging_color_space`| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to `NULL`  
`colors_diverging_custom_domain`| Domain. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`colors_diverging_domain_min`| Min. Flourish type hint: number, defaults to `NULL`  
`colors_diverging_domain_mid`| Mid. Flourish type hint: number, defaults to `NULL`  
`colors_diverging_domain_max`| Max. Flourish type hint: number, defaults to `NULL`  
`dot_opacity`| Opacity. Opacity of the dots. Flourish type hint: number, defaults to `NULL`  
`dot_size`| Size. Choices: 1.3, 2.5, 6, custom. Flourish type hint: string, defaults to `NULL`  
`dot_size_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`dot_border`| Border size. Choices: 0, 0.2, 0.5, custom. Flourish type hint: string, defaults to `NULL`  
`dot_border_custom`| Custom. Flourish type hint: number, defaults to `NULL`  
`dot_border_color`| Color. Outline color of the dots. Flourish type hint: color, defaults to `NULL`  
`label_mode`| Labels. Choices: `TRUE`, `FALSE`. Labels will always be hidden if there are more than 200 data points. Flourish type hint: boolean, defaults to `NULL`  
`label_color`| Color. Label color. Defaults to layout font color settings if not set. Flourish type hint: color, defaults to `NULL`  
`label_weight`| Weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`label_size`| Size. Choices: 0.8, 1, 1.2, custom. Sizing unit is relative to root font size. Flourish type hint: string, defaults to `NULL`  
`label_size_custom`| Custom. Specify a custom responsive font size. Best results will be with values between 1.2 and 3. Flourish type hint: number, defaults to `NULL`  
`show_squad_numbers`| Show Squad Numbers. Optional squad number to appear within dot. Flourish type hint: boolean, defaults to `NULL`  
`squad_number_size`| Size Mode. Choices: 1.1, 1.4, 1.7, custom. Resizes the font size as a proportion of the dots radius. Flourish type hint: string, defaults to `NULL`  
`squad_number_size_custom`| Custom. Specify a custom responsive font size. Best results are betwen 0.8 and 2. Flourish type hint: number, defaults to `NULL`  
`squad_number_weight`| Weight. Choices: normal, bold. Flourish type hint: string, defaults to `NULL`  
`squad_number_color`| Color. Flourish type hint: color, defaults to `NULL`  
`squad_number_vertical_adjust`| Adjust vertical spacing. Adjust vertical centering for custom fonts. Flourish type hint: number, defaults to `NULL`  
`image_contrast`| Contrast. Flourish type hint: number, defaults to `NULL`  
`image_brightness`| Brightness. Flourish type hint: number, defaults to `NULL`  
`image_saturation`| Saturation. Flourish type hint: number, defaults to `NULL`  
`image_blend_mode`| Blend mode. Choices: normal, multiply, screen, overlay, darken, lighten. Flourish type hint: string, defaults to `NULL`  
`animation_target`| Animate. Choices: position, opacity, both. Choose whether you want to animate the animate the positions or fade, for example when changing the filter, or drag players positions in the story editor. Flourish type hint: string, defaults to `NULL`  
`animation_duration`| Duration. Specified in seconds. Flourish type hint: number, defaults to `NULL`  
`trail`| Trail lines. Choices: `FALSE`, `TRUE`. Show trail lines when a point is dragged to a new position. Only visible in the story editor. Flourish type hint: boolean, defaults to `NULL`  
`trail_color`| Color. Flourish type hint: color, defaults to `NULL`  
`trail_opacity`| Opacity. Flourish type hint: number, defaults to `NULL`  
`trail_size`| Size. Choices: 0.2, 0.5, custom. Flourish type hint: string, defaults to `NULL`  
`trail_size_custom`| Custom. Proportional to the smallest point size. Flourish type hint: number, defaults to `NULL`  
`trail_style`| Style. Choices: solid, dotted. Flourish type hint: string, defaults to `NULL`  
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
`chart_filter_controls_container_alignment`| Alignment. Choices: start, center, end. Flourish type hint: string, defaults to `NULL`  
`chart_filter_controls_container_controls_spacing`| Spacing. The space between controls, like dropdowns and adjacent button sets, in em units. Flourish type hint: number, defaults to `NULL`  
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
`filter_include_all`| Include "all". Include "All" in the filter dropdown. Flourish type hint: boolean, defaults to `NULL`  
`filter_all_label`| All label. Flourish type hint: string, defaults to `NULL`  
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
