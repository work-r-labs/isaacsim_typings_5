from __future__ import annotations
import carb as carb
import isaacsim.core.api.sensors.base_sensor
from isaacsim.core.api.sensors.base_sensor import BaseSensor
from isaacsim.core.nodes.bindings import _isaacsim_core_nodes
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.stage import traverse_stage
from isaacsim.sensors.physics import _sensor
import numpy as np
import omni as omni
from omni.isaac import IsaacSensorSchema
from pxr import PhysxSchema
__all__ = ['BaseSensor', 'IMUSensor', 'IsaacSensorSchema', 'PhysxSchema', 'carb', 'get_prim_at_path', 'is_prim_path_valid', 'np', 'omni', 'traverse_stage']
class IMUSensor(isaacsim.core.api.sensors.base_sensor.BaseSensor):
    def __init__(self, prim_path: str, name: typing.Optional[str] = 'imu_sensor', frequency: typing.Optional[int] = None, dt: typing.Optional[float] = None, translation: typing.Optional[numpy.ndarray] = None, position: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = None, linear_acceleration_filter_size: typing.Optional[int] = 1, angular_velocity_filter_size: typing.Optional[int] = 1, orientation_filter_size: typing.Optional[int] = 1) -> None:
        ...
    def get_current_frame(self, read_gravity = True) -> dict:
        ...
    def get_dt(self) -> float:
        ...
    def get_frequency(self) -> int:
        ...
    def initialize(self, physics_sim_view = None) -> None:
        ...
    def is_paused(self) -> bool:
        ...
    def pause(self) -> None:
        ...
    def resume(self) -> None:
        ...
    def set_dt(self, value: float) -> None:
        ...
    def set_frequency(self, value: int) -> None:
        ...
