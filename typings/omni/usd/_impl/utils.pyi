from __future__ import annotations
import asyncio as asyncio
import carb as carb
import functools as functools
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.usd._usd import get_context_from_stage_id
import pxr.Gf
from pxr import Gf
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
from pxr import UsdLux
from pxr import UsdShade
from pxr import UsdUtils
import re as re
import typing as typing
import weakref as weakref
__all__ = ['Gf', 'PrimCaching', 'Sdf', 'Tf', 'Trace', 'Usd', 'UsdGeom', 'UsdLux', 'UsdShade', 'UsdUtils', 'WRITABLE_USD_FILE_EXTS_STR', 'asyncio', 'can_be_copied', 'can_prim_have_children', 'carb', 'check_ancestral', 'clear_attr_val_at_time', 'correct_filename_case', 'create_material_input', 'duplicate_prim', 'find_path_in_nodes', 'find_spec_on_session_or_its_sublayers', 'functools', 'gather_default_attributes', 'get_authored_prim', 'get_composed_payloads_from_prim', 'get_composed_references_from_prim', 'get_context_from_stage', 'get_context_from_stage_id', 'get_introducing_layer', 'get_local_transform_SRT', 'get_local_transform_matrix', 'get_prim_at_path', 'get_prim_descendents', 'get_prop_at_path', 'get_prop_auto_target_session_layer', 'get_sdf_layer', 'get_shader_from_material', 'get_stage_next_free_path', 'get_subidentifier_from_material', 'get_subidentifier_from_mdl', 'get_url_from_prim', 'get_world_transform_matrix', 'handle_exception', 'is_ancestor_prim_type', 'is_child_type', 'is_hidden_type', 'is_path_valid', 'is_prim_material_supported', 'is_usd_readable_filetype', 'is_usd_writable_filetype', 'make_path_relative_to_current_edit_target', 'omni', 're', 'readable_usd_dotted_file_exts', 'readable_usd_file_exts', 'readable_usd_file_exts_str', 'readable_usd_files_desc', 'readable_usd_re', 'remove_property', 'run_coroutine', 'set_attr_val', 'set_prop_val', 'typing', 'weakref', 'writable_usd_dotted_file_exts', 'writable_usd_file_exts', 'writable_usd_file_exts_str', 'writable_usd_files_desc', 'writable_usd_re']
class PrimCaching:
    """
    Internal. Utility class that monitors changes from specific prim type.
    """
    @staticmethod
    def _on_usd_changed(*args, **kwargs):
        ...
    @staticmethod
    def _update_usd_cache_state(*args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, usd_type: typing.Any, stage: pxr.Usd.Stage, on_changed: typing.Callable[[], NoneType] = None):
        """
        Constructor.
        
                Args:
                    usd_type (Any): Usd prim type, like UsdShade.Material, UsdShade.Shader, etc.
                    stage (Usd.Stage): The stage to listen.
                    on_changed (Callable[[], None], optional): The callback to invoke when interested prims are changed or any prims are removed.
                        Defaults to None.
                
        """
    def _on_stage_event(self, event: carb.events._events.IEvent):
        ...
    def destroy(self):
        ...
    def get_cache_state(self) -> bool:
        """
        Gets cache state.
        
                Returns:
                    bool: True if cached, or False otherwise.
                
        """
    def get_stage(self) -> typing.Optional[pxr.Usd.Stage]:
        """
        Gets listened stage handle.
        
                Returns:
                    Optional[Usd.Stage]: Stage handle or None.
                
        """
    def set_cache_state(self, state: bool):
        """
        Sets cache state.
        
                Args:
                    state (bool): True for cached, and False for non-cached.
                
        """
def __get_stage(usd_context_or_stage: typing.Union[str, pxr.Usd.Stage] = ''):
    ...
def _bake_readable_usd_file_info():
    ...
def _set_prop_val(prop: pxr.Usd.Property, val: typing.Any, time_code = ...):
    ...
def can_be_copied(prim):
    """
    Internal. If the prim can be copied. A prim can be copied means the prim is authored to the local layer stack directly.
    
        REMINDER: This function works differently as :class:`omni.usd.commands.CopyPrimCommand`.
        Please don't depend on this function to check if a prim can be copied or not. It's kept for
        back compatibility.
        
    """
