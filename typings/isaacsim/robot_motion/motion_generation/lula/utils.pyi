from __future__ import annotations
import isaacsim.core.prims.impl.single_xform_prim
from isaacsim.core.prims.impl.single_xform_prim import SingleXFormPrim
from isaacsim.core.utils.numpy.rotations import quats_to_rot_matrices
import lula as lula
__all__ = ['SingleXFormPrim', 'get_pose3', 'get_pose_rel_robot_base', 'get_prim_pose_in_meters', 'get_prim_pose_in_meters_rel_robot_base', 'lula', 'quats_to_rot_matrices']
def get_pose3(trans = None, rot_mat = None, rot_quat = None) -> lula.Pose3:
    """
    
        Get lula.Pose3 type representing a transformation.
        rot_mat will take precedence over rot_quat if both are supplied
        
    """
def get_pose_rel_robot_base(trans, rot, robot_pos, robot_rot):
    ...
def get_prim_pose_in_meters(prim: isaacsim.core.prims.impl.single_xform_prim.SingleXFormPrim, meters_per_unit: float):
    ...
def get_prim_pose_in_meters_rel_robot_base(prim, meters_per_unit, robot_pos, robot_rot):
    ...
