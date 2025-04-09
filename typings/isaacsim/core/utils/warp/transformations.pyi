from __future__ import annotations
from isaacsim.core.utils.torch.rotations import gf_quat_to_tensor as torch_gf_quat_to_tensor
from isaacsim.core.utils.torch.transformations import tf_matrices_from_poses as torch_tf_matrices_from_poses
import numpy as np
from pxr import Gf
from scipy.spatial.transform._rotation import Rotation
import torch as torch
import warp as wp
import warp.context
__all__ = ['Gf', 'Rotation', 'assign_pose', 'get_local_from_world', 'get_pose', 'get_world_from_local', 'np', 'torch', 'torch_gf_quat_to_tensor', 'torch_tf_matrices_from_poses', 'wp']
def assign_pose(current_positions, current_orientations, positions, orientations, indices, device, pose):
    ...
def get_local_from_world(parent_transforms, positions, orientations, device):
    ...
def get_pose(positions, orientations, device):
    ...
def get_world_from_local(parent_transforms, translations, orientations, device):
    ...
_assign_current_pose: warp.context.Kernel  # value = <warp.context.Kernel object>
_assign_new_pose: warp.context.Kernel  # value = <warp.context.Kernel object>
_assign_pose: warp.context.Kernel  # value = <warp.context.Kernel object>
_local_to_world: warp.context.Kernel  # value = <warp.context.Kernel object>
