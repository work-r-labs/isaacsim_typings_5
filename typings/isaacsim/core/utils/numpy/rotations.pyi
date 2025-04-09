from __future__ import annotations
import numpy as np
import numpy
from pxr import Gf
from scipy.spatial.transform._rotation import Rotation
import typing as typing
__all__ = ['Gf', 'Rotation', 'deg2rad', 'euler_angles_to_quats', 'gf_quat_to_tensor', 'np', 'quats_to_euler_angles', 'quats_to_rot_matrices', 'quats_to_rotvecs', 'rad2deg', 'rot_matrices_to_quats', 'rotvecs_to_quats', 'typing', 'wxyz2xyzw', 'xyzw2wxyz']
def deg2rad(degree_value: numpy.ndarray, device = None) -> numpy.ndarray:
    """
    _summary_
    
        Args:
            degree_value (np.ndarray): _description_
            device (_type_, optional): _description_. Defaults to None.
    
        Returns:
            np.ndarray: _description_
        
    """
def euler_angles_to_quats(euler_angles: numpy.ndarray, degrees: bool = False, extrinsic: bool = True, device = None) -> numpy.ndarray:
    """
    Vectorized version of converting euler angles to quaternion (scalar first)
    
        Args:
            euler_angles np.ndarray: euler angles with shape (N, 3) or (3,) representation XYZ in extrinsic coordinates
            extrinsic (bool, optional): True if the euler angles follows the extrinsic angles
                       convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
                       the intrinsic angles conventions (equivalent to XYZ ordering).
                       Defaults to True.
            degrees (bool, optional): True if degrees, False if radians. Defaults to False.
    
        Returns:
            np.ndarray: quaternions representation of the angles (N, 4) or (4,) - scalar first.
        
    """
def gf_quat_to_tensor(orientation: typing.Union[pxr.Gf.Quatd, pxr.Gf.Quatf, pxr.Gf.Quaternion], device = None) -> numpy.ndarray:
    """
    Converts a pxr Quaternion type to a numpy array following [w, x, y, z] convention.
    
        Args:
            orientation (typing.Union[Gf.Quatd, Gf.Quatf, Gf.Quaternion]): [description]
    
        Returns:
            np.ndarray: [description]
        
    """
def quats_to_euler_angles(quaternions: numpy.ndarray, degrees: bool = False, extrinsic: bool = True, device = None) -> numpy.ndarray:
    """
    Vectorized version of converting quaternions (scalar first) to euler angles
    
        Args:
            quaternions (np.ndarray): quaternions with shape (N, 4) or (4,) - scalar first
            degrees (bool, optional): Return euler angles in degrees if True, radians if False. Defaults to False.
            extrinsic (bool, optional): True if the euler angles follows the extrinsic angles
                       convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
                       the intrinsic angles conventions (equivalent to XYZ ordering).
                       Defaults to True.
    
        Returns:
            np.ndarray: Euler angles in extrinsic or intrinsic coordinates XYZ order with shape (N, 3) or (3,) corresponding to the quaternion rotations
        
    """
def quats_to_rot_matrices(quaternions: numpy.ndarray, device = None) -> numpy.ndarray:
    """
    Vectorized version of converting quaternions to rotation matrices
    
        Args:
            quaternions (np.ndarray): quaternions with shape (N, 4) or (4,) and scalar first
    
        Returns:
            np.ndarray: N Rotation matrices with shape (N, 3, 3) or (3, 3)
        
    """
def quats_to_rotvecs(quaternions: numpy.ndarray, device = None) -> numpy.ndarray:
    """
    Vectorized version of converting quaternions to rotation vectors
    
        Args:
            quaternions (np.ndarray): quaternions with shape (N, 4) or (4,) and scalar first
    
        Returns:
            np.ndarray: N rotation vectors with shape (N,3) or (3,).  The magnitude of the rotation vector describes the magnitude of the rotation.
                The normalized rotation vector represents the axis of rotation.
        
    """
def rad2deg(radian_value: numpy.ndarray, device = None) -> numpy.ndarray:
    """
    _summary_
    
        Args:
            radian_value (np.ndarray): _description_
            device (_type_, optional): _description_. Defaults to None.
    
        Returns:
            np.ndarray: _description_
        
    """
def rot_matrices_to_quats(rotation_matrices: numpy.ndarray, device = None) -> numpy.ndarray:
    """
    Vectorized version of converting rotation matrices to quaternions
    
        Args:
            rotation_matrices (np.ndarray): N Rotation matrices with shape (N, 3, 3) or (3, 3)
    
        Returns:
            np.ndarray: quaternion representation of the rotation matrices (N, 4) or (4,) - scalar first
        
    """
def rotvecs_to_quats(rotation_vectors: numpy.ndarray, degrees: bool = False, device = None) -> numpy.ndarray:
    """
    Vectorized version of converting rotation vectors to quaternions
    
        Args:
            rotation_vectors (np.ndarray): N rotation vectors with shape (N, 3) or (3,).  The magnitude of the rotation vector describes the magnitude of the rotation.
                The normalized rotation vector represents the axis of rotation.
            degrees (bool): The magnitude of the rotation vector will be interpreted as degrees if True, and radians if False.  Defaults to False.
    
        Returns:
            np.ndarray: quaternion representation of the rotation matrices (N, 4) or (4,) - scalar first
        
    """
def wxyz2xyzw(q, ret_torch = False):
    ...
def xyzw2wxyz(q, ret_torch = False):
    ...
