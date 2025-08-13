from __future__ import annotations
from collections import namedtuple
from datetime import datetime
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.helper.file_utils import asset_types
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.window.filepicker.detail_view import DetailFrameController
from omni import ui
import os as os
import pathlib
from pathlib import Path
from pxr import Usd
import typing
__all__: list[str] = ['DetailFrameController', 'EXTENSION_FOLDER_PATH', 'ExtendedFileInfo', 'FileBrowserItem', 'ICON_PATH', 'IMPORTER_FILETYPES', 'Path', 'TXT_FILETYPES', 'USD_FILETYPES', 'Usd', 'asset_types', 'datetime', 'namedtuple', 'omni', 'os', 'run_coroutine', 'ui']
class ExtendedFileInfo(omni.kit.window.filepicker.detail_view.DetailFrameController):
    """
    Extended file info show in detail view
    """
    class MockListEntry(tuple):
        """
        MockListEntry(relative_path, modified_time, created_by, modified_by, size)
        """
        __match_args__: typing.ClassVar[tuple] = ('relative_path', 'modified_time', 'created_by', 'modified_by', 'size')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('relative_path', 'modified_time', 'created_by', 'modified_by', 'size')
        @staticmethod
        def __new__(_cls, relative_path, modified_time, created_by, modified_by, size):
            """
            Create new instance of MockListEntry(relative_path, modified_time, created_by, modified_by, size)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new MockListEntry object from a sequence or iterable
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
            Return a new MockListEntry object replacing specified fields with new values
            """
    _empty_list_entry: typing.ClassVar[MockListEntry]  # value = MockListEntry(relative_path='File info', modified_time=datetime.datetime(2025, 8, 13, 15, 56, 56, 737563), created_by='', modified_by='', size=0)
    def __init__(self):
        ...
    def _build_ui_async(self, selected: typing.List[str] = list()):
        ...
    def _build_ui_impl(self, selected: typing.List[str] = list()):
        ...
    def _destroy_impl(self, _):
        ...
    def _on_file_change_event(self, result: omni.client.impl._omniclient.Result, entry: omni.client.impl._omniclient.ListEntry):
        ...
    def _on_selection_changed_impl(self, selected: typing.List[str] = list()):
        ...
    def build_header(self, collapsed: bool, title: str):
        """
        
                Builds the header. It is used to show the header of the file info.
                Args:
                    collapsed (bool): True if the header is collapsed.
                    title (str): title of the header to be shown.
                
        """
EXTENSION_FOLDER_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.content_browser')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/videos/isaacsim/_build/linux-x86_64/release/exts/isaacsim.gui.content_browser/icons')
IMPORTER_FILETYPES: tuple = ('.urdf', '.mjcf')
TXT_FILETYPES: tuple = ('.json', '.yaml', '.yml', '.pt', '.txt', '.log')
USD_FILETYPES: tuple = ('.usd', '.usda', '.usdc', '.usdz')
