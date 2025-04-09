"""
pybind11 isaacsim.sensors.rtx bindings
"""
from __future__ import annotations
__all__ = ['IIsaacSimSensorsRtx', 'acquire_interface', 'release_interface']
class IIsaacSimSensorsRtx:
    pass
def acquire_interface(plugin_name: str = None, library_path: str = None) -> IIsaacSimSensorsRtx:
    ...
def release_interface(arg0: IIsaacSimSensorsRtx) -> None:
    ...
