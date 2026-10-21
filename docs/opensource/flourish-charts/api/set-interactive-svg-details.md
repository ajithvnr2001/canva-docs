---
url: https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/
title: Set interactive svg chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:30.520408+00:00
---

# Set interactive svg chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set interactive svg chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_interactive_svg_details(
    
        self,
    
        svg_url: str = None,
    
        svg_width_wide: float = None,
    
        mobile_view: bool = None,
    
        mobile_breakpoint: float = None,
    
        mobile_svg_mode: str = None,
    
        mobile_svg_url: str = None,
    
        mobile_svg_width: float = None,
    
        mobile_content_mode: str = None,
    
        clickable_svg_animation: str = None,
    
        clickable_svg_animation_duration: float = None,
    
        clickable_svg_animation_config: bool = None,
    
        clickable_svg_animation_attr: str = None,
    
        clickable_svg_animation_values: str = None,
    
        clickable_svg_animation_repeat: str = None,
    
        text_panel_enabled: bool = None,
    
        h3_default: Union[list, str] = None,
    
        h3_size: float = None,
    
        h4_default: Union[list, str] = None,
    
        h4_size: float = None,
    
        content_default: Union[list, str] = None,
    
        content_size: float = None,
    
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
    
        svg_reset_fonts: bool = None,
    
        show_css: bool = None,
    
        stylesheet: Union[list, str] = None,
    
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
    
    
    set_interactive_svg_details(
    
        .,
    
        svg_url = NULL,
    
        svg_width_wide = NULL,
    
        mobile_view = NULL,
    
        mobile_breakpoint = NULL,
    
        mobile_svg_mode = NULL,
    
        mobile_svg_url = NULL,
    
        mobile_svg_width = NULL,
    
        mobile_content_mode = NULL,
    
        clickable_svg_animation = NULL,
    
        clickable_svg_animation_duration = NULL,
    
        clickable_svg_animation_config = NULL,
    
        clickable_svg_animation_attr = NULL,
    
        clickable_svg_animation_values = NULL,
    
        clickable_svg_animation_repeat = NULL,
    
        text_panel_enabled = NULL,
    
        h3_default = NULL,
    
        h3_size = NULL,
    
        h4_default = NULL,
    
        h4_size = NULL,
    
        content_default = NULL,
    
        content_size = NULL,
    
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
    
        svg_reset_fonts = NULL,
    
        show_css = NULL,
    
        stylesheet = NULL,
    
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
`svg_url`| `str`, optional| SVG file. Flourish type hint: url, defaults to None  
`svg_width_wide`| `float`, optional| Image width. The width in percentage of the image in standard wide-screen view. Flourish type hint: number, defaults to None  
`mobile_view`| `bool`, optional| Different mobile view. Flourish type hint: boolean, defaults to None  
`mobile_breakpoint`| `float`, optional| Breakpoint. The size in pixels at which to switch to mobile layout Flourish type hint: number, defaults to None  
`mobile_svg_mode`| `str`, optional| Image on mobile. Choices: none, same, different. Whether to show the image at all on mobile. Flourish type hint: string, defaults to None  
`mobile_svg_url`| `str`, optional| SVG file (mobile). Flourish type hint: url, defaults to None  
`mobile_svg_width`| `float`, optional| Width. The width in percentage of the image on a mobile view. Flourish type hint: number, defaults to None  
`mobile_content_mode`| `str`, optional| Mobile content mode. Choices: interactive, all, accordion. If turned on all content will display on load in mobile view. Flourish type hint: string, defaults to None  
`clickable_svg_animation`| `str`, optional| Animation clickable elements. Choices: off, animation. Flourish type hint: string, defaults to None  
`clickable_svg_animation_duration`| `float`, optional| Duration. The duration of the highlight animation on each clickable element. Flourish type hint: number, defaults to None  
`clickable_svg_animation_config`| `bool`, optional| Advanced. Reveal settings to adjust the SVG Animation properties on clickable elements. See Mozilla docs for more detailsFlourish type hint: boolean, defaults to None  
`clickable_svg_animation_attr`| `str`, optional| Attribute. Flourish type hint: string, defaults to None  
`clickable_svg_animation_values`| `str`, optional| Values. Flourish type hint: string, defaults to None  
`clickable_svg_animation_repeat`| `str`, optional| Repeat. Flourish type hint: string, defaults to None  
`text_panel_enabled`| `bool`, optional| Text panel enabled. Disable to only show text in popups. Flourish type hint: boolean, defaults to None  
`h3_default`| `Union[list, str]`, optional| Default heading. The text to show on load. Flourish type hint: text, defaults to None  
`h3_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`h4_default`| `Union[list, str]`, optional| Default subheading. The text to show on load. Flourish type hint: text, defaults to None  
`h4_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`content_default`| `Union[list, str]`, optional| Default text. The text to show on load. Flourish type hint: text, defaults to None  
`content_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
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
`svg_reset_fonts`| `bool`, optional| Override fonts in SVG. If enabled, font-family styles will be removed in the SVG, allowing the text to be inherited from the current theme or settings. Flourish type hint: boolean, defaults to None  
`show_css`| `bool`, optional| Edit CSS. Flourish type hint: boolean, defaults to None  
`stylesheet`| `Union[list, str]`, optional| Custom styles. Use the CSS class .clickable-element to target all interactive elements. When one is clicked, it has the CSS class is .highlighted and the others are .faded. The text for each clickable element is inside a .text-block, which is also .accordion in accordion mode. Flourish type hint: code, defaults to None  
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
`svg_url`| SVG file. Flourish type hint: url, defaults to `NULL`  
`svg_width_wide`| Image width. The width in percentage of the image in standard wide-screen view. Flourish type hint: number, defaults to `NULL`  
`mobile_view`| Different mobile view. Flourish type hint: boolean, defaults to `NULL`  
`mobile_breakpoint`| Breakpoint. The size in pixels at which to switch to mobile layout Flourish type hint: number, defaults to `NULL`  
`mobile_svg_mode`| Image on mobile. Choices: none, same, different. Whether to show the image at all on mobile. Flourish type hint: string, defaults to `NULL`  
`mobile_svg_url`| SVG file (mobile). Flourish type hint: url, defaults to `NULL`  
`mobile_svg_width`| Width. The width in percentage of the image on a mobile view. Flourish type hint: number, defaults to `NULL`  
`mobile_content_mode`| Mobile content mode. Choices: interactive, all, accordion. If turned on all content will display on load in mobile view. Flourish type hint: string, defaults to `NULL`  
`clickable_svg_animation`| Animation clickable elements. Choices: off, animation. Flourish type hint: string, defaults to `NULL`  
`clickable_svg_animation_duration`| Duration. The duration of the highlight animation on each clickable element. Flourish type hint: number, defaults to `NULL`  
`clickable_svg_animation_config`| Advanced. Reveal settings to adjust the SVG Animation properties on clickable elements. See Mozilla docs for more detailsFlourish type hint: boolean, defaults to `NULL`  
`clickable_svg_animation_attr`| Attribute. Flourish type hint: string, defaults to `NULL`  
`clickable_svg_animation_values`| Values. Flourish type hint: string, defaults to `NULL`  
`clickable_svg_animation_repeat`| Repeat. Flourish type hint: string, defaults to `NULL`  
`text_panel_enabled`| Text panel enabled. Disable to only show text in popups. Flourish type hint: boolean, defaults to `NULL`  
`h3_default`| Default heading. The text to show on load. Flourish type hint: text, defaults to `NULL`  
`h3_size`| Size. Flourish type hint: number, defaults to `NULL`  
`h4_default`| Default subheading. The text to show on load. Flourish type hint: text, defaults to `NULL`  
`h4_size`| Size. Flourish type hint: number, defaults to `NULL`  
`content_default`| Default text. The text to show on load. Flourish type hint: text, defaults to `NULL`  
`content_size`| Size. Flourish type hint: number, defaults to `NULL`  
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
`svg_reset_fonts`| Override fonts in SVG. If enabled, font-family styles will be removed in the SVG, allowing the text to be inherited from the current theme or settings. Flourish type hint: boolean, defaults to `NULL`  
`show_css`| Edit CSS. Flourish type hint: boolean, defaults to `NULL`  
`stylesheet`| Custom styles. Use the CSS class .clickable-element to target all interactive elements. When one is clicked, it has the CSS class is .highlighted and the others are .faded. The text for each clickable element is inside a .text-block, which is also .accordion in accordion mode. Flourish type hint: code, defaults to `NULL`  
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
