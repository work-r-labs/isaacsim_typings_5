from __future__ import annotations
import omni as omni
from omni.kit.widget.toolbar.hotkey import Hotkey
from omni.kit.widget.toolbar.widget_group import WidgetGroup
import weakref as weakref
__all__: list = ['SimpleToolButton']
class SimpleToolButton(omni.kit.widget.toolbar.widget_group.WidgetGroup):
    """
    
        A helper class to create simple WidgetGroup that contains only one ToolButton.
    
        Args:
            name: Name of the ToolButton.
            tooltip: Tooltip of the ToolButton.
            icon_path: The icon to be used when button is not checked.
            icon_checked_path: The icon to be used when button is checked.
            hotkey: HotKey to toggle the button (optional).
            toggled_fn: Callback function when button is toggled. Signature: on_toggled(checked) (optional).
            model: Model for the ToolButton (optional).
            additional_style: Additional styling to apply to the ToolButton (optional).
        
    """
    def __init__(self, name, tooltip, icon_path, icon_checked_path, hotkey = None, toggled_fn = None, model = None, additional_style = None):
        ...
    def _on_hotkey(self):
        ...
    def clean(self):
        ...
    def create(self, default_size):
        ...
    def get_style(self):
        ...
    def get_tool_button(self):
        ...
