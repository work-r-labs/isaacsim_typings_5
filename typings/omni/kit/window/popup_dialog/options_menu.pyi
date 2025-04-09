from __future__ import annotations
from collections import namedtuple
import omni.kit.window.popup_dialog.dialog
from omni.kit.window.popup_dialog.dialog import AbstractDialog
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni.kit.window.popup_dialog.options_dialog import OptionsWidget
from omni.kit.window.popup_dialog.style import get_style
from omni import ui
import omni.ui._ui
__all__ = ['AbstractDialog', 'OptionsMenu', 'OptionsMenuWidget', 'OptionsWidget', 'PopupDialog', 'get_style', 'namedtuple', 'ui']
class OptionsMenu(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    
        A simple checkbox menu with a set of options
    
        Keyword Args:
            title (str): Title of this menu. Default None.
            field_defs ([OptionsMenu.FieldDef]): List of FieldDefs. Default [].
            value_changed_fn (Callable): This callback is triggered on any value change.
    
        Note:
            OptionsMenu.FieldDef: 
                A namedtuple of (name, label, glyph, default) for describing the options field,
                e.g. OptionsDialog.FieldDef("option", "Option", None, True).
    
        
    """
    FieldDef = OptionsMenuFieldDef
    def __init__(self, width: int = 400, parent: omni.ui._ui.Widget = None, title: str = None, ok_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, cancel_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, ok_label: str = 'Ok', cancel_label: str = 'Cancel', field_defs: typing.List[omni.kit.window.popup_dialog.options_menu.OptionsMenuFieldDef] = None, value_changed_fn: typing.Callable = None):
        ...
    def _build_widgets(self):
        ...
    def destroy(self):
        """
        Destructor
        """
    def get_value(self, name: str) -> bool:
        """
        
                Returns value of the named field.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    bool
        
                
        """
    def get_values(self) -> dict:
        """
        
                Returns all values in a dictionary.
        
                Returns:
                    dict
        
                
        """
    def reset_values(self):
        """
        Resets all values to their defaults.
        """
    def set_value(self, name: str, value: bool):
        """
        
                Sets the value of the named field.
        
                Args:
                    name (str): Name of the field.
                    value (bool): New value
        
                
        """
class OptionsMenuWidget:
    """
    
        A simple checkbox widget with a set of options. As opposed to the menu class, the widget can be combined 
        with other widget types in the same window.
    
        Keyword Args:
            title (str): Title of this menu. Default None.
            field_defs ([OptionsDialog.FieldDef]): List of FieldDefs. Default [].
            value_changed_fn (Callable): This callback is triggered on any value change.
            build_ui (bool): Build ui when created.
    
        Note:
            OptionsMenu.FieldDef: 
                A namedtuple of (name, label, glyph, default) for describing the options field,
                e.g. OptionsDialog.FieldDef("option", "Option", None, True).
    
        
    """
    def __init__(self, title: str = None, field_defs: typing.List[omni.kit.window.popup_dialog.options_menu.OptionsMenuFieldDef] = list(), value_changed_fn: typing.Callable = None, build_ui: bool = True):
        ...
    def build_ui(self):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def get_value(self, name: str) -> bool:
        """
        
                Returns value of the named field.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    bool
        
                
        """
    def get_values(self) -> dict:
        """
        
                Returns all values in a dictionary.
        
                Returns:
                    dict
        
                
        """
    def reset_values(self):
        """
        Resets all values to their defaults.
        """
    def set_value(self, name: str, value: bool):
        """
        
                Sets the value of the named field.
        
                Args:
                    name (str): Name of the field.
                    value (bool): New value
        
                
        """
