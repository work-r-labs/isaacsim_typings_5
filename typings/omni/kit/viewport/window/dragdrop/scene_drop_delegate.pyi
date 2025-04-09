from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.viewport.window.dragdrop.delegate import DragDropDelegate
from omni import ui
from omni.ui import scene as sc
import os as os
import pxr.Gf
from pxr import Gf
from pxr import Sdf
import pxr.Sdf
from pxr import Tf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
import typing
__all__: list = ['SceneDropDelegate']
class SceneDropDelegate(omni.kit.viewport.window.dragdrop.delegate.DragDropDelegate):
    _SceneDropDelegate__g_ignore_extensions: typing.ClassVar[set] = set()
    _SceneDropDelegate__g_ignore_protocols: typing.ClassVar[set] = {'material::', 'sky::'}
    @staticmethod
    def add_ignored_extension(extension: str):
        """
        Add a file extension that should be ignored by default file-handlers
        """
    @staticmethod
    def add_ignored_protocol(protocol: str):
        """
        Add a protocol that should be ignored by default file-handlers
        """
    @staticmethod
    def is_ignored_extension(url: str):
        """
        Early out for other extension handlers that claim the format
        """
    @staticmethod
    def is_ignored_protocol(url: str):
        """
        Early out for other protocol handlers that claim the format
        """
    @staticmethod
    def remove_ignored_extension(extension: str):
        """
        Remove a file extension that should no longer be ignored by default file-handlers
        """
    @staticmethod
    def remove_ignored_protocol(protocol: str):
        """
        Remove a protocol that should be ignored by default file-handlers
        """
    def _SceneDropDelegate__cache_screen_ndc(self, viewport_api, world_space_pos: pxr.Gf.Vec3d):
        ...
    def __init__(self, *args, **kw_args):
        ...
    def _get_world_position(self, drop_data: dict) -> pxr.Gf.Vec3d:
        ...
    def _get_world_position_object(self, viewport_api, world_space_pos: pxr.Gf.Vec3d, drop_data: dict) -> typing.Tuple[pxr.Gf.Vec3d, bool]:
        """
        Return a world-space position that is located between two objects as mouse is dragged over them
        """
    def _get_world_position_plane(self, viewport_api, world_space_pos: pxr.Gf.Vec3d, drop_data: dict, mode: str) -> typing.Tuple[pxr.Gf.Vec3d, bool]:
        ...
    def accepted(self, drop_data: dict):
        ...
    def add_drop_marker(self, drop_data: dict, world_space_pos: pxr.Gf.Vec3d):
        ...
    def add_drop_shape(self, world_space_pos: pxr.Gf.Vec3d, scale: float = 50, thickness: float = 1, color: <omni.ui.color_utils.ColorShade object> = None):
        ...
    def add_reference_to_stage(self, usd_context, stage: pxr.Usd.Stage, url: str) -> typing.Tuple[str, pxr.Usd.EditContext, str]:
        """
        Add a Usd.Prim to an exiting Usd.Stage, pointing to the url
        """
    def cancel(self, drop_data: dict):
        ...
    def create_as_payload(self, usd_context, stage: pxr.Usd.Stage, url: str, prim_path: str):
        """
        Return whether to create as a reference or payload
        """
    def create_instanceable_reference(self, usd_context, stage: pxr.Usd.Stage, url: str, prim_path: str) -> bool:
        """
        Return whether to create the reference as instanceable=True
        """
    def dropped(self, drop_data: dict):
        ...
    def get_context_and_stage(self, drop_data: dict):
        ...
    def get_url(self, drop_data: dict):
        ...
    def make_prim_path(self, stage: pxr.Usd.Stage, url: str, prim_path: pxr.Sdf.Path = None, prim_name: str = None):
        """
        Make a new/unique prim path for the given url
        """
    def make_relative_to_layer(self, stage: pxr.Usd.Stage, url: str) -> str:
        ...
    def normalize_sdf_path(self, sdf_layer_path: str):
        ...
    def remove_drop_marker(self, drop_data: dict):
        ...
    def reset_state(self):
        ...
    def update_drop_position(self, drop_data: dict):
        ...
    @property
    def add_outline(self) -> bool:
        ...
    @property
    def color(self):
        ...
    @property
    def honor_picking_mode(self) -> bool:
        ...
