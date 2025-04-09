from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb import events
from carb import log_warn
import omni as omni
from omni.kit import async_engine
from omni.kit.widget.filebrowser.filesystem_model import FileSystemModel
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.widget.filebrowser.nucleus_model import NucleusConnectionItem
from omni.kit.widget.filebrowser.nucleus_model import NucleusModel
from omni.kit.widget.filebrowser.widget import FileBrowserWidget
from omni.kit.window.filepicker.bookmark_model import BookmarkItem
from omni.kit.window.filepicker.bookmark_model import BookmarkModel
from omni.kit.window.filepicker.collection_data import CollectionData
from omni.kit.window.filepicker.model import FilePickerModel
from omni.kit.window.filepicker.utils import exec_after_redraw
from omni.kit.window.filepicker.utils import get_user_folders_dict
import os as os
import pathlib
import platform as platform
import traceback as traceback
import typing
__all__: list = ['FilePickerView']
class FilePickerView:
    """
    
        An embeddable UI component for browsing the filesystem. This widget is more full-functioned
        than :obj:`FileBrowserWidget` but less so than :obj:`FilePickerWidget`. More specifically, this is one of
        the 3 sub-components of its namesake :obj:`FilePickerWidget`. The difference is it doesn't have the Browser Bar
        (at top) or the File Bar (at bottom). This gives users the flexibility to substitute in other surrounding
        components instead.
    
        Args:
            title (str): Widget title. Default None.
    
        Keyword Args:
            layout (int): The overall layout of the window, one of: {LAYOUT_SPLIT_PANES, LAYOUT_SINGLE_PANE_SLIM,
                LAYOUT_SINGLE_PANE_WIDE, LAYOUT_DEFAULT}. Default LAYOUT_SPLIT_PANES.
            splitter_offset (int): Position of vertical splitter bar. Default 300.
            show_grid_view (bool): Display grid view in the intial layout. Default True.
            show_recycle_widget (bool): Display recycle widget in the intial layout. Default False.
            grid_view_scale (int): Scales grid view, ranges from 0-5. Default 2.
            on_toggle_grid_view_fn (Callable): Callback after toggle grid view is executed. Default None.
            on_scale_grid_view_fn (Callable): Callback after scale grid view is executed. Default None.
            show_only_collections (list[str]): List of collections to display, any combination of ["bookmarks",
                "omniverse", "my-computer"]. If None, then all are displayed. Default None.
            tooltip (bool): Display tooltips when hovering over items. Default True.
            allow_multi_selection (bool): Allow multiple items to be selected at once. Default False.
            mouse_pressed_fn (Callable): Function called on mouse press. Function signature:
                void mouse_pressed_fn(pane: int, button: int, key_mode: int, item: :obj:`FileBrowserItem`)
            mouse_double_clicked_fn (Callable): Function called on mouse double click.  Function signature:
                void mouse_double_clicked_fn(pane: int, button: int, key_mode: int, item: :obj:`FileBrowserItem`)
            selection_changed_fn (Callable): Function called when selection changed. Function signature:
                void selection_changed_fn(pane: int, selections: list[:obj:`FileBrowserItem`])
            drop_handler (Callable): Function called to handle drag-n-drops.
                Function signature: void drop_fn(dst_item: :obj:`FileBrowserItem`, src_paths: [str])
            item_filter_fn (Callable): This handler should return True if the given tree view item is visible,
                False otherwise. Function signature: bool item_filter_fn(item: :obj:`FileBrowserItem`)
            thumbnail_provider (Callable): This callback returns the path to the item's thumbnail. If not specified,
                then a default thumbnail is used. Signature: str thumbnail_provider(item: :obj:`FileBrowserItem`).
            icon_provider (Callable): This callback provides an icon to replace the default in the tree view.
                Signature str icon_provider(item: :obj:`FileBrowserItem`)
            badges_provider (Callable): This callback provides the list of badges to layer atop the thumbnail
                in the grid view. Callback signature: [str] badges_provider(item: :obj:`FileBrowserItem`)
            treeview_identifier (str): widget identifier for treeview, only used by tests.
            enable_zoombar (bool): Enables/disables zoombar. Default True.
        
    """
    _FilePickerView__connected_servers: typing.ClassVar[set] = set()
    _FilePickerView__placeholder_model: typing.ClassVar[omni.kit.widget.filebrowser.model.FileBrowserModel]  # value = <omni.kit.widget.filebrowser.model.FileBrowserModel object>
    @staticmethod
    def is_connected(url: str) -> bool:
        """
        
                 Check if a server is connected.
        
                 Args:
                      url: The url of the server
        
                 Returns:
                      True if the server is connected, False if not
                
        """
    def __init__(self, title: str, **kwargs):
        ...
    def _build_bookmarks_collection(self):
        ...
    def _build_computer_collection(self):
        ...
    def _build_omniverse_collection(self):
        ...
    def _build_ui(self):
        """
         
        """
    def _find_item_with_callback(self, path: str, callback: typing.Callable):
        """
        
                Wrapper around FilePickerModel.find_item_with_callback. This is a workaround for accessing the
                model's class method, which in hindsight should've been made a utility function.
        
                
        """
    def _is_placeholder(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        """
        
                Returns True if given item is the placeholder item.
        
                Returns:
                    bool
        
                
        """
    def _on_connection_failed(self, event: carb.events._events.IEvent):
        ...
    def _on_connection_succeeded(self, event: carb.events._events.IEvent):
        ...
    def _server_status_changed(self, url: str, status: omni.client.impl._omniclient.ConnectionStatus) -> None:
        """
        Updates NucleuseConnectionItem signed in status based upon server status changed.
        """
    def add_bookmark(self, name: str, path: str, is_folder: bool = True, publish_event: bool = True) -> omni.kit.window.filepicker.bookmark_model.BookmarkItem:
        """
        
                Creates a :obj:`FileBrowserModel` rooted at the given path, and connects its subtree to the
                tree view.
        
                Args:
                    name (str): Name of the bookmark.
                    path (str): Fullpath of the connection, e.g. "omniverse://ov-content". Paths to
                        Omniverse servers should contain the prefix, "omniverse://".
                    is_folder (bool): If the item to be bookmarked is a folder or not. Default to True.
                    publish_event (bool): If True, push a notification to the event stream.
        
                Returns:
                    :obj:`BookmarkItem`
        
                
        """
    def add_custom_collection(self, collection_data: omni.kit.window.filepicker.collection_data.CollectionData):
        ...
    def add_server(self, name: str, path: str, publish_event: bool = True, auto_select: bool = True) -> omni.kit.widget.filebrowser.model.FileBrowserModel:
        """
        
                Creates a :obj:`FileBrowserModel` rooted at the given path, and connects its subtree to the
                tree view.
        
                Args:
                    name (str): Name, label really, of the connection.
                    path (str): Fullpath of the connection, e.g. "omniverse://ov-content". Paths to
                        Omniverse servers should contain the prefix, "omniverse://".
                    publish_event (bool): If True, push a notification to the event stream.
        
                Returns:
                    :obj:`FileBrowserModel`
        
                Raises:
                    :obj:`RuntimeWarning`: If unable to add server.
        
                
        """
    def all_collection_items(self, collection: str = None) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Returns all connections as items for the specified collection. If collection is 'None', then return connections
                from all collections.
        
                Args:
                    collection (str): One of ['bookmarks', 'omniverse', 'my-computer']. Default None.
        
                Returns:
                    List[FileBrowserItem]: All connections found.
        
                
        """
    def delete_bookmark(self, item: omni.kit.window.filepicker.bookmark_model.BookmarkItem, publish_event: bool = True):
        """
        
                Deletes the given bookmark.
        
                Args:
                    item (:obj:`FileBrowserItem`): Bookmark item.
                    publish_event (bool): If True, push a notification to the event stream.
        
                
        """
    def delete_server(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, publish_event: bool = True):
        """
        
                Disconnects the subtree rooted at the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): Root of subtree to disconnect.
                    publish_event (bool): If True, push a notification to the event stream.
        
                
        """
    def destroy(self):
        """
         Destructor 
        """
    def get_connection_with_url(self, url: str) -> typing.Optional[omni.kit.widget.filebrowser.nucleus_model.NucleusConnectionItem]:
        """
        
                Gets the connection item with the given url.
        
                Args:
                    name (str): name (could be aliased name) of connection
        
                Returns:
                    NucleusConnectionItem
                
        """
    def get_root(self, pane: int = None) -> omni.kit.widget.filebrowser.model.FileBrowserItem:
        """
        
                Returns the root item of the specified pane.
        
                Args:
                    pane (int): One of {TREEVIEW_PANE, LISTVIEW_PANE}.
                
        """
    def get_selections(self, pane: int = 2) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Returns list of currently selected items.
        
                Args:
                    pane (int): One of {TREEVIEW_PANE, LISTVIEW_PANE}.
        
                Returns:
                    list[:obj:`FileBrowserItem`]
        
                
        """
    def has_connection_with_name(self, name: str, collection: str = None) -> bool:
        """
        
                Returns True if named connection exists within the collection.
        
                Args:
                    name (str): name (could be aliased name) of connection
                    collection (str): One of {'bookmarks', 'omniverse', 'my-computer'}. Default None.
        
                Returns:
                    bool
        
                
        """
    def hide_notification(self):
        """
        Utility to hide the notification frame.
        """
    def is_bookmark(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, path: typing.Optional[str] = None) -> bool:
        """
        
                Returns true if given item is a bookmarked item, or if a given path is bookmarked.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item in question.
                    path (Optional[str]): Path in question.
        
                Returns:
                    bool
        
                
        """
    def is_collection_node(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        """
        
                Returns true if given item is a collection node.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item in question.
        
                Returns:
                    bool
        
                
        """
    def is_collection_root(self, url: str = None) -> bool:
        """
        
                Returns True if the given url is a collection root url.
        
                Args:
                    url (str): The url to query. Default None.
        
                Returns:
                    bool: The result.
                
        """
    def is_connection_point(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        """
        
                Returns true if given item is a direct child of a collection node.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item in question.
        
                Returns:
                    bool
        
                
        """
    def is_local_point(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        """
        
                Returns true if given item is a direct child of a my-computer's node.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item in question.
        
                Returns:
                    bool
        
                
        """
    def log_out_server(self, item: omni.kit.widget.filebrowser.nucleus_model.NucleusConnectionItem):
        """
        
                Log out from the server at the given path.
        
                Args:
                    item (:obj:`NucleusConnectionItem`): Connection item.
        
                
        """
    def mount_user_folders(self, folders: dict):
        """
        
                Mounts given set of user folders under the local collection.
        
                Args:
                    folders (dict): Name, path pairs.
        
                
        """
    def reconnect_server(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        """
        
                Reconnects the server at the given path. Clears out any cached authentication tokens to force the action.
        
                Args:
                    item (:obj:`FileBrowserItem`): Connection item.
        
                
        """
    def refresh_ui(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem = None):
        """
        
                Redraws the subtree rooted at the given item. If item is None, then redraws entire tree.
        
                Args:
                    item (:obj:`FileBrowserItem`): Root of subtree to redraw. Default None, i.e. root.
        
                
        """
    def remove_collection(self, collection_id: str):
        ...
    def rename_bookmark(self, item: omni.kit.window.filepicker.bookmark_model.BookmarkItem, new_name: str, new_url: str, publish_event: bool = True):
        """
        
                Renames the bookmark item. Note: doesn't change the connection itself, only how it's labeled
                in the tree view.
        
                Args:
                    item (:obj:`FileBrowserItem`): Bookmark item.
                    new_name (str): New name.
                    new_url (str): New url address.
                    publish_event (bool): If True, push a notification to the event stream.
        
                
        """
    def rename_server(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, new_name: str, publish_event: bool = True):
        """
        
                Renames the connection item. Note: doesn't change the connection itself, only how it's labeled
                in the tree view.
        
                Args:
                    item (:obj:`FileBrowserItem`): Root of subtree to disconnect.
                    new_name (str): New name.
                    publish_event (bool): If True, push a notification to the event stream.
        
                
        """
    def scale_grid_view(self, scale: float):
        """
        
                Scale file picker's grid view icon size.
        
                Args:
                    scale (float): Scale of the icon.
        
                
        """
    def select_and_center(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        """
        
                Selects and centers the view on the given item, expanding the tree if needed.
        
                Args:
                    item (:obj:`FileBrowserItem`): The selected item.
        
                
        """
    def set_item_filter_fn(self, item_filter_fn: typing.Callable[[str], bool]):
        """
        
                Sets the item filter function.
        
                Args:
                    item_filter_fn (Callable): Signature is bool fn(item: FileBrowserItem)
        
                
        """
    def set_selections(self, selections: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem], pane: int = 1):
        """
        
                Selected given items in given pane.
        
                ARGS:
                    selections (list[:obj:`FileBrowserItem`]): list of selections.
                    pane (int): One of TREEVIEW_PANE, LISTVIEW_PANE, or None for both. Default None.
        
                
        """
    def show_connect_dialog(self):
        """
        Displays the add connection dialog.
        """
    def show_model(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel):
        """
        Displays the model on the right side of the split pane
        """
    def show_notification(self):
        """
        Utility to show the notification frame.
        """
    def toggle_grid_view(self, show_grid_view: bool):
        """
        
                Toggles file picker between grid and list view.
        
                Args:
                    show_grid_view (bool): True to show grid view, False to show list view.
        
                
        """
    @property
    def collections(self):
        """
        dict: Dictionary of collections, e.g. 'bookmarks', 'omniverse', 'my-computer'.
        """
    @property
    def filebrowser(self):
        """
         Gets the filebrowser of this view. 
        """
    @property
    def notification_frame(self):
        """
        The notification frame.
        """
    @property
    def show_grid_view(self):
        """
        
                Gets file picker stage of grid or list view.
        
                Returns:
                    bool: True if grid view shown or False if list view shown.
        
                
        """
    @property
    def show_only_collections(self):
        """
         Gets the collections list only to show.
        """
    @property
    def show_udim_sequence(self):
        """
         Whether or not to show UDIM sequence. 
        """
    @show_udim_sequence.setter
    def show_udim_sequence(self, value: bool):
        """
         Show or hides UDIM sequence. 
        """
BOOKMARK_ADDED_EVENT: int = 14293204382964729133
BOOKMARK_DELETED_EVENT: int = 12591526458620793410
BOOKMARK_RENAMED_EVENT: int = 2010616043326768797
CONNECTION_ERROR_EVENT: int = 1730322306128580327
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons/NvidiaDark')
LAYOUT_DEFAULT: int = 3
LISTVIEW_PANE: int = 2
NUCLEUS_CONNECTION_SUCCEEDED_EVENT: int = 12539978195413966289
NUCLEUS_SERVER_ADDED_EVENT: int = 2703271046647040724
NUCLEUS_SERVER_DELETED_EVENT: int = 7113468990364096071
NUCLEUS_SERVER_RENAMED_EVENT: int = 8294859433106236004
TREEVIEW_PANE: int = 1
have_nucleus: bool = True
