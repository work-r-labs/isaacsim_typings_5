from __future__ import annotations
import omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate
from omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate import AbstractWidgetMenuDelegate
from omni import ui
import omni.ui._ui
__all__: list = ['CheckboxMenuDelegate']
class CheckboxMenuDelegate(omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate.AbstractWidgetMenuDelegate):
    """
    A menu delegate that creates checkbox within a viewport menubar.
    """
    def __del__(self):
        ...
    def __init__(self, model: typing.Optional[omni.ui._ui.SimpleBoolModel] = None, tooltip: typing.Optional[str] = None, width: omni.ui._ui.Length = 300, height: omni.ui._ui.Length = 0, enabled: bool = True, use_in_menubar: bool = False, has_reset: bool = False):
        """
        
                Constructor.
        
                Keyword Args:
                    model (Optional[ui.SimpleBoolModel]): Checkbox data model.
                    tooltip (Optional[str]): Delegate tooltip text, defaults to None means no tooltip.
                    width (ui.Length): Delegate width, defaults to 300 pixels.
                    height (ui.Length): Delegate height, defaults to 0 means auto.
                    enabled (bool): Delegate enabled state, defaults to True.
                    use_in_menubar (bool): Show delegate in menu bar, defaults to False.
                    has_reset (bool): Show reset button, defaults to False.
                
        """
    def build_widget(self, item: omni.ui._ui.MenuHelper) -> None:
        """
        
                Build checkbox.
        
                Args:
                    item (ui.MenuItem): Menu item.
                
        """
    def destroy(self) -> None:
        """
        Release resources.
        """