def can_prim_have_children(stage: pxr.Usd.Stage, new_path: pxr.Sdf.Path, prim: pxr.Usd.Prim):
    """
    Internal. If a prim can have children authored.
    
        It's recommended from Pixar USD that UsdGeom.Gprim is better to be the leaf node instead of
        having children attached. This function will check if it's a UsdGeom.Gprim or it's already under
        a UsdGeom.Gprim node.
    
        Args:
            stage (Usd.Stage): The stage of the prim.
            new_path (Sdf.Path): New prim path to create under the parent.
            prim (Usd.Prim): The parent prim.
        
    """
def check_ancestral(prim: pxr.Usd.Prim) -> bool:
    """
    Check if prim is brought into composition by its ancestor.
    
        Args:
            prim (Usd.Prim): The prim to check.
    
        Returns:
            bool: True if it's ancestral prim, or False otherwise.
        
    """
def clear_attr_val_at_time(attr: pxr.Usd.Attribute, time_code = ..., auto_target_layer: bool = True):
    """
    Clears attribute at specified timecode.
    
        Args:
            attr (Usd.Attribute): Attribute handle.
            time_code (_type_, optional): specified timecode. Defaults to Usd.TimeCode.Default().
            auto_target_layer (bool, optional): When it's True and the property exists in session layer or its sublayers,
                it will switch EditTarget to the session layer instead to clear the strongest opinion. Defaults to True.
        
    """
def correct_filename_case(file: str) -> str:
    """
    Internal.
    """
def create_material_input(prim: pxr.Usd.Prim, name: str, value: typing.Any, vtype: str, def_value: typing.Any = None, min_value: typing.Any = None, max_value: typing.Any = None, display_name: str = None, display_group: str = None, color_space: str = None) -> pxr.Usd.Attribute:
    """
    Creates a material input.
    
        Args:
            prim (Usd.Prim): Prim handle.
            name (str): Name of the input.
            value (Any): Value of the input.
            vtype (str): Type of the value.
            def_value (Any, optional): Default value. Defaults to None.
            min_value (Any, optional): Min value. Defaults to None.
            max_value (Any, optional): Max value. Defaults to None.
            display_name (str, optional): Display name. Defaults to None.
            display_group (str, optional): Display group. Defaults to None.
            color_space (str, optional): Color space of the input. Defaults to None.
    
        Returns:
            Usd.Attribute: The created input attribute.
        
    """
def duplicate_prim(stage: pxr.Usd.Stage, prim_path: typing.Union[str, pxr.Sdf.Path], path_to: typing.Union[str, pxr.Sdf.Path], duplicate_layers: bool = True):
    """
    
        Duplicate prim.
    
        Args:
            stage (Usd.Stage): Stage handle.
    
            prim_path (Union[str, Sdf.Path]): Prim path.
    
            path_to (Union[str, Sdf.Path]): Copy to path.
    
            duplicate_layers (bool): True if it's to duplicate this prim in all local layers.
                False if it's to duplicate this prim to the current edit target. And it
                depends on whether the prim is defined or not. If it's not defined, it will only
                copy the opinions in the current edit target if it exists. Otherwise, it
                will copy the def to the current edit target, even it's from other layers
                instead of the current edit target. If you want to collapse all overrides
                inside all local layers for the prim, see omni.usd.stitch_prim_specs for reference.
        Return:
            True if successful, or false otherwise.
        
    """
def find_path_in_nodes(node, set_fn):
    """
    Internal. Finds specific spec recursively from node's layer stack.
    """
def find_spec_on_session_or_its_sublayers(*args, **kwds):
    """
    
        Finds spec in the session layer or its sublayers.
    
        Args:
            stage (Usd.Stage): Stage instance.
            path (Sdf.Path): Spec path to find.
            predicate (Callable[[Sdf.Spec], bool]): If it's provided, the spec to find must pass the predicate.
    
        Returns:
            (Sdf.Layer, Sdf.Spec): Layer that the spec resides in, and the spec handle. Or (None, None) if it cannot be found.
        
    """
def gather_default_attributes(prim_type):
    """
    Internal. Gets default attributes for specific prim type.
    """
def get_authored_prim(prim):
    """
    Internal.
    """
