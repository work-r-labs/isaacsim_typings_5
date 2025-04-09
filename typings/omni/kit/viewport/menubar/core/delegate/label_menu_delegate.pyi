from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__ = ['LabelMenuDelegate', 'ui']
class LabelMenuDelegate(omni.ui._ui.MenuDelegate):
    """
    A menu delegate that creates a label within a viewport menubar.
    """
    def __init__(self, enabled: bool = True, width: typing.Optional[omni.ui._ui.Length] = None, height: omni.ui._ui.Length = 26, alignment: omni.ui._ui.Alignment = ...):
        """
        
                Constructor.
        
                Keyword Args:
                    enable (bool):Delegate enabled state, defaults to True.
                    width (ui.Length): Label width, defaults to None means ui.Fraction(1).
                    height (ui.Length): Label height, defaults to 26 pixels.
                    alignment (ui.Alignment): Label alignment, defaults to ui.Alignment.CENTER.
                
        """
    def build_item(self, item: omni.ui._ui.MenuItem) -> None:
        """
        
                Build a label.
        
                Args:
                    item (ui.MenuItem): Menu item.
                
        """
