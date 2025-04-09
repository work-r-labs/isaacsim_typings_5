from __future__ import annotations
import omni.ui.color_utils
__all__ = ['cl', 'default_datetime_window_style', 'select_circle_style', 'unselect_circle_style']
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
default_datetime_window_style: dict  # value = {'Window': {'background_color': 'transparent'}, 'Button': {'margin_height': 0.5, 'margin_width': 0.5}, 'Button::day:selected': {'background_color': 'datetime_fg'}, 'ComboBox::year': {'background_color': 'datetime_bg'}, 'ComboBox::timezone': {'secondary_color': 'datetime_bg'}, 'Rectangle::blank': {'background_color': 'transparent'}, 'Label::number': {'font_size': 32}, 'Label::morning': {'font_size': 14}, 'Label::week': {'font_size': 16}, 'Triangle::spinner': {'background_color': 'datetime_fg2', 'border_width': 0}, 'Triangle::spinner:hovered': {'background_color': 'datetime_fg'}, 'Triangle::spinner:pressed': {'background_color': 'datetime_fg'}, 'Circle::clock': {'background_color': 'datetime_fg2', 'border_width': 0}, 'Circle::day': {'background_color': 'transparent', 'border_color': 'transparent', 'border_width': 2, 'margin': 2}, 'Circle::day:hovered': {'border_color': 'blue_light'}}
select_circle_style: dict  # value = {'border_color': 'blue_light'}
unselect_circle_style: dict  # value = {'border_color': 'transparent'}
