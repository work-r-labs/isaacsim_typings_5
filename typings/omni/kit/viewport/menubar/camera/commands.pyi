from __future__ import annotations
import carb as carb
import omni as omni
from pxr import Gf
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
import typing
__all__ = ['CAMERA_LOCK_NAME', 'DuplicateCameraCommand', 'DuplicateViewportCameraCommand', 'Gf', 'Sdf', 'SetViewportCameraCommand', 'Usd', 'UsdGeom', 'carb', 'omni', 'register_commands', 'unregister_commands']
class DuplicateCameraCommand(omni.kit.commands.command.Command):
    """
    
        Duplicates a camera at a specific time
    
        Args:
            camera_path (str): name of the camera to duplicate.
            time (float): Time at which to duplicate, or None to use active time
            usd_context_name (str): The name of a valid omni.UsdContext to target
            new_camera_path (str): Path to create the new camera at (None for automatic path)
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, camera_path: str = '', time: float = None, usd_context_name: str = '', new_camera_path: str = None):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class DuplicateViewportCameraCommand(omni.kit.commands.command.Command):
    """
    
        Duplicates a Viewport's actively bound camera and bind active camera to the duplicated one.
    
        Args:
            viewport_api: The viewport to target
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, viewport_api, *args, **kwargs):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class SetViewportCameraCommand(omni.kit.commands.command.Command):
    """
    
        Sets a Viewport's actively bound camera to camera at given path
    
        Args:
            camera_path (Union[str, Sdf.Path): New camera path to bind to viewport.
            viewport_api: the viewport to target.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def read_camera_path(viewport_api) -> pxr.Sdf.Path:
        ...
    def _SetViewportCameraCommand__save_to_file(self, camera_path: str):
        ...
    def __init__(self, camera_path: typing.Union[str, pxr.Sdf.Path], viewport_api, *args, **kwargs):
        ...
    def do(self):
        ...
    def undo(self, look_through = None):
        ...
def register_commands():
    ...
def unregister_commands(cmds):
    ...
CAMERA_LOCK_NAME: str = 'omni:kit:cameraLock'
