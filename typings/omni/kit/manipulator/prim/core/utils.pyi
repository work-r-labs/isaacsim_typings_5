"""
This module provides utilities for manipulating and transforming primitives in 3D space, including functions to flatten matrices, compose transformation matrices from translation, rotation, and scale, generate compatible euler angles, find the best euler angles for a given transformation, and construct transformation matrices from separate components.
"""
from __future__ import annotations
import carb as carb
import math as math
from pxr import Gf
from pxr import Usd
from pxr import UsdGeom
import usdrt as usdrt
__all__ = ['Gf', 'Usd', 'UsdGeom', 'carb', 'compose_transform_ops_to_matrix', 'construct_transform_matrix_from_SRT', 'find_best_euler_angles', 'flatten', 'generate_compatible_euler_angles', 'math', 'repeat', 'usdrt']
def compose_transform_ops_to_matrix(translation: usdrt.Gf._Gf.Vec3d | usdrt.Gf._Gf.Vec3f | usdrt.Gf._Gf.Vec3h, rotation: usdrt.Gf._Gf.Vec3d | usdrt.Gf._Gf.Vec3f | usdrt.Gf._Gf.Vec3h, rotation_order: usdrt.Gf._Gf.Vec3i, scale: usdrt.Gf._Gf.Vec3d | usdrt.Gf._Gf.Vec3f | usdrt.Gf._Gf.Vec3h) -> usdrt.Gf._Gf.Matrix4d:
    """
    Composes a transformation matrix from translation, rotation, rotation order, and scale vectors.
    
        Args:
            translation (Union[:obj:`usdrt.Gf.Vec3d`, :obj:`usdrt.Gf.Vec3f`, :obj:`usdrt.Gf.Vec3h`]): The translation vector specifying the translation part of the transform.
            rotation (Union[:obj:`usdrt.Gf.Vec3d`, :obj:`usdrt.Gf.Vec3f`, :obj:`usdrt.Gf.Vec3h`]): The rotation vector specifying the rotation part of the transform in degrees.
            rotation_order (:obj:`usdrt.Gf.Vec3i`): The order of axes for the rotation specified as integers. Each element corresponds to an axis (0 for x, 1 for y, 2 for z).
            scale (Union[:obj:`usdrt.Gf.Vec3d`, :obj:`usdrt.Gf.Vec3f`, :obj:`usdrt.Gf.Vec3h`]): The scale vector specifying the scale part of the transform.
    
        Returns:
            :obj:`usdrt.Gf.Matrix4d`: The composed transformation matrix as a 4x4 matrix.
    """
def construct_transform_matrix_from_SRT(t: usdrt.Gf._Gf.Vec3d, rot_euler: usdrt.Gf._Gf.Vec3d, rot_order: usdrt.Gf._Gf.Vec3i, scale: usdrt.Gf._Gf.Vec3d, pivot_inv: usdrt.Gf._Gf.Matrix4d) -> usdrt.Gf._Gf.Matrix4d:
    """
    Constructs a transformation matrix from separate components of scale, rotation, and translation.
    
        Args:
            t (usdrt.Gf.Vec3d): The translation vector.
            rot_euler (usdrt.Gf.Vec3d): The rotation vector in Euler angles.
            rot_order (usdrt.Gf.Vec3i): The order of rotations to apply.
            scale (usdrt.Gf.Vec3d): The scaling vector.
            pivot_inv (usdrt.Gf.Matrix4d): The inverse of the pivot matrix.
    
        Returns:
            usdrt.Gf.Matrix4d: The constructed transform matrix as a 4x4 matrix.
    """
def find_best_euler_angles(old_rot_vec: usdrt.Gf._Gf.Vec3d, new_rot_vec: usdrt.Gf._Gf.Vec3d, rotation_order: usdrt.Gf._Gf.Vec3i) -> usdrt.Gf._Gf.Vec3d:
    """
    Finds the closest euler angles to the old rotation vector that correspond to the new rotation vector.
    
        Args:
            old_rot_vec (:obj:`usdrt.Gf.Vec3d`): The original rotation vector that the new euler angles should be close to.
            new_rot_vec (:obj:`usdrt.Gf.Vec3d`): The target rotation vector to find the closest euler angles for.
            rotation_order (:obj:`usdrt.Gf.Vec3i`): The order of rotations to be considered when generating euler angles.
    
        Returns:
            :obj:`usdrt.Gf.Vec3d`: The euler angles that are closest to the original rotation vector.
    """
def flatten(*args, **kwds):
    """
    Convert array[4][4] to array[16]
    """
def generate_compatible_euler_angles(euler: usdrt.Gf._Gf.Vec3d, rotation_order: usdrt.Gf._Gf.Vec3i) -> typing.List[usdrt.Gf._Gf.Vec3d]:
    """
    Generates a list of euler angles that are compatible with the provided euler angles and rotation order.
    
        Args:
            euler (:obj:`usdrt.Gf.Vec3d`): The original euler angles to find compatible angles for.
            rotation_order (:obj:`usdrt.Gf.Vec3i`): The order of rotation axes.
    
        Returns:
            List[:obj:`usdrt.Gf.Vec3d`]: A list of euler angles compatible with the given euler angles and rotation order.
        
    """
def repeat(t: float, length: float) -> float:
    """
    Args:
            t (float): The value to be repeated within the range.
            length (float): The range length within which the value 't' is to be repeated.
    
        Returns:
            float: The repeated value of 't' within the range of 'length'.
    """
