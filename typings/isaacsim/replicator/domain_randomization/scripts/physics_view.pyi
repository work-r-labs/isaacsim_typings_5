from __future__ import annotations
import copy as copy
import isaacsim as isaacsim
from isaacsim.core.prims.impl.articulation import Articulation
from isaacsim.core.prims.impl.rigid_prim import RigidPrim
from isaacsim.core.utils.numpy.rotations import quats_to_euler_angles as quat_to_euler_numpy
from isaacsim.replicator.domain_randomization.scripts import context
from isaacsim.replicator.domain_randomization.scripts.context import trigger_randomization
import numpy as np
from omni.replicator.core.scripts import distribution
import omni.replicator.core.scripts.utils.utils
from omni.replicator.core.scripts.utils.utils import ReplicatorItem
from omni.replicator.core.scripts.utils.utils import ReplicatorWrapper
from omni.replicator.core.utils import utils
import torch as torch
__all__ = ['Articulation', 'ReplicatorItem', 'ReplicatorWrapper', 'RigidPrim', 'TENDON_ATTRIBUTES', 'context', 'copy', 'distribution', 'isaacsim', 'np', 'quat_to_euler_numpy', 'quat_to_euler_torch', 'randomize_articulation_view', 'randomize_rigid_prim_view', 'randomize_simulation_context', 'register_articulation_view', 'register_rigid_prim_view', 'register_simulation_context', 'step_randomization', 'torch', 'trigger_randomization', 'utils']
def register_articulation_view(articulation_view: isaacsim.core.prims.impl.articulation.Articulation) -> None:
    """
    
        Args:
            articulation_view (Articulation): Registering the Articulation to be randomized.
        
    """
def register_rigid_prim_view(rigid_prim_view: isaacsim.core.prims.impl.rigid_prim.RigidPrim) -> None:
    """
    
        Args:
            rigid_prim_view (isaacsim.core.prims.RigidPrim): Registering the RigidPrim to be randomized.
        
    """
def register_simulation_context(simulation_context: typing.Union[isaacsim.core.api.simulation_context.simulation_context.SimulationContext, isaacsim.core.api.world.world.World]) -> None:
    """
    
        Args:
            simulation_context (Union[isaacsim.core.api.SimulationContext, isaacsim.core.api.World]): Registering the SimulationContext.
        
    """
def step_randomization(reset_inds: typing.Union[list, numpy.ndarray, torch.Tensor, NoneType] = list()) -> None:
    """
    
        Args:
            reset_inds (Optional[Union[list, np.ndarray, torch.Tensor]]): The indices corresonding to the prims to be reset in the views.
        
    """
TENDON_ATTRIBUTES: list = ['tendon_stiffnesses', 'tendon_dampings', 'tendon_limit_stiffnesses', 'tendon_lower_limits', 'tendon_upper_limits', 'tendon_rest_lengths', 'tendon_offsets']
_articulation_views: dict = {}
_articulation_views_initial_values: dict = {}
_articulation_views_reset_values: dict = {}
_current_tendon_properties: dict = {}
_rigid_prim_views: dict = {}
_rigid_prim_views_initial_values: dict = {}
_rigid_prim_views_reset_values: dict = {}
_simulation_context = None
_simulation_context_initial_values: dict = {}
_simulation_context_reset_values: dict = {}
_write_physics_view_node: omni.replicator.core.scripts.utils.utils.ReplicatorWrapper  # value = <omni.replicator.core.scripts.utils.utils.ReplicatorWrapper object>
quat_to_euler_torch: torch.jit.ScriptFunction  # value = <torch.jit.ScriptFunction object>
randomize_articulation_view: omni.replicator.core.scripts.utils.utils.ReplicatorWrapper  # value = <omni.replicator.core.scripts.utils.utils.ReplicatorWrapper object>
randomize_rigid_prim_view: omni.replicator.core.scripts.utils.utils.ReplicatorWrapper  # value = <omni.replicator.core.scripts.utils.utils.ReplicatorWrapper object>
randomize_simulation_context: omni.replicator.core.scripts.utils.utils.ReplicatorWrapper  # value = <omni.replicator.core.scripts.utils.utils.ReplicatorWrapper object>
