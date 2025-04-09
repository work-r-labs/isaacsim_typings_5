from __future__ import annotations
import carb as carb
import omni.kit.property.usd.prim_selection_payload
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni import ui
__all__: list = list()
class ContextMenu:
    def __init__(self):
        ...
    def on_mouse_event(self, event: ContextMenuEvent):
        ...
    def show_context_menu(self, objects: dict = None, menu_list: list = None, delegate = None):
        ...
class ContextMenuEvent:
    """
    The object compatible with ContextMenu
    """
    def __init__(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload, menu_items: list, xpos: int, ypos: int, delegate = None):
        ...
