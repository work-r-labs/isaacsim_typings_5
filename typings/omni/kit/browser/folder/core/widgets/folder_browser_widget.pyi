from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.browser.core.models.browser_item import DetailItem
from omni.kit.browser.core.widgets.browser_widget import BrowserWidget
from omni.kit.browser.core.widgets.category_delegate import CategoryDelegate
from omni.kit.browser.core.widgets.search_bar import BrowserSearchBar
from omni.kit.browser.core.widgets.search_bar import OptionsMenu
from omni.kit.browser.folder.core.models.folder_browser_data import FileSystemFolder
from omni.kit.browser.folder.core.models.folder_browser_item import FolderCategoryItem
from omni.kit.browser.folder.core.models.folder_browser_model import FolderBrowserModel
from omni.kit.browser.folder.core.widgets.folder_category_delegate import FolderCategoryDelegate
from omni.kit.browser.folder.core.widgets.folder_detail_delegate import FolderDetailDelegate
from omni.kit.browser.folder.core.widgets.options_menu import FolderOptionsMenu
from omni.kit.window.filepicker.dialog import FilePickerDialog
from omni import ui
__all__ = ['BrowserSearchBar', 'BrowserWidget', 'CategoryDelegate', 'DetailItem', 'FilePickerDialog', 'FileSystemFolder', 'FolderBrowserModel', 'FolderBrowserWidget', 'FolderCategoryDelegate', 'FolderCategoryItem', 'FolderDetailDelegate', 'FolderOptionsMenu', 'OptionsMenu', 'asyncio', 'omni', 'ui']
class FolderBrowserWidget:
    """
    
        Represent a widget for folders.
        Args:
            browser_model (FolderBrowserModel): Folder browser model used in the widget.
        Keyword args:
            detail_delegate (Optional[FolderDetailDelegate]): Detail delegate used in the widget. Default None means using standard folder detail delegate.
            options_menu (Optional[OptionsMenu]): Options menu used in the widget. Default None means using default (Add/Remove collection) in the widget.
            style (dict): Extra ui style. Default empty.
            min_thumbnail_size (int): min thumbnail size used in zoom bar. Default 32.
            max_thumbnail_size (int): max thumbnail size used in zoom bar. Default 512.
            detail_thumbnail_size (int): size of detail item thumbnail, in pixel. Default 128.
            thumbnail_aspect (float): Aspect ratio of thumbnail. Default 1.0 (width / height).
            extra_filter_fn (callable): Extra filter function called to filter items. Return True to show item otherwise hide.
                Default None. Function signure: bool extra_filter_fn(item: DetailItem)
            predownload_folder (Optional[str]): Folder to predownload files and sub folders. Predownload is used to download items from remote folder to local when startup.
                Default None means no predowndload.
            category_tree_mode (Optional[bool]): Show categories in tree mode rather than flat mode.
            show_category_splitter (Optional[bool]): Show adjustable splitter bar between category and detail views.
            category_width (Optional[float]): Set starting width of category view.
            splitter_extra_width (int): Width added to vertical splitter between category view and detail view.
            multiple_drag (bool): True to allow drag multiple items. Default False.
        
    """
    category_selection: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]
    detail_selection: typing.List[omni.kit.browser.core.models.browser_item.DetailItem]
    def _FolderBrowserWidget__find_category_item_by_url(self, url: str, parent_item: omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem) -> typing.Optional[omni.kit.browser.folder.core.models.folder_browser_item.FolderCategoryItem]:
        ...
    def _FolderBrowserWidget__on_browser_model_changed(self, model: omni.kit.browser.folder.core.models.folder_browser_model.FolderBrowserModel, item: omni.ui._ui.AbstractItem):
        ...
    def __init__(self, browser_model: omni.kit.browser.folder.core.models.folder_browser_model.FolderBrowserModel, category_delegate: typing.Optional[omni.kit.browser.core.widgets.category_delegate.CategoryDelegate] = None, detail_delegate: typing.Optional[omni.kit.browser.folder.core.widgets.folder_detail_delegate.FolderDetailDelegate] = None, options_menu: typing.Optional[omni.kit.browser.core.widgets.search_bar.OptionsMenu] = None, min_thumbnail_size: int = 32, max_thumbnail_size: int = 512, detail_thumbnail_size: int = 128, thumbnail_aspect: float = 1.0, predownload_folder: typing.Optional[str] = None, style: typing.Dict = {}, extra_filter_fn: callable = None, category_tree_mode = False, show_category_splitter = False, category_width: float = 120, splitter_extra_width: int = 4, always_select_category: bool = True, multiple_drag: bool = False):
        ...
    def _build_browser_widget(self):
        ...
    def _build_browser_widget_internal(self, *args, **kwargs):
        ...
    def _build_search_bar(self):
        ...
    def _build_ui(self):
        ...
    def _create_filepicker(self, title: str, filters: list = ['All Files (*)'], click_apply_fn: typing.Callable = None, error_fn: typing.Callable = None, dir_only: bool = False) -> omni.kit.window.filepicker.dialog.FilePickerDialog:
        ...
    def _on_add_collection(self) -> None:
        ...
    def _on_folder_picked(self, url: typing.Optional[str]) -> None:
        ...
    def _on_new_collection_added(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder) -> None:
        ...
    def _on_remove_collection(self) -> None:
        ...
    def _on_thumbnail_size_changed(self, thumbnail_size: int) -> None:
        ...
    def build_widgets(self):
        ...
    def destroy(self) -> None:
        """
        Clean up
        """
    def select_folder(self, folder: omni.kit.browser.folder.core.models.folder_browser_data.FileSystemFolder, expand: bool = False):
        ...
