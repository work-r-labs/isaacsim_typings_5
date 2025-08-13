from __future__ import annotations
import carb as carb
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.nucleus_model import NucleusModel
import omni.kit.window.filepicker.collections.collection_item
from omni.kit.window.filepicker.collections.collection_item import AddNewItem
from omni.kit.window.filepicker.collections.collection_item import CollectionItem
import pathlib
__all__: list[str] = ['AddNewItem', 'AddNucleusConnectionItem', 'CollectionItem', 'FileBrowserItem', 'ICON_PATH', 'NucleusCollectionItem', 'NucleusModel', 'carb']
class AddNucleusConnectionItem(omni.kit.window.filepicker.collections.collection_item.AddNewItem):
    def add_new(self, on_success_fn: typing.Callable[[str, str, bool, bool], NoneType]) -> None:
        ...
class NucleusCollectionItem(omni.kit.window.filepicker.collections.collection_item.CollectionItem):
    def __init__(self):
        ...
    def create_add_new_item(self) -> typing.Optional[omni.kit.window.filepicker.collections.nucleus_collection.AddNucleusConnectionItem]:
        ...
    def create_child_item(self, name: str, path: str, is_folder: bool = True) -> typing.Optional[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        ...
    @property
    def connections(self) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        List[:obj:`FileBrowserItem`]: List of connections of this item.
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/extscache/omni.kit.window.filepicker-2.13.3+8131b85d/icons/NvidiaDark')
