from __future__ import annotations
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni.kit.viewport.menubar.core.menu_item.viewport_menu_separator import ViewportMenuSeparator
import omni.kit.viewport.menubar.core.model.combobox_model
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxModel
from omni.kit.viewport.menubar.core.utils import menu_is_tearable
from omni import ui
import omni.ui._ui
__all__: list = ['RadioMenuCollection']
class RadioMenuCollection(omni.ui._ui.MenuItemCollection):
    """
    
        A menu collection for radio menu items.
        
    """
    def _RadioMenuCollection__destroy_menu_items(self, value = None):
        ...
    def __init__(self, text: str, model: omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxModel, identifier: typing.Optional[str] = None, hide_on_click: bool = False, can_toggle_off: bool = False, delegate: omni.ui._ui.MenuDelegate = None):
        """
        
                Constructor.
        
                Args:
                    text (str): Menu text.
                    model (ComboBoxModel): Radio data model.
        
                Keyword Args:
                    identifier (Optional[str]): Menu item Identifier, defaults to None.
                    hide_on_click (bool): Hide menu when radio menu item clicked, defaults to False.
                    can_toggle_off (bool):Toggle selected state to off when radio menu item clicked and already selected, defaults to False.
                    delegate (ui.MenuDelegate): Menu item Delegate, defaults to None.
                
        """
    def _build_menu_items(self):
        ...
    def _item_chosen(self, index: int):
        ...
    def _on_current_changed(self, model: omni.ui._ui.AbstractValueModel):
        ...
    def _on_item_changed(self, model: omni.ui._ui.AbstractValueModel, item: omni.ui._ui.AbstractItem):
        ...
    def build_menu_item(self, item: omni.ui._ui.AbstractItem) -> omni.ui._ui.MenuItem:
        """
        
                Build single radio menu item.
        
                Args:
                    item (ui.AbstractItem): Model item.
                
        """
    def destroy(self) -> None:
        """
        Release resources
        """
