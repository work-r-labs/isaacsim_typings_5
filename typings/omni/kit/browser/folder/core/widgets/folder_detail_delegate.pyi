from __future__ import annotations
import omni.kit.browser.core.widgets.detail_delegate
from omni.kit.browser.core.widgets.detail_delegate import DetailDelegate
import omni.kit.browser.folder.core.models.folder_browser_item
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
import omni.kit.browser.folder.core.models.folder_browser_model
from omni.kit.browser.folder.core.models.folder_browser_model import FolderBrowserModel
from pathlib import Path
__all__ = ['DetailDelegate', 'FileDetailItem', 'FolderBrowserModel', 'FolderDetailDelegate', 'Path']
class FolderDetailDelegate(omni.kit.browser.core.widgets.detail_delegate.DetailDelegate):
    """
    
        Delegate to show folder item in detail view.
        Keyword args:
            model (FolderBrowserModel): Folder browser model. Default None.
        
    """
    def __init__(self, model: omni.kit.browser.folder.core.models.folder_browser_model.FolderBrowserModel = None):
        ...
    def destroy(self) -> None:
        ...
    def get_label(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem) -> typing.Optional[str]:
        ...
    def get_label_height(self) -> int:
        ...
    def get_tooltip(self, item: omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem) -> str:
        ...
