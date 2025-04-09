from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__ = ['ExpandMenuItem', 'ui']
class ExpandMenuItem(omni.ui._ui.MenuItem):
    def __init__(self, expand_model):
        ...
    @property
    def checked(self):
        ...
    @checked.setter
    def checked(self, value: bool):
        ...
class _ExpandButtonDelegate(omni.ui._ui.MenuDelegate):
    """
    Simple button with left arrow
    """
    checked: bool
    def __init__(self, expanded: bool, **kwargs):
        ...
    def build_item(self, item: omni.ui._ui.MenuHelper):
        ...
