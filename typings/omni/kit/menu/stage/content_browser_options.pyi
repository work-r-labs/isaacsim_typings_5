from __future__ import annotations
from carb import log_error
from carb import settings
import carb.settings._settings
from functools import partial
import omni as omni
from omni.kit.commands.command import create
import os as os
import pxr.Gf
from pxr import Gf
from pxr import Sdf
from pxr import Tf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
__all__ = ['ContentBrowserOptions', 'Gf', 'Sdf', 'Tf', 'Usd', 'UsdGeom', 'create', 'log_error', 'omni', 'os', 'partial', 'settings']
class ContentBrowserOptions:
    @staticmethod
    def _add_file_to_stage(file_path: str, settings: carb.settings._settings.ISettings, replace_selection: bool):
        """
        
                Add reference/payload to stage from file.
        
                If has a reference or payload selected, honor that type when doing replace at selected.
                If multi selection, honor the first.
                Otherwise honor the preferences setting.
        
                Where the new prim is placed depends on the current selection:
        
                If one or more prims is selected, the new prim is placed at the average position of those prims' transforms.
        
                If replace_selection is True, the selected prims are deleted before the new prim is added,
                and the new one is added as a child of the selected prims' first common parent.
        
                If nothing is selected, the new prim is placed on the ground plane in front of the camera
                (or, if the camera is not looking at the ground, at the camera's target point).
                In this case, the first instance of a Viewport 2 window is preferred; if this is unavailable,
                we fall back to a Viewport 1 version.
                
        """
    @staticmethod
    def _add_to_stage_helper(context: omni.usd._usd.UsdContext, stage: pxr.Usd.Stage, file_path: str, position: pxr.Gf.Vec3d, replace_selection: bool = False, selected_prims = list()):
        ...
    @staticmethod
    def _add_to_stage_using_selection(context: omni.usd._usd.UsdContext, stage: pxr.Usd.Stage, file_path: str, replace_selection: bool):
        ...
    @staticmethod
    def _add_to_stage_using_vp1(context, stage, file_path, settings):
        """
        Deprecated.
        """
    @staticmethod
    def _add_to_stage_using_vp2(context, stage, file_path, settings):
        ...
    @staticmethod
    def _add_to_stage_using_vp2_helper(context, stage, file_path, settings, camera_path, position):
        ...
    @staticmethod
    def _get_grid_intersection(grid_plane, camera_position, camera_direction, default_value):
        ...
    def __init__(self):
        ...
    def _on_content_browser_load(self):
        ...
    def _on_content_browser_unload(self):
        ...
    def shutdown(self):
        ...
    def startup(self):
        ...
