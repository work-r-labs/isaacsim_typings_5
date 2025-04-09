from __future__ import annotations
import asyncio as asyncio
from isaacsim.asset.importer.urdf.scripts.samples.common import set_drive_parameters
from isaacsim.examples.browser.extension import get_instance as get_browser_instance
from isaacsim.gui.components.style import get_style
from isaacsim.gui.components.ui_utils import btn_builder
from isaacsim.gui.components.ui_utils import setup_ui_headers
import math as math
import omni as omni
from omni.kit.viewport.utility.camera_state import ViewportCameraState
from omni import ui
from pxr import Gf
from pxr import PhysicsSchemaTools
from pxr import Sdf
from pxr import UsdLux
from pxr import UsdPhysics
import weakref as weakref
__all__ = ['EXTENSION_NAME', 'Extension', 'Gf', 'PhysicsSchemaTools', 'Sdf', 'UsdLux', 'UsdPhysics', 'ViewportCameraState', 'asyncio', 'btn_builder', 'get_browser_instance', 'get_style', 'math', 'omni', 'set_drive_parameters', 'setup_ui_headers', 'ui', 'weakref']
class Extension(omni.ext._extensions.IExt):
    def _build_ui(self):
        ...
    def _build_window(self):
        ...
    def _load_kaya(self, task):
        ...
    def _menu_callback(self):
        ...
    def _on_config_drives(self):
        ...
    def _on_config_robot(self):
        ...
    def _on_load_robot(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
EXTENSION_NAME: str = 'Import Kaya'
