from __future__ import annotations
from isaacsim.core.utils.torch.rotations import gf_quat_to_tensor
from isaacsim.core.utils.torch.rotations import wxyz2xyzw
from isaacsim.core.utils.torch.rotations import xyzw2wxyz
from isaacsim.core.utils.torch.tensor import create_zeros_tensor
from pxr import Gf
from scipy.spatial.transform._rotation import Rotation
import torch as torch
__all__ = ['Gf', 'Rotation', 'assign_pose', 'create_zeros_tensor', 'get_local_from_world', 'get_pose', 'get_world_from_local', 'get_world_from_local_position', 'gf_quat_to_tensor', 'normalise_quat_in_pose', 'quat_apply', 'quat_conjugate', 'quat_mul', 'tf_apply', 'tf_combine', 'tf_inverse', 'tf_matrices_from_poses', 'tf_vector', 'torch', 'wxyz2xyzw', 'xyzw2wxyz']
def assign_pose(current_positions, current_orientations, positions, orientations, indices, device, pose = None):
    ...
def get_local_from_world(parent_transforms, positions, orientations, device):
    ...
def get_pose(positions, orientations, device):
    ...
def get_world_from_local(parent_transforms, translations, orientations, device):
    ...
def normalise_quat_in_pose(pose):
    """
    Takes a pose and normalises the quaternion portion of it.
    
        Args:
            pose: shape N, 7
        Returns:
            Pose with normalised quat. Shape N, 7
        
    """
def tf_matrices_from_poses(translations: torch.Tensor, orientations: torch.Tensor, device = None) -> torch.Tensor:
    """
    [summary]
    
        Args:
            translations (Union[np.ndarray, torch.Tensor]): translations with shape (N, 3).
            orientations (Union[np.ndarray, torch.Tensor]): quaternion representation (scalar first) with shape (N, 4).
    
        Returns:
            Union[np.ndarray, torch.Tensor]: transformation matrices with shape (N, 4, 4)
        
    """
get_world_from_local_position: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_apply: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_conjugate: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
quat_mul: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
tf_apply: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
tf_combine: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
tf_inverse: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
tf_vector: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
