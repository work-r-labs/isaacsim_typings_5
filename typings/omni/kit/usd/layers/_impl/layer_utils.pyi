from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.usd.layers._impl.path_utils import PathUtils
import os as os
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
from pxr import UsdUtils
import typing
__all__: list = ['LayerUtils']
class LayerUtils:
    """
    LayerUtils provides utilities for operating layers.
    """
    LAYER_AUTHORING_LAYER_CUSTOM_KEY: typing.ClassVar[str] = 'authoring_layer'
    LAYER_LOCK_STATUS_CUSTOM_KEY: typing.ClassVar[str] = 'locked'
    LAYER_MUTENESS_CUSTOM_KEY: typing.ClassVar[str] = 'muteness'
    LAYER_NAME_CUSTOM_KEY: typing.ClassVar[str] = 'custom_name'
    LAYER_OMNI_CUSTOM_KEY: typing.ClassVar[str] = 'omni_layer'
    @staticmethod
    def _get_layer_custom_data_value(root_layer: pxr.Sdf.Layer, layer_identifier: str, key: str, default_value = None):
        ...
    @staticmethod
    def _is_versioning_enabled():
        ...
    @staticmethod
    def _remove_layer_custom_data_by_key(root_layer: pxr.Sdf.Layer, layer_identifier: str, key: str):
        ...
    @staticmethod
    def _set_layer_custom_data_value(root_layer: pxr.Sdf.Layer, layer_identifier: str, key: str, value):
        ...
    @staticmethod
    def create_checkpoint(layer_identifier: typing.Union[str, typing.List[str]], comment: str, force = False):
        ...
    @staticmethod
    def create_checkpoint_async(layer_identifier: typing.Union[str, typing.List[str]], comment: str, force = False):
        ...
    @staticmethod
    def create_checkpoint_for_stage_async(stage, comment: str, only_dirty_layers = False, force = False):
        ...
    @staticmethod
    def create_sublayer(layer: pxr.Sdf.Layer, sublayer_position: int, layer_identifier: str):
        """
        Creates new sublayer at specific position.
        
                Args:
                    layer (Sdf.Layer): Layer handle.
                    sublayer_position: Position to create the new layer.
                                       Position should be -1 (the last position) or above 0.
                                       If position == -1 or position > len(layer.subLayerPaths), it will create the sublayer at the end.
                                       Any other position will be treated as invalid index.
                    layer_identifier: New layer path. If it's empty or None, it will create anonymous layer.
        
                Return:
                    New sublayer handle or None if sublayer_position is not valid.
                
        """
    @staticmethod
    def get_all_sublayers(stage, include_session_layers = False, include_only_omni_layers = False, include_anonymous_layers = True) -> typing.List[str]:
        ...
    @staticmethod
    def get_custom_layer_name(layer: pxr.Sdf.Layer):
        """
        Gets the custom name of layer. This name is saved inside the custom data of layer.
        """
    @staticmethod
    def get_dirty_layers(stage, include_root_layer = True, include_only_omni_layers = False) -> typing.List[str]:
        ...
    @staticmethod
    def get_edit_target(stage) -> str:
        ...
    @staticmethod
    def get_layer_global_muteness(root_layer: pxr.Sdf.Layer, layer_identifier: str):
        ...
    @staticmethod
    def get_layer_lock_status(root_layer: pxr.Sdf.Layer, layer_identifier: str):
        ...
    @staticmethod
    def get_sublayer_identifier(layer_identifier: str, sublayer_position: int):
        """
        
                Gets the sublayer identifier at specific postion with validality.
        
                Args:
                    layer_identifier (str): Parent layer identifier.
                    sublayer_position (int): Position of sublayer. It must be -1, which means to
                    return the last item. Or it should be equal or above 0.
        
                Returns:
                    None if sublayer_position is invalid or overflow. Or sublayer identifier otherwise.
                
        """
    @staticmethod
    def get_sublayer_position_in_parent(parent_layer_identifier: str, layer_identifier: str):
        """
        
                Gets the sublayer position in the parent layer.
        
                Args:
                    parent_layer_identifier (str): Parent layer identifier.
                    layer_identifier (str): layer identifier to query.
        
                Returns:
                    Position of layer in the subLayerPaths of the parent, or -1 if it cannot be found.
                
        """
    @staticmethod
    def has_prim_spec(layer_identifier: str, prim_spec_path):
        ...
    @staticmethod
    def insert_sublayer(layer: pxr.Sdf.Layer, sublayer_position: int, layer_identifier: str, check_empty_layer = True):
        """
        Inserts new sublayer at specific position.
        
                Args:
                    layer (Sdf.Layer): Layer handle.
                    sublayer_position: Position to insert the new layer.
                                       Position should be -1 (the last position) or above 0.
                                       If position == -1 or position > len(layer.subLayerPaths), it will insert the sublayer at the end.
                                       Any other position will be treated as invalid index.
                    layer_identifier: New layer path.
        
                Return:
                    Sublayer handle or None if sublayer_position is not valid or layer_identifier is empty or inserted layer is not existed.
                
        """
    @staticmethod
    def is_layer_writable(layer_identifier) -> bool:
        """
        Checks if layer is a writable format or writable on the file system.
        """
    @staticmethod
    def move_layer(from_parent_layer_identifier, from_sublayer_position, to_parent_layer_identifier, to_sublayer_position, remove_source = False):
        """
        Move sublayer from source parent to position of target parent.
        
                Args:
                    from_parent_layer_identifier: The parent of source sublayer.
                    from_sublayer_position: The sublayer position to be moved.
                    to_parent_layer_identifier: The parent of target sublayer.
                    to_sublayer_position: The sublayer position in target parent that source moves to.
                    remove_source: Removes the source sublayer or not from source parent after move.
                                   If from_parent_layer_identifier == to_parent_layer_layer_identifier,
                                   it will always be True.
        
                Return:
                    True if it's successful, False otherwise,
                
        """
    @staticmethod
    def reload_all_layers(layer_identifiers: typing.Union[str, typing.List[str]]):
        """
        Reloads all layers in batch.
        """
    @staticmethod
    def remove_layer_global_muteness(root_layer: pxr.Sdf.Layer, layer_identifier: str):
        ...
    @staticmethod
    def remove_layer_lock_status(root_layer: pxr.Sdf.Layer, layer_identifier: str):
        ...
    @staticmethod
    def remove_prim_spec(layer: pxr.Sdf.Layer, prim_spec_path: typing.Union[str, pxr.Sdf.Path]):
        """
        
                Utility to remove prim spec from layer.
        
                Args:
                    layer (Sdf.Layer): Layer handle.
                    prim_spec_path (Union[str, Sdf.Path]): Path of prim spec.
        
                Returns:
                    True if success, or False otherwise.
                
        """
    @staticmethod
    def remove_sublayer(layer: pxr.Sdf.Layer, position):
        ...
    @staticmethod
    def replace_sublayer(layer: pxr.Sdf.Layer, sublayer_position: int, layer_identifier: str):
        """
        Replaces new sublayer at specific position.
        
                Args:
                    layer (Sdf.Layer): Layer handle.
                    sublayer_position: Position to insert the new layer.
                                       Position should be less than len(layer.subLayerPaths).
                                       Any other position will be treated as invalid index.
                    layer_identifier: New layer path.
        
                Return:
                    Sublayer handle or None if sublayer_position is not valid or layer_identifier is empty or replaced layer is not existed.
                
        """
    @staticmethod
    def resolve_paths(base_layer: pxr.Sdf.Layer, target_layer: pxr.Sdf.Layer, store_relative_path = True, relative_to_base_layer = False, copy_sublayer_offsets = False):
        """
        Resolve all paths from References, Sublayers and AssetPaths of target layer based on source layer.
                This function is used normally when you transfer the content from source layer to target layer that
                are not in the same directory. So it needs to resolve all references so that they point to correct
                location.
        
                Args:
                    base_layer (Sdf.Layer): Source layer that references in target layer based on.
                    target_layer (Sdf.Layer): Target layer to resolve.
                    store_relative_path (bool): True to store relative path, or False to store absolute path.
                                              if relative path cannot be computed (like source layer and
                                              target are not in the same domain), it will save absolute paths.
                    relative_to_base_layer (bool): True if the relative path is computed against the target_layer.
                                              False otherwise.
                    copy_sublayer_offsets (bool): True to copy sublayer offsets and scales from base to target.
                
        """
    @staticmethod
    def restore_authoring_layer_from_custom_data(stage):
        ...
    @staticmethod
    def restore_muteness_from_custom_data(stage):
        ...
    @staticmethod
    def save_authoring_layer_to_custom_data(stage):
        ...
    @staticmethod
    def set_custom_layer_name(layer: pxr.Sdf.Layer, name: str):
        """
        
                Sets the custom name of layer, or clear it if name is empty or None.
                The name is saved inside the custom data of layer and can only be
                consumed by Kit application.
                
        """
    @staticmethod
    def set_edit_target(stage, layer_identifier):
        ...
    @staticmethod
    def set_layer_global_muteness(root_layer: pxr.Sdf.Layer, layer_identifier: str, muted: bool):
        ...
    @staticmethod
    def set_layer_lock_status(root_layer: pxr.Sdf.Layer, layer_identifier: str, locked: bool):
        ...
    @staticmethod
    def transfer_layer_content(source_layer: pxr.Sdf.Layer, target_layer: pxr.Sdf.Layer, copy_custom_data = True, skip_sublayers = True):
        """
        
                Transfer layer content from source layer to target layer with re-pathing all external
                dependencies.
        
                Args:
                    source_layer (Sdf.Layer): Source layer handle.
                    target_layer (Sdf.Layer): Target layer handle.
                    copy_custom_data (bool): Whether copying layer metadata or not.
                    skip_sublayers (bool): Whether skipping to copy sublayers or not if copy_custom_data is True.
                
        """
