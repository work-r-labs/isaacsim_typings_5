from __future__ import annotations
import asyncio as asyncio
from collections import namedtuple
from omni.kit.async_engine.async_engine import run_coroutine
import omni.kit.window.popup_dialog.dialog
from omni.kit.window.popup_dialog.dialog import AbstractDialog
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni.kit.window.popup_dialog.dialog import get_field_value
from omni.kit.window.popup_dialog.style import get_style
from omni import ui
import omni.ui._ui
__all__: list = ['FormDialog', 'FormWidget']
class FormDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    
        A simple popup dialog with a set of input fields and two buttons, OK and Cancel
    
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
            field_defs ([FormDialog.FieldDef]): List of FieldDefs. Default [].
            input_width (int): OBSOLETE.
    
        Note:
            FormDialog.FieldDef: 
                A namedtuple of (name, label, type, default value) for describing the input field,
                e.g. FormDialog.FieldDef("name", "Name:  ", omni.ui.StringField, "Bob").
    
        
    """
    FieldDef = FormDialogFieldDef
    def __init__(self, width: int = 400, parent: omni.ui._ui.Widget = None, message: str = None, title: str = None, ok_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, cancel_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, ok_label: str = 'Ok', cancel_label: str = 'Cancel', field_defs: typing.List[omni.kit.window.popup_dialog.form_dialog.FormDialogFieldDef] = None, input_width: int = 250):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def get_field(self, name: str) -> omni.ui._ui.AbstractField:
        """
        
                Returns widget corresponding to named field.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    omni.ui.AbstractField
        
                
        """
    def get_value(self, name: str) -> typing.Union[str, int, float, bool]:
        """
        
                Returns value of the named field.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    Union[str, int, float, bool]
        
                Note:
                    Doesn't currently return MultiFields correctly.
        
                
        """
    def get_values(self) -> dict:
        """
        
                Returns all values in a dict.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    dict
        
                Note:
                    Doesn't currently return MultiFields correctly.
        
                
        """
    def reset_values(self):
        """
        Resets all values to their defaults.
        """
    def show(self, offset_x: int = 0, offset_y: int = 0, parent: omni.ui._ui.Widget = None):
        """
        
                Shows this dialog, optionally offset from the parent widget, if any.
        
                Keyword Args:
                    offset_x (int): X offset. Default 0.
                    offset_y (int): Y offset. Default 0.
                    parent (ui.Widget): Offset from this parent widget. Default None.
        
                
        """
class FormWidget:
    """
    
        A simple form widget with a set of input fields. As opposed to the dialog class, the widget can be combined 
        with other widget types in the same window.
    
        Keyword Args:
            message (str): Message string.
            field_defs ([FormDialog.FieldDef]): List of FieldDefs. Default [].
    
        Note:
            FormDialog.FieldDef: 
                A namedtuple of (name, label, type, default value) for describing the input field,
                e.g. FormDialog.FieldDef("name", "Name:  ", omni.ui.StringField, "Bob").
    
        
    """
    def __init__(self, message: str = None, field_defs: typing.List[omni.kit.window.popup_dialog.form_dialog.FormDialogFieldDef] = list()):
        ...
    def _build_ui(self, message: str, field_defs: typing.List[omni.kit.window.popup_dialog.form_dialog.FormDialogFieldDef]):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def focus(self) -> None:
        """
        Focus fields for the current widget.
        """
    def get_field(self, name: str) -> omni.ui._ui.AbstractField:
        """
        
                Returns widget corresponding to named field.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    omni.ui.AbstractField
        
                
        """
    def get_value(self, name: str) -> typing.Union[str, int, float, bool]:
        """
        
                Returns value of the named field.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    Union[str, int, float, bool]
        
                Note:
                    Doesn't currently return MultiFields correctly.
        
                
        """
    def get_values(self) -> dict:
        """
        
                Returns all values in a dict.
        
                Args:
                    name (str): Name of the field.
        
                Returns:
                    dict
        
                Note:
                    Doesn't currently return MultiFields correctly.
        
                
        """
    def reset_values(self):
        """
        Resets all values to their defaults.
        """
