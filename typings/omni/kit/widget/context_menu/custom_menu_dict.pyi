from __future__ import annotations
import carb as carb
import copy as copy
from omni.kit.widget.context_menu.singleton import Singleton
import typing
__all__ = ['ContextMenuEventType', 'Singleton', 'add_menu', 'carb', 'copy', 'get_menu_dict', 'get_menu_event_stream', 'merge_menus']
class ContextMenuEventType:
    """
    
        Event sent when menus are added or removed
        
    """
    ADDED: typing.ClassVar[int] = 0
    REMOVED: typing.ClassVar[int] = 1
def add_menu(menu_dict, index: str = 'MENU', extension_id: str = ''):
    """
    Add custom menu to any context_menu
    
        Examples
            menu = {"name": "Open in Material Editor", "onclick_fn": open_material}
            # add to all context menus
            self._my_custom_menu = omni.kit.context_menu.add_menu(menu, "MENU", "")
            # add to omni.kit.widget.stage context menu
            self._my_custom_menu = omni.kit.context_menu.add_menu(menu, "MENU", "omni.kit.widget.stage")
    
        Args:
            menu_dict: a dictionary containing menu settings. See ContextMenuExtension docs for information on values
            index: name of the menu EG. "MENU"
            extension_id: name of the target EG. "" or "omni.kit.widget.stage"
    
        NOTE: index and extension_id are extension arbitrary values. add_menu(menu, "MENU", "omni.kit.widget.stage") works
              as omni.kit.widget.stage retrieves custom context_menus with get_menu_dict("MENU", "omni.kit.widget.stage")
              Adding a menu to an extension that doesn't support context_menus would have no effect.
    
        Returns:
            (MenuSubscription): A MenuSubscription, keep a copy of this as the custom menu will be removed when `release()`
              is explicitly called or this is garbage collected.
        
    """
def get_menu_dict(index: str = 'MENU', extension_id: str = '') -> typing.List[dict]:
    """
    Get custom menus
    
        see add_menu for dictionary info
    
        Args:
            index (str): name of the menu
            extension_id (str): name of the target
    
        Returns:
            (list): a list of dictionaries containing custom menu settings. See ContextMenuExtension docs for information on values
        
    """
def get_menu_event_stream():
    """
    
        Gets menu event stream.
    
        Returns:
            (IEventStream): Event stream.
        
    """
def merge_menus(menu_list: list) -> typing.List[dict]:
    """
    Merge custom menus
    
        Args:
            menu_list (list): list of dictionaries
    
        Returns:
            (list): a list of dictionaries containing custom menu settings. See ContextMenuExtension docs for information on values
        
    """
