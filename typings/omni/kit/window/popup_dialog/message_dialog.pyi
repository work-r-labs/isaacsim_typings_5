from __future__ import annotations
import omni.kit.window.popup_dialog.dialog
from omni.kit.window.popup_dialog.dialog import AbstractDialog
from omni.kit.window.popup_dialog.dialog import PopupDialog
from omni.kit.window.popup_dialog.style import get_style
from omni import ui
import omni.ui._ui
__all__ = ['AbstractDialog', 'MessageDialog', 'MessageWidget', 'PopupDialog', 'get_style', 'ui']
class MessageDialog(omni.kit.window.popup_dialog.dialog.PopupDialog):
    """
    
        This simplest of all popup dialogs displays a confirmation message before executing an action.
            
        Keyword Args:
            width (int): Width of popup window. Default 400.
            parent (:obj:'omni.ui.Widget'):OBSOLETE.
            message (str): The displayed message. Default ''.
            title (str): Title of popup window. Default None.
            ok_handler (Callable[[AbstractDialog], None]): Handler called when click ok button. Default None.
                        Function signature is: void ok_handler(AbstractDialog)
            cancel_handler (Callable[[AbstractDialog], None]): Handler called when click cancel button. Default None.
                        Function signature is: void ok_handler(AbstractDialog)
            ok_label (str): Label text for ok button. Default "Ok".
            cancel_label (str): Label text for cancel button. Default "Cancel".
            disable_okay_button (bool): If True, then don't display 'Ok' button. Default False.
            disable_cancel_button (bool): If True, then don't display 'Cancel' button. Default False.
            warning_message (Optional[str]): Warning message that will displayed in red with the warning glyph. Default None.
        
    """
    def __init__(self, width: int = 400, parent: omni.ui._ui.Widget = None, message: str = '', title: str = None, ok_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, cancel_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, ok_label: str = 'Ok', cancel_label: str = 'Cancel', disable_okay_button: bool = False, disable_cancel_button: bool = False, warning_message: typing.Optional[str] = None):
        ...
    def destroy(self):
        ...
    def set_message(self, message: str):
        """
        
                Updates the message string.
        
                Args:
                    message (str): The message string.
        
                
        """
class MessageWidget:
    """
    
        This widget displays a custom message. As opposed to the dialog class, the widget can be combined 
        with other widget types in the same window.
    
        Keyword Args:
            message (str): The message string
    
        
    """
    def __init__(self, message: str = ''):
        ...
    def _build_ui(self, message: str):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def set_message(self, message: str):
        """
        
                Updates the message string.
        
                Args:
                    message (str): The message string.
        
                
        """
