from __future__ import annotations
import asyncio as asyncio
from carb import log_info
from carb import log_warn
import omni as omni
from omni.kit.helper.file_utils import asset_types
from omni.kit.widget.browser_bar.widget import BrowserBar
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.widget.filebrowser.model import FileBrowserUdimItem
from omni.kit.window.filepicker.bookmark_model import BookmarkItem
from omni.kit.window.filepicker.collection_data import CollectionData
from omni.kit.window.filepicker.context_menu import ContextMenu
from omni.kit.window.filepicker.detail_view import DetailFrameController
from omni.kit.window.filepicker.detail_view import DetailView
from omni.kit.window.filepicker.file_bar import FileBar
from omni.kit.window.filepicker.model import FilePickerModel
from omni.kit.window.filepicker.utils import LoadingPane
from omni.kit.window.filepicker.view import FilePickerView
import os as os
__all__: list = ['FilePickerAPI']
class FilePickerAPI:
    """
    This class defines the API methods for :obj:`FilePickerWidget`.
    """
    def __init__(self, model: omni.kit.window.filepicker.model.FilePickerModel = None, view: omni.kit.window.filepicker.view.FilePickerView = None):
        """
        
                Initialize the FilePickerAPI.
        
                Args:
                    model (:obj:'FilePickerModel'): The model background, default None.
                    view (:obj:'FilePickerView'): the content view object. Default None.
                
        """
    def _info(self, msg: str):
        ...
    def _is_nucleus_server_url(self, url: str):
        ...
    def _update_bookmarks(self, client_bookmarks: typing.Dict):
        ...
    def _update_nucleus_servers(self, client_bookmarks: typing.Dict):
        ...
    def _warn(self, msg: str):
        ...
    def add_collection(self, collection_data: omni.kit.window.filepicker.collection_data.CollectionData):
        """
        
                Add custom collection to current content view.
                samples of collection: "My Computer", "Omniverse Bookmark", ...
        
                Args:
                    collection_data (CollectionData): Data to add.
        
                
        """
    def add_connections(self, connections: dict):
        """
        
                Adds specified server connections to the tree browser. To facilitate quick startup time, doesn't check
                whether the connection is actually valid.
        
                Args:
                    connections (dict): A dictionary of name, path pairs. For example:
                        {"C:": "C:", "ov-content": "omniverse://ov-content"}.  Paths to Omniverse servers
                        should be prefixed with "omniverse://".
        
                
        """
    def add_context_menu(self, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index: int = -1, separator_name = '_add_on_end_separator_') -> str:
        """
        
                Adds menu item, with corresponding callbacks, to the context menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open'), this name must be unique across the context menu.
                    glyph (str): Associated glyph to display for this menu item.
                    click_fn (Callable): This callback function is executed when the menu item is clicked. Function signature:
                        void fn(name: str, path: str), where name is menu name and path is absolute path to clicked item.
                    show_fn (Callable): Returns True to display this menu item. Function signature: bool fn(path: str).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
                    index (int): The postion that this menu item will be inserted to.
                    separator_name (str): The separator name of the separator menu item. Default to '_placeholder_'. When the
                        index is not explicitly set, or if the index is out of range, this will be used to locate where to add
                        the menu item; if specified, the index passed in will be counted from the saparator with the provided
                        name. This is for OM-86768 as part of the effort to match Navigator and Kit UX for Filepicker/Content Browser for context menus.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
        
                
        """
    def add_detail_frame(self, name: str, glyph: str, build_fn: typing.Callable[[], NoneType], selection_changed_fn: typing.Callable[[typing.List[str]], NoneType] = None, filename_changed_fn: typing.Callable[[str], NoneType] = None, destroy_fn: typing.Callable[[], NoneType] = None):
        """
        
                Adds sub-frame to the detail view, and populates it with a custom built widget.
        
                Args:
                    name (str): Name of the widget sub-section, this name must be unique over all detail sub-sections.
                    glyph (str): Associated glyph to display for this subj-section
                    build_fn (Callable): This callback function builds the widget.
        
                Keyword Args:
                    selection_changed_fn (Callable): This callback is invoked to handle selection changes.
                    filename_changed_fn (Callable): This callback is invoked when filename is changed.
                    destroy_fn (Callable): Cleanup function called when destroyed.
        
                
        """
    def add_detail_frame_from_controller(self, name: str, controller: omni.kit.window.filepicker.detail_view.DetailFrameController):
        """
        
                Adds sub-frame to the detail view, and populates it with a custom built widget.
        
                Args:
                    name (str): Name of the widget sub-section, this name must be unique over all detail sub-sections.
                    controller (:obj:`DetailFrameController`): Controller object that encapsulates all aspects of creating,
                        updating, and deleting a detail frame widget.
        
                
        """
    def add_listview_menu(self, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index: int = -1) -> str:
        """
        
                Adds menu item, with corresponding callbacks, to the list view menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open'), this name must be unique across the list view menu.
                    glyph (str): Associated glyph to display for this menu item.
                    click_fn (Callable): This callback function is executed when the menu item is clicked. Function signature:
                        void fn(name: str, path: str), where name is menu name and path is absolute path to clicked item.
                    show_fn (Callable): Returns True to display this menu item. Function signature: bool fn(path: str).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
                    index (int): The postion that this menu item will be inserted to.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
        
                
        """
    def add_show_only_collection(self, collection_id: str):
        """
        
                Add a filter to show collections. If this collection filter is provided,
                only those that match the filter will be shown, other collections will be hidden.
                Otherwise all collections are shown.
        
                Args:
                    collection_id (str): the filter.
        
                
        """
    def connect_server(self, url: str, callback: typing.Callable = None):
        """
        
                Connects the server for given url.
        
                Args:
                    url (str): Given url.
                    callback (Callable): On successfully connecting the server, executes this callback. Function signature:
                        void callback(name: str, server_url: str)
        
                
        """
    def delete_context_menu(self, name: str):
        """
        
                Deletes the menu item, with the given name, from the context menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open').
        
                
        """
    def delete_detail_frame(self, name: str):
        """
        
                Deletes the specified detail subsection.
        
                Args:
                    name (str): Name previously assigned to the detail frame.
        
                
        """
    def delete_listview_menu(self, name: str):
        """
        
                Deletes the menu item, with the given name, from the list view menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open').
        
                
        """
    def destroy(self):
        """
        Destructor.
        """
    def find_subdirs_async(self, url: str, callback: typing.Callable) -> typing.List[str]:
        """
        
                Asynchronously executes callback on list of subdirectories at given url.
        
                Args:
                    url (str): Url.
                    callback (Callable): On success executes this callback with the list of subdir names. Function
                        signature: void callback(subdirs: List[str])
        
                
        """
    def find_subdirs_with_callback(self, url: str, callback: typing.Callable):
        """
        
                Executes callback on list of subdirectories at given url.
        
                Args:
                    url (str): Url.
                    callback (Callable): On success executes this callback with the list of subdir names. Function
                        signature: void callback(subdirs: List[str])
        
                
        """
    def get_current_directory(self) -> str:
        """
        
                Returns the current directory from the browser bar.
        
                Returns:
                    str: The system path, which may be different from the displayed path.
        
                
        """
    def get_current_selections(self, pane: int = 2) -> typing.List[str]:
        """
        
                Returns current selected as list of system path names.
        
                Args:
                    pane (int): Specifies pane to retrieve selections from, one of {TREEVIEW_PANE = 1, LISTVIEW_PANE = 2,
                        BOTH = None}.  Default LISTVIEW_PANE.
                Returns:
                    [str]: List of system paths (which may be different from displayed paths, e.g. bookmarks)
        
                
        """
    def get_filename(self) -> str:
        """
        
                Returns:
                    str: Currently selected filename.
                
        """
    def hide_loading_pane(self):
        """
        
                Hide the loading icon if it exist.
                
        """
    def navigate_to(self, url: str, callback: typing.Callable = None):
        """
        
                Navigates to the given url, expanding all parent directories in the path.
        
                Args:
                    url (str): The url to navigate to.
                    callback (Callable): On successfully finding the item, executes this callback. Function signature:
                        void callback(item: FileBrowserItem)
        
                
        """
    def navigate_to_async(self, url: str, callback: typing.Callable = None):
        """
        
                Asynchronously navigates to the given url, expanding the all parent directories in the path.
        
                Args:
                    url (str): The url to navigate to.
                    callback (Callable): On successfully finding the item, executes this callback. Function signature:
                        void callback(item: FileBrowserItem)
        
                
        """
    def refresh_current_directory(self):
        """
        Refreshes the current directory set in the browser bar.
        """
    def remove_collection(self, collection_id: str):
        """
        
                Remove custom collection from current content view.
                samples of collection: "My Computer", "Omniverse Bookmark", ...
        
                Args:
                    collection_id (str): Data id to remove.
        
                
        """
    def remove_show_only_collection(self, collection_id: str):
        """
        
                Remove the collection filter
        
                Args:
                    collection_id (str): The filter that previously added.
        
                
        """
    def select_items_async(self, url: str, filenames: typing.List[str] = list()) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Asynchronously select one or more items in the content view.
        
                Args:
                    url (str): Url.
                Keyword Args:
                    filenames (List[str]): A list of file names that to be selected
                
        """
    def set_current_directory(self, path: str):
        """
        
                Procedurally sets the current directory. Use this method to set the path in the browser bar.
        
                Args:
                    path (str): The full path name of the folder, e.g. "omniverse://ov-content/Users/me.
        
                
        """
    def set_filename(self, filename: str):
        """
        
                Sets the filename in the file bar, at bottom of the dialog. The file is not
                required to already exist.
        
                Args:
                    filename (str): The filename only (and not the fullpath), e.g. "myfile.usd".
        
                
        """
    def set_search_delegate(self, delegate):
        """
        
                Sets a custom search delegate for the tool bar.
        
                Args:
                    delegate (:obj:`SearchDelegate`): Object that creates the search widget.
        
                
        """
    def show_model(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel):
        """
        
                Displays the given model in the list view, overriding the default model.  For example, this model
                might be the result of a search.
        
                Args:
                    model (:obj:`FileBrowserModel`): Model to display.
        
                
        """
    def subscribe_client_bookmarks_changed(self):
        """
        Subscribe to omni.client bookmark changes.
        """
    def toggle_bookmark_from_path(self, name: str, path: str, is_bookmark: bool, is_folder: bool = True):
        """
        
                Adds/deletes the given bookmark with the specified path. If deleting, then the path argument
                is optional.
        
                Args:
                    name (str): Name to call the bookmark or existing name if delete.
                    path (str): Path to the bookmark.
                    is_bookmark (bool): True to add, False to delete.
                    is_folder (bool): Whether the item to be bookmarked is a folder.
        
                
        """
LISTVIEW_PANE: int = 2
TREEVIEW_PANE: int = 1
have_nucleus: bool = True
