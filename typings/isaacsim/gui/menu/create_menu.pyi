from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
from isaacsim.core.utils.viewports import set_camera_view
from isaacsim.gui.components.menu import make_menu_item_description
from isaacsim.storage.native.nucleus import get_assets_root_path
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.layout import MenuLayout
from omni.kit.menu.utils.utils import add_menu_items
from pathlib import Path
import weakref as weakref
__all__ = ['CreateMenuExtension', 'MenuItemDescription', 'MenuLayout', 'Path', 'add_menu_items', 'asyncio', 'carb', 'get_assets_root_path', 'make_menu_item_description', 'omni', 'partial', 'set_camera_view', 'weakref']
class CreateMenuExtension:
    def __del__(self):
        ...
    def __init__(self, ext_id):
        ...
    def create_apriltag(self, usd_path, shader_name, stage_path, tag_path):
        ...
    def create_asset(self, usd_path, stage_path, camera_position = None, camera_target = None):
        ...
