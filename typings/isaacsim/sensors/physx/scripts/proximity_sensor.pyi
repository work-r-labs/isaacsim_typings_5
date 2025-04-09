from __future__ import annotations
import carb as carb
import numpy as np
import omni as omni
from omni.physx import get_physx_scene_query_interface
from omni.usd._impl.utils import get_prim_at_path
from omni.usd._impl.utils import get_world_transform_matrix
from pxr import Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
import time as time
import typing
__all__ = ['ProximitySensor', 'ProximitySensorManager', 'Sdf', 'Usd', 'UsdGeom', 'carb', 'clear_sensors', 'get_physx_scene_query_interface', 'get_prim_at_path', 'get_world_transform_matrix', 'np', 'omni', 'register_sensor', 'time']
class ProximitySensor:
    def __init__(self, parent: pxr.Usd.Prim, callback_fns = [None, None, None], exclusions = list()):
        ...
    def check_for_overlap(self):
        ...
    def get_active_zones(self) -> typing.List[str]:
        """
        Returns a list of the prim paths of all the collision meshes the tracker is inside of.
        
                Returns:
                    list(str): prim paths as strings
                
        """
    def get_data(self) -> typing.Dict[str, typing.Dict[str, float]]:
        """
        
                Returns dictionary of overlapped geometry and respective metadata.
        
                    key: prim_path of overlapped geometry
                    val: dictionary of metadata:
        
                        "duration": float of time since overlap
                        "distance": distance from origin of tracker to origin of overlapped geometry
        
                Returns:
                    Dict[str, Dict[str, float]]: overlapped geometry and metadata
                
        """
    def get_entered_zones(self) -> typing.List[str]:
        """
        Returns a list of the prim paths of all the collision meshes the tracker just entered.
        
                Returns:
                    list(str): prim paths as strings
                
        """
    def get_exited_zones(self) -> typing.List[str]:
        """
        Returns a list of the prim paths of all the collision meshes the tracker just exited.
        
                Returns:
                    list(str): prim paths as strings
                
        """
    def is_overlapping(self):
        ...
    def report_hit(self, hit):
        ...
    def reset(self):
        ...
    def status(self):
        ...
    def to_string(self):
        ...
    def update(self):
        ...
class ProximitySensorManager:
    _instance: typing.ClassVar[ProximitySensorManager]  # value = <isaacsim.sensors.physx.scripts.proximity_sensor.ProximitySensorManager object>
    sensors: typing.ClassVar[list] = list()
    @classmethod
    def __new__(cls):
        ...
    def clear_sensors(self):
        ...
    def register_sensor(self, sensor: ProximitySensor):
        ...
    def update(self):
        ...
def clear_sensors():
    ...
def register_sensor(sensor: ProximitySensor):
    ...
