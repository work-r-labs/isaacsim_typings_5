from __future__ import annotations
import asyncio as asyncio
import carb as carb
from collections import namedtuple
import gc as gc
from isaacsim.asset.importer.mjcf import _mjcf
from isaacsim.asset.importer.mjcf.scripts.option_widget import OptionWidget
from isaacsim.asset.importer.mjcf.scripts.ui_utils import btn_builder
from isaacsim.asset.importer.mjcf.scripts.ui_utils import cb_builder
from isaacsim.asset.importer.mjcf.scripts.ui_utils import dropdown_builder
from isaacsim.asset.importer.mjcf.scripts.ui_utils import float_builder
from isaacsim.asset.importer.mjcf.scripts.ui_utils import str_builder
import omni as omni
from omni.kit.helper.file_utils import asset_types
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.utils import add_menu_items
from omni.kit.menu.utils.utils import remove_menu_items
from omni.kit.notification_manager.extension import post_notification
from omni.kit.notification_manager.notification_info import NotificationStatus
from omni.kit.tool import asset_importer as ai
from omni.kit.viewport.utility import get_active_viewport
from omni.kit.window.filepicker.dialog import FilePickerDialog
from omni import ui
import os as os
from pathlib import Path
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import weakref as weakref
__all__ = ['EXTENSION_NAME', 'Extension', 'FilePickerDialog', 'MenuItemDescription', 'MjcfImporterDelegate', 'NotificationStatus', 'OptionWidget', 'Path', 'Sdf', 'Usd', 'UsdGeom', 'UsdPhysics', 'add_menu_items', 'ai', 'asset_types', 'asyncio', 'btn_builder', 'carb', 'cb_builder', 'dropdown_builder', 'float_builder', 'gc', 'get_active_viewport', 'is_mjcf_file', 'make_menu_item_description', 'namedtuple', 'omni', 'on_filter_item', 'os', 'post_notification', 'remove_menu_items', 'str_builder', 'ui', 'weakref']
class Extension(omni.ext._extensions.IExt):
    def _load_robot(self, path = None, **kargs):
        ...
    def _parse_mjcf(self):
        ...
    def _refresh_filebrowser(self):
        ...
    def _select_picked_file_callback(self, dialog: omni.kit.window.filepicker.dialog.FilePickerDialog, filename = None, path = None):
        ...
    def build_new_optons(self):
        ...
    def build_options_frame_left_top(self):
        ...
    def build_options_frame_right_bottom(self):
        ...
    def build_ui(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def reset_config(self):
        ...
class MjcfImporterDelegate(omni.kit.tool.asset_importer.importer_delegate.AbstractImporterDelegate):
    """
    
        Mjcf importer delegate implementation for Asset Importer AbstractImporterDelegate.
        
    """
    def __init__(self, name, filters, descriptions):
        ...
    def _on_import_complete(self, file_paths):
        ...
    def build_options(self, paths):
        ...
    def convert_assets(self, paths, **kargs):
        ...
    def destroy(self):
        ...
    def set_importer(self, importer):
        ...
    def show_destination_frame(self):
        ...
    @property
    def filter_descriptions(self):
        ...
    @property
    def filter_regexes(self):
        ...
    @property
    def name(self):
        ...
def is_mjcf_file(path: str):
    ...
def make_menu_item_description(ext_id: str, name: str, onclick_fun, action_name: str = '') -> None:
    """
    Easily replace the onclick_fn with onclick_action when creating a menu description
    
        Args:
            ext_id (str): The extension you are adding the menu item to.
            name (str): Name of the menu item displayed in UI.
            onclick_fun (Function): The function to run when clicking the menu item.
            action_name (str): name for the action, in case ext_id+name don't make a unique string
    
        Note:
            ext_id + name + action_name must concatenate to a unique identifier.
    
        
    """
def on_filter_item(item) -> bool:
    ...
EXTENSION_NAME: str = 'MJCF Importer'
