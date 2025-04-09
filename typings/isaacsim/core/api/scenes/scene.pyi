from __future__ import annotations
import builtins as builtins
import carb as carb
import gc as gc
from isaacsim.core.api.materials.deformable_material import DeformableMaterial
from isaacsim.core.api.materials.deformable_material_view import DeformableMaterialView
from isaacsim.core.api.materials.particle_material import ParticleMaterial
from isaacsim.core.api.materials.particle_material_view import ParticleMaterialView
from isaacsim.core.api.materials.physics_material import PhysicsMaterial
import isaacsim.core.api.objects.ground_plane
from isaacsim.core.api.objects.ground_plane import GroundPlane
from isaacsim.core.api.robots.robot import Robot
from isaacsim.core.api.robots.robot_view import RobotView
from isaacsim.core.api.scenes.scene_registry import SceneRegistry
from isaacsim.core.api.sensors.base_sensor import BaseSensor
from isaacsim.core.api.sensors.rigid_contact_view import RigidContactView
from isaacsim.core.prims.impl.articulation import Articulation
from isaacsim.core.prims.impl.cloth_prim import ClothPrim
from isaacsim.core.prims.impl.deformable_prim import DeformablePrim
from isaacsim.core.prims.impl.geometry_prim import GeometryPrim
from isaacsim.core.prims.impl.particle_system import ParticleSystem
from isaacsim.core.prims.impl.rigid_prim import RigidPrim
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
from isaacsim.core.prims.impl.single_cloth_prim import SingleClothPrim
from isaacsim.core.prims.impl.single_deformable_prim import SingleDeformablePrim
from isaacsim.core.prims.impl.single_geometry_prim import SingleGeometryPrim
from isaacsim.core.prims.impl.single_particle_system import SingleParticleSystem
from isaacsim.core.prims.impl.single_rigid_prim import SingleRigidPrim
import isaacsim.core.prims.impl.single_xform_prim
from isaacsim.core.prims.impl.single_xform_prim import SingleXFormPrim
from isaacsim.core.prims.impl.xform_prim import XFormPrim
from isaacsim.core.utils.prims import get_prim_children
from isaacsim.core.utils.prims import get_prim_parent
from isaacsim.core.utils.prims import get_prim_path
from isaacsim.core.utils.prims import is_prim_ancestral
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.prims import is_prim_root_path
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.utils.stage import get_current_stage
from isaacsim.core.utils.stage import update_stage
from isaacsim.core.utils.string import find_unique_string_name
from isaacsim.storage.native.nucleus import get_assets_root_path
import numpy as np
import omni as omni
from pxr import Sdf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
__all__ = ['Articulation', 'BaseSensor', 'ClothPrim', 'DeformableMaterial', 'DeformableMaterialView', 'DeformablePrim', 'GeometryPrim', 'GroundPlane', 'ParticleMaterial', 'ParticleMaterialView', 'ParticleSystem', 'PhysicsMaterial', 'RigidContactView', 'RigidPrim', 'Robot', 'RobotView', 'Scene', 'SceneRegistry', 'Sdf', 'SingleArticulation', 'SingleClothPrim', 'SingleDeformablePrim', 'SingleGeometryPrim', 'SingleParticleSystem', 'SingleRigidPrim', 'SingleXFormPrim', 'Usd', 'UsdGeom', 'XFormPrim', 'add_reference_to_stage', 'builtins', 'carb', 'find_unique_string_name', 'gc', 'get_assets_root_path', 'get_current_stage', 'get_prim_children', 'get_prim_parent', 'get_prim_path', 'is_prim_ancestral', 'is_prim_path_valid', 'is_prim_root_path', 'np', 'omni', 'update_stage']
class Scene:
    """
    Provide methods to add objects of interest in the stage to retrieve their information and set their
        reset default state in an easy way
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.api.scenes import Scene
            >>>
            >>> scene = Scene()
            >>> scene
            <isaacsim.core.api.scenes.scene.Scene object at 0x...>
        
    """
    def __del__(self):
        ...
    def __init__(self) -> None:
        ...
    def _finalize(self, physics_sim_view) -> None:
        ...
    def add(self, obj: isaacsim.core.prims.impl.single_xform_prim.SingleXFormPrim) -> isaacsim.core.prims.impl.single_xform_prim.SingleXFormPrim:
        """
        Add an object to the scene registry
        
                Args:
                    obj (SingleXFormPrim): object to be added
        
                Raises:
                    Exception: The object type is not supported yet
        
                Returns:
                    SingleXFormPrim: object
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.core.prims import XFormPrim
                    >>>
                    >>> prims = XFormPrim(prim_paths_expr="/World")
                    >>> scene.add(prims)
                    <isaacsim.core.prims.XFormPrim object at 0x...>
                
        """
    def add_default_ground_plane(self, z_position: float = 0, name = 'default_ground_plane', prim_path: str = '/World/defaultGroundPlane', static_friction: float = 0.5, dynamic_friction: float = 0.5, restitution: float = 0.8) -> isaacsim.core.api.objects.ground_plane.GroundPlane:
        """
        Create a ground plane (using the default asset for Isaac Sim environments) and add it to the scene registry
        
                Args:
                    z_position (float, optional): ground plane position in the z-axis. Defaults to 0.
                    name (str, optional): shortname to be used as a key by Scene class.
                                        Note: needs to be unique if the object is added to the Scene.
                                        Defaults to "default_ground_plane".
                    prim_path (str, optional): prim path of the prim to create. Defaults to "/World/defaultGroundPlane".
                    static_friction (float, optional): static friction coefficient. Defaults to 0.5.
                    dynamic_friction (float, optional): dynamic friction coefficient. Defaults to 0.5.
                    restitution (float, optional): restitution coefficient. Defaults to 0.8.
        
                Returns:
                    GroundPlane: ground plane instance
        
                Example:
        
                .. code-block:: python
        
                    >>> scene.add_default_ground_plane()
                    server...
                    <isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x...>
                
        """
    def add_ground_plane(self, size: typing.Optional[float] = None, z_position: float = 0, name = 'ground_plane', prim_path: str = '/World/groundPlane', static_friction: float = 0.5, dynamic_friction: float = 0.5, restitution: float = 0.8, color: typing.Optional[numpy.ndarray] = None) -> isaacsim.core.api.objects.ground_plane.GroundPlane:
        """
        Create a ground plane and add it to the scene registry
        
                Args:
                    size (Optional[float], optional): length of each edge. Defaults to 5000.0.
                    z_position (float, optional): ground plane position in the z-axis. Defaults to 0.
                    name (str, optional): shortname to be used as a key by Scene class.
                                        Note: needs to be unique if the object is added to the Scene.
                                        Defaults to "ground_plane".
                    prim_path (str, optional): prim path of the prim to create. Defaults to "/World/groundPlane".
                    static_friction (float, optional): static friction coefficient. Defaults to 0.5.
                    dynamic_friction (float, optional): dynamic friction coefficient. Defaults to 0.5.
                    restitution (float, optional): restitution coefficient. Defaults to 0.8.
                    color (Optional[np.ndarray], optional): color of the visual plane. Defaults to None, which means 50% gray
        
                Returns:
                    GroundPlane: ground plane instance
        
                Example:
        
                .. code-block:: python
        
                    >>> scene.add_ground_plane()
                    <isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x...>
                
        """
    def clear(self, registry_only: bool = False) -> None:
        """
        Clear the stage from all added objects to the scene registry.
        
                Args:
                    registry_only (bool, optional): True to remove the object from the scene registry only and not the USD. Defaults to False.
        
                Example:
        
                .. code-block:: python
        
                    >>> scene.clear()
                
        """
    def compute_object_AABB(self, name: str) -> typing.Tuple[numpy.ndarray, numpy.ndarray]:
        """
        Compute the bounding box points (minimum and maximum) of a registered object given its name
        
                .. warning::
        
                    The bounding box computations should be enabled, via the ``enable_bounding_boxes_computations`` method,
                    before querying the Axis-Aligned Bounding Box (AABB) of an object
        
                Args:
                    name (str): object name
        
                Raises:
                    Exception: If the bounding box computation is not enabled
        
                Returns:
                    Tuple[np.ndarray, np.ndarray]: bounding box points (minimum and maximum)
        
                Example:
        
                .. code-block:: python
        
                    >>> scene.enable_bounding_boxes_computations()
                    >>>
                    >>> bbox = scene.compute_object_AABB("ground_plane")
                    >>> bbox[0]  # minimum
                    array([-50., -50.,  0.])
                    >>> bbox[1]  # maximum
                    array([50., 50.,  0.])
                
        """
    def disable_bounding_boxes_computations(self) -> None:
        """
        Disable the bounding boxes computations
        
                Example:
        
                .. code-block:: python
        
                    >>> scene.disable_bounding_boxes_computations()
                
        """
    def enable_bounding_boxes_computations(self) -> None:
        """
        Enable the bounding boxes computations
        
                Example:
        
                .. code-block:: python
        
                    >>> scene.enable_bounding_boxes_computations()
                
        """
    def get_object(self, name: str) -> isaacsim.core.prims.impl.single_xform_prim.SingleXFormPrim:
        """
        Get a registered object by its name if exists otherwise None
        
                .. note::
        
                    Object can be registered via the ``add`` method
        
                Args:
                    name str: object name
        
                Returns:
                    SingleXFormPrim: object if it exists otherwise None
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a default ground plane named 'default_ground_plane'
                    >>> scene.get_object("default_ground_plane")
                    <isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x...>
                
        """
    def object_exists(self, name: str) -> bool:
        """
        Check if an object exists in the scene registry
        
                Args:
                    name (str): object name
        
                Returns:
                    bool: whether the object exists in the scene registry or not
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a default ground plane named 'default_ground_plane'
                    >>> scene.object_exists("default_ground_plane")
                    True
                
        """
    def post_reset(self) -> None:
        """
        Call the ``post_reset`` method on all added objects to the scene registry
        
                Example:
        
                .. code-block:: python
        
                    >>> scene.post_reset()
                
        """
    def remove_object(self, name: str, registry_only: bool = False) -> None:
        """
        Remove and object from the scene registry and the USD stage if specified (enable by default)
        
                Args:
                    name (str): Name of the prim to be removed.
                    registry_only (bool, optional): True to remove the object from the scene registry only and not the USD. Defaults to False.
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a default ground plane named 'default_ground_plane'
                    >>> scene.remove_object("default_ground_plane")
                
        """
    @property
    def stage(self) -> pxr.Usd.Stage:
        """
        
                Returns:
                    Usd.Stage: current USD stage
        
                Example:
        
                .. code-block:: python
        
                    >>> scene.stage
                    Usd.Stage.Open(rootLayer=Sdf.Find('anon:0x...usd'),
                                   sessionLayer=Sdf.Find('anon:0x...usda'),
                                   pathResolverContext=<invalid repr>)
                
        """
