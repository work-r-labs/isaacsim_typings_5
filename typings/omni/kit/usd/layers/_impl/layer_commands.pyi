from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.usd.layers._impl.extension import get_layers
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import get_all_locked_specs
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import get_all_spec_links
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import get_spec_layer_links
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import get_spec_links_for_layers
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import is_spec_linked
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import is_spec_locked
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import link_specs
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import lock_specs
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import unlink_all_specs
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import unlink_specs
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import unlink_specs_from_all_layers
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import unlink_specs_to_layers
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import unlock_all_specs
from omni.kit.usd.layers._impl.specs_linking_and_locking_utils import unlock_specs
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdUtils
import typing
__all__: list = ['AbstractLayerCommand', 'SetEditTargetCommand', 'CreateSublayerCommand', 'RemoveSublayerCommand', 'RemovePrimSpecCommand', 'MergeLayersCommand', 'FlattenLayersCommand', 'CreateLayerReferenceCommand', 'StitchPrimSpecsToLayer', 'MovePrimSpecsToLayerCommand', 'MoveSublayerCommand', 'ReplaceSublayerCommand', 'SetLayerMutenessCommand', 'LockLayerCommand', 'LinkSpecsCommand', 'UnlinkSpecsCommand', 'LockSpecsCommand', 'UnlockSpecsCommand']
class AbstractLayerCommand(omni.kit.commands.command.Command):
    """
    
        Abstract base class for layer commands.
        It's mainly responsible to create a commmon class
        to save all states before command execution, and restore them
        in the undo function.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, context_name_or_instance: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        ...
    def _restore_spec_links_from_dict(self, spec_path_to_layers):
        ...
    def do(self):
        ...
    def do_impl(self):
        """
        Abstract do function to be implemented.
        """
    def get_layers(self):
        ...
    def get_specs_linking(self):
        ...
    def get_specs_locking(self):
        ...
    def undo(self):
        ...
    def undo_impl(self):
        """
        Abstract undo function to be implemented.
        """
class CreateLayerReferenceCommand(AbstractLayerCommand):
    """
    
        Create reference in specific layer.
    
        It creates a new prim and adds the asset and path as references in specific layer.
    
        Args:
            layer_identifier: str: Layer identifier to create prim inside.
    
            path_to (Sdf.Path): Path to create a new prim.
    
            asset_path (str): The asset it's necessary to add to references.
    
            prim_path (Sdf.Path): The prim in asset to reference.
    
            usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer_identifier: str, path_to: pxr.Sdf.Path, asset_path: str = None, prim_path: pxr.Sdf.Path = None, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        ...
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class CreateSublayerCommand(AbstractLayerCommand):
    """
    Creates or inserts a sublayer.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer_identifier: str, sublayer_position: int, new_layer_path: str, transfer_root_content: bool, create_or_insert: bool, layer_name: str = '', usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword arguments::
                    layer_identifier  (str): The identifier of layer to create sublayer. It should be found by Sdf.Find.
        
                    sublayer_position (int): Sublayer position that the new sublayer is created before.
                                             If position_before == -1, it will create layer at the end of sublayer list.
                                             If position_before >= total_number_of_sublayers, it will create layer at the end of sublayer list.
                    new_layer_path (str): Absolute path of new layer. If it's empty, it will create anonymous layer if create_or_insert == True.
                                         If create_or_insert == False and it's empty, it will fail to insert layer.
        
                    transfer_root_content (bool): True if we should move the root contents to the new layer.
        
                    create_or_insert (bool): If it's true, it will create layer from this path. It's insert, otherwise.
        
                    layer_name (str, optional): If it's to create anonymous layer (new_layer_path is empty), this name is used.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class FlattenLayersCommand(AbstractLayerCommand):
    """
    Flatten Layers.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def _get_sublayers_from_strongest_to_weakest(self):
        ...
    def _traverse(self, results, parent_layer_identifier, layer, layer_identifier, current_subtree_stack):
        ...
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class LinkSpecsCommand(AbstractLayerCommand):
    """
    Links spec paths to layers.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, spec_paths: typing.Union[str, typing.List[str]], layer_identifiers: typing.Union[str, typing.List[str]], additive: bool = True, hierarchy: bool = False, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    spec_paths (Union[str, List[str]]): List of spec paths or single spec path to be linked.
        
                    layer_identifiers (Union[str, List[str]]): List of layer identifiers or single layer identifier.
        
                    additive (bool): Clearing exsiting links or not.
        
                    hierarchy (bool): Linking descendant specs or not.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class LockLayerCommand(AbstractLayerCommand):
    """
    Sets lock state for layer.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer_identifier: str, locked: bool, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor. REMINDER: Locking root layer is not permitted.
        
                Keyword Arguments:
                    layer_identifier (str): The identifier of layer to be muted/unmuted.
        
                    locked (bool): Muted or not of this layer.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class LockSpecsCommand(AbstractLayerCommand):
    """
    Locks spec paths in the UsdContext.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, spec_paths: typing.Union[str, typing.List[str]], hierarchy = False, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    spec_paths (Union[str, List[str]]): List of spec paths or single spec path to be locked.
        
                    hierarchy (bool): Locking descendant specs or not.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class MergeLayersCommand(AbstractLayerCommand):
    """
    Merges two layers.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, dst_parent_layer_identifier: str, dst_layer_identifier, src_parent_layer_identifier: str, src_layer_identifier: str, dst_stronger_than_src: bool, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = '', src_layer_offset: pxr.Sdf.LayerOffset = ...):
        """
        Constructor.
        
                Keyword Arguments:
                    dst_parent_layer_identifier: The parent of target layer.
        
                    dst_layer_identifier: The target layer that source layer is merged to.
        
                    src_parent_layer_identifier: The parent of source layer.
        
                    src_layer_identifier: The source layer.
        
                    dst_stronger_than_src (bool): If target layer is stronger than source, which will decide
                                                  how to merge opinions that appear in both layers.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
        
                    src_layer_offset (Sdf.LayerOffset): The source layer offset to target layer. By default, it's identity.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class MovePrimSpecsToLayerCommand(AbstractLayerCommand):
    """
    Merge prim spec from src layer to dst layer and remove it from src layer.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, dst_layer_identifier: str, src_layer_identifier: str, prim_spec_path: str, dst_stronger_than_src: bool, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    dst_layer_identifier (str): The identifier of target layer.
        
                    src_layer_identifier (str): The identifier of source layer.
        
                    prim_spec_path (str): The prim spec path to be merged.
        
                    dst_stronger_than_src (bool): Target layer is stronger than source layer in stage.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class MoveSublayerCommand(AbstractLayerCommand):
    """
    Moves sublayer from one location to the other.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, from_parent_layer_identifier: str, from_sublayer_position: int, to_parent_layer_identifier: str, to_sublayer_position: int, remove_source: bool = False, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    from_parent_layer_identifier (str): The identifier of source parent layer.
        
                    from_sublayer_position (int): The sublayer position in source parent layer to move.
        
                    to_parent_layer_identifier (str): The identifier of target parent layer.
        
                    to_sublayer_position (int): The sublayer position in target parent layer that layers moves to.
                                                If this position is -1, it means the last position of sublayer array.
                                                If this position is beyond the end of sublayer array. It means to
                                                move this layer to the end of that array.
                                                Otherwise, it's invalid if it's below 0.
        
                    remove_source (bool): Remove source sublayer after moving to target or not.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def _move_layer(self, from_parent_layer_identifier, sublayer_identifier, to_parent_layer_identifier, to_sublayer_position, remove_source):
        ...
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class RemovePrimSpecCommand(omni.kit.commands.command.Command):
    """
    Removes prim spec from a layer.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer_identifier: str, prim_spec_path: typing.Union[pxr.Sdf.Path, typing.List[pxr.Sdf.Path]], usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    layer_identifier (str): The identifier of layer to remove prim.
        
                    prim_spec_path (Union[Sdf.Path, List[Sdf.Path]]): The prim paths to be removed.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class RemoveSublayerCommand(AbstractLayerCommand):
    """
    Removes a sublayer from parent layer.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer_identifier: str, sublayer_position: int, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    layer_identifier (str): The identifier of layer to remove sublayer.
        
                    sublayer_position (int): The sublayer position to be removed.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class ReplaceSublayerCommand(AbstractLayerCommand):
    """
    Replaces sublayer with a new layer.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer_identifier: str, sublayer_position: int, new_layer_path: str, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    layer_identifier (str): The identifier of layer to replace sublayer.
        
                    sublayer_position (int): The sublayer position to be replaced.
        
                    new_layer_path (str): The path of new layer.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class SetEditTargetCommand(AbstractLayerCommand):
    """
    Sets layer as Edit Target.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer_identifier: str, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    layer_identifier (str): Layer identifier.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class SetLayerMutenessCommand(AbstractLayerCommand):
    """
    Sets mute state for layer.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, layer_identifier: str, muted: bool, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    layer_identifier (str): The identifier of layer to be muted/unmuted.
        
                    muted (bool): Muted or not of this layer.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class StitchPrimSpecsToLayer(AbstractLayerCommand):
    """
    Flatten specific prims in the stage. It will remove original prim specs after flatten.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_paths: typing.List[str], target_layer_identifier: str, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    prim_paths (List[str]): A list of prim_paths to flatten with.
        
                    target_layer_identifier (str): The target layer to store the flatten results.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do_impl(self):
        ...
    def undo_impl(self):
        ...
class UnlinkSpecsCommand(AbstractLayerCommand):
    """
    Unlinks spec paths to layers.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, spec_paths: typing.Union[str, typing.List[str]], layer_identifiers: typing.Union[str, typing.List[str]], hierarchy = False, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    spec_paths (Union[str, List[str]]): List of spec paths or single spec path to be unlinked.
        
                    layer_identifiers (Union[str, List[str]]): List of layer identifiers or single layer identifier.
        
                    hierarchy (bool): Unlinking descendant specs or not.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
class UnlockSpecsCommand(AbstractLayerCommand):
    """
    Unlocks spec paths in the UsdContext
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, spec_paths: typing.Union[str, typing.List[str]], hierarchy = False, usd_context: typing.Union[str, omni.usd._usd.UsdContext] = ''):
        """
        Constructor.
        
                Keyword Arguments:
                    spec_paths (Union[str, List[str]]): List of spec paths or single spec path to be unlocked.
        
                    hierarchy (bool): Unlocking descendant specs or not.
        
                    usd_context (Union[str, omni.usd.UsdContext]): Usd context name or instance. It uses default context if it's empty.
                
        """
    def do(self):
        ...
    def undo(self):
        ...
def _get_usd_context(context_name_or_instance: typing.Union[str, omni.usd._usd.UsdContext] = ''):
    ...
