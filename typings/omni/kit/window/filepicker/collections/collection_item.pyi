from __future__ import annotations
from abc import abstractmethod
import carb as carb
from collections import namedtuple
from datetime import datetime
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni import ui
import pathlib
import typing
__all__: list[str] = ['AddNewItem', 'CollectionItem', 'CollectionItemFields', 'FileBrowserItem', 'FileBrowserItemFields', 'ICON_PATH', 'abstractmethod', 'carb', 'datetime', 'namedtuple', 'omni', 'ui']
class AddNewItem(omni.kit.widget.filebrowser.model.FileBrowserItem):
    def __init__(self, name: str, icon: str = '/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.filepicker-2.13.3+8131b85d/icons/NvidiaDark/hdd_plus.svg'):
        """
        
                Item to add a new child.
        
                Args:
                    name (str): Name of the item.
                    icon (str): Icon of the item.
                
        """
    def add_new(self, on_success_fn: typing.Callable[[str, str, bool, bool], NoneType]) -> None:
        """
        
                Add a new child. Override this method to show UI to add a new child.
        
                Args:
                    on_success_fn (Callable[[str, str, bool, bool], None]): Callback function that is called when the child is added.
                        The function signature is: def on_success_fn(name: str, path: str, publish_event: bool, auto_select: bool) -> None:
                
        """
class CollectionItem(omni.kit.widget.filebrowser.model.FileBrowserItem):
    def __init__(self, identifier: str, title: str, icon: str, access: int = 3, populated: bool = True, order = 10000):
        """
        
                Item for a collection which is a singleton that manages the a set of connections/bookmarks/drivers for the browser.
        
                Args:
                    identifier (str): Identifier of the collection. Could be "omniverse" or "https".
                    title (str): Title of the collection.
                    icon (str): Icon of the collection.
                    access (int): Access flags of the collection. Default is omni.client.AccessFlags.READ | omni.client.AccessFlags.WRITE.
                    populated (bool): Whether the collection is populated. Default is True. If False, will populate the collection when list children.
                    order (int): Order of the collection. Default is 10000.
                
        """
    def accept_url(self, url: str) -> bool:
        """
        
                Check if the url is accepted by the collection.
        
                Args:
                    url (str): Url to check.
        
                Returns:
                    bool: True if the url is accepted, False otherwise.
                
        """
    def add_child(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> typing.Optional[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        ...
    def add_path(self, name: str, path: str, is_folder: bool = True) -> typing.Optional[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Add a path to the collection.
        
                Args:
                    name (str): Name the path.
                    path (str): Path.
                    is_folder (bool): Whether the path represents a folder.
        
                Returns:
                    Optional[:obj:`FileBrowserItem`]: The added child item.
                
        """
    def create_add_new_item(self) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.AddNewItem]:
        """
        
                Create a item to add a new connection. Override this method to create a custom item.
        
                Returns:
                    Optional[:obj:`AddNewItem`]: Item to add a new connection. None if the collection does not support adding new connections.
                
        """
    def create_child_item(self, name: str, path: str, is_folder: bool = True) -> typing.Optional[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Create a connection item. Override this method to create a custom connection item.
        
                Args:
                    name (str): Name of the item.
                    path (str): Path of the item.
                    is_folder (bool): Whether the item is a folder.
        
                Returns:
                    Optional[:obj:`FileBrowserItem`]: The created child item.
                
        """
    @property
    def add_new_item(self) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.AddNewItem]:
        """
        Optional[:obj:`AddNewItem`]: Add new connection item.
        """
    @property
    def children(self) -> typing.Dict[str, omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        dict[:obj:`FileBrowserItem`]: Children of this item.  Does not populate the item if not already populated.
        """
    @property
    def children_list(self) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        List[:obj:`FileBrowserItem`]: List of avalible children of this item. Does not include the add new connection item.
        """
    @property
    def connections(self) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        List[:obj:`FileBrowserItem`]: List of connections of this item.
        """
class CollectionItemFields(tuple):
    """
    CollectionItemFields(name, date, size, permissions, order)
    """
    __match_args__: typing.ClassVar[tuple] = ('name', 'date', 'size', 'permissions', 'order')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('name', 'date', 'size', 'permissions', 'order')
    @staticmethod
    def __new__(_cls, name, date, size, permissions, order):
        """
        Create new instance of CollectionItemFields(name, date, size, permissions, order)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new CollectionItemFields object from a sequence or iterable
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
        Return a new CollectionItemFields object replacing specified fields with new values
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.filepicker-2.13.3+8131b85d/icons/NvidiaDark')
