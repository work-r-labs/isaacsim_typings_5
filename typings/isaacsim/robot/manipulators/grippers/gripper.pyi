from __future__ import annotations
from abc import abstractmethod
import isaacsim.core.prims.impl.single_rigid_prim
from isaacsim.core.prims.impl.single_rigid_prim import SingleRigidPrim
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
import omni as omni
__all__ = ['ArticulationAction', 'Gripper', 'SingleRigidPrim', 'abstractmethod', 'omni']
class Gripper(isaacsim.core.prims.impl.single_rigid_prim.SingleRigidPrim):
    """
    Provides high level functions to set/ get properties and actions of a gripper.
    
        Args:
            end_effector_prim_path (str): prim path of the Prim that corresponds to the gripper root/ end effector.
        
    """
    def __init__(self, end_effector_prim_path: str) -> None:
        ...
    def close(self) -> None:
        """
        Applies actions to the articulation that closes the gripper (ex: to hold an object).
        """
    def forward(self, *args, **kwargs) -> isaacsim.core.utils.types.ArticulationAction:
        """
        calculates the ArticulationAction for all of the articulation joints that corresponds to a specific action
                   such as "open" for an example.
        
                Returns:
                    ArticulationAction: articulation action to be passed to the articulation itself
                                        (includes all joints of the articulation).
                
        """
    def get_default_state(self, *args, **kwargs):
        """
        Gets the default state of the gripper
        """
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and creates a rigid prim view using physX tensor api.
                    This needs to be called after each hard reset (i.e stop + play on the timeline) before interacting with any
                    of the functions of this class.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
                
        """
    def open(self) -> None:
        """
        Applies actions to the articulation that opens the gripper (ex: to release an object held).
        """
    def set_default_state(self, *args, **kwargs):
        """
        Sets the default state of the gripper
        """
