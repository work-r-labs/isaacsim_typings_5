from __future__ import annotations
import omni.kit.window.filepicker.datetime.models
from omni.kit.window.filepicker.datetime.models import ZoneModel
from omni import ui
__all__ = ['TimezoneWidget', 'ZoneModel', 'ui']
class TimezoneWidget:
    """
    
        a combox for common timezones.
        Keyword Args:
        model (ZoneModel): Widget model.
        width (int): Widget width. Default 80.
        
    """
    def __del__(self):
        ...
    def __init__(self, model: omni.kit.window.filepicker.datetime.models.ZoneModel = None, **kwargs):
        ...
    def _get_pytz_timezones(self):
        ...
    def _on_combo_selected(self, model, item):
        ...
    def _on_zone_changed(self, model):
        ...
    def _set_timezone(self, index):
        ...
    def destroy(self):
        ...
    @property
    def model(self):
        ...
