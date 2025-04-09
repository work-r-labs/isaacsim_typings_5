from __future__ import annotations
import isaacsim.core.api.materials.deformable_material
from isaacsim.core.api.materials.deformable_material import DeformableMaterial
import isaacsim.core.api.materials.deformable_material_view
from isaacsim.core.api.materials.deformable_material_view import DeformableMaterialView
import isaacsim.core.api.materials.particle_material
from isaacsim.core.api.materials.particle_material import ParticleMaterial
import isaacsim.core.api.materials.particle_material_view
from isaacsim.core.api.materials.particle_material_view import ParticleMaterialView
import isaacsim.core.api.robots.robot
from isaacsim.core.api.robots.robot import Robot
import isaacsim.core.api.robots.robot_view
from isaacsim.core.api.robots.robot_view import RobotView
import isaacsim.core.api.sensors.base_sensor
from isaacsim.core.api.sensors.base_sensor import BaseSensor
import isaacsim.core.api.sensors.rigid_contact_view
from isaacsim.core.api.sensors.rigid_contact_view import RigidContactView
import isaacsim.core.prims.impl.articulation
from isaacsim.core.prims.impl.articulation import Articulation
import isaacsim.core.prims.impl.cloth_prim
from isaacsim.core.prims.impl.cloth_prim import ClothPrim
import isaacsim.core.prims.impl.deformable_prim
from isaacsim.core.prims.impl.deformable_prim import DeformablePrim
import isaacsim.core.prims.impl.geometry_prim
from isaacsim.core.prims.impl.geometry_prim import GeometryPrim
import isaacsim.core.prims.impl.particle_system
from isaacsim.core.prims.impl.particle_system import ParticleSystem
import isaacsim.core.prims.impl.rigid_prim
from isaacsim.core.prims.impl.rigid_prim import RigidPrim
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
import isaacsim.core.prims.impl.single_cloth_prim
from isaacsim.core.prims.impl.single_cloth_prim import SingleClothPrim
import isaacsim.core.prims.impl.single_deformable_prim
from isaacsim.core.prims.impl.single_deformable_prim import SingleDeformablePrim
import isaacsim.core.prims.impl.single_geometry_prim
from isaacsim.core.prims.impl.single_geometry_prim import SingleGeometryPrim
import isaacsim.core.prims.impl.single_particle_system
from isaacsim.core.prims.impl.single_particle_system import SingleParticleSystem
import isaacsim.core.prims.impl.single_rigid_prim
from isaacsim.core.prims.impl.single_rigid_prim import SingleRigidPrim
import isaacsim.core.prims.impl.single_xform_prim
from isaacsim.core.prims.impl.single_xform_prim import SingleXFormPrim
import isaacsim.core.prims.impl.xform_prim
from isaacsim.core.prims.impl.xform_prim import XFormPrim
__all__ = ['Articulation', 'BaseSensor', 'ClothPrim', 'DeformableMaterial', 'DeformableMaterialView', 'DeformablePrim', 'GeometryPrim', 'ParticleMaterial', 'ParticleMaterialView', 'ParticleSystem', 'RigidContactView', 'RigidPrim', 'Robot', 'RobotView', 'SceneRegistry', 'SingleArticulation', 'SingleClothPrim', 'SingleDeformablePrim', 'SingleGeometryPrim', 'SingleParticleSystem', 'SingleRigidPrim', 'SingleXFormPrim', 'XFormPrim']
class SceneRegistry:
    """
    Class to keep track of the different types of objects added to the scene
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.api.scenes import SceneRegistry
            >>>
            >>> scene_registry = SceneRegistry()
            >>> scene_registry
            <isaacsim.core.api.scenes.scene_registry.SceneRegistry object at 0x...>
        
    """
    def __init__(self) -> None:
        ...
    def add_articulated_system(self, name: str, articulated_system: isaacsim.core.prims.impl.single_articulation.SingleArticulation) -> None:
        """
        Register a ``SingleArticulation`` (or subclass) object
        
                Args:
                    name (str): object name
                    articulated_system (SingleArticulation): object
                
        """
    def add_articulated_view(self, name: str, articulated_view: isaacsim.core.prims.impl.articulation.Articulation) -> None:
        """
        Register a ``Articulation`` (or subclass) object
        
                Args:
                    name (str): object name
                    articulated_view (Articulation): object
                
        """
    def add_cloth(self, name: str, cloth: isaacsim.core.prims.impl.single_cloth_prim.SingleClothPrim) -> None:
        """
        Register a ``SingleClothPrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    cloth (SingleClothPrim): object
                
        """
    def add_cloth_view(self, name: str, cloth_prim_view: isaacsim.core.prims.impl.cloth_prim.ClothPrim) -> None:
        """
        Register a ``ClothPrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    cloth_prim_view (ClothPrim): object
                
        """
    def add_deformable(self, name: str, deformable: isaacsim.core.prims.impl.single_deformable_prim.SingleDeformablePrim) -> None:
        """
        Register a ``SingleDeformablePrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    deformable (SingleDeformablePrim): object
                
        """
    def add_deformable_material(self, name: str, deformable_material: isaacsim.core.api.materials.deformable_material.DeformableMaterial) -> None:
        """
        Register a ``DeformableMaterial`` (or subclass) object
        
                Args:
                    name (str): object name
                    deformable_material (DeformableMaterial): object
                
        """
    def add_deformable_material_view(self, name: str, deformable_material_view: isaacsim.core.api.materials.deformable_material_view.DeformableMaterialView) -> None:
        """
        Register a ``DeformableMaterialView`` (or subclass) object
        
                Args:
                    name (str): object name
                    deformable_material_view (DeformableMaterialView): object
                
        """
    def add_deformable_view(self, name: str, deformable_prim_view: isaacsim.core.prims.impl.deformable_prim.DeformablePrim) -> None:
        """
        Register a ``DeformablePrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    deformable_prim_view (DeformablePrim): object
                
        """
    def add_geometry_object(self, name: str, geometry_object: isaacsim.core.prims.impl.single_geometry_prim.SingleGeometryPrim) -> None:
        """
        Register a ``SingleGeometryPrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    geometry_object (SingleGeometryPrim): object
                
        """
    def add_geometry_prim_view(self, name: str, geometry_prim_view: isaacsim.core.prims.impl.geometry_prim.GeometryPrim) -> None:
        """
        Register a ``GeometryPrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    geometry_prim_view (GeometryPrim): object
                
        """
    def add_particle_material(self, name: str, particle_material: isaacsim.core.api.materials.particle_material.ParticleMaterial) -> None:
        """
        Register a ``ParticleMaterial`` (or subclass) object
        
                Args:
                    name (str): object name
                    particle_material (ParticleMaterial): object
                
        """
    def add_particle_material_view(self, name: str, particle_material_view: isaacsim.core.api.materials.particle_material_view.ParticleMaterialView) -> None:
        """
        Register a ``ParticleMaterialView`` (or subclass) object
        
                Args:
                    name (str): object name
                    particle_material_view (ParticleMaterialView): object
                
        """
    def add_particle_system(self, name: str, particle_system: isaacsim.core.prims.impl.single_particle_system.SingleParticleSystem) -> None:
        """
        Register a ``SingleParticleSystem`` (or subclass) object
        
                Args:
                    name (str): object name
                    particle_system (ParticleSystem): object
                
        """
    def add_particle_system_view(self, name: str, particle_system_view: isaacsim.core.prims.impl.particle_system.ParticleSystem) -> None:
        """
        Register a ``ParticleSystem`` (or subclass) object
        
                Args:
                    name (str): object name
                    particle_system_view (ParticleSystem): object
                
        """
    def add_rigid_contact_view(self, name: str, rigid_contact_view: isaacsim.core.api.sensors.rigid_contact_view.RigidContactView) -> None:
        """
        Register a ``RigidContactView`` (or subclass) object
        
                Args:
                    name (str): object name
                    rigid_contact_view (RigidContactView): object
                
        """
    def add_rigid_object(self, name: str, rigid_object: isaacsim.core.prims.impl.single_rigid_prim.SingleRigidPrim) -> None:
        """
        Register a ``SingleRigidPrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    rigid_object (SingleRigidPrim): object
                
        """
    def add_rigid_prim_view(self, name: str, rigid_prim_view: isaacsim.core.prims.impl.rigid_prim.RigidPrim) -> None:
        """
        Register a ``RigidPrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    rigid_prim_view (RigidPrim): object
                
        """
    def add_robot(self, name: str, robot: isaacsim.core.api.robots.robot.Robot) -> None:
        """
        Register a ``Robot`` (or subclass) object
        
                Args:
                    name (str): object name
                    robot (Robot): object
                
        """
    def add_robot_view(self, name: str, robot_view: isaacsim.core.api.robots.robot_view.RobotView) -> None:
        """
        Register a ``RobotView`` (or subclass) object
        
                Args:
                    name (str): object name
                    robot_view (RobotView): object
                
        """
    def add_sensor(self, name: str, sensor: isaacsim.core.api.sensors.base_sensor.BaseSensor) -> None:
        """
        Register a ``BaseSensor`` (or subclass) object
        
                Args:
                    name (str): object name
                    sensor (BaseSensor): object
                
        """
    def add_xform(self, name: str, xform: isaacsim.core.prims.impl.single_xform_prim.SingleXFormPrim) -> None:
        """
        Register a ``SingleXFormPrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    robot (Robot): object
                
        """
    def add_xform_view(self, name: str, xform_prim_view: isaacsim.core.prims.impl.xform_prim.XFormPrim) -> None:
        """
        Register a ``XFormPrim`` (or subclass) object
        
                Args:
                    name (str): object name
                    xform_prim_view (XFormPrim): object
                
        """
    def get_object(self, name: str) -> isaacsim.core.prims.impl.single_xform_prim.SingleXFormPrim:
        """
        Get a registered object by its name if exists otherwise None
        
                Args:
                    name (str): object name
        
                Returns:
                    SingleXFormPrim: the object if it exists otherwise None
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered ground plane named 'default_ground_plane'
                    >>> scene_registry.get_object("default_ground_plane")
                    <isaacsim.core.api.objects.ground_plane.GroundPlane object at 0x...>
                
        """
    def name_exists(self, name: str) -> bool:
        """
        Check if an object exists in the registry by its name
        
                Args:
                    name (str): object name
        
                Returns:
                    bool: whether the object is registered or not
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered ground plane named 'default_ground_plane'
                    >>> scene_registry.name_exists("default_ground_plane")
                    True
                
        """
    def remove_object(self, name: str) -> None:
        """
        Remove and object from the registry
        
                .. note::
        
                    This method will only remove the object from the internal registry.
                    The wrapped object will not be removed from the USD stage
        
                Args:
                    name (str): object name
        
                Raises:
                    Exception: If the name doesn't exist in the registry
        
                Example:
        
                .. code-block:: python
        
                    >>> # given a registered ground plane named 'default_ground_plane'
                    >>> scene_registry.remove_object("default_ground_plane")
                
        """
    @property
    def articulated_systems(self) -> dict:
        """
        Registered ``SingleArticulation`` objects
        """
    @property
    def articulated_views(self) -> dict:
        """
        Registered ``Articulation`` objects
        """
    @property
    def cloth_prim_views(self) -> dict:
        """
        Registered ``ClothPrim`` objects
        """
    @property
    def cloth_prims(self) -> dict:
        """
        Registered ``SingleClothPrim`` objects
        """
    @property
    def deformable_material_views(self) -> dict:
        """
        Registered ``DeformableMaterialView`` objects
        """
    @property
    def deformable_materials(self) -> dict:
        """
        Registered ``DeformableMaterial`` objects
        """
    @property
    def deformable_prim_views(self) -> dict:
        """
        Registered ``DeformablePrim`` objects
        """
    @property
    def deformable_prims(self) -> dict:
        """
        Registered ``SingleDeformablePrim`` objects
        """
    @property
    def geometry_prim_views(self) -> dict:
        """
        Registered ``GeometryPrim`` objects
        """
    @property
    def particle_material_views(self) -> dict:
        """
        Registered ``particle_material_view`` objects
        """
    @property
    def particle_materials(self) -> dict:
        """
        Registered ``ParticleMaterial`` objects
        """
    @property
    def particle_system_views(self) -> dict:
        """
        Registered ``ParticleSystem`` objects
        """
    @property
    def particle_systems(self) -> dict:
        """
        Registered ``SingleParticleSystem`` objects
        """
    @property
    def rigid_contact_views(self) -> dict:
        """
        Registered ``RigidContactView`` objects
        """
    @property
    def rigid_objects(self) -> dict:
        """
        Registered ``SingleRigidPrim`` objects
        """
    @property
    def rigid_prim_views(self) -> dict:
        """
        Registered ``RigidPrim`` objects
        """
    @property
    def robot_views(self) -> dict:
        """
        Registered ``RobotView`` objects
        """
    @property
    def robots(self) -> dict:
        """
        Registered ``Robot`` objects
        """
    @property
    def sensors(self) -> dict:
        """
        Registered ``BaseSensor`` (and derived) objects
        """
    @property
    def xform_prim_views(self) -> dict:
        """
        Registered ``XFormPrim`` objects
        """
    @property
    def xforms(self) -> dict:
        """
        Registered ``SingleXFormPrim`` objects
        """
