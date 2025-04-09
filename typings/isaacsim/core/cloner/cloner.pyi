from __future__ import annotations
import carb as carb
from isaacsim.core.simulation_manager.impl.simulation_manager import SimulationManager
import numpy as np
import omni as omni
from omni.physx import get_physx_replicator_interface
from omni.physx import get_physx_simulation_interface
from pxr import Gf
from pxr import PhysxSchema
from pxr import Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdUtils
from pxr import Vt
import torch as torch
__all__ = ['Cloner', 'Gf', 'PhysxSchema', 'Sdf', 'SimulationManager', 'Usd', 'UsdGeom', 'UsdUtils', 'Vt', 'carb', 'get_physx_replicator_interface', 'get_physx_simulation_interface', 'np', 'omni', 'torch']
class Cloner:
    """
    This class provides a set of simple APIs to make duplication of objects simple.
        Objects can be cloned using this class to create copies of the same object,
        placed at user-specified locations in the scene.
    
        Note that the cloning process is performed in a for-loop, so performance should
        be expected to follow linear scaling with an increase of clones.
        
    """
    def __init__(self, stage: pxr.Usd.Stage = None):
        """
        
                Args:
                    stage (Usd.Stage): Usd stage where source prim and clones are added to.
                
        """
    def clone(self, source_prim_path: str, prim_paths: typing.List[str], positions: typing.Union[numpy.ndarray, torch.Tensor] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor] = None, replicate_physics: bool = False, base_env_path: str = None, root_path: str = None, copy_from_source: bool = False, unregister_physics_replication: bool = False, enable_env_ids: bool = False):
        """
        Clones a source prim at user-specified destination paths.
                    Clones will be placed at user-specified positions and orientations.
        
                Args:
                    source_prim_path (str): Path of source object.
                    prim_paths (List[str]): List of destination paths.
                    positions (Union[np.ndarray, torch.Tensor]): An array containing target positions of clones. Dimension must equal length of prim_paths.
                                            Defaults to None. Clones will be placed at (0, 0, 0) if not specified.
                    orientations (Union[np.ndarray, torch.Tensor]): An array containing target orientations of clones. Dimension must equal length of prim_paths.
                                            Defaults to None. Clones will have identity orientation (1, 0, 0, 0) if not specified.
                    replicate_physics (bool): Uses omni.physics replication. This will replicate physics properties directly for paths beginning with root_path and skip physics parsing for anything under the base_env_path.
                    base_env_path (str): Path to namespace for all environments. Required if replicate_physics=True and define_base_env() not called.
                    root_path (str): Prefix path for each environment. Required if replicate_physics=True and generate_paths() not called.
                    copy_from_source: (bool): Setting this to False will inherit all clones from the source prim; any changes made to the source prim will be reflected in the clones.
                                 Setting this to True will make copies of the source prim when creating new clones; changes to the source prim will not be reflected in clones. Defaults to False. Note that setting this to True will take longer to execute.
                    unregister_physics_replication (bool): Setting this to True will unregister the physics replicator on the current stage.
                    enable_env_ids (bool): Setting this enables co-location of clones in physics with automatic filtering of collisions between clones.
                Raises:
                    Exception: Raises exception if source prim path is not valid.
        
                
        """
    def define_base_env(self, base_env_path: str):
        """
        Creates a USD Scope at base_env_path. This is designed to be the parent that holds all clones.
        
                Args:
                    base_env_path (str): Path to create the USD Scope at.
                
        """
    def disable_change_listener(self):
        ...
    def enable_change_listener(self):
        ...
    def filter_collisions(self, physicsscene_path: str, collision_root_path: str, prim_paths: typing.List[str], global_paths: typing.List[str] = list()):
        """
        Filters collisions between clones. Clones will not collide with each other, but can collide with objects specified in global_paths.
        
                Args:
                    physicsscene_path (str): Path to PhysicsScene object in stage.
                    collision_root_path (str): Path to place collision groups under.
                    prim_paths (List[str]): Paths of objects to filter out collision.
                    global_paths (List[str]): Paths of objects to generate collision (e.g. ground plane).
        
                
        """
    def generate_paths(self, root_path: str, num_paths: int):
        """
        Generates a list of paths under the root path specified.
        
                Args:
                    root_path (str): Base path where new paths will be created under.
                    num_paths (int): Number of paths to generate.
        
                Returns:
                    paths (List[str]): A list of paths
                
        """
    def replicate_physics(self, source_prim_path: str, prim_paths: list, base_env_path: str, root_path: str, enable_env_ids: bool = False):
        """
        Replicates physics properties directly in omni.physics to avoid performance bottlenecks when parsing physics.
        
                Args:
                    source_prim_path (str): Path of source object.
                    prim_paths (List[str]): List of destination paths.
                    base_env_path (str): Path to namespace for all environments.
                    root_path (str): Prefix path for each environment.
                    useEnvIds (bool): Whether to use envIDs functionality in physics to enable co-location of clones. Clones will be filtered automatically.
                Raises:
                    Exception: Raises exception if base_env_path is None or root_path is None.
        
                
        """
