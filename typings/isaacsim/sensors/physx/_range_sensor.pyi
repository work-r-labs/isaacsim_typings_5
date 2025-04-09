"""

        This extension provides an interface to a `pxr.RangeSensorSchemaLidar` prim defined in a stage.

        Example:
            To use this interface you must first call the acquire interface function.
            It is also recommended to use the `is_range_sensor` function to check if a given USD path is valid

            ::

                import isaacsim.sensors.physx._range_sensor.acquire_lidar_sensor_interface
                lidar_sensor_interface = acquire_lidar_sensor_interface()
                if lidar_sensor_interface.is_lidar_sensor("/World/Lidar"):
                    print("range_sensor is valid")

        Refer to the sample documentation for more examples and usage
                
"""
from __future__ import annotations
import numpy
import typing
__all__ = ['GenericSensorInterface', 'LidarSensorInterface', 'LightBeamSensorInterface', 'acquire_generic_sensor_interface', 'acquire_lidar_sensor_interface', 'acquire_lightbeam_sensor_interface', 'release_generic_sensor_interface', 'release_lidar_sensor_interface', 'release_lightbeam_sensor_interface']
class GenericSensorInterface:
    def get_azimuth_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The azimuth angle in radians for each column
        """
    def get_depth_data(self, arg0: str) -> typing.Any:
        """
                    Args:
                        arg0 (:obj:`str`): USD path to sensor as a string
        
                    Returns:
                        :obj:`numpy.ndarray`: The distance from the sensor to the hit for each beam in uint16 and scaled by min and max distance
        """
    def get_intensity_data(self, arg0: str) -> typing.Any:
        """
                    Args:
                        arg0 (:obj:`str`): USD path to sensor as a string
        
                    Returns:
                        :obj:`numpy.ndarray`: The observed specular intensity of each beam, 255 if hit, 0 if not
        """
    def get_linear_depth_data(self, arg0: str) -> typing.Any:
        """
                    Args:
                        arg0 (:obj:`str`): USD path to sensor as a string
        
                    Returns:
                        :obj:`numpy.ndarray`: The distance from the sensor to the hit for each beam in meters
        """
    def get_num_samples_ticked(self, arg0: str) -> int:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                             :obj:`int`: The number of sample points the sensor completed in the last simulation step, 0 if error occurred.
        """
    def get_point_cloud_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The hit position in xyz relative to the sensor origin, not accounting for individual ray offsets
        """
    def get_zenith_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The zenith angle in radians for each row
        """
    def is_generic_sensor(self, arg0: str) -> bool:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`bool`: True if a sensor exists at the give path, False otherwise
        """
    def send_next_batch(self, arg0: str) -> bool:
        """
        ready for next batch
        """
    def set_next_batch_offsets(self, arg0: str, arg1: numpy.ndarray[numpy.float32]) -> None:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
                            arg1 (:obj:`numpy.ndaray`): The offset xyz, a 2D array for individual rays, or 1D array for a constant offset
        """
    def set_next_batch_rays(self, arg0: str, arg1: numpy.ndarray[numpy.float32]) -> None:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
                            arg1 (:obj:`numpy.ndaray`): The azimuth and zenith angles in radians for each column
        """
class LidarSensorInterface:
    def get_azimuth_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The azimuth angle in radians for each column
        """
    def get_depth_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The distance from the sensor to the hit for each beam in uint16 and scaled by min and max distance
        """
    def get_intensity_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The observed specular intensity of each beam, 255 if hit, 0 if not
        """
    def get_linear_depth_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The distance from the sensor to the hit for each beam in meters
        """
    def get_num_cols(self, arg0: str) -> int:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`int`: The number of vertical scans of the sensor, 0 if error occurred
        """
    def get_num_cols_ticked(self, arg0: str) -> int:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                             :obj:`int`: The number of vertical scans the sensor completed in the last simulation step, 0 if error occurred. Generally only useful for lidars with a non-zero rotation speed
        """
    def get_num_rows(self, arg0: str) -> int:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                             :obj:`int`: The number of horizontal scans of the sensor, 0 if error occurred
        """
    def get_point_cloud_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The hit position in xyz relative to the sensor origin, not accounting for individual ray offsets
        """
    def get_prim_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`list`: The prim path of the hit for each beam as a string
        """
    def get_semantic_data(self, arg0: str) -> typing.Any:
        """
        [Deprecated]
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The semantic id of the hit for each beam in uint16
        """
    def get_zenith_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The zenith angle in radians for each row
        """
    def is_lidar_sensor(self, arg0: str) -> bool:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`bool`: True if a sensor exists at the give path, False otherwise
        """
class LightBeamSensorInterface:
    def get_beam_hit_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: True for light beam sensor detecting a raycast hit, False for not no hit
        """
    def get_hit_pos_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: Hit positions in xyz for each light beam relative to sensor origin
        """
    def get_linear_depth_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD path to sensor as a string
        
                        Returns:
                            :obj:`numpy.ndarray`: The distance from the sensor to the hit for each light beam in meters
        """
    def get_num_rays(self, arg0: str) -> int:
        """
                        Args:
                            arg0 (:obj:`str`): USD Path to sensor as string
                        Returns:
                            :obj:`int`: The number of rays in the light curtain.
        """
    def is_lightbeam_sensor(self, arg0: str) -> bool:
        """
                        Args:
                            arg0 (:obj:`str`): USD Path to sensor as string
                        Returns:
                            :obj:`bool`: True for is light beam sensor, False for not light beam sensor.
        """
def acquire_generic_sensor_interface(plugin_name: str = None, library_path: str = None) -> GenericSensorInterface:
    ...
def acquire_lidar_sensor_interface(plugin_name: str = None, library_path: str = None) -> LidarSensorInterface:
    ...
def acquire_lightbeam_sensor_interface(plugin_name: str = None, library_path: str = None) -> LightBeamSensorInterface:
    ...
def release_generic_sensor_interface(arg0: GenericSensorInterface) -> None:
    ...
def release_lidar_sensor_interface(arg0: LidarSensorInterface) -> None:
    ...
def release_lightbeam_sensor_interface(arg0: LightBeamSensorInterface) -> None:
    ...
