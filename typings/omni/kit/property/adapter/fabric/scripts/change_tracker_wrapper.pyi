from __future__ import annotations
import omni as omni
from usdrt import Rt
from usdrt import Sdf
import usdrt.Sdf._Sdf
from usdrt import Usd
import usdrt.Usd._Usd
__all__ = ['Rt', 'RtChangeTrackerWrapper', 'Sdf', 'Usd', 'omni']
class RtChangeTrackerWrapper:
    class Notice:
        def GetChangedInfoOnlyPaths(self):
            ...
        def GetResyncedPaths(self):
            ...
        def __init__(self, resynced_paths: list[usdrt.Sdf._Sdf.Path], changed_info_only_paths: list[usdrt.Sdf._Sdf.Path]):
            ...
        @property
        def is_fabric(self):
            ...
    def __del__(self):
        ...
    def __init__(self, attr_names: list[str], prim_paths: list[usdrt.Sdf._Sdf.Path], callback: typing.Callable[[omni.kit.property.adapter.fabric.scripts.change_tracker_wrapper.RtChangeTrackerWrapper.Notice, usdrt.Usd._Usd.Stage], NoneType], stage: usdrt.Usd._Usd.Stage):
        ...
    def _on_update(self, event):
        ...
    def destroy(self):
        ...
