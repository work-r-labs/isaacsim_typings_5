import OmniAudioSchema as OmniAudioSchema
from __future__ import annotations
import carb as carb
import enum
from enum import Enum
from enum import auto
import math as math
import omni as omni
from omni.kit.usd_undo.layer_undo import UsdEditTargetUndo
from omni.usd.commands.stage_helper import UsdStageHelper
import os as os
import pxr.Gf
from pxr import Gf
from pxr import Kind
import pxr.Sdf
from pxr import Sdf
from pxr import Sdr
from pxr import Tf
from pxr import Trace
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import pxr.UsdGeom
from pxr import UsdLux
from pxr import UsdShade
import typing
import weakref as weakref
__all__ = ['AddPayloadCommand', 'AddReferenceCommand', 'AddRelationshipTargetCommand', 'BindMaterialCommand', 'ChangeAttributesColorSpaceCommand', 'ChangeMetadataCommand', 'ChangeMetadataInPrimsCommand', 'ChangePropertyCommand', 'ClearCurvesSplitsOverridesCommand', 'ClearRefinementOverridesCommand', 'CopyPrimCommand', 'CopyPrimsCommand', 'CreateAudioPrimFromAssetPathCommand', 'CreateDefaultXformOnPrimCommand', 'CreateInstanceCommand', 'CreateInstancesCommand', 'CreateMdlMaterialPrimCommand', 'CreateMtlxMaterialPrimCommand', 'CreatePayloadCommand', 'CreatePreviewSurfaceMaterialPrimCommand', 'CreatePreviewSurfaceTextureMaterialPrimCommand', 'CreatePrimCommand', 'CreatePrimCommandBase', 'CreatePrimWithDefaultXformCommand', 'CreatePrimsCommand', 'CreateReferenceCommand', 'CreateShaderPrimFromSdrCommand', 'CreateUsdAttributeCommand', 'CreateUsdAttributeOnPathCommand', 'DeletePrimsCommand', 'Enum', 'FramePrimsCommand', 'Gf', 'GroupPrimsCommand', 'Kind', 'MovePrimCommand', 'MovePrimsCommand', 'OmniAudioSchema', 'PERSISTENT_SETTINGS_PREFIX', 'ParentPrimsCommand', 'PayloadCommandBase', 'ReferenceCommandBase', 'RelationshipTargetBase', 'RemovePayloadCommand', 'RemovePropertyCommand', 'RemoveReferenceCommand', 'RemoveRelationshipTargetCommand', 'RenamePrimCommand', 'ReplacePayloadCommand', 'ReplaceReferenceCommand', 'ReplaceReferencesCommand', 'SETTING_NESTED_GPRIMS_AUTHORING', 'Sdf', 'Sdr', 'SelectPrimsCommand', 'SetMaterialStrengthCommand', 'SetPayLoadLoadSelectedPrimsCommand', 'SetRelationshipTargetsCommand', 'Tf', 'ToggleActivePrimsCommand', 'TogglePayLoadLoadSelectedPrimsCommand', 'ToggleVisibilitySelectedPrimsCommand', 'Trace', 'TransformPrimCommand', 'TransformPrimSRTCommand', 'TransformPrimsCommand', 'TransformPrimsSRTCommand', 'UngroupPrimsCommand', 'UnhideAllPrimsCommand', 'UnparentPrimsCommand', 'Usd', 'UsdEditTargetUndo', 'UsdGeom', 'UsdLux', 'UsdShade', 'UsdStageHelper', 'active_edit_context', 'allow_prim_parenting', 'auto', 'carb', 'ensure_parents_are_active', 'get_child_position_in_the_parent', 'get_context_and_stage', 'get_default_camera_rotation_order_str', 'get_default_rotation_order_str', 'get_default_rotation_order_type', 'math', 'move_prim_to_location', 'omni', 'os', 'post_notification', 'prim_can_be_removed_without_destruction', 'remove_prim_spec', 'should_keep_children_order', 'weakref', 'write_refinement_override_enabled_hint']
class AddPayloadCommand(PayloadCommandBase):
    """
    Add a payload to primitive.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, payload: pxr.Sdf.Payload, position = ...):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): The stage to operate.
                    prim_path (Sdf.Path): The prim path to add payload.
                    payload (Sdf.Payload): The payload to be added.
                    position (Usd.ListPosition): The list position to add the payload. Defaults to Usd.ListPositionBackOfPrependList.
                
        """
    def do(self):
        ...
class AddReferenceCommand(ReferenceCommandBase):
    """
    Add reference to primitive.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, reference: pxr.Sdf.Reference, position: pxr.Usd.ListPosition = ...):
        """
        Constructor.
        
                Args:
                    stage (Usd.Stage): The stage to operate.
                    prim_path (Sdf.Path): The prim path to add reference.
                    reference (Sdf.Reference): The reference to be added.
                    position (Usd.ListPosition): The list position to add the reference. Defaults to Usd.ListPositionBackOfPrependList.
                
        """
    def do(self):
        ...
class AddRelationshipTargetCommand(RelationshipTargetBase):
    """
    Add target to a relationship.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, relationship: pxr.Usd.Relationship, target: pxr.Sdf.Path, position: pxr.Usd.ListPosition = ...):
        """
        Constructor.
        
                Args:
                    relationship (Usd.Relationship): Relationship handle.
                    target (Sdf.Path): The target path to add into the target list of relationship.
                    position (Usd.ListPosition, optional): List position to add the target path to. Defaults to Usd.ListPositionBackOfPrependList.
                
        """
    def do(self):
        ...
class BindMaterialCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    Bind material to a primitive.
    """
    class PathType(enum.Enum):
        """
        An enumeration.
        """
        Collection: typing.ClassVar[BindMaterialCommand.PathType]  # value = <PathType.Collection: 2>
        Neither: typing.ClassVar[BindMaterialCommand.PathType]  # value = <PathType.Neither: 3>
        Prim: typing.ClassVar[BindMaterialCommand.PathType]  # value = <PathType.Prim: 1>
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def _get_binding_strength():
        ...
    def __init__(self, prim_path: typing.Union[str, list], material_path: str, strength = None, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None, material_purpose: typing.Optional[str] = ''):
        """
        
                Constructor.
        
                Args:
                    prim_path (str or list): Path(s) to prim or collection
                    material_path (str): Path to material to bind.
                    strength (float, optional): Strength. Default is None, which sets the strength value from setting
                        **/persistent/app/stage/materialStrength**. If no setting is set, it's set to
                        UsdShade.Tokens.weakerThanDescendants.
                    stage (Usd.Stage, optional): Stage to operate. Default is None, which means the stage in the default UsdContext is used.
                    context_name (str, optional): The usd context to operate. Default is None, which means the default UsdContext is used.
                    material_purpose (str, optional): Material purpose. Default is UsdShade.Tokens.allPurpose.
                
        """
    def _bind(self, binding_api, material_prim, strength = None, collection_api = None):
        ...
    def _bind_material(self, material_path, strength):
        ...
    def _bind_material_list(self, prim_paths, material_path, material_strength):
        ...
    def _get_path_type(self, path: str, stage: pxr.Usd.Stage):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class ChangeAttributesColorSpaceCommand(omni.kit.commands.command.Command):
    """
    Change attribute color space.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, attributes: typing.List[pxr.Usd.Attribute], color_space: typing.Any):
        """
        
                Constructor.
        
                Args:
                    attributes (List[str]): attributes to set color space on.
                    color_space: Value of metadata to change to.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class ChangeMetadataCommand(omni.kit.commands.command.Command):
    """
    Modify metadata of multiple objects.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, object_paths: typing.List[str], key: typing.Any, value: typing.Any, usd_context_name: str = ''):
        """
        
                Constructor.
        
                Args:
                    object_paths (List[str]): A list of object paths, which could be prims, attributes, etc.
                    key (Any): Key of metadata to change.
                    value (Any): Value of metadata to change to.
                    usd_context_name (str, optional): Name of the usd context to work on. Leave to "" to use default USD context.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class ChangeMetadataInPrimsCommand(omni.kit.commands.command.Command):
    """
    
        Deprecated. Modifies metadata of multiple primitives.
    
        See command :class:`.ChangeMetadataCommand`, which provides the same functionalities.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_paths: typing.List[str], key: typing.Any, value: typing.Any, usd_context_name: str = ''):
        """
        
                Constructor.
        
                Args:
                    prim_paths (List[str]): Prim paths.
                    key (Any): Key of metadata to change.
                    value (Any): Value of metadata to change to.
                    usd_context_name (str, optional): Name of the usd context to work on. Leave to "" to use default USD context.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class ChangePropertyCommand(omni.kit.commands.command.Command):
    """
    Change property value.
    
        By default, this command changes the value of the property when it exists.
        If the property doesn't exist, **type_to_create_if_not_exist** must be given to explicitly tell
        this command to create a new property with the new type and value.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    overriden_notification = None
    def __init__(self, prop_path: str, value: typing.Any, prev: typing.Any, timecode = ..., type_to_create_if_not_exist: pxr.Sdf.ValueTypeNames = None, target_layer: pxr.Sdf.Layer = None, usd_context_name: typing.Union[str, omni.usd._usd.UsdContext, pxr.Usd.Stage] = '', is_custom: bool = False, variability: pxr.Sdf.Variability = ...):
        """
        
                Constructor.
        
                Args:
                    prop_path (str): Prim property path.
                    value (Any): Value to change to. If it's None, current attribute value is cleared.
                    prev (Any): Value to undo to.
                    timecode (Usd.TimeCode, optional): The timecode to set property value to. Default is Usd.TimeCode.Default().
                    type_to_create_if_not_exist (Sdf.ValueTypeName): If not None and property doesn't exist, a new property will
                        be created with given type and value. Default is None.
                    target_layer (sdf.Layer, optional): Target layer to write value to. Leave to None to use the current edit target.
                    usd_context_name (Union[str, omni.usd.UsdContext, Usd.Stage], optional): Union that could be:
                                    * Name of the usd context to work on. Leave to "" to use default USD context.
                                    * Instance of UsdContext.
                                    * Or stage instance.
                                    Default is None, which means the default UsdContext is used.
                    is_custom (bool, optional): If the property is created, specifiy if it is a 'custom' property (not part of the Schema).
                        Default is False.
                    variability (Sdf.Variability, optional): If the property is created, specify the variability. Default is Sdf.VariabilityVarying.
                
        """
    def _clear_notification_if_dismissed(self):
        ...
    def _get_target_layer(self):
        ...
    def _has_overrides_in_stronger_layer(self, current_layer):
        ...
    def _set_prop_value(self) -> bool:
        ...
    def do(self):
        ...
    def undo(self):
        ...
class ClearCurvesSplitsOverridesCommand(omni.kit.commands.command.Command):
    """
    Clear Curves Splits Overrides.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def do(self):
        ...
class ClearRefinementOverridesCommand(omni.kit.commands.command.Command):
    """
    Clear Refinement Overrides.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class CopyPrimCommand(omni.kit.commands.command.Command):
    """
    Copy a primitive to a new path.
    
        Due to the complexity of the USD composition, this command provide several options to handle
        different scenarios:
    
        * A prim is defined and authored in single layer, this command will simply copy it.
        * A prim is defined and authored in multiple layers, this command will copy the prim according
          to options **duplicate_layers** and **combine_layers**. See :func:`omni.usd.commands.CopyPrimCommand.__init__` for reference.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path_from: str, path_to: str = None, duplicate_layers: bool = False, combine_layers: bool = False, exclusive_select: bool = True, usd_context_name: str = '', flatten_references: bool = False, copy_to_introducing_layer: bool = False):
        """
        
                Constructor.
        
                Args:
                    path_from (str): Path to copy from.
                    path_to (str, optional): Path to copy to. If it's None, a path is auto-generated from stage. Default is None.
                    duplicate_layers (bool, optional): Duplicate prim in all layers from the local layer stack. Default is False,
                        which means it only copies the prim spec with **def** specifier to the target path, and ignores all
                        **over** opinions in the other layers the local layer stack. This option can only be enabled when **combine_layers**
                        and copy_to_introducing_layer are False. This option is full with assumption and does not work well when prim
                        has multiple defs in different layers, which is mostly ok for now as most of the contents authored with Kit
                        has only one **def** for the same prim.
                    combine_layers (bool, optional): Combine layers on copy. When this option is enabled, it will combine all opinions
                        authored to the source prim scattered in all the layers from the local layer stack. Default is False.
                    exclusive_select (bool, optional): If to exclusively select (clear old selections) the newly create object. Default is True.
                    flatten_references (bool, optional): Flatten references during copy. It's only valid when **combine_layers** is True, and **copy_to_introducing_layer** is False.
                    copy_to_introducing_layer (bool, optional): If to copy it to the introducing layer, or the current edit target. Default is False,
                        which means the current edit target.
                
        """
    def do(self):
        ...
    def modify_callback_info(self, cb_type: str, cmd_args: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        ...
    def undo(self):
        ...
class CopyPrimsCommand(omni.kit.commands.command.Command):
    """
    
        Copy multiple primitives to new paths.
    
        This command is a batch version of command :class:`.CopyPrimCommand`.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, paths_from: typing.List[str], paths_to: typing.List[str] = None, duplicate_layers: bool = False, combine_layers: bool = False, flatten_references: bool = False, copy_to_introducing_layer: bool = False):
        """
        Constructor.
        
                See :func:`omni.usd.commands.CopyPrimCommand.__init__` for the details of all parameters except **paths_from**, which
                is a list of prim paths to be copied.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateAudioPrimFromAssetPathCommand(CreatePrimCommandBase):
    """
    Create a new Audio primitive from asset path.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, usd_context: omni.usd._usd.UsdContext, path_to: pxr.Sdf.Path, asset_path: str, select_prim: bool = True):
        """
        Constructor.
        
                Args:
                    usd_context (omni.usd.UsdContext): UsdContext this command to run on.
                    path_to (Sdf.Path): Path to create a new prim.
                    asset_path (str): The asset path of the audio file.
                    select_prim (bool, optional): If to select the newly created UsdPrim or not. Defaults to True.
                
        """
    def do(self):
        ...
