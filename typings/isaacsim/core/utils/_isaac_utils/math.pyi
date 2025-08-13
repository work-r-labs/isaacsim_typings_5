"""
 
            
        Math Utils
        -----------

        This submodule provides math bindings for vector operations, and other facilitators such as `lerp` functions.
            
        
        
"""
from __future__ import annotations
import carb._carb
import typing
__all__: list[str] = ['add', 'cross', 'dot', 'get_basis_vector_x', 'get_basis_vector_y', 'get_basis_vector_z', 'inverse', 'lerp', 'mul', 'normalize', 'rotate', 'slerp', 'transform_inv']
def add(arg0: carb._carb.Float3, arg1: carb._carb.Float3) -> carb._carb.Float3:
    """
     Adds two 3D vectors
            Args:
                arg0 (:obj:`carb.Float3`): First 3D vector
    
                arg1 (:obj:`carb.Float3`): Second 3D vector
    
            Returns:
    
                :obj:`carb.Float3`: ``arg0 + arg1``.
    """
def cross(arg0: carb._carb.Float3, arg1: carb._carb.Float3) -> carb._carb.Float3:
    """
                 Performs Cross product between 3D vectors
                 Args:
                     arg0 (:obj:`carb.Float3`): 3D vector
    
                     arg1 (:obj:`carb.Float3`): 3D vector
    
                 Returns:
    
                    :obj:`carb.Float3`: cross poduct ``arg0 x arg1``.
    """
@typing.overload
def dot(arg0: carb._carb.Float3, arg1: carb._carb.Float3) -> float:
    """
    Performs Dot product between 3D vectors
                 Args:
                     arg0 (:obj:`carb.Float3`): 3D vector
    
                     arg1 (:obj:`carb.Float3`): 3D vector
    
                 Returns:
    
                     :obj:`carb.Float3`: dot poduct ``arg0 * arg1``.
    """
@typing.overload
def dot(arg0: carb._carb.Float4, arg1: carb._carb.Float4) -> float:
    """
    Performs Dot product between 4D vectors
                 Args:
                     arg0 (:obj:`carb.Float4`): 4D vector
    
                     arg1 (:obj:`carb.Float4`): 4D vector
    
                 Returns:
    
                     :obj:`carb.Float4`: dot poduct ``arg0 * arg1``.
    """
def get_basis_vector_x(arg0: carb._carb.Float4) -> carb._carb.Float3:
    """
                    Gets Basis vector X of quaternion
    
                    Args:
    
                        arg0 (:obj:`carb.Float4`): Quaternion
    
                    Returns:
    
                        :obj:`carb.Float3`: Basis Vector X
    """
def get_basis_vector_y(arg0: carb._carb.Float4) -> carb._carb.Float3:
    """
                    Gets Basis vector Y of quaternion
    
                    Args:
    
                        arg0 (:obj:`carb.Float4`): Quaternion
    
                    Returns:
    
                        :obj:`carb.Float3`: Basis Vector Y
    """
def get_basis_vector_z(arg0: carb._carb.Float4) -> carb._carb.Float3:
    """
                    Gets Basis vector Z of quaternion
    
                    Args:
    
                        arg0 (:obj:`carb.Float4`): Quaternion
    
                    Returns:
    
                        :obj:`carb.Float3`: Basis Vector Z
    """
def inverse(arg0: carb._carb.Float4) -> carb._carb.Float4:
    """
    Gets Inverse Quaternion
                 Args:
    
                     arg0 (:obj:`carb.Float4`): quaternion
    
                 Returns:
                 
                     :obj:`carb.Float4`: The inverse quaternion
    """
@typing.overload
def lerp(arg0: carb._carb.Float3, arg1: carb._carb.Float3, arg2: float) -> carb._carb.Float3:
    """
                    Performs Linear interpolation between points arg0 and arg1
    
                    Args:
    
                        arg0 (:obj:`carb.Float3`): Point
    
                        arg1 (:obj:`carb.Float3`): Point
    
                        arg2 (:obj:`float`): distance from 0 to 1, where 0 is closest to arg0, and 1 is closest to arg1
    
                    Returns:
    
                        :obj:`carb.Float3`: Interpolated point
    """
