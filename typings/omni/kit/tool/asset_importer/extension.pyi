from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.tool.asset_importer.builtin_importer import BuiltinImporter
from omni.kit.tool.asset_importer.file_picker import FilePicker
from omni.kit.tool.asset_importer.filebrowser import FileBrowserMode
from omni.kit.tool.asset_importer.filebrowser import FileBrowserSelectionType
from omni.kit.tool.asset_importer.importer_delegate import AbstractImporterDelegate
from omni.kit.tool.asset_importer.importers_manager import ImportersManager
from omni.kit.tool.asset_importer.options_window import OptionsWindow
from omni.kit.tool.asset_importer.utils import Utils
from omni.kit.widget.prompt.prompt import PromptButtonInfo
from omni.kit.widget.prompt.prompt import PromptManager
from omni.kit.window import content_browser as content
import os as os
from pathlib import Path
from pxr import Sdf
from pxr import Tf
from pxr import Usd
from pxr import UsdUtils
import typing
import urllib as urllib
__all__ = ['AbstractImporterDelegate', 'AssetImporterExtension', 'BuiltinImporter', 'FileBrowserMode', 'FileBrowserSelectionType', 'FilePicker', 'ImportersManager', 'MenuItemDescription', 'OptionsWindow', 'Path', 'PromptButtonInfo', 'PromptManager', 'Sdf', 'Tf', 'Usd', 'UsdUtils', 'Utils', 'asyncio', 'carb', 'content', 'is_supported_format', 'omni', 'os', 'partial', 'register_importer', 'remove_importer', 'urllib']
class AssetImporterExtension(omni.ext._extensions.IExt):
    CONVERT_TO_USD_MENU_NAME: typing.ClassVar[str] = 'Convert to USD'
    IMPORT_AND_CONVERT_MENU_NAME: typing.ClassVar[str] = 'Import and Convert'
    IMPORT_FILE_MENU_NAME: typing.ClassVar[str] = 'Import'
    IMPORT_ICON_MENU_NAME: typing.ClassVar[str] = 'External Asset (FBX, OBJ...)'
    PERSISTENT_APP_IMPORT_SETTINGS_PATH: typing.ClassVar[str] = '/persistent/app/stage/dragDropImport'
    UPLOAD_MENU_NAME: typing.ClassVar[str] = 'Upload Files and Folders'
    @staticmethod
    def get_instance():
        ...
    def _convert_file(self, file_paths, add_reference = True):
        ...
    def _deregister_action(self, extension_id: str):
        ...
    def _get_current_dir_in_content_window(self):
        ...
    def _get_export_folder(self, asset_paths, export_to_current_folder, current_folder = None):
        ...
    def _is_nucleus_server_url(self, url: str):
        ...
    def _is_show_convert_visible(self, content_url):
        ...
    def _is_show_import_menu(self):
        ...
    def _is_show_open_visible(self, content_url):
        ...
    def _is_show_upload_visible(self, url):
        ...
    def _load_default_settings(self) -> dict:
        ...
    def _on_client_bookmarks_changed(self, client_bookmarks: typing.Dict):
        ...
    def _on_icon_menu_click(self, menu, value):
        ...
    def _on_menu_convert_click(self, add_reference = True, export_to_current_folder = True):
        ...
    def _on_menu_upload_click(self):
        ...
    def _register_action(self, extension_id: str):
        ...
    def _register_menus(self):
        ...
    def _save_default_settings(self, default_settings: typing.Dict):
        ...
    def _show_options_window_and_convert(self, paths: typing.List[str]):
        ...
    def _unregister_menus(self):
        ...
    def add_import_canceled_callback(self, callback):
        ...
    def add_import_complete_callback(self, callback):
        ...
    def add_importer(self, importer_delegate: omni.kit.tool.asset_importer.importer_delegate.AbstractImporterDelegate):
        ...
    def get_filter_options(self):
        ...
    def import_asset(self, add_reference = False, export_to_current_folder = True):
        ...
    def is_supported_format(self, path: str):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def remove_import_canceled_callback(self, callback):
        ...
    def remove_import_complete_callback(self, callback):
        ...
    def remove_importer(self, importer_delegate: omni.kit.tool.asset_importer.importer_delegate.AbstractImporterDelegate):
        ...
def is_supported_format(path: str):
    """
    Check if this asset format is supported by any importers already.
    """
def register_importer(importer_delegate: omni.kit.tool.asset_importer.importer_delegate.AbstractImporterDelegate):
    """
    Register external importer. Asset importer includes builtin
        importers to convert FBX/OBJ/GLTF... files that Assimp supports.
        This is used to register external importers that's not supported
        by builtin importers.
    
        Args:
            importer_delegate (omni.kit.tool.asset_importer.AbstractImporterDelegate):
                The delegate to define the details of an importer. Refer class `AbstractImporterDelegate`
                for reference.
        
    """
def remove_importer(importer_delegate: omni.kit.tool.asset_importer.importer_delegate.AbstractImporterDelegate):
    """
    Unregister importer.
    """
_global_instance: AssetImporterExtension  # value = <omni.kit.tool.asset_importer.extension.AssetImporterExtension object>
