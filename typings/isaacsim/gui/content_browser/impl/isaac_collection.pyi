from __future__ import annotations
import asyncio as asyncio
import carb as carb
from datetime import datetime
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.widget.filebrowser.nucleus_model import NucleusItem
from omni.kit.window.filepicker.collections.collection_item import AddNewItem
from omni.kit.window.filepicker.collections.collection_item import CollectionItem
from omni import ui
import pathlib
from pathlib import Path
import typing
from typing import Any
__all__: list[str] = ['AddNewItem', 'Any', 'CURRENT_PATH', 'CollectionItem', 'FileBrowserItemFields', 'ICON_PATH', 'IsaacCollection', 'IsaacConnectionItem', 'NucleusItem', 'Path', 'SETTING_FOLDER', 'asyncio', 'carb', 'datetime', 'omni', 'ui']
class IsaacCollection(omni.kit.window.filepicker.collections.collection_item.CollectionItem):
    def __init__(self):
        ...
    def create_add_new_item(self) -> typing.Optional[omni.kit.window.filepicker.collections.collection_item.AddNewItem]:
        ...
    def create_child_item(self, name: str, path: str, is_folder: bool = True) -> typing.Optional[isaacsim.gui.content_browser.impl.isaac_collection.IsaacConnectionItem]:
        ...
    def populate_children_async(self) -> typing.Any:
        ...
class IsaacConnectionItem(omni.kit.widget.filebrowser.nucleus_model.NucleusItem):
    """
    
        A item for a Isaac connection
        Sub-classed from :obj:`NucleusItem`.
    
        Args:
            name (str): Name of the item.
            path (str): Path of the item.
        
    """
    def __init__(self, name: str, path: str):
        ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.content_browser/isaacsim/gui/content_browser/impl')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.content_browser/icons')
SETTING_FOLDER: str = '/exts/isaacsim.gui.content_browser/folders'
