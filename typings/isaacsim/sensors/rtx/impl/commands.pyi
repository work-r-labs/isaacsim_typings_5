from __future__ import annotations
import carb as carb
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.utils.stage import get_next_free_path
from isaacsim.core.utils.xforms import reset_and_set_xform_ops
from isaacsim.storage.native.nucleus import get_assets_root_path
import omni as omni
from omni.isaac import IsaacSensorSchema
from omni.replicator import core as rep
from pathlib import Path
from pxr import Gf
from pxr import Sdf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import typing
__all__: list[str] = ['Gf', 'IsaacSensorCreateRtxIDS', 'IsaacSensorCreateRtxLidar', 'IsaacSensorCreateRtxRadar', 'IsaacSensorCreateRtxSensor', 'IsaacSensorCreateRtxUltrasonic', 'IsaacSensorSchema', 'Path', 'SUPPORTED_LIDAR_CONFIGS', 'SUPPORTED_LIDAR_VARIANT_SET_NAME', 'Sdf', 'Usd', 'UsdGeom', 'add_reference_to_stage', 'carb', 'get_assets_root_path', 'get_next_free_path', 'omni', 'rep', 'reset_and_set_xform_ops']
class IsaacSensorCreateRtxIDS(IsaacSensorCreateRtxSensor):
    """
    Command class for creating RTX Idealized Depth Sensors (IDSs).
    
        This class specializes the base RTX sensor creation for IDSs, providing
        specific configuration and plugin settings for IDS functionality.
    
        Attributes:
            _sensor_type: Set to "ids".
            _sensor_plugin_name: Name of the IDS sensor plugin.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    _sensor_plugin_name: typing.ClassVar[str] = 'omni.sensors.nv.ids.ids.plugin'
    _sensor_type: typing.ClassVar[str] = 'ids'
    def __init__(self, **kwargs):
        """
        Initialize the RTX IDS sensor creation command.
        
                Sets default configuration to "idsoccupancy" if no config is provided.
        
                Args:
                    **kwargs: Keyword arguments passed to the parent class constructor.
                
        """
class IsaacSensorCreateRtxLidar(IsaacSensorCreateRtxSensor):
    """
    Command class for creating RTX Lidar sensors.
    
        This class specializes the base RTX sensor creation for Lidar sensors, providing
        specific configuration and plugin settings for Lidar functionality.
    
        Attributes:
            _replicator_api: Static method reference to the Lidar Replicator API.
            _sensor_type: Set to "lidar".
            _supported_configs: List of supported Lidar configurations.
            _schema: Schema for Lidar sensors.
            _sensor_plugin_name: Name of the Lidar sensor plugin.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    _sensor_plugin_name: typing.ClassVar[str] = 'omni.sensors.nv.lidar.lidar_core.plugin'
    _sensor_type: typing.ClassVar[str] = 'lidar'
    _supported_configs: typing.ClassVar[dict] = {'/Isaac/Sensors/HESAI/XT32_SD10/HESAI_XT32_SD10.usd': set(), '/Isaac/Sensors/NVIDIA/Example_Rotary_2D.usda': set(), '/Isaac/Sensors/NVIDIA/Example_Rotary.usda': set(), '/Isaac/Sensors/NVIDIA/Example_Solid_State.usda': set(), '/Isaac/Sensors/NVIDIA/Simple_Example_Solid_State.usda': set(), '/Isaac/Sensors/Ouster/OS0/OS0.usd': {'OS0_REV6_128ch20hz1024res', 'OS0_REV6_128ch10hz1024res', 'OS0_REV7_128ch20hz1024res', 'OS0_REV7_128ch20hz512res', 'OS0_REV7_128ch10hz512res', 'OS0_REV7_128ch10hz2048res', 'OS0_REV6_128ch10hz2048res', 'OS0_REV6_128ch10hz512res', 'OS0_REV6_128ch20hz512res', 'OS0_REV7_128ch10hz1024res'}, '/Isaac/Sensors/Ouster/OS1/OS1.usd': {'OS1_REV7_128ch10hz1024res', 'OS1_REV6_128ch10hz2048res', 'OS1_REV6_32ch20hz512res', 'OS1_REV6_128ch20hz512res', 'OS1_REV6_128ch10hz1024res', 'OS1_REV6_128ch20hz1024res', 'OS1_REV7_128ch10hz512res', 'OS1_REV7_128ch10hz2048res', 'OS1_REV7_128ch20hz1024res', 'OS1_REV6_32ch10hz1024res', 'OS1_REV6_128ch10hz512res', 'OS1_REV7_128ch20hz512res', 'OS1_REV6_32ch10hz2048res', 'OS1_REV6_32ch20hz1024res', 'OS1_REV6_32ch10hz512res'}, '/Isaac/Sensors/Ouster/OS2/OS2.usd': {'OS2_REV7_128ch20hz1024res', 'OS2_REV6_128ch10hz2048res', 'OS2_REV7_128ch20hz512res', 'OS2_REV6_128ch10hz512res', 'OS2_REV7_128ch10hz1024res', 'OS2_REV7_128ch10hz512res', 'OS2_REV6_128ch10hz1024res', 'OS2_REV7_128ch10hz2048res', 'OS2_REV6_128ch20hz1024res', 'OS2_REV6_128ch20hz512res'}, '/Isaac/Sensors/Ouster/VLS_128/Ouster_VLS_128.usd': set(), '/Isaac/Sensors/SICK/microScan3/SICK_microScan3.usd': {'Profile_1', 'Profile_5', 'Profile_3', 'Profile_4', 'Profile_6', 'Profile_2'}, '/Isaac/Sensors/SICK/multiScan136/SICK_multiScan136.usd': set(), '/Isaac/Sensors/SICK/multiScan165/SICK_multiScan165.usd': set(), '/Isaac/Sensors/SICK/nanoScan3/SICK_nanoScan3.usd': {'CAAZ30AN1'}, '/Isaac/Sensors/SICK/picoScan150/SICK_picoScan150.usd': {'Profile_9', 'Profile_7', 'Profile_3', 'Profile_6', 'Profile_2', 'Profile_8', 'Profile_11', 'Profile_5', 'Profile_4', 'Profile_10', 'Profile_1'}, '/Isaac/Sensors/SICK/TIM781/SICK_TIM781.usd': set(), '/Isaac/Sensors/Slamtec/RPLIDAR_S2E/Slamtec_RPLIDAR_S2E.usd': set(), '/Isaac/Sensors/ZVISION/ZVISION_ML30S.usda': set(), '/Isaac/Sensors/ZVISION/ZVISION_MLXS.usda': set()}
    _schema = omni.isaac.IsaacSensorSchema.IsaacRtxLidarSensorAPI
    @staticmethod
    def _replicator_api(position: typing.Union[float, typing.Tuple[float]] = None, rotation: typing.Union[float, typing.Tuple[float]] = None, name: typing.Optional[str] = None, parent: typing.Union[str, pxr.Sdf.Path, pxr.Usd.Prim] = None, **kwargs) -> typing.List[typing.Union[pxr.Usd.Prim, usdrt.Usd._Usd.Prim]]:
        """
        Create a LiDAR sensor.
        
            Args:
                position: XYZ coordinates in world space. If a single value is provided, all axes will be set to that value.
                rotation: Euler angles in degrees in XYZ order. If a single value is provided, all axes will be set to that
                    value.
                name: Name for the LiDAR sensor
                parent: Parent prim path to create LiDAR under
                **kwargs: Additional attributes to be added to the LiDAR sensor
        
            Example:
                >>> import omni.replicator.core as rep
                >>> # Create LiDAR sensor
                >>> lidar = rep.functional.create.omni_lidar(
                ...     position=(100, 100, 100),
                ...     rotation=(45, 45, 0),
                ... )
            
        """
    def __init__(self, **kwargs):
        """
        Initialize the RTX Lidar sensor creation command.
                Args:
                    **kwargs: Keyword arguments passed to the parent class constructor.
                
        """
    def do(self) -> pxr.Usd.Prim:
        """
        Executes the sensor creation command.
        """
