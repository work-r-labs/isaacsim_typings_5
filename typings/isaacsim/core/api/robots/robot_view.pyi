from __future__ import annotations
import isaacsim.core.prims.impl.articulation
from isaacsim.core.prims.impl.articulation import Articulation
import numpy as np
import torch as torch
__all__ = ['Articulation', 'RobotView', 'np', 'torch']
class RobotView(isaacsim.core.prims.impl.articulation.Articulation):
    """
    Implementation (on ``Articulation`` class) to deal with articulation prims as robots
    
        This class wraps all matching articulations found at the regex provided at the ``prim_paths_expr`` argument
    
        .. warning::
    
            The robot (articulation) view object must be initialized in order to be able to operate on it.
            See the ``initialize`` method for more details.
    
        Args:
            prim_paths_expr (str): prim paths regex to encapsulate all prims that match it.
                                    example: "/World/Env[1-5]/Franka" will match /World/Env1/Franka,
                                    /World/Env2/Franka, etc.
                                    (a non regex prim path can also be used to encapsulate one rigid prim).
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "rigid_prim_view".
            positions (Optional[Union[np.ndarray, torch.Tensor]], optional): default positions in the world frame of the prims.
                                                            shape is (N, 3). Defaults to None, which means left unchanged.
            translations (Optional[Union[np.ndarray, torch.Tensor]], optional):
                                                            default translations in the local frame of the prims
                                                            (with respect to its parent prims). shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            orientations (Optional[Union[np.ndarray, torch.Tensor]], optional):
                                                            default quaternion orientations in the world/ local frame of the prims
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (N, 4).
            scales (Optional[Union[np.ndarray, torch.Tensor]], optional): local scales to be applied to
                                                            the prim's dimensions in the view. shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            visibilities (Optional[Union[np.ndarray, torch.Tensor]], optional): set to false for an invisible prim in
                                                                                the stage while rendering. shape is (N,).
                                                                                Defaults to None.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> from isaacsim.core.cloner import GridCloner
            >>> from isaacsim.core.api.robots import RobotView
            >>> from pxr import UsdGeom
            >>>
            >>> usd_path = "/home/<user>/Documents/Assets/Robots/Franka/franka_alt_fingers.usd"
            >>> env_zero_path = "/World/envs/env_0"
            >>> num_envs = 5
            >>>
            >>> # load the Franka Panda robot USD file
            >>> stage_utils.add_reference_to_stage(usd_path, prim_path=f"{env_zero_path}/panda")  # /World/envs/env_0/panda
            >>>
            >>> # clone the environment (num_envs)
            >>> cloner = GridCloner(spacing=1.5)
            >>> cloner.define_base_env(env_zero_path)
            >>> UsdGeom.Xform.Define(stage_utils.get_current_stage(), env_zero_path)
            >>> cloner.clone(source_prim_path=env_zero_path, prim_paths=cloner.generate_paths("/World/envs/env", num_envs))
            >>>
            >>> # wrap all robots
            >>> prims = RobotView(prim_paths_expr="/World/envs/env.*/panda", name="franka_panda_view")
            >>> print(prims)
            <isaacsim.core.api.robots.robot_view.RobotView object at 0x7f12785a5fc0>
        
    """
    def __init__(self, prim_paths_expr: str, name: str = 'rigid_prim_view', positions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, translations: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, visibilities: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None) -> None:
        ...
    def post_reset(self) -> None:
        """
        Reset the robots to their default states
        
                .. note::
        
                    For the robots, in addition to configuring the root prim's default positions and spatial orientations
                    (defined via the ``set_default_state`` method), the joint's positions, velocities, and efforts
                    (defined via the ``set_joints_default_state`` method) and the joint's stiffness and dampings
                    (defined via the ``set_gains`` method) are imposed
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.post_reset()
                
        """
