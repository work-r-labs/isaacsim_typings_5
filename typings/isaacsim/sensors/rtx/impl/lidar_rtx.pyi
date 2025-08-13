from __future__ import annotations
import carb as carb
import isaacsim.core.api.sensors.base_sensor
from isaacsim.core.api.sensors.base_sensor import BaseSensor
from isaacsim.core.nodes.bindings import _isaacsim_core_nodes
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_type_name
from isaacsim.core.utils.prims import is_prim_path_valid
import numpy as np
import omni as omni
from omni.graph import core as og
from omni.replicator import core as rep
from pxr import Gf
__all__: list[str] = ['BaseSensor', 'Gf', 'LidarRtx', 'carb', 'get_prim_at_path', 'get_prim_type_name', 'is_prim_path_valid', 'np', 'og', 'omni', 'rep']
class LidarRtx(isaacsim.core.api.sensors.base_sensor.BaseSensor):
    """
    RTX-based Lidar sensor implementation.
    
        This class provides functionality for creating and managing RTX-based Lidar sensors in Isaac Sim.
        It supports various annotators and writers for data collection and visualization.
    
        The sensor can be configured with different parameters and supports both point cloud and flat scan data collection.
        
    """
    @staticmethod
    def make_add_remove_deprecated_attr(deprecated_attr: str):
        """
        Creates deprecated add/remove attribute methods.
        
                Args:
                    param deprecated_attr (str): Name of the deprecated attribute to create methods for.
        
                Returns:
                    list: List of method functions for adding and removing the deprecated attribute.
                
        """
    def __del__(self):
        ...
    def __init__(self, prim_path: str, name: str = 'lidar_rtx', position: typing.Optional[numpy.ndarray] = None, translation: typing.Optional[numpy.ndarray] = None, orientation: typing.Optional[numpy.ndarray] = ..., config_file_name: typing.Optional[str] = None, **kwargs) -> None:
        """
        Initialize the RTX Lidar sensor.
        
                Args:
                    param prim_path (str): Path to the USD prim for the Lidar sensor.
                    param name (str): Name of the Lidar sensor.
                    param position (Optional[np.ndarray]): Global position of the sensor as [x, y, z].
                    param translation (Optional[np.ndarray]): Local translation of the sensor as [x, y, z].
                    param orientation (Optional[np.ndarray]): Orientation quaternion as [w, x, y, z].
                    param config_file_name (Optional[str]): Path to the configuration file for the sensor.
                    param **kwargs: Additional keyword arguments for sensor configuration.
        
                Raises:
                    Exception: If the prim at prim_path is not an OmniLidar or doesn't have the required API.
                
        """
    def _create_flat_scan_graph_node(self):
        """
        Create a flat scan graph node for the Lidar sensor.
        
                This method is deprecated as of Isaac Sim 5.0. Use attach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def _create_point_cloud_graph_node(self):
        """
        Create a point cloud graph node for the Lidar sensor.
        
                This method is deprecated as of Isaac Sim 5.0. Use attach_annotator('IsaacExtractRTXSensorPointCloud') instead.
                
        """
    def _data_acquisition_callback(self, event: carb.events._events.IEvent):
        """
        Handle data acquisition callback for the Lidar sensor.
        
                Args:
                    param event (carb.events.IEvent): The event that triggered the callback.
                
        """
    def _stage_open_callback_fn(self, event):
        """
        Handle stage open event by cleaning up callbacks.
        
                Args:
                    param event (carb.events.IEvent): The stage open event.
                
        """
    def _timeline_timer_callback_fn(self, event):
        """
        Handle timeline timer events for pausing and resuming the sensor.
        
                Args:
                    param event (carb.events.IEvent): The timeline event.
                
        """
    def add_azimuth_data_to_frame(self):
        """
        Add azimuth data to the current frame.
        
                This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.
                
        """
    def add_azimuth_range_to_frame(self):
        """
        Add azimuth range data to the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use attach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def add_elevation_data_to_frame(self):
        """
        Add elevation data to the current frame.
        
                This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.
                
        """
    def add_horizontal_resolution_to_frame(self):
        """
        Add horizontal resolution data to the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use attach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def add_intensities_data_to_frame(self):
        """
        Add intensities data to the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use attach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def add_linear_depth_data_to_frame(self):
        """
        Add linear depth data to the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use attach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def add_point_cloud_data_to_frame(self):
        """
        Add point cloud data to the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use attach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def add_range_data_to_frame(self):
        """
        Add range data to the current frame.
        
                This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.
                
        """
    def attach_annotator(self, annotator_name: typing.Literal['IsaacComputeRTXLidarFlatScan', 'IsaacExtractRTXSensorPointCloudNoAccumulator', 'IsaacCreateRTXLidarScanBuffer']) -> None:
        """
        Attach an annotator to the Lidar sensor.
        
                Args:
                    param annotator_name (Literal): Name of the annotator to attach. Must be one of:
                        - "IsaacComputeRTXLidarFlatScan"
                        - "IsaacExtractRTXSensorPointCloudNoAccumulator"
                        - "IsaacCreateRTXLidarScanBuffer"
                
        """
    def attach_writer(self, writer_name: str) -> None:
        """
        Attach a writer to the Lidar sensor.
        
                Args:
                    param writer_name (str): Name of the writer to attach.
                
        """
    def detach_all_annotators(self) -> None:
        """
        Detach all annotators from the Lidar sensor.
        """
    def detach_all_writers(self) -> None:
        """
        Detach all writers from the Lidar sensor.
        """
    def detach_annotator(self, annotator_name: str) -> None:
        """
        Detach an annotator from the Lidar sensor.
        
                Args:
                    param annotator_name (str): Name of the annotator to detach.
                
        """
    def detach_writer(self, writer_name: str) -> None:
        """
        Detach a writer from the Lidar sensor.
        
                Args:
                    param writer_name (str): Name of the writer to detach.
                
        """
    def disable_visualization(self):
        """
        Disable visualization of the Lidar point cloud data.
        """
    def enable_visualization(self):
        """
        Enable visualization of the Lidar point cloud data.
        """
    def get_annotators(self) -> dict:
        """
        Get all attached annotators.
        
                Returns:
                    dict: Dictionary mapping annotator names to their instances.
                
        """
    def get_azimuth_range(self) -> typing.Tuple[float, float]:
        """
        Get the azimuth range of the Lidar sensor.
        
                This method is deprecated as of Isaac Sim 5.0. Use the azimuth_range attribute in the current frame instead.
        
                Returns:
                    Optional[Tuple[float, float]]: Tuple of (min_azimuth, max_azimuth) if available, None otherwise.
                
        """
    def get_current_frame(self) -> dict:
        """
        Get the current frame data from the Lidar sensor.
        
                Returns:
                    dict: Dictionary containing the current frame data including rendering time,
                        frame number, and any attached annotator data.
                
        """
    def get_depth_range(self) -> typing.Tuple[float, float]:
        """
        Get the depth range of the Lidar sensor.
        
                This method is deprecated as of Isaac Sim 5.0. Use the depth_range attribute in the current frame instead.
        
                Returns:
                    Optional[Tuple[float, float]]: Tuple of (min_depth, max_depth) if available, None otherwise.
                
        """
    def get_horizontal_fov(self) -> float:
        """
        Get the horizontal field of view of the Lidar sensor.
        
                This method is deprecated as of Isaac Sim 5.0. Use the horizontal_fov attribute in the current frame instead.
        
                Returns:
                    Optional[float]: The horizontal field of view value if available, None otherwise.
                
        """
    def get_horizontal_resolution(self) -> float:
        """
        Get the horizontal resolution of the Lidar sensor.
        
                This method is deprecated as of Isaac Sim 5.0. Use the horizontal_resolution attribute in the current frame instead.
        
                Returns:
                    Optional[float]: The horizontal resolution value if available, None otherwise.
                
        """
    def get_num_cols(self) -> int:
        """
        Get the number of columns in the Lidar scan.
        
                This method is deprecated as of Isaac Sim 5.0. Use the num_cols attribute in the current frame instead.
        
                Returns:
                    Optional[int]: The number of columns if available, None otherwise.
                
        """
    def get_num_rows(self) -> int:
        """
        Get the number of rows in the Lidar scan.
        
                This method is deprecated as of Isaac Sim 5.0. Use the num_rows attribute in the current frame instead.
        
                Returns:
                    Optional[int]: The number of rows if available, None otherwise.
                
        """
    def get_render_product_path(self) -> str:
        """
        Get the path to the render product used by the Lidar.
        
                Returns:
                    str: Path to the render product.
                
        """
    def get_rotation_frequency(self) -> float:
        """
        Get the rotation frequency of the Lidar sensor.
        
                This method is deprecated as of Isaac Sim 5.0. Use the rotation_frequency attribute in the current frame instead.
        
                Returns:
                    Optional[float]: The rotation frequency value if available, None otherwise.
                
        """
    def get_writers(self) -> dict:
        """
        Get all attached writers.
        
                Returns:
                    dict: Dictionary mapping writer names to their instances.
                
        """
    def initialize(self, physics_sim_view = None) -> None:
        """
        Initialize the Lidar sensor.
        
                Args:
                    param physics_sim_view (Optional): Optional physics simulation view.
                
        """
    def is_paused(self) -> bool:
        """
        Check if the Lidar sensor is paused.
        
                Returns:
                    True if the sensor is paused, False otherwise.
                
        """
    def pause(self) -> None:
        """
        Pause data acquisition for the Lidar sensor.
        """
    def post_reset(self) -> None:
        """
        Perform post-reset operations for the Lidar sensor.
        """
    def remove_azimuth_data_to_frame(self):
        """
        Remove azimuth data from the current frame.
        
                This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.
                
        """
    def remove_azimuth_range_to_frame(self):
        """
        Remove azimuth range data from the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use detach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def remove_elevation_data_to_frame(self):
        """
        Remove elevation data from the current frame.
        
                This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.
                
        """
    def remove_horizontal_resolution_to_frame(self):
        """
        Remove horizontal resolution data from the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use detach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def remove_intensities_data_to_frame(self):
        """
        Remove intensities data from the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use detach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def remove_linear_depth_data_to_frame(self):
        """
        Remove linear depth data from the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use detach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def remove_point_cloud_data_to_frame(self):
        """
        Remove point cloud data from the current frame.
        
                This method is deprecated as of Isaac Sim 5.0. Use detach_annotator('IsaacComputeRTXLidarFlatScanSimulationTime') instead.
                
        """
    def remove_range_data_to_frame(self):
        """
        Remove range data from the current frame.
        
                This method is deprecated as of Isaac Sim 5.0 and will be removed in a future release.
                
        """
    def resume(self) -> None:
        """
        Resume data acquisition for the Lidar sensor.
        """
