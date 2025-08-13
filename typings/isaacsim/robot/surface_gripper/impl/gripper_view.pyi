from __future__ import annotations
import isaacsim.core.experimental.prims.impl.xform_prim
from isaacsim.core.experimental.prims.impl.xform_prim import XformPrim
from isaacsim.core.experimental.utils import ops as ops_utils
from isaacsim.robot.surface_gripper import _surface_gripper as surface_gripper
import numpy as np
import typing
from usd.schema.isaac import robot_schema
import warp as wp
__all__: list[str] = ['GripperView', 'XformPrim', 'np', 'ops_utils', 'robot_schema', 'surface_gripper', 'wp']
class GripperView(isaacsim.core.experimental.prims.impl.xform_prim.XformPrim):
    """
    Provides high level functions to deal with batched data from surface gripper
    
        Args:
            paths: Prim paths regex to encapsulate all prims that match it. E.g.: "/World/Env[1-5]/Gripper" will match
                   /World/Env1/Gripper, /World/Env2/Gripper..etc. Additionally a list of regex can be provided.
            max_grip_distance: Maximum distance for which the surface gripper can gripped an object. Shape is (N).
                               Defaults to None, which means left unchanged.
            coaxial_force_limit: Maximum coaxial force that the surface gripper can withstand without dropping the gripped object. Shape is (N).
                                 Defaults to None, which means left unchanged.
            shear_force_limit: Maximum shear force that the surface gripper can withstand without dropping the gripped object. Shape is (N).
                               Defaults to None, which means left unchanged.
            retry_interval: Indicates the duration for which the surface gripper is attempting to grip an object.
                            Defaults to None, which means left unchanged.
            positions: Default positions in the world frame of the prim. Shape is (N, 3).
                       Defaults to None, which means left unchanged.
            translations: Default translations in the local frame of the prims (with respect to its parent prims). shape is (N, 3).
                          Defaults to None, which means left unchanged.
            orientations: Default quaternion orientations in the world/ local frame of the prim (depends if translation
                          or position is specified). Quaternion is scalar-first (w, x, y, z). Shape is (N, 4).
                          Defaults to None, which means left unchanged.
            scales: Local scales to be applied to the prim's dimensions. Shape is (N, 3).
                    Defaults to None, which means left unchanged.
            reset_xform_properties: True if the prims don't have the right set of xform properties (i.e: translate,
                                    orient and scale) ONLY and in that order. Set this parameter to False if the object
                                    were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.
    
        Raises:
            Exception: if translations and positions defined at the same time.
            Exception: No prim was matched using the prim_paths_expr provided.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __del__(self):
        ...
    def __init__(self, paths: str = None, max_grip_distance: np.ndarray | wp.array | None = None, coaxial_force_limit: np.ndarray | wp.array | None = None, shear_force_limit: np.ndarray | wp.array | None = None, retry_interval: np.ndarray | wp.array | None = None, positions: np.ndarray | wp.array | None = None, translations: np.ndarray | wp.array | None = None, orientations: np.ndarray | wp.array | None = None, scales: np.ndarray | wp.array | None = None, reset_xform_op_properties: bool = True):
        ...
    def apply_gripper_action(self, values: list[float], indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set up the status for the surface grippers.
        
                Args:
                    values: New status of the surface gripper. Shape (N,). Where N is the number of encapsulated prims in the view.
                    indices: Specific surface gripper to update. Shape (M,). Where M <= size of the encapsulated prims in the view.
                             Defaults to None (i.e: all prims in the view).
        
                Raises:
                    Exception: If the length of values does not match the number of encapsulated prims in the view.
                    Exception: If a value in indices is larger then the number of encapsulated prims in the view.
                
        """
    def get_surface_gripper_properties(self, indices: list | np.ndarray | wp.array | None = None) -> tuple[list[float], list[float], list[float], list[float]]:
        """
        Get the properties for the surface grippers.
        
                Args:
                    indices: Specific surface gripper to update. Shape (M,). Where M <= size of the encapsulated prims in the view.
                             Defaults to None (i.e: all prims in the view).
        
                Returns:
                    tuple[list[float], list[float], list[float], list[float]]: First index is maximum grip distance. Shape (M,).
                                                                               Second index is coaxial force limit. Shape (M,).
                                                                               Third index is shear force limit. Shape (M,).
                                                                               Fourth index is the retry interval. Shape (M,).
                
        """
    def get_surface_gripper_status(self, indices: list | np.ndarray | wp.array | None = None) -> list[str]:
        """
        Get the status for the surface grippers.
        
                Args:
                    indices: Specific surface gripper to update. Shape (M,). Where M <= size of the encapsulated prims in the view.
                             Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[str]: Status of the surface grippers ("Open", "Closing", or "Closed"). Shape (M,).
                
        """
    def set_surface_gripper_properties(self, max_grip_distance: list[float] | None = None, coaxial_force_limit: list[float] | None = None, shear_force_limit: list[float] | None = None, retry_interval: list[float] | None = None, indices: list | np.ndarray | wp.array | None = None) -> None:
        """
        Set up the properties for the surface grippers.
        
                Args:
                    max_grip_distance: New maximum grip distance of the surface gripper. Shape (N,). Where N is the number of encapsulated prims in the view.
                                       Defaults to None, which means left unchanged.
                    coaxial_force_limit: New coaxial force limit of the surface gripper. Shape (N,). Where N is the number of encapsulated prims in the view.
                                         Defaults to None, which means left unchanged.
                    shear_force_limit: New shear force limit of the surface gripper. Shape (N,). Where N is the number of encapsulated prims in the view.
                                       Defaults to None, which means left unchanged.
                    retry_interval: New retry interval of the surface gripper. Shape (N,). Where N is the number of encapsulated prims in the view.
                                    Defaults to None, which means left unchanged.
                    indices: Specific surface gripper to update. Shape (M,). Where M <= size of the encapsulated prims in the view.
                             Defaults to None (i.e: all prims in the view).
        
                Raises:
                    Exception: If the length of any properties does not match the number of encapsulated prims in the view.
                    Exception: If a value in indices is larger then the number of encapsulated prims in the view.
                
        """
