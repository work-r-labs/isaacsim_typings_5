from __future__ import annotations
import asyncio as asyncio
import carb as carb
import importlib as importlib
import inspect as inspect
import omni as omni
from omni.kit.scripting.scripts.loader.io import isabs
from omni.kit.scripting.scripts.loader.omni_cache import OmniCache
from omni.kit.scripting.scripts.loader import omni_finder_loader
from omni.kit.scripting.scripts.loader.omni_finder_loader import OmniFinder
from omni.kit.scripting.scripts.loader.omni_finder_loader import get_dependency_list
from omni.kit.scripting.scripts.loader.omni_finder_loader import get_dependency_module_name
from omni.kit.scripting.scripts.utils import show_security_popup
from omni.kit.scripting.scripts.utils import traceback_format_exception
import os as os
from pxr import Sdf
from pxr import Tf
from pxr import Usd
from pxr import UsdUtils
import sys as sys
import typing
import usdrt as usdrt
__all__ = ['EVENT_TYPE_SCRIPT_FILE_DELETED', 'EVENT_TYPE_SCRIPT_FILE_UPDATED', 'OmniCache', 'OmniFinder', 'SCRIPTS_ATTR', 'SETTINGS_IGNORE_WARNING', 'STAGEUPDATE_ORDER', 'ScriptManager', 'Sdf', 'Tf', 'Usd', 'UsdUtils', 'asyncio', 'carb', 'get_dependency_list', 'get_dependency_module_name', 'importlib', 'inspect', 'isabs', 'omni', 'omni_finder_loader', 'os', 'show_security_popup', 'sys', 'traceback_format_exception', 'usdrt']
class ScriptManager:
    _ScriptManager__instance: typing.ClassVar[ScriptManager]  # value = <omni.kit.scripting.scripts.script_manager.ScriptManager object>
    @classmethod
    def get_instance(cls) -> ScriptManager:
        ...
    def __init__(self):
        ...
    def _apply_scripts(self, prim: Usd.Prim):
        ...
    def _create_script_instance(self, prim_path_str, script_path):
        ...
    def _destroy_script(self, prim_path_str, script_path):
        ...
    def _destroy_script_instance(self, prim_path_str, script_path, script_instance):
        ...
    def _foreach_script_instance(self, fn: typing.Callable):
        ...
    def _load_all_scripts(self):
        ...
    def _load_script(self, script_path: str) -> bool:
        ...
    def _on_script_event(self, e: carb.events.IEvent):
        ...
    def _on_stage_attach(self, stage_id, meters_per_unit):
        ...
    def _on_stage_detach(self):
        ...
    def _on_stage_update(self, current_time: float, delta_time: float):
        ...
    def _on_timeline_event(self, e: carb.events.IEvent):
        ...
    def _on_usd_objects_changed(self, objects_changed, stage):
        ...
    def _open_stage(self):
        ...
    def _pending_sync_task_handler(self):
        ...
    def _reload_script(self, script_path: str) -> bool:
        ...
    def _security_check_and_wait(self, future, proceed_fn):
        ...
    def _unload_all_scripts(self):
        ...
    def _unload_script(self, script_path: str):
        ...
    def destroy(self):
        ...
    def get_event_stream(self) -> carb.events.IEventStream:
        ...
EVENT_TYPE_SCRIPT_FILE_DELETED: int = 683852953784394755
EVENT_TYPE_SCRIPT_FILE_UPDATED: int = 11220903237346331397
SCRIPTS_ATTR: str = 'omni:scripting:scripts'
SETTINGS_IGNORE_WARNING: str = '/app/scripting/ignoreWarningDialog'
STAGEUPDATE_ORDER: int = 200
