from __future__ import annotations
import asyncio as asyncio
import carb as carb
from isaacsim.core.utils._isaac_utils import transforms
import omni as omni
from pxr import Sdf
import typing
__all__ = ['IsaacSimDestroyPrim', 'IsaacSimScalePrim', 'IsaacSimSpawnPrim', 'IsaacSimTeleportPrim', 'Sdf', 'asyncio', 'carb', 'omni', 'transforms']
class IsaacSimDestroyPrim(omni.kit.commands.command.Command):
    """
    Command to set a delete a prim. This variant has less overhead than other commands as it doesn't store an undo operation
    
        Typical usage example:
    
        .. code-block:: python
    
            omni.kit.commands.execute(
                "IsaacSimDestroyPrim",
                prim_path="/World/Prim,
            )
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: str):
        ...
    def do(self) -> bool:
        ...
    def undo(self):
        ...
class IsaacSimScalePrim(omni.kit.commands.command.Command):
    """
    Command to set a scale of a prim
    
        Typical usage example:
    
        .. code-block:: python
    
            omni.kit.commands.execute(
                "IsaacSimScalePrim",
                prim_path="/World/Prim,
                scale=(1.5, 1.5, 1.5),
            )
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: str, scale: carb._carb.Float3 = (0, 0, 0)):
        ...
    def do(self) -> bool:
        ...
    def undo(self):
        ...
class IsaacSimSpawnPrim(omni.kit.commands.command.Command):
    """
    Command to spawn a new prim in the stage and set its transform. This uses dynamic_control to properly handle physics objects and articulation
    
        Typical usage example:
    
        .. code-block:: python
    
            omni.kit.commands.execute(
                "IsaacSimSpawnPrim",
                usd_path="/path/to/file.usd",
                prim_path="/World/Prim,
                translation=(0, 0, 0),
                rotation=(0, 0, 0, 1),
            )
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, usd_path: str, prim_path: str, translation: carb._carb.Float3 = (0, 0, 0), rotation: carb._carb.Float4 = (0, 0, 0, 1)):
        ...
    def do(self) -> bool:
        ...
    def undo(self):
        ...
class IsaacSimTeleportPrim(omni.kit.commands.command.Command):
    """
    Command to set a transform of a prim. This uses dynamic_control to properly handle physics objects and articulation
    
        Typical usage example:
    
        .. code-block:: python
    
            omni.kit.commands.execute(
                "IsaacSimTeleportPrim",
                prim_path="/World/Prim,
                translation=(0, 0, 0),
                rotation=(0, 0, 0, 1),
            )
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, prim_path: str, translation: carb._carb.Float3 = (0, 0, 0), rotation: carb._carb.Float4 = (0, 0, 0, 1)):
        ...
    def do(self) -> bool:
        ...
    def undo(self):
        ...
