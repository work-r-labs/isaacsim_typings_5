"""

Context menu for group header classes.
"""
from __future__ import annotations
import typing
__all__: list = ['GroupHeaderContextMenuEvent', 'GroupHeaderContextMenuEvent', 'GroupHeaderContextMenu']
class GroupHeaderContextMenu:
    """
    
        Context menu for group headers.
        
    """
    _instance: typing.ClassVar[GroupHeaderContextMenu]  # value = <omni.kit.window.property.templates.header_context_menu.GroupHeaderContextMenu object>
    @classmethod
    def on_mouse_event(cls, event: GroupHeaderContextMenuEvent):
        """
        
                Mouse event received. Used to show context menu.
        
                Arg:
                    event (GroupHeaderContextMenuEvent): Mouse event
                
        """
    def __del__(self):
        ...
    def __init__(self):
        """
        Initialize function.
        """
    def _on_mouse_event(self, event: GroupHeaderContextMenuEvent):
        ...
    def destroy(self):
        """
        Destroy function. Class cleanup function.
        """
class GroupHeaderContextMenuEvent:
    """
    
        Right mouse click event sent by SimplePropertyWidget
        
    """
    def __init__(self, group_id: str, payload: typing.Any):
        """
        Initialize class function.
        
                Args:
                    group_id (str): Group identifier for event.
                    payload (Any): payload for event
                
        """
