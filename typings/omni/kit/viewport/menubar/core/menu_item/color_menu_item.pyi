from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.viewport.menubar.core.delegate.color_menu_delegate import ColorMenuDelegate
from omni.kit.viewport.menubar.core.model.list_model import ColorModel
from omni import ui
__all__: list = ['AbstractColorMenuItem', 'FloatArraySettingColorMenuItem']
class AbstractColorMenuItem(omni.ui._ui.MenuItem):
    """
    
        Base menu item to show/change colors.
        
    """
    def __init__(self, colors: typing.List[float], name: str = '', default: typing.Optional[typing.List[float]] = None, has_reset: bool = False):
        """
        
                Constructor.
        
                Args:
                    colors (List[float]): Colors attached to this menu item.
        
                Keyword Args:
                    name (str): Text of menu item. Default empty string.
                    default Optional[List[float]. Default colors when reset. Default None.
                    has_reset (bool): Show reset button, defaults to False.
                
        """
    def destroy(self) -> None:
        """
        Release resources.
        """
    def on_color_changed(self, colors: typing.List[float]) -> None:
        """
        
                Callback when colors changed.
        
                Args:
                    colors colors: List[float]: Changed colors.
                
        """
    def reset(self) -> None:
        """
        Callback when reset colors
        """
class FloatArraySettingColorMenuItem(AbstractColorMenuItem):
    """
     A menu item to show/change colors from carb.settings
    """
    def _FloatArraySettingColorMenuItem__create_color_subs(self):
        ...
    def _FloatArraySettingColorMenuItem__get_color_paths(self):
        ...
    def _FloatArraySettingColorMenuItem__on_change(self, item: carb.dictionary._dictionary.Item, event_type: carb.settings._settings.ChangeEventType) -> None:
        ...
    def __del__(self):
        ...
    def __init__(self, setting_path: str, default: typing.List[float], name: str = '', start_index: int = 0, has_reset: bool = False):
        """
        
                Constructor.
        
                Args:
                    setting_path (str): Colors setting path.
        
                Keyword Args:
                    default Optional[List[float]. Default colors when reset, defaults to None.
                    name (str): Menu item text, defaults to "".
                    start_index (int): Index of this color in data array from setting path, defaults to 0.
                    has_reset (bool): Show reset button, defaults to False.
                
        """
    def _get_color(self) -> typing.List[float]:
        ...
    def destroy(self) -> None:
        """
        Release resources
        """
    def on_color_changed(self, colors: typing.List[float]) -> None:
        """
        
                Callback when colors changed.
        
                Args:
                    colors colors: List[float]: Changed colors.
                
        """
    def reset(self) -> None:
        """
        Callback when reset colors
        """
