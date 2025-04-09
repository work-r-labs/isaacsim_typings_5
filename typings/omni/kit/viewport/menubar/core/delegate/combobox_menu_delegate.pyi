from __future__ import annotations
import omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate
from omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate import AbstractWidgetMenuDelegate
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxModel
from omni import ui
import omni.ui._ui
__all__: list = ['ComboBoxMenuDelegate']
class ComboBoxMenuDelegate(omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate.AbstractWidgetMenuDelegate):
    """
    A menu delegate that creates combobox within a viewport menubar.
    """
    def __del__(self):
        ...
    def __init__(self, model: typing.Optional[omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxModel] = None, height: omni.ui._ui.Length = 0, width: omni.ui._ui.Length = 300, enabled: bool = True, text: bool = True, icon_name: typing.Optional[str] = None, icon_width: omni.ui._ui.Length = 30, icon_height: omni.ui._ui.Length = 30, tooltip: typing.Optional[str] = None, use_in_menubar: bool = False, has_reset: bool = False):
        """
        
                Constructor.
        
                Keyword Args:
                    model (Optional[ComboBoxModel]): Combobox data model, defaults to None.
                    height (ui.Length): Delegate height, defaults to 0 means auto height.
                    width (ui.Length): Delegate width, defaults to 300 pixels.
                    enabled (bool): Delegate enabled state, defaults to True.
                    text (bool): Show text before combobox, defaults to True.
                    icon_name (Optional[str]): Name of additional icon to be displayed before text, defaults to None means no additional icon.
                    icon_width (ui.Length): Width of additional icon. Only available when icon_name is valid, defaults to 30 pixels.
                    icon_height (ui.Length): Height of additional icon. Only available when icon_name is valid, defaults to 30 pixels.
                    tooltip (Optional[str]): Delegate tooltip, defaults to None means no tooltip.
                    use_in_menubar (bool): Show delegate in menu bar, defaults to False.
                    has_reset (bool): Show reset button, defaults to False.
                
        """
    def build_widget(self, item: omni.ui._ui.MenuHelper) -> None:
        """
        
                Build combobox with optional icon and label.
        
                Args:
                    item (ui.MenuHelper): Menu item.
                
        """
    def destroy(self) -> None:
        """
        Release resources.
        """
