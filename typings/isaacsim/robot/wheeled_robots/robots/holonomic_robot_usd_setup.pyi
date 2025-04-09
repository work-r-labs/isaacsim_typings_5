from __future__ import annotations
import carb as carb
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.rotations import gf_rotation_to_np_array
from isaacsim.core.utils.stage import get_current_stage
import numpy as np
import omni as omni
from pxr import Gf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
__all__ = ['Gf', 'HolonomicRobotUsdSetup', 'Usd', 'UsdGeom', 'UsdPhysics', 'carb', 'get_current_stage', 'get_prim_at_path', 'gf_rotation_to_np_array', 'np', 'omni']
class HolonomicRobotUsdSetup:
    """
    
        Sets up the attributes on the prims of a holonomic robot. Specifically adds the `isaacmecanumwheel:radius` and `isaacmecanumwheel:angle` attributes to the wheel joints of the robot prim
    
        Args:
    
            prim_path (str): path of the robot articulation
            com_prim_path (str): path of the xform representing the center of mass of the vehicle
        
    """
    def __init__(self, robot_prim_path: str, com_prim_path: str):
        ...
    def from_usd(self, robot_prim_path, com_prim_path):
        """
        
                if the USD contains all the necessary information, automatically extract them and compile
                
        """
    def get_articulation_controller_params(self):
        ...
    def get_holonomic_controller_params(self):
        ...
    @property
    def mecanum_angles(self):
        ...
    @property
    def up_axis(self):
        ...
    @property
    def wheel_axis(self):
        ...
    @property
    def wheel_dof_names(self):
        ...
    @property
    def wheel_orientations(self):
        ...
    @property
    def wheel_positions(self):
        ...
    @property
    def wheel_radius(self):
        ...
