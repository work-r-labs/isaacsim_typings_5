from __future__ import annotations
import asyncio as asyncio
import carb as carb
import contextlib as contextlib
import omni as omni
from omni.kit.widget.viewport.capture import Capture
from omni.kit.widget.viewport.impl.utility import _report_error
from pxr import CameraUtil
import pxr.Gf
from pxr import Gf
from pxr import Sdf
import pxr.Sdf
import pxr.Usd
from pxr import Usd
import pxr.UsdGeom
from pxr import UsdGeom
import weakref as weakref
__all__: list = ['ViewportAPI']
class ViewportAPI:
    fill_frame: bool
    freeze_frame: bool
    lock_to_render_result: bool
    updates_enabled: bool
    _ViewportAPI__ViewportSubscription = ViewportAPI.__ViewportSubscription
    @staticmethod
    def _ViewportAPI__flatten_matrix(m):
        ...
    def _ViewportAPI__accelerate_rtx_changed(self, *args, **kwargs):
        ...
    def _ViewportAPI__callback_args(self, fn_container: typing.Sequence):
        ...
    def _ViewportAPI__clean_weak_views(self, *args):
        ...
    def _ViewportAPI__get_conform_policy(self):
        """
        
                TODO: Need python exposure via UsdContext or HydraTexture
                import carb
                conform_setting = carb.settings.get_settings().get("/app/hydra/aperture/conform")
                if (conform_setting is None) or (conform_setting == 1) or (conform_setting == "horizontal"):
                    return CameraUtil.MatchHorizontally
                if (conform_setting == 0) or (conform_setting == "vertical"):
                    return CameraUtil.MatchVertically
                if (conform_setting == 2) or (conform_setting == "fit"):
                    return CameraUtil.Fit
                if (conform_setting == 3) or (conform_setting == "crop"):
                    return CameraUtil.Crop
                if (conform_setting == 4) or (conform_setting == "stretch"):
                    return CameraUtil.DontConform
                
        """
    def _ViewportAPI__notify_objects(self, fn_container: typing.Sequence):
        ...
    def _ViewportAPI__notify_scene_views(self, view: bool, proj: bool):
        ...
    def _ViewportAPI__set_hydra_texture(self, viewport_texture, hydra_texture):
        ...
    def _ViewportAPI__subscribe_to_change(self, callback: typing.Callable, container: set, name: str):
        ...
    def __del__(self):
        ...
    def __init__(self, usd_context_name: str, viewport_id: str, viewport_changed_fn: typing.Optional[typing.Callable]):
        ...
    def _conform_projection(self, policy, camera: pxr.UsdGeom.Camera, image_aspect: float, canvas_aspect: float, projection: typing.Sequence[float] = None):
        """
        
                For the given camera (or possible incoming projection) return a projection matrix that matches the rendered image
                but keeps NDC co-ordinates for the texture bound to [-1, 1]
                
        """
    def _notify_frame_change(self):
        ...
    def _notify_render_settings_change(self):
        ...
    def _sync_viewport_api(self, camera: pxr.UsdGeom.Camera, canvas_size: typing.Sequence[int], time: pxr.Usd.TimeCode | None = None, view: typing.Sequence[float] = None, projection: typing.Sequence[float] = None, force_update: bool = False):
        """
        Sync the ui and viewport state, and inform any view-scubscribers if a change occured
        """
    def add_scene_view(self, scene_view):
        """
        
                Add an omni.ui.scene.SceneView to push view and projection changes to.
                The provided scene_view will be saved as a weak-ref.
        
                Args:
                    scene_view (omni.ui.scene.SceneView): The scene_view to add into this Viewport
                
        """
    def get_active_camera(self) -> pxr.Sdf.Path:
        """
        Deprecated method to return an Sdf.Path to the active rendering camera
        """
    def get_full_texture_resolution(self) -> typing.Tuple[float, float]:
        """
        Return a tuple of (full_resolution_x, full_resolution_y)
        """
    def get_render_product_path(self) -> str:
        """
        Deprecated method to return a string to the UsdRender.Product used by the Viewport
        """
    def get_texture_resolution(self) -> typing.Tuple[float, float]:
        """
        Deprecated method to return a tuple of (resolution_x, resolution_y)
        """
    def get_texture_resolution_scale(self) -> float:
        """
        Get the scaling factor for the Viewport's render resolution.
        """
    def map_ndc_to_texture(self, mouse: typing.Sequence[float]) -> typing.Tuple[typing.Tuple[float, float], ForwardRef('ViewportAPI')]:
        ...
    def map_ndc_to_texture_pixel(self, mouse: typing.Sequence[float]) -> typing.Tuple[typing.Tuple[float, float], ForwardRef('ViewportAPI')]:
        ...
    def pick(self, *args, **kwargs):
        ...
    def query(self, mouse, *args, **kwargs):
        ...
    def remove_scene_view(self, scene_view):
        """
        
                Remove an omni.ui.scene.SceneView that was receiving view and projection changes.
        
                Args:
                    scene_view (omni.ui.scene.SceneView): The scene_view to add into this Viewport
                
        """
    def request_pick(self, *args, **kwargs):
        """
        
                Request a pick in the Viewport.
        
                Args:
                    top_left (Tuple[int, int]): Top left corner for the pick (in pixel coordinates).
                    bottom_right (Tuple[int, int]): Bottom right corner for the pick (in pixel coordinates).
                    mode (omni.usd.PickingMode): The mode that wil effect the selection when the pick completes.
                
        """
    def request_query(self, *args, **kwargs):
        """
        
                Request a query into the world the Viewport is rendering.
        
                Args:
                    pixel (Tuple[int, int]): The pixel to query the scene from
                    callback (Callable): Object to invoke when the query completes.
                        def on_query_complete(prim_path: str, world_pos: Tuple[float, float, float], viewport_api)
                    query_name (str): Give the name a query so it can be replaced/updated with a new one before completed.
                
        """
    def schedule_capture(self, delegate: omni.kit.widget.viewport.capture.Capture) -> omni.kit.widget.viewport.capture.Capture:
        """
        
                Schedule a capture of the rendered output
        
                Args:
                    delegate (Capture): The object to invoke when the capture has completed.
                
        """
    def set_active_camera(self, camera_path: pxr.Sdf.Path):
        """
        Deprecated method to set the active rendering camera from an Sdf.Path
        """
    def set_render_product_path(self, *args, **kwargs):
        """
        Set the UsdRender.Product used by the Viewport with a string and optional arguments
        """
    def set_texture_resolution(self, value: typing.Tuple[float, float]):
        """
        Deprecated method to set the resolution to render with (resolution_x, resolution_y)
        """
    def set_texture_resolution_scale(self, value: float):
        """
        Set the scaling factor for the Viewport's render resolution.
        """
    def set_updates_enabled(self, enabled: bool = True):
        ...
    def subscribe_to_frame_change(self, callback: typing.Callable):
        """
        
                Add a function to be called when the renderer has delivered a new frame.
        
                Args:
                    callback (Callable): The object to invoke when the renderer has delivered a new frame.
                
        """
    def subscribe_to_render_settings_change(self, callback: typing.Callable):
        """
        
                Add a function to be called when the renderer's setting have changed (such as resolution, renderer in use)
        
                Args:
                    callback (Callable): The object to invoke when the renderer's setting have changed.
                
        """
    def subscribe_to_view_change(self, callback: typing.Callable):
        """
        
                Add a function to be called when the camera-view changes.
        
                Args:
                    callback (Callable): The object to invoke when the camera-view changes.
                
        """
    def wait_for_render_settings_change(self):
        ...
    def wait_for_rendered_frames(self, additional_frames: int = 0):
        ...
    @property
    def _hydra_texture(self):
        ...
    @property
    def _settings_path(self) -> str:
        ...
    @property
    def _viewport_texture(self):
        ...
    @property
    def camera_path(self) -> pxr.Sdf.Path:
        """
        Return an Sdf.Path to the active rendering camera
        """
    @camera_path.setter
    def camera_path(self, camera_path: typing.Union[pxr.Sdf.Path, str]):
        """
        Set the active rendering camera from an Sdf.Path
        """
    @property
    def display_render_var(self) -> str | None:
        ...
    @display_render_var.setter
    def display_render_var(self, name: str):
        ...
    @property
    def fps(self) -> float:
        """
        Return the frames-per-second this Viewport is running at
        """
    @property
    def frame_info(self) -> dict:
        ...
    @property
    def full_resolution(self) -> typing.Tuple[float, float]:
        """
        Return a tuple of the full (full_resolution_x, full_resolution_y) this Viewport is rendering at, not accounting for scale.
        """
    @property
    def hydra_engine(self):
        """
        Get the name of the active omni.hydra.engine for this Viewport
        """
    @hydra_engine.setter
    def hydra_engine(self, hd_engine: str):
        """
        Set the name of the active omni.hydra.engine for this Viewport
        """
    @property
    def id(self) -> str:
        ...
    @property
    def ndc_to_world(self) -> pxr.Gf.Matrix4d:
        ...
    @property
    def projection(self) -> pxr.Gf.Matrix4d:
        """
        Return the projection of the UsdCamera in terms of the ui element it sits in.
        """
    @property
    def render_mode(self):
        """
        Get the render-mode for the active omni.hydra.engine used in this Viewport
        """
    @render_mode.setter
    def render_mode(self, render_mode: str):
        """
        Set the render-mode for the active omni.hydra.engine used in this Viewport
        """
    @property
    def render_product_path(self) -> str:
        """
        Return a string to the UsdRender.Product used by the Viewport
        """
    @render_product_path.setter
    def render_product_path(self, prim_path: str):
        """
        Set the UsdRender.Product used by the Viewport with a string
        """
    @property
    def resolution(self) -> typing.Tuple[float, float]:
        """
        Return a tuple of (resolution_x, resolution_y) this Viewport is rendering at, accounting for scale.
        """
    @resolution.setter
    def resolution(self, value: typing.Tuple[float, float]):
        """
        Set the resolution to render with (resolution_x, resolution_y).
                The provided resolution should be full resolution, as any texture scaling will be applied to it.
        """
    @property
    def resolution_scale(self) -> float:
        """
        Get the scaling factor for the Viewport's render resolution.
        """
    @resolution_scale.setter
    def resolution_scale(self, value: float):
        """
        Set the scaling factor for the Viewport's render resolution.
        """
    @property
    def set_hd_engine(self):
        """
        Set the active omni.hydra.engine for this Viewport, and optionally its render-mode
        """
    @property
    def stage(self) -> pxr.Usd.Stage:
        """
        Return the Usd.Stage of the omni.usd.UsdContext this Viewport is attached to
        """
    @property
    def time(self) -> pxr.Usd.TimeCode:
        """
        Return the Usd.TimeCode this Viewport is using
        """
    @property
    def transform(self) -> pxr.Gf.Matrix4d:
        """
        Return the world-space transform of the UsdGeom.Camera being used to render
        """
    @property
    def usd_context(self):
        """
        Return the omni.usd.UsdContext this Viewport is attached to
        """
    @property
    def usd_context_name(self) -> str:
        """
        Return the name of the omni.usd.UsdContext this Viewport is attached to
        """
    @property
    def view(self) -> pxr.Gf.Matrix4d:
        """
        Return the inverse of the world-space transform of the UsdGeom.Camera being used to render
        """
    @property
    def viewport_changed(self):
        ...
    @property
    def world_to_ndc(self) -> pxr.Gf.Matrix4d:
        ...
