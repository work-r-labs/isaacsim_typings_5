from __future__ import annotations
import carb as carb
import omni as omni
from omni.graph import core as og
import pxr as pxr
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdPhysics
import typing
__all__ = ['CreateSurfaceGripper', 'Usd', 'UsdGeom', 'UsdPhysics', 'carb', 'og', 'omni', 'pxr']
class CreateSurfaceGripper(omni.kit.commands.command.Command):
    """
    Creates Action graph containing a Surface Gripper node, and all prims to facilitate its creation
    
        Typical usage example:
    
        .. code-block:: python
    
            result, prim  = omni.kit.commands.execute(
                    "CreateSurfaceGripper",
                    prim_name="SurfaceGripperActionGraph",
                    conveyor_prim="/SurfaceGripperRigidBody"
                )
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_name: str = 'SurfaceGripperActionGraph', surface_gripper_prim = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
