from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__ = ['SeparatorDelegate', 'ui']
class SeparatorDelegate(omni.ui._ui.MenuDelegate):
    """
     A menu delegate that creates separator between items within a viewport menubar
    """
    def __del__(self):
        ...
    def __init__(self):
        """
        Constructor
        """
    def build_item(self, item: omni.ui._ui.MenuItem) -> None:
        """
        
                Build a line as separator.
        
                Args:
                    item (ui.MenuItem): Menu item.
                
        """
    def destroy(self) -> None:
        """
        Release resources
        """