class IsaacSensorCreateRtxRadar(IsaacSensorCreateRtxSensor):
    """
    Command class for creating RTX Radar sensors.
    
        This class specializes the base RTX sensor creation for Radar sensors, providing
        specific configuration and plugin settings for Radar functionality.
    
        Attributes:
            _replicator_api: Static method reference to the Radar Replicator API.
            _sensor_type: Set to "radar".
            _schema: Schema for Radar sensors.
            _sensor_plugin_name: Name of the Radar sensor plugin.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    _sensor_plugin_name: typing.ClassVar[str] = 'omni.sensors.nv.radar.wpm_dmatapprox.plugin'
    _sensor_type: typing.ClassVar[str] = 'radar'
    _schema = omni.isaac.IsaacSensorSchema.IsaacRtxRadarSensorAPI
    @staticmethod
    def _replicator_api(position: typing.Union[float, typing.Tuple[float]] = None, rotation: typing.Union[float, typing.Tuple[float]] = None, name: typing.Optional[str] = None, parent: typing.Union[str, pxr.Sdf.Path, pxr.Usd.Prim] = None, **kwargs) -> typing.List[typing.Union[pxr.Usd.Prim, usdrt.Usd._Usd.Prim]]:
        """
        Create a Radar sensor.
        
            Args:
                position: XYZ coordinates in world space. If a single value is provided, all axes will be set to that value.
                rotation: Euler angles in degrees in XYZ order. If a single value is provided, all axes will be set to that
                    value.
                name: Name for the Radar sensor
                parent: Parent prim path to create Radar under
                **kwargs: Additional attributes to be added to the Radar sensor
        
            Example:
                >>> import omni.replicator.core as rep
                >>> # Create Radar sensor
                >>> radar = rep.functional.create.omni_radar(
                ...     position=(100, 100, 100),
                ...     rotation=(45, 45, 0),
                ... )
            
        """
class IsaacSensorCreateRtxSensor(omni.kit.commands.command.Command):
    """
    Base class for creating RTX sensors in Isaac Sim.
    
        This class provides functionality to create various types of RTX sensors (lidar, radar, etc.)
        in the Isaac Sim environment. It handles sensor creation through either USD references,
        Replicator API, or direct camera prim creation.
    
        Attributes:
            _replicator_api: Static method reference to the Replicator API for sensor creation.
            _sensor_type: String identifier for the type of sensor.
            _supported_configs: List of supported sensor configurations.
            _schema: Schema for the sensor type.
            _sensor_plugin_name: Name of the sensor plugin.
            _camera_config_name: Name of the camera configuration.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    _camera_config_name: typing.ClassVar[str] = ''
    _replicator_api = None
    _schema = None
    _sensor_plugin_name: typing.ClassVar[str] = ''
    _sensor_type: typing.ClassVar[str] = 'sensor'
    _supported_configs: typing.ClassVar[list] = list()
    def __init__(self, path: typing.Optional[str] = None, parent: typing.Optional[str] = None, config: typing.Optional[str] = None, translation: typing.Optional[pxr.Gf.Vec3d] = ..., orientation: typing.Optional[pxr.Gf.Quatd] = ..., visibility: typing.Optional[bool] = False, variant: typing.Optional[str] = None, force_camera_prim: bool = False, **kwargs):
        """
        Initialize the RTX sensor creation command.
        
                Args:
                    path: Optional path where the sensor will be created. If None, a default path will be used.
                    parent: Optional parent prim path for the sensor.
                    config: Optional configuration name for the sensor.
                    translation: Optional 3D translation vector for sensor placement.
                    orientation: Optional quaternion for sensor orientation.
                    visibility: Optional visibility flag for the sensor.
                    variant: Optional variant name for the sensor configuration.
                    force_camera_prim: If True, forces creation of a camera prim instead of using references or Replicator API.
                    **kwargs: Additional keyword arguments for prim creation.
                
        """
    def _add_reference(self) -> pxr.Usd.Prim:
        """
        Adds a reference to the stage if a config is provided.
        
                If a config is provided, this method adds a reference to the stage and sets the prim's
                variant if provided. It also handles finding the correct sensor prim within referenced assets.
        
                Returns:
                    Usd.Prim: The created or found prim, or None if no config was provided or found.
                
        """
    def _call_replicator_api(self) -> pxr.Usd.Prim:
        """
        Creates a sensor using the Replicator API.
        
                Converts position and orientation into the format required by the Replicator API
                and creates the sensor prim.
        
                Returns:
                    Usd.Prim: The created prim, or None if no Replicator API is available.
                
        """
    def _create_camera_prim(self) -> pxr.Usd.Prim:
        """
        Creates a camera prim for the sensor.
        
                This method is deprecated as of Isaac Sim 5.0. It creates a basic camera prim
                with sensor-specific attributes.
        
                Returns:
                    Usd.Prim: The created camera prim.
        
                Raises:
                    Warning: If called, as this functionality is deprecated.
                
        """
    def do(self) -> pxr.Usd.Prim:
        """
        Executes the sensor creation command.
        
                Creates the sensor using the most appropriate method based on the configuration
                and available APIs.
        
                Returns:
                    Usd.Prim: The created sensor prim.
                
        """
    def undo(self) -> None:
        """
        Undoes the sensor creation command.
        
                Currently not implemented.
                
        """
