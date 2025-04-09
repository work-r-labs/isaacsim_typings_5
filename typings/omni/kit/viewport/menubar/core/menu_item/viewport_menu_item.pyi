from __future__ import annotations
import omni.kit.viewport.menubar.core.viewport_menu_model
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenuItem
from omni import ui
import omni.ui._ui
__all__: list = ['ViewportMenuItem']
class ViewportMenuItem(omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem):
    """
    A general menu item within a viewport menubar
    """
    def __init__(self, name: str = '', icon: str = '', hide_on_click: bool = True, appear_after: str = '', onclick_fn: typing.Optional[typing.Callable] = None, delegate: typing.Optional[omni.ui._ui.MenuDelegate] = None, visible_setting_path: typing.Optional[str] = None, order_setting_path: typing.Optional[str] = None, expand_setting_path: typing.Optional[str] = None, style: typing.Optional[typing.Dict] = None, order: typing.Optional[int] = None):
        """
        
                Constructor.
        
                Keyword Args:
                    name (str): Menu item text, defaults to "".
                    icon (str): Menu item icon. Defaults to "".
                    hide_on_click (bool): Hide menu when radio menu item clicked, defaults to True.
                    appear_after (str): Name of menu item position to be after, defaults to "".
                    onclick_fn (Optional[Callable]): Callback when menu item clicked, defaults to None.
                    delegate (Optional[ui.MenuDelegate]): Menu item delegate, defaults to None.
                    visible_setting_path (Optional[str]): Setting path for menu item visibility, defaults to None.
                    order_setting_path (Optional[str]): Setting path for menu item order in menu bar, defaults to None.
                    expand_setting_path (Optional[str]): Setting path for menu item expand status in menu bar, defaults to None.
                    style (Optional[Dict]): Menu item additional UI style, defaults to None.
                    order (Optional[int]): Menu item order, deprecated. Using order_setting_path instead to be changed/saved.
                
        """
    def build_fn(self, factory_args: typing.Dict):
        """
        
                Callback to build this menu item. Reimplement it to have own customized item.
        
                Args:
                    factory_args (dict): Argument related to viewport.
                
        """
    def destroy(self) -> None:
        """
        Release resources
        """
    def invalidate(self) -> None:
        """
        Refresh menu item
        """
    @property
    def menu_item(self) -> omni.ui._ui.MenuItem:
        """
        Menu item widget
        """
    @property
    def visible(self) -> bool:
        """
        Menu item visibility
        """
    @visible.setter
    def visible(self, value: bool) -> None:
        ...
