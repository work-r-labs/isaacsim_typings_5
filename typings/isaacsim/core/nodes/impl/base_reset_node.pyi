from __future__ import annotations
import carb as carb
import omni as omni
__all__ = ['BaseResetNode', 'carb', 'omni']
class BaseResetNode:
    """
    
        Base class for nodes that automatically reset when stop is pressed.
        
    """
    def __init__(self, initialize = False):
        ...
    def custom_reset(self):
        ...
    def on_stop_play(self, event: carb.events._events.IEvent):
        ...
    def reset(self):
        ...