def get_composed_payloads_from_prim(prim: pxr.Usd.Prim, fix_slashes: bool = True) -> typing.List[typing.Tuple[pxr.Sdf.Payload, pxr.Sdf.Layer]]:
    """
    Gets composed payload list from prim.
    
        Args:
            prim (Usd.Prim): Handle of Usd.Prim.
    
        Returns:
            List of payload items. Each item is a tuple that includes payload handle, and
            the layer it's from.
        
    """
def get_composed_references_from_prim(prim: pxr.Usd.Prim, fix_slashes: bool = True) -> typing.List[typing.Tuple[pxr.Sdf.Reference, pxr.Sdf.Layer]]:
    """
    Gets composed reference list from prim.
    
        Args:
            prim (Usd.Prim): Handle of Usd.Prim.
    
        Returns:
            List of reference items. Each item is a tuple that includes reference handle, and
            the layer it's from.
        
    """
def get_context_from_stage(stage):
    """
    Gets corresponding UsdContext of the stage if it's found.
    """
def get_introducing_layer(prim: pxr.Usd.Prim) -> typing.Tuple[pxr.Sdf.Layer, pxr.Sdf.Path]:
    """
    Gets the introducing layer.
    
        This function will find the local layer that defines this prim, or the first introducing
        layer that introduces the prim into the local layer stack if prim is defined in a reference
        or payload.
    
        An introducting layer is the layer that adds the prim into the composition graph.
        The difference of this function to Usd.PrimCompositionQuery is that it will return
        the first local layer where the prim is defined. If it's not defined locally, it will find
        the reference or payload arcs with Usd.PrimCompositionQuery to find the first introducing
        layer and its introducing prim path in the local layer stack.
    
        Args:
            prim (Usd.Prim): Prim handle
    
        Returns:
            Tuple[Sdf.Layer, Sdf.Path]: Introducing layer and its introducing prim path.
        
    """
def get_local_transform_SRT(prim, time = ...) -> typing.Tuple[pxr.Gf.Vec3d | pxr.Gf.Vec3f | pxr.Gf.Vec3h, pxr.Gf.Vec3d | pxr.Gf.Vec3f | pxr.Gf.Vec3h, pxr.Gf.Vec3i, pxr.Gf.Vec3d | pxr.Gf.Vec3f | pxr.Gf.Vec3h]:
    """
    Internal. Return a tuple of [scale, rotation, rotation_order, translate] for given prim.
    """
def get_local_transform_matrix(prim: pxr.Usd.Prim, time_code: pxr.Usd.TimeCode = ...) -> pxr.Gf.Matrix4d:
    """
    Gets local transform matrix of specific time code from prim.
    
        Args:
            prim (Usd.Prim): The prim handle.
            time_code (Usd.TimeCode, optional): Time code to query. Defaults to Usd.TimeCode.Default().
    
        Returns:
            Gf.Matrix4d: Local transform matrix.
        
    """
def get_prim_at_path(path: pxr.Sdf.Path, usd_context_name: typing.Union[str, pxr.Usd.Stage] = '') -> pxr.Usd.Prim:
    """
    Internal. Gets prim at specific path.
    """
def get_prim_descendents(root_prim: pxr.Usd.Prim) -> typing.List[pxr.Usd.Prim]:
    """
    Internal. Returns all descendants for a given prim.
    
        Args:
            root_prim (Usd.Prim): The root prim to query.
    
        Returns:
            List[Usd.Prim]: A list of prim handles.
        
    """
def get_prop_at_path(path: pxr.Sdf.Path, usd_context_name: typing.Union[str, pxr.Usd.Stage] = '') -> pxr.Usd.Property:
    """
    Internal. Gets property at specific path.
    """
def get_prop_auto_target_session_layer(stage: pxr.Usd.Stage, prop_path: pxr.Sdf.Path):
    """
    
        Get property auto retarget layer.
    
        Args:
            stage (Usd.Stage): Usd stage
            prop_path (Sdf.Path): property path
        
    """
def get_sdf_layer(prim):
    """
    Internal. Gets the introducing layer of the prim.
    """
def get_shader_from_material(prim, get_prim = False):
    ...
