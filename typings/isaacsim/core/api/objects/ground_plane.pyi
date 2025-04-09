from __future__ import annotations
import carb as carb
import isaacsim.core.api.materials.physics_material
from isaacsim.core.api.materials.physics_material import PhysicsMaterial
from isaacsim.core.api.materials.preview_surface import PreviewSurface
from isaacsim.core.api.materials.visual_material import VisualMaterial
import isaacsim.core.prims.impl.single_geometry_prim
from isaacsim.core.prims.impl.single_geometry_prim import SingleGeometryPrim
import isaacsim.core.prims.impl.single_xform_prim
from isaacsim.core.prims.impl.single_xform_prim import SingleXFormPrim
from isaacsim.core.utils.prims import get_first_matching_child_prim
from isaacsim.core.utils.prims import get_prim_path
from isaacsim.core.utils.prims import get_prim_type_name
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_current_stage
from isaacsim.core.utils.stage import get_stage_units
from isaacsim.core.utils.string import find_unique_string_name
import isaacsim.core.utils.types
from isaacsim.core.utils.types import XFormPrimState
import numpy as np
from pxr import Gf
from pxr import PhysicsSchemaTools
from pxr import Usd
import pxr.Usd
__all__ = ['Gf', 'GroundPlane', 'PhysicsMaterial', 'PhysicsSchemaTools', 'PreviewSurface', 'SingleGeometryPrim', 'SingleXFormPrim', 'Usd', 'VisualMaterial', 'XFormPrimState', 'carb', 'find_unique_string_name', 'get_current_stage', 'get_first_matching_child_prim', 'get_prim_path', 'get_prim_type_name', 'get_stage_units', 'is_prim_path_valid', 'np']
class GroundPlane:
    """
    High level wrapper to create/encapsulate a ground plane
    
        Args:
            prim_path (str): prim path of the Prim to encapsulate or create
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "ground_plane".
            size (Optional[float], optional): length of each edge. Defaults to 5000.0.
            z_position (float, optional): ground plane position in the z-axis. Defaults to 0.
            scale (Optional[np.ndarray], optional): local scale to be applied to the prim's dimensions. Defaults to None.
            visible (bool, optional): set to false for an invisible prim in the stage while rendering. Defaults to True.
            color (Optional[np.ndarray], optional): color of the visual plane. Defaults to None.
            physics_material_path (Optional[PhysicsMaterial], optional): path of the physics material to be applied to the held prim.
                                                                Defaults to None. If not specified, a default physics material will be added.
            visual_material (Optional[VisualMaterial], optional): visual material to be applied to the held prim.
                                    Defaults to None. If not specified, a default visual material will be added.
            static_friction (float, optional): static friction coefficient. Defaults to 0.5.
            dynamic_friction (float, optional): dynamic friction coefficient. Defaults to 0.5.
            restitution (float, optional): restitution coefficient. Defaults to 0.8.
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.api.objects import GroundPlane
            >>> import numpy as np
            >>>
            >>> # create a ground plane placed at 0 in the z-axis
            >>> plane = GroundPlane(prim_path="/World/GroundPlane", z_position=0)
            >>> plane
            <isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x7f15d003fb50>
        
    """
    def __init__(self, prim_path: str, name: str = 'ground_plane', size: typing.Optional[float] = None, z_position: typing.Optional[float] = None, scale: typing.Optional[numpy.ndarray] = None, visible: typing.Optional[bool] = None, color: typing.Optional[numpy.ndarray] = None, physics_material: typing.Optional[isaacsim.core.api.materials.physics_material.PhysicsMaterial] = None, visual_material: typing.Optional[isaacsim.core.api.materials.visual_material.VisualMaterial] = None) -> None:
        ...
    def apply_physics_material(self, physics_material: isaacsim.core.api.materials.physics_material.PhysicsMaterial, weaker_than_descendants: bool = False):
        """
        Used to apply physics material to the held prim and optionally its descendants.
        
                Args:
                    physics_material (PhysicsMaterial): physics material to be applied to the held prim. This where you want to
                                                        define friction, restitution..etc. Note: if a physics material is not
                                                        defined, the defaults will be used from PhysX.
                    weaker_than_descendants (bool, optional): True if the material shouldn't override the descendants
                                                              materials, otherwise False. Defaults to False.
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.api.materials import PhysicsMaterial
                    >>>
                    >>> # create a rigid body physical material
                    >>> material = PhysicsMaterial(
                    ...     prim_path="/World/physics_material/aluminum",  # path to the material prim to create
                    ...     dynamic_friction=0.4,
                    ...     static_friction=1.1,
                    ...     restitution=0.1
                    ... )
                    >>> plane.apply_physics_material(material)
                
        """
    def get_applied_physics_material(self) -> isaacsim.core.api.materials.physics_material.PhysicsMaterial:
        """
        Returns the current applied physics material in case it was applied using apply_physics_material or not.
        
                Returns:
                    PhysicsMaterial: the current applied physics material.
        
                Example:
        
                .. code-block:: python
        
                    >>> plane.get_applied_physics_material()
                    <isaacsim.core.api.materials.physics_material.PhysicsMaterial object at 0x7f517ff62920>
                
        """
    def get_default_state(self) -> isaacsim.core.utils.types.XFormPrimState:
        """
        Get the default prim states (spatial position and orientation).
        
                Returns:
                    XFormPrimState: an object that contains the default state of the prim (position and orientation)
        
                Example:
        
                .. code-block:: python
        
                    >>> state = plane.get_default_state()
                    >>> state
                    <isaacsim.core.utils.types.XFormPrimState object at 0x7f6efff41cf0>
                    >>>
                    >>> state.position
                    [0. 0. 0.]
                    >>> state.orientation
                    [1. 0. 0. 0.]
                
        """
    def get_world_pose(self) -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
        """
        Get prim's pose with respect to the world's frame
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: first index is the position in the world frame (with shape (3, )).
                    Second index is quaternion orientation (with shape (4, )) in the world frame
        
                Example:
        
                .. code-block:: python
        
                    >>> # if the prim is in position (0.0, 0.0, 0.0) with respect to the world frame
                    >>> position, orientation = prim.get_world_pose()
                    >>> position
                    [0. 0. 0.]
                    >>> orientation
                    [1. 0. 0. 0.]
                
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
        
                    >>> plane.initialize()
                
        """
    def is_valid(self) -> bool:
        """
        Check if the prim path has a valid USD Prim at it
        
                Returns:
                    bool: True is the current prim path corresponds to a valid prim in stage. False otherwise.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given an existing and valid prim
                    >>> plane.is_valid()
                    True
                
        """
    def post_reset(self) -> None:
        """
        Reset the prim to its default state (position and orientation).
        
                Example:
        
                .. code-block:: python
        
                    >>> plane.post_reset()
                
        """
    def set_default_state(self, position: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None) -> None:
        """
        Sets the default state of the prim (position and orientation), that will be used after each reset.
        
                Args:
                    position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                               Defaults to None, which means left unchanged.
                    orientation (Optional[Sequence[float]], optional): quaternion orientation in the world frame of the prim.
                                                                  quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                                  Defaults to None, which means left unchanged.
        
                Example:
        
                .. code-block:: python
        
                    >>> # configure default state
                    >>> plane.set_default_state(position=np.array([0.0, 0.0, -1.0]), orientation=np.array([1, 0, 0, 0]))
                    >>>
                    >>> # set default states during post-reset
                    >>> plane.post_reset()
                
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
        
                    >>> plane.set_world_pose(position=np.array([0.0, 0.0, 0.5]), orientation=np.array([1., 0., 0., 0.]))
                
        """
    @property
    def collision_geometry_prim(self) -> isaacsim.core.prims.impl.single_geometry_prim.SingleGeometryPrim:
        """
        
                Returns:
                    SingleGeometryPrim: wrapped object as a SingleGeometryPrim
        
                Example:
        
                .. code-block:: python
        
                    >>> plane.collision_geometry_prim
                    <isaacsim.core.prims.single_geometry_prim.SingleGeometryPrim object at 0x7f15ff3461a0>
                
        """
    @property
    def name(self) -> typing.Optional[str]:
        """
        
                Returns:
                    str: name given to the prim when instantiating it. Otherwise None.
        
                Example:
        
                .. code-block:: python
        
                    >>> plane.name
                    ground_plane
                
        """
    @property
    def prim(self) -> pxr.Usd.Prim:
        """
        
                Returns:
                    Usd.Prim: USD Prim object that this object holds.
        
                Example:
        
                .. code-block:: python
        
                    >>> plane.prim
                    Usd.Prim(</World/GroundPlane>)
                
        """
    @property
    def prim_path(self) -> str:
        """
        
                Returns:
                    str: prim path in the stage.
        
                Example:
        
                .. code-block:: python
        
                    >>> plane.prim_path
                    /World/GroundPlane
                
        """
    @property
    def xform_prim(self) -> isaacsim.core.prims.impl.single_xform_prim.SingleXFormPrim:
        """
        
                Returns:
                    SingleXFormPrim: wrapped object as a SingleXFormPrim
        
                Example:
        
                .. code-block:: python
        
                    >>> plane.xform_prim
                    <isaacsim.core.prims.single_xform_prim.SingleXFormPrim object at 0x7f1578d32560>
                
        """
