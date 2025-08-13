from __future__ import annotations
import carb as carb
import ctypes as ctypes
import gc as gc
from isaacsim.core.nodes.scripts.utils import register_annotator_from_node_with_telemetry
from isaacsim.core.nodes.scripts.utils import register_node_writer_with_telemetry
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.utils.stage import get_next_free_path
from isaacsim.core.utils.xforms import reset_and_set_xform_ops
from isaacsim.sensors.rtx.impl import commands
from isaacsim.sensors.rtx.impl.commands import IsaacSensorCreateRtxIDS
from isaacsim.sensors.rtx.impl.commands import IsaacSensorCreateRtxLidar
from isaacsim.sensors.rtx.impl.commands import IsaacSensorCreateRtxRadar
from isaacsim.sensors.rtx.impl.commands import IsaacSensorCreateRtxSensor
from isaacsim.sensors.rtx.impl.commands import IsaacSensorCreateRtxUltrasonic
from isaacsim.sensors.rtx.impl import extension
from isaacsim.sensors.rtx.impl.extension import Extension
from isaacsim.sensors.rtx.impl.extension import get_gmo_data
from isaacsim.sensors.rtx.impl import lidar_rtx
from isaacsim.sensors.rtx.impl.lidar_rtx import LidarRtx
from isaacsim.sensors.rtx.impl import supported_lidar_configs
from isaacsim.storage.native.nucleus import get_assets_root_path
import numpy as np
import omni as omni
from omni.graph import core as og
from omni.isaac import IsaacSensorSchema
from omni.replicator import core as rep
from omni.replicator.core.scripts.annotators import AnnotatorRegistry
from omni.syntheticdata.scripts import sensors
from pathlib import Path
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from . import bindings
from . import generic_model_output
from . import impl
from . import tests
__all__: list[str] = ['AnnotatorRegistry', 'EXTENSION_NAME', 'Extension', 'Gf', 'IsaacSensorCreateRtxIDS', 'IsaacSensorCreateRtxLidar', 'IsaacSensorCreateRtxRadar', 'IsaacSensorCreateRtxSensor', 'IsaacSensorCreateRtxUltrasonic', 'IsaacSensorSchema', 'LidarRtx', 'Path', 'SUPPORTED_LIDAR_CONFIGS', 'SUPPORTED_LIDAR_VARIANT_SET_NAME', 'Sdf', 'Usd', 'UsdGeom', 'add_reference_to_stage', 'bindings', 'carb', 'commands', 'ctypes', 'extension', 'gc', 'generic_model_output', 'get_assets_root_path', 'get_gmo_data', 'get_next_free_path', 'get_prim_at_path', 'gmo_utils', 'impl', 'lidar_rtx', 'np', 'og', 'omni', 'register_annotator_from_node_with_telemetry', 'register_node_writer_with_telemetry', 'rep', 'reset_and_set_xform_ops', 'sensors', 'supported_lidar_configs', 'tests']
EXTENSION_NAME: str = 'Isaac Sensor'
SUPPORTED_LIDAR_CONFIGS: dict = {'/Isaac/Sensors/HESAI/XT32_SD10/HESAI_XT32_SD10.usd': set(), '/Isaac/Sensors/NVIDIA/Example_Rotary_2D.usda': set(), '/Isaac/Sensors/NVIDIA/Example_Rotary.usda': set(), '/Isaac/Sensors/NVIDIA/Example_Solid_State.usda': set(), '/Isaac/Sensors/NVIDIA/Simple_Example_Solid_State.usda': set(), '/Isaac/Sensors/Ouster/OS0/OS0.usd': {'OS0_REV6_128ch20hz1024res', 'OS0_REV6_128ch10hz1024res', 'OS0_REV7_128ch20hz1024res', 'OS0_REV7_128ch20hz512res', 'OS0_REV7_128ch10hz512res', 'OS0_REV7_128ch10hz2048res', 'OS0_REV6_128ch10hz2048res', 'OS0_REV6_128ch10hz512res', 'OS0_REV6_128ch20hz512res', 'OS0_REV7_128ch10hz1024res'}, '/Isaac/Sensors/Ouster/OS1/OS1.usd': {'OS1_REV7_128ch10hz1024res', 'OS1_REV6_128ch10hz2048res', 'OS1_REV6_32ch20hz512res', 'OS1_REV6_128ch20hz512res', 'OS1_REV6_128ch10hz1024res', 'OS1_REV6_128ch20hz1024res', 'OS1_REV7_128ch10hz512res', 'OS1_REV7_128ch10hz2048res', 'OS1_REV7_128ch20hz1024res', 'OS1_REV6_32ch10hz1024res', 'OS1_REV6_128ch10hz512res', 'OS1_REV7_128ch20hz512res', 'OS1_REV6_32ch10hz2048res', 'OS1_REV6_32ch20hz1024res', 'OS1_REV6_32ch10hz512res'}, '/Isaac/Sensors/Ouster/OS2/OS2.usd': {'OS2_REV7_128ch20hz1024res', 'OS2_REV6_128ch10hz2048res', 'OS2_REV7_128ch20hz512res', 'OS2_REV6_128ch10hz512res', 'OS2_REV7_128ch10hz1024res', 'OS2_REV7_128ch10hz512res', 'OS2_REV6_128ch10hz1024res', 'OS2_REV7_128ch10hz2048res', 'OS2_REV6_128ch20hz1024res', 'OS2_REV6_128ch20hz512res'}, '/Isaac/Sensors/Ouster/VLS_128/Ouster_VLS_128.usd': set(), '/Isaac/Sensors/SICK/microScan3/SICK_microScan3.usd': {'Profile_1', 'Profile_5', 'Profile_3', 'Profile_4', 'Profile_6', 'Profile_2'}, '/Isaac/Sensors/SICK/multiScan136/SICK_multiScan136.usd': set(), '/Isaac/Sensors/SICK/multiScan165/SICK_multiScan165.usd': set(), '/Isaac/Sensors/SICK/nanoScan3/SICK_nanoScan3.usd': {'CAAZ30AN1'}, '/Isaac/Sensors/SICK/picoScan150/SICK_picoScan150.usd': {'Profile_9', 'Profile_7', 'Profile_3', 'Profile_6', 'Profile_2', 'Profile_8', 'Profile_11', 'Profile_5', 'Profile_4', 'Profile_10', 'Profile_1'}, '/Isaac/Sensors/SICK/TIM781/SICK_TIM781.usd': set(), '/Isaac/Sensors/Slamtec/RPLIDAR_S2E/Slamtec_RPLIDAR_S2E.usd': set(), '/Isaac/Sensors/ZVISION/ZVISION_ML30S.usda': set(), '/Isaac/Sensors/ZVISION/ZVISION_MLXS.usda': set()}
SUPPORTED_LIDAR_VARIANT_SET_NAME: str = 'sensor'
gmo_utils = generic_model_output