class CreateDefaultXformOnPrimCommand(omni.kit.commands.command.Command):
    """
    Create default xformOp on prim.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: str, stage: pxr.Usd.Stage):
        """
        
                Constructor.
        
                Args:
                    prim_path (str): Path of the primitive to be create xform attribtues
                    stage (Usd.Stage): The USD stage to operate.
                
        """
    def _convert_default_euler_angle(self, rotation, default_euler, default_rotation_order):
        ...
    def _get_default_euler_angle(self, prim, stage, vector_type):
        """
        
                rotation specified as if applied in XYZ order
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateInstanceCommand(omni.kit.commands.command.Command):
    """
    Instance a primitive.
    
        It creates a new prim, adds the master object to references, and flags this prim as instanceable. It the prim is
        Xform, this command copies the transforms from the current frame. If the source prim is already instanceable, it
        tries to find master prim of this prim and uses it.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path_from: str):
        """
        Constructor.
        
                Args:
                    path_from (str): Path to instance from.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateInstancesCommand(omni.kit.commands.command.Command):
    """
    Instance multiple primitives.
    
        This command is a batch version of :class:`.CreateInstanceCommand`.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, paths_from: typing.List[str]):
        """
        Constructor.
        
                Args:
                    paths_from List[str]: Prim paths to instance from.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateMdlMaterialPrimCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    Create a MDL Material.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mtl_url: str, mtl_name: str, mtl_path: str, select_new_prim: bool = False, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None):
        """
        
                Constructor.
        
                Args:
                    mtl_url (str): MDL file path.
                    mtl_name (str): MDL material name.
                    mtl_path (str): Target prim path to create in the stage.
                    select_new_prim (bool, optional): If to select the new created material after creation. Default is False.
                    stage (Usd.Stage, optional): Stage to operate. Default is None, which means the stage in the default UsdContext is used.
                    context_name (str, optional): The usd context to operate. Default is None, which means the default UsdContext is used.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateMtlxMaterialPrimCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    Create a MaterialX material.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mtlx_url: str, base_path: str, select_new_prim: bool = False, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None):
        """
        
                Constructor.
        
                Args:
                    mtlx_url (str): Material file path.
                    base_path (str): Target prim path to create the material under.
                    select_new_prim (bool, optional): If to select new created prim. Default is False.
                    stage (Usd.Stage, optional): Stage to operate. Default is None, which means the stage in the default UsdContext is used.
                    context_name (str, optional): The usd context to operate. Default is None, which means the default UsdContext is used.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreatePayloadCommand(CreatePrimCommandBase):
    """
    Create a new prim with payload.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, usd_context: omni.usd._usd.UsdContext, path_to: pxr.Sdf.Path, asset_path: str = None, prim_path: pxr.Sdf.Path = None, instanceable: bool = True, select_prim: bool = True):
        """
        Constructor.
        
                Args:
                    usd_context (omni.usd.UsdContext): UsdContext this command to run on.
                    path_to (Sdf.Path): Path to create a new prim.
                    asset_path (str, optional): The asset path to payload. Defaults to None.
                    prim_path (Sdf.Path): The prim path to payload. Defaults to None.
                    instanceable (bool, optional): If to set the prim instanceable. It works together with `/persistent/app/stage/instanceableOnCreatingReference` setting.
                        Defaults to True.
                    select_prim (bool): If to select the created primitive.
                        Defaults to True.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreatePreviewSurfaceMaterialPrimCommand(omni.kit.commands.command.Command):
    """
    Create a USD Preview Surface Material.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mtl_path: str, shader_prim_name = 'Shader', select_new_prim: bool = False):
        """
        
                Constructor.
        
                Args:
                    mtl_path (str): The material path to create.
                    shader_prim_name (str, optional): The name of the root shader prim. Default is "Shader".
                    select_new_prim (bool, optional): If to select new created prim. Default is False.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreatePreviewSurfaceTextureMaterialPrimCommand(omni.kit.commands.command.Command):
    """
    Create a USD Preview Surface Texture Material.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, mtl_path: typing.Union[str, pxr.Sdf.Path], select_new_prim: bool = False):
        """
        
                Constructor.
        
                Args:
                    mtl_path (Union[str, Sdf.Path]): The material path to create.
                    select_new_prim (bool, optional): If to select new created prim. Default is False.
                
        """
    def _createAndConnectTexture(self, name, input_shader, input_port_name, output_port_name, params, primvar_reader_output_port):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class CreatePrimCommand(CreatePrimWithDefaultXformCommand):
    """
    
        Create a primitive to stage. It is the same as :class:`.CreatePrimWithDefaultXformCommand` and kept for backward compatibility.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_type: str, prim_path: str = None, select_new_prim: bool = True, attributes: typing.Dict[str, typing.Any] = {}, create_default_xform = True, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None):
        """
        
                Constructor.
        
                Args:
                    prim_type (str): Primitive type supported by USD, e.g. "Xform", "Camera", "Sphere", "Cube" etc.
                    prim_path (str, optional): Path of the primitive to be created at. If None is provided,
                        it will be placed at stage root or under default prim using Type name. Default is None.
                    select_new_prim (bool, optional) : Whether to select the prim after it's created. Default is True.
                    attributes (Dict[str, object], optional): Attributes dict to set after creation. Default is {}.
                    create_default_xform (bool, optional): Whether to create default xform operators. Default is True.
                    stage (Usd.Stage, optional): Stage to operate. Default is None, which means the stage in the default UsdContext is used.
                    context_name (str, optional): The usd context to operate. Default is None, which means the default UsdContext is used.
                        Param `stage`, to some extent, is duplicate to this param. They are both kept for back-compatibility.
                
        """
