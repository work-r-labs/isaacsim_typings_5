from __future__ import annotations
import asyncio as asyncio
import carb as carb
import concurrent as concurrent
import contextlib as contextlib
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.widget.viewport.api import ViewportAPI
from omni.kit.widget.viewport.display_delegate import ViewportDisplayDelegate
from omni.kit.widget.viewport.impl.texture import ViewportTexture
from omni.kit.widget.viewport.impl.utility import StageAxis
from omni.kit.widget.viewport.impl.utility import init_settings
from omni.kit.widget.viewport.impl.utility import save_implicit_cameras
from omni import ui
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import typing
import weakref as weakref
__all__: list = ['ViewportWidget']
class ViewportWidget:
    """
    
        A low level omni.ui.Widget for displaying rendered output.
        
    """
    _ViewportWidget__g_instances: typing.ClassVar[list]  # value = [<weakproxy at 0x709fbdf09170 to ViewportWidget at 0x709fadb34820>]
    @staticmethod
    def _ViewportWidget__clean_instances(dead, self = None):
        ...
    @staticmethod
    def get_instances():
        """
        Return an iterable object to enumerate all known ViewportWidget instances
        """
    def _ViewportWidget__build_ui(self, usd_context_name: str, camera_path: str, resolution: typing.Union[str, tuple], hd_engine: str):
        ...
    def _ViewportWidget__destroy_ui(self):
        ...
    def _ViewportWidget__ensure_usd_context(self, usd_context: omni.usd._usd.UsdContext = None):
        ...
    def _ViewportWidget__ensure_usd_stage(self, usd_context: omni.usd._usd.UsdContext = None):
        ...
    def _ViewportWidget__get_texture_resolution(self, resolution: typing.Union[str, tuple]):
        ...
    def _ViewportWidget__is_first_instance(self) -> bool:
        ...
    def _ViewportWidget__on_stage_opened(self, stage: pxr.Usd.Stage, camera_path: str, resolution: tuple, hd_engine: str):
        """
        Called when opening a new stage
        """
    def _ViewportWidget__remove_notifications(self):
        ...
    def _ViewportWidget__resolve_resolution(self, resolution):
        ...
    def _ViewportWidget__root_size_changed(self, *args, **kwargs):
        ...
    def _ViewportWidget__set_image_data(self, texture, presentation_key = 0):
        ...
    def _ViewportWidget__setup_notifications(self, stage: pxr.Usd.Stage, hydra_texture):
        ...
    def __init__(self, usd_context_name: str = '', camera_path: typing.Optional[str] = None, resolution: typing.Optional[tuple] = None, hd_engine: typing.Optional[str] = None, viewport_api: typing.Union[omni.kit.widget.viewport.api.ViewportAPI, str, NoneType] = None, hydra_engine_options: typing.Optional[dict] = None, **ui_kwargs):
        """
        
                ViewportWidget constructor
        
                Args:
                    usd_context_name (str): The name of a UsdContext this Viewport will be viewing.
                    camera_path (str): The path to a UsdGeom.Camera to render with.
                    resolution: (x,y): The size of the backing texture that is rendered into (or 'fill_frame' to lock to UI size).
                    viewport_api: (ViewportAPI, str) A ViewportAPI instance that users have access to via .viewport_api property
                                                     or a unique string id used to create a default ViewportAPI instance.
                
        """
    def _viewport_changed(self, camera_path: pxr.Sdf.Path, stage: pxr.Usd.Stage, time: pxr.Usd.TimeCode | None = None):
        ...
    def destroy(self):
        """
        
                Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
                
        """
    def set_resolution(self, resolution: typing.Tuple[float, float]) -> None:
        ...
    @property
    def display_delegate(self):
        ...
    @display_delegate.setter
    def display_delegate(self, display_delegate: omni.kit.widget.viewport.display_delegate.ViewportDisplayDelegate):
        ...
    @property
    def expand_viewport(self) -> bool:
        """
        Whether the ui object containing the Viewport texture expands one dimension of resolution to cover the full ui size
        """
    @expand_viewport.setter
    def expand_viewport(self, value: bool) -> None:
        """
        Tell the ui object containing the Viewport texture to expand one dimension of resolution to cover the full ui size
        """
    @property
    def fill_frame(self) -> bool:
        """
        Whether the ui object containing the Viewport texture expands both dimensions of resolution based on the ui size
        """
    @fill_frame.setter
    def fill_frame(self, value: bool) -> None:
        """
        Tell the ui object containing the Viewport texture to expand both dimensions of resolution based on the ui size
        """
    @property
    def full_resolution(self):
        """
        Return the resolution being requested (not accounting for any % down-scaling
        """
    @property
    def name(self):
        """
        Return the name of the ViewportWidget
        """
    @property
    def resolution(self) -> typing.Tuple[float, float]:
        """
        Return the resolution that the renderer is providing images at.
        """
    @resolution.setter
    def resolution(self, resolution: typing.Tuple[float, float]):
        """
        Set the resolution that the renderer is providing images at.
        """
    @property
    def resolution_uses_dpi(self) -> bool:
        """
        Whether to account for DPI when driving the Viewport texture resolution
        """
    @resolution_uses_dpi.setter
    def resolution_uses_dpi(self, value: bool) -> None:
        """
        Tell the ui object whether to use DPI scale when driving the Viewport texture resolution
        """
    @property
    def usd_context_name(self) -> str:
        """
        Return the name of the USdContext this instance is attached to
        """
    @property
    def viewport_api(self):
        """
        Return the active omni.kit.widget.viewport.ViewportAPI for the ViewportWidget
        """
    @property
    def visible(self):
        """
        Set the visibility of this ViewportWidget
        """
    @visible.setter
    def visible(self, value) -> bool:
        """
        Get the visibility of this ViewportWidget
        """
