from __future__ import annotations
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_attribute_names
from isaacsim.core.utils.prims import get_prim_attribute_value
from isaacsim.core.utils.prims import get_prim_parent
from isaacsim.core.utils.prims import get_prim_path
from isaacsim.core.utils.prims import is_prim_path_valid
import numpy as np
import pxr.Gf
from pxr import Gf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
from scipy.spatial.transform._rotation import Rotation
import usdrt as usdrt
__all__ = ['Gf', 'Rotation', 'Usd', 'UsdGeom', 'clear_xform_ops', 'get_local_pose', 'get_prim_at_path', 'get_prim_attribute_names', 'get_prim_attribute_value', 'get_prim_parent', 'get_prim_path', 'get_world_pose', 'is_prim_path_valid', 'np', 'reset_and_set_xform_ops', 'reset_xform_ops', 'usdrt']
def _get_world_pose_transform_w_scale(prim_path):
    ...
def clear_xform_ops(prim: pxr.Usd.Prim):
    """
    Remove all xform ops from input prim.
    
        Args:
            prim (Usd.Prim): The input USD prim.
        
    """
def get_local_pose(prim_path):
    ...
def get_world_pose(prim_path):
    ...
def reset_and_set_xform_ops(prim: pxr.Usd.Prim, translation: pxr.Gf.Vec3d, orientation: pxr.Gf.Quatd, scale: pxr.Gf.Vec3d = ...):
    """
    Reset xform ops to isaac sim defaults, and set their values
    
        Args:
            prim (Usd.Prim): Prim to reset
            translation (Gf.Vec3d): translation to set
            orientation (Gf.Quatd): orientation to set
            scale (Gf.Vec3d, optional): scale to set. Defaults to Gf.Vec3d([1.0, 1.0, 1.0]).
        
    """
def reset_xform_ops(prim: pxr.Usd.Prim):
    """
    Reset xform ops for a prim to isaac sim defaults,
    
        Args:
            prim (Usd.Prim): Prim to reset xform ops on
        
    """