def get_stage_next_free_path(stage: pxr.Usd.Stage, path: typing.Union[str, pxr.Sdf.Path], prepend_default_prim: bool):
    """
    Gets a new prim path that doesn't exist in the stage given a base path.
    
        If the given path doesn't exist in the stage already, it returns the given path directly.
        Otherwise, it appends a suffix with number index to the given path until it finds a path that's not taken.
    
        Args:
            stage (Usd.Stage): The stage handle.
            path (Union[str, Sdf.Path]): Base prim path.
            prepend_default_prim (bool): Whether it should prepend default prim name to the path or not.
    
        Raises:
            ValueError: Path is not a valid prim path.
    
        Returns:
            str: prim path that doesn't exist in the stage.
        
    """
def get_subidentifier_from_material(prim: pxr.Usd.Prim, on_complete_fn: typing.Callable = None):
    """
    Deprecated. Use {py:func}`omni.kit.material.library.get_subidentifier_from_material` instead.
    """
def get_subidentifier_from_mdl(mdl_file: str, on_complete_fn: typing.Callable = None):
    """
    Deprecated. Use {py:func}`omni.kit.material.library.get_subidentifier_from_mdl` instead.
    """
def get_url_from_prim(prim):
    """
    Returns url of Prim when authored reference or None.
    """
def get_world_transform_matrix(prim: pxr.Usd.Prim, time_code: pxr.Usd.TimeCode = ...) -> pxr.Gf.Matrix4d:
    """
    Gets work transform matrix of specific time code from prim.
    
        Args:
            prim (Usd.Prim): The prim handle.
            time_code (Usd.TimeCode, optional): Time code to query. Defaults to Usd.TimeCode.Default().
    
        Returns:
            Gf.Matrix4d: World transform matrix.
        
    """
def handle_exception(func):
    """
    Decorator to print exception in async functions.
    """
def is_ancestor_prim_type(*args, **kwargs):
    """
    Internal. If any parent prims of the prim are specific type.
    """
def is_child_type(*args, **kwargs):
    """
    Internal. If prim has specific type of children.
    """
def is_hidden_type(*args, **kwargs):
    """
    Internal. If prim or its parent has metadata "hide_in_stage_window" authored. 
    """
def is_path_valid(path: typing.Union[str, pxr.Sdf.Path]):
    """
    Internal. If the path points to a valid USD object in the default UsdContext.
    """
def is_prim_material_supported(prim):
    """
    Internal. If material can be bound to the prim.
    """
def is_usd_readable_filetype(filepath: str) -> bool:
    """
    Whether the given file path is a supported readable USD file or not.
    """
def is_usd_writable_filetype(filepath: str) -> bool:
    """
    Whether the given file path is a supported writable USD file or not.
    """
def make_path_relative_to_current_edit_target(url_path: str, stage: pxr.Usd.Stage = None) -> str:
    """
    Make path relative to the current edit target of the stage.
    
        Args:
            url_path (str): The asset url.
            stage (Usd.Stage, optional): The stage that the **url_path** is relative to. Defaults to None.
    
        Returns:
            str: Relative path if it can be computed or url_path untouched.
        
    """
def readable_usd_dotted_file_exts() -> typing.List[str]:
    """
    Gets a list of file extensions about readable USD formats.
    
        Returns:
            List[str]: A list of file extensions, like ('usd', 'usda', 'usdc', 'live').
        
    """
def readable_usd_file_exts() -> typing.List[str]:
    """
    Gets a list of file extensions (without dots) about readable USD formats.
    
        Returns:
            List[str]: A list of file extensions (without dots), like ('usd', 'usda', 'usdc', 'live').
        
    """
def readable_usd_file_exts_str() -> str:
    """
    Gets a string that includes all readable USD file formats supported by Kit.
    
        Returns:
            str: A string includes all file extensions of readable USD formats, and is separated by "|", like "usd|usda|usdc|live".
        
    """
def readable_usd_files_desc() -> str:
    """
    Gets a description of all readable USD file formats.
    
        Returns:
            str: A description string, like "USD Files (*.usd;*.usda;*.usdc;*.live)
        
    """
def readable_usd_re() -> re.Pattern:
    """
    Gets the regex that matches readable USD files.
    
        Returns:
            re.Pattern: A compiled regex.
        
    """
def remove_property(prim_path: typing.Union[str, pxr.Sdf.Path], property_name: str, usd_context_or_stage: typing.Union[str, pxr.Usd.Stage] = ''):
    """
    Removes specified property from the prim.
    
        Args:
            prim_path (Union[str, Sdf.Path]): Prim path.
            property_name (str): Specified property name.
            usd_context_or_stage (Union[str, Usd.Stage], optional): Stage or UsdContext applies the changes to.
                It can be instance of Usd.Stage or context name. By default, it will apply
                the changes to the stage in default UsdContext.
        
    """
