from __future__ import annotations
import omni as omni
import typing
from usd.schema.isaac import robot_schema
__all__: list[str] = ['CreateSurfaceGripper', 'omni', 'robot_schema']
class CreateSurfaceGripper(omni.kit.commands.command.Command):
    """
    Creates Action graph containing a Surface Gripper node, and all prims to facilitate its creation
    
        Typical usage example:
    
        .. code-block:: python
    
            result, prim  = omni.kit.commands.execute(
                    "CreateSurfaceGripper",
                    prim_path="/SurfaceGripper",
                )
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: str = ''):
        ...
    def do(self):
        ...
    def undo(self):
        ...
