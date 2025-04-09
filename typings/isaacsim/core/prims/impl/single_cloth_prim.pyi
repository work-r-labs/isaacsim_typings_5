from __future__ import annotations
import carb as carb
import isaacsim.core.prims.impl._impl.single_prim_wrapper
from isaacsim.core.prims.impl._impl.single_prim_wrapper import _SinglePrimWrapper
from isaacsim.core.prims.impl.cloth_prim import ClothPrim
import isaacsim.core.prims.impl.single_particle_system
from isaacsim.core.prims.impl.single_particle_system import SingleParticleSystem
from isaacsim.core.utils.stage import get_current_stage
import isaacsim.core.utils.types
from isaacsim.core.utils.types import DynamicState
import numpy as np
from omni.physx.scripts import particleUtils
from omni.physx.scripts import physicsUtils
from pxr import Gf
from pxr import PhysxSchema
from pxr import Sdf
from pxr import UsdGeom
import pxr.UsdGeom
from pxr import UsdPhysics
from pxr import UsdShade
import torch as torch
__all__ = ['ClothPrim', 'DynamicState', 'Gf', 'PhysxSchema', 'Sdf', 'SingleClothPrim', 'SingleParticleSystem', 'UsdGeom', 'UsdPhysics', 'UsdShade', 'carb', 'get_current_stage', 'np', 'particleUtils', 'physicsUtils', 'torch']
class SingleClothPrim(isaacsim.core.prims.impl._impl.single_prim_wrapper._SinglePrimWrapper):
    """
    Cloth primitive object provide functionalities to create and control cloth parameters
    """
    def __init__(self, prim_path: str, particle_system: isaacsim.core.prims.impl.single_particle_system.SingleParticleSystem, particle_material: typing.Optional[ForwardRef('ParticleMaterial')] = None, name: typing.Optional[str] = 'cloth', position: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, scale: typing.Optional[typing.Sequence[float]] = None, visible: typing.Optional[bool] = None, particle_mass: typing.Optional[float] = 0.01, pressure: typing.Optional[float] = None, particle_group: typing.Optional[int] = 0, self_collision: typing.Optional[bool] = True, self_collision_filter: typing.Optional[bool] = True, stretch_stiffness: typing.Optional[float] = None, bend_stiffness: typing.Optional[float] = None, shear_stiffness: typing.Optional[float] = None, spring_damping: typing.Optional[float] = None) -> None:
        """
        Creates a cloth at prim_path given a particle_system and the cloth parameters.
                Args:
                    prim_path (str): the absolute path that the prim is supposed to be registered in.
                    particle_system (SingleParticleSystem): the particle system that this cloth is using.
                    particle_material (ParticleMaterial): the particle material that is cloth is using.
                    name (str, optional): name given to the prim, this can be different than the prim path. Defaults to None.
                    position (Sequence[float], optional): the position of the center of the cloth.
                    orientation (Sequence[float], optional): the initial orientation of the cloth, assuming cloth is flat.
                    scale (Sequence[float], optional): the scale of the cloth.
                    visible (bool, optional): True if the cloth is supposed to be visible, False otherwise.
                    ==================================== particle physic cloth coefficients ====================================
                    particle_mass (float, optional): the mass of one single particle.
                    pressure (float, optional): if > 0, a particle cloth has an additional pressure constraint that provides
                                                inflatable (i.e. balloon-like) dynamics. The pressure times the rest volume
                                                defines the volume the inflatable tries to match. Pressure only works well for
                                                closed or approximately closed meshes, range: [0, inf), units: dimensionless
                    particle_group (int, optional): group Id of the particles, range: [0, 2^20)
                    self_collision (bool, optional): enable self collision of the particles or of the particle object.
                    self_collision_filter (bool, optional): whether the simulation should filter particle-particle collisions
                                                            based on the rest position distances.
                    stretch_stiffness (Sequence[float], optional): represents a stiffness for linear springs placed between particles to
                                                         counteract stretching, range: [0, inf), units: force / distance =
                                                         mass / second / second
                    bend_stiffness (Sequence[float], optional): represents a stiffness for linear springs placed in a way to counteract
                                                      bending, range: [0, inf), units: force / distance = mass / second / second
                    shear_stiffness (Sequence[float], optional): represents a stiffness for linear springs placed in a way to counteract
                                                       shear, range: [0, inf), units: force / distance = mass / second / second
                    spring_damping (Sequence[float], optional): damping on cloth spring constraints. Applies to all constraints
                                                      parameterized by stiffness attributes, range: [0, inf),
                                                      units: force * second / distance = mass / second
                Note:
                    Particles / objects in different groups in the same system collide with each other. Within the same group in
                    the same system, the collision behavior is controlled by the self_collision parameter.
                
        """
    def _get_points_pose(self):
        """
        Return the position of the points of the cloth prim with respect to the center of the cloth prim
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: position of the points that the cloth is composed of.
                
        """
    def get_cloth_bend_stiffness(self) -> float:
        """
        
                Reports a single value that would be used to generate the stiffnesses. This API does not report the actually created stiffnesses.
        
                Returns:
                    float: The bend stiffness.
                
        """
    def get_cloth_damping(self) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Reports a single value that would be used to generate the dampings. This API does not report the actually created dampings.
        
                Returns:
                    float: The spring damping.
                
        """
    def get_cloth_shear_stiffness(self) -> float:
        """
        
                Reports a single value that would be used to generate the stiffnesses. This API does not report the actually created stiffnesses.
        
                Returns:
                    float: The shear stiffness.
                
        """
    def get_cloth_stretch_stiffness(self) -> float:
        """
        
                Reports a single value that would be used to generate the stiffnesses. This API does not report the actually created stiffnesses.
        
                Returns:
                    float: The stretch stiffness.
                
        """
    def get_current_dynamic_state(self) -> isaacsim.core.utils.types.DynamicState:
        """
        Return the DynamicState that contains the position and orientation of the cloth prim
        
                Returns:
                    DynamicState:
                        position (np.ndarray, optional):
                                    position in the world frame of the prim. shape is (3, ).
                                    Defaults to None, which means left unchanged.
                        orientation (np.ndarray, optional):
                                    quaternion orientation in the world frame of the prim.
                                    quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                    Defaults to None, which means left unchanged.
                
        """
    def get_particle_group(self) -> int:
        """
        
                Returns:
                    bool: self collision.
                
        """
    def get_pressure(self) -> float:
        """
        
                Returns:
                    float: pressure value.
                
        """
    def get_self_collision(self) -> bool:
        """
        
                Returns:
                    bool: self collision.
                
        """
    def get_self_collision_filter(self) -> bool:
        """
        
                Returns:
                    bool: self collision filter.
                
        """
    def get_spring_damping(self) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Gets damping values of spring constraints
        
                Returns:
                    Union[np.ndarray, torch.Tensor]: The spring damping.
                
        """
    def get_stretch_stiffness(self) -> typing.Union[numpy.ndarray, torch.Tensor]:
        """
        
                Gets stretch stiffness values of spring constraints
        
                Returns:
                    float: The stretch stiffness.
                
        """
    def set_cloth_bend_stiffness(self, stiffness: float) -> None:
        """
        Sets a single bend stiffness value to all springs constraints in the cloth
        
                Args:
                    stiffness (float): The cloth springs bend stiffness value.
                        Range: [0 , inf), Units: force/distance = mass/second/second
                
        """
    def set_cloth_damping(self, damping: float) -> None:
        """
        Sets a single damping value to all springs constraints in the cloth
        
                Args:
                    damping (float): The cloth springs damping value.
                        Range: [0 , inf), Units: force/velocity = mass/second
                
        """
    def set_cloth_shear_stiffness(self, stiffness: float) -> None:
        """
        Sets a single shear stiffness value to all springs constraints in the cloth
        
                Args:
                    stiffness (float): The cloth springs shear stiffness value.
                        Range: [0 , inf), Units: force/distance = mass/second/second
                
        """
    def set_cloth_stretch_stiffness(self, stiffness: typing.Union[numpy.ndarray, torch.Tensor]) -> None:
        """
        Sets a single stretch stiffness value to all springs constraints in the cloth
        
                Args:
                    stiffness (Union[np.ndarray, torch.Tensor]): The cloth springs stretch stiffness value.
                        Range: [0 , inf), Units: force/distance = mass/second/second
                
        """
    def set_particle_group(self, particle_group: int) -> None:
        """
        
                Args:
                    particle_group(int): particle group.
                
        """
    def set_pressure(self, pressure: float) -> None:
        """
        
                Args:
                    pressure(float): pressure value.
                
        """
    def set_self_collision(self, self_collision: bool) -> None:
        """
        
                Args:
                    self_collision(bool): self collision.
                
        """
    def set_self_collision_filter(self, self_collision_filter: bool) -> None:
        """
        
                Args:
                    self_collision_filter(bool): self collision filter.
                
        """
    def set_spring_damping(self, damping: typing.Union[numpy.ndarray, torch.Tensor]) -> None:
        """
        
                Sets damping values of spring constraints in the cloth
        
                Args:
                    damping (List[float]): The damping values of springs.
                        Range: [0 , inf), Units: force/distance = mass/second
                
        """
    def set_stretch_stiffness(self, stiffness: typing.Union[numpy.ndarray, torch.Tensor]) -> None:
        """
        
                Sets stretch stiffness values of spring constraints in the cloth
                It represents a stiffness for linear springs placed between particles to counteract stretching.
        
                Args:
                    stiffness (Union[np.ndarray, torch.Tensor]): The stretch stiffnesses.
                        Range: [0 , inf), Units: force/distance = mass/second/second
                
        """
    @property
    def mesh(self) -> pxr.UsdGeom.Mesh:
        """
        
                Returns:
                    Usd.Prim: USD Prim object that this object tracks.
                
        """
