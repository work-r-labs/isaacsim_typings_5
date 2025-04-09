from __future__ import annotations
from abc import abstractmethod
import asyncio as asyncio
import omni as omni
from omni.kit.widget.toolbar.context_menu import ContextMenuEvent
from omni import ui
__all__: list = ['WidgetGroup']
class WidgetGroup:
    """
    
        Base class to create a group of widgets on Toolbar
        
    """
    def __init__(self):
        ...
    def _acquire_toolbar_context(self):
        """
        
                Request toolbar to switch to current widget's context.
                
        """
    def _build_flyout_indicator(self, width, height, index: str, extension_id: str = 'omni.kit.widget.toolbar', padding = 7, min_menu_count = 2):
        ...
    def _invoke_context_menu(self, button_id: str, min_menu_entries: int = 1):
        """
        
                Function to invoke context menu.
        
                Args:
                    button_id: button_id of the context menu to be invoked.
                    min_menu_entries: minimal number of menu entries required for menu to be visible (default 1).
                
        """
    def _is_in_context(self):
        """
        
                Checks if the Toolbar is in default context or owned by current widget's context.
        
                Override this function if you want to customize the behavior.
        
                Returns:
                    True if toolbar is either in default context or owned by current widget.
                    False otherwise.
                
        """
    def _on_mouse_pressed(self, button, button_id: str, min_menu_entries: int = 2):
        """
        
                Function to handle flyout menu. Either with LMB long press or RMB click.
        
                Args:
                    button_id: button_id of the context menu to be invoked.
                    min_menu_entries: minimal number of menu entries required for menu to be visible (default 1).
                
        """
    def _on_mouse_released(self, button):
        ...
    def _release_toolbar_context(self):
        """
        
                Release the ownership of toolbar context and reset to default. If the ownership was preemptively taken by other owner, release does nothing.
                
        """
    def _schedule_show_menu(self, button_id: str, min_menu_entries: int = 2):
        ...
    def clean(self):
        """
        
                Clean up function to be called before destroying the object.
                
        """
    def create(self, default_size) -> dict[str, omni.ui._ui.Widget]:
        """
        
                Main function to creates widget.
                If you want to export widgets and allow external code to fetch and manipulate them, return a Dict[str, Widget] mapping from name to instance at the end of the function.
                
        """
    def get_style(self) -> dict:
        """
        
                Gets the style of all widgets defined in this Widgets group.
                
        """
    def on_added(self, context):
        """
        
                Called when widget is added to toolbar when calling Toolbar.add_widget
        
                Args:
                    context: the context used to add widget when calling Toolbar.add_widget.
                
        """
    def on_removed(self):
        """
        
                Called when widget is removed from toolbar when calling Toolbar.remove_widget
                
        """
    def on_toolbar_context_changed(self, context: str):
        """
        
                Called when toolbar's effective context has changed.
        
                Args:
                    context: new toolbar context.
                
        """
