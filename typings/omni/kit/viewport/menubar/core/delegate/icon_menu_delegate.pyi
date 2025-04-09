from __future__ import annotations
from omni import ui
import omni.ui._ui
__all__: list = ['IconMenuDelegate']
class IconMenuDelegate(omni.ui._ui.MenuDelegate):
    """
    A menu delegate that creates icon and optionally text within a viewport menubar.
    """
    def __init__(self, name: str, text: bool = False, width: omni.ui._ui.Length = 30, height: omni.ui._ui.Length = 30, has_triangle: bool = True, triangle_size: float = 6, checked: bool = False, enabled: bool = True, triggered_fn: typing.Callable[[NoneType], NoneType] = None, right_clicked_fn: typing.Callable[[NoneType], NoneType] = None, tooltip: typing.Optional[str] = None, build_custom_widgets: typing.Callable[[omni.ui._ui.MenuItem], NoneType] = None):
        """
        
                Constructor.
        
                Args:
                    name: (str): Icon Name of "Menu.Item.Icon" in UI style definition.
                    text (bool): Show text before icon, defaults to False.
                    width (ui.Length): Delegate width, defaults to 30 pixels.
                    height (ui.Length): Delegate height, defaults to 30 pixels.
                    has_triangle (bool): Show drop-down carrot, defaults to True.
                    triangle_size (float): Size of drop-down carrot, defaults to 6 pixels.
                    checked (bool): Delegate checked state, defaults to False.
                    enabled (bool): Delegate enabled state, defaults to True.
                    triggered_fn (Callable[[None], None]): Callback when menu item clicked, defaults to None.
                    right_clicked_fn (Callable[[None], None]): Callback when right click on this menu item, defaults to None.
                    tooltip (Optional[str]): Delegate tooltip, Default None means no tooltip.
                    build_custom_widget (Callable[[ui.MenuItem], None]): Callback to build more widgets, defaults to None.
                
        """
    def _build_icon(self) -> None:
        ...
    def _on_mouse_released(self, button: int) -> None:
        ...
    def build_item(self, item: omni.ui._ui.MenuItem) -> None:
        """
        
                Build icon with optional drop-down carrot and label.
        
                Args:
                    item (ui.MenuItem): Menu item.
                
        """
    def destroy(self):
        """
        Release resources.
        """
    @property
    def checked(self) -> bool:
        """
        
                Delegate checked state.
                
        """
    @checked.setter
    def checked(self, value) -> None:
        ...
    @property
    def enabled(self) -> bool:
        """
        
                Delegate enabled state.
                
        """
    @enabled.setter
    def enabled(self, value) -> None:
        ...
    @property
    def text(self) -> str:
        """
        Label text
        """
    @text.setter
    def text(self, txt: str):
        ...
    @property
    def text_size(self) -> float:
        """
        
                Label size.
                
        """
    @property
    def text_visible(self) -> bool:
        """
        
                Label visibility.
                
        """
    @text_visible.setter
    def text_visible(self, value: bool) -> None:
        ...
