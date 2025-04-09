from __future__ import annotations
import omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate
from omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate import AbstractWidgetMenuDelegate
from omni.kit.viewport.menubar.core.model.list_model import ColorModel
from omni import ui
import omni.ui._ui
__all__: list = ['ColorMenuDelegate']
class ColorMenuDelegate(omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate.AbstractWidgetMenuDelegate):
    """
    A menu delegate that creates color picker within a viewport menubar.
    """
    def __del__(self):
        ...
    def __init__(self, model: typing.Optional[omni.kit.viewport.menubar.core.model.list_model.ColorModel] = None, tooltip: typing.Optional[str] = None, has_reset: bool = False):
        """
        
                Constructor.
        
                Keyword Args:
                    model (Optional[ColorModel]): Color data model.
                    tooltip (Optional[str]): Delegate tooltip, defaults to None means no tooltip.
                    has_reset (bool): Show reset button, defaults to False.
                
        """
    def build_widget(self, item: omni.ui._ui.MenuHelper) -> None:
        """
        
                Build color picker.
        
                Args:
                    item (ui.MenuHelper): Menu item.
                
        """
    def destroy(self) -> None:
        """
        Release resources.
        """
