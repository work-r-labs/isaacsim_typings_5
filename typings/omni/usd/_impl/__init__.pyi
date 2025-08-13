from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb.eventdispatcher import get_eventdispatcher
from enum import Enum
import functools as functools
from functools import partial
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.usd._impl.api import on_layers_saved_result
from omni.usd._impl.api import on_stage_result
from omni.usd._impl.layer_utils import get_all_sublayers
from omni.usd._impl.layer_utils import get_dirty_layers
from omni.usd._impl.layer_utils import get_edit_target_identifier
from omni.usd._impl.layer_utils import is_layer_locked
from omni.usd._impl.layer_utils import is_layer_writable
from omni.usd._impl.layer_utils import set_edit_target_by_identifier
from omni.usd._impl.layer_utils import stitch_prim_specs
from omni.usd._impl.prim_lists import get_geometry_standard_prim_list
from omni.usd._impl.prim_lists import get_light_prim_list
from omni.usd._impl.timesample_utils import Value_On_Layer
from omni.usd._impl.timesample_utils import attr_has_timesample_on_key
from omni.usd._impl.timesample_utils import copy_timesamples_from_weaker_layer
from omni.usd._impl.timesample_utils import get_attribute_effective_defaultvalue_layer_info
from omni.usd._impl.timesample_utils import get_attribute_effective_timesample_layer_info
from omni.usd._impl.timesample_utils import get_attribute_effective_value_layer_info
from omni.usd._impl.timesample_utils import get_frame_time
from omni.usd._impl.timesample_utils import get_frame_time_code
from omni.usd._impl.timesample_utils import get_timesamples_count_in_authoring_layer
from omni.usd._impl.transform_helper import TransformHelper
from omni.usd._impl.utils import PrimCaching
from omni.usd._impl.utils import can_be_copied
from omni.usd._impl.utils import can_prim_have_children
from omni.usd._impl.utils import check_ancestral
from omni.usd._impl.utils import clear_attr_val_at_time
from omni.usd._impl.utils import correct_filename_case
from omni.usd._impl.utils import create_material_input
from omni.usd._impl.utils import duplicate_prim
from omni.usd._impl.utils import find_path_in_nodes
from omni.usd._impl.utils import find_spec_on_session_or_its_sublayers
from omni.usd._impl.utils import gather_default_attributes
from omni.usd._impl.utils import get_authored_prim
from omni.usd._impl.utils import get_composed_payloads_from_prim
from omni.usd._impl.utils import get_composed_references_from_prim
from omni.usd._impl.utils import get_context_from_stage
from omni.usd._impl.utils import get_introducing_layer
from omni.usd._impl.utils import get_local_transform_SRT
from omni.usd._impl.utils import get_local_transform_matrix
from omni.usd._impl.utils import get_prim_at_path
from omni.usd._impl.utils import get_prim_descendents
from omni.usd._impl.utils import get_prop_at_path
from omni.usd._impl.utils import get_prop_auto_target_session_layer
from omni.usd._impl.utils import get_sdf_layer
from omni.usd._impl.utils import get_shader_from_material
from omni.usd._impl.utils import get_stage_next_free_path
from omni.usd._impl.utils import get_subidentifier_from_material
from omni.usd._impl.utils import get_subidentifier_from_mdl
from omni.usd._impl.utils import get_url_from_prim
from omni.usd._impl.utils import get_world_transform_matrix
from omni.usd._impl.utils import handle_exception
from omni.usd._impl.utils import is_ancestor_prim_type
from omni.usd._impl.utils import is_child_type
from omni.usd._impl.utils import is_hidden_type
from omni.usd._impl.utils import is_path_valid
from omni.usd._impl.utils import is_prim_material_supported
from omni.usd._impl.utils import is_usd_crate_file
from omni.usd._impl.utils import is_usd_crate_file_version_supported
from omni.usd._impl.utils import is_usd_readable_filetype
from omni.usd._impl.utils import is_usd_writable_filetype
from omni.usd._impl.utils import make_path_relative_to_current_edit_target
from omni.usd._impl.utils import readable_usd_dotted_file_exts
from omni.usd._impl.utils import readable_usd_file_exts
from omni.usd._impl.utils import readable_usd_file_exts_str
from omni.usd._impl.utils import readable_usd_files_desc
from omni.usd._impl.utils import readable_usd_re
from omni.usd._impl.utils import remove_property
from omni.usd._impl.utils import set_attr_val
from omni.usd._impl.utils import set_prop_val
from omni.usd._impl.utils import writable_usd_dotted_file_exts
from omni.usd._impl.utils import writable_usd_file_exts
from omni.usd._impl.utils import writable_usd_file_exts_str
from omni.usd._impl.utils import writable_usd_files_desc
from omni.usd._impl.utils import writable_usd_re
from omni.usd._impl.watcher import UsdWatcher
from omni.usd._impl.watcher import get_watcher
from omni.usd._usd import AudioManager
from omni.usd._usd import EngineCreationFlags
from omni.usd._usd import HydraEngineCreationConfig
from omni.usd._usd import HydraEngineDesc
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
from omni.usd._usd import create_hydra_engine
from omni.usd._usd import create_hydra_engine_with_config
from omni.usd._usd import destroy_context
from omni.usd._usd import destroy_hydra_engine
from omni.usd._usd import get_context
from omni.usd._usd import get_context_from_stage_id
from omni.usd._usd import make_valid_identifier
from omni.usd._usd import merge_layers
from omni.usd._usd import merge_prim_spec
from omni.usd._usd import release_all_hydra_engines
from omni.usd._usd import resolve_paths
from omni.usd._usd import resolve_prim_path_references
from omni.usd._usd import resolve_prim_paths_references
from omni.usd._usd import shutdown_usd
from omni.usd._usd import stage_event_type
from omni.usd._usd import stage_rendering_event_type
from pxr import Gf
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdLux
from pxr import UsdShade
from pxr import UsdUtils
import re as re
import typing as typing
from typing import Any
import weakref as weakref
from . import api
from . import layer_utils
from . import prim_lists
from . import timesample_utils
from . import transform_helper
from . import utils
from . import watcher
__all__: list[str] = ['Any', 'AudioManager', 'EngineCreationFlags', 'Enum', 'Gf', 'HydraEngineCreationConfig', 'HydraEngineDesc', 'HydraEngineInvalidUniqueId', 'MOTION_RAYTRACING_ENABLED', 'NONE', 'OpaqueSharedHydraEngineContext', 'PickingMode', 'PrimCaching', 'SKIP_ON_WORKER_PROCESS', 'Sdf', 'Selection', 'StageEventType', 'StageRenderingEventType', 'StageState', 'Tf', 'Trace', 'TransformHelper', 'Usd', 'UsdContext', 'UsdContextInitialLoadSet', 'UsdExtension', 'UsdGeom', 'UsdLux', 'UsdShade', 'UsdUtils', 'UsdWatcher', 'Value_On_Layer', 'WRITABLE_USD_FILE_EXTS_STR', 'add_hydra_engine', 'api', 'asyncio', 'attach_all_hydra_engines', 'attr_has_timesample_on_key', 'can_be_copied', 'can_prim_have_children', 'carb', 'check_ancestral', 'clear_attr_val_at_time', 'copy_timesamples_from_weaker_layer', 'correct_filename_case', 'create_context', 'create_hydra_engine', 'create_hydra_engine_with_config', 'create_material_input', 'destroy_context', 'destroy_hydra_engine', 'duplicate_prim', 'find_path_in_nodes', 'find_spec_on_session_or_its_sublayers', 'functools', 'gather_default_attributes', 'get_all_sublayers', 'get_attribute_effective_defaultvalue_layer_info', 'get_attribute_effective_timesample_layer_info', 'get_attribute_effective_value_layer_info', 'get_authored_prim', 'get_composed_payloads_from_prim', 'get_composed_references_from_prim', 'get_context', 'get_context_from_stage', 'get_context_from_stage_id', 'get_dirty_layers', 'get_edit_target_identifier', 'get_eventdispatcher', 'get_frame_time', 'get_frame_time_code', 'get_geometry_standard_prim_list', 'get_introducing_layer', 'get_light_prim_list', 'get_local_transform_SRT', 'get_local_transform_matrix', 'get_prim_at_path', 'get_prim_descendents', 'get_prop_at_path', 'get_prop_auto_target_session_layer', 'get_sdf_layer', 'get_shader_from_material', 'get_stage_next_free_path', 'get_subidentifier_from_material', 'get_subidentifier_from_mdl', 'get_timesamples_count_in_authoring_layer', 'get_url_from_prim', 'get_watcher', 'get_world_transform_matrix', 'handle_exception', 'is_ancestor_prim_type', 'is_child_type', 'is_hidden_type', 'is_layer_locked', 'is_layer_writable', 'is_path_valid', 'is_prim_material_supported', 'is_usd_crate_file', 'is_usd_crate_file_version_supported', 'is_usd_readable_filetype', 'is_usd_writable_filetype', 'layer_utils', 'make_path_relative_to_current_edit_target', 'make_valid_identifier', 'merge_layers', 'merge_prim_spec', 'omni', 'on_layers_saved_result', 'on_stage_result', 'partial', 'prim_lists', 're', 'readable_usd_dotted_file_exts', 'readable_usd_file_exts', 'readable_usd_file_exts_str', 'readable_usd_files_desc', 'readable_usd_re', 'release_all_hydra_engines', 'remove_property', 'resolve_paths', 'resolve_prim_path_references', 'resolve_prim_paths_references', 'run_coroutine', 'set_attr_val', 'set_edit_target_by_identifier', 'set_prop_val', 'shutdown_usd', 'stage_event_type', 'stage_rendering_event_type', 'stitch_prim_specs', 'timesample_utils', 'transform_helper', 'typing', 'utils', 'watcher', 'weakref', 'writable_usd_dotted_file_exts', 'writable_usd_file_exts', 'writable_usd_file_exts_str', 'writable_usd_files_desc', 'writable_usd_re']
class UsdExtension(omni.ext._extensions.IExt):
    """
    omni.usd extension class.
    """
    def _UsdExtension__clear_history(self):
        ...
    def _UsdExtension__init_stage_event(self, app):
        ...
    def _UsdExtension__on_stage_closing(self):
        ...
    def _UsdExtension__on_stage_opened(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
def _get_stage(self):
    """
    Gets current opened :class:`pxr.Usd.Stage`
    """
def _next_frame_async(self, viewport = None, n_frames: int = 1) -> None:
    """
    Wait for an amount of frame complete events from Kit, possibly targeting a specific viewport.
    """
HydraEngineInvalidUniqueId: int = 4294967295
MOTION_RAYTRACING_ENABLED: omni.usd._usd.EngineCreationFlags  # value = <EngineCreationFlags.MOTION_RAYTRACING_ENABLED: 1>
NONE: omni.usd._usd.EngineCreationFlags  # value = <EngineCreationFlags.NONE: 0>
SKIP_ON_WORKER_PROCESS: omni.usd._usd.EngineCreationFlags  # value = <EngineCreationFlags.SKIP_ON_WORKER_PROCESS: 2>
WRITABLE_USD_FILE_EXTS_STR: str = 'usd|usda|usdc|live'
