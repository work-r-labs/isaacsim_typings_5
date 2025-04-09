from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.widget.toolbar.builtin_tools.builtin_tools import BuiltinTools
from omni.kit.widget.toolbar.commands import ToolbarPauseButtonClickedCommand
from omni.kit.widget.toolbar.commands import ToolbarPlayButtonClickedCommand
from omni.kit.widget.toolbar.commands import ToolbarPlayFilterCheckedCommand
from omni.kit.widget.toolbar.commands import ToolbarPlayFilterSelectAllCommand
from omni.kit.widget.toolbar.commands import ToolbarStopButtonClickedCommand
from omni.kit.widget.toolbar.context_menu import ContextMenu
from omni.kit.widget.toolbar.context_menu import ContextMenuEvent
from omni.kit.widget.toolbar.widget_group import WidgetGroup
from omni import ui
import typing as typing
__all__: list = ['Toolbar']
class Toolbar:
    """
    
        Main Toolbar class.
        
    """
    DEFAULT_CONTEXT: typing.ClassVar[str] = ''
    DEFAULT_CONTEXT_TOKEN: typing.ClassVar[int] = 0
    DEFAULT_SIZE: typing.ClassVar[int] = 38
    WINDOW_NAME: typing.ClassVar[str] = 'Main ToolBar'
    @staticmethod
    def _delayed_rebuild(*args, **kwargs):
        ...
    def _Toolbar__init_shades(self):
        """
        Style colors
        """
    def __init__(self):
        ...
    def _create_grab(self, axis):
        ...
    def _create_separator(self, axis):
        ...
    def _set_toolbar_dirty(self):
        ...
    def acquire_toolbar_context(self, context: str):
        """
        
                Request toolbar to switch to given context.
                It takes the context preemptively even if previous context owner has not release the context.
        
                Args:
                    context (str): Context to switch to.
        
                Returns:
                    A token to be used to release_toolbar_context
                
        """
    def add_custom_move_type(self, entry_name: str, move_type: str):
        ...
    def add_custom_select_type(self, entry_name: str, selection_types: list):
        ...
    def add_widget(self, widget_group: omni.kit.widget.toolbar.widget_group.WidgetGroup, priority: int, context: str = ''):
        """
        
                Adds a WidgetGroup instance to the Toolbar.
        
                Args:
                    widget_group (WidgetGroup): The WidgetGroup instance to be added to the Toolbar.
                    priority (int): priority of the WidgetGroup. With a smaller number the WidgetGroup will be shown on Toolbar first.
                    context (str): A context the WidgetGroup is associated with.
                
        """
    def destroy(self):
        ...
    def get_context(self):
        """
        
                Gets the current context of the Toolbar.
                
        """
    def get_widget(self, name: str) -> omni.ui._ui.Widget:
        """
        
                Gets a ui.Widget item by its name.
        
                Args:
                    name (str): The name of widget to fetch.
        
                Returns:
                    The ui.Widget associated with such name. None if not found.
                
        """
    def rebuild_toolbar(self, root_frame = None):
        ...
    def release_toolbar_context(self, token: int):
        """
        
                Request toolbar to release context associated with token.
                If token is expired (already released or context ownership taken by others), this function does nothing.
        
                Args:
                    token (int): Context token to release.
                
        """
    def remove_custom_move(self, entry_name: str):
        ...
    def remove_custom_select(self, entry_name):
        ...
    def remove_widget(self, widget_group: omni.kit.widget.toolbar.widget_group.WidgetGroup):
        """
        
                Removes a WidgetGroup instance from the Toolbar.
        
                Args:
                    widget_group (WidgetGroup): The WidgetGroup instance to be removed from the Toolbar.
                
        """
    def set_axis(self, axis: omni.ui._ui.ToolBarAxis):
        """
        
                Sets the axis direction of the Toolbar
        
                Args:
                    axis (ui.ToolBarAxis). ui.ToolBarAxis.X for horizontal toolbar and ui.ToolBarAxis.Y for vertical.
                
        """
    def subscribe_grab_mouse_pressed(self, function: typing.Callable[[int, ForwardRef('weakref.ref')], NoneType]):
        ...
    @property
    def context_menu(self):
        ...
GRAB_ENABLED_SETTING_PATH: str = '/exts/omni.kit.widget.toolbar/Grab/enabled'
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
