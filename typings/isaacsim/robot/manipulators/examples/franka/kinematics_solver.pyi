from __future__ import annotations
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
import isaacsim.robot_motion.motion_generation.articulation_kinematics_solver
from isaacsim.robot_motion.motion_generation.articulation_kinematics_solver import ArticulationKinematicsSolver
from isaacsim.robot_motion.motion_generation import interface_config_loader
from isaacsim.robot_motion.motion_generation.lula.kinematics import LulaKinematicsSolver
__all__ = ['ArticulationKinematicsSolver', 'KinematicsSolver', 'LulaKinematicsSolver', 'SingleArticulation', 'interface_config_loader']
class KinematicsSolver(isaacsim.robot_motion.motion_generation.articulation_kinematics_solver.ArticulationKinematicsSolver):
    """
    Kinematics Solver for Franka robot.  This class loads a LulaKinematicsSovler object
    
        Args:
            robot_articulation (SingleArticulation): An initialized Articulation object representing this Franka
            end_effector_frame_name (Optional[str]): The name of the Franka end effector.  If None, an end effector link will
                be automatically selected.  Defaults to None.
        
    """
    def __init__(self, robot_articulation: isaacsim.core.prims.impl.single_articulation.SingleArticulation, end_effector_frame_name: typing.Optional[str] = None) -> None:
        ...
