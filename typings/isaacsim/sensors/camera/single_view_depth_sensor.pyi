from __future__ import annotations
import carb as carb
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.utils.xforms import reset_and_set_xform_ops
import isaacsim.sensors.camera.camera
from isaacsim.sensors.camera.camera import Camera
import numpy as np
import omni as omni
from pxr import Gf
from pxr import Usd
import pxr.Usd
__all__: list[str] = ['Camera', 'Gf', 'SingleViewDepthSensor', 'SingleViewDepthSensorAsset', 'Usd', 'add_reference_to_stage', 'carb', 'get_prim_at_path', 'np', 'omni', 'reset_and_set_xform_ops']
class SingleViewDepthSensor(isaacsim.sensors.camera.camera.Camera):
    _render_product_prim = None
    def get_baseline_mm(self) -> float:
        """
        Get the baseline distance in millimeters.
        """
    def get_confidence_threshold(self) -> float:
        """
        Get the confidence threshold for the depth sensor.
        """
    def get_enabled(self) -> bool:
        """
        Get whether the depth sensor is enabled.
        """
    def get_focal_length_pixel(self) -> float:
        """
        Get the focal length in pixels.
        """
    def get_max_disparity_pixel(self) -> float:
        """
        Get the maximum disparity in pixels.
        """
    def get_max_distance(self) -> float:
        """
        Get the maximum distance for disparity generation.
        """
    def get_min_distance(self) -> float:
        """
        Get the minimum distance for disparity generation.
        """
    def get_noise_downscale_factor_pixel(self) -> float:
        """
        Get the noise downscale factor in pixels.
        """
    def get_noise_mean(self) -> float:
        """
        Get the noise mean.
        """
    def get_noise_sigma(self) -> float:
        """
        Get the noise sigma.
        """
    def get_outlier_removal_enabled(self) -> int:
        """
        Get the outlier removal enabled attribute. Samples separated by this range (in pixels) will be removed.
        """
    def get_rgb_depth_output_mode(self) -> int:
        """
        Get the RGB depth output mode.
        """
    def get_sensor_size_pixel(self) -> int:
        """
        Get the sensor size in pixels.
        """
    def get_show_distance(self) -> bool:
        """
        Get whether to show the distance.
        """
    def initialize(self, physics_sim_view = None, attach_rgb_annotator = False) -> None:
        """
        Initialize the depth camera.
        
                Calls the parent class's initialize method, then retrieves the render product prim
                and applies the appropriate schema to enable depth sensing functionality.
        
                Supports the following annotators:
                - DepthSensorDistance
                - DepthSensorPointCloudPosition
                - DepthSensorPointCloudColor
                - DepthSensorImager
                
        """
    def set_baseline_mm(self, baseline_mm: float = 55) -> None:
        """
        Set the baseline distance in millimeters.
        """
    def set_confidence_threshold(self, confidence_threshold: float = 0.95) -> None:
        """
        Set the confidence threshold for the depth sensor.
        """
    def set_enabled(self, enabled: bool = False) -> None:
        """
        Enable or disable the depth sensor.
        """
    def set_focal_length_pixel(self, focal_length_pixel: float = 897) -> None:
        """
        Set the focal length in pixels.
        """
    def set_max_disparity_pixel(self, max_disparity_pixel: float = 110) -> None:
        """
        Set the maximum disparity in pixels.
        """
    def set_max_distance(self, max_distance: float = 10000000) -> None:
        """
        Set the maximum distance for disparity generation.
        """
    def set_min_distance(self, min_distance: float = 0.5) -> None:
        """
        Set the minimum distance for disparity generation.
        """
    def set_noise_downscale_factor_pixel(self, noise_downscale_factor_pixel: float = 1) -> None:
        """
        Set the noise downscale factor in pixels.
        """
    def set_noise_mean(self, noise_mean: float = 0.25) -> None:
        """
        Set the noise mean.
        """
    def set_noise_sigma(self, noise_sigma: float = 0.25) -> None:
        """
        Set the noise sigma.
        """
    def set_outlier_removal_enabled(self, outlier_removal_enabled: int = 3) -> None:
        """
        Set the outlier removal enabled attribute. Samples separated by this range (in pixels) will be removed.
        """
    def set_rgb_depth_output_mode(self, rgb_depth_output_mode: int = 0) -> None:
        """
        Set the RGB depth output mode.
        """
    def set_sensor_size_pixel(self, sensor_size_pixel: int = 1280) -> None:
        """
        Set the sensor size in pixels.
        """
    def set_show_distance(self, show_distance: bool = False) -> None:
        """
        Set whether to show the distance.
        """
