from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__: list = ['is_window_hovered', 'get_hovered_window']
def get_hovered_window(pos_x: float, pos_y: float) -> typing.Optional[str]:
    """
    
        Get first window under mouse.
    
        Args:
            pos_x (float): X position.
            pos_y (float): Y position.
    
        Return None if nothing found.
        If multiple window found, float window first. If multiple float window, just first result
        
    """
def is_window_hovered(pos_x: float, pos_y: float, window: omni.ui._ui.Window) -> bool:
    """
    
        Check if window under mouse position.
        Args:
            pos_x (float): X position.
            pos_y (float): Y position.
            window (ui.Window): Window to check.
        
    """
EXCLUDE_WINDOWS: list = ['Debug##Default']
