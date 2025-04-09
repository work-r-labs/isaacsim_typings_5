from __future__ import annotations
import omni.kit.browser.core.widgets.tree_browser_widget
from omni.kit.browser.core.widgets.tree_browser_widget import TreeBrowserWidget
import omni.kit.browser.folder.core.models.folder_browser_data
from omni.kit.browser.folder.core.models.folder_browser_data import FileSystemFolder
import omni.kit.browser.folder.core.models.folder_browser_item
from omni.kit.browser.folder.core.models.folder_browser_item import FolderCategoryItem
import omni.kit.browser.folder.core.widgets.folder_browser_widget
from omni.kit.browser.folder.core.widgets.folder_browser_widget import FolderBrowserWidget
from omni.kit.browser.folder.core.widgets.folder_category_delegate import FolderCategoryDelegate
__all__ = ['FileSystemFolder', 'FolderBrowserWidget', 'FolderCategoryDelegate', 'FolderCategoryItem', 'TreeBrowserWidget', 'TreeFolderBrowserWidget']
class TreeFolderBrowserWidget(omni.kit.browser.folder.core.widgets.folder_browser_widget.FolderBrowserWidget):
    def __init__(self, *args, category_delegate: typing.Optional[omni.kit.browser.folder.core.widgets.folder_category_delegate.FolderCategoryDelegate] = None, **kwargs):
        ...
    def _build_browser_widget_internal(self, *args, **kwargs) -> omni.kit.browser.core.widgets.tree_browser_widget.TreeBrowserWidget:
        ...
    def _on_category_selection_changed(self, category_item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem) -> None:
        ...
    def _on_new_collection_added(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder) -> None:
        ...