class SingleViewDepthSensorAsset:
    """
    Asset-based wrapper for single view depth sensors.
    
        This class provides a high-level interface for working with single view depth sensor assets.
        It automatically discovers and manages depth sensor templates from USD assets and provides
        access to individual depth sensors through their camera prim paths.
    
        The class handles the initialization of depth sensor assets by:
        1. Loading the specified USD asset as a reference on the stage
        2. Discovering render products with depth sensor schemas
        3. Creating SingleViewDepthSensor instances for each discovered camera
        4. Managing the mapping between render products and depth sensors
    
        Args:
            prim_path: The USD prim path where the asset will be placed.
            asset_path: The relative path to the USD asset file within the assets root.
            position: World position of the asset as a numpy array [x, y, z]. Defaults to None.
            translation: Local translation of the asset as a numpy array [x, y, z]. Defaults to None.
            orientation: Quaternion orientation as a numpy array [w, x, y, z]. Defaults to [1.0, 0.0, 0.0, 0.0].
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.sensors.camera import SingleViewDepthSensorAsset
            >>> import numpy as np
            >>>
            >>> # Create a depth sensor asset
            >>> depth_sensor_asset = SingleViewDepthSensorAsset(
            ...     prim_path="/World/DepthSensor",
            ...     asset_path="/Isaac/Sensors/DepthSensor/depth_sensor.usd",
            ...     position=np.array([0.0, 0.0, 1.0]),
            ...     orientation=np.array([1.0, 0.0, 0.0, 0.0])
            ... )
            >>>
            >>> # Initialize all the depth sensors inthe asset
            >>> depth_sensor_asset.initialize()
            >>>
            >>> # Get a specific depth sensor by camera prim path
            >>> depth_sensor = depth_sensor_asset.get_child_depth_sensor("/World/DepthSensor/Camera")
        
    """
    @staticmethod
    def add_template_render_product(parent_prim_path: str, camera_prim_path: str, **kwargs) -> pxr.Usd.Prim:
        """
        Add a template render product for a depth sensor to the USD stage.
        
                This static method creates a new RenderProduct prim with the depth sensor API
                and establishes a relationship with the specified camera prim. The render product
                is created as a child of the specified parent prim and is named based on the
                camera prim's name with "_render_product" suffix.
        
                The method performs validation to ensure:
                - The parent prim path is valid
                - The camera prim exists and is of type "Camera"
                - The render product can be successfully created
        
                Args:
                    parent_prim_path: The USD path to the parent prim where the render product will be created.
                        If the path ends with "/", it will be automatically removed.
                    camera_prim_path: The USD path to the camera prim that will be associated with the render product.
                    **kwargs: Additional keyword arguments to pass to the RenderProduct prim as attributes.
        
                Raises:
                    RuntimeError: If the USD stage cannot be accessed.
                    ValueError: If the camera prim path is invalid or the prim is not a Camera.
        
                Example:
        
                .. code-block:: python
        
                    >>> from isaacsim.sensors.camera import SingleViewDepthSensorAsset
                    >>>
                    >>> # Add a template render product for a depth sensor
                    >>> SingleViewDepthSensorAsset.add_template_render_product(
                    ...     parent_prim_path="/World/DepthSensor",
                    ...     camera_prim_path="/World/DepthSensor/Camera"
                    ... )
                    >>>
                    >>> # This creates a render product at "/World/DepthSensor/Camera_render_product"
                    >>> # with the OmniSensorDepthSensorSingleViewAPI applied and a relationship
                    >>> # to the camera at "/World/DepthSensor/Camera"
                
        """
    def __init__(self, prim_path: str, asset_path: str, position: typing.Optional[numpy.ndarray] = None, translation: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = ...) -> None:
        ...
    def _make_depth_sensor_from_render_product(self, render_product_path: str, camera_prim_path: str) -> SingleViewDepthSensor:
        """
        Create a SingleViewDepthSensor instance from a render product.
        
                This method extracts the resolution from the template render product and creates
                a new SingleViewDepthSensor instance with the specified camera prim path.
        
                Args:
                    render_product_path: The USD path to the template render product.
                    camera_prim_path: The USD path to the camera prim.
        
                Returns:
                    A configured SingleViewDepthSensor instance.
                
        """
    def get_all_depth_sensor_paths(self) -> typing.List[str]:
        """
        Get all depth sensor paths in the asset.
        """
    def get_all_depth_sensors(self) -> typing.List[isaacsim.sensors.camera.single_view_depth_sensor.SingleViewDepthSensor]:
        """
        Get all depth sensors in the asset.
        """
    def get_child_depth_sensor(self, camera_prim_path: str) -> SingleViewDepthSensor:
        """
        Get a specific depth sensor by its camera prim path.
        
                This method returns the SingleViewDepthSensor instance associated with the
                specified camera prim path. This allows access to individual depth sensors
                within the asset for configuration and data retrieval.
        
                Args:
                    camera_prim_path: The USD path to the camera prim.
        
                Returns:
                    The SingleViewDepthSensor instance for the specified camera.
        
                Raises:
                    KeyError: If no depth sensor is found for the specified camera prim path.
        
                Example:
        
                .. code-block:: python
        
                    >>> depth_sensor_asset = SingleViewDepthSensorAsset(
                    ...     prim_path="/World/DepthSensor",
                    ...     asset_path="/Isaac/Sensors/DepthSensor/depth_sensor.usd"
                    ... )
                    >>>
                    >>> # Get a specific depth sensor
                    >>> depth_sensor = depth_sensor_asset.get_child_depth_sensor("/World/DepthSensor/Camera")
                    >>>
                    >>> # Configure the depth sensor
                    >>> depth_sensor.set_baseline_mm(60.0)
                    >>> depth_sensor.set_confidence_threshold(0.95)
                
        """
    def initialize(self, physics_sim_view = None, attach_rgb_annotator = False) -> None:
        """
        Initialize all child depth sensors in the asset.
        
                This method initializes each depth sensor template and copies depth sensor
                attributes from the template render products to the actual render products.
                This ensures that all depth sensors have the correct configuration.
        
                Each depth sensor will be enabled, even if the template render product is disabled.
        
                Args:
                    physics_sim_view: Optional physics simulation view. Defaults to None.
                    attach_rgb_annotator: Whether to attach RGB annotator. Defaults to False.
        
                Example:
        
                .. code-block:: python
        
                    >>> depth_sensor_asset = SingleViewDepthSensorAsset(
                    ...     prim_path="/World/DepthSensor",
                    ...     asset_path="/Isaac/Sensors/DepthSensor/depth_sensor.usd"
                    ... )
                    >>>
                    >>> # Initialize all depth sensors in the asset
                    >>> depth_sensor_asset.initialize(attach_rgb_annotator=True)
                
        """