class CreatePrimCommandBase(omni.kit.commands.command.Command):
    """
    Base class to create a prim (and remove when undo).
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, usd_context: omni.usd._usd.UsdContext, path_to: pxr.Sdf.Path, asset_path: str, select_prim: bool = True):
        """
        Constructor.
        
                Args:
                    usd_context (omni.usd.UsdContext): UsdContext this command to run on.
                    path_to (Sdf.Path): Path to create a new prim.
                    asset_path (str): The asset it's necessary to add to references.
                    select_prim (bool, optional):If to select the newly created UsdPrim. Defaults to True.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreatePrimWithDefaultXformCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    Create a primitive to stage.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_type: str, prim_path: str = None, select_new_prim: bool = True, attributes: typing.Dict[str, typing.Any] = {}, create_default_xform = True, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None):
        """
        
                Constructor.
        
                Args:
                    prim_type (str): Primitive type supported by USD, e.g. "Xform", "Camera", "Sphere", "Cube" etc.
                    prim_path (str, optional): Path of the primitive to be created at. If None is provided,
                        it will be placed at stage root or under default prim using Type name. Default is None.
                    select_new_prim (bool, optional) : Whether to select the prim after it's created. Default is True.
                    attributes (Dict[str, object], optional): Attributes dict to set after creation. Default is {}.
                    create_default_xform (bool, optional): Whether to create default xform operators. Default is True.
                    stage (Usd.Stage, optional): Stage to operate. Default is None, which means the stage in the default UsdContext is used.
                    context_name (str, optional): The usd context to operate. Default is None, which means the default UsdContext is used.
                        Param `stage`, to some extent, is duplicate to this param. They are both kept for back-compatibility.
                
        """
    def _create_light_extra(self, prim, stage):
        ...
    def _set_refinement_level(self, prim, stage):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class CreatePrimsCommand(omni.kit.commands.command.Command):
    """
    
        Create multiple primitives.
    
        This command is a batch version of command :class:`.CreatePrimCommand`.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_types: typing.List[str], usd_context_name: typing.Optional[str] = None):
        """
        
                Constructor.
        
                Args:
                    prim_types (List[str]): List of primitive types to create, e.g ["Sphere", "Cone"].
                    usd_context_name (str, optional): The usd context to operate. Default is None, which means the default UsdContext.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateReferenceCommand(CreatePrimCommandBase):
    """
    Create a new prim with reference.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, usd_context: omni.usd._usd.UsdContext, path_to: pxr.Sdf.Path, asset_path: str = None, prim_path: pxr.Sdf.Path = None, instanceable: bool = True, select_prim: bool = True):
        """
        Constructor.
        
                Args:
                    usd_context (omni.usd.UsdContext): UsdContext this command to run on.
                    path_to (Sdf.Path): Path to create a new prim.
                    asset_path (str, optional): The asset path for reference. If not specified, it's a prim reference. Defaults to None.
                    prim_path (Sdf.Path): The prim path to reference. Defaults to None.
                    instanceable (bool, optional): If to set the prim instanceable. It works together with `/persistent/app/stage/instanceableOnCreatingReference` setting.
                        Defaults to True.
                    select_prim (bool): If to select the created primitive.
                        Defaults to True.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateShaderPrimFromSdrCommand(omni.kit.commands.command.Command):
    """
    
        Load the shader specified by 'identifier' from the SDR registry and create a shader prim under
        the specified parent. The parent must be of type UsdShade.Material or UsdShade.NodeGraph.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def _CreateShaderPrimFromSdrCommand__get_context_and_stage(self, stage_or_context):
        ...
    def __init__(self, parent_path: str, identifier: str, name: str = None, select_new_prim: bool = False, stage_or_context: typing.Union[str, pxr.Usd.Stage, omni.usd._usd.UsdContext] = None):
        """
        
                Constructor.
        
                Args:
                    parent_path (str): The path of the parent UsdShade.Material or UsdShade.NodeGraph
                    identifier (str): The identifer of the node Sdr registry which will be used to define the shader.
                    name (str, optional): The name of the UsdShade.Shader prim to be created. If it's None, identifier will be used. Default is None.
                    select_new_prim (bool, optional): If to select new created prim. Default is False.
                    stage_or_context: (Union[str, Usd.Stage, omni.usd.UsdContext]): Stage or UsdContext applies the changes to.
                        It can be instance of Usd.Stage or omni.usd.UsdContext, or context name. By default, it will apply
                        the changes to the stage in default UsdContext.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateUsdAttributeCommand(omni.kit.commands.command.Command):
    """
    Creates a USD Attribute for a primitive.
    
        Example of usage:
            omni.kit.commands.execute("CreateUsdAttribute",
                                       prim=prim,
                                       attr_name="custom",
                                       attr_type=Sdf.ValueTypeNames.Double3)
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def _CreateUsdAttributeCommand__get_prim(self):
        ...
    def __init__(self, prim: pxr.Usd.Prim, attr_name: str, attr_type: pxr.Sdf.ValueTypeName, custom: bool = True, variability: pxr.Sdf.Variability = ..., attr_value: typing.Any = None):
        """
        Constructor.
        
                Args:
                    prim (Usd.Prim): USD primitive to create the attribute.
                    attr_name (str): New attribute's name.
                    attr_type (Sdf.ValueTypeName): New attribute's type.
                    custom (bool, optional): If the attribute is custom. Default is True.
                    variability (Sdf.Variability, optional): whether the attribute may vary over time and value coordinates,
                        and if its value comes through authoring or from its owner. Default is Sdf.VariabilityVarying.
                    attr_value (Any, optional): New attribute's value. Leave it as None to use default value.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class CreateUsdAttributeOnPathCommand(omni.kit.commands.command.Command):
    """
    Creates a USD Attribute with attribute path.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, attr_path: typing.Union[pxr.Sdf.Path, str], attr_type: pxr.Sdf.ValueTypeName, custom: bool = True, variability: pxr.Sdf.Variability = ..., attr_value: typing.Any = None, usd_context_name: str = ''):
        """
        Constructor.
        
                Args:
                    attr_path (Union[Sdf.Path, str]): Path to the new attribute to be created. The prim of this path must already exist.
                    attr_type (Sdf.ValueTypeName): New attribute's type.
                    custom (bool, optional): If the attribute is custom. Default is True.
                    variability (Sdf.Variability, optional): whether the attribute may vary over time and value coordinates,
                        and if its value comes through authoring or from its owner. Default is Sdf.VariabilityVarying.
                    attr_value (Any, optional): New attribute's value. Leave it as None to use default value.
                    usd_context_name(str): Name of the usd context to execute the command on. Default is None, which uses the default UsdContext.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class DeletePrimsCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    Delete primitives from stage.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def _remove_prim_specs(*args, **kwargs):
        ...
    def __init__(self, paths: typing.List[typing.Union[str, pxr.Sdf.Path]], destructive = True, stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None):
        """
        
                Constructor.
        
                Args:
                    paths (List[str]): Paths to prims to delete.
        
                    destructive (bool, optional): If it's false, the delete will only happen in the current target, and follows:
                                    1. If the prim spec is a def, it will remove the prim spec.
                                    2. If the prim spec is a over, it will only deactivate this prim.
                                    3. If the prim spec is not existed, it will create over prim and deactivate it.
                                    4. If there is an overridden in a stronger layer, it will report errors.
        
                                    If it's true, it will remove all prim specs in all local layers.
        
                                    By default, it's True and means the delete operation is destructive for back-compatibility.
        
                    stage (Usd.Stage, optional): Stage to operate. Default is None, which means to use the stage in the default UsdContext.
                    context_name (str, optional): The usd context to operate. Default is None, which means to use the default UsdContext.
                
        """
    def _has_overridden_in_stronger_layer(self, stage, prim_path):
        ...
    def _has_prim_specs(self, stage, path):
        ...
    def _is_auto_authoring_layer(self, layer_identifier):
        ...
    def _remove_prim_spec_in_auto_authoring_layer(self, stage, path):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class FramePrimsCommand(omni.kit.commands.command.Command):
    """
    Transform camera to encompass the bounds of a list of paths.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def _FramePrimsCommand__calculate_distance(self, radius, prim) -> typing.Tuple[float, bool]:
        ...
    def _FramePrimsCommand__compute_local_transform(self, stage: pxr.Usd.Stage):
        ...
    def __init__(self, prim_to_move: typing.Union[str, pxr.Sdf.Path], prims_to_frame: typing.Optional[typing.Sequence[typing.Union[str, pxr.Sdf.Path]]] = None, time_code: pxr.Usd.TimeCode = ..., usd_context_name: str = '', aspect_ratio: float = 1, use_horizontal_fov: bool = None, zoom: float = 0.45, horizontal_fov: float = 0.20656116130367255):
        """
        
                Constructor.
        
                Args:
                    prim_to_move(Union[str, Sdf.Path]): Path to the camera primitive that is being moved.
                    prims_to_frame(Sequence[Union[str, Sdf.Path]], optional): Sequence of primitives to use to calculate the bounds to frame.
                        If it's None, it means to calculate bound box for the whole stage. Default is None.
                    time_code(Usd.TimeCode, optional): Timecode to set values at. Default is Usd.TimeCode.Default().
                    usd_context_name(str, optional): Name of the usd context to work on. Default is None, which means the default UsdContext is used.
                    aspect_ratio(float, optional): Width / Height of the final image. Default is 1.
                    use_horizontal_fov(bool, optional): Whether to use a camera's horizontal or vertical field of view for framing.
                    zoom(float, optional): Final zoom in or out of the framed box. Values above 0.5 move further away and below 0.5 go closer.
                        Default is 0.45.
                    horizontal_fov(float, optional): Default horizontal field-of-view to use for framing if one cannot be calculated.
                        Default is 0.20656116130367255.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class GroupPrimsCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    Group primitives to the same parent.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def _create_group_xform_impl(*args, **kwargs):
        ...
    def __init__(self, prim_paths: typing.List[typing.Union[str, pxr.Sdf.Path]], stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None, destructive = True):
        """
        
                Constructor.
        
                Args:
                    prim_paths (List[str]): Prim paths that will be grouped.
                    stage (Usd.Stage, optional): Stage to operate. Default is None, which means the stage in the default UsdContext is used.
                    context_name (str, optional): The usd context to operate. Default is None, which means the default UsdContext is used.
                        Param `stage`, to some extent, is duplicate to this param. They are both kept for back-compatibility.
                    destructive (bool, optional): If it's true, it will group all prims and remove original prims, which
                                        may edit other layers that are not edit target currently.
                                        If it's false, all changes will be made only to the current edit target without
                                        touching other layers. By default, it's true for back compatibility.
                
        """
    def _resolve_usd_references(self, is_undo = False):
        ...
    def _set_prim_pivot(self, prim, pivot):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class MovePrimCommand(omni.kit.commands.command.Command):
    """
    Moves a primitive to a new path.
    
        This command moves a primitive from a old path to a new path. It can be used to
        re-organize the stage hierarchy. It supports two kinds of move: destructive and non-destructive.
        Destructive move means it will move opinions of the prim to the new path in all layers from the local layer stack
        instead of touching the current edit target only. Non-destructive move means it will not touch other layers instead
        of the current edit target only by merging all opinions from all local layers and moving them to the new path. It
        deactivates the old path instead of removing it depending on the condition if it will break the principle of non-destrutive
        authoring. Due to historical reason, this command is built with destuctive move so destructive move is enabled by
        default. It's recommended to use non-destructive move to ensure the command only influences the current edit target.
        REMINDER: Moving primitive to change stage's hierarchy in USD is a heavy operation that may trigger big composition cost.
        
    """
    class RenameHandler:
        def __init__(self, old_path: pxr.Sdf.Path):
            """
            Cache all objects that reference the old_path, before any rename occurs
            """
        def apply_change(self, old_path: pxr.Sdf.Path, new_path: pxr.Sdf.Path):
            ...
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def _move(*args, **kwargs):
        ...
    @staticmethod
    def _move_prim_spec(*args, **kwargs):
        ...
    def __init__(self, path_from: typing.Union[str, pxr.Sdf.Path], path_to: typing.Union[str, pxr.Sdf.Path], time_code: pxr.Usd.TimeCode = ..., keep_world_transform: bool = True, on_move_fn: typing.Callable[[pxr.Sdf.Path, pxr.Sdf.Path], NoneType] = None, destructive = True, stage_or_context: typing.Union[str, pxr.Usd.Stage, omni.usd._usd.UsdContext] = None, resolve_reference: bool = True):
        """
        
                Constructor.
        
                Args:
                    path_from (str): Path to move prim from.
                    path_to(str): Path to move prim to.
                    time_code(Usd.TimeCode, optional): Current timecode of the stage. Default is Usd.TimeCode.Default().
                    keep_world_transform(bool, optional): True to keep world transform after prim path is moved.
                        False to keep local transfrom only. Default is True.
                    on_move_fn(Callable[[Sdf.Path, Sdf.Path], None], optional): Function to call when prim is renamed, that
                        the first param is the source path, and second one is the target path. Default is None.
                    destructive(bool, optional): If it's false, it will not remove original prim but deactivate it. Default is True
                        for back compatibility.
                    stage_or_context: (Union[str, Usd.Stage, omni.usd.UsdContext]): Stage or UsdContext applies the changes to.
                        It can be instance of Usd.Stage or omni.usd.UsdContext, or context name. By default, it will apply
                        the changes to the stage in default UsdContext.
                    resolve_reference (bool, optional): If to resolve primitive's references after prim is moved to new path.
                
        """
    def _is_auto_authoring_layer(self, layer_identifier):
        ...
    def _remove_prim_spec_in_auto_authoring_layer(self, stage, path):
        ...
    def do(self):
        ...
    def modify_callback_info(self, cb_type: str, cmd_args: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        ...
    def undo(self):
        ...
class MovePrimsCommand(omni.kit.commands.command.Command):
    """
    
        Move a list of primitives to new locations.
    
        This command is a batch version of command :class:`.MovePrimCommand`
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, paths_to_move: typing.Dict[str, str], time_code: pxr.Usd.TimeCode = ..., keep_world_transform: bool = True, on_move_fn: typing.Callable = None, destructive = True, stage_or_context: typing.Union[str, pxr.Usd.Stage, omni.usd._usd.UsdContext] = None):
        """
        
                Constructor.
        
                Args:
                    paths_to_move(Dict[str, str]): The dictionary contains entry of {path_from : path_to}.
                    time_code(Usd.TimeCode, optional): Current timecode of the stage. Default is Usd.TimeCode.Default().
                    keep_world_transform(bool, optional): True to keep world transform after prim path is moved.
                        False to keep local transfrom only. Default is True.
                    on_move_fn(Callable, optional): Function to call when prim is renamed. Default is None.
                    destructive(bool, optional): If it's false, it will not remove original prim but deactivate it. Default is True
                        for back compatibility.
                    stage_or_context: (Union[str, Usd.Stage, omni.usd.UsdContext]): Stage or UsdContext applies the changes to.
                        It can be instance of Usd.Stage or omni.usd.UsdContext, or context name. By default, it will apply
                        the changes to the stage in default UsdContext.
                
        """
    def _add_resolve_path(self, layer_identifiers, path_from: typing.Union[pxr.Sdf.Path, str], path_to: typing.Union[pxr.Sdf.Path, str]):
        ...
    def _resolve_usd_references(self, is_undo = False):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class ParentPrimsCommand(omni.kit.commands.command.Command):
    """
    Moves prims into children of "parent" primitives.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, parent_path: str, child_paths: typing.List[str], on_move_fn: callable = None, keep_world_transform: bool = True, stage_or_context: typing.Union[str, pxr.Usd.Stage, omni.usd._usd.UsdContext] = None):
        """
        Constructor.
        
                Args:
                    parent_path (str): prim path to become parent of child_paths
                    child_paths (List[str]): prim paths to become children of parent_prim
                    on_move_fn(Callable[[Sdf.Path, Sdf.Path], None], optional): Function to call when prim is re-parented, that
                        the first param is the source path, and second one is the target path. Defaults to None.
                    keep_world_transform (bool, optional): If it needs to keep the world transform after parenting. Defaults to True
                    stage_or_context (Union[str, Usd.Stage, omni.usd.UsdContext], optional): Stage or UsdContext applies the changes to.
                        It can be instance of Usd.Stage or omni.usd.UsdContext, or context name. By default, it will apply
                        the changes to the stage in default UsdContext.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class PayloadCommandBase(omni.kit.commands.command.Command):
    """
    Base class for payload related commands.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'do'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage, prim_path: pxr.Sdf.Path, payload: pxr.Sdf.Payload):
        ...
    def _get_payloads(self):
        ...
    def _reserve_payloads(self):
        ...
    def undo(self):
        ...
