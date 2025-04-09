import OmniScriptingSchema as OmniScriptingSchema
import OmniScriptingSchemaTools as OmniScriptingSchemaTools
from __future__ import annotations
import omni as omni
from omni.kit.scripting.scripts.command import ApplyScriptingAPICommand
from omni.kit.scripting.scripts.command import RefreshScriptingPropertyWindowCommand
from omni.kit.scripting.scripts.command import RemoveScriptingAPICommand
from omni.kit.scripting.scripts.loader.omni_finder_loader import disable_omni_finder_loader
from omni.kit.scripting.scripts.loader.omni_finder_loader import enable_omni_finder_loader
from omni.kit.scripting.scripts.properties_widget import ScriptingProperties
from omni.kit.scripting.scripts.script_editor import ScriptEditor
from omni.kit.scripting.scripts.script_manager import ScriptManager
from omni.kit.scripting.scripts.utils import open_script_file
from omni.kit.scripting.scripts.utils import refresh_property_window
from omni.kit.usd_undo.layer_undo import UsdLayerUndo
import os as os
from pxr import Sdf
import typing
__all__ = ['ApplyScriptingAPICommand', 'EDIT_PYTHON_SCRIPT', 'Extension', 'NEW_PYTHON_SCRIPT_BEHAVIOR', 'NEW_PYTHON_SCRIPT_EMPTY', 'OPEN_SCRIPT_HANDLER', 'OmniScriptingSchema', 'OmniScriptingSchemaTools', 'RefreshScriptingPropertyWindowCommand', 'RemoveScriptingAPICommand', 'SCRIPTS_ATTR', 'ScriptEditor', 'ScriptManager', 'ScriptingProperties', 'Sdf', 'UsdLayerUndo', 'disable_omni_finder_loader', 'enable_omni_finder_loader', 'omni', 'open_script_file', 'os', 'refresh_property_window']
class Extension(omni.ext._extensions.IExt):
    _instance: typing.ClassVar[Extension]  # value = <omni.kit.scripting.scripts.extension.Extension object>
    @classmethod
    def get_instance(cls):
        ...
    def _add_content_browser_ui(self):
        ...
    def _remove_content_browser_ui(self):
        ...
    def get_script_editor(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
EDIT_PYTHON_SCRIPT: str = 'Edit Python Script'
NEW_PYTHON_SCRIPT_BEHAVIOR: str = 'New Python Script (BehaviorScript)'
NEW_PYTHON_SCRIPT_EMPTY: str = 'New Python Script (Empty)'
OPEN_SCRIPT_HANDLER: str = 'Open Python Script Handler'
SCRIPTS_ATTR: str = 'omni:scripting:scripts'
