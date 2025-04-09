from __future__ import annotations
import carb as carb
import functools as functools
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
import isaacsim.core.utils.types
from isaacsim.core.utils.types import ArticulationAction
from isaacsim.core.utils.types import JointsState
import numpy as np
import numpy
__all__ = ['ArticulationAction', 'ArticulationSubset', 'JointsState', 'SingleArticulation', 'carb', 'functools', 'np', 'require_initialized']
class ArticulationSubset:
    """
    A utility class for viewing a subset of the joints in a robot Articulation object.
    
        This class can be helpful in two ways:
    
        1) The order of joints returned by a robot Articulation may not match the order of joints
           expected by a function
    
        2) A function may only care about a subset of the joint states that are returned by a robot
           Articulation.
    
        Example:
    
            Suppose the robot Articulation returns positions [0,1,2] for joints ["A","B","C"], and
            suppose that we pass joint_names = ["B","A"].
    
            ArticulationSubset.get_joint_positions() -> [1,0]
            ArticulationSubset.map_to_articulation_order([1,0]) -> [0,1,None]
    
        Args:
            articulation (SingleArticulation):
                An initialized SingleArticulation object representing the simulated robot
            joint_names (List[str]):
                A list of joint names whose order determines the order of the joints returned by
                functions like get_joint_positions()
    """
    def __init__(self, articulation: isaacsim.core.prims.impl.single_articulation.SingleArticulation, joint_names: typing.List[str]) -> None:
        ...
    def _get_joint_indices(self):
        """
        Internal member which initializes the subset's joint indices from the specified names
                the first time through and returns that from then on out.
                
        """
    def apply_action(self, *args, **kwargs) -> None:
        """
        Apply the specified control actions to this views joints.
        
                Args:
                    joint_positions: Target joint positions for this subset's joints.
                    joint_velocities: Target joint velocities for this subset's joints.
                
        """
    def get_applied_action(self, *args, **kwargs) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Retrieves the latest applied action for this subset.
        
                Returns: The ArticulationAction for this subset. Each commanded entry is either None or
                contains one value for each of the subset's joints. The joint_indices is set to this
                subset's joint indices.
                
        """
    def get_joint_efforts(self, *args, **kwargs) -> numpy.array:
        """
        Get joint efforts for the joint names that were passed into this articulation view on
                initialization.  The indices of the joint efforts returned correspond to the indices of the
                joint names.
        
                Returns:
                    np.array: joint efforts
                
        """
    def get_joint_positions(self, *args, **kwargs) -> numpy.array:
        """
        Get joint positions for the joint names that were passed into this articulation view on
                initialization.  The indices of the joint positions returned correspond to the indices of
                the joint names.
        
                Returns:
                    np.array: joint positions
                
        """
    def get_joint_subset_indices(self) -> numpy.array:
        """
        Accessor for the joint indices for this subset. These are the indices into the full
                articulation degrees of freedom corresponding to this subset of joints.
        
                Returns:
                    np.array: An array of joint indices defining the subset.
                
        """
    def get_joint_velocities(self, *args, **kwargs) -> numpy.array:
        """
        Get joint velocities for the joint names that were passed into this articulation view on
                initialization.  The indices of the joint velocities returned correspond to the indices of
                the joint names.
        
                Returns:
                    np.array: joint velocities
                
        """
    def get_joints_state(self, *args, **kwargs) -> isaacsim.core.utils.types.JointsState:
        ...
    def make_articulation_action(self, *args, **kwargs) -> isaacsim.core.utils.types.ArticulationAction:
        """
        Make an articulation action for only this subset's joints using the given target
                position and velocity values.
        
                Args:
                    joint_positions: Target joint positions for this subset's joints.
                    joint_velocities: Target joint velocities for this subset's joints.
        
                Returns: An ArticulationAction object specifying the action for this subset's joints.
                
        """
    def map_to_articulation_order(self, *args, **kwargs) -> numpy.array:
        """
        Map a set of joint values to a format consumable by the robot Articulation.
        
                Args:
                    joint_values (np.array): a set of joint values corresponding to the joint_names used to initialize this class.
                        joint_values may be either one or two dimensional.
        
                        If one dimensional with shape (k,): A vector will be returned with length (self.articulation.num_dof) that may
                        be consumed by the robot Articulation in an ArticulationAction.
        
                        If two dimensional with shape (N, k): A matrix will be returned with shape (N, self.articulation.num_dof) that may be
                        converted to N ArticulationActions
        
                Returns:
                    np.array: a set of joint values that is padded with None to match the shape and order expected by the robot Articulation.
                
        """
    def set_joint_efforts(self, *args, **kwargs) -> None:
        """
        Set the joint efforts for this view.
        
                Args:
                    efforts: The effort values, one for each view joint in the order specified on
                    construction.
                
        """
    def set_joint_positions(self, *args, **kwargs) -> None:
        """
        Set the joint positions for this view.
        
                Args:
                    positions: The position values, one for each view joint in the order specified on
                    construction.
                
        """
    def set_joint_velocities(self, *args, **kwargs) -> None:
        """
        Set the joint velocities for this view.
        
                Args:
                    velocities: The velocity values, one for each view joint in the order specified on
                    construction.
                
        """
    @property
    def is_initialized(self):
        """
        Returns whether or not the underlying articulation object has been initialized.
        """
    @property
    def joint_indices(self):
        ...
    @property
    def num_joints(self):
        ...
def require_initialized(func):
    """
    Prints a warning if the underlying articulation isn't initialized and returns None. If it
        is initialized, the function is called as usual and the value returned.
        
    """