class ReferenceCommandBase(omni.kit.commands.command.Command):
    """
    Base class for reference related commands.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'do'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage, prim_path: pxr.Sdf.Path, reference: pxr.Sdf.Reference):
        ...
    def _get_references(self):
        ...
    def _reserve_references(self):
        ...
    def undo(self):
        ...
class RelationshipTargetBase(omni.kit.commands.command.Command):
    """
    Base class of relationship related commands.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'do'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, relationship: pxr.Usd.Relationship, target: pxr.Sdf.Path):
        ...
    def _get_relationship(self):
        ...
    def undo(self):
        ...
class RemovePayloadCommand(PayloadCommandBase):
    """
    Remove specified payload from primitive.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage, prim_path: pxr.Sdf.Path, payload: pxr.Sdf.Payload):
        """
        Constructor.
        
                Args:
                    stage (Usd.Stage): The stage to operate.
                    prim_path (Sdf.Path): The prim path to remove the payload.
                    payload (Sdf.Payload): The specified payload to be removed.
                
        """
    def do(self):
        ...
class RemovePropertyCommand(omni.kit.commands.command.Command):
    """
    Remove property.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prop_path: typing.Union[pxr.Sdf.Path, str], usd_context_name: typing.Union[str, pxr.Usd.Stage] = '', remove_from_layers: typing.Union[typing.List[typing.Union[str, pxr.Sdf.Layer]], str, pxr.Sdf.Layer, NoneType] = None):
        """
        
                Constructor.
        
                Args:
                    prop_path (str): Path of the property to be removed.
                    usd_context_name (str, optional): Usd context name to run the command on. Default is None, which means the default UsdContext is used.
                    remove_from_layers (Optional[Union[List[Union[str, Sdf.Layer]], str, Sdf.Layer]]): A list of layers to remove the
                        property from. Default to None, which removes the property from all layers. Default is None.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class RemoveReferenceCommand(ReferenceCommandBase):
    """
    Remove specified reference from primitive.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, reference: pxr.Sdf.Reference):
        """
        Constructor.
        
                Args:
                    stage (Usd.Stage): The stage to operate.
                    prim_path (Sdf.Path): The prim path to remove the reference.
                    reference (Sdf.Reference): The specified reference to be removed.
                
        """
    def do(self):
        ...
