from __future__ import annotations
import numpy as np
from pxr import Gf
from scipy.spatial.transform._rotation import Rotation
import torch as torch
import typing as typing
import warp as wp
import warp.context
import warp.types
__all__ = ['Gf', 'PI', 'Rotation', 'deg2rad', 'euler_angles_to_quats', 'gf_quat_to_tensor', 'np', 'rad2deg', 'torch', 'typing', 'wp', 'wxyz2xyzw', 'xyzw2wxyz']
def deg2rad(degree_value: warp.types.array, device = None) -> warp.types.array:
    """
    _summary_
    
        Args:
            degree_value (torch.Tensor): _description_
            device (_type_, optional): _description_. Defaults to None.
    
        Returns:
            wp.types.array: _description_
        
    """
def euler_angles_to_quats(euler_angles: warp.types.array, degrees: bool = False, extrinsic: bool = True, device = None) -> warp.types.array:
    """
    Vectorized version of converting euler angles to quaternion (scalar first)
    
        Args:
            euler_angles (wp.types.array): euler angles with shape (N, 3)
            extrinsic (bool, optional): True if the euler angles follows the extrinsic angles
                       convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
                       the intrinsic angles conventions (equivalent to XYZ ordering).
                       Defaults to True.
            degrees (bool, optional): True if degrees, False if radians. Defaults to False.
    
        Returns:
            wp.types.array: quaternions representation of the angles (N, 4) - scalar first.
        
    """
def gf_quat_to_tensor(orientation: typing.Union[pxr.Gf.Quatd, pxr.Gf.Quatf, pxr.Gf.Quaternion], device = None) -> warp.types.array:
    """
    Converts a pxr Quaternion type to a torch array (scalar first).
    
        Args:
            orientation (typing.Union[Gf.Quatd, Gf.Quatf, Gf.Quaternion]): [description]
    
        Returns:
           wp.types.array: quaternion tensor
        
    """
def rad2deg(radian_value: warp.types.array, device = None) -> warp.types.array:
    """
    _summary_
    
        Args:
            radian_value (wp.types.array): _description_
            device (_type_, optional): _description_. Defaults to None.
    
        Returns:
            wp.types.array: _description_
        
    """
def wxyz2xyzw(q):
    ...
def xyzw2wxyz(q):
    ...
PI: float = 3.141592653589793
_wxyz2xyzw1: warp.context.Kernel  # value = <warp.context.Kernel object>
_wxyz2xyzw2: warp.context.Kernel  # value = <warp.context.Kernel object>
_wxyz2xyzw3: warp.context.Kernel  # value = <warp.context.Kernel object>
_xyzw2wxyz1: warp.context.Kernel  # value = <warp.context.Kernel object>
_xyzw2wxyz2: warp.context.Kernel  # value = <warp.context.Kernel object>
_xyzw2wxyz3: warp.context.Kernel  # value = <warp.context.Kernel object>
