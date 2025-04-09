from __future__ import annotations
import isaacsim.core.prims.impl.single_articulation
from isaacsim.core.prims.impl.single_articulation import SingleArticulation
import isaacsim.core.prims.impl.single_rigid_prim
from isaacsim.core.prims.impl.single_rigid_prim import SingleRigidPrim
import isaacsim.robot.manipulators.grippers.gripper
from isaacsim.robot.manipulators.grippers.gripper import Gripper
from isaacsim.robot.manipulators.grippers.parallel_gripper import ParallelGripper
from isaacsim.robot.manipulators.grippers.surface_gripper import SurfaceGripper
import omni as omni
__all__ = ['Gripper', 'ParallelGripper', 'SingleArticulation', 'SingleManipulator', 'SingleRigidPrim', 'SurfaceGripper', 'omni']
class SingleManipulator(isaacsim.core.prims.impl.single_articulation.SingleArticulation):
    """
    Provides high level functions to set/ get properties and actions of a manipulator with a single end effector
        and optionally a gripper.
    
        Args:
    
            prim_path (str): prim path of the Prim to encapsulate or create.
            end_effector_prim_name (str): end effector prim name to be used to track the rigid body that corresponds
                                            to the end effector. One of the following args can be specified only:
                                            end_effector_prim_name or end_effector_prim_path.
            end_effector_prim_path (str): end effector prim path to be used to track the rigid body that corresponds
                                            to the end effector. One of the following args can be specified only:
                                            end_effector_prim_name or end_effector_prim_path.
            name (str, optional): shortname to be used as a key by Scene class. Note: needs to be unique if the
                                    object is added to the Scene. Defaults to "single_manipulator".
            position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                                (with respect to its parent prim). shape is (3, ).
                                                                Defaults to None, which means left unchanged.
            orientation (Optional[Sequence[float]], optional): quaternion orientation in the world/ local frame of the prim
                                                                (depends if translation or position is specified).
                                                                quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                                Defaults to None, which means left unchanged.
            scale (Optional[Sequence[float]], optional): local scale to be applied to the prim's dimensions. shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            visible (Optional[bool], optional): set to false for an invisible prim in the stage while rendering. Defaults to True.
            gripper (Gripper, optional): Gripper to be used with the manipulator. Defaults to None.
        
    """
    def __init__(self, prim_path: str, end_effector_prim_name: str = None, end_effector_prim_path: str = None, name: str = 'single_manipulator', position: typing.Optional[typing.Sequence[float]] = None, translation: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, scale: typing.Optional[typing.Sequence[float]] = None, visible: typing.Optional[bool] = None, gripper: isaacsim.robot.manipulators.grippers.gripper.Gripper = None) -> None:
        ...
    def initialize(self, physics_sim_view: omni.physics.tensors.bindings._physicsTensors.SimulationView = None) -> None:
        """
        Create a physics simulation view if not passed and creates an articulation view using physX tensor api.
                    This needs to be called after each hard reset (i.e stop + play on the timeline) before interacting with any
                    of the functions of this class.
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
                
        """
    def post_reset(self) -> None:
        """
        Resets the manipulator, the end effector and the gripper to its default state.
        """
    @property
    def end_effector(self) -> isaacsim.core.prims.impl.single_rigid_prim.SingleRigidPrim:
        """
        
                Returns:
                    SingleRigidPrim: end effector of the manipulator (can be used to get its world pose, angular velocity..etc).
                
        """
    @property
    def gripper(self) -> isaacsim.robot.manipulators.grippers.gripper.Gripper:
        """
        
                Returns:
                    Gripper: gripper of the manipulator (can be used to open or close the gripper, get its world pose or angular velocity..etc).
                
        """
