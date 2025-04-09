from __future__ import annotations
from isaacsim.core.utils.numpy.rotations import gf_quat_to_tensor
from isaacsim.core.utils.numpy.rotations import wxyz2xyzw
from isaacsim.core.utils.numpy.rotations import xyzw2wxyz
from isaacsim.core.utils.numpy.tensor import create_zeros_tensor
import numpy as np
import numpy
from pxr import Gf
from scipy.spatial.transform._rotation import Rotation
__all__ = ['Gf', 'Rotation', 'assign_pose', 'create_zeros_tensor', 'get_local_from_world', 'get_pose', 'get_world_from_local', 'gf_quat_to_tensor', 'np', 'tf_matrices_from_poses', 'wxyz2xyzw', 'xyzw2wxyz']
def assign_pose(current_positions, current_orientations, positions, orientations, indices, device = None, pose = None):
    ...
def get_local_from_world(parent_transforms, positions, orientations, device = None):
    ...
def get_pose(positions, orientations, device = None):
    ...
def get_world_from_local(parent_transforms, translations, orientations, device = None):
    ...
def tf_matrices_from_poses(translations: numpy.ndarray, orientations: numpy.ndarray, device = None) -> numpy.ndarray:
    """
    [summary]
    
        Args:
            translations (Union[np.ndarray, torch.Tensor]): translations with shape (N, 3).
            orientations (Union[np.ndarray, torch.Tensor]): quaternion representation (scalar first) with shape (N, 4).
    
        Returns:
            Union[np.ndarray, torch.Tensor]: transformation matrices with shape (N, 4, 4)
        
    """
