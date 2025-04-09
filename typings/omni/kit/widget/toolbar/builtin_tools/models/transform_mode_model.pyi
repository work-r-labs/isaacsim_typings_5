from __future__ import annotations
import carb as carb
from omni import ui
import omni.ui._ui
import typing
__all__: list = ['TransformModeModel']
class LocalGlobalTransformModeModel(TransformModeModel):
    TRANSFORM_MODE_GLOBAL: typing.ClassVar[str] = 'global'
    TRANSFORM_MODE_LOCAL: typing.ClassVar[str] = 'local'
    def __init__(self, op, op_space_setting_path):
        ...
    def _on_op_space_changed(self, item, event_type):
        ...
    def clean(self):
        ...
    def get_op_space_mode(self):
        ...
    def get_value_as_string(self):
        ...
    def set_value(self, value):
        ...
class TransformModeModel(omni.ui._ui.AbstractValueModel):
    """
    The value model that is reimplemented in Python to watch the prim select mode
    """
    TRANSFORM_OP_MOVE: typing.ClassVar[str] = 'move'
    TRANSFORM_OP_ROTATE: typing.ClassVar[str] = 'rotate'
    TRANSFORM_OP_SCALE: typing.ClassVar[str] = 'scale'
    TRANSFORM_OP_SELECT: typing.ClassVar[str] = 'select'
    TRANSFORM_OP_SETTING: typing.ClassVar[str] = '/app/transform/operation'
    def __init__(self, op):
        ...
    def _on_op_change(self, item, event_type):
        ...
    def _on_op_space_changed(self, item, event_type):
        ...
    def clean(self):
        ...
    def get_value_as_bool(self):
        ...
    def set_value(self, value):
        """
        Reimplemented set bool
        """
