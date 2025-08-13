from __future__ import annotations
import carb as carb
from datetime import datetime
import omni.kit.widget.filebrowser.model
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.window.filepicker.collections.bookmark_collection import BookmarkCollectionItem
import omni.kit.window.filepicker.collections.collection_data
from omni.kit.window.filepicker.collections.collection_data import CollectionData
import omni.kit.window.filepicker.collections.collection_item
from omni.kit.window.filepicker.collections.collection_item import CollectionItem
from omni.kit.window.filepicker.collections.collection_item import CollectionItemFields
from omni.kit.window.filepicker.collections.filesystem_collection import FileSystemCollectionItem
from omni.kit.window.filepicker.collections.nucleus_collection import NucleusCollectionItem
from omni.kit.window.filepicker.collections.s3_collection import S3Collection
from omni import ui
__all__: list[str] = ['BookmarkCollectionItem', 'CollectionData', 'CollectionItem', 'CollectionItemFields', 'FileBrowserItem', 'FileBrowserModel', 'FileSystemCollectionItem', 'NavigationModel', 'NucleusCollectionItem', 'S3Collection', 'carb', 'datetime', 'ui']
class NavigationModel(omni.kit.widget.filebrowser.model.FileBrowserModel):
    def __init__(self, name: str, drop_fn: typing.Callable, filter_fn: typing.Callable, available_collections: str):
        """
        
                Model for the navigation tree view for collections and connections.
        
                Args:
                    name (str): Name of the model.
                    drop_fn (Callable): Drop function.
                    filter_fn (Callable): Filter function.
                    available_collections (str): Available collections. 
                
        """
    def add_collection(self, collection_item: omni.kit.window.filepicker.collections.collection_item.CollectionItem) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.CollectionItem]:
        """
        
                Add a collection item to the navigation model.
        
                Args:
                    collection_item (:obj:`CollectionItem`): Collection item.
        
                Returns:
                    :obj:`CollectionItem`: The added collection item.
                
        """
    def add_collection_by_data(self, collection_data: omni.kit.window.filepicker.collections.collection_data.CollectionData) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.CollectionItem]:
        """
        
                Add a collection to the navigation model by CollectionData.
        
                Args:
                    collection_data (:obj:`CollectionData`): Collection data.
        
                Returns:
                    :obj:`CollectionItem`: The added collection item.
                
        """
    def add_path(self, name: str, path: str) -> typing.Tuple[typing.Optional[omni.kit.window.filepicker.collections.collection_item.CollectionItem], typing.Optional[omni.kit.widget.filebrowser.model.FileBrowserItem]]:
        """
        
                Creates a :obj:`FileBrowserItem` at the given path.
        
                Args:
                    name (str): Name, label really, of the path.
                    path (str): Fullpath, e.g. "omniverse://ov-content". Paths to
                        Omniverse servers should contain the prefix, "omniverse://".
        
                Returns:
                    Tuple[:obj:`CollectionItem`, :obj:`FileBrowserItem`]: The added collection item and child item.
        
                Raises:
                    :obj:`RuntimeWarning`: If unable to add path.
        
                
        """
    def create_root_item(self, name: str, path: str) -> omni.kit.widget.filebrowser.model.FileBrowserItem:
        ...
    def filter_collection(self, url: str = None) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.CollectionItem]:
        """
        
                Filter the collection based on the url.
        
                Args:
                    url (str): The url to filter the collection.
        
                Returns:
                    :obj:`CollectionItem`: The filtered collection.
                
        """
    def get_collection(self, identifier: str) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.CollectionItem]:
        """
        
                Get a collection from the navigation model.
        
                Args:
                    identifier (str): Identifier of the collection.
        
                Returns:
                    :obj:`CollectionItem`: The collection item.
                
        """
    def get_connections(self, identifier: str = None) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Returns all connections as items for the specified collection. If collection is 'None', then return connections
                from all collections.
        
                Args:
                    identifier (str): Connection identifier. Default None.
        
                Returns:
                    List[FileBrowserItem]: All connections found.
        
                
        """
    def remove_collection(self, identifier: str) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.CollectionItem]:
        """
        
                Remove a collection from the navigation model.
        
                Args:
                    identifier (str): Identifier of the collection.
        
                Returns:
                    :obj:`CollectionItem`: The removed collection item.
                
        """
    @property
    def available_collections(self) -> typing.List[str]:
        """
        List[str]: Available collections identifiers in the navigation model.
        """
    @available_collections.setter
    def available_collections(self, values: typing.List[str]):
        """
        Sets the available collections identifiers in the navigation model.
        """
    @property
    def collection_items(self) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        List[:obj:`FileBrowserItem`]: Available collection items in the navigation model.
        """
    @property
    def collections(self) -> typing.Dict[str, omni.kit.window.filepicker.collections.collection_item.CollectionItem]:
        """
        dict[:obj:`CollectionItem`]: Available collections dict in the navigation model.
        """
