from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__: list = ['ViewportMenuDelegate']
class ViewportMenuDelegate(omni.ui._ui.MenuDelegate):
    """
    A basic menu delegate within a viewport menubar
    """
    def _ViewportMenuDelegate__icon_clicked(self, x, y, *arg, **kwargs) -> None:
        ...
    def __init__(self, icon_name: str = '', icon_width: int = 16, reserve_status: bool = True, force_checked: bool = False, icon_clicked_fn: typing.Callable[[NoneType], NoneType] = None, build_custom_widgets: typing.Callable[[omni.ui._ui.MenuDelegate, typing.Union[omni.ui._ui.MenuItem, omni.ui._ui.Menu]], NoneType] = None, show_hotkey_placeholder: bool = False):
        """
        
                Constructor.
        
                Keyword Args:
                    icon_name (str): Name of icon to show after menu text, defaults to "" means no icon.
                    icon_width (int): Icon width, defaults to 16 pixels.
                    reserve_status (bool): Show additional space before widgets, defaults to False. Used to align with other menu items which have status icon.
                    force_checked (bool): Force to show checked status, defaults to False.
                        It is strange that when a menu is checked, sub menu items checked flag will be cleared. Use this flag to show correct sub menu item status.
                    icon_clicked_fn (Callable[[None], None]): Callback when icon clicked, defaults to None
                    build_custom_widgets (Callable[[ui.MenuDelegate, Union[ui.MenuItem, ui.Menu]], None]): Callback to build custom widgets, defaults to None.
                    show_hotkey_placeholder (bool): Show placeholder for hotkey text, defaults to False. Used to align with other menu items which have hotkeys.
                
        """
    def build_item(self, item: typing.Union[omni.ui._ui.MenuItem, omni.ui._ui.Menu]) -> None:
        """
        
                Build widgets (from left to right):
                 - Selected icon
                 - Menu item label
                 - Menu item Icon
                 - Custom widgets (Optional)
                 - Hotkey label
                 - Arrow for sub menus (only for ui.Menu)
        
                Args:
                    item Union[ui.MenuItem, ui.Menu]): Menu item.
                
        """
    def get_checked(self) -> bool:
        """
        Delegate checked state
        """
    def get_selected(self) -> bool:
        """
        Delegate selected state
        """
    def set_checked(self, value: bool) -> bool:
        """
        Set delegate checked state and return whether it changed or not.
        """
    def set_selected(self, value: bool) -> bool:
        """
        Set delegate selected state and return whether it changed or not.
        """
    @property
    def checked(self) -> bool:
        """
        Delegate checked state
        """
    @checked.setter
    def checked(self, value: bool) -> None:
        ...
    @property
    def selected(self) -> bool:
        """
        Delegate selected state
        """
    @selected.setter
    def selected(self, value: bool) -> None:
        ...
MENU_ARROW_SIZE: int = 8
STATUS_ICON_WIDTH: int = 20
