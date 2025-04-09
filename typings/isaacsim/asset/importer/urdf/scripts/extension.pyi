from __future__ import annotations
import asyncio as asyncio
import carb as carb
from collections import namedtuple
from functools import partial
import gc as gc
from isaacsim.asset.importer.urdf import _urdf
from isaacsim.asset.importer.urdf.scripts.ui.UrdfJointWidgetWithID import UrdfJointWidget
from isaacsim.asset.importer.urdf.scripts.ui.UrdfOptionWidget import UrdfOptionWidget
from isaacsim.asset.importer.urdf.scripts.ui.style import get_option_style
from isaacsim.asset.importer.urdf.scripts.ui.ui_utils import btn_builder
from isaacsim.asset.importer.urdf.scripts.ui.ui_utils import cb_builder
from isaacsim.asset.importer.urdf.scripts.ui.ui_utils import dropdown_builder
from isaacsim.asset.importer.urdf.scripts.ui.ui_utils import float_builder
from isaacsim.asset.importer.urdf.scripts.ui.ui_utils import setup_ui_headers
from isaacsim.asset.importer.urdf.scripts.ui.ui_utils import str_builder
from isaacsim.asset.importer.urdf.scripts.ui.ui_utils import string_filed_builder
import omni as omni
from omni.kit.helper.file_utils import asset_types
from omni.kit.notification_manager.extension import post_notification
from omni.kit.notification_manager.notification_info import NotificationStatus
from omni.kit.tool import asset_importer as ai
from omni import ui
import os as os
from pathlib import Path
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
from pxr import UsdUtils
import weakref as weakref
__all__ = ['EXTENSION_NAME', 'Extension', 'NotificationStatus', 'Path', 'Sdf', 'Singleton', 'UrdfImporterDelegate', 'UrdfJointWidget', 'UrdfOptionWidget', 'Usd', 'UsdGeom', 'UsdPhysics', 'UsdUtils', 'ai', 'asset_types', 'asyncio', 'btn_builder', 'carb', 'cb_builder', 'dir_exists', 'dropdown_builder', 'float_builder', 'gc', 'get_option_style', 'is_urdf_file', 'namedtuple', 'omni', 'on_filter_folder', 'on_filter_item', 'os', 'partial', 'post_notification', 'setup_ui_headers', 'str_builder', 'string_filed_builder', 'ui', 'weakref']
class Extension(omni.ext._extensions.IExt):
    def _menu_callback(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
class UrdfImporterDelegate(omni.kit.tool.asset_importer.importer_delegate.AbstractImporterDelegate):
    """
    
        Urdf importer delegate implementation for Asset Importer AbstractImporterDelegate.
        
    """
    def __init__(self, name, filters, descriptions, ext_id):
        ...
    def _on_import_complete(self, file_paths):
        ...
    def build_options(self, paths):
        ...
    def convert_assets(self, paths, **kargs):
        ...
    def destroy(self):
        ...
    def show_destination_frame(self):
        ...
    def supports_usd_stage_cache(self):
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
def Singleton(class_):
    """
    A singleton decorator
    """
def dir_exists(path: str, timeout: float = 10.0) -> bool:
    ...
def is_urdf_file(path: str):
    ...
def on_filter_folder(item) -> bool:
    ...
def on_filter_item(item) -> bool:
    ...
EXTENSION_NAME: str = 'URDF Importer'
