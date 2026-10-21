---
url: https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/
title: Set sports race chart details - Add extra details to charts - Canva Flourish Charts Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:57:50.269247+00:00
---

# Set sports race chart details - Add extra details to charts - Canva Flourish Charts Documentation

> Source: https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/

Add extra details to charts

[Set functions](https://www.canva.dev/opensource/flourish-charts/api/set/)[Set audio chart details](https://www.canva.dev/opensource/flourish-charts/api/set-audio-details/)[Set bar chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bar-chart-race-details/)[Set bubble chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-bubble-chart-details/)[Set calculator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-calculator-details/)[Set cards chart details](https://www.canva.dev/opensource/flourish-charts/api/set-cards-details/)[Set chord diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-chord-diagram-details/)[Set countdown chart details](https://www.canva.dev/opensource/flourish-charts/api/set-countdown-details/)[Set draw the line chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-draw-the-line-details/)[Set election results chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-election-results-chart-details/)[Set gantt chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gantt-details/)[Set gauge chart details](https://www.canva.dev/opensource/flourish-charts/api/set-gauge-details/)[Set hierarchy chart details](https://www.canva.dev/opensource/flourish-charts/api/set-hierarchy-details/)[Set line chart race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-horserace-details/)[Set interactive svg chart details](https://www.canva.dev/opensource/flourish-charts/api/set-interactive-svg-details/)[Set line, bar and pie charts chart details](https://www.canva.dev/opensource/flourish-charts/api/set-line-bar-pie-details/)[Set marimekko chart details](https://www.canva.dev/opensource/flourish-charts/api/set-marimekko-details/)[Set network graph chart details](https://www.canva.dev/opensource/flourish-charts/api/set-network-graph-details/)[Set number ticker chart details](https://www.canva.dev/opensource/flourish-charts/api/set-number-ticker-details/)[Set parliament chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-parliament-chart-details/)[Set photo slider chart details](https://www.canva.dev/opensource/flourish-charts/api/set-photo-slider-details/)[Set pictogram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-pictogram-details/)[Set quiz chart details](https://www.canva.dev/opensource/flourish-charts/api/set-quiz-details/)[Set radar chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-radar-details/)[Set sankey diagram chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sankey-details/)[Set scatter chart details](https://www.canva.dev/opensource/flourish-charts/api/set-scatter-details/)[Set slope chart chart details](https://www.canva.dev/opensource/flourish-charts/api/set-slope-chart-details/)[Set sports chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-details/)[Set sports race chart details](https://www.canva.dev/opensource/flourish-charts/api/set-sports-race-details/)[Set survey chart details](https://www.canva.dev/opensource/flourish-charts/api/set-survey-details/)[Set svg annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-svg-annotator-details/)[Set table chart details](https://www.canva.dev/opensource/flourish-charts/api/set-table-details/)[Set text annotator chart details](https://www.canva.dev/opensource/flourish-charts/api/set-text-annotator-details/)[Set timeline chart details](https://www.canva.dev/opensource/flourish-charts/api/set-timeline-details/)[Set tournament chart details](https://www.canva.dev/opensource/flourish-charts/api/set-tournament-details/)[Set word cloud chart details](https://www.canva.dev/opensource/flourish-charts/api/set-word-cloud-details/)

# Set sports race chart details

Copy page

## Usage

PythonPython

RR
    
    
    def set_sports_race_details(
    
        self,
    
        preset_svg: str = None,
    
        custom_svg: Union[list, str] = None,
    
        track_path_id: str = None,
    
        track_lane_width: float = None,
    
        track_back_and_forth: bool = None,
    
        participant_icon_mode: str = None,
    
        participant_size: float = None,
    
        participant_stroke_width: float = None,
    
        participant_stroke_opacity: float = None,
    
        participant_fill_opacity: float = None,
    
        preset_participant_image: str = None,
    
        custom_participant_start_image: str = None,
    
        custom_participant_race_image: str = None,
    
        custom_participant_finish_image: str = None,
    
        image_initial_rotation: str = None,
    
        image_initial_flip_x: bool = None,
    
        image_initial_flip_y: bool = None,
    
        image_transform_mode: str = None,
    
        participant_icon_recolor: bool = None,
    
        chart_participant_color_scale_categorical_palette: Union[list, str] = None,
    
        chart_participant_color_scale_categorical_extend: bool = None,
    
        chart_participant_color_scale_categorical_custom_palette: Union[list, str] = None,
    
        chart_participant_color_scale_numeric_type: str = None,
    
        chart_participant_color_scale_binning: bool = None,
    
        chart_participant_color_scale_bin_mode: str = None,
    
        chart_participant_color_scale_bin_count: float = None,
    
        chart_participant_color_scale_bin_thresholds: str = None,
    
        chart_participant_color_scale_sequential_palette: str = None,
    
        chart_participant_color_scale_sequential_reverse: bool = None,
    
        chart_participant_color_scale_sequential_custom_min: str = None,
    
        chart_participant_color_scale_sequential_custom_max: str = None,
    
        chart_participant_color_scale_sequential_color_space: str = None,
    
        chart_participant_color_scale_sequential_custom_domain: bool = None,
    
        chart_participant_color_scale_sequential_domain_min: float = None,
    
        chart_participant_color_scale_sequential_domain_max: float = None,
    
        chart_participant_color_scale_diverging_palette: str = None,
    
        chart_participant_color_scale_diverging_reverse: bool = None,
    
        chart_participant_color_scale_diverging_custom_min: str = None,
    
        chart_participant_color_scale_diverging_custom_mid: str = None,
    
        chart_participant_color_scale_diverging_custom_max: str = None,
    
        chart_participant_color_scale_diverging_color_space: str = None,
    
        chart_participant_color_scale_diverging_custom_domain: bool = None,
    
        chart_participant_color_scale_diverging_domain_min: float = None,
    
        chart_participant_color_scale_diverging_domain_mid: float = None,
    
        chart_participant_color_scale_diverging_domain_max: float = None,
    
        camera_mode: str = None,
    
        zoom: float = None,
    
        checkpoint_mode: str = None,
    
        checkpoints: Union[list, str] = None,
    
        times_cumulative: bool = None,
    
        participant_label_mode: str = None,
    
        participant_label_custom: Union[list, str] = None,
    
        participant_label_position: str = None,
    
        participant_label_style: bool = None,
    
        participant_label_color: str = None,
    
        participant_label_size: float = None,
    
        participant_label_stroke: str = None,
    
        participant_label_stroke_size: float = None,
    
        participant_label_weight: str = None,
    
        participant_highlight: bool = None,
    
        participant_highlight_color: str = None,
    
        participant_highlight_width: float = None,
    
        label_position_enabled: bool = None,
    
        label_position_time: str = None,
    
        label_position_type: str = None,
    
        label_medal_enabled: bool = None,
    
        label_medal_time: str = None,
    
        label_medal_type: str = None,
    
        label_medal_replace_position: bool = None,
    
        label_finishing_time_enabled: bool = None,
    
        label_finishing_time_time: str = None,
    
        participant_stacking: str = None,
    
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
    
    
    set_sports_race_details(
    
        .,
    
        preset_svg = NULL,
    
        custom_svg = NULL,
    
        track_path_id = NULL,
    
        track_lane_width = NULL,
    
        track_back_and_forth = NULL,
    
        participant_icon_mode = NULL,
    
        participant_size = NULL,
    
        participant_stroke_width = NULL,
    
        participant_stroke_opacity = NULL,
    
        participant_fill_opacity = NULL,
    
        preset_participant_image = NULL,
    
        custom_participant_start_image = NULL,
    
        custom_participant_race_image = NULL,
    
        custom_participant_finish_image = NULL,
    
        image_initial_rotation = NULL,
    
        image_initial_flip_x = NULL,
    
        image_initial_flip_y = NULL,
    
        image_transform_mode = NULL,
    
        participant_icon_recolor = NULL,
    
        chart_participant_color_scale_categorical_palette = NULL,
    
        chart_participant_color_scale_categorical_extend = NULL,
    
        chart_participant_color_scale_categorical_custom_palette = NULL,
    
        chart_participant_color_scale_numeric_type = NULL,
    
        chart_participant_color_scale_binning = NULL,
    
        chart_participant_color_scale_bin_mode = NULL,
    
        chart_participant_color_scale_bin_count = NULL,
    
        chart_participant_color_scale_bin_thresholds = NULL,
    
        chart_participant_color_scale_sequential_palette = NULL,
    
        chart_participant_color_scale_sequential_reverse = NULL,
    
        chart_participant_color_scale_sequential_custom_min = NULL,
    
        chart_participant_color_scale_sequential_custom_max = NULL,
    
        chart_participant_color_scale_sequential_color_space = NULL,
    
        chart_participant_color_scale_sequential_custom_domain = NULL,
    
        chart_participant_color_scale_sequential_domain_min = NULL,
    
        chart_participant_color_scale_sequential_domain_max = NULL,
    
        chart_participant_color_scale_diverging_palette = NULL,
    
        chart_participant_color_scale_diverging_reverse = NULL,
    
        chart_participant_color_scale_diverging_custom_min = NULL,
    
        chart_participant_color_scale_diverging_custom_mid = NULL,
    
        chart_participant_color_scale_diverging_custom_max = NULL,
    
        chart_participant_color_scale_diverging_color_space = NULL,
    
        chart_participant_color_scale_diverging_custom_domain = NULL,
    
        chart_participant_color_scale_diverging_domain_min = NULL,
    
        chart_participant_color_scale_diverging_domain_mid = NULL,
    
        chart_participant_color_scale_diverging_domain_max = NULL,
    
        camera_mode = NULL,
    
        zoom = NULL,
    
        checkpoint_mode = NULL,
    
        checkpoints = NULL,
    
        times_cumulative = NULL,
    
        participant_label_mode = NULL,
    
        participant_label_custom = NULL,
    
        participant_label_position = NULL,
    
        participant_label_style = NULL,
    
        participant_label_color = NULL,
    
        participant_label_size = NULL,
    
        participant_label_stroke = NULL,
    
        participant_label_stroke_size = NULL,
    
        participant_label_weight = NULL,
    
        participant_highlight = NULL,
    
        participant_highlight_color = NULL,
    
        participant_highlight_width = NULL,
    
        label_position_enabled = NULL,
    
        label_position_time = NULL,
    
        label_position_type = NULL,
    
        label_medal_enabled = NULL,
    
        label_medal_time = NULL,
    
        label_medal_type = NULL,
    
        label_medal_replace_position = NULL,
    
        label_finishing_time_enabled = NULL,
    
        label_finishing_time_time = NULL,
    
        participant_stacking = NULL,
    
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
`preset_svg`| `str`, optional| Choices: athletics, swimming, cycling, custom. Flourish type hint: string, defaults to None  
`custom_svg`| `Union[list, str]`, optional| Custom SVG. Use a custom track using your own SVG Flourish type hint: text, defaults to None  
`track_path_id`| `str`, optional| Path ID. The ID of the element in the SVG which defines the center of the track. Flourish type hint: string, defaults to None  
`track_lane_width`| `float`, optional| Lane width. The distance between each participant. Flourish type hint: number, defaults to None  
`track_back_and_forth`| `bool`, optional| Track type. Choices: False, True. Whether the track goes back and forth, like a swimming pool, or back to the start, like a race track. Flourish type hint: boolean, defaults to None  
`participant_icon_mode`| `str`, optional| Icon type. Choices: circle, image. Flourish type hint: string, defaults to None  
`participant_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`participant_stroke_width`| `float`, optional| Line width. Flourish type hint: number, defaults to None  
`participant_stroke_opacity`| `float`, optional| Stroke opacity. Flourish type hint: number, defaults to None  
`participant_fill_opacity`| `float`, optional| Fill opacity. Flourish type hint: number, defaults to None  
`preset_participant_image`| `str`, optional| Default images. Choices: runner, swimmer, cyclist, custom. The images used if no image is included for the participant in the datasheet. Flourish type hint: string, defaults to None  
`custom_participant_start_image`| `str`, optional| Custom start image. The image shown at the start of the race. Flourish type hint: url, defaults to None  
`custom_participant_race_image`| `str`, optional| Custom racing image. The image shown while the participant is racing. Flourish type hint: url, defaults to None  
`custom_participant_finish_image`| `str`, optional| Custom finish image. The image shown when the participant has finished the race. Flourish type hint: url, defaults to None  
`image_initial_rotation`| `str`, optional| Rotate images. Choices: 0, 90, 180, 270. Flourish type hint: string, defaults to None  
`image_initial_flip_x`| `bool`, optional| Flip horizontally. Flourish type hint: boolean, defaults to None  
`image_initial_flip_y`| `bool`, optional| Flip vertically. Flourish type hint: boolean, defaults to None  
`image_transform_mode`| `str`, optional| Direction change. Choices: rotate, flip_x, flip_y, flip_both, static. Change the direction of the image based on which way the participant is traveling. Rotate rotates the image to face the direction of travel. Flip horizontally flips the image horizontally depending on whether the participant is traveling towards the left or right. Flip vertically flips the image vertically depending on whether the participant is traveling towards the top or bottom. Flip horizontally and vertically combines the horizontal and vertical flip settings. Static doesnt change the direction of the image. Flourish type hint: string, defaults to None  
`participant_icon_recolor`| `bool`, optional| Recolor icons. Apply colors to differentiate the participants. Works best with greyscale images. Flourish type hint: boolean, defaults to None  
`chart_participant_color_scale_categorical_palette`| `Union[list, str]`, optional| Palette. Flourish type hint: colors, defaults to None  
`chart_participant_color_scale_categorical_extend`| `bool`, optional| Extend. Automatically generate additional colours when needed to avoid the palette colours being used more than once. Flourish type hint: boolean, defaults to None  
`chart_participant_color_scale_categorical_custom_palette`| `Union[list, str]`, optional| Custom overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to None  
`chart_participant_color_scale_numeric_type`| `str`, optional| Scale type. Choices: sequential, diverging. Flourish type hint: string, defaults to None  
`chart_participant_color_scale_binning`| `bool`, optional| Choices: False, True. In linear mode, the color scale will run as a smooth gradient between 2 colors. In binned mode, the gradient will be divided in smaller blocks. Flourish type hint: boolean, defaults to None  
`chart_participant_color_scale_bin_mode`| `str`, optional| Binning mode. Choices: fixed, quantile, custom. Flourish type hint: string, defaults to None  
`chart_participant_color_scale_bin_count`| `float`, optional| Number of bins. Flourish type hint: number, defaults to None  
`chart_participant_color_scale_bin_thresholds`| `str`, optional| Custom thresholds. Enter your desired thresholds, separating them with a ";". For instance, "5;10;15". Bins form as follows: From the datas minimum value (domain minimum) up to the first threshold. Between consecutive thresholds. From the last threshold to the datas maximum value (domain maximum). For "5;10;15", youll get four bins based on your datas range. Flourish type hint: string, defaults to None  
`chart_participant_color_scale_sequential_palette`| `str`, optional| Palette. Flourish type hint: string, defaults to None  
`chart_participant_color_scale_sequential_reverse`| `bool`, optional| Reverse. Flourish type hint: boolean, defaults to None  
`chart_participant_color_scale_sequential_custom_min`| `str`, optional| Minimum color. Flourish type hint: color, defaults to None  
`chart_participant_color_scale_sequential_custom_max`| `str`, optional| Maximum color. Flourish type hint: color, defaults to None  
`chart_participant_color_scale_sequential_color_space`| `str`, optional| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to None  
`chart_participant_color_scale_sequential_custom_domain`| `bool`, optional| Domain. Choices: False, True. Flourish type hint: boolean, defaults to None  
`chart_participant_color_scale_sequential_domain_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_participant_color_scale_sequential_domain_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`chart_participant_color_scale_diverging_palette`| `str`, optional| Palette. Flourish type hint: string, defaults to None  
`chart_participant_color_scale_diverging_reverse`| `bool`, optional| Reverse. Flourish type hint: boolean, defaults to None  
`chart_participant_color_scale_diverging_custom_min`| `str`, optional| Minimum color. Flourish type hint: color, defaults to None  
`chart_participant_color_scale_diverging_custom_mid`| `str`, optional| Midpoint color. Flourish type hint: color, defaults to None  
`chart_participant_color_scale_diverging_custom_max`| `str`, optional| Maximum color. Flourish type hint: color, defaults to None  
`chart_participant_color_scale_diverging_color_space`| `str`, optional| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to None  
`chart_participant_color_scale_diverging_custom_domain`| `bool`, optional| Domain. Choices: False, True. Flourish type hint: boolean, defaults to None  
`chart_participant_color_scale_diverging_domain_min`| `float`, optional| Min. Flourish type hint: number, defaults to None  
`chart_participant_color_scale_diverging_domain_mid`| `float`, optional| Mid. Flourish type hint: number, defaults to None  
`chart_participant_color_scale_diverging_domain_max`| `float`, optional| Max. Flourish type hint: number, defaults to None  
`camera_mode`| `str`, optional| Camera mode. Choices: track, leader. Flourish type hint: string, defaults to None  
`zoom`| `float`, optional| Zoom level. How much to zoom in when playing. Flourish type hint: number, defaults to None  
`checkpoint_mode`| `str`, optional| Checkpoint mode. Choices: laps, splits, custom. Flourish type hint: string, defaults to None  
`checkpoints`| `Union[list, str]`, optional| Checkpoints. Enter the number of laps completed at each recorded checkpoint/column in the data. E.g. "0.5, 1, 1.5, 2" would mean that the times were taken every half a lap. Enter one checkpoint per line. Flourish type hint: text, defaults to None  
`times_cumulative`| `bool`, optional| Times are cumulative. Switch on if the time columns represent the cumulative time taken at each checkpoint (e.g. 12, 25, 36). Switch off if the times represent how long individual checkpoints took to complete (e.g. 12, 13, 11). Flourish type hint: boolean, defaults to None  
`participant_label_mode`| `str`, optional| Label mode. Choices: auto, leader, all, custom. Determines which labels are drawn. Auto draws as many labels as possible whilst avoiding overlaps. Flourish type hint: string, defaults to None  
`participant_label_custom`| `Union[list, str]`, optional| Participants to label. Enter the names of the participants to label. These must exactly match the names in your data. Enter one name per line. Flourish type hint: text, defaults to None  
`participant_label_position`| `str`, optional| Label position. Choices: auto, left, right. Flourish type hint: string, defaults to None  
`participant_label_style`| `bool`, optional| Style. Flourish type hint: boolean, defaults to None  
`participant_label_color`| `str`, optional| Color. Flourish type hint: color, defaults to None  
`participant_label_size`| `float`, optional| Size. Flourish type hint: number, defaults to None  
`participant_label_stroke`| `str`, optional| Outline. Flourish type hint: color, defaults to None  
`participant_label_stroke_size`| `float`, optional| Outline width. As a % of the font size. Flourish type hint: number, defaults to None  
`participant_label_weight`| `str`, optional| Weight. Choices: 400, 600. Flourish type hint: string, defaults to None  
`participant_highlight`| `bool`, optional| Highlight icons. Highlight the labeled participant(s). Flourish type hint: boolean, defaults to None  
`participant_highlight_color`| `str`, optional| Highlight color. Flourish type hint: color, defaults to None  
`participant_highlight_width`| `float`, optional| Highlight width. Flourish type hint: number, defaults to None  
`label_position_enabled`| `bool`, optional| Choices: False, True. Whether to show the position of the participant in the label. Flourish type hint: boolean, defaults to None  
`label_position_time`| `str`, optional| Show position. Choices: always, race, finish. Set to At finish, to only show a participants position when theyve completed the race. Set to During race, to only show a participants position while they are still racing. Flourish type hint: string, defaults to None  
`label_position_type`| `str`, optional| Position to show. Choices: current, finish. Whether to show a participants current position in the race, or their finishing position. Flourish type hint: string, defaults to None  
`label_medal_enabled`| `bool`, optional| Choices: False, True. Flourish type hint: boolean, defaults to None  
`label_medal_time`| `str`, optional| Show medals. Choices: always, race, finish. Set to At finish, to only show a participants medal when theyve completed the race. Set to During race, to only show a participants medal while they are still racing. Flourish type hint: string, defaults to None  
`label_medal_type`| `str`, optional| Medal to show. Choices: current, finish. Whether to show the medal position for a participant at the current point in the race, or the medal they win at the end of the race. Flourish type hint: string, defaults to None  
`label_medal_replace_position`| `bool`, optional| Replace position. Turn on to replace a participants position label with their medal if they are in a medal position. Flourish type hint: boolean, defaults to None  
`label_finishing_time_enabled`| `bool`, optional| Choices: False, True. Flourish type hint: boolean, defaults to None  
`label_finishing_time_time`| `str`, optional| Show finishing time. Choices: always, finish. Flourish type hint: string, defaults to None  
`participant_stacking`| `str`, optional| Choices: sheet_order, rank, y_position. Determines which participants obscure other participants when they overlap. Flourish type hint: string, defaults to None  
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
`preset_svg`| Choices: athletics, swimming, cycling, custom. Flourish type hint: string, defaults to `NULL`  
`custom_svg`| Custom SVG. Use a custom track using your own SVG Flourish type hint: text, defaults to `NULL`  
`track_path_id`| Path ID. The ID of the element in the SVG which defines the center of the track. Flourish type hint: string, defaults to `NULL`  
`track_lane_width`| Lane width. The distance between each participant. Flourish type hint: number, defaults to `NULL`  
`track_back_and_forth`| Track type. Choices: `FALSE`, `TRUE`. Whether the track goes back and forth, like a swimming pool, or back to the start, like a race track. Flourish type hint: boolean, defaults to `NULL`  
`participant_icon_mode`| Icon type. Choices: circle, image. Flourish type hint: string, defaults to `NULL`  
`participant_size`| Size. Flourish type hint: number, defaults to `NULL`  
`participant_stroke_width`| Line width. Flourish type hint: number, defaults to `NULL`  
`participant_stroke_opacity`| Stroke opacity. Flourish type hint: number, defaults to `NULL`  
`participant_fill_opacity`| Fill opacity. Flourish type hint: number, defaults to `NULL`  
`preset_participant_image`| Default images. Choices: runner, swimmer, cyclist, custom. The images used if no image is included for the participant in the datasheet. Flourish type hint: string, defaults to `NULL`  
`custom_participant_start_image`| Custom start image. The image shown at the start of the race. Flourish type hint: url, defaults to `NULL`  
`custom_participant_race_image`| Custom racing image. The image shown while the participant is racing. Flourish type hint: url, defaults to `NULL`  
`custom_participant_finish_image`| Custom finish image. The image shown when the participant has finished the race. Flourish type hint: url, defaults to `NULL`  
`image_initial_rotation`| Rotate images. Choices: 0, 90, 180, 270. Flourish type hint: string, defaults to `NULL`  
`image_initial_flip_x`| Flip horizontally. Flourish type hint: boolean, defaults to `NULL`  
`image_initial_flip_y`| Flip vertically. Flourish type hint: boolean, defaults to `NULL`  
`image_transform_mode`| Direction change. Choices: rotate, flip_x, flip_y, flip_both, static. Change the direction of the image based on which way the participant is traveling. Rotate rotates the image to face the direction of travel. Flip horizontally flips the image horizontally depending on whether the participant is traveling towards the left or right. Flip vertically flips the image vertically depending on whether the participant is traveling towards the top or bottom. Flip horizontally and vertically combines the horizontal and vertical flip settings. Static doesnt change the direction of the image. Flourish type hint: string, defaults to `NULL`  
`participant_icon_recolor`| Recolor icons. Apply colors to differentiate the participants. Works best with greyscale images. Flourish type hint: boolean, defaults to `NULL`  
`chart_participant_color_scale_categorical_palette`| Palette. Flourish type hint: colors, defaults to `NULL`  
`chart_participant_color_scale_categorical_extend`| Extend. Automatically generate additional colours when needed to avoid the palette colours being used more than once. Flourish type hint: boolean, defaults to `NULL`  
`chart_participant_color_scale_categorical_custom_palette`| Custom overrides. Enter the label name for which you wish to set the color, followed by a colon and the desired color value. Colors can be set using Hex, RGB, color names or RGBA, if you want to set the opacity Multiple colors can be set using multiple lines. For example: Party 1: red Party 2: #4455AA Party 3: rgb(30,168,26). Flourish type hint: text, defaults to `NULL`  
`chart_participant_color_scale_numeric_type`| Scale type. Choices: sequential, diverging. Flourish type hint: string, defaults to `NULL`  
`chart_participant_color_scale_binning`| Choices: `FALSE`, `TRUE`. In linear mode, the color scale will run as a smooth gradient between 2 colors. In binned mode, the gradient will be divided in smaller blocks. Flourish type hint: boolean, defaults to `NULL`  
`chart_participant_color_scale_bin_mode`| Binning mode. Choices: fixed, quantile, custom. Flourish type hint: string, defaults to `NULL`  
`chart_participant_color_scale_bin_count`| Number of bins. Flourish type hint: number, defaults to `NULL`  
`chart_participant_color_scale_bin_thresholds`| Custom thresholds. Enter your desired thresholds, separating them with a ";". For instance, "5;10;15". Bins form as follows: From the datas minimum value (domain minimum) up to the first threshold. Between consecutive thresholds. From the last threshold to the datas maximum value (domain maximum). For "5;10;15", youll get four bins based on your datas range. Flourish type hint: string, defaults to `NULL`  
`chart_participant_color_scale_sequential_palette`| Palette. Flourish type hint: string, defaults to `NULL`  
`chart_participant_color_scale_sequential_reverse`| Reverse. Flourish type hint: boolean, defaults to `NULL`  
`chart_participant_color_scale_sequential_custom_min`| Minimum color. Flourish type hint: color, defaults to `NULL`  
`chart_participant_color_scale_sequential_custom_max`| Maximum color. Flourish type hint: color, defaults to `NULL`  
`chart_participant_color_scale_sequential_color_space`| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to `NULL`  
`chart_participant_color_scale_sequential_custom_domain`| Domain. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_participant_color_scale_sequential_domain_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_participant_color_scale_sequential_domain_max`| Max. Flourish type hint: number, defaults to `NULL`  
`chart_participant_color_scale_diverging_palette`| Palette. Flourish type hint: string, defaults to `NULL`  
`chart_participant_color_scale_diverging_reverse`| Reverse. Flourish type hint: boolean, defaults to `NULL`  
`chart_participant_color_scale_diverging_custom_min`| Minimum color. Flourish type hint: color, defaults to `NULL`  
`chart_participant_color_scale_diverging_custom_mid`| Midpoint color. Flourish type hint: color, defaults to `NULL`  
`chart_participant_color_scale_diverging_custom_max`| Maximum color. Flourish type hint: color, defaults to `NULL`  
`chart_participant_color_scale_diverging_color_space`| Color space. Choices: rgb, lab, hcl, hsl. Flourish type hint: string, defaults to `NULL`  
`chart_participant_color_scale_diverging_custom_domain`| Domain. Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`chart_participant_color_scale_diverging_domain_min`| Min. Flourish type hint: number, defaults to `NULL`  
`chart_participant_color_scale_diverging_domain_mid`| Mid. Flourish type hint: number, defaults to `NULL`  
`chart_participant_color_scale_diverging_domain_max`| Max. Flourish type hint: number, defaults to `NULL`  
`camera_mode`| Camera mode. Choices: track, leader. Flourish type hint: string, defaults to `NULL`  
`zoom`| Zoom level. How much to zoom in when playing. Flourish type hint: number, defaults to `NULL`  
`checkpoint_mode`| Checkpoint mode. Choices: laps, splits, custom. Flourish type hint: string, defaults to `NULL`  
`checkpoints`| Checkpoints. Enter the number of laps completed at each recorded checkpoint/column in the data. E.g. "0.5, 1, 1.5, 2" would mean that the times were taken every half a lap. Enter one checkpoint per line. Flourish type hint: text, defaults to `NULL`  
`times_cumulative`| Times are cumulative. Switch on if the time columns represent the cumulative time taken at each checkpoint (e.g. 12, 25, 36). Switch off if the times represent how long individual checkpoints took to complete (e.g. 12, 13, 11). Flourish type hint: boolean, defaults to `NULL`  
`participant_label_mode`| Label mode. Choices: auto, leader, all, custom. Determines which labels are drawn. Auto draws as many labels as possible whilst avoiding overlaps. Flourish type hint: string, defaults to `NULL`  
`participant_label_custom`| Participants to label. Enter the names of the participants to label. These must exactly match the names in your data. Enter one name per line. Flourish type hint: text, defaults to `NULL`  
`participant_label_position`| Label position. Choices: auto, left, right. Flourish type hint: string, defaults to `NULL`  
`participant_label_style`| Style. Flourish type hint: boolean, defaults to `NULL`  
`participant_label_color`| Color. Flourish type hint: color, defaults to `NULL`  
`participant_label_size`| Size. Flourish type hint: number, defaults to `NULL`  
`participant_label_stroke`| Outline. Flourish type hint: color, defaults to `NULL`  
`participant_label_stroke_size`| Outline width. As a % of the font size. Flourish type hint: number, defaults to `NULL`  
`participant_label_weight`| Weight. Choices: 400, 600. Flourish type hint: string, defaults to `NULL`  
`participant_highlight`| Highlight icons. Highlight the labeled participant(s). Flourish type hint: boolean, defaults to `NULL`  
`participant_highlight_color`| Highlight color. Flourish type hint: color, defaults to `NULL`  
`participant_highlight_width`| Highlight width. Flourish type hint: number, defaults to `NULL`  
`label_position_enabled`| Choices: `FALSE`, `TRUE`. Whether to show the position of the participant in the label. Flourish type hint: boolean, defaults to `NULL`  
`label_position_time`| Show position. Choices: always, race, finish. Set to At finish, to only show a participants position when theyve completed the race. Set to During race, to only show a participants position while they are still racing. Flourish type hint: string, defaults to `NULL`  
`label_position_type`| Position to show. Choices: current, finish. Whether to show a participants current position in the race, or their finishing position. Flourish type hint: string, defaults to `NULL`  
`label_medal_enabled`| Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`label_medal_time`| Show medals. Choices: always, race, finish. Set to At finish, to only show a participants medal when theyve completed the race. Set to During race, to only show a participants medal while they are still racing. Flourish type hint: string, defaults to `NULL`  
`label_medal_type`| Medal to show. Choices: current, finish. Whether to show the medal position for a participant at the current point in the race, or the medal they win at the end of the race. Flourish type hint: string, defaults to `NULL`  
`label_medal_replace_position`| Replace position. Turn on to replace a participants position label with their medal if they are in a medal position. Flourish type hint: boolean, defaults to `NULL`  
`label_finishing_time_enabled`| Choices: `FALSE`, `TRUE`. Flourish type hint: boolean, defaults to `NULL`  
`label_finishing_time_time`| Show finishing time. Choices: always, finish. Flourish type hint: string, defaults to `NULL`  
`participant_stacking`| Choices: sheet_order, rank, y_position. Determines which participants obscure other participants when they overlap. Flourish type hint: string, defaults to `NULL`  
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
