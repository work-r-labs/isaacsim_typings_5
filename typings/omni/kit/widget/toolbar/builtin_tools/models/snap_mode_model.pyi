from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
import typing
__all__ = ['SnapModeModel', 'carb', 'ui']
class SnapModeModel(omni.ui._ui.AbstractValueModel):
    """
    The value model that is reimplemented in Python to watch the prim select mode
    """
    SNAP_MODE_FACE: typing.ClassVar[str] = 'Snap to Face'
    SNAP_MODE_INCREMENT: typing.ClassVar[str] = 'Snap to Increment'
    SNAP_MODE_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/snapToSurface'
    def __init__(self):
        ...
    def _on_snap_change(self, item, event_type):
        ...
    def clean(self):
        ...
    def get_value_as_bool(self):
        ...
    def get_value_as_string(self):
        ...
    def set_value(self, value):
        ...
