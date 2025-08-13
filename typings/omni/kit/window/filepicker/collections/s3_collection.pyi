from __future__ import annotations
from datetime import datetime
from functools import partial
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.widget.filebrowser.nucleus_model import NucleusItem
from omni.kit.window.filepicker.collections.collection_item import AddNewItem
from omni.kit.window.filepicker.collections.collection_item import CollectionItem
from omni.kit.window.filepicker.collections.s3_connector_dialog import S3ConnectorDialog
from omni import ui
import pathlib
__all__: list[str] = ['AddNewItem', 'AddS3ConnectionItem', 'CollectionItem', 'FileBrowserItem', 'FileBrowserItemFields', 'ICON_PATH', 'NucleusItem', 'S3Collection', 'S3ConnectionItem', 'S3ConnectorDialog', 'datetime', 'omni', 'partial', 'ui']
class AddS3ConnectionItem(omni.kit.window.filepicker.collections.collection_item.AddNewItem):
    def add_new(self, on_success_fn: typing.Callable[[str, str, bool, bool], NoneType]) -> None:
        ...
class S3Collection(omni.kit.window.filepicker.collections.collection_item.CollectionItem):
    def __init__(self):
        ...
    def create_add_new_item(self) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.AddNewItem]:
        ...
    def create_child_item(self, name: str, path: str, is_folder: bool = True) -> typing.Optional[omni.kit.window.filepicker.collections.s3_collection.S3ConnectionItem]:
        ...
    @property
    def connections(self) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        List[:obj:`FileBrowserItem`]: List of connections of this item.
        """
class S3ConnectionItem(omni.kit.widget.filebrowser.nucleus_model.NucleusItem):
    """
    
        A item for a S3 connection
        Sub-classed from :obj:`NucleusItem`.
    
        Args:
            name (str): Name of the item.
            path (str): Path of the item.
        
    """
    def __init__(self, name: str, path: str):
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.filepicker-2.13.3+8131b85d/icons/NvidiaDark')
