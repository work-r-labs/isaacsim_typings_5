from __future__ import annotations
import abc as abc
from omni.kit.viewport.menubar.core.model.reset_button import ResetButton
from omni import ui
import omni.ui._ui
__all__ = ['AbstractWidgetMenuDelegate', 'MENU_ARROW_SIZE', 'ResetButton', 'abc', 'ui']
class AbstractWidgetMenuDelegate(omni.ui._ui.MenuDelegate):
    """
    Base class for menu delegate which has widgets
    """
    def __init__(self, model: typing.Optional[omni.ui._ui.AbstractItemModel] = None, width: typing.Optional[omni.ui._ui.Length] = None, height: typing.Optional[omni.ui._ui.Length] = None, enabled: bool = True, has_reset: bool = False, reserve_status: bool = False, use_in_menubar: bool = False, content_clipping: bool = True, visible: bool = True):
        """
        
                Constructor.
        
                Args:
                    model (Optional[ui.AbstractItemModel]): Delegate data model, defaults to None.
                    width (ui.Length): Delegate width, defaults to None means ui.Fraction(1).
                    height (ui.Length): Delegate height, defaults to None means ui.Fraction(1).
                    enabled (bool): Delegate enabled state, defaults to True.
                    has_reset (bool): Show reset button, defaults to False.
                    reserve_status (bool): Show additional space before widgets, defaults to False. Used to align with other menu items which have status icon.
                    use_in_menubar (bool): Show delegate in menu bar, defaults to False.
                    content_clipping (bool): Delegate content clipping, defaults to True.
                    visible (bool): Delegate visibility, defaults to True.
                
        """
    def build_item(self, item: omni.ui._ui.MenuItem) -> None:
        """
        
                Callback to build menu item.
        
                Args:
                    item (ui.MenuItem): Menu item.
                
        """
    def build_widget(self, item: omni.ui._ui.MenuHelper) -> None:
        """
        
                Callback to build widgets.
        
                Args:
                    item (ui.MenuHelper): Menu item.
                
        """
    def destroy(self) -> None:
        """
        Override to release resources.
        """
    @property
    def enabled(self) -> bool:
        """
        Delegate enabled status
        """
    @enabled.setter
    def enabled(self, value) -> None:
        ...
    @property
    def visible(self) -> bool:
        """
        Delegate visibility
        """
    @visible.setter
    def visible(self, value: bool) -> None:
        ...
MENU_ARROW_SIZE: int = 8
