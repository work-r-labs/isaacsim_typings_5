from __future__ import annotations
import asyncio as asyncio
import carb as carb
from isaacsim.gui.content_browser.impl.detail_view import ExtendedFileInfo
from isaacsim.gui.content_browser.impl.isaac_collection import IsaacCollection
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.window.content_browser import get_content_window
from omni.kit.window.filepicker.collections.collection_data import CollectionData
import weakref as weakref
__all__: list[str] = ['CollectionData', 'ExtendedFileInfo', 'Extension', 'FileBrowserModel', 'IsaacCollection', 'asyncio', 'carb', 'get_content_window', 'omni', 'weakref']
class Extension(omni.ext._extensions.IExt):
    """
    The Extension class
    """
    def _add_isim_content(self):
        ...
    def _expand_collections(self):
        ...
    def _populate_asset_info(self):
        ...
    def on_shutdown(self):
        """
        Method called when the extension is disabled
        """
    def on_startup(self, ext_id):
        """
        Method called when the extension is loaded/enabled
        """
