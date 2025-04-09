from __future__ import annotations
import omni.kit.browser.core.widgets.search_bar
from omni.kit.browser.core.widgets.search_bar import OptionMenuDescription
from omni.kit.browser.core.widgets.search_bar import OptionsMenu
from omni.kit.browser.folder.core.models.folder_browser_item import FolderCollectionItem
from omni.kit.browser.folder.core.models.tree_folder_browser_model import TreeFolderBrowserModel
from omni.kit.browser.folder.core.widgets.predownload import PredownloadHelper
__all__ = ['FolderCollectionItem', 'FolderOptionsMenu', 'OptionMenuDescription', 'OptionsMenu', 'PredownloadHelper', 'TreeFolderBrowserModel']
class FolderOptionsMenu(omni.kit.browser.core.widgets.search_bar.OptionsMenu):
    """
    
        Represent options menu used in material browser.
        Args:
            predownload_folder (Optional[str]): Folder to predownload files and sub folders. Predownload is used to download items from remote folder to local when startup.
                Default None means no predowndload.
        
    """
    def __init__(self, predownload_folder: typing.Optional[str] = None):
        ...
    def _get_menu_item_text(self) -> str:
        ...
    def _is_download_collection_enable(self):
        ...
    def _is_refresh_collection_visible(self) -> bool:
        ...
    def _is_remote_folder(self, url):
        ...
    def _is_remove_collection_enabled(self) -> bool:
        ...
    def _on_download_collection(self) -> None:
        ...
    def _on_refresh_collection(self):
        ...
    def _on_remove_collection(self) -> None:
        ...
    def destroy(self) -> None:
        ...
