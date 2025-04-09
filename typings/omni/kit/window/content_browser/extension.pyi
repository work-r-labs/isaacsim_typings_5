from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.menu.utils.extension_window_helper import MenuHelperExtension
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.window.content_browser.api import ContentBrowserAPI
from omni.kit.window.content_browser.hotkey import ContentHotkeys
from omni.kit.window.content_browser.window import ContentBrowserWindow
from omni.kit.window import content_browser_registry as registry
from omni.kit.window.filepicker.collection_data import CollectionData
from omni import ui
import os as os
__all__ = ['CollectionData', 'ContentBrowser', 'ContentBrowserAPI', 'ContentBrowserWindow', 'ContentHotkeys', 'FILE_OPENED_EVENT', 'FileBrowserItem', 'FileBrowserModel', 'MenuHelperExtension', 'UI_READY_EVENT', 'asyncio', 'carb', 'g_api_singleton', 'get_content_instance', 'get_instance', 'omni', 'os', 'partial', 'registry', 'ui']
class ContentBrowser:
    """
    The Content Browser extension API
    
        This class serves as the API of the Content Browser extension. It manages the extension's API.
        
    """
    def __init__(self):
        """
        Initializes the ContentBrowserExtension instance.
        """
    def _destroy(self):
        ...
    def add_checkpoint_menu(self, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index = -1) -> str:
        """
        
                Add menu item, with corresponding callbacks, to checkpoint items.
        
                Args:
                    name (str): Name of the menu item, this name must be unique across the menu.
                    glyph (str): Associated glyph to display for this menu item.
                    click_fn (Callable): This callback function is executed when the menu item is clicked. Function signature:
                        void fn(name: str, path: str), where name is menu name and path is absolute path to clicked item.
                    show_fn (Callable): Returns True to display this menu item. Function signature: bool fn(path: str).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
                    index (int): The position that this menu item will be inserted to. By default, the item will be appened.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
                
        """
    def add_collection_data(self, collection_data: omni.kit.window.filepicker.collection_data.CollectionData):
        """
        Adds collection data to the browser.
        
                Args:
                    collection_data (CollectionData): The collection data to add.
        """
    def add_connections(self, connections: dict):
        """
        
                Adds specified server connections to the tree browser.
        
                Args:
                    connections (dict): A dictionary of name, path pairs. For example:
                        {"C:": "C:", "ov-content": "omniverse://ov-content"}.  Paths to Omniverse servers
                        should be prefixed with "omniverse://".
        
                
        """
    def add_context_menu(self, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index: int = 0, separator_name = '_add_on_end_separator_') -> str:
        """
        
        		Add menu item, with corresponding callbacks, to the context menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open'), this name must be unique across the context menu.
                    glyph (str): Associated glyph to display for this menu item.
                    click_fn (Callable): This callback function is executed when the menu item is clicked. Function signature is
                        void fn(name: str, path: str), where name is menu name and path is absolute path to clicked item.
                    show_fn (Callable): Returns True to display this menu item. Function signature - bool fn(path: str).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
                    index (int): The position that this menu item will be inserted to.
                    separator_name (str): The separator name of the separator menu item. Default to '_placeholder_'. When the
                        index is not explicitly set, or if the index is out of range, this will be used to locate where to add
                        the menu item; if specified, the index passed in will be counted from the saparator with the provided
                        name. This is for OM-86768 as part of the effort to match Navigator and Kit UX for Filepicker/Content Browser for context menus.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
        
                
        """
    def add_file_open_handler(self, name: str, open_fn: typing.Callable, file_type: typing.Union[int, typing.Callable]) -> str:
        """
        
                Registers callback/handler to open a file of matching type.
        
                Args:
                    name (str): Unique name of handler.
                    open_fn (Callable): This function is executed when a matching file is selected for open, i.e. double clicked,
                        right mouse menu open, or path submitted to browser bar.  Function signature:
                        void open_fn(full_path: str), full_path is the file's system path.
                    file_type (Union[int, func]): Can either be an enumerated int that is one of: [FILE_TYPE_USD,
                        FILE_TYPE_IMAGE, FILE_TYPE_SOUND, FILE_TYPE_TEXT, FILE_TYPE_VOLUME] or a more general boolean function
                        that returns True if this function should be activated on the given file.  Function
                        signature: bool file_type(full_path: str).
        
                Returns:
                    str - Name if successful, None otherwise.
        
                
        """
    def add_import_menu(self, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable) -> str:
        """
        
                Add menu item, with corresponding callbacks, to the Import combo box.
        
                Args:
                    name (str): Name of the menu item, this name must be unique across the menu.
                    glyph (str): Associated glyph to display for this menu item.
                    click_fn (Callable): This callback function is executed when the menu item is clicked. Function signature:
                        void fn(name: str, path: str), where name is menu name and path is absolute path to clicked item.
                    show_fn (Callable): Returns True to display this menu item. Function signature: bool fn(path: str).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
        
                
        """
    def add_listview_menu(self, name: str, glyph: str, click_fn: typing.Callable, show_fn: typing.Callable, index: int = -1) -> str:
        """
        
                Add menu item, with corresponding callbacks, to the list view menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open'), this name must be unique across the list view menu.
                    glyph (str): Associated glyph to display for this menu item.
                    click_fn (Callable): This callback function is executed when the menu item is clicked. Function signature:
                        void fn(name: str, path: str), where name is menu name and path is absolute path to clicked item.
                    show_fn (Callable): Returns True to display this menu item. Function signature: bool fn(path: str).
                        For example, test filename extension to decide whether to display a 'Play Sound' action.
                    index (int): The position that this menu item will be inserted to.
        
                Returns:
                    str: Name of menu item if successful, None otherwise.
        
                
        """
    def decorate_from_registry(self, event: carb.events._events.IEvent):
        """
        Decorates from registry based on the event.
        
                Args:
                    event (carb.events.IEvent): Event that triggers decoration.
        """
    def delete_checkpoint_menu(self, name: str):
        """
        
                Delete the menu item, with the given name, from context menu of checkpoint item.
        
                Args:
                    name (str): Name of the menu item.
                
        """
    def delete_context_menu(self, name: str):
        """
        
                Delete the menu item, with the given name, from the context menu.
        
                Args:
                    name (str): Name of the menu item (e.g. 'Open').
        
                
        """
    def delete_file_open_handler(self, name: str):
        """
        
                Unregisters the named file open handler.
        
                Args:
                    name (str): Name of the handler.
        
                
        """
    def delete_import_menu(self, name: str):
        """
        
                Delete the menu item, with the given name, from the Import combo box.
        
                Args:
                    name (str): Name of the menu item.
        
                
        """
    def delete_listview_menu(self, name: str):
        """
        
                Delete the menu item, with the given name, from the list view menu.
        
                Args:
                    name (str) - Name of the menu item (e.g. 'Open').
        
                
        """
    def get_checkpoint_widget(self) -> CheckpointWidget:
        """
        Gets the checkpoint widget.
        
                Returns:
                    CheckpointWidget: The checkpoint widget if present; otherwise, None.
        """
    def get_current_directory(self) -> str:
        """
        
                Returns the current directory fom the browser bar.
        
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
                    List[str]: List of system paths (which may be different from displayed paths, e.g. bookmarks)
        
                
        """
    def get_file_open_handler(self, url: str) -> typing.Callable:
        """
        Returns the matching file open handler for the given file path.
        
                Args:
                    url (str): The url of the file to open.
        
                Returns:
                    Callable: The function to handle the file open event for the given url if one exists; otherwise, None.
        """
    def get_timestamp_widget(self) -> TimestampWidget:
        """
        Gets the timestamp widget.
        
                Returns:
                    TimestampWidget: The timestamp widget if present; otherwise, None.
        """
    def navigate_to(self, url: str):
        """
        
                Navigates to the given url, expanding all parent directories along the path.
        
                Args:
                    url (str): The path to navigate to.
        
                
        """
    def navigate_to_async(self, url: str):
        """
        
                Asynchronously navigates to the given url, expanding all parent directories along the path.
        
                Args:
                    url (str): The url to navigate to.
        
                
        """
    def refresh_current_directory(self):
        """
        Refreshes the current directory set in the browser bar.
        """
    def remove_collection_data(self, collection_id: str):
        """
        Removes collection data from the browser.
        
                Args:
                    collection_id (str): Identifier of the collection to remove.
        """
    def select_items_async(self, url: str, filenames: typing.List[str] = list()) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Asynchronously selects display items by their names.
        
                Args:
                    url (str): Url of the parent folder.
                    filenames (List[str]): Names of items to select.
        
                Returns:
                    List[FileBrowserItem]: List of selected items.
        
                
        """
    def set_current_directory(self, path: str):
        """
        
                Procedurally sets the current directory path.
        
                Args:
                    path (str): The full path name of the folder, e.g. "omniverse://ov-content/Users/me.
        
                Raises:
                    RuntimeWarning: If path doesn't exist or is unreachable.
        
                
        """
    def set_search_delegate(self, delegate: SearchDelegate):
        """
        
                Sets a custom search delegate for the tool bar.
        
                Args:
                    delegate (SearchDelegate): Object that creates the search widget.
        
                
        """
    def show_model(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel):
        """
        
                Displays the given model in the list view, overriding the default model.  For example, this model
                might be the result of a search.
        
                Args:
                    model (FileBrowserModel): Model to display.
        
                
        """
    def show_window(self, menu, value):
        """
        Shows the Content Browser window, creating it if it does not exist.
        
                Args:
                    menu: The menu from which the show window action was triggered.
                    value (bool): The desired visibility state of the Content Browser window.
        """
    def subscribe_selection_changed(self, fn: typing.Callable):
        """
        
                Subscribes to file selection changes.
        
                Args:
                    fn (Callable): callback function when file selection changed.
        
                
        """
    def toggle_bookmark_from_path(self, name: str, path: str, is_bookmark: bool, is_folder: bool = True) -> bool:
        """
        
                Adds/deletes the given bookmark with the specified path. If deleting, then the path argument
                is optional.
        
                Args:
                    name (str): Name to call the bookmark or existing name if delete.
                    path (str): Path to the bookmark.
                    is_bookmark (bool): True to add, False to delete.
                    is_folder (bool): Whether the item to be bookmarked is a folder.
        
                Returns:
                    bool: True if successful.
        
                
        """
    def toggle_grid_view(self, show_grid_view: bool):
        """
        
                Toggles file picker between grid and list view.
        
                Args:
                    show_grid_view (bool): True to show grid view, False to show list view.
        
                
        """
    def unset_search_delegate(self, delegate: SearchDelegate):
        """
        
                Clears the custom search delegate for the tool bar.
        
                Args:
                    delegate (:obj:`SearchDelegate`): Object that creates the search widget.
        
                
        """
    def unsubscribe_selection_changed(self, fn: typing.Callable):
        """
        
                Unsubscribes this callback from selection changes.
        
                Args:
                    fn (Callable): callback function when file selection changed.
        
                
        """
    @property
    def api(self) -> omni.kit.window.content_browser.api.ContentBrowserAPI:
        """
        Gets the Content Browser API instance.
        
                Returns:
                    ContentBrowserAPI: The API instance if the extensions is present; otherwise, None.
        """
    @property
    def window(self) -> omni.ui._ui.Window:
        """
        Gets the main dialog window for this extension.
        
                Returns:
                    ui.Window: The associated window instance if present; otherwise, None.
        """
    @window.setter
    def window(self, window: omni.ui._ui.Window):
        """
        Set the main dialog window for this content browser api class.
        
                Args:
                    ui.Window: The associated window instance.
        """
def get_content_instance():
    ...
def get_instance():
    ...
FILE_OPENED_EVENT: int = 3872619916304892462
UI_READY_EVENT: int = 284649323482245942
g_api_singleton: ContentBrowser  # value = <omni.kit.window.content_browser.extension.ContentBrowser object>
