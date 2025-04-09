from __future__ import annotations
import numpy
import numpy as np
import pxr.Usd
from pxr import Usd
import torch as torch
__all__ = ['ArticulationAction', 'ArticulationActions', 'DOFInfo', 'DataFrame', 'DynamicState', 'DynamicsViewState', 'JointsState', 'SDF_type_to_Gf', 'Usd', 'XFormPrimState', 'XFormPrimViewState', 'np', 'torch']
class ArticulationAction:
    """
    [summary]
    
        Args:
            joint_positions (Optional[Union[List, np.ndarray]], optional): [description]. Defaults to None.
            joint_velocities (Optional[Union[List, np.ndarray]], optional): [description]. Defaults to None.
            joint_efforts (Optional[Union[List, np.ndarray]], optional): [description]. Defaults to None.
        
    """
    def __init__(self, joint_positions: typing.Union[typing.List, numpy.ndarray, NoneType] = None, joint_velocities: typing.Union[typing.List, numpy.ndarray, NoneType] = None, joint_efforts: typing.Union[typing.List, numpy.ndarray, NoneType] = None, joint_indices: typing.Union[typing.List, numpy.ndarray, NoneType] = None) -> None:
        ...
    def __str__(self) -> str:
        ...
    def get_dict(self) -> dict:
        """
        [summary]
        
                Returns:
                    dict: [description]
                
        """
    def get_dof_action(self, index: int) -> dict:
        """
        [summary]
        
                Args:
                    index (int): [description]
        
                Returns:
                    dict: [description]
                
        """
    def get_length(self) -> typing.Optional[int]:
        """
        [summary]
        
                Returns:
                    Optional[int]: [description]
                
        """
class ArticulationActions:
    """
    [summary]
    
        Args:
            joint_positions (Optional[Union[List, np.ndarray]], optional): [description]. Defaults to None.
            joint_velocities (Optional[Union[List, np.ndarray]], optional): [description]. Defaults to None.
            joint_efforts (Optional[Union[List, np.ndarray]], optional): [description]. Defaults to None.
            joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                     to manipulate. Shape (K,).
                                                                                     Where K <= num of dofs.
                                                                                     Defaults to None (i.e: all dofs).
            joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                (can't be sppecified together with joint_indices). Shape (K,).
                                                Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
    """
    def __init__(self, joint_positions: typing.Union[typing.List, numpy.ndarray, NoneType] = None, joint_velocities: typing.Union[typing.List, numpy.ndarray, NoneType] = None, joint_efforts: typing.Union[typing.List, numpy.ndarray, NoneType] = None, joint_indices: typing.Union[typing.List, numpy.ndarray, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        ...
class DOFInfo:
    """
    [summary]
    
        Args:
            prim_path (str): [description]
            handle (int): [description]
            prim (Usd.Prim): [description]
            index (int): [description]
        
    """
    def __init__(self, prim_path: str, handle: int, prim: pxr.Usd.Prim, index: int) -> None:
        ...
class DataFrame:
    """
    [summary]
    
        Args:
            current_time_step (int): [description]
            current_time (float): [description]
            data (dict): [description]
        
    """
    @classmethod
    def init_from_dict(cls, dict_representation: dict):
        """
        [summary]
        
                Args:
                    dict_representation (dict): [description]
        
                Returns:
                    DataFrame: [description]
                
        """
    def __init__(self, current_time_step: int, current_time: float, data: dict) -> None:
        ...
    def __str__(self) -> str:
        ...
    def get_dict(self) -> dict:
        """
        [summary]
        
                Returns:
                    dict: [description]
                
        """
class DynamicState:
    """
    [summary]
    
        Args:
            position (np.ndarray): [description]
            orientation (np.ndarray): [description]
        
    """
    def __init__(self, position: numpy.ndarray, orientation: numpy.ndarray, linear_velocity: numpy.ndarray, angular_velocity: numpy.ndarray) -> None:
        ...
class DynamicsViewState:
    """
    [summary]
    
        Args:
            position (np.ndarray): [description]
            orientation (np.ndarray): [description]
        
    """
    def __init__(self, positions: typing.Union[numpy.ndarray, torch.Tensor], orientations: typing.Union[numpy.ndarray, torch.Tensor], linear_velocities: typing.Union[numpy.ndarray, torch.Tensor], angular_velocities: typing.Union[numpy.ndarray, torch.Tensor]) -> None:
        ...
class JointsState:
    """
    [summary]
    
        Args:
            positions (np.ndarray): [description]
            velocities (np.ndarray): [description]
            efforts (np.ndarray): [description]
        
    """
    def __init__(self, positions: numpy.ndarray, velocities: numpy.ndarray, efforts: numpy.ndarray) -> None:
        ...
class XFormPrimState:
    """
    [summary]
    
        Args:
            position (np.ndarray): [description]
            orientation (np.ndarray): [description]
        
    """
    def __init__(self, position: numpy.ndarray, orientation: numpy.ndarray) -> None:
        ...
class XFormPrimViewState:
    """
    [summary]
    
        Args:
            positions (Union[np.ndarray, torch.Tensor]): positions with shape of (N, 3).
            orientations (Union[np.ndarray, torch.Tensor]): quaternion representation of orientation (scalar first) with shape (N, 4).
        
    """
    def __init__(self, positions: typing.Union[numpy.ndarray, torch.Tensor], orientations: typing.Union[numpy.ndarray, torch.Tensor]) -> None:
        ...
SDF_type_to_Gf: dict = {'matrix3d': 'Gf.Matrix3d', 'matrix3f': 'Gf.Matrix3f', 'matrix4d': 'Gf.Matrix4d', 'matrix4f': 'Gf.Matrix4f', 'quatd': 'Gf.Quatd', 'quatf': 'Gf.Quatf', 'quath': 'Gf.Quath', 'range1d': 'Gf.Range1d', 'range1f': 'Gf.Range1f', 'range2d': 'Gf.Range2d', 'range2f': 'Gf.Range2f', 'range3d': 'Gf.Range3d', 'range3f': 'Gf.Range3f', 'rect2i': 'Gf.Rect2i', 'vec2d': 'Gf.Vec2d', 'vec2f': 'Gf.Vec2f', 'vec2h': 'Gf.Vec2h', 'vec2i': 'Gf.Vec2i', 'vec3d': 'Gf.Vec3d', 'double3': 'Gf.Vec3d', 'vec3f': 'Gf.Vec3f', 'vec3h': 'Gf.Vec3h', 'vec3i': 'Gf.Vec3i', 'vec4d': 'Gf.Vec4d', 'vec4f': 'Gf.Vec4f', 'vec4h': 'Gf.Vec4h', 'vec4i': 'Gf.Vec4i'}
