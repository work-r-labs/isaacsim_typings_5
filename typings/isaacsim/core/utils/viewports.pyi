from __future__ import annotations
import carb as carb
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.prims import set_prim_hide_in_stage_window
from isaacsim.core.utils.prims import set_prim_no_delete
from isaacsim.core.utils.stage import get_current_stage
import numpy as np
import numpy
import omni as omni
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
__all__ = ['Gf', 'Sdf', 'Usd', 'UsdGeom', 'add_aov_to_viewport', 'backproject_depth', 'carb', 'create_viewport_for_camera', 'destroy_all_viewports', 'get_current_stage', 'get_id_from_index', 'get_intrinsics_matrix', 'get_viewport_names', 'get_window_from_id', 'is_prim_path_valid', 'np', 'omni', 'project_depth_to_worldspace', 'set_camera_view', 'set_intrinsics_matrix', 'set_prim_hide_in_stage_window', 'set_prim_no_delete']
def add_aov_to_viewport(viewport_api, aov_name: str):
    ...
def backproject_depth(depth_image: numpy.array, viewport_api: typing.Any, max_clip_depth: float) -> numpy.array:
    """
    Backproject depth image to image space
    
        Args:
            depth_image (np.array): Depth image buffer
            viewport_api (Any): Handle to viewport api
            max_clip_depth (float): Depth values larger than this will be clipped
    
        Returns:
            np.array: [description]
        
    """
def create_viewport_for_camera(viewport_name: str, camera_prim_path: str, width: int = 1280, height: int = 720, position_x: int = 0, position_y: int = 0):
    """
    Create a new viewport and peg it to a specific camera specified by camera_prim_path. If the viewport already exists with the specified viewport_name, that viewport will be replaced with the new camera view.
    
        Args:
            viewport_name (str): name of the viewport. If not provided, it will default to camera name.
            camera_prim_path (str): name of the prim path of the camera
            width (int): width of the viewport window, in pixels.
            height (int): height of the viewport window, in pixels.
            position_x (int): location x of the viewport window.
            position_y (int): location y of the viewport window.
        
    """
def destroy_all_viewports(usd_context_name: str = None, destroy_main_viewport = True):
    """
    Destroys all viewport windows
    
        Args:
            usd_context_name (str, optional): usd context to use. Defaults to None.
            destroy_main_viewport (bool, optional): set to true to not destroy the default viewport. Defaults to False.
        
    """
def get_id_from_index(index):
    """
    Get the viewport id for a given index.
        This function was added for backwards compatibility for VP2 as viewport IDs are not the same as the viewport index
    
        Args:
            index (_type_): viewport index to retrieve ID for
    
        Returns:
            viewport id : Returns None if window index was not found
        
    """
def get_intrinsics_matrix(viewport_api: typing.Any) -> numpy.ndarray:
    """
    Get intrinsic matrix for the camera attached to a specific viewport
    
        Args:
            viewport (Any): Handle to viewport api
    
        Returns:
            np.ndarray: the intrinsic matrix associated with the specified viewport
                    The following image convention is assumed:
                        +x should point to the right in the image
                        +y should point down in the image
        
    """
def get_viewport_names(usd_context_name: str = None) -> typing.List[str]:
    """
    Get list of all viewport names
    
        Args:
            usd_context_name (str, optional):  usd context to use. Defaults to None.
    
        Returns:
            List[str]: List of viewport names
        
    """
def get_window_from_id(id, usd_context_name: str = None):
    """
    Find window that matches a given viewport id
    
        Args:
            id (_type_): Viewport ID to get window for
            usd_context_name (str, optional): usd context to use. Defaults to None.
    
        Returns:
            Window : Returns None if window with matching ID was not found
        
    """
def project_depth_to_worldspace(depth_image: numpy.array, viewport_api: typing.Any, max_clip_depth: float) -> typing.List[carb._carb.Float3]:
    """
    Project depth image to world space
    
        Args:
            depth_image (np.array): Depth image buffer
            viewport_api (Any): Handle to viewport api
            max_clip_depth (float): Depth values larger than this will be clipped
    
        Returns:
            List[carb.Float3]: List of points from depth in world space
        
    """
def set_camera_view(eye: numpy.array, target: numpy.array, camera_prim_path: str = '/OmniverseKit_Persp', viewport_api = None) -> None:
    """
    Set the location and target for a camera prim in the stage given its path
    
        Args:
            eye (np.ndarray): Location of camera.
            target (np.ndarray,): Location of camera target.
            camera_prim_path (str, optional): Path to camera prim being set. Defaults to "/OmniverseKit_Persp".
        
    """
def set_intrinsics_matrix(viewport_api: typing.Any, intrinsics_matrix: numpy.ndarray, focal_length: float = 1.0) -> None:
    """
    Set intrinsic matrix for the camera attached to a specific viewport
    
        Note:
            We assume cx and cy are centered in the camera
            horizontal_aperture_offset and vertical_aperture_offset are computed and set on the camera prim but are not used
    
        Args:
            viewport (Any): Handle to viewport api
            intrinsics_matrix (np.ndarray): A 3x3 intrinsic matrix
            focal_length (float, optional): Default focal length to use when computing aperture values. Defaults to 1.0.
    
        Raises:
            ValueError: If intrinsic matrix is not a 3x3 matrix.
            ValueError: If camera prim is not valid
        
    """
