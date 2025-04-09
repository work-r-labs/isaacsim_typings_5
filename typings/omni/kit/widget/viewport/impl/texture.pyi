from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.hydra_texture import create_hydra_texture
from omni.kit.widget.viewport.capture import Capture
from omni.kit.widget.viewport.impl.utility import _init_viewport_cameras
from omni.kit.widget.viewport.impl.utility import _report_error
from omni.kit.widget.viewport.impl.utility import _run_viewport_auto_frame
from pxr import Sdf
import pxr.Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
import typing
import weakref as weakref
__all__: list = ['ViewportTexture']
class ViewportTexture:
    _ViewportTexture__g_hd_texture_counter: typing.ClassVar[int] = 1
    camera_path = ...
    def _ViewportTexture__allow_hd_engine(self, hd_engine: str, hd_renderer: str | None = None):
        ...
    def _ViewportTexture__create_subscription_to_drawable_changed(self, callback_fn: typing.Callable = None):
        ...
    def _ViewportTexture__enable_hydra_engine(self, hd_engine_name, usd_context):
        ...
    def _ViewportTexture__ensure_usd_context(self, usd_context: omni.usd._usd.UsdContext = None):
        ...
    def _ViewportTexture__ensure_usd_stage(self, usd_context: omni.usd._usd.UsdContext = None, stage: pxr.Usd.Stage = None):
        ...
    def _ViewportTexture__render_mode_setting(self, hd_engine: str) -> str:
        ...
    def _ViewportTexture__resolve_default_renderer(self, active: str = None, auto_load: bool = False):
        ...
    def _ViewportTexture__set_hd_engine(self, hd_engine: str, hd_renderer: str | None = None, first_init: bool = False):
        ...
    def _ViewportTexture__set_viewport_handle(self, viewport_handle: int):
        ...
    def _ViewportTexture__setup_resolution(self, resolution: typing.Sequence[int], setting_scope: str):
        ...
    def _ViewportTexture__validate_camera(self, cam_path: pxr.Sdf.Path, stage: pxr.Usd.Stage = None):
        ...
    def __init__(self, usd_context_name: typing.Optional[str], camera_path: typing.Optional[str] = None, resolution: typing.Optional[typing.Sequence] = None, hd_engine: typing.Optional[str] = None, hydra_engine_options: typing.Optional[dict] = None, update_api_texture: typing.Optional[typing.Callable] = None):
        ...
    def _add_render_settings_changed_fn(self, callback = None) -> None:
        ...
    def _on_stage_opened(self, drawable_changed_fn, camera_path: str, first_init: bool):
        """
        Called when opening a new stage
        """
    def _remove_render_settings_changed_fn(self, callback):
        ...
    def _render_settings_changed(self):
        ...
    def destroy(self):
        """
        
                Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
                
        """
    def schedule_capture(self, delegate: omni.kit.widget.viewport.capture.Capture) -> omni.kit.widget.viewport.capture.Capture:
        ...
    @property
    def display_render_var(self):
        ...
    @display_render_var.setter
    def display_render_var(self, name: str):
        ...
    @property
    def frame_info(self):
        ...
    @property
    def full_resolution(self):
        """
        Return a tuple of the full (full_resolution_x, full_resolution_y) this Texture is rendering at, not accounting for scale.
        """
    @property
    def hydra_engine(self):
        ...
    @property
    def render_mode(self):
        ...
    @render_mode.setter
    def render_mode(self, render_mode: str):
        ...
    @property
    def resolution(self):
        """
        Return a tuple of (resolution_x, resolution_y) this Texture is rendering at, accounting for scale.
        """
    @resolution.setter
    def resolution(self, resolution):
        ...
    @property
    def resolution_scale(self) -> float:
        """
        Get the scaling factor for the Texture's render resolution.
        """
    @resolution_scale.setter
    def resolution_scale(self, value: float):
        """
        Set the scaling factor for the Texture's render resolution.
        """
    @property
    def set_hd_engine(self):
        ...
