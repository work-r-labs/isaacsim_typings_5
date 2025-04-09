"""

omni.kit.window.property managed_frame functions. This provides persistent open/closed states for ui.CollapsableFrames
"""
from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__: list = ['prep', 'set_collapsed_state', 'get_collapsed_state', 'reset_collapsed_state']
def get_collapsed_state(index_name: str = None):
    """
    Get current collapsed state for `index_name`.
    
        Args:
            index_name (str): group name of the frame.
    
        Returns:
            dict: collapsed settings dictionary.
        
    """
def prep(frame: omni.ui._ui.CollapsableFrame, group_name: str):
    """
    Update ui.CollapsableFrame and insert hooks so collapsed state can be tracked.
    
        Args:
            frame (ui.CollapsableFrame): frame to be prepared.
            group_name (str): group name of the frame.
        
    """
def reset_collapsed_state():
    """
    Reset collapsed state data, so default will be used.
    """
def set_collapsed_state(index_name: str, state: bool):
    """
    Set new collapsed state.
    
        Args:
            index_name (str): group name of the frame.
            state (bool): new collapsed state of the frame.
        
    """
collapsed_settings: dict = {}
