from __future__ import annotations
import carb as carb
import math as math
import omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate
from omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate import AbstractWidgetMenuDelegate
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
import omni.kit.viewport.menubar.core.menu_item.radio_menu_collection
from omni.kit.viewport.menubar.core.menu_item.radio_menu_collection import RadioMenuCollection
import omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model
from omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model import ComboBoxResolutionModel
from omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model import ResolutionComboBoxItem
from omni import ui
import omni.ui._ui
import typing
import weakref as weakref
__all__ = ['AbstractWidgetMenuDelegate', 'ComboBoxResolutionModel', 'DEFAULT_RATIOS', 'RadioMenuCollection', 'ResolutionCollectionDelegate', 'ResolutionCollectionMenu', 'ResolutionComboBoxItem', 'SETTING_CUSTOM_RESOLUTION_LIST', 'ViewportMenuDelegate', 'carb', 'math', 'ui', 'weakref']
class ResolutionCollectionDelegate(omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate.AbstractWidgetMenuDelegate):
    def _ResolutionCollectionDelegate__get_current_resolution(self):
        ...
    def _ResolutionCollectionDelegate__on_index_changed(self) -> None:
        ...
    def __init__(self, model: omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model.ComboBoxResolutionModel):
        ...
    def build_widget(self, item: omni.ui._ui.MenuHelper):
        ...
    def destroy(self):
        ...
class ResolutionCollectionMenu(omni.kit.viewport.menubar.core.menu_item.radio_menu_collection.RadioMenuCollection):
    ITEM_HEIGHT: typing.ClassVar[int] = 20
    def _ResolutionCollectionMenu__build_resolution_menuitem_widgets(self, item: omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model.ResolutionComboBoxItem):
        ...
    def _ResolutionCollectionMenu__delete_resolution(self, item: omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model.ResolutionComboBoxItem):
        ...
    def __init__(self, text: str, model: omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model.ComboBoxResolutionModel):
        ...
    def build_menu_item(self, item: omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model.ResolutionComboBoxItem) -> omni.ui._ui.MenuItem:
        ...
    def destroy(self):
        ...
    def get_ratio_text(self, ratio: float):
        ...
DEFAULT_RATIOS: dict = {'16:9': 1.7777777777777777, '1:1': 1, '32:9': 3.5555555555555554, '4:3': 1.3333333333333333, '21:9': 2.3333333333333335}
SETTING_CUSTOM_RESOLUTION_LIST: str = '/persistent/app/renderer/resolution/custom/list'
