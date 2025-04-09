from __future__ import annotations
import carb as carb
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
from isaacsim.core.utils.carb import get_carb_setting
from isaacsim.core.utils.carb import set_carb_setting
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_path
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_current_stage
from isaacsim.core.utils.stage import get_stage_units
from isaacsim.core.utils.stage import traverse_stage
import omni as omni
from pxr import Gf
from pxr import PhysxSchema
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
from pxr import UsdShade
__all__ = ['AXES_INDICES', 'Gf', 'PhysicsContext', 'PhysxSchema', 'Sdf', 'SimulationManager', 'Usd', 'UsdGeom', 'UsdPhysics', 'UsdShade', 'carb', 'get_carb_setting', 'get_current_stage', 'get_prim_at_path', 'get_prim_path', 'get_stage_units', 'is_prim_path_valid', 'omni', 'set_carb_setting', 'traverse_stage']
class PhysicsContext:
    """
    Provides high level functions to deal with a physics scene and its settings. This will create a
           a PhysicsScene prim at the specified prim path in case there is no PhysicsScene present in the current
           stage.
           If there is a PhysicsScene present, it will discard the prim_path specified and sets the
           default settings on the current PhysicsScene found.
    
        Args:
            physics_dt (float, optional): specifies the physics_dt of the simulation. Defaults to 1.0 / 60.0.
            prim_path (Optional[str], optional): specifies the prim path to create a PhysicsScene at,
                                                 only in the case where no PhysicsScene already defined.
                                                 Defaults to "/physicsScene".
            set_defaults (bool, optional): set to True to use the defaults physics parameters
                                            [physics_dt = 1.0/ 60.0,
                                            gravity = -9.81 m / s
                                            ccd_enabled,
                                            stabilization_enabled,
                                            gpu dynamics turned off,
                                            broadcast type is MBP,
                                            solver type is TGS]. Defaults to True.
    
        Raises:
            Exception: If prim_path is not absolute.
            Exception: if prim_path already exists and its type is not a PhysicsScene.
        
    """
    def __del__(self):
        ...
    def __init__(self, physics_dt: typing.Optional[float] = None, prim_path: str = '/physicsScene', sim_params: dict = None, set_defaults: bool = True) -> None:
        ...
    def _create_new_physics_scene(self, prim_path: str):
        ...
    def _step(self, current_time: float) -> None:
        ...
    def enable_ccd(self, flag: bool) -> None:
        """
        Enables a second broad phase after integration that makes it possible to prevent objects from tunneling
                   through each other.
        
                Args:
                    flag (bool): enables or disables ccd on the PhysicsScene
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def enable_fabric(self, enable):
        ...
    def enable_gpu_dynamics(self, flag: bool) -> None:
        """
        Enables gpu dynamics pipeline, required for deformables for instance.
        
                Args:
                    flag (bool): enables or disables gpu dynamics on the PhysicsScene
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def enable_residual_reporting(self, flag: bool):
        """
        Set the physx scene flag to enable/disable solver residual reporting.
        
                Args:
                    flag (bool): enables or disables scene residuals on the PhysicsScene
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def enable_stablization(self, flag: bool) -> None:
        """
        Enables additional stabilization pass in the solver.
        
                Args:
                    flag (bool): enables or disables stabilization on the PhysicsScene
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def get_bounce_threshold(self) -> float:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    float: [description]
                
        """
    def get_broadphase_type(self) -> str:
        """
        Gets current broadcast phase algorithm type.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    str: Broadcast phase algorithm used.
                
        """
    def get_current_physics_scene_prim(self) -> typing.Optional[pxr.Usd.Prim]:
        """
        Used to return the PhysicsScene prim in stage by traversing the stage.
        
                Returns:
                    Optional[Usd.Prim]: returns a PhysicsScene prim if found in current stage. Otherwise, None.
                
        """
    def get_enable_scene_query_support(self) -> bool:
        """
        Retrieves the Enable Scene Query Support attribute in Physx Scene
        
                Raises:
                    Exception: [description]
        
                Returns:
                    bool: enable scene query support attribute
                
        """
    def get_friction_correlation_distance(self) -> float:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    float: [description]
                
        """
    def get_friction_offset_threshold(self) -> float:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    float: [description]
                
        """
    def get_gpu_collision_stack_size(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_found_lost_aggregate_pairs_capacity(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_found_lost_pairs_capacity(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_heap_capacity(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_max_num_partitions(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_max_particle_contacts(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_max_rigid_contact_count(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_max_rigid_patch_count(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_max_soft_body_contacts(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_temp_buffer_capacity(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gpu_total_aggregate_pairs_capacity(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_gravity(self) -> typing.Tuple[typing.List, float]:
        """
        Gets current gravity.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    Tuple[list, float]: returns a tuple, first element corresponds to the gravity direction vector and second element is the magnitude.
                
        """
    def get_invert_collision_group_filter(self) -> int:
        """
        [summary]
        
                Raises:
                    Exception: [description]
        
                Returns:
                    int: [description]
                
        """
    def get_physics_dt(self) -> float:
        """
        Returns the current physics dt.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    float: physics dt.
                
        """
    def get_physx_update_transformations_settings(self) -> typing.Tuple[bool, bool, bool, bool]:
        """
        Gets how physx syncs with the usd when transformations are updated.
        
                Returns:
                    Tuple[bool, bool, bool, bool]: [update_to_usd, update_velocities_to_usd, output_velocities_local_space]
                
        """
    def get_solver_position_residual(self, report_max: bool = True):
        """
        Enable physics scene residual reporting API and chooses between RMS vs Max criteri for position residuals.
        
                Args:
                    report_max (bool): Use the max residual criterion if True, otherwise use the RMS criterion.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def get_solver_type(self) -> str:
        """
        Gets current solver type.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    str: solver used for simulation.
                
        """
    def get_solver_velocity_residual(self, report_max: bool = True):
        """
        Enable physics scene residual reporting API and chooses between RMS vs Max criteri for velocity residuals.
        
                Args:
                    report_max (bool): Use the max residual criterion if True, otherwise use the RMS criterion.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def is_ccd_enabled(self) -> bool:
        """
        Checks if ccd is enabled.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    bool: True if ccd is enabled, otherwise False.
                
        """
    def is_gpu_dynamics_enabled(self) -> bool:
        """
        Checks if Gpu Dynamics is enabled.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    bool: True if Gpu Dynamics is enabled, otherwise False.
                
        """
    def is_stablization_enabled(self) -> bool:
        """
        Checks if stabilization is enabled.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
        
                Returns:
                    bool: True if stabilization is enabled, otherwise False.
                
        """
    def set_bounce_threshold(self, value: float) -> None:
        """
        [summary]
        
                Args:
                    value (float): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_broadphase_type(self, broadcast_type: str) -> None:
        """
        Broadcast phase algorithm used in simulation.
        
                Args:
                    broadcast_type (str): type of broadcasting to be used, can be "MBP"
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def set_enable_scene_query_support(self, enable_scene_query_support: bool) -> None:
        """
        Sets the Enable Scene Query Support attribute in Physx Scene
        
                Args:
                    enable_scene_query_support (bool): Whether to enable scene query support
        
                Raises:
                    Exception: [description]
                
        """
    def set_friction_correlation_distance(self, value: float) -> None:
        """
        [summary]
        
                Args:
                    value (float): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_friction_offset_threshold(self, value: float) -> None:
        """
        [summary]
        
                Args:
                    value (float): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_collision_stack_size(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_found_lost_aggregate_pairs_capacity(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_found_lost_pairs_capacity(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_heap_capacity(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_max_num_partitions(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_max_particle_contacts(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_max_rigid_contact_count(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_max_rigid_patch_count(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_max_soft_body_contacts(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_temp_buffer_capacity(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gpu_total_aggregate_pairs_capacity(self, value: int) -> None:
        """
        [summary]
        
                Args:
                    value (int): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_gravity(self, value: float) -> None:
        """
        sets the gravity direction and magnitude.
        
                Args:
                    value (float): gravity value to be used in simulation.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def set_invert_collision_group_filter(self, invert_collision_group_filter: bool) -> None:
        """
        [summary]
        
                Args:
                    invert_collision_group_filter (bool): [description]
        
                Raises:
                    Exception: [description]
                
        """
    def set_physics_dt(self, dt: float = 0.016666666666666666, substeps: int = 1) -> None:
        """
        Sets the physics dt on the PhysicsScene
        
                Args:
                    dt (float, optional): physics dt. Defaults to 1.0/60.0.
                    substeps (int, optional): number of physics steps to run for before rendering a frame. Defaults to 1.
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                    ValueError: Physics dt must be a >= 0.
                    ValueError: Physics dt must be a <= 1.0.
                
        """
    def set_physx_update_transformations_settings(self, update_to_usd: typing.Optional[bool] = None, update_velocities_to_usd: typing.Optional[bool] = None, output_velocities_local_space: typing.Optional[bool] = None) -> None:
        """
        Sets how physx syncs with the usd when transformations are updated.
        
                Args:
                    update_to_usd (bool, optional): Updates to USD the transformations. Defaults to True.
                    update_velocities_to_usd (bool, optional): Updates Velocities to USD. Defaults to True.
                    output_velocities_local_space (bool, optional): Output the velocities in the local frame and not the world frame. Defaults to False.
                
        """
    def set_solver_type(self, solver_type: str) -> None:
        """
        solver used for simulation.
        
                Args:
                    solver_type (str): can be "TGS" or "PGS". for references look at..
        
                Raises:
                    Exception: If the prim path registered in context doesn't correspond to a valid prim path currently.
                
        """
    def warm_start(self):
        ...
    @property
    def device(self) -> str:
        ...
    @property
    def prim_path(self):
        ...
    @property
    def use_fabric(self):
        ...
    @property
    def use_gpu_pipeline(self):
        ...
    @property
    def use_gpu_sim(self):
        ...
AXES_INDICES: dict = {'X': 0, 'x': 0, 'Y': 1, 'y': 1, 'Z': 2, 'z': 2}
