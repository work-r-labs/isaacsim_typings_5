from __future__ import annotations
import carb as carb
from isaacsim.examples.browser.delegate import AssetDetailDelegate
import isaacsim.examples.browser.model
from isaacsim.examples.browser.model import ExampleBrowserModel
from isaacsim.examples.browser.property_delegate import EmptyPropertyDelegate
from isaacsim.examples.browser.property_delegate import MultiPropertyDelegate
from isaacsim.examples.browser.property_delegate import PropAssetPropertyDelegate
from omni.kit.browser.core.widgets.tree_category_delegate import TreeCategoryDelegate
import omni.kit.browser.folder.core.property.tree_folder_browser_widget_ex
from omni.kit.browser.folder.core.property.tree_folder_browser_widget_ex import TreeFolderBrowserWidgetEx
from omni import ui
import omni.ui._ui
import os as os
import typing
__all__ = ['AssetDetailDelegate', 'BrowserWidget', 'EmptyPropertyDelegate', 'ExampleBrowserModel', 'ExampleBrowserWindow', 'MultiPropertyDelegate', 'PropAssetPropertyDelegate', 'TreeCategoryDelegate', 'TreeFolderBrowserWidgetEx', 'carb', 'os', 'ui']
class BrowserWidget(omni.kit.browser.folder.core.property.tree_folder_browser_widget_ex.TreeFolderBrowserWidgetEx):
    def _on_thumbnail_size_changed(self, thumbnail_size: int) -> None:
        ...
class ExampleBrowserWindow(omni.ui._ui.Window):
    """
    
        Represent a window to show Assets
        
    """
    WINDOW_TITLE: typing.ClassVar[str] = 'Robotics Examples'
    def __init__(self, model: isaacsim.examples.browser.model.ExampleBrowserModel, visible = True):
        ...
    def _build_ui(self):
        ...
