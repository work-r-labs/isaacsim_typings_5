from __future__ import annotations
from isaacsim.core.utils.torch.maths import cos
from isaacsim.core.utils.torch.maths import inverse
from isaacsim.core.utils.torch.maths import matmul
from isaacsim.core.utils.torch.maths import set_seed
from isaacsim.core.utils.torch.maths import sin
from isaacsim.core.utils.torch.maths import transpose_2d
from isaacsim.core.utils.torch.maths import unscale_np
import numpy as np
import os as os
from pxr import Gf
import random as random
from scipy.spatial.transform._rotation import Rotation
import torch as torch
import typing as typing
import warp as wp
__all__ = ['Gf', 'Rotation', 'compute_heading_and_up', 'compute_rot', 'copysign', 'cos', 'deg2rad', 'euler_angles_to_quats', 'get_basis_vector', 'get_euler_xyz', 'gf_quat_to_tensor', 'inverse', 'matmul', 'matrices_to_euler_angles', 'normalise_quat_in_pose', 'normalize', 'normalize_angle', 'np', 'os', 'quat_apply', 'quat_axis', 'quat_conjugate', 'quat_diff_rad', 'quat_from_angle_axis', 'quat_from_euler_xyz', 'quat_mul', 'quat_rotate', 'quat_rotate_inverse', 'quat_unit', 'quats_to_rot_matrices', 'rad2deg', 'random', 'rot_matrices_to_quats', 'scale', 'scale_transform', 'set_seed', 'sin', 'tensor_clamp', 'torch', 'torch_rand_float', 'torch_random_dir_2', 'transpose_2d', 'typing', 'unscale', 'unscale_np', 'unscale_transform', 'wp', 'wxyz2xyzw', 'xyzw2wxyz']
def deg2rad(degree_value: float, device = None) -> torch.Tensor:
    """
    _summary_
    
        Args:
            degree_value (torch.Tensor): _description_
            device (_type_, optional): _description_. Defaults to None.
    
        Returns:
            torch.Tensor: _description_
        
    """
def euler_angles_to_quats(euler_angles: torch.Tensor, degrees: bool = False, extrinsic: bool = True, device = None) -> torch.Tensor:
    """
    Vectorized version of converting euler angles to quaternion (scalar first)
    
        Args:
            euler_angles (typing.Union[np.ndarray, torch.Tensor]): euler angles with shape (N, 3)
            degrees (bool, optional): True if degrees, False if radians. Defaults to False.
            extrinsic (bool, optional): True if the euler angles follows the extrinsic angles
                       convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
                       the intrinsic angles conventions (equivalent to XYZ ordering).
                       Defaults to True.
    
        Returns:
            typing.Union[np.ndarray, torch.Tensor]: quaternions representation of the angles (N, 4) - scalar first.
        
    """
def gf_quat_to_tensor(orientation: typing.Union[pxr.Gf.Quatd, pxr.Gf.Quatf, pxr.Gf.Quaternion], device = None) -> torch.Tensor:
    """
    Converts a pxr Quaternion type to a torch array (scalar first).
    
        Args:
            orientation (typing.Union[Gf.Quatd, Gf.Quatf, Gf.Quaternion]): [description]
    
        Returns:
           torch.Tensor: [description]
        
    """
def normalise_quat_in_pose(pose):
    """
    Takes a pose and normalises the quaternion portion of it.
    
        Args:
            pose: shape N, 7
        Returns:
            Pose with normalised quat. Shape N, 7
        
    """
def rad2deg(radian_value: torch.Tensor, device = None) -> torch.Tensor:
    """
    _summary_
    
        Args:
            radian_value (torch.Tensor): _description_
            device (_type_, optional): _description_. Defaults to None.
    
        Returns:
            torch.Tensor: _description_
        
    """
def rot_matrices_to_quats(rotation_matrices: torch.Tensor, device = None) -> torch.Tensor:
    """
    Vectorized version of converting rotation matrices to quaternions
    
        Args:
            rotation_matrices (torch.Tensor): N Rotation matrices with shape (N, 3, 3) or (3, 3)
    
        Returns:
            torch.Tensor: quaternion representation of the rotation matrices (N, 4) or (4,) - scalar first
        
    """
def wxyz2xyzw(q):
    ...
def xyzw2wxyz(q):
    ...
compute_heading_and_up: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
compute_rot: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
copysign: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
get_basis_vector: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
get_euler_xyz: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
matrices_to_euler_angles: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
normalize: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
normalize_angle: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_apply: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_axis: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_conjugate: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_diff_rad: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_from_angle_axis: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_from_euler_xyz: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_mul: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_rotate: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_rotate_inverse: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_unit: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quats_to_rot_matrices: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
scale: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
scale_transform: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
tensor_clamp: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
torch_rand_float: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
torch_random_dir_2: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
unscale: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
unscale_transform: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
