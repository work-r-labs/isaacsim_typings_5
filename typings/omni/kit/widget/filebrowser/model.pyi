from __future__ import annotations
import asyncio as asyncio
from carb import log_warn
from collections import OrderedDict
from collections import namedtuple
from datetime import datetime
import omni as omni
from omni.kit import async_engine
from omni.kit.helper.file_utils import asset_types
from omni.kit.widget.filebrowser.date_format_menu import get_datetime_format
from omni.kit.widget.filebrowser.thumbnails import list_thumbnails_for_folder_async
from omni import ui
import os as os
import re as re
import threading as threading
import typing
__all__: list = ['FileBrowserItem', 'FileBrowserItemFactory', 'FileBrowserModel']
class FileBrowserItem(omni.ui._ui.AbstractItem):
    """
    
        Base class for the Filebrowser view Item.
        Should be sub-classed to implement specific filesystem behavior. The Constructor should not be
        called directly.  Instead there are factory methods available for creating instances when needed.
    
        Args:
            path (str): Path of the item.
            fields (:obj:`FileBrowserItemFields`): Fields of the item.
            is_folder (bool): Set to True if the item is a folder.
            is_deleted (bool): Set to True if the item is deleted.
        
    """
    @staticmethod
    def datetime_as_string(value: datetime) -> str:
        """
         Convert datatime to string. 
        """
    @staticmethod
    def size_as_string(value: int) -> str:
        """
         Convert data size in bytes to a human readable string. 
        """
    def __init__(self, path: str, fields: FileBrowserItemFields, is_folder: bool = False, is_deleted: bool = False):
        ...
    def add_child(self, item: typing.Any):
        """
        
                Add item as child.
        
                Args:
                    item (:obj:`FileBrowserItem`): Child item.
        
                
        """
    def del_child(self, item_name: str):
        """
        
                Delete child item by name.
        
                Args:
                    item_name (str): Name of child item.
        
                
        """
    def get_custom_thumbnails_for_folder_async(self) -> dict:
        """
        
                Return the thumbnail dictionary for this (folder) item.
        
                Returns:
                    Dict: With children url's as keys, and url's to thumbnail files as values.
        
                
        """
    def get_subitem_model(self, index: int) -> typing.Any:
        """
        
                Return ith column of this item.
        
                Returns:
                    :obj:`AbstractValueModel`
        
                
        """
    def has_mouse_pressed_fn(self):
        """
         Check if the item has a mouse pressed callback assigned. 
        """
    def mouse_pressed_fn(self):
        """
         Mouse pressed callback. 
        """
    def on_list_change_event(self, event: omni.client.ListEvent, entry: omni.client.ListEntry) -> bool:
        """
        
                Virtual method to be implemented by sub-class. When called with a ListEvent, should update
                this item's children list with the corresponding ListEntry.
        
                Args:
                    event (:obj:`omni.client.ListEvent`): One of of {UNKNOWN, CREATED, UPDATED, DELETED, METADATA, LOCKED, UNLOCKED}.
                    entry (:obj:`omni.client.ListEntry`): Updated entry as defined by omni.client.
        
                
        """
    def on_populated_async(self, result = None, children: dict[str, FileBrowserItem] | None = None, callback: typing.Callable[[dict[str, FileBrowserItem]], None] | None = None):
        """
        
                async callback after finish populating the item.
        
                Args:
                    result(Any): result from populate async.
                    children(Dict[str, :obj:`FileBrowserItem`]): dictionary of children items to pass to the callback.
                    callback(Callable): function to call.Function signature:
                        callback(result: Any, children: Dict[str, FileBrowserItem]) -> None
        
                
        """
    def populate_async(self, callback_async: typing.Callable = None, timeout: float = 10.0) -> typing.Any:
        """
        
                Populate current item asynchronously if not already. Override this method to customize for specific
                file systems.
        
                Args:
                    callback_async (Callable): Function signature is void callback(result, children: Dict[str, FileBrowserItem]),
                        where result is an Exception type upon error.
                    timeout (float): Time out duration on failed server connections. Default 10.0.
        
                Returns:
                    Any: Result of executing callback.
        
                
        """
    def populate_with_callback(self, callback: typing.Callable, timeout: float = 10.0):
        """
        
                Populate this item if not already populated. When done, executes callback.
        
                Args:
                    callback (Callable): Function signature is void callback(children: [FileBrowserItem]).
                    timeout (float): Time out duration on failed server connections. Default 10.0.
        
                
        """
    def update_permissions(self, new_permissions: 'omni.client.AccessFlags'):
        """
        
                Update item's permissions.
        
                Args:
                    new_permissions(:obj:'omni.client.AccessFlags'): New permissions to this item.
                
        """
    @property
    def alert(self) -> tuple[int, str]:
        """
         Get/set alert level and message. 
        """
    @alert.setter
    def alert(self, alert: tuple[int, str]):
        ...
    @property
    def children(self) -> dict[str, FileBrowserItem]:
        """
        dict[:obj:`FileBrowserItem`]: Children of this item.  Does not populate the item if not already populated.
        """
    @property
    def context_menu(self) -> 'BaseContextMenu' | None:
        """
         Optionally provide a context menu to be show when this item is right-clicked. 
        """
    @property
    def enable_sorting(self) -> bool:
        """
        bool: True if item's children are sortable.
        """
    @property
    def expandable(self) -> bool:
        """
        whether this FileBrowserItem is expandable. Override to change behavior
        """
    @property
    def fields(self) -> FileBrowserItemFields:
        """
        :obj:`FileBrowserItemFields`: A subset of the item's stats stored as a string tuple.
        """
    @property
    def hideable(self) -> bool:
        """
        whether this FileBrowserItem is hideable. Override to change behavior
        """
    @property
    def icon(self) -> str:
        """
        str: Get/set path to icon file.
        """
    @icon.setter
    def icon(self, icon: str):
        ...
    @property
    def is_deleted(self) -> bool:
        """
        bool: True if this item is a deleted folder/file.
        """
    @is_deleted.setter
    def is_deleted(self, value: bool):
        ...
    @property
    def is_folder(self) -> bool:
        """
        bool: True if this item is a folder.
        """
    @property
    def is_udim_file(self) -> bool:
        """
        bool: Get/Set item udim_file state.
        """
    @is_udim_file.setter
    def is_udim_file(self, value: bool):
        ...
    @property
    def item_changed(self) -> bool:
        """
        bool: True if this item is has been restore/delete aready.
        """
    @item_changed.setter
    def item_changed(self, value: bool):
        ...
    @property
    def models(self) -> tuple:
        """
        Tuple[:obj:`ui.AbstractValueModel`]: The columns of this item.
        """
    @property
    def name(self) -> str:
        """
        str: Item name.
        """
    @property
    def parent(self) -> typing.Any:
        """
        :obj:`FileBrowserItem`: Parent of this item.
        """
    @property
    def path(self) -> str:
        """
        str: Full path name.
        """
    @property
    def populated(self) -> bool:
        """
        bool: Get/Set item populated state.
        """
    @populated.setter
    def populated(self, value: bool):
        ...
    @property
    def readable(self) -> bool:
        """
         True if the item is readable. 
        """
    @property
    def writeable(self) -> bool:
        """
         True if the item is writeable. 
        """
