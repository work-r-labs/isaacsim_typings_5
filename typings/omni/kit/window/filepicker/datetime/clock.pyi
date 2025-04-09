from __future__ import annotations
import omni.kit.window.filepicker.datetime.models
from omni.kit.window.filepicker.datetime.models import TimeModel
from omni import ui
__all__ = ['ClockWidget', 'TimeModel', 'ui']
class ClockWidget:
    """
    
        Represents a clock to show hour minute and second
        Keyword Args:
            model (TimeModel): Widget model.
            width (int): Widget width. Default 160.
            height (int): Widget height. Default 32.
        
    """
    def __del__(self):
        ...
    def __init__(self, model: omni.kit.window.filepicker.datetime.models.TimeModel, width: int = 160, height: int = 32):
        ...
    def _on_half_day_clicked(self, key):
        ...
    def _on_hour_clicked(self, key, step):
        ...
    def _on_minute_clicked(self, key, step):
        ...
    def _on_time_changed(self, model):
        ...
    def destroy(self):
        ...
    @property
    def model(self):
        ...
