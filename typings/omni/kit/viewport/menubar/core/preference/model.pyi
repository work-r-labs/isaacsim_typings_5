from __future__ import annotations
from omni.kit.viewport.menubar.core.menu_item.viewport_menubar_item import ViewportMenubar
import omni.kit.viewport.menubar.core.viewport_menu_model
from omni.kit.viewport.menubar.core.viewport_menu_model import AbstractViewportMenuItem
from omni import ui
import omni.ui._ui
__all__: list = ['PreferenceModel']
class PreferenceModel(omni.ui._ui.AbstractItemModel):
    """
    
        Wrapper model for preference page.
        Only show default menubar in preference page. So using this wrapper to get menu items for default menubar only.
        
    """
    def _PreferenceModel__on_menubar_changed(self, model: omni.ui._ui.AbstractItemModel, item: omni.ui._ui.AbstractItem):
        ...
    def __init__(self, model: <function singleton.<locals>.getinstance at 0x709ef21dcca0>):
        ...
    def _drop_item(self, target: omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem, source: omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem, drop_location = -1):
        ...
    def destroy(self):
        ...
    def drop(self, target_item, source, drop_location = -1):
        """
        Reimplemented from AbstractItemModel. Called when dropping something to the item.
        """
    def drop_accepted(self, target_item, source, drop_location = -1):
        """
        Reimplemented from AbstractItemModel. Called to highlight target when drag and drop.
        """
    def get_drag_mime_data(self, item):
        """
        Returns Multipurpose Internet Mail Extensions (MIME) data for be able to drop this item somewhere
        """
    def get_item_children(self, parent_item = None):
        ...
    def get_item_value_model(self, item: omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem, column_id: int):
        ...
    def get_item_value_model_count(self, item: omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem):
        """
        The number of columns
        """
DEFAULT_MENUBAR_NAME: str = '__DEFAULT__MENUBAR__'
