from __future__ import annotations
import _asyncio
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.usd._usd import AudioManager
from omni.usd._usd import EngineCreationConfig
from omni.usd._usd import EngineCreationFlags
from omni.usd._usd import OpaqueSharedHydraEngineContext
from omni.usd._usd import PickingMode
from omni.usd._usd import Selection
from omni.usd._usd import StageEventType
from omni.usd._usd import StageRenderingEventType
from omni.usd._usd import StageState
from omni.usd._usd import UsdContext
from omni.usd._usd import UsdContextInitialLoadSet
from omni.usd._usd import add_hydra_engine
from omni.usd._usd import attach_all_hydra_engines
from omni.usd._usd import create_context
from omni.usd._usd import destroy_context
from omni.usd._usd import get_context
from omni.usd._usd import get_context_from_stage_id
from omni.usd._usd import get_or_create_hydra_engine
from omni.usd._usd import merge_layers
from omni.usd._usd import merge_prim_spec
from omni.usd._usd import new_stage as __old_new_stage
from omni.usd._usd import new_stage_with_callback as __old_new_stage_with_callback
from omni.usd._usd import release_all_hydra_engines
from omni.usd._usd import release_hydra_engine
from omni.usd._usd import resolve_paths
from omni.usd._usd import resolve_prim_path_references
from omni.usd._usd import resolve_prim_paths_references
from omni.usd._usd import shutdown_usd
from pxr import Usd
import pxr.Usd
from pxr import UsdUtils
__all__ = ['AudioManager', 'EngineCreationConfig', 'EngineCreationFlags', 'MOTION_RAYTRACING_ENABLED', 'NONE', 'OpaqueSharedHydraEngineContext', 'PickingMode', 'SKIP_ON_WORKER_PROCESS', 'Selection', 'StageEventType', 'StageRenderingEventType', 'StageState', 'Usd', 'UsdContext', 'UsdContextInitialLoadSet', 'UsdUtils', 'WRITABLE_USD_FILE_EXTS_STR', 'add_hydra_engine', 'asyncio', 'attach_all_hydra_engines', 'carb', 'create_context', 'destroy_context', 'get_context', 'get_context_from_stage_id', 'get_or_create_hydra_engine', 'merge_layers', 'merge_prim_spec', 'omni', 'on_layers_saved_result', 'on_stage_result', 'partial', 'release_all_hydra_engines', 'release_hydra_engine', 'resolve_paths', 'resolve_prim_path_references', 'resolve_prim_paths_references', 'shutdown_usd']
def _attach_stage_async(self, stage: pxr.Usd.Stage) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.attach_stage_with_callback`. Attaches an opened stage to the context.
    
        Args:
            stage (pxr.Usd.Stage): The instance of UsdStage.
    
        Returns:
            (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                the second one tells the error message if the operation is failed.
        
    """
def _close_stage_async(self) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.close_stage_with_callback`. Closes the current stage.
    
        Returns:
            (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                the second one tells the error message if the operation is failed.
        
    """
def _export_as_stage_async(self, url: str) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.export_as_stage_with_callback`. Flattens and exports the current stage.
    
        Returns:
            (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                the second one tells the error message if the operation is failed.
        
    """
def _load_mdl_parameters_for_prim_async(self, prim, recreate: bool = False):
    ...
def _new_stage_async(self, load_set: omni.usd._usd.UsdContextInitialLoadSet = ...) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.new_stage_with_callback`. Creates a new stage with anonymous root layer.
    
        Args:
            load_set (omni.usd.UsdContextInitialLoadSet): Whether it should open stage with payloads loaded or not. By default, it loads all payloads.
    
        Returns:
            (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                the second one tells the error message if the operation is failed.
        
    """
def _new_stage_python_wrapper(self, fn = None, load_set: omni.usd._usd.UsdContextInitialLoadSet = ...):
    """
    Asynchronous version of :func:`omni.usd.UsdContext.new_stage` that supports to customize load set of new stage.
    """
def _new_stage_sync(self, load_set: omni.usd._usd.UsdContextInitialLoadSet = ...) -> bool:
    ...
def _next_stage_event_async(self) -> typing.Tuple[omni.usd._usd.StageEventType, typing.Dict[typing.Any, typing.Any]]:
    """
    Wait for next stage event of omni.usd.
    """
def _open_stage_async(self, url: str, load_set: omni.usd._usd.UsdContextInitialLoadSet = ..., session_layer_url: str = None) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.open_stage_with_callback`. Opens a new stage.
    
        Args:
            url (str): Stage URL to open.
            load_set (omni.usd.UsdContextInitialLoadSet): If it's to open all payloads or none.
            session_layer_url (str): Specified session layer.
    
        Returns:
            (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                the second one tells the error message if the operation is failed.
        
    """
def _reopen_stage_async(self, load_set: omni.usd._usd.UsdContextInitialLoadSet = ...) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.reopen_stage_with_callback`. Re-opens the current stage.
    
        Args:
            load_set (omni.usd.UsdContextInitialLoadSet): If it's to open all payloads or none.
    
        Returns:
            (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                the second one tells the error message if the operation is failed.
        
    """
def _save_as_stage_async(self, url: str) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.save_as_stage_with_callback`. Saves the current stage to a new location.
    
        Args:
            url (str): New location to save the current stage.
    
        Returns:
            (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                the second one tells the error message if the operation is failed.
        
    """
def _save_layers_async(self, new_root_layer_path: str, layer_identifiers: typing.List[str]) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.save_layers_with_callback`. Saves specified layers.
    
        Args:
            new_root_layer_path (str): New location for root layer if it's to save-as the current stage. If it's empty, it will save specified layers only.
            layer_identifiers (List[str]): List of layer identifiers to be saved.
    
        Returns:
            (bool, str, List[str]): A tuple where the first element tells whether the operation is successful or not, the second one tells the error message if it's faled and
                the third param is the list of layer identifiers that are saved successfully.
        
    """
def _save_stage_async(self) -> typing.Tuple[bool, str]:
    """
    
        Asynchronous version of :func:`omni.usd.UsdContext.save_stage_with_callback`. Saves the current stage.
    
        Returns:
            (bool, str): A tuple where the first element tells whether the operation is successful or not, and
                the second one tells the error message if the operation is failed.
        
    """
def _selection_changed_async(self) -> typing.List[str]:
    """
    Wait for selection to be changed. Return a list of newly selected paths.
    """
def on_layers_saved_result(result: bool, err_msg: str, saved_layers: typing.List[str], future: _asyncio.Future):
    """
    Internal callback.
    """
def on_stage_result(result: bool, err_msg: str, future: _asyncio.Future):
    """
    Internal callback.
    """
MOTION_RAYTRACING_ENABLED: omni.usd._usd.EngineCreationFlags  # value = <EngineCreationFlags.MOTION_RAYTRACING_ENABLED: 1>
NONE: omni.usd._usd.EngineCreationFlags  # value = <EngineCreationFlags.NONE: 0>
SKIP_ON_WORKER_PROCESS: omni.usd._usd.EngineCreationFlags  # value = <EngineCreationFlags.SKIP_ON_WORKER_PROCESS: 2>
WRITABLE_USD_FILE_EXTS_STR: str = 'usd|usda|usdc|live'
