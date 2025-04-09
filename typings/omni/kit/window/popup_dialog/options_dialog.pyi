from __future__ import annotations
from collections import namedtuple
import omni.kit.window.popup_dialog.dialog
from omni.kit.window.popup_dialog.dialog import AbstractDialog
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni.kit.window.popup_dialog.style import get_style
from omni import ui
import omni.ui._ui
import pathlib
__all__ = ['AbstractDialog', 'ICON_PATH', 'OptionsDialog', 'OptionsWidget', 'PopupDialog', 'get_style', 'namedtuple', 'ui']
class OptionsDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    
        A simple checkbox dialog with a set options and two buttons, OK and Cancel
    
        Keyword Args:
            width (int): Width of popup window. Default 400.
            parent (:obj:'omni.ui.Widget'):OBSOLETE.
            message (str): Message string.
            title (str): Title of popup window. Default None.
            ok_handler (Callable[[AbstractDialog], None]): Handler called when click ok button. Default None.
                        Function signature is: void ok_handler(AbstractDialog)
            cancel_handler (Callable[[AbstractDialog], None]): Handler called when click cancel button. Default None.
                        Function signature is: void ok_handler(AbstractDialog)
            ok_label (str): Label text for ok button. Default "Ok".
            cancel_label (str): Label text for cancel button. Default "Cancel".
            field_defs ([OptionsDialog.FieldDef]): List of FieldDefs. Default [].
            value_changed_fn (Callable): This callback is triggered on any value change.
            radio_group (bool): If True, then only one option can be selected at a time.
    
        Note:
            OptionsDialog.FieldDef: 
                A namedtuple of (name, label, default) for describing the options field,
                e.g. OptionsDialog.FieldDef("option", "Option", True).
    
        
    """
    FieldDef = OptionsDialogFieldDef
    def __init__(self, width: int = 400, parent: omni.ui._ui.Widget = None, message: str = None, title: str = None, ok_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, cancel_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, ok_label: str = 'Ok', cancel_label: str = 'Cancel', field_defs: typing.List[omni.kit.window.popup_dialog.options_dialog.OptionsDialogFieldDef] = None, value_changed_fn: typing.Callable = None, radio_group: bool = False):
        ...
    def destroy(self):
        ...
    def get_choice(self) -> str:
        """
        
                Returns name of chosen option.
        
                Returns:
                    str
        
                
        """
    def get_value(self, name: str) -> bool:
        """
        
                Returns value of the named field.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    bool
        
                
        """
    def get_values(self) -> typing.Dict:
        """
        
                Returns all values in a dictionary.
        
                Returns:
                    Dict
        
                
        """
class OptionsWidget:
    """
    
        A simple checkbox widget with a set options. As opposed to the dialog class, the widget can be combined 
        with other widget types in the same window.
    
        Keyword Args:
            message (str): Message string.
            field_defs ([OptionsDialog.FieldDef]): List of FieldDefs. Default [].
            value_changed_fn (Callable): This callback is triggered on any value change.
            radio_group (bool): If True, then only one option can be selected at a time.
    
        Note:
            OptionsDialog.FieldDef: 
                A namedtuple of (name, label, default) for describing the options field,
                e.g. OptionsDialog.FieldDef("option", "Option", True).
    
        
    """
    def __init__(self, message: str = None, field_defs: typing.List[omni.kit.window.popup_dialog.options_dialog.OptionsDialogFieldDef] = list(), value_changed_fn: typing.Callable = None, radio_group: bool = False):
        ...
    def _build_ui(self, message: str, field_defs: typing.List[omni.kit.window.popup_dialog.options_dialog.OptionsDialogFieldDef], value_changed_fn: typing.Callable, radio_group: typing.Optional[omni.ui._ui.RadioCollection]):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def get_choice(self) -> str:
        """
        
                Returns name of chosen option.
        
                Returns:
                    str
        
                
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
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.popup_dialog-2.0.24+d02c707b/icons/NvidiaDark')
