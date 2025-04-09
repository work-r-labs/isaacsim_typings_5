from __future__ import annotations
import carb as carb
from isaacsim.core.utils.prims import delete_prim
from isaacsim.core.utils.stage import get_next_free_path
from isaacsim.core.utils.xforms import reset_and_set_xform_ops
import omni as omni
from omni.isaac import IsaacSensorSchema
import pxr.Gf
from pxr import Gf
from pxr import PhysxSchema
import typing
__all__ = ['Gf', 'IsaacSensorCreateContactSensor', 'IsaacSensorCreateImuSensor', 'IsaacSensorCreatePrim', 'IsaacSensorSchema', 'PhysxSchema', 'carb', 'delete_prim', 'get_next_free_path', 'omni', 'reset_and_set_xform_ops']
class IsaacSensorCreateContactSensor(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str = '/Contact_Sensor', parent: str = None, min_threshold: float = 0, max_threshold: float = 100000, color: pxr.Gf.Vec4f = ..., radius: float = -1, sensor_period: float = -1, translation: pxr.Gf.Vec3d = ...):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class IsaacSensorCreateImuSensor(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str = '/Imu_Sensor', parent: str = None, sensor_period: float = -1, translation: pxr.Gf.Vec3d = ..., orientation: pxr.Gf.Quatd = ..., linear_acceleration_filter_size: int = 1, angular_velocity_filter_size: int = 1, orientation_filter_size: int = 1):
        ...
    def do(self):
        ...
    def undo(self):
        ...
class IsaacSensorCreatePrim(omni.kit.commands.command.Command):
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __init__(self, path: str = '', parent: str = '', translation: pxr.Gf.Vec3d = ..., orientation: pxr.Gf.Quatd = ..., schema_type = omni.isaac.IsaacSensorSchema.IsaacBaseSensor):
        ...
    def do(self):
        ...
    def undo(self):
        ...
