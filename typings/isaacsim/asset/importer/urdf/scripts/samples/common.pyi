from __future__ import annotations
import carb as carb
import omni as omni
import os as os
from pxr import PhysxSchema
from pxr import UsdGeom
from pxr import UsdPhysics
__all__ = ['PhysxSchema', 'UsdGeom', 'UsdPhysics', 'carb', 'omni', 'os', 'set_drive_parameters']
def set_drive_parameters(drive, target_type, target_value, stiffness = None, damping = None, max_force = None):
    """
    Enable velocity drive for a given joint
    """
