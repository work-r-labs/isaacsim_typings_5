from __future__ import annotations
from isaacsim.gui.components.style import get_style
from omni import ui
import omni.ui._ui
__all__ = ['UIWidgetWrapper', 'get_style', 'ui']
class UIWidgetWrapper:
    """
    
        Base class for creating wrappers around any subclass of omni.ui.Widget in order to provide an easy interface
        for creating and managing specific types of widgets such as state buttons or file pickers.
        
    """
    enabled: bool
    visible: bool
    def __init__(self, container_frame: omni.ui._ui.Frame):
        ...
    def cleanup(self):
        """
        
                Perform any necessary cleanup
                
        """
    @property
    def container_frame(self) -> omni.ui._ui.Frame:
        ...
