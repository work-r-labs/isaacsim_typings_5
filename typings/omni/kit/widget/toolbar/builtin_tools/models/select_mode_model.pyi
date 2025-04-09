from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
import typing
__all__: list = ['SelectModeModel']
class SelectModeModel(omni.ui._ui.AbstractValueModel):
    """
    The value model that is reimplemented in Python to watch the prim select mode
    """
    PICKING_MODE_DEFAULT: typing.ClassVar[str] = 'type:ALL'
    PICKING_MODE_MODELS: typing.ClassVar[str] = 'kind:model.ALL'
    PICKING_MODE_PRIMS: typing.ClassVar[str] = 'type:ALL'
    PICKING_MODE_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/pickingMode'
    def __init__(self):
        ...
    def _on_change(self, item, event_type):
        ...
    def clean(self):
        ...
    def get_value_as_bool(self):
        ...
    def get_value_as_string(self):
        ...
    def set_value(self, value):
        ...
