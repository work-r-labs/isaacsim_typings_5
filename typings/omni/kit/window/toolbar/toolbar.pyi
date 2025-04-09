from __future__ import annotations
import asyncio as asyncio
from functools import lru_cache
from functools import partial
import omni as omni
from omni.kit.menu.utils.extension_window_helper import MenuHelperExtension
from omni.kit.widget.toolbar.builtin_tools.builtin_tools import BuiltinTools
from omni.kit.widget.toolbar.commands import ToolbarPauseButtonClickedCommand
from omni.kit.widget.toolbar.commands import ToolbarPlayButtonClickedCommand
from omni.kit.widget.toolbar.commands import ToolbarPlayFilterCheckedCommand
from omni.kit.widget.toolbar.commands import ToolbarPlayFilterSelectAllCommand
from omni.kit.widget.toolbar.commands import ToolbarStopButtonClickedCommand
from omni.kit.widget.toolbar.context_menu import ContextMenu
from omni.kit.widget.toolbar.context_menu import ContextMenuEvent
from omni.kit.widget.toolbar.extension import get_instance as _get_widget_instance
from omni.kit.widget.toolbar.widget_group import WidgetGroup
from omni import ui
import pathlib
from pathlib import Path
import typing
import weakref as weakref
__all__ = ['BuiltinTools', 'ContextMenu', 'ContextMenuEvent', 'DATA_PATH', 'MenuHelperExtension', 'Path', 'Toolbar', 'ToolbarPauseButtonClickedCommand', 'ToolbarPlayButtonClickedCommand', 'ToolbarPlayFilterCheckedCommand', 'ToolbarPlayFilterSelectAllCommand', 'ToolbarStopButtonClickedCommand', 'WidgetGroup', 'asyncio', 'get_instance', 'lru_cache', 'omni', 'partial', 'ui', 'weakref']
class Toolbar(omni.ext._extensions.IExt, omni.kit.menu.utils.extension_window_helper.MenuHelperExtension):
    MENU_GROUP: typing.ClassVar[str] = 'Window'
    WINDOW_NAME: typing.ClassVar[str] = 'Main ToolBar'
    @staticmethod
    def _dock():
        ...
    def _Toolbar__on_grab_mouse_pressed(self, x, y, button, *args, **kwargs):
        ...
    def __init__(self):
        ...
    def _menu_hide_toolbar(self, objects):
        ...
    def _on_axis_changed(self, axis):
        ...
    def _rebuild_toolbar(self):
        ...
    def _register_context_menu(self):
        ...
    def _show_hide_window(self, menu, value):
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
    def add_custom_select_type(self, entry_name: str, selection_types: list):
        ...
    def add_widget(self, widget_group: WidgetGroup, priority: int, context: str = ''):
        ...
    def create_main_toolbar(self):
        ...
    def get_context(self):
        ...
    def get_widget(self, name: str):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def release_toolbar_context(self, token: int):
        """
        
                Request toolbar to release context associated with token.
                If token is expired (already released or context ownership taken by others), this function does nothing.
        
                Args:
                    token (int): Context token to release.
                
        """
    def remove_custom_select(self, entry_name):
        ...
    def remove_widget(self, widget_group: WidgetGroup):
        ...
    @property
    def context_menu(self):
        ...
def get_instance():
    ...
DATA_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.toolbar-1.6.2+d02c707b/data')
_toolbar_instance: Toolbar  # value = <omni.kit.window.toolbar.toolbar.Toolbar object>
