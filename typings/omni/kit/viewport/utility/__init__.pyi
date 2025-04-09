"""
An utility module to access [active] Viewport information
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from pxr import Gf
import pxr.Sdf
from pxr import Sdf
import typing
from . import camera_state
__all__: list = ['frame_viewport_prims', 'frame_viewport_selection', 'get_viewport_from_window_name', 'get_active_viewport', 'get_active_viewport_window', 'get_active_viewport_and_window', 'get_viewport_window_camera_path', 'get_viewport_window_camera_string', 'get_active_viewport_camera_path', 'get_active_viewport_camera_string', 'get_num_viewports', 'capture_viewport_to_file', 'capture_viewport_to_buffer', 'post_viewport_message', 'toggle_global_visibility', 'create_drop_helper', 'disable_selection', 'get_ground_plane_info']
class ViewportPrimReferencePoint:
    """
    An enumeration for specifying reference points on a USD prim's bounding box within a viewport.
    """
    BOUND_BOX_BOTTOM: typing.ClassVar[int] = 4
    BOUND_BOX_CENTER: typing.ClassVar[int] = 0
    BOUND_BOX_LEFT: typing.ClassVar[int] = 1
    BOUND_BOX_RIGHT: typing.ClassVar[int] = 2
    BOUND_BOX_TOP: typing.ClassVar[int] = 3
class _CaptureHelper:
    def __init__(self, legacy_window, is_hdr: bool, file_path: str = None, render_product_path: str = None, on_capture_fn: typing.Callable = None, format_desc: dict = None):
        ...
    def capture_function(self, *args):
        ...
    def wait_for_result(self, completion_frames: int = 2):
        ...
class _DisableViewportWindowLayer:
    def __del__(self):
        ...
    def __init__(self, viewport_or_window, layers_and_categories):
        ...
def __frame_viewport_objects(viewport_api = None, prims: typing.Optional[typing.List[str]] = None, force_legacy_api: bool = False):
    ...
def _get_default_viewport_window_name(window_name: str = None):
    ...
def _is_viewport_next(self):
    ...
def add_aov_to_viewport(viewport_api, aov_name: str):
    """
    Adds an Arbitrary Output Variable (AOV) to the specified viewport.
    
        Args:
            viewport_api: The viewport API instance to which the AOV will be added.
            aov_name (str): The name of the AOV to add.
    
        Returns:
            bool: True if the AOV was successfully added, False otherwise.
    
        Raises:
            RuntimeError: If the renderProduct or renderVar cannot be created or set.
        
    """
def capture_viewport_to_buffer(viewport_api, on_capture_fn: typing.Callable, is_hdr: bool = False):
    """
    
        Captures the current viewport and sends the image to a callback function.
    
        Args:
            viewport_api (ViewportAPI): The viewport API instance to capture.
            on_capture_fn (Callable): The callback function that will receive the image.
            is_hdr (bool, optional): If True, captures the HDR buffer; otherwise, captures the LDR buffer. Defaults to False.
    
        Returns:
            A future-like object that can be awaited to ensure the capture completes.
        
    """
def capture_viewport_to_file(viewport_api, file_path: str = None, is_hdr: bool = False, render_product_path: str = None, format_desc: dict = None):
    """
    Capture the provided viewport to a file.
    
        Args:
            viewport_api (ViewportAPI): The viewport API instance to capture.
            file_path (str, optional): The file path where the captured image will be saved. If not specified, a default path is used.
            is_hdr (bool, optional): If True, captures the HDR buffer; otherwise, captures the LDR buffer. Defaults to False.
            render_product_path (str, optional): Render product path to use for capturing. Defaults to None.
            format_desc (dict, optional): A dictionary describing the format in which to save the captured image. Defaults to None.
    
        Returns:
            A future-like object that can be awaited to ensure the capture completes.
        
    """
def create_drop_helper(*args, **kwargs):
    """
    
        Creates a helper object to handle drag-and-drop operations in a viewport.
    
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
    
        Returns:
            Any: The drop helper object that can be used to manage drag-and-drop events.
        
    """
def create_viewport_window(name: str = None, usd_context_name: str = '', width: int = 1280, height: int = 720, position_x: int = 0, position_y: int = 0, camera_path: pxr.Sdf.Path = None, **kwargs):
    """
    Creates a new viewport window with the given parameters.
    
        Args:
            name (str, optional): The name of the new viewport window. If None, a default name is generated.
            usd_context_name (str, optional): The name of the USD context to associate with the new viewport window.
            width (int, optional): The width of the new viewport window in pixels.
            height (int, optional): The height of the new viewport window in pixels.
            position_x (int, optional): The x-coordinate of the new viewport window's position.
            position_y (int, optional): The y-coordinate of the new viewport window's position.
            camera_path (Sdf.Path, optional): The path to the camera to be used in the new viewport window.
            **kwargs: Arbitrary keyword arguments to be passed into create_viewport_window.
    
        Returns:
            The created viewport window or None if the creation fails.
        
    """
def disable_context_menu(viewport_or_window = None):
    """
    Disable context menu on a Viewport or ViewportWindow.
        Returns an object that resets context menu visibility when it goes out of scope.
    
        Args:
            viewport_or_window (ViewportAPI or ViewportWindow, optional): The viewport API instance or viewport window to which the context menu disabling will be applied.
    
        Returns:
            object: An object that, upon deletion, will reset the context menu capability to its original state.
        
    """
def disable_selection(viewport_or_window, disable_click: bool = True):
    """
    Disables selection for a given viewport.
    
        Disable selection rect and possible the single click selection on a Viewport or ViewportWindow.
        Returns an object that resets selection when it goes out of scope.
    
        Args:
            viewport_or_window: The viewport API instance or viewport window to which the selection disabling will be applied.
            disable_click (bool, optional): If set to True, disables single click selection. Defaults to True.
    
        Returns:
            object: An object that, upon deletion, will reset the selection capability to its original state.
        
    """
def frame_viewport_prims(viewport_api = None, prims: typing.List[str] = None):
    """
    Frames the view of the viewport to include the specified prims.
    
        Args:
            viewport_api (ViewportAPI, optional): The viewport API instance to operate on.
                If not provided, the active viewport is used.
            prims (List[str], optional): A list of USD prim paths to frame in the viewport.
                If not provided or empty, no action is taken.
    
        Returns:
            bool: True if the operation was successful, False otherwise.
    """
def frame_viewport_selection(viewport_api = None, force_legacy_api: bool = False):
    """
    Frames the camera in the viewport to include the current selection.
    
        This function adjusts the camera in the viewport to frame the currently
        selected objects. If no objects are selected, it adjusts the camera to show
        the entire scene.
    
        Args:
            viewport_api (ViewportAPI, optional): The viewport API instance to operate on.
                If not provided, the active viewport is used.
            force_legacy_api (bool, optional): If set to True, forces the use of the legacy viewport API.
                Defaults to False.
    
        Returns:
            bool: True if the operation was successful, False otherwise.
    """
def get_active_viewport(usd_context_name: str = ''):
    """
    
        Retrieves the active viewport API instance for a given USD context.
    
        If no USD context name is provided, the current USD context is used.
    
        Args:
            usd_context_name (str, optional): The name of the USD context to query. Defaults to an empty string,
                which indicates the current USD context.
    
        Returns:
            Optional[ViewportAPI]: The active viewport API instance, or None if not found.
        
    """
def get_active_viewport_and_window(usd_context_name: str = '', wrap_legacy: bool = True, window_name: str = None):
    """
    
        Retrieves the active viewport and its window for a given USD context and window name.
    
        Args:
            usd_context_name (str, optional): The name of the USD context to query. If empty, the current USD context is used.
            wrap_legacy (bool, optional): Flag to determine if a legacy viewport should be wrapped.
            window_name (str, optional): The name of the window to query. If none is provided, defaults to the viewport window name from settings.
    
        Returns:
            Tuple[Optional[ViewportAPI], Optional[Window]]: A tuple containing the active viewport API instance and the corresponding window instance, or (None, None) if not found.
        
    """
def get_active_viewport_camera_path(usd_context_name: str = '') -> pxr.Sdf.Path:
    """
    
        Retrieves the camera Sdf.Path for the active viewport within a specified USD context.
    
        Args:
            usd_context_name (str, optional): The name of the USD context to query.
                If empty, the current USD context is used. Defaults to an empty string.
    
        Returns:
            Sdf.Path: The SDF path to the camera used by the active viewport, or None if no active viewport is found.
        
    """
def get_active_viewport_camera_string(usd_context_name: str = '') -> str:
    """
    
        Retrieves the camera path string for the active viewport within a specified USD context.
    
        Args:
            usd_context_name (str, optional): The name of the USD context to query.
                If empty, the current USD context is used. Defaults to an empty string.
    
        Returns:
            str: The camera path string for the active viewport, or an empty string if no active viewport is found.
        
    """
def get_active_viewport_window(window_name: str = None, wrap_legacy: bool = True, usd_context_name: str = ''):
    """
    
        Retrieves the active viewport window, optionally for a specified USD context and window name.
    
        Args:
            window_name (str, optional): The name of the window to query. If none is provided, defaults to the viewport window name from settings.
            wrap_legacy (bool, optional): Flag to determine if a legacy viewport should be wrapped.
            usd_context_name (str, optional): The name of the USD context to query. If empty, the current USD context is used.
    
        Returns:
            Optional[Window]: The active viewport window instance or None if not found.
        
    """
def get_available_aovs_for_viewport(viewport_api):
    """
    Retrieves a list of available AOVs for the given viewport.
    
        This function checks if the viewport API has a legacy window and retrieves the AOV list accordingly.
        If the viewport API does not have a legacy window or the AOVs are not implemented, an error is logged.
    
        Args:
            viewport_api (ViewportAPI): The viewport API instance for which to retrieve the available AOVs.
    
        Returns:
            List[str]: A list of AOV names that are available for the given viewport. If AOVs are not implemented, returns an empty list.
        
    """
def get_ground_plane_info(viewport, ortho_special: bool = True) -> typing.Tuple[pxr.Gf.Vec3d, typing.List[str]]:
    """
    
        Retrieves the ground plane information including its normal and the planes it occupies.
    
        Args:
            viewport (ViewportAPI): The viewport API instance for which to get the ground plane information.
            ortho_special (bool, optional): If True, uses an alternate ground plane for orthographic cameras
                that are looking down a single axis. Defaults to True.
    
        Returns:
            Tuple[Gf.Vec3d, List[str]]: A tuple containing the ground plane normal vector and a list of
                plane axes it occupies (e.g., ['x', 'z']).
        
    """
def get_num_viewports(usd_context_name: str = None):
    """
    
        Returns the number of active viewports within an optional USD context.
    
        Args:
            usd_context_name (str, optional): The name of the USD context for which to count the viewports.
                If None, all viewports across all USD contexts are counted. Defaults to None.
    
        Returns:
            int: The number of active viewports.
        
    """
def get_ui_position_for_prim(viewport_window, prim_path: str, alignment: ViewportPrimReferencePoint = 0, force_legacy_api: bool = False):
    """
    
        Calculates the UI position of a given USD primitive in the viewport window.
    
        Args:
            viewport_window: The viewport window instance or its name as a string.
            prim_path (str): The USD path to the primitive whose UI position is to be calculated.
            alignment (ViewportPrimReferencePoint, optional): The reference point on the primitive's bounding box to align with.
                Defaults to ViewportPrimReferencePoint.BOUND_BOX_CENTER.
            force_legacy_api (bool, optional): If True, forces the use of the legacy viewport API regardless of current viewport API.
                Defaults to False.
    
        Returns:
            Tuple[Tuple[float, float], bool]: A tuple containing the (x, y) UI position of the primitive and a boolean indicating success.
        
    """
def get_viewport_from_window_name(window_name: str = None):
    """
    
        Retrieves the first viewport API instance from a specified window name.
    
        If a window name is not provided or is None, it defaults to the viewport window name
        defined in the settings ('/exts/omni.kit.viewport.window/startup/windowName') or 'Viewport'.
    
        Args:
            window_name (str, optional): The name of the window from which to retrieve the viewport API.
    
        Returns:
            Optional[ViewportAPI]: An instance of the viewport API or None if no viewport was found.
        
    """
def get_viewport_window_camera_path(window_name: str = None) -> pxr.Sdf.Path:
    """
    Retrieves the camera path for the viewport in the specified window.
    
        If the window name is not provided, the default viewport window is used.
    
        Args:
            window_name (str, optional): The name of the window from which to retrieve the camera path.
    
        Returns:
            Sdf.Path: The SDF path to the camera used by the viewport, or None if the viewport is not found.
        
    """
def get_viewport_window_camera_string(window_name: str = None) -> str:
    """
    
        Retrieves the camera path string for the viewport in the specified window.
    
        If the window name is not provided, the default viewport window is used.
    
        Args:
            window_name (str, optional): The name of the window from which to retrieve the camera path string.
    
        Returns:
            str: The camera path string for the viewport, or None if the viewport is not found.
        
    """
def next_viewport_frame_async(viewport, n_frames: int = 0):
    """
    
        Waits until frames have been delivered to the Viewport.
    
        Args:
            viewport: the Viewport to wait for a frame on.
            n_frames: the number of rendered frames to wait for.
        
    """
def post_viewport_message(viewport_api_or_window, message: str, message_id: str = None):
    """
    
        Posts a message as a toast notification to the viewport or viewport window.
    
        Args:
            viewport_api_or_window: The viewport API instance or viewport window to which the message will be posted.
            message (str): The content of the message to post.
            message_id (str, optional): A unique identifier for the message. Defaults to None.
        
    """
def toggle_global_visibility(force_legacy_api: bool = False):
    """
    
        .. deprecated:: 1.0.15
            use omni.kit.viewport.actions.toggle_global_visibility instead.
    
        Toggles the global visibility of all viewport layers.
    
        This function is used to toggle the visibility of all the viewport layers, such as the grid, axis, and
        stage lights. It can be useful when you want to declutter the viewport or focus on specific elements.
    
        Args:
            force_legacy_api (bool, optional): If True, forces the use of the legacy viewport API. Defaults to False.
        
    """
_g_is_viewport_next = None
