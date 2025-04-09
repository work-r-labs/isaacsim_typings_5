from __future__ import annotations
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
from isaacsim.core.utils.extensions import get_extension_path_from_name
import isaacsim.robot_motion.motion_generation.articulation_kinematics_solver
from isaacsim.robot_motion.motion_generation.articulation_kinematics_solver import ArticulationKinematicsSolver
from isaacsim.robot_motion.motion_generation.lula.kinematics import LulaKinematicsSolver
import os as os
__all__ = ['ArticulationKinematicsSolver', 'KinematicsSolver', 'LulaKinematicsSolver', 'SingleArticulation', 'get_extension_path_from_name', 'os']
class KinematicsSolver(isaacsim.robot_motion.motion_generation.articulation_kinematics_solver.ArticulationKinematicsSolver):
    """
    Kinematics Solver for UR10 robot.  This class loads a LulaKinematicsSolver object
    
        Args:
            robot_articulation (SingleArticulation): An initialized Articulation object representing this UR10
            end_effector_frame_name (Optional[str]): The name of the UR10 end effector.  If None, an end effector link will
                be automatically selected.  Defaults to None.
            attach_gripper (Optional[bool]): If True, a URDF will be loaded that includes a suction gripper.  Defaults to False.
        
    """
    def __init__(self, robot_articulation: isaacsim.core.prims.impl.single_articulation.SingleArticulation, end_effector_frame_name: typing.Optional[str] = None, attach_gripper: typing.Optional[bool] = False) -> None:
        ...
