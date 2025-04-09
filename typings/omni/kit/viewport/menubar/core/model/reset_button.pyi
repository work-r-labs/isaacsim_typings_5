from __future__ import annotations
import abc as abc
import carb as carb
from omni import ui
__all__ = ['ResetButton', 'ResetHelper', 'abc', 'carb', 'ui']
class ResetButton:
    """
    A button to reset value
    """
    def __init__(self, helpers: typing.Optional[typing.List[omni.kit.viewport.menubar.core.model.reset_button.ResetHelper]] = None, on_reset_fn: typing.Callable[[NoneType], NoneType] = None):
        """
        
                Constructor.
        
                Keyword Args:
                    helpers (Optional[List[ResetHelper]]): List for reset helper attached to this button, defaults to None.
                    on_reset_fn (Callable[[None], None]): Callback when button clicked, defaults to None.
                
        """
    def _build_ui(self):
        ...
    def _restore_defaults(self):
        ...
    def add_setting_model(self, helper: ResetHelper) -> None:
        """
        
                Add reset helper.
        
                Args:
                    helper (ResetHelper): Reset helper.
                
        """
    def refresh(self):
        """
        Refresh button status
        """
class ResetHelper:
    """
    
        A helper class for reset button.
        
    """
    def __init__(self, reset_button: typing.Optional[ForwardRef('ResetButton')] = None):
        """
        
                Constructor.
        
                Keyword Args:
                    reset_button (Optional["ResetButton"]): Reset button to attach, defaults to None.
                
        """
    def _update_reset_button(self):
        ...
    def get_default(self):
        """
        Get default value
        """
    def get_value(self):
        """
        Get current value
        """
    def restore_default(self):
        """
        Restore default value
        """
    def set_reset_button(self, button: ResetButton):
        """
        
                Attach to a reset button.
        
                Args:
                    button ("ResetButton"): Reset button to attach.
                
        """
