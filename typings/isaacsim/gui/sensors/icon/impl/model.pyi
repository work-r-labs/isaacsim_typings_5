from __future__ import annotations
import carb as carb
import omni as omni
from omni.ui import scene as sc
from pathlib import Path
from pxr import Gf
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
from pxr import UsdGeom
import typing
import usdrt as usdrt
__all__: list = ['IconModel']
class IconModel(omni.ui_scene._scene.AbstractManipulatorModel):
    class IconItem(omni.ui_scene._scene.AbstractManipulatorItem):
        def __init__(self, prim_path, icon_url):
            ...
    SENSOR_TYPES: typing.ClassVar[list] = ['Lidar', 'OmniLidar', 'IsaacContactSensor', 'IsaacLightBeamSensor', 'IsaacImuSensor', 'Generic']
    @staticmethod
    def _on_frame_update(*args, **kwargs):
        ...
    @staticmethod
    def _populate_initial_icons(*args, **kwargs):
        """
        Populate icons by querying the USDrt stage. Skip if icon visibility is disabled.
        """
    @staticmethod
    def get_position(*args, **kwargs):
        ...
    @staticmethod
    def refresh_all_icon_visuals(*args, **kwargs):
        """
        Force a refresh notification for all currently tracked icon items.
        """
    @staticmethod
    def show_sensor_icon(*args, **kwargs):
        """
        Show a sensor icon by setting the USD prim visibility to visible and immediately updating internal state.
        """
    def __del__(self):
        ...
    def __init__(self):
        ...
    def _connect_to_stage(self):
        ...
    def _on_stage_closed(self, event):
        ...
    def _on_stage_opened(self, event):
        ...
    def add_sensor_icon(self, prim_path, icon_url = None):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def get_icon_url(self, prim_path):
        ...
    def get_item(self, identifier):
        ...
    def get_on_click(self, prim_path):
        ...
    def get_prim_paths(self):
        ...
    def get_world_unit(self):
        ...
    def hide_all(self):
        ...
    def hide_sensor_icon(self, prim_path):
        """
        Hide a sensor icon by setting the USD prim visibility to invisible and immediately updating internal state.
        """
    def remove_sensor_icon(self, prim_path):
        ...
    def set_icon_click_fn(self, prim_path, call_back):
        ...
    def show_all(self):
        ...