class RemoveRelationshipTargetCommand(RelationshipTargetBase):
    """
    Remove target from a relationship.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, relationship: pxr.Usd.Relationship, target: pxr.Sdf.Path):
        """
        Constructor.
        
                Args:
                    relationship (Usd.Relationship): Relationship handle.
                    target (Sdf.Path): Target path to remove from relationship list.
                
        """
    def do(self):
        ...
class RenamePrimCommand(omni.kit.commands.command.Command):
    """
    
        Rename a primitive undoable **Command**.
    
        Args:
            prim_path (str): path of prim to be renamed.
            new_name (str): new name.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: str, new_name: str):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class ReplacePayloadCommand(PayloadCommandBase):
    """
    Replace the specified reference with a new one.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage, prim_path: pxr.Sdf.Path, old_payload: pxr.Sdf.Payload, new_payload: pxr.Sdf.Payload):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): The stage to operate.
                    prim_path (Sdf.Path): The prim path to replace payload.
                    old_payload (Sdf.Payload): The payload to be replaced.
                    new_payload (Sdf.Payload): The new payload handle.
                
        """
    def do(self):
        ...
class ReplaceReferenceCommand(ReferenceCommandBase):
    """
    Replace the specified reference with a new one.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, old_reference: pxr.Sdf.Reference, new_reference: pxr.Sdf.Reference):
        """
        
                Constructor.
        
                Args:
                    stage (Usd.Stage): The stage to operate.
                    prim_path (Sdf.Path): The prim path to replace reference.
                    old_reference (Sdf.Reference): The reference handle to be replaced.
                    new_reference (Sdf.Reference): The new reference handle.
                
        """
    def do(self):
        ...
class ReplaceReferencesCommand(omni.kit.commands.command.Command):
    """
    Deprecated. Clears/Adds references.
    
        NOTE: THIS COMMAND HAS A LOT OF ISSUES AND IS DEPRECATED. PLEASE USE ReplaceReferenceCommand instead!
    
        Args:
            path (str): Prim path.
            old_url(str): Url to be replaced.
            new_url(str): Replacement url.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str, old_url: str, new_url: str):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SelectPrimsCommand(omni.kit.commands.command.Command):
    """
    Select primitives.
    
        See :mod:`omni.kit.selection` for more details about selection.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, old_selected_paths: typing.List[str], new_selected_paths: typing.List[str], expand_in_stage: bool = True, source: omni.usd._usd.Selection.SourceType = ...):
        """
        
                Constructor.
        
                Args:
                    old_selected_paths (List[str]): Old selected prim paths.
                    new_selected_paths (List[str]): Prim paths to be selected.
                    expand_in_stage (bool, DEPRECATED): Whether to expand the path in Stage Window on selection.
                        This param is left for back compatibility.
                    source (omni.usd.Selection.SourceType, optional): USD/FABRIC/ALL, indicates which stage selection should be set to
                        Default is omni.usd.Selection.SourceType.USD.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class SetMaterialStrengthCommand(omni.kit.commands.command.Command):
    """
    Set material binding strength.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, rel, strength):
        """
        
                Constructor.
        
                Args:
                    rel: Material binding relationship.
                    strength (float): Strength.
                
        """
    def _set_strength(self, rel, strength):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SetPayLoadLoadSelectedPrimsCommand(omni.kit.commands.command.Command):
    """
    Set the loaded/unloaded payloads of the selected primitives.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, selected_paths: typing.List[str], value: bool, stage_or_context: typing.Union[str, pxr.Usd.Stage, omni.usd._usd.UsdContext] = None):
        """
        Constructor.
        
                Args:
                    selected_paths (List[str]): Old selected prim paths.
                    value (bool): True for load, and False for unload.
                    stage_or_context (Union[str, Usd.Stage, omni.usd.UsdContext], optional): Stage or UsdContext applies the changes to.
                        It can be instance of Usd.Stage or omni.usd.UsdContext, or context name. By default, it will apply
                        the changes to the stage in default UsdContext.
                
        """
    def _set_load(self):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SetRelationshipTargetsCommand(RelationshipTargetBase):
    """
    Set target(s) to a relationship.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, relationship: pxr.Usd.Relationship, targets: typing.List[pxr.Sdf.Path]):
        """
        
                Constructor.
        
                Args:
                    relationship (Usd.Relationship): Relationship handle.
                    targets (List[Sdf.Path]): A list of target paths to set for the relationship.
                
        """
    def do(self):
        ...
class ToggleActivePrimsCommand(omni.kit.commands.command.Command):
    """
    Toggle the active state of prims.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_paths: typing.List[pxr.Sdf.Path], stage_or_context: typing.Union[pxr.Usd.Stage, str, omni.usd._usd.UsdContext] = None, active: typing.Optional[bool] = None):
        """
        
                Constructor.
        
                Args:
                    prim_paths (List[Sdf.Path]): A list of prim paths.
                    stage_or_context (Union[str, Usd.Stage, omni.usd.UsdContext], optional): Stage or UsdContext applies the changes to.
                        It can be instance of Usd.Stage or omni.usd.UsdContext, or context name. By default, it will apply
                        the changes to the stage in default UsdContext.
                    active (Union[bool, None], optional): If active flag is not None, it will set the active states to the value specified
                        by it. Otherwise, it will revert the active states of prims. Defaults to None.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class TogglePayLoadLoadSelectedPrimsCommand(omni.kit.commands.command.Command):
    """
    Toggles the loaded/unloaded payloads of the selected primitives.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, selected_paths: typing.List[str], stage_or_context: typing.Union[str, pxr.Usd.Stage, omni.usd._usd.UsdContext] = None):
        """
        Constructor.
        
                Args:
                    selected_paths (List[str]): Old selected prim paths.
                    stage_or_context (Union[str, Usd.Stage, omni.usd.UsdContext], optional): Stage or UsdContext applies the changes to.
                        It can be instance of Usd.Stage or omni.usd.UsdContext, or context name. By default, it will apply
                        the changes to the stage in default UsdContext.
                
        """
    def _toggle_load(self):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class ToggleVisibilitySelectedPrimsCommand(omni.kit.commands.command.Command):
    """
    Toggles the visiblity of the selected primitives.
    
        This command will invert the visibilities for the specified list of primitives. Therefore,
        those visible primitives will be invisible after this command, and vice versa for
        invisible primitives.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, selected_paths: typing.List[str], stage: typing.Optional[pxr.Usd.Stage] = None, visible: typing.Optional[bool] = None):
        """
        
                Constructor.
        
                Args:
                    selected_paths (List[str]): A list of prim paths to toggle visibility.
                    stage (Usd.Stage, optional): The stage to operate. Default is None,
                        which means the stage in the default UsdContext is used.
                    visible (Optional[bool]): By default, it's None that means to invert the visibility state for each prim.
                        When it's set as a bool value, it will set all visibilities to the specified value instead of inverting them.
                
        """
    def _get_prim_visibility(self, prim, time):
        ...
    def _toggle_visibility(self):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class TransformPrimCommand(omni.kit.commands.command.Command):
    """
    Set primitive's local transform.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str, new_transform_matrix: pxr.Gf.Matrix4d, old_transform_matrix: pxr.Gf.Matrix4d = None, time_code: pxr.Usd.TimeCode = ..., had_transform_at_key: bool = False, usd_context_name: str = ''):
        """
        
                Constructor.
        
                Args:
                    path (str): Prim path.
                    new_transform_matrix (Gf.Matrix4d): New local transform matrix.
                    old_transform_matrix (Gf.Matrix4d, optional): Old local transform matrix that is used for undo. If it's not given,
                        it's the current local transform matrix when this command is instantiated. Default is None.
                    time_code (Usd.TimeCode): The timecode to change. Default is Usd.TimeCode.Default().
                    had_transform_at_key (bool): If the local transform is set already before this command. This is used for undo to
                        decide if it needs to clear the new value. Default is False.
                    usd_context_name (str): The UsdContext to operate. Default is empty, which means the default UsdContext is used.
                
        """
    def _clear_transform_at_time(self, time_code: pxr.Usd.TimeCode):
        ...
    def _has_time_sample(self, xform_op, time_code):
        ...
    def _set_transform_matrix(self, matrix, time_code: pxr.Usd.TimeCode = ..., skip_equal_set_for_timesample: bool = False):
        ...
    def _set_value_with_precision(self, xform_op, value, time_code: pxr.Usd.TimeCode = ..., skip_equal_set_for_timesample: bool = False):
        ...
    def _stage(self):
        ...
    def _switch_edit_tgt(self):
        ...
    def _xform_is_time_sampled(self, xform: pxr.UsdGeom.Xformable):
        ...
    def _xform_op_is_time_sampled(self, xform_op: pxr.UsdGeom.XformOp):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class TransformPrimSRTCommand(omni.kit.commands.command.Command):
    """
    Set primitive's local transform with scale, rotation and transform values.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def _set_transform_srt(*args, **kwds):
        ...
    @staticmethod
    def _set_value_with_precision(*args, **kwds):
        ...
    def __init__(self, path: str, new_translation: pxr.Gf.Vec3d = None, new_rotation_euler: pxr.Gf.Vec3d = None, new_scale: pxr.Gf.Vec3d = None, new_rotation_order: pxr.Gf.Vec3i = None, old_translation: pxr.Gf.Vec3d = None, old_rotation_euler: pxr.Gf.Vec3d = None, old_rotation_order: pxr.Gf.Vec3i = None, old_scale: pxr.Gf.Vec3d = None, time_code: pxr.Usd.TimeCode = ..., had_transform_at_key: bool = False, usd_context_name: str = ''):
        """
        
                Constructor.
        
                Args:
                    path (str): Prim path.
                    new_translation (Gf.Vec3d, optional): New local translation. Leave to None to use current value.
                        Default is None.
                    new_rotation_euler (Gf.Vec3d, optional): New local rotation euler angles (in degree).
                        Leave to None to use current value. Default is None.
                    new_scale (Gf.Vec3d, optional): New scale. Leave to None to use current value. Default is None
                    new_rotation_order (Gf.Vec3i, optional): New rotation order (e.g. (0, 1, 2) means XYZ).
                        Leave to None to use current value. Default is None.
                    old_translation (Gf.Vec3d, optional): Old local translation for undo. Leave to None to use current value.
                        Default is None.
                    old_rotation_euler (Gf.Vec3d, optional): Old local rotation euler angles for undo. Leave to None to use current value.
                        Default is None.
                    old_rotation_order (Gf.Vec3i, optional): Old local rotation order for undo. Leave to None to use current value.
                        Default is None.
                    old_scale (Gf.Vec3d, optional): Old scale for undo. Leave to None to use current value. Default is None.
                    time_code (Usd.TimeCode, optional): TimeCode to set transform to. Default is Usd.TimeCode.Default().
                    had_transform_at_key (bool): If the local transform is set already before this command. This is used for undo to
                        decide if it needs to clear the new value. Default is False.
                    usd_context_name (str): The UsdContext to operate. Default is empty, which means the default UsdContext is used.
                
        """
    def _clear_transform_at_time(self, time_code: pxr.Usd.TimeCode):
        ...
    def _construct_transfrom_matrix_from_SRT(self, translation: pxr.Gf.Vec3d, rotation_euler: pxr.Gf.Vec3d, rotation_order: pxr.Gf.Vec3i, scale: pxr.Gf.Vec3d):
        ...
    def _has_time_sample(self, xform_op, time_code):
        ...
    def _switch_edit_tgt(self):
        ...
    def _xform_is_time_sampled(self, xform: pxr.UsdGeom.Xformable):
        ...
    def _xform_op_is_time_sampled(self, xform_op: pxr.UsdGeom.XformOp):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class TransformPrimsCommand(omni.kit.commands.command.Command):
    """
    Set local transforms for multiple primitives.
    
        This command is a batch version of :class:`.TransformPrimCommand`
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prims_to_transform: typing.List[typing.Tuple[str, pxr.Gf.Matrix4d, pxr.Gf.Matrix4d, pxr.Usd.TimeCode]]):
        """
        
                Constructor.
        
                Args:
                    prims_to_transform (ListList[Tuple[str, Gf.Matrix4d, Gf.Matrix4d, Usd.TimeCode]]): List of primitives to transform
                        in a tuple of (path, new_transform, old_transform).
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class TransformPrimsSRTCommand(omni.kit.commands.command.Command):
    """
    Set local transforms of multiple primitives with scale, rotation and transform values.
    
        This command is a batch version of :class:`.TransformPrimSRTCommand`
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prims_to_transform: typing.List[typing.Tuple[str, pxr.Gf.Vec3d, pxr.Gf.Vec3d, pxr.Gf.Vec3i, pxr.Gf.Vec3d, pxr.Gf.Vec3d, pxr.Gf.Vec3d, pxr.Gf.Vec3i, pxr.Gf.Vec3d, pxr.Usd.TimeCode, bool]]):
        """
        
                Constructor.
        
                Args:
                    prims_to_transform: List of primitive to transform in a tuple of
                                        (path,
                                        new_translation,
                                        new_rotation_euler,
                                        new_rotation_order,
                                        new_scale,
                                        old_translation,
                                        old_rotation_euler,
                                        old_rotation_order,
                                        old_scale,
                                        time_code,
                                        had_transform_at_key).
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class UngroupPrimsCommand(omni.kit.commands.command.Command, omni.usd.commands.stage_helper.UsdStageHelper):
    """
    Ungroup primitives from the parent.
    """
    class ExitCode(enum.Enum):
        """
        An enumeration.
        """
        NoParent: typing.ClassVar[UngroupPrimsCommand.ExitCode]  # value = <ExitCode.NoParent: 2>
        Success: typing.ClassVar[UngroupPrimsCommand.ExitCode]  # value = <ExitCode.Success: 1>
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_paths: typing.List[typing.Union[str, pxr.Sdf.Path]], stage: typing.Optional[pxr.Usd.Stage] = None, context_name: typing.Optional[str] = None, destructive = True):
        """
        
                Constructor.
        
                Args:
                    prim_paths (List[str]): Prim paths that will be grouped.
                    stage (Usd.Stage, optional): Stage to operate. Default is None, which means the stage in the default UsdContext is used.
                    context_name (str, optional): The usd context to operate. Default is None, which means the default UsdContext is used.
                        Param `stage`, to some extent, is duplicate to this param. They are both kept for back-compatibility.
                    destructive (bool, optional): If it's true, it will group all prims and remove original prims, which
                                        may edit other layers that are not edit target currently.
                                        If it's false, all changes will be made only to the current edit target without
                                        touching other layers. By default, it's true for back compatibility.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class UnhideAllPrimsCommand(omni.kit.commands.command.Command):
    """
    Unhide all primitives in the default UsdContext.
    
        This command will traverse the whole stage and unhides all primitives that are marked
        as invisible.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def do(self):
        ...
    def undo(self):
        ...
class UnparentPrimsCommand(omni.kit.commands.command.Command):
    """
    Moves prims into root "/" primitive.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, paths: typing.List[str], on_move_fn: callable = None, keep_world_transform: bool = True, stage_or_context: typing.Union[str, pxr.Usd.Stage, omni.usd._usd.UsdContext] = None):
        """
        
        
                Args:
                    paths: prim path to become parent of child_paths
                    on_move_fn(Callable[[Sdf.Path, Sdf.Path], None], optional): Function to call when prim is re-parented, that
                        the first param is the source path, and second one is the target path. Defaults to None.
                    keep_world_transform (bool, optional): If it needs to keep the world transform after parenting. Defaults to True
                    stage_or_context (Union[str, Usd.Stage, omni.usd.UsdContext], optional): Stage or UsdContext applies the changes to.
                        It can be instance of Usd.Stage or omni.usd.UsdContext, or context name. By default, it will apply
                        the changes to the stage in default UsdContext.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
def active_edit_context(usd_context_or_stage):
    """
    Internal. Utility to return active edit context.
        By default, it will return the current edit target. When it's in auto-authoring mode,
        it will return the edit context of the default layer. You can refer to :mod:`omni.kit.usd.layers`
        for more details about auto-authoring.
        
    """
def allow_prim_parenting(stage: pxr.Usd.Stage, path_from: str, path_to: str, action: str):
    """
    Internal. Checkes if parenting a prim to a target location is allowed.
    """
def ensure_parents_are_active(stage, path):
    """
    
        Internal. It will ensure parents are active. If they are not, it will change the active
        flag into active, and all of their children will be marked to inacitve.
        This is normally used when it's to create materials under /World/Looks, as it's
        possible /World/Looks is deactivated. While creating a prim under an inactive parent
        will throw exceptions by USD.
        
    """
def get_child_position_in_the_parent(stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path):
    """
    Internal. Gets the index of the prim inside its parent.
    """
def get_context_and_stage(stage_or_context: typing.Union[str, pxr.Usd.Stage, omni.usd._usd.UsdContext]):
    """
    Internal. Returns instances of UsdContext and UsdStage based on the union argument.
    """
def get_default_camera_rotation_order_str():
    """
    Internal. Gets default camera rotation order from setting /persistent/app/primCreation/DefaultCameraRotationOrder. 
    """
def get_default_rotation_order_str():
    """
    Internal. Gets default rotation order from setting /persistent/app/primCreation/DefaultRotationOrder. 
    """
def get_default_rotation_order_type(is_camera: bool = False):
    """
    Internal. Gets default rotation order.
    """
def move_prim_to_location(stage: pxr.Usd.Stage, prim_path: pxr.Sdf.Path, location: int, old_name: str = None):
    """
    Internal. Moves prim to specific location of its parent.
    """
def post_notification(message: str, info: bool = False, duration: int = 3):
    """
    Internal. Posts notification if omni.kit.notification_manager is enabled.
    """
def prim_can_be_removed_without_destruction(usd_context_or_stage, prim_path):
    """
    
        Internal. A destructive remove is one that will not only edit current edit target,     but also other non-anonymous layers. Why anonymous layers is not counted is because     anonymous layers are writable in Kit, and it's only existed when it's a new     stage or under session layer. Any deltas inside those anonymous layers can be safely     removed. Otherwise, this function will return false, which means it will not remove     prim specs in all layers, but deactivates them to avoid editing non-anonymous layers except     current edit target.
        
    """
def remove_prim_spec(layer: pxr.Sdf.Layer, prim_spec_path: str):
    """
    Internal. Removes prim spec from layer.
    """
def should_keep_children_order():
    """
    Internal. Whether it should keep children order after prim is renamed or removed.
    """
def write_refinement_override_enabled_hint(stage):
    """
    Internal. If the user authors refinementEnableOverride, drop a hint in customLayerData
        that we can use to enable/disable the checking for override attributes
        in the scene delegate (i.e., assuaging Pixar's concern that even assets
        that do not opt into per-mesh refinement must check for their presence at load
        time).
    
        The hint also gives us a numerical value that we can use to maintain
        backwards compatibility, as it is almost certain that the attributes and
        the value resolution logic governing this override behavior will be revisted,
        i.e., also encodable in a more high-level enum like Complexity setting in
        usdview, which could also be an attribute than lives on any prim, not just
        meshes, and whose behavior would inherit down namespace.
        
    """
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
SETTING_NESTED_GPRIMS_AUTHORING: str = '/persistent/app/stage/nestedGprimsAuthoring'
