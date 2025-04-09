import OmniScriptingSchema as OmniScriptingSchema
import OmniScriptingSchemaTools as OmniScriptingSchemaTools
from __future__ import annotations
import carb as carb
import omni as omni
from omni.appwindow._appwindow import IAppWindow
from omni.kit.app._app import IApp
from omni.kit.scripting.scripts import command
from omni.kit.scripting.scripts.command import ApplyScriptingAPICommand
from omni.kit.scripting.scripts.command import RefreshScriptingPropertyWindowCommand
from omni.kit.scripting.scripts.command import RemoveScriptingAPICommand
from omni.kit.scripting.scripts import extension
from omni.kit.scripting.scripts.extension import Extension
from omni.kit.scripting.scripts import loader
from omni.kit.scripting.scripts.loader.omni_finder_loader import disable_omni_finder_loader
from omni.kit.scripting.scripts.loader.omni_finder_loader import enable_omni_finder_loader
from omni.kit.scripting.scripts import properties_widget
from omni.kit.scripting.scripts.properties_widget import ScriptingProperties
from omni.kit.scripting.scripts import script_editor
from omni.kit.scripting.scripts.script_editor import ScriptEditor
from omni.kit.scripting.scripts import script_manager
from omni.kit.scripting.scripts.script_manager import ScriptManager
from omni.kit.scripting.scripts import utils
from omni.kit.scripting.scripts.utils import open_script_file
from omni.kit.scripting.scripts.utils import refresh_property_window
from omni.kit.usd_undo.layer_undo import UsdLayerUndo
from omni.timeline._timeline import ITimeline
from omni.usd._usd import Selection
from omni.usd._usd import UsdContext
import os as os
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
import pxr.Usd
from pxr import UsdUtils
from . import scripts
__all__ = ['ApplyScriptingAPICommand', 'BehaviorScript', 'EDIT_PYTHON_SCRIPT', 'EVENT_TYPE_BEHAVIOR_SCRIPT_LOADED', 'EVENT_TYPE_BEHAVIOR_SCRIPT_UNLOADED', 'Extension', 'IApp', 'IAppWindow', 'ITimeline', 'NEW_PYTHON_SCRIPT_BEHAVIOR', 'NEW_PYTHON_SCRIPT_EMPTY', 'OPEN_SCRIPT_HANDLER', 'OmniScriptingSchema', 'OmniScriptingSchemaTools', 'RefreshScriptingPropertyWindowCommand', 'RemoveScriptingAPICommand', 'SCRIPTS_ATTR', 'ScriptEditor', 'ScriptManager', 'ScriptingProperties', 'Sdf', 'Selection', 'Usd', 'UsdContext', 'UsdLayerUndo', 'UsdUtils', 'carb', 'command', 'disable_omni_finder_loader', 'enable_omni_finder_loader', 'extension', 'get_event_stream', 'loader', 'omni', 'open_script_file', 'os', 'properties_widget', 'refresh_property_window', 'script_editor', 'script_manager', 'scripts', 'utils']
class BehaviorScript:
    """
    
        Base class for for developing per USD Prim behaviors.
        
    """
    def __init__(self, prim_path: pxr.Sdf.Path):
        """
        Initializes a BehaviorScript for the prim_path( Sdf.Path) this script was assigned to.
        """
    def on_destroy(self):
        """
        Override this method to handle when the BehaviorScript is destroyed from being unassigned from a USD prim.
        """
    def on_init(self):
        """
        Override this method to handle when the BehaviorScript is initialize from being assigned to a USD prim.
        """
    def on_pause(self):
        """
        Override this method to handle when `pause` is pressed.
                
        """
    def on_play(self):
        """
        Override this method to handle when `play` is pressed.
                
        """
    def on_stop(self):
        """
        Override this method to handle when the `stop` is pressed.
                
        """
    def on_update(self, current_time: float, delta_time: float):
        """
        Override this method to handle per frame update events that occur when `playing`.
                Args:
                    current_time: The current time. (in seconds).
                    delta_time: The delta time (in seconds).
                
        """
    @property
    def app(self) -> omni.kit.app._app.IApp:
        """
        Returns the kit application interface.
        """
    @property
    def default_app_window(self) -> omni.appwindow._appwindow.IAppWindow:
        ...
    @property
    def input(self) -> carb.input.IInput:
        """
        Returns the application input interface.
        """
    @property
    def message_bus_event_stream(self) -> carb.events._events.IEventStream:
        """
        Returns the application message bus event stream.
        """
    @property
    def prim(self) -> pxr.Usd.Prim:
        """
        Returns the prim that this script is assigned to.
        """
    @property
    def prim_path(self) -> pxr.Sdf.Path:
        """
        Returns the prim path that this script is assigned to.
        """
    @property
    def selection(self) -> omni.usd._usd.Selection:
        """
        Returns the current USD context selection interface in the application.
        """
    @property
    def settings(self) -> carb.settings._settings.ISettings:
        """
        Returns the current settings.
        """
    @property
    def stage(self) -> pxr.Usd.Stage:
        """
        Returns the current USD stage that is opened/loaded.
        """
    @property
    def timeline(self) -> omni.timeline._timeline.ITimeline:
        """
        Returns the application timeline interface.
        """
    @property
    def usd_context(self) -> omni.usd._usd.UsdContext:
        """
        Returns the current USD context.
        """
def get_event_stream() -> carb.events._events.IEventStream:
    """
    
        Returns the scripting events stream to receive events when script are loaded and unloaded.
    
        EVENT_TYPE_BEHAVIOR_SCRIPT_LOADED
        Args:
            prim_path: The Sdf.Path the BehaviorScript is associated to:
            script_path: The script path.
            script_instance: The python BehaviorScript instance.
    
    
        EVENT_TYPE_BEHAVIOR_SCRIPT_UNLOADED
        Args:
            prim_path: The Sdf.Path the BehaviorScript is associated to:
            script_path: The script path.
        
    """
EDIT_PYTHON_SCRIPT: str = 'Edit Python Script'
EVENT_TYPE_BEHAVIOR_SCRIPT_LOADED: int = 17862895898868367521
EVENT_TYPE_BEHAVIOR_SCRIPT_UNLOADED: int = 10876748312031697622
NEW_PYTHON_SCRIPT_BEHAVIOR: str = 'New Python Script (BehaviorScript)'
NEW_PYTHON_SCRIPT_EMPTY: str = 'New Python Script (Empty)'
OPEN_SCRIPT_HANDLER: str = 'Open Python Script Handler'
SCRIPTS_ATTR: str = 'omni:scripting:scripts'
