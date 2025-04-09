from __future__ import annotations
import isaacsim.core.utils.types
from isaacsim.core.utils.types import XFormPrimState
import numpy
import numpy as np
import pxr.Usd
from pxr import Usd
__all__ = ['Usd', 'XFormPrimState', 'np']
class _SinglePrimWrapper:
    def __init__(self, view) -> None:
        ...
    def _view_state_conversion(self, view_state):
        ...
    def apply_visual_material(self, visual_material: VisualMaterial, weaker_than_descendants: bool = False) -> None:
        """
        Apply visual material to the held prim and optionally its descendants.
        
                Args:
                    visual_material (VisualMaterial): visual material to be applied to the held prim. Currently supports
                                                      PreviewSurface, OmniPBR and OmniGlass.
                    weaker_than_descendants (bool, optional): True if the material shouldn't override the descendants
                                                              materials, otherwise False. Defaults to False.
        
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
                    >>> prim.apply_visual_material(material)
                
        """
    def get_applied_visual_material(self) -> VisualMaterial:
        """
        Return the current applied visual material in case it was applied using apply_visual_material
                or it's one of the following materials that was already applied before: PreviewSurface, OmniPBR and OmniGlass.
        
                Returns:
                    VisualMaterial: the current applied visual material if its type is currently supported.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a visual material applied
                    >>> prim.get_applied_visual_material()
                    <isaacsim.core.api.materials.omni_glass.OmniGlass object at 0x7f36263106a0>
                
        """
    def get_default_state(self) -> isaacsim.core.utils.types.XFormPrimState:
        """
        Get the default prim states (spatial position and orientation).
        
                Returns:
                    XFormPrimState: an object that contains the default state of the prim (position and orientation)
        
                Example:
        
                .. code-block:: python
        
                    >>> state = prim.get_default_state()
                    >>> state
                    <isaacsim.core.utils.types.XFormPrimState object at 0x7f33addda650>
                    >>>
                    >>> state.position
                    [-4.5299529e-08 -1.8347054e-09 -2.8610229e-08]
                    >>> state.orientation
                    [1. 0. 0. 0.]
                
        """
    def get_local_pose(self) -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
        """
        Get prim's pose with respect to the local frame (the prim's parent frame)
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: first index is the position in the local frame (with shape (3, )).
                    Second index is quaternion orientation (with shape (4, )) in the local frame
        
                Example:
        
                .. code-block:: python
        
                    >>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
                    >>> position, orientation = prim.get_local_pose()
                    >>> position
                    [0. 0. 0.]
                    >>> orientation
                    [0. 0. 0.]
                
        """
    def get_local_scale(self) -> numpy.ndarray:
        """
        Get prim's scale with respect to the local frame (the parent's frame)
        
                Returns:
                    np.ndarray: scale applied to the prim's dimensions in the local frame. shape is (3, ).
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_local_scale()
                    [1. 1. 1.]
                
        """
    def get_visibility(self) -> bool:
        """
        
                Returns:
                    bool: true if the prim is visible in stage. false otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> # get the visible state of an visible prim on the stage
                    >>> prim.get_visibility()
                    True
                
        """
    def get_world_pose(self) -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
        """
        Get prim's pose with respect to the world's frame
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: first index is the position in the world frame (with shape (3, )).
                    Second index is quaternion orientation (with shape (4, )) in the world frame
        
                Example:
        
                .. code-block:: python
        
                    >>> # if the prim is in position (1.0, 0.5, 0.0) with respect to the world frame
                    >>> position, orientation = prim.get_world_pose()
                    >>> position
                    [1.  0.5 0. ]
                    >>> orientation
                    [1. 0. 0. 0.]
                
        """
    def get_world_scale(self) -> numpy.ndarray:
        """
        Get prim's scale with respect to the world's frame
        
                Returns:
                    np.ndarray: scale applied to the prim's dimensions in the world frame. shape is (3, ).
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.get_world_scale()
                    [1. 1. 1.]
                
        """
    def initialize(self, physics_sim_view = None) -> None:
        """
        Create a physics simulation view if not passed and using PhysX tensor API
        
                .. note::
        
                    If the prim has been added to the world scene (e.g., ``world.scene.add(prim)``),
                    it will be automatically initialized when the world is reset (e.g., ``world.reset()``).
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.initialize()
                
        """
    def is_valid(self) -> bool:
        """
        Check if the prim path has a valid USD Prim at it
        
                Returns:
                    bool: True is the current prim path corresponds to a valid prim in stage. False otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given an existing and valid prim
                    >>> prims.is_valid()
                    True
                
        """
    def is_visual_material_applied(self) -> bool:
        """
        Check if there is a visual material applied
        
                Returns:
                    bool: True if there is a visual material applied. False otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a visual material applied
                    >>> prim.is_visual_material_applied()
                    True
                
        """
    def post_reset(self) -> None:
        """
        Reset the prim to its default state (position and orientation).
        
                .. note::
        
                    For an articulation, in addition to configuring the root prim's default position and spatial orientation
                    (defined via the ``set_default_state`` method), the joint's positions, velocities, and efforts
                    (defined via the ``set_joints_default_state`` method) are imposed
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.post_reset()
                
        """
    def set_default_state(self, position: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None) -> None:
        """
        Set the default state of the prim (position and orientation), that will be used after each reset.
        
                Args:
                    position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                               Defaults to None, which means left unchanged.
                    orientation (Optional[Sequence[float]], optional): quaternion orientation in the world frame of the prim.
                                                                  quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                                  Defaults to None, which means left unchanged.
        
                Example:
        
                .. code-block:: python
        
                    >>> # configure default state
                    >>> prim.set_default_state(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1, 0, 0, 0]))
                    >>>
                    >>> # set default states during post-reset
                    >>> prim.post_reset()
                
        """
    def set_local_pose(self, translation: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None) -> None:
        """
        Set prim's pose with respect to the local frame (the prim's parent frame).
        
                .. warning::
        
                    This method will change (teleport) the prim pose immediately to the indicated value
        
                Args:
                    translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                                  (with respect to its parent prim). shape is (3, ).
                                                                  Defaults to None, which means left unchanged.
                    orientation (Optional[Sequence[float]], optional): quaternion orientation in the local frame of the prim.
                                                                  quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                                  Defaults to None, which means left unchanged.
                .. hint::
        
                    This method belongs to the methods used to set the prim state
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.set_local_pose(translation=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
                
        """
    def set_local_scale(self, scale: typing.Optional[typing.Sequence[float]]) -> None:
        """
        Set prim's scale with respect to the local frame (the prim's parent frame).
        
                Args:
                    scale (Optional[Sequence[float]]): scale to be applied to the prim's dimensions. shape is (3, ).
                                                  Defaults to None, which means left unchanged.
        
                Example:
        
                .. code-block:: python
        
                    >>> # scale prim 10 times smaller
                    >>> prim.set_local_scale(np.array([0.1, 0.1, 0.1]))
                
        """
    def set_visibility(self, visible: bool) -> None:
        """
        Set the visibility of the prim in stage
        
                Args:
                    visible (bool): flag to set the visibility of the usd prim in stage.
        
                Example:
        
                .. code-block:: python
        
                    >>> # make prim not visible in the stage
                    >>> prim.set_visibility(visible=False)
                
        """
    def set_world_pose(self, position: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None) -> None:
        """
        Ses prim's pose with respect to the world's frame
        
                .. warning::
        
                    This method will change (teleport) the prim pose immediately to the indicated value
        
                Args:
                    position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                               Defaults to None, which means left unchanged.
                    orientation (Optional[Sequence[float]], optional): quaternion orientation in the world frame of the prim.
                                                                  quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                                  Defaults to None, which means left unchanged.
        
                .. hint::
        
                    This method belongs to the methods used to set the prim state
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.set_world_pose(position=np.array([1.0, 0.5, 0.0]), orientation=np.array([1., 0., 0., 0.]))
                
        """
    @property
    def name(self) -> typing.Optional[str]:
        """
        
                Returns:
                    str: name given to the prim when instantiating it. Otherwise None.
                
        """
    @property
    def non_root_articulation_link(self) -> bool:
        """
        Used to query if the prim is a non root articulation link
        
                Returns:
                    bool: True if the prim itself is a non root link
        
                Example:
        
                .. code-block:: python
        
                    >>> # for a wrapped articulation (where the root prim has the Physics Articulation Root property applied)
                    >>> prim.non_root_articulation_link
                    False
                
        """
    @property
    def prim(self) -> pxr.Usd.Prim:
        """
        
                Returns:
                    Usd.Prim: USD Prim object that this object holds.
                
        """
    @property
    def prim_path(self) -> str:
        """
        
                Returns:
                    str: prim path in the stage
                
        """
