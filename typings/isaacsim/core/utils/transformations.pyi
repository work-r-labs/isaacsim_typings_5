from __future__ import annotations
from isaacsim.core.utils.rotations import gf_quat_to_np_array
import numpy
import numpy as np
from pxr import Gf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
from scipy.spatial.transform._rotation import Rotation
import torch as torch
__all__ = ['Gf', 'Rotation', 'Usd', 'UsdGeom', 'get_relative_transform', 'get_transform_with_normalized_rotation', 'get_translation_from_target', 'get_world_pose_from_relative', 'gf_quat_to_np_array', 'np', 'pose_from_tf_matrix', 'tf_matrices_from_poses', 'tf_matrix_from_pose', 'torch']
def get_relative_transform(source_prim: pxr.Usd.Prim, target_prim: pxr.Usd.Prim) -> numpy.ndarray:
    """
    Get the relative transformation matrix from the source prim to the target prim.
    
        Args:
            source_prim (Usd.Prim): source prim from which frame to compute the relative transform.
            target_prim (Usd.Prim): target prim to which frame to compute the relative transform.
    
        Returns:
            np.ndarray: Column-major transformation matrix with shape (4, 4).
        
    """
def get_transform_with_normalized_rotation(transform: numpy.ndarray) -> numpy.ndarray:
    """
    Get the transform after normalizing rotation component.
    
        Args:
            transform (np.ndarray): transformation matrix with shape (4, 4).
    
        Returns:
            np.ndarray: transformation matrix with normalized rotation with shape (4, 4).
        
    """
def get_translation_from_target(translation_from_source: numpy.ndarray, source_prim: pxr.Usd.Prim, target_prim: pxr.Usd.Prim) -> numpy.ndarray:
    """
    Get a translation with respect to the target's frame, from a translation in the source's frame.
    
        Args:
            translation_from_source (np.ndarray): translation from the frame of the prim at source_path. Shape is (3, ).
            source_prim (Usd.Prim): prim path of the prim whose frame the original/untransformed translation
                               (translation_from_source) is defined with respect to.
            target_prim (Usd.Prim): prim path of the prim whose frame corresponds to the target frame that the returned
                               translation will be defined with respect to.
    
        Returns:
            np.ndarray: translation with respect to the target's frame. Shape is (3, ).
        
    """
def get_world_pose_from_relative(coord_prim: pxr.Usd.Prim, relative_translation: numpy.ndarray, relative_orientation: numpy.ndarray) -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Get a pose defined in the world frame from a pose defined relative to the frame of the coord_prim.
    
        Args:
            coord_prim (Usd.Prim): path of the prim whose frame the relative pose is defined with respect to.
            relative_translation (np.ndarray): translation relative to the frame of the prim at prim_path. Shape is (3, ).
            relative_orientation (np.ndarray): quaternion orientation relative to the frame of the prim at prim_path.
                                               Quaternion is scalar-first (w, x, y, z). Shape is (4, ).
    
        Returns:
            Tuple[np.ndarray, np.ndarray]: first index is position in the world frame. Shape is (3, ). Second index is
                                           quaternion orientation in the world frame. Quaternion is scalar-first
                                           (w, x, y, z). Shape is (4, ).
        
    """
def pose_from_tf_matrix(transformation: numpy.ndarray) -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
    """
    Gets pose corresponding to input transformation matrix.
    
        Args:
            transformation (np.ndarray): Column-major transformation matrix. shape is (4, 4).
    
        Returns:
            Tuple[np.ndarray, np.ndarray]: first index is translation corresponding to transformation. shape is (3, ).
                                           second index is quaternion orientation corresponding to transformation.
                                           quaternion is scalar-first (w, x, y, z). shape is (4, ).
        
    """
def tf_matrices_from_poses(translations: typing.Union[numpy.ndarray, torch.Tensor], orientations: typing.Union[numpy.ndarray, torch.Tensor]) -> typing.Union[numpy.ndarray, torch.Tensor]:
    """
    [summary]
    
        Args:
            translations (Union[np.ndarray, torch.Tensor]): translations with shape (N, 3).
            orientations (Union[np.ndarray, torch.Tensor]): quaternion representation (scalar first) with shape (N, 4).
    
        Returns:
            Union[np.ndarray, torch.Tensor]: transformation matrices with shape (N, 4, 4)
        
    """
def tf_matrix_from_pose(translation: typing.Sequence[float], orientation: typing.Sequence[float]) -> numpy.ndarray:
    """
    Compute input pose to transformation matrix.
    
        Args:
            pos (Sequence[float]): The translation vector.
            rot (Sequence[float]): The orientation quaternion.
    
        Returns:
            np.ndarray: A 4x4 matrix.
        
    """
