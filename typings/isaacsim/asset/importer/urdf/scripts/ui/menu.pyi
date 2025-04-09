from __future__ import annotations
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
__all__ = ['MenuItemDescription', 'make_menu_item_description', 'omni']
def make_menu_item_description(ext_id: str, name: str, onclick_fun, action_name: str = '') -> None:
    """
    Easily replace the onclick_fn with onclick_action when creating a menu description
    
        Args:
            ext_id (str): The extension you are adding the menu item to.
            name (str): Name of the menu item displayed in UI.
            onclick_fun (Function): The function to run when clicking the menu item.
            action_name (str): name for the action, in case ext_id+name don't make a unique string
    
        Note:
            ext_id + name + action_name must concatenate to a unique identifier.
    
        
    """