class IsaacSensorCreateRtxUltrasonic(IsaacSensorCreateRtxSensor):
    """
    Command class for creating RTX Ultrasonic sensors.
    
        This class specializes the base RTX sensor creation for Ultrasonic sensors, providing
        specific configuration and plugin settings for Ultrasonic functionality.
    
        Attributes:
            _sensor_type: Set to "ultrasonic".
            _sensor_plugin_name: Name of the Ultrasonic sensor plugin.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    _sensor_plugin_name: typing.ClassVar[str] = 'omni.sensors.nv.ultrasonic.wpm_ultrasonic.plugin'
    _sensor_type: typing.ClassVar[str] = 'ultrasonic'
SUPPORTED_LIDAR_CONFIGS: dict = {'/Isaac/Sensors/HESAI/XT32_SD10/HESAI_XT32_SD10.usd': set(), '/Isaac/Sensors/NVIDIA/Example_Rotary_2D.usda': set(), '/Isaac/Sensors/NVIDIA/Example_Rotary.usda': set(), '/Isaac/Sensors/NVIDIA/Example_Solid_State.usda': set(), '/Isaac/Sensors/NVIDIA/Simple_Example_Solid_State.usda': set(), '/Isaac/Sensors/Ouster/OS0/OS0.usd': {'OS0_REV6_128ch20hz1024res', 'OS0_REV6_128ch10hz1024res', 'OS0_REV7_128ch20hz1024res', 'OS0_REV7_128ch20hz512res', 'OS0_REV7_128ch10hz512res', 'OS0_REV7_128ch10hz2048res', 'OS0_REV6_128ch10hz2048res', 'OS0_REV6_128ch10hz512res', 'OS0_REV6_128ch20hz512res', 'OS0_REV7_128ch10hz1024res'}, '/Isaac/Sensors/Ouster/OS1/OS1.usd': {'OS1_REV7_128ch10hz1024res', 'OS1_REV6_128ch10hz2048res', 'OS1_REV6_32ch20hz512res', 'OS1_REV6_128ch20hz512res', 'OS1_REV6_128ch10hz1024res', 'OS1_REV6_128ch20hz1024res', 'OS1_REV7_128ch10hz512res', 'OS1_REV7_128ch10hz2048res', 'OS1_REV7_128ch20hz1024res', 'OS1_REV6_32ch10hz1024res', 'OS1_REV6_128ch10hz512res', 'OS1_REV7_128ch20hz512res', 'OS1_REV6_32ch10hz2048res', 'OS1_REV6_32ch20hz1024res', 'OS1_REV6_32ch10hz512res'}, '/Isaac/Sensors/Ouster/OS2/OS2.usd': {'OS2_REV7_128ch20hz1024res', 'OS2_REV6_128ch10hz2048res', 'OS2_REV7_128ch20hz512res', 'OS2_REV6_128ch10hz512res', 'OS2_REV7_128ch10hz1024res', 'OS2_REV7_128ch10hz512res', 'OS2_REV6_128ch10hz1024res', 'OS2_REV7_128ch10hz2048res', 'OS2_REV6_128ch20hz1024res', 'OS2_REV6_128ch20hz512res'}, '/Isaac/Sensors/Ouster/VLS_128/Ouster_VLS_128.usd': set(), '/Isaac/Sensors/SICK/microScan3/SICK_microScan3.usd': {'Profile_1', 'Profile_5', 'Profile_3', 'Profile_4', 'Profile_6', 'Profile_2'}, '/Isaac/Sensors/SICK/multiScan136/SICK_multiScan136.usd': set(), '/Isaac/Sensors/SICK/multiScan165/SICK_multiScan165.usd': set(), '/Isaac/Sensors/SICK/nanoScan3/SICK_nanoScan3.usd': {'CAAZ30AN1'}, '/Isaac/Sensors/SICK/picoScan150/SICK_picoScan150.usd': {'Profile_9', 'Profile_7', 'Profile_3', 'Profile_6', 'Profile_2', 'Profile_8', 'Profile_11', 'Profile_5', 'Profile_4', 'Profile_10', 'Profile_1'}, '/Isaac/Sensors/SICK/TIM781/SICK_TIM781.usd': set(), '/Isaac/Sensors/Slamtec/RPLIDAR_S2E/Slamtec_RPLIDAR_S2E.usd': set(), '/Isaac/Sensors/ZVISION/ZVISION_ML30S.usda': set(), '/Isaac/Sensors/ZVISION/ZVISION_MLXS.usda': set()}
SUPPORTED_LIDAR_VARIANT_SET_NAME: str = 'sensor'
