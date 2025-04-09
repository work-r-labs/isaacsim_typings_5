from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_item import ViewportMenuItem
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenuItem
from omni.kit.viewport.menubar.core.viewport_menu_model import get_items
from omni.kit.viewport.menubar.core.viewport_menu_model import pop_from_scope
from omni.kit.viewport.menubar.core.viewport_menu_model import push_to_scope
from omni import ui
__all__: list = ['ViewportMenuContainer']
class ViewportMenuContainer(omni.kit.viewport.menubar.core.menu_item.viewport_menu_item.ViewportMenuItem):
    """
    A menu container within a viewport menubar.
    """
    def _ViewportMenuContainer__setup_hotkey_watching(self) -> None:
        ...
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self, *args, **kwargs):
        """
        
                Constructor.
        
                For args and keyword args, please refer to ViewportMenuItem.
                
        """
    def _clean(self):
        ...
    def _get_menu_item_hotkey_text(self, text: str) -> str:
        ...
    def _invalidate(self) -> None:
        ...
    def _on_hotkey_changed(self, event: carb.events._events.IEvent) -> None:
        ...
    def _on_hotkey_deregister(self, event: carb.events._events.IEvent) -> None:
        ...
    def build_fn(self, factory_args: typing.Dict):
        """
        
                Callback to build menu. Reimplement it to have own customized item.
        
                Args:
                    factory_args (dict): Argument related to viewport.
                
        """
    def destroy(self) -> None:
        """
        Release resources
        """
    @property
    def _children(self) -> typing.List[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem]:
        """
        All child items
        """
