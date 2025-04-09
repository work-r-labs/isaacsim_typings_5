from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.window.popup_dialog.dialog import AbstractDialog
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni.kit.window.popup_dialog.dialog import get_field_value
from omni.kit.window.popup_dialog.style import get_style
from omni import ui
__all__ = ['AbstractDialog', 'InputDialog', 'InputWidget', 'PopupDialog', 'asyncio', 'get_field_value', 'get_style', 'omni', 'ui']
class InputDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    
        A simple popup dialog with an input field and two buttons, OK and Cancel
    
        Keyword Args:
            width (int): Width of popup window. Default 400.
            parent (:obj:'omni.ui.Widget'):OBSOLETE.
            message (str): Message to display.
            title (str): Title of popup window.  Default None.
            ok_handler (Callable[[AbstractDialog], None]): Handler called when click ok button. Default None.
                        Function signature is: void ok_handler(AbstractDialog)
            cancel_handler (Callable[[AbstractDialog], None]): Handler called when click cancel button. Default None.
                        Function signature is: void ok_handler(AbstractDialog)
            ok_label (str): Label text for ok button. Default "Ok".
            cancel_label (str): Label text for cancel button. Default "Cancel".
            input_cls (omni.ui.AbstractField): Type of input field specified by class name, e.g.
                omni.ui.StringField, omni.ui.IntField, omni.ui.CheckBox. Default is omni.ui.StringField.
            pre_label (str): Text displayed before input field. Default None.
            post_label (str): Text displayed after input field. Default None.
            default_value (str): Default value of the input field.
            warning_message (Optional[str]): Warning message that will displayed in red with the warning glyph. Default None.
    
        
    """
    def __init__(self, width: int = 400, parent: omni.ui._ui.Widget = None, message: str = None, title: str = None, ok_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, cancel_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, ok_label: str = 'Ok', cancel_label: str = 'Cancel', input_cls: omni.ui._ui.AbstractField = None, pre_label: str = None, post_label: str = None, default_value: str = None, warning_message: typing.Optional[str] = None):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def get_value(self) -> typing.Any:
        """
        
                Returns field value.
        
                Returns:
                    Any, e.g. one of [str, int, float, bool]
        
                
        """
class InputWidget:
    """
    
        A simple widget with an input field. As opposed to the dialog class, the widget can be combined 
        with other widget types in the same window.
    
        Keyword Args:
            message (str): Message to display.
            input_cls (omni.ui.AbstractField): Class of the input field, e.g.
                omni.ui.StringField, omni.ui.IntField, omni.ui.CheckBox. Default is omni.ui.StringField.
            pre_label (str): Text displayed before input field. Default None.
            post_label (str): Text displayed after input field. Default None.
            default_value (str): Default value of the input field.
    
        
    """
    def __init__(self, message: str = None, input_cls: omni.ui._ui.AbstractField = None, pre_label: str = None, post_label: str = None, default_value: typing.Any = None):
        ...
    def _build_ui(self, message: str, input_cls: omni.ui._ui.AbstractField, pre_label: str, post_label: str, default_value: typing.Any):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def get_value(self) -> typing.Any:
        """
        
                Returns value of input field.
        
                Returns:
                    Any
                
        """
