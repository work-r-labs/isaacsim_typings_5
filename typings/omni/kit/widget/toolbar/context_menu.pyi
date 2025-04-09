from __future__ import annotations
import carb as carb
import omni as omni
from omni import ui
__all__: list = ['ContextMenu', 'ContextMenuEvent']
class ContextMenu:
    def on_mouse_event(self, event):
        ...
class ContextMenuEvent:
    """
    The object compatible with ContextMenu
    """
    def __init__(self):
        ...
