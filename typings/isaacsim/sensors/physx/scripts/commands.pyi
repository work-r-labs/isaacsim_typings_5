from __future__ import annotations
import carb as carb
from isaacsim.core.utils.stage import get_next_free_path
import omni as omni
from omni.isaac import IsaacSensorSchema
from omni.isaac import RangeSensorSchema
import pxr.Gf
from pxr import Gf
from pxr import UsdGeom
import typing
__all__ = ['Gf', 'IsaacSensorCreateLightBeamSensor', 'IsaacSensorSchema', 'RangeSensorCreateGeneric', 'RangeSensorCreateLidar', 'RangeSensorCreatePrim', 'RangeSensorSchema', 'UsdGeom', 'carb', 'get_next_free_path', 'omni', 'setup_base_prim']
class IsaacSensorCreateLightBeamSensor(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str = '/LightBeam_Sensor', parent: str = None, translation: pxr.Gf.Vec3d = ..., orientation: pxr.Gf.Quatd = ..., num_rays: int = 1, curtain_length: float = 0.0, forward_axis: pxr.Gf.Vec3d = ..., curtain_axis: pxr.Gf.Vec3d = ..., min_range: float = 0.4, max_range: float = 100.0, draw_points: bool = False, draw_lines: bool = False):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class RangeSensorCreateGeneric(omni.kit.commands.command.Command):
    """
    Commands class to create a generic range sensor.
    
        Typical usage example:
    
        .. code-block:: python
    
            result, prim = omni.kit.commands.execute(
                "RangeSensorCreateGeneric",
                path="/GenericSensor",
                parent=None,
                min_range=0.4,
                max_range=100.0,
                draw_points=False,
                draw_lines=False,
                sampling_rate=60,
            )
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str = '/GenericSensor', parent = None, min_range: float = 0.4, max_range: float = 100.0, draw_points: bool = False, draw_lines: bool = False, sampling_rate: int = 60):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class RangeSensorCreateLidar(omni.kit.commands.command.Command):
    """
    Commands class to create a lidar sensor.
    
        Typical usage example:
    
        .. code-block:: python
    
            result, prim = omni.kit.commands.execute(
                "RangeSensorCreateLidar",
                path="/Lidar",
                parent=None,
                min_range=0.4,
                max_range=100.0,
                draw_points=False,
                draw_lines=False,
                horizontal_fov=360.0,
                vertical_fov=30.0,
                horizontal_resolution=0.4,
                vertical_resolution=4.0,
                rotation_rate=20.0,
                high_lod=False,
                yaw_offset=0.0,
                enable_semantics=False,
            )
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str = '/Lidar', parent = None, min_range: float = 0.4, max_range: float = 100.0, draw_points: bool = False, draw_lines: bool = False, horizontal_fov: float = 360.0, vertical_fov: float = 30.0, horizontal_resolution: float = 0.4, vertical_resolution: float = 4.0, rotation_rate: float = 20.0, high_lod: bool = False, yaw_offset: float = 0.0, enable_semantics: bool = False):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class RangeSensorCreatePrim(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str = '', parent: str = '', schema_type = omni.isaac.RangeSensorSchema.RangeSensor, min_range: float = 0.4, max_range: float = 100.0, draw_points: bool = False, draw_lines: bool = False):
        ...
    def do(self):
        ...
    def undo(self):
        ...
def setup_base_prim(prim, enabled, draw_points, draw_lines, min_range, max_range):
    ...
