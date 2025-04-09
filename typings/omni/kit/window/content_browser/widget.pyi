from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.helper.file_utils import asset_types
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.window.content_browser.api import ContentBrowserAPI
from omni.kit.window.content_browser.context_menu import ContextMenu
from omni.kit.window.content_browser.file_ops import drop_items
from omni.kit.window.content_browser.file_ops import get_file_open_handler
from omni.kit.window.content_browser.file_ops import open_file
from omni.kit.window.content_browser.file_ops import open_stage
from omni.kit.window.content_browser.tool_bar import ToolBar
from omni.kit.window.filepicker.context_menu import BookmarkContextMenu
from omni.kit.window.filepicker.context_menu import CollectionContextMenu
from omni.kit.window.filepicker.context_menu import ConnectionContextMenu
from omni.kit.window.filepicker.context_menu import LocalContextMenu
from omni.kit.window.filepicker.context_menu import UdimContextMenu
from omni.kit.window.filepicker.widget import FilePickerWidget
import os as os
import pathlib
__all__ = ['BookmarkContextMenu', 'CollectionContextMenu', 'ConnectionContextMenu', 'ContentBrowserAPI', 'ContentBrowserWidget', 'ContextMenu', 'FILE_TYPE_USD', 'FileBrowserItem', 'FilePickerWidget', 'ICON_COMMON_PATH', 'LISTVIEW_PANE', 'LocalContextMenu', 'SETTING_PERSISTENT_CURRENT_DIRECTORY', 'SETTING_ROOT', 'ToolBar', 'UdimContextMenu', 'asset_types', 'carb', 'drop_items', 'get_file_open_handler', 'omni', 'open_file', 'open_stage', 'os']
class ContentBrowserWidget(omni.kit.window.filepicker.widget.FilePickerWidget):
    """
    The Content Browser widget
    """
    def __init__(self, **kwargs):
        ...
    def _apply_filter_options(self):
        ...
    def _build_checkpoint_widget(self):
        """
        Overrides base builder, adds items to context menu
        """
    def _build_context_menus(self):
        """
        Overrides base builder, injects custom context menus
        """
    def _build_tool_bar(self):
        """
        Overrides base builder, injects custom tool bar
        """
    def _get_mounted_servers(self) -> typing.Dict:
        """
        Overrides base getter, returns mounted server dict from settings
        """
    def _item_filter_fn(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        """
        
                Default item filter callback. Returning True means the item is visible.
        
                Args:
                    item (:obj:`FileBrowseritem`): Item in question.
        
                Returns:
                    bool
        
                
        """
    def _on_mouse_double_clicked(self, pane: int, button: int, key_mod: int, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        ...
    def _on_selection_changed(self, pane: int, selected: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem] = list()):
        ...
    def _open_and_navigate_to(self, url: str):
        ...
    def destroy(self):
        ...
FILE_TYPE_USD: int = 1
ICON_COMMON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.content_browser-2.10.3+d02c707b/icons/common')
LISTVIEW_PANE: int = 2
SETTING_PERSISTENT_CURRENT_DIRECTORY: str = '/persistent/exts/omni.kit.window.content_browser/current_directory'
SETTING_ROOT: str = '/exts/omni.kit.window.content_browser/'
