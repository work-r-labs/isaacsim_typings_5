"""

    This Extension provides an interface to 'pxr.IsaacSensorSchemaIsaacBaseSensor' to be used in a stage.
    
"""
from __future__ import annotations
import carb._carb
import typing
__all__ = ['ContactSensorInterface', 'CsRawData', 'CsSensorReading', 'ImuSensorInterface', 'IsSensorReading', 'acquire_contact_sensor_interface', 'acquire_imu_sensor_interface', 'release_contact_sensor_interface', 'release_imu_sensor_interface']
class ContactSensorInterface:
    """
    """
    def decode_body_name(self, arg0: int) -> str:
        """
                        Decodes the body name pointers from the contact raw data into a string
                        Args:
                            arg0 (:obj:`int`): body name handle
                        Returns:
                            :obj:`str`: The body name.
        """
    def get_contact_sensor_raw_data(self, arg0: str) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`str`): USD Path to contact sensor as string
        
                        Returns:
                            :obj:`numpy.array`: The list of contact raw data that contains the specified body that the contact sensor is attached to.
        """
    def get_rigid_body_raw_data(self, arg0: str) -> typing.Any:
        """
                        Get raw data from a rigid body that have contact report API enabled
                        Args:
                            arg0 (:obj:`str`): USD Path to rigid body as string
        
                        Returns:
                            :obj:`numpy.array`: The list of contact raw data that contains the specified body.
        """
    def get_sensor_reading(self, sensor_path: str, use_latest_data: bool = False) -> CsSensorReading:
        """
                        Args:
                            arg0 (:obj:`char*`): the sensor path
                            arg1 (:obj:`bool`): use_latest_data
                        Returns:
                            :obj:`numpy.array`: The reading for the current sensor period.
        """
    def is_contact_sensor(self, arg0: str) -> bool:
        """
                        Args:
                            arg0 (:obj:`str`): USD Path to sensor as string
                        Returns:
                            :obj:`bool`: True for is contact sensor, False for not contact sensor.
        """
class CsRawData:
    """
    Contact Raw Data
    """
    def __init__(self) -> None:
        ...
    @property
    def body0(self) -> int:
        """
        Body 0 name handle, (:obj:`int`)
        """
    @property
    def body1(self) -> int:
        """
        Body 1 name handle, (:obj:`int`)
        """
    @property
    def dt(self) -> float:
        """
        timestep during this contact report, (:obj:`float`)
        """
    @dt.setter
    def dt(self, arg0: float) -> None:
        ...
    @property
    def impulse(self) -> carb._carb.Float3:
        """
        impulse, global coordinates , (:obj:`carb.Float3`)
        """
    @impulse.setter
    def impulse(self, arg0: carb._carb.Float3) -> None:
        ...
    @property
    def normal(self) -> carb._carb.Float3:
        """
        normal, global coordinates , (:obj:`carb.Float3`)
        """
    @normal.setter
    def normal(self, arg0: carb._carb.Float3) -> None:
        ...
    @property
    def position(self) -> carb._carb.Float3:
        """
        position, global coordinates, (:obj:`carb.Float3`)
        """
    @position.setter
    def position(self, arg0: carb._carb.Float3) -> None:
        ...
    @property
    def time(self) -> float:
        """
        simulation timestamp, (:obj:`float`)
        """
    @time.setter
    def time(self, arg0: float) -> None:
        ...
class CsSensorReading:
    """
    Contact Sensor Reading
    """
    def __init__(self) -> None:
        ...
    @property
    def inContact(self) -> bool:
        """
        **Deprecation Alert**, inContact will be renamed to in_contact. boolean that flags if the sensor registers a contact. (:obj:`bool`)
        """
    @inContact.setter
    def inContact(self, arg0: bool) -> None:
        ...
    @property
    def in_contact(self) -> bool:
        """
        boolean that flags if the sensor registers a contact. (:obj:`bool`)
        """
    @in_contact.setter
    def in_contact(self, arg0: bool) -> None:
        ...
    @property
    def is_valid(self) -> bool:
        """
        validity of the data. (:obj:`bool`)
        """
    @is_valid.setter
    def is_valid(self, arg0: bool) -> None:
        ...
    @property
    def time(self) -> float:
        """
        timestamp of the reading, in seconds . (:obj:`float`)
        """
    @time.setter
    def time(self, arg0: float) -> None:
        ...
    @property
    def value(self) -> float:
        """
        sensor force reading value. (:obj:`float`)
        """
    @value.setter
    def value(self, arg0: float) -> None:
        ...
class ImuSensorInterface:
    """
    """
    def get_sensor_reading(self, sensor_path: str, interpolation_function: typing.Callable[[list[IsSensorReading], float], IsSensorReading] = None, use_latest_data: bool = False, read_gravity: bool = True) -> typing.Any:
        """
                        Args:
                            arg0 (:obj:`char*`): the sensor path
                            arg1 (:obj:`std::function<IsReading(std::vector<IsReading>, float)>&`): interpolation_function
                            arg2 (:obj:`bool`): use_latest_data
                            arg3 (:obj:`bool`): read_gravity
                        Returns:
                            :obj:`numpy.array`: The reading for the current sensor period.
        """
    def is_imu_sensor(self, arg0: str) -> bool:
        """
                        Args:
                            arg0 (:obj:`str`): USD Path to sensor as string
                        Returns:
                            :obj:`bool`: True for is imu sensor, False for not imu sensor.
        """
class IsSensorReading:
    """
    Imu Sensor Reading
    """
    def __init__(self) -> None:
        ...
    @property
    def ang_vel_x(self) -> float:
        """
        Gyroscope reading value x axis, in rad/s. (:obj:`float`)
        """
    @ang_vel_x.setter
    def ang_vel_x(self, arg0: float) -> None:
        ...
    @property
    def ang_vel_y(self) -> float:
        """
        Gyroscope reading value y axis, in rad/s. (:obj:`float`)
        """
    @ang_vel_y.setter
    def ang_vel_y(self, arg0: float) -> None:
        ...
    @property
    def ang_vel_z(self) -> float:
        """
        Gyroscope reading value z axis, in rad/s. (:obj:`float`)
        """
    @ang_vel_z.setter
    def ang_vel_z(self, arg0: float) -> None:
        ...
    @property
    def is_valid(self) -> bool:
        """
        validity of sensor reading. (:obj:`bool`)
        """
    @is_valid.setter
    def is_valid(self, arg0: bool) -> None:
        ...
    @property
    def lin_acc_x(self) -> float:
        """
        Accelerometer reading value x axis, in m/s^2. (:obj:`float`)
        """
    @lin_acc_x.setter
    def lin_acc_x(self, arg0: float) -> None:
        ...
    @property
    def lin_acc_y(self) -> float:
        """
        Accelerometer reading value y axis, in m/s^2. (:obj:`float`)
        """
    @lin_acc_y.setter
    def lin_acc_y(self, arg0: float) -> None:
        ...
    @property
    def lin_acc_z(self) -> float:
        """
        Accelerometer reading value z axis, in m/s^2. (:obj:`float`)
        """
    @lin_acc_z.setter
    def lin_acc_z(self, arg0: float) -> None:
        ...
    @property
    def orientation(self) -> carb._carb.Float4:
        """
        Orientation quaternion reading (x, y, z, w). (:obj:`carb.Float4`)
        """
    @orientation.setter
    def orientation(self, arg0: carb._carb.Float4) -> None:
        ...
    @property
    def time(self) -> float:
        """
        timestamp of the reading, in seconds. (:obj:`float`)
        """
    @time.setter
    def time(self, arg0: float) -> None:
        ...
def acquire_contact_sensor_interface(plugin_name: str = None, library_path: str = None) -> ...:
    """
    Acquire Contact Sensor interface. This is the base object that all of the Contact Sensor functions are defined on
    """
def acquire_imu_sensor_interface(plugin_name: str = None, library_path: str = None) -> ...:
    """
    Acquire Contact Sensor interface. This is the base object that all of the Contact Sensor functions are defined on
    """
def release_contact_sensor_interface(arg0: ...) -> None:
    """
    Release Contact Sensor interface. Generally this does not need to be called, the Contact Sensor interface is released on extension shutdown
    """
def release_imu_sensor_interface(arg0: ...) -> None:
    """
    Release Contact Sensor interface. Generally this does not need to be called, the Contact Sensor interface is released on extension shutdown
    """
