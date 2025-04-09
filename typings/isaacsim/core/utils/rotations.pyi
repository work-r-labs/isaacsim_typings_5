from __future__ import annotations
import math as math
import numpy as np
import numpy
import pxr.Gf
from pxr import Gf
import typing as typing
__all__ = ['Gf', 'euler_angles_to_quat', 'euler_to_rot_matrix', 'gf_quat_to_np_array', 'gf_rotation_to_np_array', 'lookat_to_quatf', 'math', 'matrix_to_euler_angles', 'np', 'quat_to_euler_angles', 'quat_to_rot_matrix', 'rot_matrix_to_quat', 'typing']
def euler_angles_to_quat(euler_angles: numpy.ndarray, degrees: bool = False, extrinsic: bool = True) -> numpy.ndarray:
    """
    Convert Euler angles to quaternion.
    
        Args:
            euler_angles (np.ndarray):  Euler XYZ angles.
            degrees (bool, optional): Whether input angles are in degrees. Defaults to False.
            extrinsic (bool, optional): True if the euler angles follows the extrinsic angles
                       convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
                       the intrinsic angles conventions (equivalent to XYZ ordering).
                       Defaults to True.
    
        Returns:
            np.ndarray: quaternion (w, x, y, z).
        
    """
def euler_to_rot_matrix(euler_angles: numpy.ndarray, degrees: bool = False, extrinsic: bool = True) -> numpy.ndarray:
    """
    Convert Euler XYZ or ZYX angles to rotation matrix.
    
        Args:
            euler_angles (np.ndarray): Euler angles.
            degrees (bool, optional): Whether passed angles are in degrees.
            extrinsic (bool, optional): True if the euler angles follows the extrinsic angles
                       convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
                       the intrinsic angles conventions (equivalent to XYZ ordering).
                       Defaults to True.
    
        Returns:
            np.ndarray:  A 3x3 rotation matrix in its extrinsic or intrinsic form depends on the extrinsic argument.
        
    """
def gf_quat_to_np_array(orientation: typing.Union[pxr.Gf.Quatd, pxr.Gf.Quatf, pxr.Gf.Quaternion]) -> numpy.ndarray:
    """
    Converts a pxr Quaternion type to a numpy array following [w, x, y, z] convention.
    
        Args:
            orientation (typing.Union[Gf.Quatd, Gf.Quatf, Gf.Quaternion]): Input quaternion object.
    
        Returns:
            np.ndarray: A (4,) quaternion array in (w, x, y, z).
        
    """
def gf_rotation_to_np_array(orientation: pxr.Gf.Rotation) -> numpy.ndarray:
    """
    Converts a pxr Rotation type to a numpy array following [w, x, y, z] convention.
    
        Args:
            orientation (Gf.Rotation): Pxr rotation object.
    
        Returns:
            np.ndarray: A (4,) quaternion array in (w, x, y, z).
        
    """
def lookat_to_quatf(camera: pxr.Gf.Vec3f, target: pxr.Gf.Vec3f, up: pxr.Gf.Vec3f) -> pxr.Gf.Quatf:
    """
    [summary]
    
        Args:
            camera (Gf.Vec3f): [description]
            target (Gf.Vec3f): [description]
            up (Gf.Vec3f): [description]
    
        Returns:
            Gf.Quatf: Pxr quaternion object.
        
    """
def matrix_to_euler_angles(mat: numpy.ndarray, degrees: bool = False, extrinsic: bool = True) -> numpy.ndarray:
    """
    Convert rotation matrix to Euler XYZ extrinsic or intrinsic angles.
    
        Args:
            mat (np.ndarray): A 3x3 rotation matrix.
            degrees (bool, optional): Whether returned angles should be in degrees.
            extrinsic (bool, optional): True if the rotation matrix follows the extrinsic matrix
                       convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
                       the intrinsic matrix conventions (equivalent to XYZ ordering).
                       Defaults to True.
    
        Returns:
            np.ndarray: Euler XYZ angles (intrinsic form) if extrinsic is False and Euler XYZ angles (extrinsic form) if extrinsic is True.
        
    """
def quat_to_euler_angles(quat: numpy.ndarray, degrees: bool = False, extrinsic: bool = True) -> numpy.ndarray:
    """
    Convert input quaternion to Euler XYZ or ZYX angles.
    
        Args:
            quat (np.ndarray): Input quaternion (w, x, y, z).
            degrees (bool, optional): Whether returned angles should be in degrees. Defaults to False.
            extrinsic (bool, optional): True if the euler angles follows the extrinsic angles
                       convention (equivalent to ZYX ordering but returned in the reverse) and False if it follows
                       the intrinsic angles conventions (equivalent to XYZ ordering).
                       Defaults to True.
    
    
        Returns:
            np.ndarray: Euler XYZ angles (intrinsic form) if extrinsic is False and Euler XYZ angles (extrinsic form) if extrinsic is True.
        
    """
def quat_to_rot_matrix(quat: numpy.ndarray) -> numpy.ndarray:
    """
    Convert input quaternion to rotation matrix.
    
        Args:
            quat (np.ndarray): Input quaternion (w, x, y, z).
    
        Returns:
            np.ndarray: A 3x3 rotation matrix.
        
    """
def rot_matrix_to_quat(mat: numpy.ndarray) -> numpy.ndarray:
    """
    Convert rotation matrix to Quaternion.
    
        Args:
            mat (np.ndarray): A 3x3 rotation matrix.
    
        Returns:
            np.ndarray: quaternion (w, x, y, z).
        
    """
_POLE_LIMIT: float = 0.999999
