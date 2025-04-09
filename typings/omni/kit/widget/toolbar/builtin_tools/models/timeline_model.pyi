from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.commands.command import execute
from omni import ui
__all__: list = ['TimelinePlayPauseModel']
class TimelinePlayPauseModel(omni.ui._ui.AbstractValueModel):
    """
    The value model that is reimplemented in Python to watch a bool setting path
    """
    def __init__(self):
        ...
    def _on_timeline_event(self, e):
        ...
    def clean(self):
        ...
    def get_value_as_bool(self):
        ...
    def set_value(self, value):
        """
        Reimplemented set bool
        """
