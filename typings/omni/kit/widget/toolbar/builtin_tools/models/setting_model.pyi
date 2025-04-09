from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
__all__: list = ['BoolSettingModel']
class BoolSettingModel(omni.ui._ui.AbstractValueModel):
    """
    The value model that is reimplemented in Python to watch a bool setting path
    """
    def __init__(self, setting_path, inverted: bool = False):
        ...
    def _on_change(self, item, event_type):
        ...
    def clean(self):
        ...
    def get_value_as_bool(self):
        ...
    def set_value(self, value):
        """
        Reimplemented set bool
        """
class FloatSettingModel(omni.ui._ui.AbstractValueModel):
    """
    The value model that is reimplemented in Python to watch a float setting path
    """
    def __init__(self, setting_path):
        ...
    def _on_change(self, item, event_type):
        ...
    def clean(self):
        ...
    def get_value_as_float(self):
        ...
    def set_value(self, value):
        """
        Reimplemented set float
        """