class FileBrowserItemFactory:
    """
    
        Factory to create :obj:`FileBrowserItem` instances.
        
    """
    @staticmethod
    def create_dummy_item(name: str, path: str) -> FileBrowserItem:
        """
        
                Create a dummy item at the given path.
        
                Args:
                    name (str): name of the item.
                    path (str): path of the item.
                
        """
    @staticmethod
    def create_group_item(name: str, path: str) -> FileBrowserItem:
        """
        
                Create a folder item at the given path.
        
                Args:
                    name (str): name of the item.
                    path (str): path of the item.
                
        """
    @staticmethod
    def create_udim_item(name: str, path: str, range_start: int, range_end: int, repr_frame: int):
        """
        
                Create a UDIM item.
        
                Args:
                    name (str): name of the item.
                    path (str): path of the item.
                    range_start (int): Starting index of UDIM sequence.
                    range_end (int): End index of UDIM sequence.
                    repr_frame (int): Index in UDIM sequence.
                
        """
class FileBrowserItemFields(tuple):
    """
    FileBrowserItemFields(name, date, size, permissions)
    """
    __match_args__: typing.ClassVar[tuple] = ('name', 'date', 'size', 'permissions')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('name', 'date', 'size', 'permissions')
    @staticmethod
    def __new__(_cls, name, date, size, permissions):
        """
        Create new instance of FileBrowserItemFields(name, date, size, permissions)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new FileBrowserItemFields object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new FileBrowserItemFields object replacing specified fields with new values
        """
