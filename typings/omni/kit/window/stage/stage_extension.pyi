from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.menu.utils.extension_window_helper import MenuHelperExtension
from omni.kit.window.stage.stage_window import StageWindow
from omni import ui
import typing
__all__: list = ['StageExtension']
class StageExtension(omni.ext._extensions.IExt, omni.kit.menu.utils.extension_window_helper.MenuHelperExtension):
    """
    The entry point for Stage Window
    """
    MENU_GROUP: typing.ClassVar[str] = 'Window'
    WINDOW_NAME: typing.ClassVar[str] = 'Stage'
    def _destroy_window_async(self):
        ...
    def _visiblity_changed_fn(self, visible):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
    def show_window(self, value):
        ...
