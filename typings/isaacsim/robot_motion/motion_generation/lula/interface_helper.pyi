from __future__ import annotations
from isaacsim.core.api import objects
from isaacsim.core.prims.impl.single_xform_prim import SingleXFormPrim
from isaacsim.core.utils.numpy.rotations import quats_to_rot_matrices
from isaacsim.core.utils.prims import delete_prim
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import get_stage_units
from isaacsim.core.utils.string import find_unique_string_name
from isaacsim.robot_motion.motion_generation.lula import utils as lula_utils
import isaacsim.robot_motion.motion_generation.lula.world
from isaacsim.robot_motion.motion_generation.lula.world import LulaWorld
import lula as lula
import numpy as np
import numpy
__all__ = ['LulaInterfaceHelper', 'LulaWorld', 'SingleXFormPrim', 'delete_prim', 'find_unique_string_name', 'get_stage_units', 'is_prim_path_valid', 'lula', 'lula_utils', 'np', 'objects', 'quats_to_rot_matrices']
class LulaInterfaceHelper(isaacsim.robot_motion.motion_generation.lula.world.LulaWorld):
    """
    
        Class containing functions common in Lula based algorithms.  The main utility of this class is handling the tracking of the robot base
        and returning basic robot information
        
    """
    def __init__(self, robot_description: lula.RobotDescription):
        ...
    def _get_pose_rel_robot_base(self, trans, rot):
        ...
    def _get_prim_pose_rel_robot_base(self, prim):
        ...
    def add_capsule(self, capsule: typing.Union[isaacsim.core.api.objects.capsule.DynamicCapsule, isaacsim.core.api.objects.capsule.VisualCapsule], static: bool = False):
        ...
    def add_cuboid(self, cuboid: typing.Union[isaacsim.core.api.objects.cuboid.DynamicCuboid, isaacsim.core.api.objects.cuboid.FixedCuboid, isaacsim.core.api.objects.cuboid.VisualCuboid], static: typing.Optional[bool] = False):
        ...
    def add_sphere(self, sphere: typing.Union[isaacsim.core.api.objects.sphere.DynamicSphere, isaacsim.core.api.objects.sphere.VisualSphere], static: bool = False):
        ...
    def get_active_joints(self):
        ...
    def get_end_effector_pose(self, active_joint_positions: numpy.array, frame_name: str) -> typing.Tuple[<built-in function array>, <built-in function array>]:
        """
        Return pose of robot end effector given current joint positions.
                The end effector position will be transformed into world coordinates based
                on the believed position of the robot base.  See set_robot_base_pose()
        
                Args:
                    active_joint_positions (np.array): positions of the active joints in the robot
        
                Returns:
                    Tuple[np.array,np.array]:
                    end_effector_translation: (3x1) translation vector for the robot end effector
                         relative to the USD stage origin 
        
                    end_effector_rotation: (3x3) rotation matrix describing the orientation of the
                        robot end effector relative to the USD global frame 
        
                
        """
    def get_watched_joints(self) -> typing.List:
        """
        Lula does not currently support watching joint states that are not controllable
        
                Returns:
                    (List): Always returns an empty list.
                
        """
    def reset(self):
        ...
    def set_robot_base_pose(self, robot_position: numpy.array, robot_orientation: numpy.array) -> None:
        """
        Update position of the robot base. Until this function is called, Lula will assume the base pose
                to be at the origin with identity rotation.
        
                Args:
                    robot_position (np.array): (3 x 1) translation vector describing the translation of the robot base relative to the USD stage origin.
                        The translation vector should be specified in the units of the USD stage
                    robot_orientation (np.array): (4 x 1) quaternion describing the orientation of the robot base relative to the USD stage global frame
                
        """
    def update_world(self, updated_obstacles: typing.Optional[typing.List] = None):
        ...
