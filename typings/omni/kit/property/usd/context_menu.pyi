from __future__ import annotations
import carb as carb
import omni.kit.property.usd.prim_selection_payload
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from omni import ui
__all__: list = list()
class ContextMenu:
    """
    
        Context menu.
        
    """
    def __init__(self):
        """
        
                Initialize the context menu.
                
        """
    def on_mouse_event(self, event: ContextMenuEvent):
        """
        
                On mouse event.
        
                Args:
                    event (ContextMenuEvent): The event.
                
        """
    def show_context_menu(self, objects: dict = None, menu_list: list = None, delegate = None):
        """
        
                Shows the context menu.
        
                Args:
                    objects (dict): The objects to pass to the context menu.
                    menu_list (list): The menu list to pass to the context menu.
                
        """
class ContextMenuEvent:
    """
    The object compatible with ContextMenu
    """
    def __init__(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload, menu_items: list, xpos: int, ypos: int, delegate = None):
        ...
