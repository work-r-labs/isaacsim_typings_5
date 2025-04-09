"""
Actions Omniverse Kit API (deprecated)

Module to work with **Actions** in the Kit. It is built on top of ``carb.input`` system that features action mapping logic.

this is deprecated as its old get_editor_menu().add_action_to_menu(..) and nothing todo with omni.kit.actions
"""
from __future__ import annotations
__all__ = ['ActionMenuSubscription', 'add_action_to_menu']
class ActionMenuSubscription:
    """
    
        Action menu subscription wrapper to make it scoped (auto unsubscribe on del) (deprecated)
        
    """
    def __del__(self):
        ...
    def __init__(self, _on_del: typing.Callable):
        ...
    def unsubscribe(self):
        ...
def add_action_to_menu(menu_path: str, on_action: typing.Callable, action_name: str = None, default_hotkey: typing.Tuple[int, int] = None, on_rmb_click: typing.Callable = None) -> ActionMenuSubscription:
    """
    
        Add action to menu path. (deprecated)
    
        This function binds passed callable `on_action` function with :mod:`carb.input` action and a menu path together. If
        `default_hotkey` is provided it is set into settings and appears on the menu.
    
        Args:
            menu_path: menu path. E.g. "File/Open".
            on_action: function to be called as an action.
            on_rmb_click: function to be called when right mouse button clicked.
            action_name: action name. If not provided menu path is used as action, where all '/' are replaced with '-'.
            default_hotkey(tuple(int, :class:`carb.input.KeyboardInput`)): modifier and key tuple to associate with given action.
    
        Returns:
            Subscription holder object. Action is removed when this object is destroyed.
        
    """
