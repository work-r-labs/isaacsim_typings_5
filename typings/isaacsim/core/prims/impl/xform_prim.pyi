from __future__ import annotations
import carb as carb
import isaacsim.core.prims.impl.prim
from isaacsim.core.prims.impl.prim import Prim
from isaacsim.core.simulation_manager.impl.isaac_events import IsaacEvents
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils import fabric as fabric_utils
from isaacsim.core.utils import interops as interops_utils
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_parent
from isaacsim.core.utils.prims import is_prim_non_root_articulation_link
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_current_stage
import isaacsim.core.utils.types
from isaacsim.core.utils.types import XFormPrimViewState
from isaacsim.core.utils.xforms import get_local_pose
from isaacsim.core.utils.xforms import get_world_pose
import numpy as np
from pxr import Gf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdShade
import re as re
import torch as torch
import usdrt as usdrt
import warp as wp
import weakref as weakref
__all__ = ['Gf', 'IsaacEvents', 'Prim', 'SimulationManager', 'Usd', 'UsdGeom', 'UsdShade', 'XFormPrim', 'XFormPrimViewState', 'carb', 'fabric_utils', 'get_current_stage', 'get_local_pose', 'get_prim_at_path', 'get_prim_parent', 'get_world_pose', 'interops_utils', 'is_prim_non_root_articulation_link', 'is_prim_path_valid', 'np', 're', 'torch', 'usdrt', 'weakref', 'wp']
class XFormPrim(isaacsim.core.prims.impl.prim.Prim):
    """
    Provides high level functions to deal with a Xform prim view (one or many) and its descendants
        as well as its attributes/properties.
    
        This class wraps all matching Xforms found at the regex provided at the ``prim_paths_expr`` argument
    
        .. note::
    
            Each prim will have ``xformOp:orient``, ``xformOp:translate`` and ``xformOp:scale`` only post-init,
            unless it is a non-root articulation link.
    
        Args:
            prim_paths_expr (Union[str, List[str]]): prim paths regex to encapsulate all prims that match it.
                                    example: "/World/Env[1-5]/Franka" will match /World/Env1/Franka,
                                    /World/Env2/Franka..etc.
                                    (a non regex prim path can also be used to encapsulate one Xform). Additionally a
                                    list of regex can be provided. example ["/World/Env[1-5]/Franka", "/World/Env[10-19]/Franka"].
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "xform_prim_view".
            positions (Optional[Union[np.ndarray, torch.Tensor]], optional):
                                                            default positions in the world frame of the prim.
                                                            shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            translations (Optional[Union[np.ndarray, torch.Tensor]], optional):
                                                            default translations in the local frame of the prims
                                                            (with respect to its parent prims). shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            orientations (Optional[Union[np.ndarray, torch.Tensor]], optional):
                                                            default quaternion orientations in the world/ local frame of the prim
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (N, 4).
                                                            Defaults to None, which means left unchanged.
            scales (Optional[Union[np.ndarray, torch.Tensor]], optional): local scales to be applied to
                                                            the prim's dimensions. shape is (N, 3).
                                                            Defaults to None, which means left unchanged.
            visibilities (Optional[Union[np.ndarray, torch.Tensor]], optional): set to false for an invisible prim in
                                                                                the stage while rendering. shape is (N,).
                                                                                Defaults to None.
            reset_xform_properties (bool, optional): True if the prims don't have the right set of xform properties
                                                    (i.e: translate, orient and scale) ONLY and in that order.
                                                    Set this parameter to False if the object were cloned using using
                                                    the cloner api in isaacsim.core.cloner. Defaults to True.
            usd (bool, optional): True to strictly read/ write from usd. Otherwise False to allow read/ write from Fabric during initialization. Defaults to True.
    
        Raises:
            Exception: if translations and positions defined at the same time.
            Exception: No prim was matched using the prim_paths_expr provided.
    
        Example:
    
        .. code-block:: python
    
            >>> import isaacsim.core.utils.stage as stage_utils
            >>> from isaacsim.core.cloner import GridCloner
            >>> from isaacsim.core.prims import XFormPrim
            >>> from pxr import UsdGeom
            >>>
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
            >>> env_pos = cloner.clone(
            ...     source_prim_path=env_zero_path,
            ...     prim_paths=cloner.generate_paths("/World/envs/env", num_envs),
            ...     copy_from_source=True
            ... )
            >>>
            >>> # wrap all Xforms
            >>> prims = XFormPrim(prim_paths_expr="/World/envs/env.*", name="xform_view")
            >>> prims
            <isaacsim.core.prims.xform_prim.XFormPrim object at 0x7f8ffd22ebc0>
        
    """
    def __init__(self, prim_paths_expr: typing.Union[str, typing.List[str]], name: str = 'xform_prim_view', positions: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, translations: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, scales: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, visibilities: typing.Union[numpy.ndarray, torch.Tensor, NoneType] = None, reset_xform_properties: bool = True, usd: bool = True) -> None:
        ...
    def _backend2warp(self, data, dtype = None) -> typing.Union[warp.types.array, torch.Tensor, numpy.ndarray]:
        ...
    def _create_fabric_view_indices(self) -> None:
        ...
    def _get_fabric_selection(self) -> None:
        ...
    def _on_post_reset(self, event) -> None:
        ...
    def _prepare_view_in_fabric(self):
        ...
    def _reset_fabric_selection(self, dt) -> None:
        ...
    def _set_xform_properties(self) -> None:
        ...
    def _warp2backend(self, data) -> typing.Union[warp.types.indexedarray, torch.Tensor, numpy.ndarray]:
        ...
    def apply_visual_materials(self, visual_materials: typing.Union[ForwardRef('VisualMaterial'), typing.List[ForwardRef('VisualMaterial')]], weaker_than_descendants: typing.Union[bool, typing.List[bool], NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Apply visual material to the prims and optionally their prim descendants.
        
                Args:
                    visual_materials (Union[VisualMaterial, List[VisualMaterial]]): visual materials to be applied to the prims. Currently supports
                                                                                    PreviewSurface, OmniPBR and OmniGlass. If a list is provided then
                                                                                    its size has to be equal the view's size or indices size.
                                                                                    If one material is provided it will be applied to all prims in the view.
                    weaker_than_descendants (Optional[Union[bool, List[bool]]], optional):  True if the material shouldn't override the descendants
                                                                                            materials, otherwise False. Defaults to False.
                                                                                            If a list of visual materials is provided then a list
                                                                                            has to be provided with the same size for this arg as well.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Raises:
                    Exception: length of visual materials != length of prims indexed
                    Exception: length of visual materials != length of weaker descendants bools arg
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.api.materials import OmniGlass
                    >>>
                    >>> # create a dark-red glass visual material
                    >>> material = OmniGlass(
                    ...     prim_path="/World/material/glass",  # path to the material prim to create
                    ...     ior=1.25,
                    ...     depth=0.001,
                    ...     thin_walled=False,
                    ...     color=np.array([0.5, 0.0, 0.0])
                    ... )
                    >>> prims.apply_visual_materials(material)
                
        """
    def get_applied_visual_materials(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[ForwardRef('VisualMaterial')]:
        """
        Get the current applied visual materials
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    List[VisualMaterial]: a list of the current applied visual materials to the prims if its type is currently supported.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all applied visual materials. Returned size is 5 for the example: 5 envs
                    >>> prims.get_applied_visual_materials()
                    [<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
                     <isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
                     <isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
                     <isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
                     <isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>]
                    >>>
                    >>> # get the applied visual materials for the first, middle and last of the 5 envs. Returned size is 3
                    >>> prims.get_applied_visual_materials(indices=np.array([0, 2, 4]))
                    [<isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
                     <isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>,
                     <isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f829c165de0>]
                
        """
    def get_default_state(self) -> isaacsim.core.utils.types.XFormPrimViewState:
        """
        Get the default states (positions and orientations) defined with the ``set_default_state`` method
        
                Returns:
                    XFormPrimViewState: returns the default state of the prims that is used after each reset.
        
                Example:
        
                .. code-block:: python
        
                    >>> state = prims.get_default_state()
                    >>> state
                    <isaacsim.core.utils.types.XFormPrimViewState object at 0x7f82f73e3070>
                    >>> state.positions
                    [[ 1.5  -0.75  0.  ]
                     [ 1.5   0.75  0.  ]
                     [ 0.   -0.75  0.  ]
                     [ 0.    0.75  0.  ]
                     [-1.5  -0.75  0.  ]]
                    >>> state.orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                
        """
    def get_local_poses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[typing.Tuple[numpy.ndarray, numpy.ndarray], typing.Tuple[torch.Tensor, torch.Tensor], typing.Tuple[warp.types.indexedarray, warp.types.indexedarray]]:
        """
        Get prim poses in the view with respect to the local frame (the prim's parent frame)
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]:
                                                  first index is translations in the local frame of the prims. shape is (M, 3).
                                                    second index is quaternion orientations in the local frame of the prims.
                                                    quaternion is scalar-first (w, x, y, z). shape is (M, 4).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all prims poses with respect to the local frame.
                    >>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
                    >>> positions, orientations = prims.get_local_poses()
                    >>> positions
                    [[ 1.5  -0.75  0.  ]
                     [ 1.5   0.75  0.  ]
                     [ 0.   -0.75  0.  ]
                     [ 0.    0.75  0.  ]
                     [-1.5  -0.75  0.  ]]
                    >>> orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                    >>>
                    >>> # get only the prims poses with respect to the local frame for the first, middle and last of the 5 envs.
                    >>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
                    >>> positions, orientations = prims.get_local_poses(indices=np.array([0, 2, 4]))
                    >>> positions
                    [[ 1.5  -0.75  0.  ]
                     [ 0.   -0.75  0.  ]
                     [-1.5  -0.75  0.  ]]
                    >>> orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                
        """
    def get_local_scales(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get prim scales in the view with respect to the local frame (the parent's frame).
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: scales applied to the prim's dimensions in the local frame. shape is (M, 3).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all prims scales with respect to the local frame.
                    >>> # Returned shape is (5, 3) for the example: 5 envs
                    >>> prims.get_local_scales()
                    [[1. 1. 1.]
                     [1. 1. 1.]
                     [1. 1. 1.]
                     [1. 1. 1.]
                     [1. 1. 1.]]
                    >>>
                    >>> # get only the prims scales with respect to the local frame for the first, middle and last of the 5 envs.
                    >>> # Returned shape is (3, 3) for the example: 3 envs selected
                    >>> prims.get_local_scales(indices=np.array([0, 2, 4]))
                    [[1. 1. 1.]
                     [1. 1. 1.]
                     [1. 1. 1.]]
                
        """
    def get_visibilities(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Returns the current visibilities of the prims in stage.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: Shape (M,) with type bool, where each item holds True
                                                     if the prim is visible in stage. False otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all visibilities. Returned shape is (5,) for the example: 5 envs
                    >>> prims.get_visibilities()
                    [ True  True  True  True  True]
                    >>>
                    >>> # get the visibilities for the first, middle and last of the 5 envs. Returned shape is (3,)
                    >>> prims.get_visibilities(indices=np.array([0, 2, 4]))
                    [ True  True  True]
                
        """
    def get_world_poses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, usd: bool = True) -> typing.Union[typing.Tuple[numpy.ndarray, numpy.ndarray], typing.Tuple[torch.Tensor, torch.Tensor], typing.Tuple[warp.types.indexedarray, warp.types.indexedarray]]:
        """
        Get the poses of the prims in the view with respect to the world's frame
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    usd (bool, optional): True to query from usd. Otherwise False to query from Fabric data. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]: first index is positions in the world frame of the prims. shape is (M, 3).
                                                                                             second index is quaternion orientations in the world frame of the prims.
                                                                                             quaternion is scalar-first (w, x, y, z). shape is (M, 4).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all prims poses with respect to the world's frame.
                    >>> # Returned shape is position (5, 3) and orientation (5, 4) for the example: 5 envs
                    >>> positions, orientations = prims.get_world_poses()
                    >>> positions
                    [[ 1.5  -0.75  0.  ]
                     [ 1.5   0.75  0.  ]
                     [ 0.   -0.75  0.  ]
                     [ 0.    0.75  0.  ]
                     [-1.5  -0.75  0.  ]]
                    >>> orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                    >>>
                    >>> # get only the prims poses with respect to the world's frame for the first, middle and last of the 5 envs.
                    >>> # Returned shape is position (3, 3) and orientation (3, 4) for the example: 3 envs selected
                    >>> positions, orientations = prims.get_world_poses(indices=np.array([0, 2, 4]))
                    >>> positions
                    [[ 1.5  -0.75  0.  ]
                     [ 0.   -0.75  0.  ]
                     [-1.5  -0.75  0.  ]]
                    >>> orientations
                    [[1. 0. 0. 0.]
                     [1. 0. 0. 0.]
                     [1. 0. 0. 0.]]
                
        """
    def get_world_scales(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.Union[numpy.ndarray, torch.Tensor, warp.types.indexedarray]:
        """
        Get prim scales in the view with respect to the world's frame
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[np.ndarray, torch.Tensor, wp.indexedarray]: scales applied to the prim's dimensions in the world frame. shape is (M, 3).
        
                Example:
        
                .. code-block:: python
        
                    >>> # get all prims scales with respect to the world's frame.
                    >>> # Returned shape is (5, 3) for the example: 5 envs
                    >>> prims.get_world_scales()
                    [[1. 1. 1.]
                     [1. 1. 1.]
                     [1. 1. 1.]
                     [1. 1. 1.]
                     [1. 1. 1.]]
                    >>>
                    >>> # get only the prims scales with respect to the world's frame for the first, middle and last of the 5 envs.
                    >>> # Returned shape is (3, 3) for the example: 3 envs selected
                    >>> prims.get_world_scales(indices=np.array([0, 2, 4]))
                    [[1. 1. 1.]
                     [1. 1. 1.]
                     [1. 1. 1.]]
                
        """
    def is_visual_material_applied(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[bool]:
        """
        Check if there is a visual material applied
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    List[bool]: True if there is a visual material applied is applied to the corresponding prim in the view. False otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a visual material that is applied only to the first and the last environment
                    >>> prims.is_visual_material_applied()
                    [True, False, False, False, True]
                    >>>
                    >>> # check for the first, middle and last of the 5 envs
                    >>> prims.is_visual_material_applied(indices=np.array([0, 2, 4]))
                    [True, False, True]
                
        """
    def set_default_state(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the default state of the prims (positions and orientations), that will be used after each reset.
        
                .. note::
        
                    The default states will be set during post-reset (e.g., calling ``.post_reset()`` or ``world.reset()`` methods)
        
                Args:
                    positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional):  positions in the world frame of the prim. shape is (M, 3).
                                                               Defaults to None, which means left unchanged.
                    orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): quaternion orientations in the world frame of the prim.
                                                                  quaternion is scalar-first (w, x, y, z). shape is (M, 4).
                                                                  Defaults to None, which means left unchanged.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # configure default states for all prims
                    >>> positions = np.zeros((num_envs, 3))
                    >>> positions[:, 0] = np.arange(num_envs)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
                    >>> prims.set_default_state(positions=positions, orientations=orientations)
                    >>>
                    >>> # set default states during post-reset
                    >>> prims.post_reset()
                
        """
    def set_local_poses(self, translations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set prim poses in the view with respect to the local frame (the prim's parent frame)
        
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
        
                    >>> # reposition all prims
                    >>> positions = np.zeros((num_envs, 3))
                    >>> positions[:,0] = np.arange(num_envs)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
                    >>> prims.set_local_poses(positions, orientations)
                    >>>
                    >>> # reposition only the prims for the first, middle and last of the 5 envs
                    >>> positions = np.zeros((3, 3))
                    >>> positions[:,1] = np.arange(3)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
                    >>> prims.set_local_poses(positions, orientations, indices=np.array([0, 2, 4]))
                
        """
    def set_local_scales(self, scales: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set prim scales in the view with respect to the local frame (the prim's parent frame)
        
                Args:
                    scales (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): scales to be applied to the prim's dimensions in the view.
                                                                        shape is (M, 3).
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # set the scale for all prims. Since there are 5 envs, the scale is repeated 5 times
                    >>> scales = np.tile(np.array([1.0, 0.75, 0.5]), (num_envs, 1))
                    >>> prims.set_local_scales(scales)
                    >>>
                    >>> # set the scale for the first, middle and last of the 5 envs
                    >>> scales = np.tile(np.array([1.0, 0.75, 0.5]), (3, 1))
                    >>> prims.set_local_scales(scales, indices=np.array([0, 2, 4]))
                
        """
    def set_visibilities(self, visibilities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the visibilities of the prims in stage
        
                Args:
                    visibilities (Union[np.ndarray, torch.Tensor, wp.array]): flag to set the visibilities of the usd prims in stage.
                                                                    Shape (M,). Where M <= size of the encapsulated prims in the view.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to manipulate. Shape (M,).
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Example:
        
                .. code-block:: python
        
                    >>> # make all prims not visible in the stage
                    >>> prims.set_visibilities(visibilities=[False] * num_envs)
                
        """
    def set_world_poses(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, usd: bool = True) -> None:
        """
        Set prim poses in the view with respect to the world's frame
        
                .. warning::
        
                    This method will change (teleport) the prim poses immediately to the indicated value
        
                Args:
                    positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): positions in the world frame of the prims. shape is (M, 3).
                                                                                     Defaults to None, which means left unchanged.
                    orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]], optional): quaternion orientations in the world frame of the prims.
                                                                                        quaternion is scalar-first (w, x, y, z). shape is (M, 4).
                                                                                        Defaults to None, which means left unchanged.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    usd (bool, optional): True to query from usd. Otherwise False to query from Fabric data. Defaults to True.
        
                .. hint::
        
                    This method belongs to the methods used to set the prim state
        
                Example:
        
                .. code-block:: python
        
                    >>> # reposition all prims in row (x-axis)
                    >>> positions = np.zeros((num_envs, 3))
                    >>> positions[:,0] = np.arange(num_envs)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (num_envs, 1))
                    >>> prims.set_world_poses(positions, orientations)
                    >>>
                    >>> # reposition only the prims for the first, middle and last of the 5 envs in column (y-axis)
                    >>> positions = np.zeros((3, 3))
                    >>> positions[:,1] = np.arange(3)
                    >>> orientations = np.tile(np.array([1.0, 0.0, 0.0, 0.0]), (3, 1))
                    >>> prims.set_world_poses(positions, orientations, indices=np.array([0, 2, 4]))
                
        """
    @property
    def is_non_root_articulation_link(self) -> bool:
        """
        
                Returns:
                    bool: True if the prim corresponds to a non root link in an articulation. Otherwise False.
                
        """