class FileBrowserModel(omni.ui._ui.AbstractItemModel):
    """
    
        Base class for the Filebrowser view Model.
        Should be sub-classed to implement specific filesystem behavior.
    
        Args:
            name (str): Name of root item. If None given, then create an initally empty model.
    
        Keyword Args:
            drop_fn (Callable): Function called to handle drag-n-drops. Function signature:
                void drop_fn(dst_item: :obj:`FileBrowserItem`, src_item: :obj:`FileBrowserItem`)
            filter_fn (Callable): This handler should return True if the given Filebrowser view item is visible,
                False otherwise. Function signature: bool filter_fn(item: :obj:`FileBrowserItem`)
            sort_by_field (str): Name of column by which to sort items in the same folder. Default "name".
            sort_ascending (bool): Sort in ascending order. Default True.
            timeout (float): Timeout when updating item asynchronously.
        
    """
    def __init__(self, name: str = None, root_path: str = '', **kwargs):
        ...
    def _delayed_item_changed(self, item: FileBrowserItem, throttle_frames: int = 1):
        """
        
                Produce item changed event after skipping a beat. This is necessary for guaranteeing that async updates
                are properly recognized and generate their own redraws.
        
                Args:
                    item (:obj:`FileBrowserItem`): The item in question.
        
                
        """
    def auto_refresh_item(self, item: FileBrowserItem, throttle_frames: int = 4):
        """
        
                Watch the given folder and updates the children list as soon as its contents are changed.
        
                Args:
                    item (:obj:`FileBrowserItem`): The folder item to watch.
                    throttle_frames: Number of frames to throttle the UI refresh.
        
                
        """
    def copy_presets(self, model: 'FileBrowserModel'):
        """
         Reset our fields to default arguments from the given model. 
        """
    def destroy(self):
        """
         Destructor. 
        """
    def drop(self, dst_item: FileBrowserItem, source: str | FileBrowserItem):
        """
        
                Invoke user-supplied function to handle dropping source onto destination item.
        
                Args:
                    dst_item (:obj:`FileBrowserItem`): Target item.
                    src_item (:obj:`FileBrowserItem`): Source item.
        
                
        """
    def drop_accepted(self, dst_item: FileBrowserItem, src_item: FileBrowserItem) -> bool:
        """
        
                Reimplemented from AbstractItemModel. Called to highlight target when drag and drop.
                Returns True if destination item is able to accept a drop. This function can be
                overriden to implement a different behavior.
        
                Args:
                    dst_item (:obj:`FileBrowserItem`): Target item.
                    src_item (:obj:`FileBrowserItem`): Source item.
        
                Returns:
                    bool
        
                
        """
    def filter_items(self, items: list[FileBrowserItem]) -> list[FileBrowserItem]:
        """
        
                Return the items fitlered with the filter function set.
                
        """
    def get_drag_mime_data(self, item: FileBrowserItem):
        """
        Return Multipurpose Internet Mail Extensions (MIME) data for be able to drop this item somewhere
        """
    def get_item_children(self, item: FileBrowserItem) -> [FileBrowserItem]:
        """
        
                Return the list of items that are nested to the given parent item.
        
                Args:
                    item (:obj:`FileBrowserItem`): Parent item.
        
                Returns:
                    list[:obj:`FileBrowserItem`]
        
                
        """
    def get_item_value_model(self, item: FileBrowserItem, index: int) -> typing.Any:
        """
        
                Get the value model associated with this item.
        
                Args:
                    item (:obj:`FileBrowserItem`): The item in question.
        
                Returns:
                    :obj:`AbstractValueModel`
        
                
        """
    def get_item_value_model_count(self, item: FileBrowserItem) -> int:
        """
        
                Return the number of columns this model item contains.
        
                Args:
                    item (:obj:`FileBrowserItem`): The item in question.
        
                Returns:
                    int
        
                
        """
    def on_list_change_event(self, item: FileBrowserItem, result: omni.client.Result, event: omni.client.ListEvent, entry: omni.client.ListEntry, throttle_frames: int = 4):
        """
        
                Process change events for the given folder.
        
                Args:
                    item (:obj:`FileBrowserItem`): The folder item.
                    result (omni.client.Result): Set by omni.client upon listing the folder.
                    event (omni.client.ListEvent): Event type.
                    throttle_frames: Number of frames to throttle the UI refresh.
        
                
        """
    def set_filter_fn(self, filter_fn: typing.Callable[[str], bool]):
        """
         Set the handler that would return True if the given Filebrowser view item is visible,
                    False otherwise. Function signature: bool filter_fn(item: :obj:`FileBrowserItem`)
        """
    def sync_up_item_changes(self, item: FileBrowserItem):
        """
        
                Scan given folder for missed changes; processes any changes found.
        
                Args:
                    item (:obj:`FileBrowserItem`): The folder item to watch.
        
                
        """
    @property
    def builtin_column_count(self):
        """
        Return the number of available columns without tag delegates
        """
    @property
    def drag_mime_data(self):
        """
        
                Return the string with the drag and drop payload.
                
        """
    @drag_mime_data.setter
    def drag_mime_data(self, data: str | list[str]):
        ...
    @property
    def root(self) -> FileBrowserItem:
        """
        :obj:`FileBrowserItem`: Get/set the root item of this model.
        """
    @root.setter
    def root(self, item: FileBrowserItem):
        ...
    @property
    def show_udim_sequence(self):
        """
         Show the UDIM sequence. 
        """
    @show_udim_sequence.setter
    def show_udim_sequence(self, value: bool):
        ...
    @property
    def single_column(self):
        """
        The panel on the left side works in one-column mode
        """
    @single_column.setter
    def single_column(self, value: bool):
        """
        Set the one-column mode
        """
    @property
    def sort_ascending(self) -> bool:
        """
        :obj:`FileBrowserItem`: Get/set the sort ascending state.
        """
    @sort_ascending.setter
    def sort_ascending(self, value: bool):
        ...
    @property
    def sort_by_field(self) -> str:
        """
        :obj:`FileBrowserItem`: Get/set the sort-by field name.
        """
    @sort_by_field.setter
    def sort_by_field(self, field: str):
        ...