@typing.overload
def lerp(arg0: carb._carb.Float4, arg1: carb._carb.Float4, arg2: float) -> carb._carb.Float4:
    """
                    Performs Linear interpolation between quaternions arg0 and arg1
    
                    Args:
    
                        arg0 (:obj:`carb.Float4`): Quaternion
    
                        arg1 (:obj:`carb.Float4`): Quaternion
    
                        arg2 (:obj:`float`): distance from 0 to 1, where 0 is closest to arg0, and 1 is closest to arg1
    
                    Returns:
    
                        :obj:`carb.Float4`: Interpolated quaternion
    """
@typing.overload
def mul(arg0: carb._carb.Float3, arg1: float) -> carb._carb.Float3:
    """
     Scales a 3D vector by a given value
            
            Args:
                arg0 (:obj:`carb.Float3`): 3D vector
    
                arg1 (:obj:`float`): scale factor
    
            Returns:
                :obj:`carb.Float3`: scaled vector.
    """
@typing.overload
def mul(arg0: carb._carb.Float4, arg1: float) -> carb._carb.Float4:
    """
     Scales a 4D vector by a given value
            
            Args:
                arg0 (:obj:`carb.Float4`): 4D vector
    
                arg1 (:obj:`float`): scale factor
    
            Returns:
                :obj:`carb.Float4`: scaled vector.
    """
@typing.overload
def mul(arg0: carb._carb.Float4, arg1: carb._carb.Float4) -> carb._carb.Float4:
    """
     Performs a Quaternion rotation between two 4D vectors
            
            Args:
                arg0 (:obj:`carb.Float4`): first 4D quaternion vector
    
                arg1 (:obj:`carb.Float4`): second 4D quaternion vector
    
            Returns:
                :obj:`carb.Float4`: rotated 4D quaternion vector.
    """
@typing.overload
def normalize(arg0: carb._carb.Float3) -> carb._carb.Float3:
    """
                    Gets normalized 3D vector
    
                    Args:
    
                        arg0 (:obj:`carb.Float3`): 3D Vector
    
                    Returns:
    
                        :obj:`carb.Float3`: Normalized 3D Vector
    """
@typing.overload
def normalize(arg0: carb._carb.Float4) -> carb._carb.Float4:
    """
                    Gets normalized 4D vector
                    Args:
    
                        arg0 (:obj:`carb.Float4`): 4D Vector
                        
                    Returns:
    
                        :obj:`carb.Float4`: Normalized 4D Vector
    """
def rotate(arg0: carb._carb.Float4, arg1: carb._carb.Float3) -> carb._carb.Float3:
    """
                    rotates the 3D vector arg1 by the quaternion `arg0`
    
                    Args:
                    
                        arg0 (:obj:`carb.Float4`): quaternion
    
                        arg1 (:obj:`carb.Float3`): 3D Vector
    
                    Returns:
    
                        :obj:`carb.Float3`: Rotated 3D Vector
    """
def slerp(arg0: carb._carb.Float4, arg1: carb._carb.Float4, arg2: float) -> carb._carb.Float4:
    """
                    Performs Spherical Linear interpolation between quaternions arg0 and arg1
    
                    Args:
    
                        arg0 (:obj:`carb.Float4`): Quaternion
    
                        arg1 (:obj:`carb.Float4`): Quaternion
    
                        arg2 (:obj:`float`): distance from 0 to 1, where 0 is closest to arg0, and 1 is closest to arg1
    
                    Returns:
    
                        :obj:`carb.Float4`: Interpolated quaternion
    """
def transform_inv(arg0: ..., arg1: ...) -> ...:
    """
                    Computes local Transform of arg1 with respect to arg0: `inv(arg0)*arg1`
    
                    Args:
                    
                        arg0 (`pxr.Transform`): origin Transform
    
                        arg1 (`pxr.Transform`): Transform
    
                    Returns:
    
                        :obj:`oxr.Transform`: resulting transform of ``inv(arg0)*arg1``
    """