def set_attr_val(attr: pxr.Usd.Attribute, val: typing.Any, time_code = ..., auto_target_layer: bool = True):
    """
    
        Deprecated. See :func:`.set_prop_val` instead.
        
    """
def set_prop_val(prop: pxr.Usd.Property, val: typing.Any, time_code = ..., auto_target_layer: bool = True):
    """
    
        Sets the value of property.
    
        Args:
            prop (Usd.Property): Property handle.
            val (typing.Any): Value of property.
            time_code (Usd.TimeCode): Time code to set, and it's Usd.TimeCode.Default() by default.
            auto_target_layer (bool): Default is True. If it's true, it will be authored into the sesison layer if
                the prim of the property is defined in the session layer. If it's not defined in the session layer,
                it will find the property inside the session layer to check if there are overrides.
                If overrides are found, the value will be authored into the found layer instead.
                Otherwise, it will be authored into the current edit target.
        
    """
def writable_usd_dotted_file_exts() -> typing.List[str]:
    """
    Gets a list of file extensions about writable USD formats.
    
        Returns:
            List[str]: A list of file extensions, like ('usd', 'usda', 'usdc', 'live').
        
    """
def writable_usd_file_exts() -> typing.List[str]:
    """
    Gets a list of file extensions (without dots) about writable USD formats.
    
        Returns:
            List[str]: A list of file extensions (without dots), like ('usd', 'usda', 'usdc', 'live').
        
    """
def writable_usd_file_exts_str() -> str:
    """
    Gets a string that includes all writable USD file formats supported by Kit.
    
        Returns:
            str: A string includes all file extensions of writable usd formats, and is separated by "|", like "usd|usda|usdc|live".
        
    """
def writable_usd_files_desc() -> str:
    """
    Gets a description of all writable USD file formats.
    
        Returns:
            str: A description string, like "USD Files (*.usd;*.usda;*.usdc;*.live)
        
    """
def writable_usd_re() -> re.Pattern:
    """
    Gets the regex that matches writable USD files.
    
        Returns:
            re.Pattern: A compiled regex.
        
    """
WRITABLE_USD_FILE_EXTS_STR: str = 'usd|usda|usdc|live'
_readable_usd_dotted_file_exts: tuple = ('.FBX', '.OBJ', '.abc', '.drc', '.fbx', '.glb', '.gltf', '.live', '.lxo', '.md5', '.metricsAssembler', '.mtlx', '.obj', '.omniabc', '.usd', '.usda', '.usdc', '.usdz')
_readable_usd_file_exts: tuple = ('FBX', 'OBJ', 'abc', 'drc', 'fbx', 'glb', 'gltf', 'live', 'lxo', 'md5', 'metricsAssembler', 'mtlx', 'obj', 'omniabc', 'usd', 'usda', 'usdc', 'usdz')
_readable_usd_file_exts_str: str = 'FBX|OBJ|abc|drc|fbx|glb|gltf|live|lxo|md5|metricsAssembler|mtlx|obj|omniabc|usd|usda|usdc|usdz'
_readable_usd_files_desc: str = 'USD Readable Files (*.FBX;*.OBJ;*.abc;*.drc;*.fbx;*.glb;*.gltf;*.live;*.lxo;*.md5;*.metricsAssembler;*.mtlx;*.obj;*.omniabc;*.usd;*.usda;*.usdc;*.usdz)'
_readable_usd_re: re.Pattern  # value = re.compile('^[^?]*\\.(FBX|OBJ|abc|drc|fbx|glb|gltf|live|lxo|md5|metricsAssembler|mtlx|obj|omniabc|usd|usda|usdc|usdz)(\\?.*)?$', re.IGNORECASE)
_writable_usd_dotted_file_exts: tuple = ('.usd', '.usda', '.usdc', '.live')
_writable_usd_file_exts: tuple = ('usd', 'usda', 'usdc', 'live')
_writable_usd_files_desc: str = 'USD Files (*.usd;*.usda;*.usdc;*.live)'
_writable_usd_re: re.Pattern  # value = re.compile('^[^?]*\\.(usd|usda|usdc|live)(\\?.*)?$', re.IGNORECASE)
