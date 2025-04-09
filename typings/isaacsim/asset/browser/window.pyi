from __future__ import annotations
import carb as carb
from isaacsim.asset.browser.delegate import AssetDetailDelegate
from isaacsim.asset.browser.empty_property_delegate import EmptyPropertyDelegate
from isaacsim.asset.browser.model import AssetBrowserModel
from isaacsim.asset.browser.multi_property_delegate import MultiPropertyDelegate
from isaacsim.asset.browser.options_menu import FolderOptionsMenu
from isaacsim.asset.browser.prop_property_delegate import PropAssetPropertyDelegate
from omni.kit.browser.core.widgets.tree_category_delegate import TreeCategoryDelegate
import omni.kit.browser.folder.core.property.tree_folder_browser_widget_ex
from omni.kit.browser.folder.core.property.tree_folder_browser_widget_ex import TreeFolderBrowserWidgetEx
from omni import ui
import omni.ui._ui
import os as os
import typing
__all__ = ['AssetBrowserModel', 'AssetBrowserWindow', 'AssetDetailDelegate', 'BrowserWidget', 'EmptyPropertyDelegate', 'FolderOptionsMenu', 'MultiPropertyDelegate', 'PROPERTY_STYLE', 'PropAssetPropertyDelegate', 'TreeCategoryDelegate', 'TreeFolderBrowserWidgetEx', 'carb', 'os', 'ui']
class AssetBrowserWindow(omni.ui._ui.Window):
    """
    
        Represent a window to show Assets
        
    """
    WINDOW_TITLE: typing.ClassVar[str] = 'Isaac Sim Assets [Beta]'
    def __init__(self, visible = True):
        ...
    def _build_ui(self):
        ...
    def destroy(self):
        ...
class BrowserWidget(omni.kit.browser.folder.core.property.tree_folder_browser_widget_ex.TreeFolderBrowserWidgetEx):
    def _on_thumbnail_size_changed(self, thumbnail_size: int) -> None:
        ...
PROPERTY_STYLE: dict = {'RadioButton': {'background_color': 0, 'padding': 0}, 'RadioButton.Image': {'image_url': '/home/chris/isaacsim/exts/isaacsim.asset.browser/icons/radio_off.svg'}, 'RadioButton.Image:checked': {'image_url': '/home/chris/isaacsim/exts/isaacsim.asset.browser/icons/radio_on.svg'}}