class FileBrowserUdimItem(FileBrowserItem):
    """
    
        A Filebrowser UDIM item class for navigating a the local filesystem in a Filebrowser view.
        Sub-classed from :obj:`FileBrowserItem`.
    
        Args:
            path (str): path of the item.
            fields (:obj:`FileBrowserItemFields`): Fields of the item.
            is_folder (bool): Specify the item as a folder.
            range_start (int): Starting index of UDIM sequence.
            range_end (int): End index of UDIM sequence.
            repr_frame (int): Index in UDIM sequence.
        
    """
    @staticmethod
    def get_udim_sequence(full_path: str):
        """
         Get the UDIM sequence by path. 
        """
    @staticmethod
    def populate_udim(parent: FileBrowserItem):
        """
         Generate UDIM items under the given item. 
        """
    def __init__(self, path: str, fields: FileBrowserItemFields, range_start: int, range_end: int, repr_frame: int = None):
        ...
    @property
    def repr_path(self) -> str:
        """
        str: Full thumbnail path name.
        """
class NoLock:
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    def __init__(self):
        ...
def handle_item_creation_exception(func: typing.Callable):
    ...
BUILTIN_COLUMNS: int = 4
CONNECTION_ERROR_EVENT: int = 1730322306128580327
compiled_regex = None
