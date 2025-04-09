from __future__ import annotations
import pxr.Gf
from pxr import Gf
from pxr import Sdf
import pxr.Usd
from pxr import Usd
from pxr import UsdGeom
__all__: list = ['ViewportCameraState']
class ViewportCameraState:
    """
    A class that encapsulates the state of a camera within a viewport.
    
        It provides methods to query and manipulate the camera's position, target, and other properties, taking into account the stage's up axis and other USD-specific details.
    
        Args:
            camera_path: str
                The path to the camera in USD.
            viewport: The viewport associated with the camera state.
            time: Usd.TimeCode
                The time code for sampling the camera data.
            force_legacy_api: bool
                Flag to force use of the legacy API if available.
    """
    def __init__(self, camera_path: str = None, viewport = None, time: pxr.Usd.TimeCode = None, force_legacy_api: bool = False):
        """
        Initializes the viewport camera state with a given camera path, viewport, time, and legacy API flag.
        
                Args:
                    camera_path (str, optional): The path to the camera in USD. Defaults to the active viewport camera path if not provided.
                    viewport (optional): The viewport to associate with the camera state. Defaults to the active viewport if not provided.
                    time (Usd.TimeCode, optional): The time code for sampling the camera data. Defaults to Usd.TimeCode.Default() if not provided.
                    force_legacy_api (bool, optional): A flag to force the use of the legacy API if available. Defaults to False.
        
                Raises:
                    RuntimeError: If no default or provided viewport is found.
        """
    def get_world_camera_up(self, stage) -> pxr.Gf.Vec3d:
        """
        Returns the world space up direction for the camera based on the stage's up axis.
        
                Args:
                    stage (Usd.Stage): The stage from which to retrieve the up axis information.
        
                Returns:
                    Gf.Vec3d: The world space up direction vector for the camera.
        """
    def set_position_world(self, world_position: pxr.Gf.Vec3d, rotate: bool):
        """
        Sets the world position of the camera, with an option to rotate it to maintain its current orientation.
        
                Args:
                    world_position (Gf.Vec3d): The new world position for the camera.
                    rotate (bool): If True, the camera will be rotated to maintain its current orientation towards the center of interest.
                
        """
    def set_target_world(self, world_target: pxr.Gf.Vec3d, rotate: bool):
        """
        Sets the world target of the camera, with an option to rotate it. This can either move the camera to keep the same orientation and distance or just rotate the camera to look at the new target.
        
                Args:
                    world_target (Gf.Vec3d): The new world target position for the camera.
                    rotate (bool): If True, the camera will rotate to look at the new target. If False, the camera will move to maintain its orientation and distance relative to the target.
                
        """
    @property
    def position_world(self):
        """
        Gets the world position of the camera.
        
                Returns:
                    Gf.Vec3d: The world position of the camera as a Gf.Vec3d vector.
        """
    @property
    def target_world(self):
        """
        Gets the world space target position of the camera.
        
                Returns:
                    Gf.Vec3d: The world space target position of the camera as a Gf.Vec3d vector.
        """
    @property
    def usd_camera(self) -> pxr.Usd.Prim:
        """
        Retrieves the USD camera primitive associated with the camera path.
        
                Returns:
                    Usd.Prim: The USD camera primitive.
        
                Raises:
                    RuntimeError: If the camera path does not correspond to a valid Usd.Prim or UsdGeom.Camera.
        """
