from __future__ import annotations
import omni as omni
from pxr import Sdf
from pxr import Trace
import pxr.Usd
from pxr import Usd
__all__: list = ['get_all_sublayers', 'is_layer_locked', 'is_layer_writable', 'get_dirty_layers', 'get_edit_target_identifier', 'set_edit_target_by_identifier', 'stitch_prim_specs']
def _layer_traverse(layer, layer_identifier: str, unique_layer_set: typing.Set[str], include_only_omni_layers: bool, include_anonymous_layers: bool) -> typing.List[str]:
    ...
def get_all_sublayers(stage, include_session_layers = False, include_only_omni_layers = False, include_anonymous_layers = True) -> typing.List[str]:
    """
    Gets all sublayers from local layer stack of the stage ranking from strongest to weakest.
    """
def get_dirty_layers(stage: pxr.Usd.Stage, include_root_layer = True):
    """
    Gets all dirty layers that have unsaved changes.
    """
def get_edit_target_identifier(stage: pxr.Usd.Stage) -> str:
    """
    
        Gets the layer identifier of current edit target.
    
        Args:
            stage (Usd.Stage): Stage handle
    
        Returns:
            Layer identifier or empty string if edit target is not set.
        
    """
def is_layer_locked(usd_context, layer_identifier: str) -> bool:
    """
    Checkes if layer is locked or not in this usd context.
    
        Layer lock is a customized concept in Kit that's not from USD. It's used to complement the concept
        of file permission. Unlike the writable permission on file system, lock is bound
        to stage. So a layer may be locked in this stage, but not for other stages. Lock status
        is persistent across sessions, and saved as a flag inside the custom data of root layer.
        
    """
def is_layer_writable(layer_identifier: str) -> bool:
    """
    Checks if layer is writable on file system.
    """
def set_edit_target_by_identifier(stage: pxr.Usd.Stage, layer_identifier: str):
    """
    
        Sets the edit target of stage by layer identifier.
    
        Args:
            stage (Usd.Stage): Stage handle
            layer_identifier (str): Layer identifier
    
        Returns:
            True if success, false if layer cannot be found, or layer is not in
            the layer statck of stage.
        
    """
def stitch_prim_specs(*args, **kwargs):
    """
    
        Sitches prim specs specified by path scattered in all sublayers and all its children to target layer.
    
        Args:
            stage (Usd.Stage): Stage handle.
            prim_path (str): Prim path to be stitched.
            target_layer (Sdf.Layer): Target layer to save the stitching results.
            target_prim_path (str): Target prim path. If it's empty or none, it will be the prim_path.
            include_references_or_payloads: If prim is defined inside references or payloads, and this is
                True, it will also stitch the defs from references or payloads, too.
        
    """
