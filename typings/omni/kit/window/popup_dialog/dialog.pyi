from __future__ import annotations
import carb as carb
from omni.kit.window.popup_dialog.style import get_style
from omni import ui
import omni.ui._ui
import typing
__all__ = ['AbstractDialog', 'PopupDialog', 'carb', 'get_field_value', 'get_style', 'ui']
class AbstractDialog:
    pass
class PopupDialog(AbstractDialog):
    """
     Base class for a simple popup dialog with two primary buttons, OK and Cancel.
    """
    WINDOW_FLAGS: typing.ClassVar[int] = 67108874
    def __del__(self):
        ...
    def __init__(self, width: int = 400, parent: omni.ui._ui.Widget = None, title: str = None, ok_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, cancel_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType] = None, ok_label: str = 'Ok', cancel_label: str = 'Cancel', hide_title_bar: bool = False, modal: bool = False, warning_message: typing.Optional[str] = None):
        """
        
                Inherited args from the base class.
        
                Keyword Args:
                    width (int): Window width. Default 400.
                    title (str): Title to display. Default None.
                    ok_handler (Callable): Function to invoke when Ok button clicked. Function signature:
                        void okay_handler(dialog: PopupDialog)
                    cancel_handler (Callable):  Function to invoke when Cancel button clicked. Function
                        signature: void cancel_handler(dialog: PopupDialog)
                    ok_label (str): Alternative text to display on 'Accept' button. Default 'Ok'.
                    cancel_label (str): Alternative text to display on 'Cancel' button. Default 'Cancel'.
                    warning_message (Optional[str]): Warning message that will displayed in red with the warning glyph. Default None.
                    parent (omni.ui.Widget): OBSOLETE.
        
                
        """
    def _build_ok_cancel_buttons(self, disable_okay_button: bool = False, disable_cancel_button: bool = False):
        ...
    def _build_warning_message(self, glyph_width = 50, glyph_height = 100):
        ...
    def _build_widgets(self):
        ...
    def _build_window(self):
        ...
    def _cancel_handler(self, dialog):
        ...
    def _ok_handler(self, dialog):
        ...
    def _on_cancel(self):
        ...
    def _on_key_pressed(self, key, mod, pressed):
        ...
    def _on_okay(self):
        ...
    def destroy(self):
        """
         Destructor 
        """
    def hide(self):
        """
        Hides this dialog.
        """
    def set_cancel_clicked_fn(self, cancel_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType]):
        """
        
                Sets function to invoke when Cancel button is clicked.
        
                Args:
                    cancel_handler (Callable): Callback with signature: void cancel_handler(dialog: PopupDialog)
        
                
        """
    def set_okay_clicked_fn(self, ok_handler: typing.Callable[[omni.kit.window.popup_dialog.dialog.AbstractDialog], NoneType]):
        """
        
                Sets function to invoke when Okay button is clicked.
        
                Args:
                    ok_handler (Callable): Callback with signature: void okay_handler(dialog: PopupDialog)
        
                
        """
    def show(self, offset_x: int = 0, offset_y: int = 0, parent: omni.ui._ui.Widget = None, recreate_window: bool = False):
        """
        
                Shows this dialog, optionally offset from the parent widget, if any.
        
                Keyword Args:
                    offset_x (int): X offset. Default 0.
                    offset_y (int): Y offset. Default 0.
                    parent (ui.Widget): Offset from this parent widget. Default None.
                    recreate_window (bool): Recreate popup window. Default False.
        
                
        """
    @property
    def position_x(self):
        """
        
                Get position x of the dialog window.
                
                Returns:
                    int
                
        """
    @property
    def position_y(self):
        """
        
                Get position y of the dialog window.
                
                Returns:
                    int
                
        """
    @property
    def window(self):
        """
        
                Get the dialog window widget.
                
                Returns:
                    :obj:'omni.ui.window'
                
        """
def get_field_value(field: omni.ui._ui.AbstractField) -> typing.Union[str, int, float, bool]:
    """
    
        Returns value of the given field.
    
        Args:
            field (:obj:'ui.AbstractField'): Name of the field.
    
        Returns:
            Union[str, int, float, bool]
        
    """
