from __future__ import annotations
import carb as carb
from collections import OrderedDict
import gc as gc
import isaacsim.core.prims.impl.xform_prim
from isaacsim.core.prims.impl.xform_prim import XFormPrim
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils import numpy as numpy_utils
from isaacsim.core.utils.prims import get_articulation_root_api_prim_path
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_parent
from isaacsim.core.utils.prims import get_prim_property
from isaacsim.core.utils.prims import set_prim_property
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationActions
from isaacsim.core.utils.types import JointsState
from isaacsim.core.utils.types import XFormPrimViewState
import numpy as np
import omni as omni
from pxr import PhysxSchema
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import torch as torch
import warp as wp
import weakref as weakref
__all__ = ['Articulation', 'ArticulationActions', 'IsaacEvents', 'JointsState', 'OrderedDict', 'PhysxSchema', 'SimulationManager', 'Usd', 'UsdGeom', 'UsdPhysics', 'XFormPrim', 'XFormPrimViewState', 'carb', 'gc', 'get_articulation_root_api_prim_path', 'get_prim_at_path', 'get_prim_parent', 'get_prim_property', 'np', 'numpy_utils', 'omni', 'set_prim_property', 'torch', 'weakref', 'wp']
class Articulation(isaacsim.core.prims.impl.xform_prim.XFormPrim):
    """
    High level wrapper to deal with prims (one or many) that have the Root Articulation API applied
        and their attributes/properties
    
        This class wraps all matching articulations found at the regex provided at the ``prim_paths_expr`` argument
    
        .. note::
    
            Each prim will have ``xformOp:orient``, ``xformOp:translate`` and ``xformOp:scale`` only post-init,
            unless it is a non-root articulation link.
    
        .. warning::
    
            The articulation view object must be initialized in order to be able to operate on it.
            See the ``initialize`` method for more details.
    
        Args:
            prim_paths_expr (Union[str, List[str]]): prim paths regex to encapsulate all prims that match it.
                                    example: "/World/Env[1-5]/Franka" will match /World/Env1/Franka,
                                    /World/Env2/Franka..etc.
                                    (a non regex prim path can also be used to encapsulate one rigid prim).
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "articulation_prim_view".
            positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): default positions in the world frame of the prims.
                                                                            shape is (N, 3). Defaults to None, which means left unchanged.
            translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional):
                                                            default translations in the local frame of the prims
                                                            (with respect to its parent prims). shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional):
                                                            default quaternion orientations in the world/ local frame of the prims
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (N, 4).
            scales (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): local scales to be applied to
                                                            the prim's dimensions in the view. shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            visibilities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): set to false for an invisible prim in
                                                                                the stage while rendering. shape is (N,).
                                                                                Defaults to None.
            reset_xform_properties (bool, optional): True if the prims don't have the right set of xform properties
                                                    (i.e: translate, orient and scale) ONLY and in that order.
                                                    Set this parameter to False if the object were cloned using using
                                                    the cloner api in isaacsim.core.cloner. Defaults to True.
            enable_residual_reports (bool optional): Setting to True will enable using the residual reporting APIs. Defaults to False.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> from isaacsim.core.cloner import GridCloner
            >>> from isaacsim.core.prims import Articulation
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
            >>> # wrap all articulations
            >>> prims = Articulation(prim_paths_expr="/World/envs/env.*/panda", name="franka_panda_view")
            >>> prims
            <isaacsim.core.prims.articulation.Articulation object at 0x7ff174054b20>
        
    """
    def __del__(self):
        ...
    def __init__(self, prim_paths_expr: typing.Union[str, typing.List[str]], name: str = 'articulation_prim_view', positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, translations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, scales: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, visibilities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, reset_xform_properties: bool = True, enable_residual_reports: bool = False) -> None:
        ...
    def _apply_residual_reporting_api(self, prim):
        ...
    def _convert_joint_names_to_indices(self, joint_names):
        ...
    def _invalidate_physics_handle_callback(self, event):
        ...
    def _on_physics_ready(self, event) -> None:
        ...
    def _on_post_reset(self, event) -> None:
        ...
    def _on_prim_deletion(self, prim_path):
        ...
    def apply_action(self, control_actions: isaacsim.core.utils.types.ArticulationActions, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Apply joint positions (targets), velocities (targets) and/or efforts to control an articulation
        
                .. note::
        
                    This method can be used instead of the separate ``set_joint_position_targets``,
                    ``set_joint_velocity_targets`` and ``set_joint_efforts``
        
                Args:
                    control_actions (ArticulationActions): actions to be applied for next physics step.
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                .. hint::
        
                    High stiffness makes the joints snap faster and harder to the desired target,
                    and higher damping smoothes but also slows down the joint's movement to target
        
                    * For position control, set relatively high stiffness and low damping (to reduce vibrations)
                    * For velocity control, stiffness must be set to zero with a non-zero damping
                    * For effort control, stiffness and damping must be set to zero
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.utils.types import ArticulationActions
                    >>>
                    >>> # move all the articulation joints to the indicated position.
                    >>> # Since there are 5 envs, the joint positions are repeated 5 times
                    >>> positions = np.tile(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]), (num_envs, 1))
                    >>> action = ArticulationActions(joint_positions=positions)
                    >>> prims.apply_action(action)
                    >>>
                    >>> # close the robot fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
                    >>> # for the first, middle and last of the 5 envs
                    >>> positions = np.tile(np.array([0.0, 0.0]), (3, 1))
                    >>> action = ArticulationActions(joint_positions=positions, joint_indices=np.array([7, 8]))
                    >>> prims.apply_action(action, indices=np.array([0, 2, 4]))
                
        """
    def get_angular_velocities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the angular velocities of prims in the view.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: angular velocities of the prims in the view. shape is (M, 3).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all articulation angular velocities. Returned shape is (5, 3) for the example: 5 envs, angular (3)
                    >>> prims.get_angular_velocities()
                    [[0. 0. 0.]
                     [0. 0. 0.]
                     [0. 0. 0.]
                     [0. 0. 0.]
                     [0. 0. 0.]]
                    >>>
                    >>> # get only the articulation angular velocities for the first, middle and last of the 5 envs
                    >>> # Returned shape is (5, 3) for the example: 3 envs selected, angular (3)
                    >>> prims.get_angular_velocities(indices=np.array([0, 2, 4]))
                    [[0. 0. 0.]
                     [0. 0. 0.]
                     [0. 0. 0.]]
                
        """
    def get_applied_actions(self, clone: bool = True) -> isaacsim.core.utils.types.ArticulationActions:
        """
        Get the last applied actions
        
                Args:
                    clone (bool, optional): True to return clones of the internal buffers. Otherwise False. Defaults to True.
        
                Returns:
                    ArticulationActions: current applied actions (i.e: current position targets and velocity targets)
        
                Example:
        
                .. code-block:: python
        
                    >>> # last applied action: joint_positions -> [0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04].
                    >>> # Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> actions = prims.get_applied_actions()
                    >>> actions
                    <isaacsim.core.utils.types.ArticulationActions object at 0x7f28af31d870>
                    >>> actions.joint_positions
                    [[ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]
                     [ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]
                     [ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]
                     [ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]
                     [ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]]
                    >>> actions.joint_velocities
                    [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]]
                    >>> actions.joint_efforts
                    [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]]
                
        """
    def get_applied_joint_efforts(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the joint efforts of articulations in the view
        
                This method will return the efforts set by the ``set_joint_efforts`` method
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: joint efforts of articulations in the view. Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all applied joint efforts. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> prims.get_applied_joint_efforts()
                    [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]]
                    >>>
                    >>> # get finger applied efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_applied_joint_efforts(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    [[0. 0.]
                     [0. 0.]
                     [0. 0.]]
                
        """
    def get_armatures(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get armatures for articulation joints in the view
        
                Search for *"Joint Armature"* in |physx_docs| for more details.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                    clone (Optional[bool]): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: joint armatures for articulations in the view. shape (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get joint armatures. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> prims.get_armatures()
                    [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]]
                    >>>
                    >>> # get only the finger joint (panda_finger_joint1 (7) and panda_finger_joint2 (8)) armatures
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_armatures(indices=np.array([0,2,4]), joint_indices=np.array([7,8]))
                    [[0. 0.]
                     [0. 0.]
                     [0. 0.]]
                
        """
    def get_articulation_body_count(self) -> int:
        """
        Get the number of rigid bodies (links) of the articulations
        
                Returns:
                    int: maximum number of rigid bodies (links) in the articulation
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.get_articulation_body_count()
                    12
                
        """
    def get_body_coms(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get rigid body center of mass (COM) of articulations in the view.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: rigid body center of mass positions and orientations
                    of articulations in the view. Position shape is (M, K, 3), orientation shape is (M, k, 4).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all body center of mass. Returned shape is (5, 12, 3) for positions and (5, 12, 4) for orientations
                    >>> # for the example: 5 envs, 12 rigid bodies
                    >>> positions, orientations = prims.get_body_coms()
                    >>> positions
                    [[[0. 0. 0.]
                      [0. 0. 0.]
                      ...
                      [0. 0. 0.]
                      [0. 0. 0.]]]
                    >>> orientations
                    [[[1. 0. 0. 0.]
                      [1. 0. 0. 0.]
                      ...
                      [1. 0. 0. 0.]
                      [1. 0. 0. 0.]]]
                    >>>
                    >>> # get finger body center of mass: panda_leftfinger (10) and panda_rightfinger (11) for the first,
                    >>> # middle and last of the 5 envs. Returned shape is (3, 2, 3) for positions and (3, 2, 4) for orientations
                    >>> positions, orientations = prims.get_body_coms(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
                    >>> positions
                    [[[0. 0. 0.]
                      [0. 0. 0.]]
                     [[0. 0. 0.]
                      [0. 0. 0.]]
                     [[0. 0. 0.]
                      [0. 0. 0.]]]
                    >>> orientations
                    [[[1. 0. 0. 0.]
                      [1. 0. 0. 0.]]
                     [[1. 0. 0. 0.]
                      [1. 0. 0. 0.]]
                     [[1. 0. 0. 0.]
                      [1. 0. 0. 0.]]]
                
        """
    def get_body_disable_gravity(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get whether the rigid bodies of articulations in the view have gravity disabled or not
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: rigid body gravity activation of articulations in the view.
                    Shape is (M, K).
        
                
        """
    def get_body_index(self, body_name: str) -> int:
        """
        Get a ridig body (link) index in the articulation view given its name
        
                Args:
                    body_name (str): name of the ridig body to query
        
                Returns:
                    int: index of the rigid body in the articulation buffers
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the index of the left finger: panda_leftfinger
                    >>> prims.get_body_index("panda_leftfinger")
                    10
                
        """
    def get_body_inertias(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get rigid body inertias of articulations in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: rigid body inertias of articulations in the view. Shape is (M, K, 9).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all body inertias. Returned shape is (5, 12, 9) for the example: 5 envs, 12 rigid bodies
                    >>> prims.get_body_inertias()
                    [[[1.2988697e-06  0.0  0.0  0.0  1.6535528e-06  0.0  0.0  0.0  2.0331163e-06]
                      [1.8686389e-06  0.0  0.0  0.0  1.4378986e-06  0.0  0.0  0.0  9.0681192e-07]
                      ...
                      [4.2041304e-10  0.0  0.0  0.0  3.9026365e-10  0.0  0.0  0.0  1.3347495e-10]
                      [4.2041304e-10  0.0  0.0  0.0  3.9026365e-10  0.0  0.0  0.0  1.3347495e-10]]]
                    >>>
                    >>> # get finger body inertias: panda_leftfinger (10) and panda_rightfinger (11)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2, 9)
                    >>> prims.get_body_inertias(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
                    [[[4.2041304e-10  0.0  0.0  0.0  3.9026365e-10  0.0  0.0  0.0  1.3347495e-10]
                      [4.2041304e-10  0.0  0.0  0.0  3.9026365e-10  0.0  0.0  0.0  1.3347495e-10]]
                     ...
                     [[4.2041304e-10  0.0  0.0  0.0  3.9026365e-10  0.0  0.0  0.0  1.3347495e-10]
                      [4.2041304e-10  0.0  0.0  0.0  3.9026365e-10  0.0  0.0  0.0  1.3347495e-10]]]
                
        """
    def get_body_inv_inertias(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get rigid body inverse inertias of articulations in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: rigid body inverse inertias of articulations in the view.
                    Shape is (M, K, 9).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all body inverse inertias. Returned shape is (5, 12, 9) for the example: 5 envs, 12 rigid bodies
                    >>> prims.get_body_inv_inertias()
                    [[[7.6990012e+05  0.0  0.0  0.0  6.0475844e+05  0.0  0.0  0.0  4.9185578e+05]
                      [5.3514888e+05  0.0  0.0  0.0  6.9545931e+05  0.0  0.0  0.0  1.1027645e+06]
                      ...
                      [2.3786132e+09  0.0  0.0  0.0  2.5623703e+09  0.0  0.0  0.0  7.4920422e+09]
                      [2.3786132e+09  0.0  0.0  0.0  2.5623703e+09  0.0  0.0  0.0  7.4920422e+09]]]
                    >>>
                    >>> # get finger body inverse inertias: panda_leftfinger (10) and panda_rightfinger (11)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2, 9)
                    >>> prims.get_body_inv_inertias(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
                    [[[2.3786132e+09  0.0  0.0  0.0  2.5623703e+09  0.0  0.0  0.0  7.4920422e+09]
                      [2.3786132e+09  0.0  0.0  0.0  2.5623703e+09  0.0  0.0  0.0  7.4920422e+09]]
                     ...
                     [[2.3786132e+09  0.0  0.0  0.0  2.5623703e+09  0.0  0.0  0.0  7.4920422e+09]
                      [2.3786132e+09  0.0  0.0  0.0  2.5623703e+09  0.0  0.0  0.0  7.4920422e+09]]]
                
        """
    def get_body_inv_masses(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get rigid body inverse masses of articulations in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: rigid body inverse masses of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all body inverse masses. Returned shape is (5, 12) for the example: 5 envs, 12 rigid bodies
                    >>> prims.get_body_inv_masses()
                    [[ 0.35534042  0.42372888  0.42025304  0.37737525  0.3710848  0.33542618  0.8860687
                       2.4673615  10. 1.7910539  71.14793  71.14793]
                     [ 0.35534042  0.42372888  0.42025304  0.37737525  0.3710848  0.33542618  0.8860687
                       2.4673615  10. 1.7910539  71.14793  71.14793]
                     [ 0.35534042  0.42372888  0.42025304  0.37737525  0.3710848  0.33542618  0.8860687
                       2.4673615  10. 1.7910539  71.14793  71.14793]
                     [ 0.35534042  0.42372888  0.42025304  0.37737525  0.3710848  0.33542618  0.8860687
                       2.4673615  10. 1.7910539  71.14793  71.14793]
                     [ 0.35534042  0.42372888  0.42025304  0.37737525  0.3710848  0.33542618  0.8860687
                       2.4673615  10. 1.7910539  71.14793  71.14793]]
                    >>>
                    >>> # get finger body inverse masses: panda_leftfinger (10) and panda_rightfinger (11)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_body_inv_masses(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
                    [[71.14793 71.14793]
                     [71.14793 71.14793]
                     [71.14793 71.14793]]
                
        """
    def get_body_masses(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get rigid body masses of articulations in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: rigid body masses of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all body masses. Returned shape is (5, 12) for the example: 5 envs, 12 rigid bodies
                    >>> prims.get_body_masses()
                    [[2.8142028  2.3599997  2.3795187  2.6498823  2.6948018  2.981282
                      1.1285807  0.40529126 0.1  0.5583305  0.01405522 0.01405522]
                     [2.8142028  2.3599997  2.3795187  2.6498823  2.6948018  2.981282
                      1.1285807  0.40529126 0.1  0.5583305  0.01405522 0.01405522]
                     [2.8142028  2.3599997  2.3795187  2.6498823  2.6948018  2.981282
                      1.1285807  0.40529126 0.1  0.5583305  0.01405522 0.01405522]
                     [2.8142028  2.3599997  2.3795187  2.6498823  2.6948018  2.981282
                      1.1285807  0.40529126 0.1  0.5583305  0.01405522 0.01405522]
                     [2.8142028  2.3599997  2.3795187  2.6498823  2.6948018  2.981282
                      1.1285807  0.40529126 0.1  0.5583305  0.01405522 0.01405522]]
                    >>>
                    >>> # get finger body masses: panda_leftfinger (10) and panda_rightfinger (11)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_body_masses(indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
                    [[0.01405522 0.01405522]
                     [0.01405522 0.01405522]
                     [0.01405522 0.01405522]]
                
        """
    def get_coriolis_and_centrifugal_forces(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the Coriolis and centrifugal forces (joint DOF forces required to counteract Coriolis and
                centrifugal forces for the given articulation state) of articulations in the view
        
                Search for *Coriolis and Centrifugal Forces* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs for fixed-based arituclations and K <= num of dofs + 6 for floating-based articulations.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: Coriolis and centrifugal forces of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all coriolis and centrifugal forces. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs for a fixed-based articulation
                    >>> prims.get_coriolis_and_centrifugal_forces()
                    [[ 1.6842524e-06 -1.8269569e-04  5.2162073e-07 -9.7677548e-05  3.0365106e-07
                       6.7375149e-06  6.1105780e-08 -4.6237556e-06 -4.1627968e-06]
                     [ 1.6842524e-06 -1.8269569e-04  5.2162073e-07 -9.7677548e-05  3.0365106e-07
                       6.7375149e-06  6.1105780e-08 -4.6237556e-06 -4.1627968e-06]
                     [ 1.6842561e-06 -1.8269687e-04  5.2162375e-07 -9.7677454e-05  3.0365084e-07
                       6.7375931e-06  6.1106007e-08 -4.6237533e-06 -4.1627954e-06]
                     [ 1.6842561e-06 -1.8269687e-04  5.2162375e-07 -9.7677454e-05  3.0365084e-07
                       6.7375931e-06  6.1106007e-08 -4.6237533e-06 -4.1627954e-06]
                     [ 1.6842524e-06 -1.8269569e-04  5.2162073e-07 -9.7677548e-05  3.0365106e-07
                       6.7375149e-06  6.1105780e-08 -4.6237556e-06 -4.1627968e-06]]
                    >>>
                    >>> # get finger joint coriolis and centrifugal forces: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_coriolis_and_centrifugal_forces(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    [[-4.6237556e-06 -4.1627968e-06]
                     [-4.6237533e-06 -4.1627954e-06]
                     [-4.6237556e-06 -4.1627968e-06]]
                
        """
    def get_dof_index(self, dof_name: str) -> int:
        """
        Get a DOF index in the joint buffers given its name
        
                Args:
                    dof_name (str): name of the joint that corresponds to the degree of freedom to query
        
                Returns:
                    int: index of the degree of freedom in the joint buffers
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the index of the left finger joint: panda_finger_joint1
                    >>> prims.get_dof_index("panda_finger_joint1")
                    7
                
        """
    def get_dof_limits(self) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Get the articulations DOFs limits (lower and upper)
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.array]: degrees of freedom position limits.
                    Shape is (N, num_dof, 2). For the last dimension, index 0 corresponds to lower limits and index 1 corresponds to upper limits
        
                Example:
        
                .. code-block:: python
        
                    >>> # get DOF limits. Returned shape is (5, 9, 2) for the example: 5 envs, 9 DOFs
                    >>> prims.get_dof_limits()
                    [[[-2.8973  2.8973]
                     [-1.7628  1.7628]
                     [-2.8973  2.8973]
                     [-3.0718 -0.0698]
                     [-2.8973  2.8973]
                     [-0.0175  3.7525]
                     [-2.8973  2.8973]
                     [ 0.      0.04  ]
                     [ 0.      0.04  ]]
                    ...
                    [[-2.8973  2.8973]
                     [-1.7628  1.7628]
                     [-2.8973  2.8973]
                     [-3.0718 -0.0698]
                     [-2.8973  2.8973]
                     [-0.0175  3.7525]
                     [-2.8973  2.8973]
                     [ 0.      0.04  ]
                     [ 0.      0.04  ]]]
                
        """
    def get_dof_types(self, dof_names: typing.List[str] = None) -> typing.List[str]:
        """
        Get the DOF types given the DOF names
        
                Args:
                    dof_names (List[str], optional): names of the joints that corresponds to the degrees of freedom to query. Defaults to None.
        
                Returns:
                    List[str]: types of the joints that corresponds to the degrees of freedom. Types can be invalid, translation or rotation.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all DOF types
                    >>> prims.get_dof_types()
                    [<DofType.Rotation: 0>, <DofType.Rotation: 0>, <DofType.Rotation: 0>,
                     <DofType.Rotation: 0>, <DofType.Rotation: 0>, <DofType.Rotation: 0>,
                     <DofType.Rotation: 0>, <DofType.Translation: 1>, <DofType.Translation: 1>]
                    >>>
                    >>> # get only the finger DOF types: panda_finger_joint1 and panda_finger_joint2
                    >>> prims.get_dof_types(dof_names=["panda_finger_joint1", "panda_finger_joint2"])
                    [<DofType.Translation: 1>, <DofType.Translation: 1>]
                
        """
    def get_drive_types(self) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Get the articulations DOFs limits (lower and upper)
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.array]: degrees of freedom position limits.
                    Shape is (N, num_dof). For the last dimension, index 0 corresponds to lower limits and index 1 corresponds to upper limits
        
                
        """
    def get_effort_modes(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> typing.List[str]:
        """
        Get effort modes for articulations in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                Returns:
                    List: Returns a List of size (M, K) indicating the effort modes: ``acceleration`` or ``force``
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the effort mode for all joints
                    >>> prims.get_effort_modes()
                    [['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration'],
                     ['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration'],
                     ['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration'],
                     ['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration'],
                     ['acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration', 'acceleration']]
                    >>>
                    >>> # get only the finger joints effort modes for the first, middle and last of the 5 envs
                    >>> prims.get_effort_modes(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    [['acceleration', 'acceleration'], ['acceleration', 'acceleration'], ['acceleration', 'acceleration']]
                
        """
    def get_enabled_self_collisions(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the enable self collisions flag (``physxArticulation:enabledSelfCollisions``) for all articulations
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: self collisions flags (boolean interpreted as int). shape (M,)
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all self collisions flags. Returned shape is (5,) for the example: 5 envs
                    >>> prims.get_enabled_self_collisions()
                    [0 0 0 0 0]
                    >>>
                    >>> # get the self collisions flags for the first, middle and last of the 5 envs. Returned shape is (3,)
                    >>> prims.get_enabled_self_collisions(indices=np.array([0, 2, 4]))
                    [0 0 0]
                
        """
    def get_fixed_tendon_dampings(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the dampings of fixed tendons for articulations in the view
        
                Search for *Fixed Tendon* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: fixed tendon dampings of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the fixed tendon dampings
                    >>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
                    >>> prims.get_fixed_tendon_dampings()
                    [[0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]]
                
        """
    def get_fixed_tendon_limit_stiffnesses(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the limit stiffness of fixed tendons for articulations in the view
        
                Search for *Fixed Tendon* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: fixed tendon stiffnesses of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the fixed tendon limit stiffnesses
                    >>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
                    >>> prims.get_fixed_tendon_limit_stiffnesses()
                    [[0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]]
                
        """
    def get_fixed_tendon_limits(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the limits of fixed tendons for articulations in the view
        
                Search for *Fixed Tendon* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: fixed tendon stiffnesses of articulations in the view.
                    Shape is (M, K, 2).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the fixed tendon limits
                    >>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
                    >>> prims.get_fixed_tendon_limits()
                    [[[-0.001  0.001] [-0.001  0.001] [-0.001  0.001] [-0.001  0.001]]
                     [[-0.001  0.001] [-0.001  0.001] [-0.001  0.001] [-0.001  0.001]]
                     [[-0.001  0.001] [-0.001  0.001] [-0.001  0.001] [-0.001  0.001]]
                     [[-0.001  0.001] [-0.001  0.001] [-0.001  0.001] [-0.001  0.001]]
                     [[-0.001  0.001] [-0.001  0.001] [-0.001  0.001] [-0.001  0.001]]]
                
        """
    def get_fixed_tendon_offsets(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the offsets of fixed tendons for articulations in the view
        
                Search for *Fixed Tendon* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: fixed tendon stiffnesses of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the fixed tendon offsets
                    >>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
                    >>> prims.get_fixed_tendon_offsets()
                    [[0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]]
                
        """
    def get_fixed_tendon_rest_lengths(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the rest length of fixed tendons for articulations in the view
        
                Search for *Fixed Tendon* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: fixed tendon stiffnesses of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the fixed tendon rest lengths
                    >>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
                    >>> prims.get_fixed_tendon_rest_lengths()
                    [[0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]]
                
        """
    def get_fixed_tendon_stiffnesses(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the stiffness of fixed tendons for articulations in the view
        
                Search for *Fixed Tendon* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: fixed tendon stiffnesses of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the fixed tendon stiffnesses
                    >>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
                    >>> prims.get_fixed_tendon_stiffnesses()
                    [[0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]
                     [0. 0. 0. 0.]]
                
        """
    def get_friction_coefficients(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.array]:
        """
        Get the friction coefficients for the articulation joints in the view
        
                Search for *"Joint Friction Coefficient"* in |physx_docs| for more details.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                    clone (Optional[bool]): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: joint friction coefficients for articulations in the view. shape (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get joint friction coefficients. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> prims.get_friction_coefficients()
                    [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]]
                    >>>
                    >>> # get only the finger joint (panda_finger_joint1 (7) and panda_finger_joint2 (8)) friction coefficients
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_friction_coefficients(indices=np.array([0,2,4]), joint_indices=np.array([7,8]))
                    [[0. 0.]
                     [0. 0.]
                     [0. 0.]]
                
        """
    def get_gains(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Tuple[typing.Union[numpy.ndarray, torch.Tensor], typing.Union[numpy.ndarray, torch.Tensor], typing.Union[warp.types.indexedarray, <Function index(a: vector(length=2, dtype=<class 'warp.types.float16'>), i: int32)>]]:
        """
        Get the implicit Proportional-Derivative (PD) controller's Kps (stiffnesses) and Kds (dampings) of articulations in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                    clone (bool, optional): True to return clones of the internal buffers. Otherwise False. Defaults to True.
        
                Returns:
                    Tuple[Union[np.ndarray, torch.Tensor], Union[np.ndarray, torch.Tensor], Union[wp.indexedarray, wp.index]]:
                    stiffness and damping of articulations in the view respectively. shapes are (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all joint stiffness and damping. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> stiffnesses, dampings = prims.get_gains()
                    >>> stiffnesses
                    [[60000. 60000. 60000. 60000. 25000. 15000.  5000.  6000.  6000.]
                     [60000. 60000. 60000. 60000. 25000. 15000.  5000.  6000.  6000.]
                     [60000. 60000. 60000. 60000. 25000. 15000.  5000.  6000.  6000.]
                     [60000. 60000. 60000. 60000. 25000. 15000.  5000.  6000.  6000.]
                     [60000. 60000. 60000. 60000. 25000. 15000.  5000.  6000.  6000.]]
                    >>> dampings
                    [[3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]
                     [3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]
                     [3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]
                     [3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]
                     [3000. 3000. 3000. 3000. 3000. 3000. 3000. 1000. 1000.]]
                    >>>
                    >>> # get finger joints stiffness and damping: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> stiffnesses, dampings = prims.get_gains(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    >>> stiffnesses
                    [[6000. 6000.]
                     [6000. 6000.]
                     [6000. 6000.]]
                    >>> dampings
                    [[1000. 1000.]
                     [1000. 1000.]
                     [1000. 1000.]]
                
        """
    def get_generalized_gravity_forces(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the generalized gravity forces (joint DOF forces required to counteract gravitational
                forces for the given articulation pose) of articulations in the view
        
                Search for *Generalized Gravity Force* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs for fixed-based arituclations and K <= num of dofs + 6 for floating-based articulations.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: generalized gravity forces of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>>
        
                    >>> # get all generalized gravity forces. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> prims.get_generalized_gravity_forces()
                    [[ 1.32438602e-08 -6.90832138e+00 -1.08629465e-05  1.91585541e+01  5.13810664e-06
                       1.18674076e+00  8.01788883e-06  5.18786255e-03 -5.18784765e-03]
                     [ 1.32438602e-08 -6.90832138e+00 -1.08629465e-05  1.91585541e+01  5.13810664e-06
                       1.18674076e+00  8.01788883e-06  5.18786255e-03 -5.18784765e-03]
                     [ 1.32438585e-08 -6.90830994e+00 -1.08778477e-05  1.91585541e+01  5.14090061e-06
                       1.18674052e+00  8.02161412e-06  5.18786255e-03 -5.18784765e-03]
                     [ 1.32438585e-08 -6.90830994e+00 -1.08778477e-05  1.91585541e+01  5.14090061e-06
                       1.18674052e+00  8.02161412e-06  5.18786255e-03 -5.18784765e-03]
                     [ 1.32438602e-08 -6.90832138e+00 -1.08629465e-05  1.91585541e+01  5.13810664e-06
                       1.18674076e+00  8.01788883e-06  5.18786255e-03 -5.18784765e-03]]
                    >>>
                    >>> # get finger joint generalized gravity forces: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_generalized_gravity_forces(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    [[ 0.00518786 -0.00518785]
                     [ 0.00518786 -0.00518785]
                     [ 0.00518786 -0.00518785]]
                
        """
    def get_jacobian_shape(self) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.array]:
        """
        Get the Jacobian matrix shape of a single articulation
        
                The Jacobian matrix maps the joint space velocities of a DOF to it's cartesian and angular velocities
        
                The shape of the Jacobian depends on the number of links (rigid bodies), DOFs,
                and whether the articulation base is fixed (e.g., robotic manipulators) or not (e.g,. mobile robots).
        
                * Fixed articulation base: ``(num_bodies - 1, 6, num_dof)``
                * Non-fixed articulation base: ``(num_bodies, 6, num_dof + 6)``
        
                Each body has 6 values in the Jacobian representing its linear and angular motion along the
                three coordinate axes. The extra 6 DOFs in the last dimension, for non-fixed base cases,
                correspond to the linear and angular degrees of freedom of the free root link
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.array]: shape of jacobian for a single articulation.
        
                Example:
        
                .. code-block:: python
        
                    >>> # for the Franka Panda (a robotic manipulator with fixed base):
                    >>> # - num_bodies: 12
                    >>> # - num_dof: 9
                    >>> prims.get_jacobian_shape()
                    (11, 6, 9)
                
        """
    def get_jacobians(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the Jacobian matrices of articulations in the view
        
                .. note::
        
                    The first dimension corresponds to the amount of wrapped articulations while the last 3 dimensions are the
                    Jacobian matrix shape. Refer to the ``get_jacobian_shape`` method for details about the Jacobian matrix shape
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: Jacobian matrices of articulations in the view.
                    Shape is (M, jacobian_shape).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the Jacobian matrices. Returned shape is (5, 11, 6, 9) for the example: 5 envs, 12 links, 9 DOFs
                    >>> prims.get_jacobians()
                    [[[[ 4.2254178e-09  0.0000000e+00  0.0000000e+00 ...  0.0000000e+00  0.0000000e+00  0.0000000e+00]
                       [ 1.2093576e-08  0.0000000e+00  0.0000000e+00 ...  0.0000000e+00  0.0000000e+00  0.0000000e+00]
                       [-6.0873992e-16  0.0000000e+00  0.0000000e+00 ...  0.0000000e+00  0.0000000e+00  0.0000000e+00]
                       [ 1.4458647e-07  0.0000000e+00  0.0000000e+00 ...  0.0000000e+00  0.0000000e+00  0.0000000e+00]
                       [-1.8178657e-10  0.0000000e+00  0.0000000e+00 ...  0.0000000e+00  0.0000000e+00  0.0000000e+00]
                       [ 9.9999976e-01  0.0000000e+00  0.0000000e+00 ...  0.0000000e+00  0.0000000e+00  0.0000000e+00]]
                      ...
                      [[-4.5089945e-02  8.1210062e-02 -3.8495898e-02 ...  2.8108317e-02  0.0000000e+00 -4.9317405e-02]
                       [ 4.2863289e-01  9.7436900e-04  4.0475106e-01 ...  2.4577195e-03  0.0000000e+00  9.9807423e-01]
                       [ 6.5973169e-09 -4.2914307e-01 -2.1542320e-02 ...  2.8352857e-02  0.0000000e+00 -3.7625343e-02]
                       [ 1.4458647e-07 -1.1999309e-02 -5.3927803e-01 ...  7.0976764e-01  0.0000000e+00  0.0000000e+00]
                       [-1.8178657e-10  9.9992776e-01 -6.4710006e-03 ...  8.5178167e-03  0.0000000e+00  0.0000000e+00]
                       [ 9.9999976e-01 -3.8743019e-07  8.4210289e-01 ... -7.0438433e-01  0.0000000e+00  0.0000000e+00]]]]
                
        """
    def get_joint_index(self, joint_name: str) -> int:
        """
        Get a joint index in the joint buffers given its name
        
                Args:
                    joint_name (str): name of the joint that corresponds to the index of the joint in the articulation
        
                Returns:
                    int: index of the joint in the joint buffers
        
                
        """
    def get_joint_max_velocities(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the maximum joint velocities for articulation dofs in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                    clone (Optional[bool]): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: maximum joint velocities for articulations dofs in the view. shape (M, K).
                
        """
    def get_joint_positions(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the joint positions of articulations in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: joint positions of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all joint positions. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> prims.get_joint_positions()
                    [[ 1.1999921e-02 -5.6962633e-01  1.3219320e-08 -2.8105433e+00  6.8276213e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]
                     [ 1.1999921e-02 -5.6962633e-01  1.3219320e-08 -2.8105433e+00  6.8276213e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]
                     [ 1.1999921e-02 -5.6962633e-01  1.3220056e-08 -2.8105433e+00  6.8276104e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]
                     [ 1.1999921e-02 -5.6962633e-01  1.3220056e-08 -2.8105433e+00  6.8276104e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]
                     [ 1.1999921e-02 -5.6962633e-01  1.3219320e-08 -2.8105433e+00  6.8276213e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]]
                    >>>
                    >>> # get finger joint positions: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_joint_positions(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    [[0.03991237 0.04      ]
                     [0.03991237 0.04      ]
                     [0.03991237 0.04      ]]
                
        """
    def get_joint_velocities(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the joint velocities of articulations in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: joint velocities of articulations in the view.
                    Shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all joint velocities. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> prims.get_joint_velocities()
                    [[ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07  1.1063669e-02 -4.6333633e-05
                       3.4824573e-02  8.8469200e-02  5.4033857e-04  1.0287426e-05]
                     [ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07  1.1063669e-02 -4.6333633e-05
                       3.4824573e-02  8.8469200e-02  5.4033857e-04  1.0287426e-05]
                     [ 1.9010074e-06 -7.6763779e-03 -2.1403629e-07  1.1063648e-02 -4.6333400e-05
                       3.4824558e-02  8.8469170e-02  5.4033566e-04  1.0287110e-05]
                     [ 1.9010074e-06 -7.6763779e-03 -2.1403629e-07  1.1063648e-02 -4.6333400e-05
                       3.4824558e-02  8.8469170e-02  5.4033566e-04  1.0287110e-05]
                     [ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07  1.1063669e-02 -4.6333633e-05
                       3.4824573e-02  8.8469200e-02  5.4033857e-04  1.0287426e-05]]
                    >>>
                    >>> # get finger joint velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_joint_velocities(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    [[5.4033857e-04 1.0287426e-05]
                     [5.4033566e-04 1.0287110e-05]
                     [5.4033857e-04 1.0287426e-05]]
                
        """
    def get_joints_default_state(self) -> isaacsim.core.utils.types.JointsState:
        """
        Get the default joint states defined with the ``set_joints_default_state`` method
        
                Returns:
                    JointsState: an object that contains the default joint states
        
                Example:
        
                .. code-block:: python
        
                    >>> # returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> states = prims.get_joints_default_state()
                    >>> states
                    <isaacsim.core.utils.types.JointsState object at 0x7fc2c174fd90>
                    >>> states.positions
                    [[ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]
                     [ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]
                     [ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]
                     [ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]
                     [ 0.   -1.    0.   -2.2   0.    2.4   0.8   0.04  0.04]]
                    >>> states.velocities
                    [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]]
                    >>> states.efforts
                    [[0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0. 0. 0. 0.]]
                
        """
    def get_joints_state(self) -> isaacsim.core.utils.types.JointsState:
        """
        Get the current joint states (positions and velocities)
        
                Returns:
                    JointsState: an object that contains the current joint positions and velocities
        
                Example:
        
                .. code-block:: python
        
                    >>> # returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> states = prims.get_joints_state()
                    >>> states
                    <isaacsim.core.utils.types.JointsState object at 0x7fc1a23a82e0>
                    >>> states.positions
                    [[ 1.1999921e-02 -5.6962633e-01  1.3219320e-08 -2.8105433e+00  6.8276213e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]
                     [ 1.1999921e-02 -5.6962633e-01  1.3219320e-08 -2.8105433e+00  6.8276213e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]
                     [ 1.1999921e-02 -5.6962633e-01  1.3220056e-08 -2.8105433e+00  6.8276104e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]
                     [ 1.1999921e-02 -5.6962633e-01  1.3220056e-08 -2.8105433e+00  6.8276104e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]
                     [ 1.1999921e-02 -5.6962633e-01  1.3219320e-08 -2.8105433e+00  6.8276213e-06
                       3.0301569e+00  7.3234755e-01  3.9912373e-02  3.9999999e-02]]
                    >>> states.velocities
                    [[ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07  1.1063669e-02 -4.6333633e-05
                       3.4824573e-02  8.8469200e-02  5.4033857e-04  1.0287426e-05]
                     [ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07  1.1063669e-02 -4.6333633e-05
                       3.4824573e-02  8.8469200e-02  5.4033857e-04  1.0287426e-05]
                     [ 1.9010074e-06 -7.6763779e-03 -2.1403629e-07  1.1063648e-02 -4.6333400e-05
                       3.4824558e-02  8.8469170e-02  5.4033566e-04  1.0287110e-05]
                     [ 1.9010074e-06 -7.6763779e-03 -2.1403629e-07  1.1063648e-02 -4.6333400e-05
                       3.4824558e-02  8.8469170e-02  5.4033566e-04  1.0287110e-05]
                     [ 1.9010375e-06 -7.6763844e-03 -2.1396865e-07  1.1063669e-02 -4.6333633e-05
                       3.4824573e-02  8.8469200e-02  5.4033857e-04  1.0287426e-05]]
                
        """
    def get_linear_velocities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, clone = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the linear velocities of prims in the view.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: linear velocities of the prims in the view. shape is (M, 3).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all articulation linear velocities. Returned shape is (5, 3) for the example: 5 envs, linear (3)
                    >>> prims.get_linear_velocities()
                    [[0. 0. 0.]
                     [0. 0. 0.]
                     [0. 0. 0.]
                     [0. 0. 0.]
                     [0. 0. 0.]]
                    >>>
                    >>> # get only the articulation linear velocities for the first, middle and last of the 5 envs.
                    >>> # Returned shape is (3, 3) for the example: 3 envs selected, linear (3)
                    >>> prims.get_linear_velocities(indices=np.array([0, 2, 4]))
                    [[0. 0. 0.]
                     [0. 0. 0.]
                     [0. 0. 0.]]
                
        """
    def get_link_index(self, link_name: str) -> int:
        """
        Get a link index in the link buffers given its name
        
                Args:
                    link_name (str): name of the link that corresponds to the index of the link in the articulation
        
                Returns:
                    int: index of the link in the link buffers
        
                
        """
    def get_local_poses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[typing.Tuple[numpy.ndarray, numpy.ndarray], typing.Tuple[torch.Tensor, torch.Tensor], typing.Tuple[warp.types.indexedarray, warp.types.indexedarray]]:
        """
        Get prim poses in the view with respect to the local frame (the prim's parent frame).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]:
                    first index is positions in the local frame of the prims. shape is (M, 3). Second index is quaternion orientations
                    in the local frame of the prims. Quaternion is scalar-first (w, x, y, z). shape is (M, 4).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all articulation poses with respect to the local frame.
                    >>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
                    >>> positions, orientations = prims.get_local_poses()
                    >>> positions
                    [[ 0.0000000e+00  0.0000000e+00 -2.8610229e-08]
                     [ 0.0000000e+00  0.0000000e+00 -2.8610229e-08]
                     [-4.5299529e-08  0.0000000e+00 -2.8610229e-08]
                     [-4.5299529e-08  0.0000000e+00 -2.8610229e-08]
                     [ 0.0000000e+00  0.0000000e+00 -2.8610229e-08]]
                    >>> orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                    >>>
                    >>> # get only the articulation poses with respect to the local frame for the first, middle and last of the 5 envs.
                    >>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
                    >>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
                    >>> positions
                    [[ 0.0000000e+00  0.0000000e+00 -2.8610229e-08]
                     [-4.5299529e-08  0.0000000e+00 -2.8610229e-08]
                     [ 0.0000000e+00  0.0000000e+00 -2.8610229e-08]]
                    >>> orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                
        """
    def get_mass_matrices(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the mass matrices of articulations in the view
        
                .. note::
        
                    The first dimension corresponds to the amount of wrapped articulations while the last 2 dimensions are the
                    mass matrix shape. Refer to the ``get_mass_matrix_shape`` method for details about the mass matrix shape
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: mass matrices of articulations in the view.
                    Shape is (M, mass_matrix_shape).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the mass matrices. Returned shape is (5, 9, 9) for the example: 5 envs, 9 DOFs for a fixed-based articulation
                    >>> prims.get_mass_matrices()
                    [[[ 5.0900602e-01  1.1794259e-06  4.2570841e-01 -1.6387942e-06 -3.1573933e-02
                       -1.9736715e-06 -3.1358242e-04 -6.0441834e-03  6.0441834e-03]
                      [ 1.1794259e-06  1.0598221e+00  7.4729815e-07 -4.2621672e-01  2.3612277e-08
                       -4.9647894e-02 -2.9080724e-07 -1.8432185e-04  1.8432130e-04]
                      ...
                      [-6.0441834e-03 -1.8432185e-04 -5.7159867e-03  4.0070520e-04  9.6930371e-04
                        1.2324301e-04  2.5264668e-10  1.4055224e-02  0.0000000e+00]
                      [ 6.0441834e-03  1.8432130e-04  5.7159867e-03 -4.0070404e-04 -9.6930366e-04
                       -1.2324269e-04 -3.6906206e-10  0.0000000e+00  1.4055224e-02]]]
                
        """
    def get_mass_matrix_shape(self) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.array]:
        """
        Get the mass matrix shape of a single articulation
        
                The mass matrix contains the generalized mass of the robot depending on the current configuration
        
                The shape of the max matrix depends on the number of DOFs as well as whether the articulation is fixed-base or floating-base.
                For fixed-base articulation the shape is ``(num_dof, num_dof)`` while for floating-base articulation the shape is ``(num_dof + 6, num_dof + 6)``
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.array]: shape of mass matrix for a single articulation.
        
                Example:
        
                .. code-block:: python
        
                    >>> # for the Franka Panda:
                    >>> # - num_dof: 9
                    >>> prims.get_mass_matrix_shape()
                    (9, 9)
                    >>> # for Ant robot:
                    >>> # - num_dof: 8
                    >>> prims.get_mass_matrix_shape()
                        (14, 14)
                
        """
    def get_max_efforts(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the maximum efforts for articulation in the view
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                    clone (Optional[bool]): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: maximum efforts for articulations in the view. shape (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all joint maximum efforts. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> prims.get_max_efforts()
                    [[5220. 5220. 5220. 5220.  720.  720.  720.  720.  720.]
                     [5220. 5220. 5220. 5220.  720.  720.  720.  720.  720.]
                     [5220. 5220. 5220. 5220.  720.  720.  720.  720.  720.]
                     [5220. 5220. 5220. 5220.  720.  720.  720.  720.  720.]
                     [5220. 5220. 5220. 5220.  720.  720.  720.  720.  720.]]
                    >>>
                    >>> # get finger joint maximum efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_max_efforts(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    [[720. 720.]
                     [720. 720.]
                     [720. 720.]]
                
        """
    def get_measured_joint_efforts(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Returns the efforts computed/measured by the physics solver of the joint forces in the DOF motion direction
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): joint indices to specify which joints
                                                                                         to query. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: computed joint efforts of articulations in the view. shape is (M, K).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all measured joint efforts. Returned shape is (5, 9) for the example: 5 envs, 9 DOFs
                    >>> prims.get_measured_joint_efforts()
                    [[ 4.8250298e-05 -6.9073005e+00  5.3364405e-05  1.9157070e+01 -5.8759182e-05
                       1.1863427e+00 -5.6388220e-05  5.1680300e-03 -5.1910817e-03]
                     [ 4.8250298e-05 -6.9073005e+00  5.3364405e-05  1.9157070e+01 -5.8759182e-05
                       1.1863427e+00 -5.6388220e-05  5.1680300e-03 -5.1910817e-03]
                     [ 4.8254540e-05 -6.9072919e+00  5.3344327e-05  1.9157072e+01 -5.8761045e-05
                       1.1863427e+00 -5.6405144e-05  5.1680212e-03 -5.1910840e-03]
                     [ 4.8254540e-05 -6.9072919e+00  5.3344327e-05  1.9157072e+01 -5.8761045e-05
                       1.1863427e+00 -5.6405144e-05  5.1680212e-03 -5.1910840e-03]
                     [ 4.8250298e-05 -6.9073005e+00  5.3364405e-05  1.9157070e+01 -5.8759182e-05
                       1.1863427e+00 -5.6388220e-05  5.1680300e-03  -5.1910817e-03]]
                    >>>
                    >>> # get finger measured joint efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs. Returned shape is (3, 2)
                    >>> prims.get_measured_joint_efforts(indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                    [[ 0.00516803 -0.00519108]
                     [ 0.00516802 -0.00519108]
                     [ 0.00516803 -0.00519108]]
                
        """
    def get_measured_joint_forces(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        Get the measured joint reaction forces and torques (link incoming joint forces and torques) to external loads
        
                .. note::
        
                    Since the *name->index* map for joints has not been exposed yet,
                    it is possible to access the joint names and their indices through the articulation metadata.
        
                    .. code-block:: python
        
                        prims._metadata.joint_names  # list of names
                        prims._metadata.joint_indices  # dict of name: index
        
                    To retrieve a specific row for the link incoming joint force/torque use ``joint_index + 1``
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor]], optional): link indices to specify which link's incoming joints to query. Shape (K,).
                                                                                            Where K <= num of links/bodies.
                                                                                            Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: joint forces and torques of articulations in the view.
                    Shape is (M, num_joint + 1, 6). Column index 0 is the incoming joint of the base link.
                    For the last dimension the first 3 values are for forces and the last 3 for torques
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all measured joint forces and torques. Returned shape is (5, 12, 6) for the example:
                    >>> # 5 envs, 9 DOFs (but 12 joints including the fixed and root joints)
                    >>> prims.get_measured_joint_forces()
                    [[[ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00]
                      [ 1.49950760e+02  3.52353277e-06  5.62586996e-04  4.82502983e-05 -6.90729856e+00  2.69259126e-05]
                      [-2.60467059e-05 -1.06778236e+02 -6.83844986e+01 -6.90730047e+00 -5.27759657e-05 -1.24897576e-06]
                      [ 8.71209946e+01 -4.46646191e-05 -5.57951622e+01  5.33644052e-05 -2.45385647e+01  1.38957939e-05]
                      [ 5.18576926e-05 -4.81099091e+01  6.07092705e+01  1.91570702e+01 -5.81023924e-05  1.46875891e-06]
                      [-3.16910419e+01  2.31799815e-04  3.99901695e+01 -5.87591821e-05 -1.18634319e+00  2.24427877e-05]
                      [-1.07621672e-04  1.53405371e+01 -1.54584875e+01  1.18634272e+00  6.09036942e-05 -1.60679410e-05]
                      [-7.54189777e+00 -5.08146524e+00 -5.65130091e+00 -5.63882204e-05  3.88599992e-01 -3.49432468e-01]
                      [ 4.74214745e+00 -3.19458222e+00  3.55281782e+00  5.58562024e-05  8.47946014e-03  7.64050474e-03]
                      [ 4.07607269e+00  2.16406956e-01 -4.05131817e+00 -5.95658377e-04  1.14070829e-02  2.13965313e-06]
                      [ 5.16803004e-03 -9.77545828e-02 -9.70939621e-02 -8.41282599e-12 -1.29066744e-12 -1.93477560e-11]
                      [-5.19108167e-03  9.75882635e-02 -9.71064270e-02  8.41282859e-12  1.29066018e-12 -1.93477543e-11]]
                     ...
                     [[ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00]
                      [ 1.49950760e+02  3.52353277e-06  5.62586996e-04  4.82502983e-05 -6.90729856e+00  2.69259126e-05]
                      [-2.60467059e-05 -1.06778236e+02 -6.83844986e+01 -6.90730047e+00 -5.27759657e-05 -1.24897576e-06]
                      [ 8.71209946e+01 -4.46646191e-05 -5.57951622e+01  5.33644052e-05 -2.45385647e+01  1.38957939e-05]
                      [ 5.18576926e-05 -4.81099091e+01  6.07092705e+01  1.91570702e+01 -5.81023924e-05  1.46875891e-06]
                      [-3.16910419e+01  2.31799815e-04  3.99901695e+01 -5.87591821e-05 -1.18634319e+00  2.24427877e-05]
                      [-1.07621672e-04  1.53405371e+01 -1.54584875e+01  1.18634272e+00  6.09036942e-05 -1.60679410e-05]
                      [-7.54189777e+00 -5.08146524e+00 -5.65130091e+00 -5.63882204e-05  3.88599992e-01 -3.49432468e-01]
                      [ 4.74214745e+00 -3.19458222e+00  3.55281782e+00  5.58562024e-05  8.47946014e-03  7.64050474e-03]
                      [ 4.07607269e+00  2.16406956e-01 -4.05131817e+00 -5.95658377e-04  1.14070829e-02  2.13965313e-06]
                      [ 5.16803004e-03 -9.77545828e-02 -9.70939621e-02 -8.41282599e-12 -1.29066744e-12 -1.93477560e-11]
                      [-5.19108167e-03  9.75882635e-02 -9.71064270e-02  8.41282859e-12  1.29066018e-12 -1.93477543e-11]]]
                    >>>
                    >>> # get measured joint forces and torques for the fingers for the first, middle and last of the 5 envs.
                    >>> # Returned shape is (3, 2, 6)
                    >>> metadata = prims._metadata
                    >>> joint_indices = 1 + np.array([
                    >>>     metadata.joint_indices["panda_finger_joint1"],
                    >>>     metadata.joint_indices["panda_finger_joint2"],
                    >>> ])
                    >>> joint_indices
                    [10 11]
                    >>> prims.get_measured_joint_forces(indices=np.array([0, 2, 4]), joint_indices=joint_indices)
                    [[[ 5.1680300e-03 -9.7754583e-02 -9.7093962e-02 -8.4128260e-12 -1.2906674e-12 -1.9347756e-11]
                      [-5.1910817e-03  9.7588263e-02 -9.7106427e-02  8.4128286e-12  1.2906602e-12 -1.9347754e-11]]
                     [[ 5.1680212e-03 -9.7754560e-02 -9.7093947e-02 -8.4141834e-12 -1.2907383e-12 -1.9348209e-11]
                      [-5.1910840e-03  9.7588278e-02 -9.7106412e-02  8.4141869e-12  1.2907335e-12 -1.9348207e-11]]
                     [[ 5.1680300e-03 -9.7754583e-02 -9.7093962e-02 -8.4128260e-12 -1.2906674e-12 -1.9347756e-11]
                      [-5.1910817e-03  9.7588263e-02 -9.7106427e-02  8.4128286e-12  1.2906602e-12 -1.9347754e-11]]]
                
        """
    def get_position_residuals(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, report_max: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get physics solver position residuals for articulations. This is the residual across all joints that are part of articulations.
                    The solver residuals are computed according to impulse variation normalized by the effective mass.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    report_max (Optional[bool]): whether to report max or RMS residual. Defaults to True, i.e. max criteria
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: Solver residuals for rigid bodies of the view
        
                
        """
    def get_sleep_thresholds(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the threshold for articulations to enter a sleep state
        
                Search for *Articulations and Sleeping* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: sleep thresholds. shape (M,).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all sleep thresholds. Returned shape is (5,) for the example: 5 envs
                    >>> prims.get_sleep_thresholds()
                    [0.005 0.005 0.005 0.005 0.005]
                    >>>
                    >>> # get the sleep thresholds for the first, middle and last of the 5 envs. Returned shape is (3,)
                    >>> prims.get_sleep_thresholds(indices=np.array([0, 2, 4]))
                    [0.005 0.005 0.005]
                
        """
    def get_solver_position_iteration_counts(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the solver (position) iteration count for the articulations
        
                The solver iteration count determines how accurately contacts, drives, and limits are resolved.
                Search for *Solver Iteration Count* in |physx_docs| for more details.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: position iteration count. Shape (M,).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all position iteration count. Returned shape is (5,) for the example: 5 envs
                    >>> prims.get_solver_position_iteration_counts()
                    [32 32 32 32 32]
                    >>>
                    >>> # get the position iteration count for the first, middle and last of the 5 envs. Returned shape is (3,)
                    >>> prims.get_solver_position_iteration_counts(indices=np.array([0, 2, 4]))
                    [32 32 32]
                
        """
    def get_solver_velocity_iteration_counts(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the solver (velocity) iteration count for the articulations
        
                The solver iteration count determines how accurately contacts, drives, and limits are resolved.
                Search for *Solver Iteration Count* in |physx_docs| for more details.
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: velocity iteration count. Shape (M,).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all velocity iteration count. Returned shape is (5,) for the example: 5 envs
                    >>> prims.get_solver_velocity_iteration_counts()
                    [32 32 32 32 32]
                    >>>
                    >>> # get the velocity iteration count for the first, middle and last of the 5 envs. Returned shape is (3,)
                    >>> prims.get_solver_velocity_iteration_counts(indices=np.array([0, 2, 4]))
                    [32 32 32]
                
        """
    def get_stabilization_thresholds(self, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the mass-normalized kinetic energy below which the articulations may participate in stabilization
        
                Search for *Stabilization Threshold* in |physx_docs| for more details
        
                Args:
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: stabilization threshold. Shape (M,).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all stabilization thresholds. Returned shape is (5,) for the example: 5 envs
                    >>> prims.get_solver_velocity_iteration_counts()
                    [0.001 0.001 0.001 0.001 0.001]
                    >>>
                    >>> # get the stabilization thresholds for the first, middle and last of the 5 envs. Returned shape is (3,)
                    >>> prims.get_solver_velocity_iteration_counts(indices=np.array([0, 2, 4]))
                    [0.001 0.001 0.001]
                
        """
    def get_velocities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get the linear and angular velocities of prims in the view.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: linear and angular velocities of the prims in the view concatenated. shape is (M, 6).
                    For the last dimension the first 3 values are for linear velocities and the last 3 for angular velocities
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all articulation velocities. Returned shape is (5, 6) for the example: 5 envs, linear (3) and angular (3)
                    >>> prims.get_velocities()
                    [[0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0.]]
                    >>>
                    >>> # get only the articulation velocities for the first, middle and last of the 5 envs.
                    >>> # Returned shape is (3, 6) for the example: 3 envs selected, linear (3) and angular (3)
                    >>> prims.get_velocities(indices=np.array([0, 2, 4]))
                    [[0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0.]
                     [0. 0. 0. 0. 0. 0.]]
                
        """
    def get_velocity_residuals(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, report_max: bool = True) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get physics solver velocity residuals for articulations. This is the residual across all joints that are part of articulations.
                    The solver residuals are computed according to impulse variation normalized by the effective mass.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view)
                    report_max (Optional[bool]): whether to report max or RMS residual. Defaults to True, i.e. max criteria
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: Solver residuals for rigid bodies of the view
        
                
        """
    def get_world_poses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, clone: bool = True, usd: bool = True) -> typing.Union[typing.Tuple[numpy.ndarray, numpy.ndarray], typing.Tuple[torch.Tensor, torch.Tensor], typing.Tuple[warp.types.indexedarray, warp.types.indexedarray]]:
        """
        Get the poses of the prims in the view with respect to the world's frame.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    clone (bool, optional): True to return a clone of the internal buffer. Otherwise False. Defaults to True.
                    usd (bool, optional): True to query from usd. Otherwise False to query from Fabric data. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]:
                    first index is positions in the world frame of the prims. shape is (M, 3). Second index is quaternion orientations
                    in the world frame of the prims. Quaternion is scalar-first (w, x, y, z). shape is (M, 4).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all articulation poses with respect to the world's frame.
                    >>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
                    >>> positions, orientations = prims.get_world_poses()
                    >>> positions
                    [[ 1.5000000e+00 -7.5000000e-01 -2.8610229e-08]
                     [ 1.5000000e+00  7.5000000e-01 -2.8610229e-08]
                     [-4.5299529e-08 -7.5000000e-01 -2.8610229e-08]
                     [-4.5299529e-08  7.5000000e-01 -2.8610229e-08]
                     [-1.5000000e+00 -7.5000000e-01 -2.8610229e-08]]
                    >>> orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                    >>>
                    >>> # get only the articulation poses with respect to the world's frame for the first, middle and last of the 5 envs.
                    >>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
                    >>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
                    >>> positions
                    [[ 1.5000000e+00 -7.5000000e-01 -2.8610229e-08]
                     [-4.5299529e-08 -7.5000000e-01 -2.8610229e-08]
                     [-1.5000000e+00 -7.5000000e-01 -2.8610229e-08]]
                    >>> orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and set other properties using the PhysX tensor API
        
                .. note::
        
                    For this particular class, calling this method will do nothing
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.initialize()
                
        """
    def is_physics_handle_valid(self) -> bool:
        """
        Check if articulation view's physics handler is initialized
        
                .. warning::
        
                    If the physics handler is not valid many of the methods that requires PhysX will return None.
        
                Returns:
                    bool: False if .initialize() needs to be called again for the physics handle to be valid. Otherwise True
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.is_physics_handle_valid()
                    True
                
        """
    def pause_motion(self) -> None:
        """
        
                Pauses the motion of all articulations wrapped under the Articulation.
                
        """
    def resume_motion(self):
        """
        
                Resumes the motion of all articulations wrapped under the Articulation using the position and velocity dof targets
                cached when pause_motion was called.
                
        """
    def set_angular_velocities(self, velocities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the angular velocities of the prims in the view
        
                The method does this through the physx API only. It has to be called after initialization.
                Note: This method is not supported for the gpu pipeline. ``set_velocities`` method should be used instead.
        
                .. warning::
        
                    This method will immediately set the articulation state
        
                Args:
                    velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): angular velocities to set the rigid prims to. shape is (M, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                .. hint::
        
                    This method belongs to the methods used to set the articulation kinematic state:
        
                    ``set_velocities`` (``set_linear_velocities``, ``set_angular_velocities``),
                    ``set_joint_positions``, ``set_joint_velocities``, ``set_joint_efforts``
        
                Example:
        
                .. code-block:: python
        
                    >>> # set each articulation linear velocity to (0.1, 0.1, 0.1)
                    >>> velocities = np.full((num_envs, 3), fill_value=0.1)
                    >>> prims.set_angular_velocities(velocities)
                    >>>
                    >>> # set only the articulation linear velocities for the first, middle and last of the 5 envs
                    >>> velocities = np.full((3, 3), fill_value=0.1)
                    >>> prims.set_angular_velocities(velocities, indices=np.array([0, 2, 4]))
                
        """
    def set_armatures(self, values: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set armatures for articulation joints in the view
        
                Search for *"Joint Armature"* in |physx_docs| for more details.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor, wp.array]): armatures for articulation joints in the view. shape (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set all joint armatures to 0.05 for all envs
                    >>> prims.set_armatures(np.full((num_envs, prims.num_dof), 0.05))
                    >>>
                    >>> # set only the finger joint (panda_finger_joint1 (7) and panda_finger_joint2 (8)) armatures
                    >>> # for the first, middle and last of the 5 envs to 0.05
                    >>> prims.set_armatures(np.full((3, 2), 0.05), indices=np.array([0,2,4]), joint_indices=np.array([7,8]))
                
        """
    def set_body_coms(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array] = None, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set body center of mass (COM) positions and orientations for articulation bodies in the view.
        
                Args:
                    positions (Union[np.ndarray, torch.Tensor, wp.array]): body center of mass positions for articulations in the view. shape (M, K, 3).
                    orientations (Union[np.ndarray, torch.Tensor, wp.array]): body center of mass orientations for articulations in the view. shape (M, K, 4).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the center of mass for all the articulation rigid bodies to the indicated values.
                    >>> # Since there are 5 envs, the inertias are repeated 5 times
                    >>> positions = np.tile(np.array([0.01, 0.02, 0.03]), (num_envs, prims.num_bodies, 1))
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, prims.num_bodies, 1))
                    >>> prims.set_body_coms(positions, orientations)
                    >>>
                    >>> # set the fingers center of mass: panda_leftfinger (10) and panda_rightfinger (11) to 0.2
                    >>> # for the first, middle and last of the 5 envs
                    >>> positions = np.tile(np.array([0.01, 0.02, 0.03]), (3, 2, 1))
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 2, 1))
                    >>> prims.set_body_coms(positions, orientations, indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
                
        """
    def set_body_disable_gravity(self, values: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set body gravity activation articulation bodies in the view.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor, wp.array]): body gravity activation for articulations in the view. shape (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
                
        """
    def set_body_inertias(self, values: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set body inertias for articulation bodies in the view.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor, wp.array]): body inertias for articulations in the view. shape (M, K, 9).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the inertias for all the articulation rigid bodies to the indicated values.
                    >>> # Since there are 5 envs, the inertias are repeated 5 times
                    >>> inertias = np.tile(np.array([0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1]), (num_envs, prims.num_bodies, 1))
                    >>> prims.set_body_inertias(inertias)
                    >>>
                    >>> # set the fingers inertias: panda_leftfinger (10) and panda_rightfinger (11) to 0.2
                    >>> # for the first, middle and last of the 5 envs
                    >>> inertias = np.tile(np.array([0.1, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.1]), (3, 2, 1))
                    >>> prims.set_body_inertias(inertias, indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
                
        """
    def set_body_masses(self, values: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, body_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set body masses for articulation bodies in the view
        
                Args:
                    values (Union[np.ndarray, torch.Tensor, wp.array]): body masses for articulations in the view. shape (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    body_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): body indices to specify which bodies
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of bodies.
                                                                                         Defaults to None (i.e: all bodies).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the masses for all the articulation rigid bodies to the indicated values.
                    >>> # Since there are 5 envs, the masses are repeated 5 times
                    >>> masses = np.tile(np.array([1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.2]), (num_envs, 1))
                    >>> prims.set_body_masses(masses)
                    >>>
                    >>> # set the fingers masses: panda_leftfinger (10) and panda_rightfinger (11) to 0.2
                    >>> # for the first, middle and last of the 5 envs
                    >>> masses = np.tile(np.array([0.2, 0.2]), (3, 1))
                    >>> prims.set_body_masses(masses, indices=np.array([0, 2, 4]), body_indices=np.array([10, 11]))
                
        """
    def set_effort_modes(self, mode: str, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set effort modes for articulations in the view
        
                Args:
                    mode (str): effort mode to be applied to prims in the view: ``acceleration`` or ``force``.
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the effort mode for all joints to 'force'
                    >>> prims.set_effort_modes("force")
                    >>>
                    >>> # set only the finger joints effort mode to 'force' for the first, middle and last of the 5 envs
                    >>> prims.set_effort_modes("force", indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def set_enabled_self_collisions(self, flags: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the enable self collisions flag (``physxArticulation:enabledSelfCollisions``)
        
                Args:
                    flags (Union[np.ndarray, torch.Tensor, wp.array]): true to enable self collision. otherwise false. shape (M,)
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # enable the self collisions flag for all envs
                    >>> prims.set_enabled_self_collisions(np.full((num_envs,), True))
                    >>>
                    >>> # enable the self collisions flag only for the first, middle and last of the 5 envs
                    >>> prims.set_enabled_self_collisions(np.full((3,), True), indices=np.array([0, 2, 4]))
                
        """
    def set_fixed_tendon_properties(self, stiffnesses: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array] = None, dampings: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array] = None, limit_stiffnesses: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array] = None, limits: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array] = None, rest_lengths: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array] = None, offsets: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array] = None, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set fixed tendon properties for articulations in the view
        
                Search for *Fixed Tendon* in |physx_docs| for more details
        
                Args:
                    stiffnesses (Union[np.ndarray, torch.Tensor, wp.array]): fixed tendon stiffnesses for articulations in the view. shape (M, K).
                    dampings (Union[np.ndarray, torch.Tensor, wp.array]): fixed tendon dampings for articulations in the view. shape (M, K).
                    limit_stiffnesses (Union[np.ndarray, torch.Tensor, wp.array]): fixed tendon limit stiffnesses for articulations in the view. shape (M, K).
                    limits (Union[np.ndarray, torch.Tensor, wp.array]): fixed tendon limits for articulations in the view. shape (M, K, 2).
                    rest_lengths (Union[np.ndarray, torch.Tensor, wp.array]): fixed tendon rest lengths for articulations in the view. shape (M, K).
                    offsets (Union[np.ndarray, torch.Tensor, wp.array]): fixed tendon offsets for articulations in the view. shape (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the limit stiffnesses and dampings
                    >>> # for the ShadowHand articulation that has 4 fixed tendons (prims.num_fixed_tendons)
                    >>> limit_stiffnesses = np.full((num_envs, prims.num_fixed_tendons), fill_value=10.0)
                    >>> dampings = np.full((num_envs, prims.num_fixed_tendons), fill_value=0.1)
                    >>> prims.set_fixed_tendon_properties(dampings=dampings, limit_stiffnesses=limit_stiffnesses)
                
        """
    def set_friction_coefficients(self, values: typing.Union[numpy.ndarray, torch.Tensor], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set the friction coefficients for articulation joints in the view
        
                Search for *"Joint Friction Coefficient"* in |physx_docs| for more details.
        
                Args:
                    values (Union[np.ndarray, torch.Tensor, wp.array]): friction coefficients for articulation joints in the view. shape (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set all joint friction coefficients to 0.05 for all envs
                    >>> prims.set_friction_coefficients(np.full((num_envs, prims.num_dof), 0.05))
                    >>>
                    >>> # set only the finger joint (panda_finger_joint1 (7) and panda_finger_joint2 (8)) friction coefficients
                    >>> # for the first, middle and last of the 5 envs to 0.05
                    >>> prims.set_friction_coefficients(np.full((3, 2), 0.05), indices=np.array([0,2,4]), joint_indices=np.array([7,8]))
                
        """
    def set_gains(self, kps: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, kds: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None, save_to_usd: bool = False) -> None:
        """
        Set the implicit Proportional-Derivative (PD) controller's Kps (stiffnesses) and Kds (dampings) of articulations in the view
        
                Args:
                    kps (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): stiffness of the drives. shape is (M, K). Defaults to None.
                    kds (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): damping of the drives. shape is (M, K).. Defaults to None.
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
                    save_to_usd (bool, optional): True to save the gains in the usd. otherwise False.
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the gains (stiffnesses and dampings) for all the articulation joints to the indicated values.
                    >>> # Since there are 5 envs, the gains are repeated 5 times
                    >>> stiffnesses = np.tile(np.array([100000, 100000, 100000, 100000, 80000, 80000, 80000, 50000, 50000]), (num_envs, 1))
                    >>> dampings = np.tile(np.array([8000, 8000, 8000, 8000, 5000, 5000, 5000, 2000, 2000]), (num_envs, 1))
                    >>> prims.set_gains(kps=stiffnesses, kds=dampings)
                    >>>
                    >>> # set the fingers gains (stiffnesses and dampings): panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # to 50000 and 2000 respectively for the first, middle and last of the 5 envs
                    >>> stiffnesses = np.tile(np.array([50000, 50000]), (3, 1))
                    >>> dampings = np.tile(np.array([2000, 2000]), (3, 1))
                    >>> prims.set_gains(kps=stiffnesses, kds=dampings, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def set_joint_efforts(self, efforts: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set the joint efforts of articulations in the view
        
                .. note::
        
                    This method can be used for effort control. For this purpose, there must be no joint drive
                    or the stiffness and damping must be set to zero.
        
                Args:
                    efforts (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): efforts of articulations in the view to be set to in the next frame.
                                                                            shape is (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                .. hint::
        
                    This method belongs to the methods used to set the articulation kinematic states:
        
                    ``set_velocities`` (``set_linear_velocities``, ``set_angular_velocities``),
                    ``set_joint_positions``, ``set_joint_velocities``, ``set_joint_efforts``
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the efforts for all the articulation joints to the indicated values.
                    >>> # Since there are 5 envs, the joint efforts are repeated 5 times
                    >>> efforts = np.tile(np.array([10, 20, 30, 40, 50, 60, 70, 80, 90]), (num_envs, 1))
                    >>> prims.set_joint_efforts(efforts)
                    >>>
                    >>> # set the fingers efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 10
                    >>> # for the first, middle and last of the 5 envs
                    >>> efforts = np.tile(np.array([10, 10]), (3, 1))
                    >>> prims.set_joint_efforts(efforts, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def set_joint_position_targets(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set the joint position targets for the implicit Proportional-Derivative (PD) controllers
        
                .. note::
        
                    This is an independent method for controlling joints. To apply multiple targets (position, velocity,
                    and/or effort) in the same call, consider using the ``apply_action`` method
        
                Args:
                    positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): joint position targets for the implicit PD controller.
                                                                            shape is (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                .. hint::
        
                    High stiffness makes the joints snap faster and harder to the desired target,
                    and higher damping smoothes but also slows down the joint's movement to target
        
                    * For position control, set relatively high stiffness and low damping (to reduce vibrations)
        
                Example:
        
                .. code-block:: python
        
                    >>> # apply the target positions (to move all the robot joints) to the indicated values.
                    >>> # Since there are 5 envs, the joint positions are repeated 5 times
                    >>> positions = np.tile(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]), (num_envs, 1))
                    >>> prims.set_joint_position_targets(positions)
                    >>>
                    >>> # close the robot fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
                    >>> # for the first, middle and last of the 5 envs
                    >>> positions = np.tile(np.array([0.0, 0.0]), (3, 1))
                    >>> prims.set_joint_position_targets(positions, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def set_joint_positions(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set the joint positions of articulations in the view
        
                .. warning::
        
                    This method will immediately set (teleport) the affected joints to the indicated value.
                    Use the ``set_joint_position_targets`` or the ``apply_action`` methods to control the articulation joints.
        
                Args:
                    positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): joint positions of articulations in the view to be set to in the next frame.
                                                                            shape is (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                .. hint::
        
                    This method belongs to the methods used to set the articulation kinematic states:
        
                    ``set_velocities`` (``set_linear_velocities``, ``set_angular_velocities``),
                    ``set_joint_positions``, ``set_joint_velocities``, ``set_joint_efforts``
        
                Example:
        
                .. code-block:: python
        
                    >>> # set all the articulation joints.
                    >>> # Since there are 5 envs, the joint positions are repeated 5 times
                    >>> positions = np.tile(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]), (num_envs, 1))
                    >>> prims.set_joint_positions(positions)
                    >>>
                    >>> # set only the fingers in closed position: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 0.0
                    >>> # for the first, middle and last of the 5 envs
                    >>> positions = np.tile(np.array([0.0, 0.0]), (3, 1))
                    >>> prims.set_joint_positions(positions, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def set_joint_velocities(self, velocities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set the joint velocities of articulations in the view
        
                .. warning::
        
                    This method will immediately set the affected joints to the indicated value.
                    Use the ``set_joint_velocity_targets`` or the ``apply_action`` methods to control the articulation joints.
        
                Args:
                    velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): joint velocities of articulations in the view to be set to in the next frame.
                                                                            shape is (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                .. hint::
        
                    This method belongs to the methods used to set the articulation kinematic states:
        
                    ``set_velocities`` (``set_linear_velocities``, ``set_angular_velocities``),
                    ``set_joint_positions``, ``set_joint_velocities``, ``set_joint_efforts``
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the velocities for all the articulation joints to the indicated values.
                    >>> # Since there are 5 envs, the joint velocities are repeated 5 times
                    >>> velocities = np.tile(np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]), (num_envs, 1))
                    >>> prims.set_joint_velocities(velocities)
                    >>>
                    >>> # set the fingers velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8) to -0.1
                    >>> # for the first, middle and last of the 5 envs
                    >>> velocities = np.tile(np.array([-0.1, -0.1]), (3, 1))
                    >>> prims.set_joint_velocities(velocities, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def set_joint_velocity_targets(self, velocities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set the joint velocity targets for the implicit Proportional-Derivative (PD) controllers
        
                .. note::
        
                    This is an independent method for controlling joints. To apply multiple targets (position, velocity,
                    and/or effort) in the same call, consider using the ``apply_action`` method
        
                Args:
                    velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): joint velocity targets for the implicit PD controller.
                                                                            shape is (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                .. hint::
        
                    High stiffness makes the joints snap faster and harder to the desired target,
                    and higher damping smoothes but also slows down the joint's movement to target
        
                    * For velocity control, stiffness must be set to zero with a non-zero damping
        
                Example:
        
                .. code-block:: python
        
                    >>> # apply the target velocities for all the articulation joints to the indicated values.
                    >>> # Since there are 5 envs, the joint velocities are repeated 5 times
                    >>> velocities = np.tile(np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]), (num_envs, 1))
                    >>> prims.set_joint_velocity_targets(velocities)
                    >>>
                    >>> # apply the fingers target velocities: panda_finger_joint1 (7) and panda_finger_joint2 (8) to -1.0
                    >>> # for the first, middle and last of the 5 envs
                    >>> velocities = np.tile(np.array([-0.1, -0.1]), (3, 1))
                    >>> prims.set_joint_velocity_targets(velocities, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def set_joints_default_state(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, velocities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, efforts: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the joints default state (joint positions, velocities and efforts) to be applied after each reset.
        
                .. note::
        
                    The default states will be set during post-reset (e.g., calling ``.post_reset()`` or ``world.reset()`` methods)
        
                Args:
                    positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): default joint positions.
                                                                                     shape is (N, num of dofs). Defaults to None.
                    velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): default joint velocities.
                                                                                     shape is (N, num of dofs). Defaults to None.
                    efforts (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): default joint efforts.
                                                                                     shape is (N, num of dofs). Defaults to None.
        
                Example:
        
                .. code-block:: python
        
                    >>> # configure default joint states for all articulations
                    >>> positions = np.tile(np.array([0.0, -1.0, 0.0, -2.2, 0.0, 2.4, 0.8, 0.04, 0.04]), (num_envs, 1))
                    >>> prims.set_joints_default_state(
                    ...     positions=positions,
                    ...     velocities=np.zeros((num_envs, prims.num_dof)),
                    ...     efforts=np.zeros((num_envs, prims.num_dof))
                    ... )
                    >>>
                    >>> # set default states during post-reset
                    >>> prims.post_reset()
                
        """
    def set_linear_velocities(self, velocities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the linear velocities of the prims in the view
        
                The method does this through the PhysX API only. It has to be called after initialization.
                Note: This method is not supported for the gpu pipeline. ``set_velocities`` method should be used instead.
        
                .. warning::
        
                    This method will immediately set the articulation state
        
                Args:
                    velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): linear velocities to set the rigid prims to. shape is (M, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                .. hint::
        
                    This method belongs to the methods used to set the articulation kinematic state:
        
                    ``set_velocities`` (``set_linear_velocities``, ``set_angular_velocities``),
                    ``set_joint_positions``, ``set_joint_velocities``, ``set_joint_efforts``
        
                Example:
        
                .. code-block:: python
        
                    >>> # set each articulation linear velocity to (1.0, 1.0, 1.0)
                    >>> velocities = np.ones((num_envs, 3))
                    >>> prims.set_linear_velocities(velocities)
                    >>>
                    >>> # set only the articulation linear velocities for the first, middle and last of the 5 envs
                    >>> velocities = np.ones((3, 3))
                    >>> prims.set_linear_velocities(velocities, indices=np.array([0, 2, 4]))
                
        """
    def set_local_poses(self, translations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set prim poses in the view with respect to the local frame (the prim's parent frame).
        
                .. warning::
        
                    This method will change (teleport) the prim poses immediately to the indicated value
        
                Args:
                    translations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional):
                                                                  translations in the local frame of the prims
                                                                  (with respect to its parent prim). shape is (M, 3).
                                                                  Defaults to None, which means left unchanged.
                    orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional):
                                                                  quaternion orientations in the local frame of the prims.
                                                                  quaternion is scalar-first (w, x, y, z). shape is (M, 4).
                                                                  Defaults to None, which means left unchanged.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                .. hint::
        
                    This method belongs to the methods used to set the prim state
        
                Example:
        
                .. code-block:: python
        
                    >>> # reposition all articulations
                    >>> positions = np.zeros((num_envs, 3))
                    >>> positions[:,0] = np.arange(num_envs)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
                    >>> prims.set_local_poses(positions, orientations)
                    >>>
                    >>> # reposition only the articulations for the first, middle and last of the 5 envs
                    >>> positions = np.zeros((3, 3))
                    >>> positions[:,1] = np.arange(3)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
                    >>> prims.set_local_poses(positions, orientations, indices=np.array([0, 2, 4]))
                
        """
    def set_max_efforts(self, values: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set maximum efforts for articulation in the view
        
                Args:
                    values (Union[np.ndarray, torch.Tensor, wp.array]): maximum efforts for articulations in the view. shape (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the max efforts for all the articulation joints to the indicated values.
                    >>> # Since there are 5 envs, the joint efforts are repeated 5 times
                    >>> max_efforts = np.tile(np.array([10000, 9000, 8000, 7000, 6000, 5000, 4000, 1000, 1000]), (num_envs, 1))
                    >>> prims.set_max_efforts(max_efforts)
                    >>>
                    >>> # set the fingers max efforts: panda_finger_joint1 (7) and panda_finger_joint2 (8) to 1000
                    >>> # for the first, middle and last of the 5 envs
                    >>> max_efforts = np.tile(np.array([1000, 1000]), (3, 1))
                    >>> prims.set_max_efforts(max_efforts, indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def set_max_joint_velocities(self, values: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Set maximum velocities for articulation in the view
        
                Args:
                    values (Union[np.ndarray, torch.Tensor, wp.array]): maximum velocities for articulations in the view. shape (M, K).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
                
        """
    def set_sleep_thresholds(self, thresholds: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the threshold for articulations to enter a sleep state
        
                Search for *Articulations and Sleeping* in |physx_docs| for more details
        
                Args:
                    thresholds (Union[np.ndarray, torch.Tensor, wp.array]): sleep thresholds to be applied. shape (M,).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the sleep threshold for all envs
                    >>> prims.set_sleep_thresholds(np.full((num_envs,), 0.01))
                    >>>
                    >>> # set only the sleep threshold for the first, middle and last of the 5 envs
                    >>> prims.set_sleep_thresholds(np.full((3,), 0.01), indices=np.array([0, 2, 4]))
                
        """
    def set_solver_position_iteration_counts(self, counts: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the solver (position) iteration count for the articulations
        
                The solver iteration count determines how accurately contacts, drives, and limits are resolved.
                Search for *Solver Iteration Count* in |physx_docs| for more details.
        
                .. warning::
        
                    Setting a higher number of iterations may improve the fidelity of the simulation, although it may affect its performance.
        
                Args:
                    counts (Union[np.ndarray, torch.Tensor, wp.array]): number of iterations for the solver. Shape (M,).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the position iteration count for all envs
                    >>> prims.set_solver_position_iteration_counts(np.full((num_envs,), 64))
                    >>>
                    >>> # set only the position iteration count for the first, middle and last of the 5 envs
                    >>> prims.set_solver_position_iteration_counts(np.full((3,), 64), indices=np.array([0, 2, 4]))
                
        """
    def set_solver_velocity_iteration_counts(self, counts: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the solver (velocity) iteration count for the articulations
        
                The solver iteration count determines how accurately contacts, drives, and limits are resolved.
                Search for *Solver Iteration Count* in |physx_docs| for more details.
        
                .. warning::
        
                    Setting a higher number of iterations may improve the fidelity of the simulation, although it may affect its performance.
        
                Args:
                    counts (Union[np.ndarray, torch.Tensor, wp.array]): number of iterations for the solver. Shape (M,).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the velocity iteration count for all envs
                    >>> prims.set_solver_velocity_iteration_counts(np.full((num_envs,), 64))
                    >>>
                    >>> # set only the velocity iteration count for the first, middle and last of the 5 envs
                    >>> prims.set_solver_velocity_iteration_counts(np.full((3,), 64), indices=np.array([0, 2, 4]))
                
        """
    def set_stabilization_thresholds(self, thresholds: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the mass-normalized kinetic energy below which the articulation may participate in stabilization
        
                Search for *Stabilization Threshold* in |physx_docs| for more details
        
                Args:
                    thresholds (Union[np.ndarray, torch.Tensor, wp.array]): stabilization thresholds to be applied. Shape (M,).
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the stabilization threshold for all envs
                    >>> prims.set_stabilization_thresholds(np.full((num_envs,), 0.005))
                    >>>
                    >>> # set only the stabilization threshold for the first, middle and last of the 5 envs
                    >>> prims.set_stabilization_thresholds(np.full((3,), 0.0051), indices=np.array([0, 2, 4]))
                
        """
    def set_velocities(self, velocities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the linear and angular velocities of the prims in the view at once.
        
                The method does this through the PhysX API only. It has to be called after initialization
        
                .. warning::
        
                    This method will immediately set the articulation state
        
                Args:
                    velocities (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): linear and angular velocities respectively to set the rigid prims to. shape is (M, 6).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                .. hint::
        
                    This method belongs to the methods used to set the articulation kinematic state:
        
                    ``set_velocities`` (``set_linear_velocities``, ``set_angular_velocities``),
                    ``set_joint_positions``, ``set_joint_velocities``, ``set_joint_efforts``
        
                Example:
        
                .. code-block:: python
        
                    >>> # set each articulation linear velocity to (1., 1., 1.) and angular velocity to (.1, .1, .1)
                    >>> velocities = np.ones((num_envs, 6))
                    >>> velocities[:,3:] = 0.1
                    >>> prims.set_velocities(velocities)
                    >>>
                    >>> # set only the articulation velocities for the first, middle and last of the 5 envs
                    >>> velocities = np.ones((3, 6))
                    >>> velocities[:,3:] = 0.1
                    >>> prims.set_velocities(velocities, indices=np.array([0, 2, 4]))
                
        """
    def set_world_poses(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, usd: bool = True) -> None:
        """
        Set poses of prims in the view with respect to the world's frame.
        
                .. warning::
        
                    This method will change (teleport) the prim poses immediately to the indicated value
        
                Args:
                    positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): positions in the world frame of the prim. shape is (M, 3).
                                                                                     Defaults to None, which means left unchanged.
                    orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): quaternion orientations in the world frame of the prims.
                                                                                        quaternion is scalar-first (w, x, y, z). shape is (M, 4).
                                                                                        Defaults to None, which means left unchanged.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    usd (bool, optional): True to query from usd. Otherwise False to query from Fabric data. Defaults to True.
        
                .. hint::
        
                    This method belongs to the methods used to set the prim state
        
                Example:
        
                .. code-block:: python
        
                    >>> # reposition all articulations in row (x-axis)
                    >>> positions = np.zeros((num_envs, 3))
                    >>> positions[:,0] = np.arange(num_envs)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
                    >>> prims.set_world_poses(positions, orientations)
                    >>>
                    >>> # reposition only the articulations for the first, middle and last of the 5 envs in column (y-axis)
                    >>> positions = np.zeros((3, 3))
                    >>> positions[:,1] = np.arange(3)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
                    >>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
                
        """
    def switch_control_mode(self, mode: str, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None, joint_names: typing.Optional[typing.List[str]] = None) -> None:
        """
        Switch control mode between ``"position"``, ``"velocity"``, or ``"effort"`` for all joints
        
                This method will set the implicit Proportional-Derivative (PD) controller's Kps (stiffnesses) and Kds (dampings),
                defined via the ``set_gains``  method, of the selected articulations and joints according to the following rule:
        
                .. list-table::
                    :header-rows: 1
        
                    * - Control mode
                      - Stiffnesses
                      - Dampings
                    * - ``"position"``
                      - Kps
                      - Kds
                    * - ``"velocity"``
                      - 0
                      - Kds
                    * - ``"effort"``
                      - 0
                      - 0
        
                Args:
                    mode (str): control mode to switch the articulations specified to. It can be ``"position"``, ``"velocity"``, or ``"effort"``
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    joint_indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): joint indices to specify which joints
                                                                                         to manipulate. Shape (K,).
                                                                                         Where K <= num of dofs.
                                                                                         Defaults to None (i.e: all dofs).
                    joint_names (Optional[List[str]]): joint names to specify which joints to manipulate
                                                      (can't be sppecified together with joint_indices). Shape (K,).
                                                      Where K <= num of dofs. Defaults to None (i.e: all dofs).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set 'velocity' as control mode for all joints
                    >>> prims.switch_control_mode("velocity")
                    >>>
                    >>> # set 'effort' as control mode only for the fingers: panda_finger_joint1 (7) and panda_finger_joint2 (8)
                    >>> # for the first, middle and last of the 5 envs
                    >>> prims.switch_control_mode("effort", indices=np.array([0, 2, 4]), joint_indices=np.array([7, 8]))
                
        """
    def switch_dof_control_mode(self, mode: str, dof_index: int, indices: typing.Union[numpy.ndarray, typing.List, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Switch control mode between ``"position"``, ``"velocity"``, or ``"effort"`` for the specified DOF
        
                This method will set the implicit Proportional-Derivative (PD) controller's Kps (stiffnesses) and Kds (dampings),
                defined via the ``set_gains``  method, of the selected DOF according to the following rule:
        
                .. list-table::
                    :header-rows: 1
        
                    * - Control mode
                      - Stiffnesses
                      - Dampings
                    * - ``"position"``
                      - Kps
                      - Kds
                    * - ``"velocity"``
                      - 0
                      - Kds
                    * - ``"effort"``
                      - 0
                      - 0
        
                Args:
                    mode (str): control mode to switch the DOF specified to. It can be ``"position"``, ``"velocity"`` or ``"effort"``
                    dof_index (int): dof index to switch the control mode of.
                    indices (Optional[Union[np.ndarray, List, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set 'velocity' as control mode for the panda_joint1 (0) joint for all envs
                    >>> prims.switch_dof_control_mode("velocity", dof_index=0)
                    >>>
                    >>> # set 'effort' as control mode for the panda_joint1 (0) for the first, middle and last of the 5 envs
                    >>> prims.switch_dof_control_mode("effort", dof_index=0, indices=np.array([0, 2, 4]))
                
        """
    @property
    def body_names(self) -> typing.List[str]:
        """
        List of prim names for each rigid body (link) of the articulations
        
                Returns:
                    List[str]: ordered names of bodies that corresponds to links for the articulations in the view
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.body_names
                    ['panda_link0', 'panda_link1', 'panda_link2', 'panda_link3', 'panda_link4', 'panda_link5',
                     'panda_link6', 'panda_link7', 'panda_link8', 'panda_hand', 'panda_leftfinger', 'panda_rightfinger']
                
        """
    @property
    def dof_names(self) -> typing.List[str]:
        """
        List of prim names for each DOF of the articulations
        
                Returns:
                    List[str]: ordered names of joints that corresponds to degrees of freedom for the articulations in the view
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.dof_names
                    ['panda_joint1', 'panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5',
                     'panda_joint6', 'panda_joint7', 'panda_finger_joint1', 'panda_finger_joint2']
                
        """
    @property
    def joint_names(self) -> typing.List[str]:
        """
        List of prim names for each joint of the articulations
        
                Returns:
                    List[str]: ordered names of joints that corresponds to degrees of freedom for the articulations in the view
        
                
        """
    @property
    def num_bodies(self) -> int:
        """
        Number of rigid bodies (links) of the articulations
        
                Returns:
                    int: maximum number of rigid bodies for the articulations in the view
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_bodies
                    12
                
        """
    @property
    def num_dof(self) -> int:
        """
        Number of DOF of the articulations
        
                Returns:
                    int: maximum number of DOFs for the articulations in the view
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_dof
                    9
                
        """
    @property
    def num_fixed_tendons(self) -> int:
        """
        Number of fixed tendons of the articulations
        
                Returns:
                    int: maximum number of fixed tendons for the articulations in the view
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_fixed_tendons
                    0
                
        """
    @property
    def num_joints(self) -> int:
        """
        Number of joints of the articulations
        
                Returns:
                    int: number of joints of the articulations in the view
        
                
        """
    @property
    def num_shapes(self) -> int:
        """
        Number of rigid shapes of the articulations
        
                Returns:
                    int: maximum number of rigid shapes for the articulations in the view
        
                Example:
        
                .. code-block:: python
        
                    >>> prims.num_shapes
                    17
                
        """
