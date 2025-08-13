from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
import typing
__all__: list = ['SelectOccludedObjectsModel']
class SelectOccludedObjectsModel(omni.ui._ui.AbstractValueModel):
    """
    The value model that is reimplemented in Python to watch the occluded objects mode
    """
    PICKING_MODE_OCCLUDED_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/pickOccluded'
    def __init__(self):
        ...
    def _on_change(self, item, event_type):
        ...
    def clean(self):
        ...
    def get_value_as_bool(self):
        ...
    def set_value(self, value):
        ...
