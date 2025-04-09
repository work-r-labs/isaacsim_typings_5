from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.window.filepicker.datetime.clock import ClockWidget
from omni.kit.window.filepicker.datetime.models import TimeModel
from omni import ui
__all__ = ['ClockWidget', 'TimeModel', 'TimeWidget', 'asyncio', 'default_datetime_window_style', 'omni', 'ui']
class TimeWidget:
    def __del__(self):
        ...
    def __init__(self, model: omni.kit.window.filepicker.datetime.models.TimeModel = None, **kwargs):
        """
        
                Time Widget.
                Keyword Args:
                model (TimeModel): Widget model.
                width (int): Input field width of widget. Default 60.
                style (dict): Widget style.
                
        """
    def _destroy_window_async(self):
        ...
    def _on_begin_edit(self, model):
        ...
    def _on_blank_clicked(self, x, y, b, m):
        ...
    def destroy(self):
        ...
    @property
    def model(self):
        ...
default_datetime_window_style: dict  # value = {'Window': {'background_color': 'transparent'}, 'Button': {'margin_height': 0.5, 'margin_width': 0.5}, 'Button::day:selected': {'background_color': 'datetime_fg'}, 'ComboBox::year': {'background_color': 'datetime_bg'}, 'ComboBox::timezone': {'secondary_color': 'datetime_bg'}, 'Rectangle::blank': {'background_color': 'transparent'}, 'Label::number': {'font_size': 32}, 'Label::morning': {'font_size': 14}, 'Label::week': {'font_size': 16}, 'Triangle::spinner': {'background_color': 'datetime_fg2', 'border_width': 0}, 'Triangle::spinner:hovered': {'background_color': 'datetime_fg'}, 'Triangle::spinner:pressed': {'background_color': 'datetime_fg'}, 'Circle::clock': {'background_color': 'datetime_fg2', 'border_width': 0}, 'Circle::day': {'background_color': 'transparent', 'border_color': 'transparent', 'border_width': 2, 'margin': 2}, 'Circle::day:hovered': {'border_color': 'blue_light'}}
