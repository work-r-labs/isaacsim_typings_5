from __future__ import annotations
import omni.kit.viewport.menubar.core.menu_item.viewport_menu_item
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_item import ViewportMenuItem
from omni.kit.viewport.menubar.core.menu_item.viewport_menubar_item import ViewportMenubar
from omni import ui
import weakref as weakref
__all__: list = ['MenuBarViewportLayer']
class MenuBarViewportLayer:
    def __init__(self, factory_args, *ui_args, **ui_kwargs):
        ...
    def _build_fn(self):
        ...
    def _menu_changed(self, model: <function singleton.<locals>.getinstance at 0x709ef21dcca0>, item: omni.kit.viewport.menubar.core.menu_item.viewport_menu_item.ViewportMenuItem) -> None:
        ...
    def destroy(self):
        ...
    @property
    def categories(self):
        ...
    @property
    def layers(self):
        ...
    @property
    def name(self):
        ...
    @property
    def visible(self):
        ...
    @visible.setter
    def visible(self, visible: bool):
        ...
