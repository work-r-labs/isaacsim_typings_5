from __future__ import annotations
import carb as carb
import copy as copy
from isaacsim.core.api.sensors.base_sensor import BaseSensor
from isaacsim.core.utils.carb import get_carb_setting
from isaacsim.core.utils import numpy as np_utils
from isaacsim.core.utils.prims import define_prim
from isaacsim.core.utils.prims import get_all_matching_child_prims
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import get_prim_path
from isaacsim.core.utils.prims import get_prim_type_name
from isaacsim.core.utils.prims import is_prim_path_valid
from isaacsim.core.utils.render_product import get_resolution
from isaacsim.core.utils.render_product import set_camera_prim_path
from isaacsim.core.utils.render_product import set_resolution
from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.utils import torch as torch_utils
from isaacsim.core.utils import warp as warp_utils
from isaacsim.core.utils.xforms import reset_and_set_xform_ops
from isaacsim.sensors.camera.camera import Camera
from isaacsim.sensors.camera.camera import distort_point_kannala_brandt
from isaacsim.sensors.camera.camera import distort_point_rational_polynomial
from isaacsim.sensors.camera.camera import get_all_camera_objects
from isaacsim.sensors.camera.camera import point_to_theta
from isaacsim.sensors.camera.camera_view import CameraView
from isaacsim.sensors.camera.extension import Extension
from isaacsim.sensors.camera.single_view_depth_sensor import SingleViewDepthSensor
from isaacsim.sensors.camera.single_view_depth_sensor import SingleViewDepthSensorAsset
import math as math
import numpy as np
import numpy
import omni as omni
from omni.graph import core as og
from omni.isaac.IsaacSensorSchema import IsaacRtxLidarSensorAPI
from omni.replicator import core as rep
from pxr import Gf
from pxr import Sdf
from pxr import Usd
from pxr import UsdGeom
from pxr import Vt
import torch as torch
import warp as wp
from . import camera
from . import camera_view
from . import extension
from . import single_view_depth_sensor
from . import tests
__all__: list[str] = ['BaseSensor', 'Camera', 'CameraView', 'EXTENSION_NAME', 'Extension', 'FTHETA_ATTRIBUTE_MAP', 'Gf', 'IsaacRtxLidarSensorAPI', 'KANNALA_BRANDT_K3_ATTRIBUTE_MAP', 'OPENCV_FISHEYE_ATTRIBUTE_MAP', 'OPENCV_PINHOLE_ATTRIBUTE_MAP', 'RAD_TAN_THIN_PRISM_ATTRIBUTE_MAP', 'R_U_TRANSFORM', 'Sdf', 'SingleViewDepthSensor', 'SingleViewDepthSensorAsset', 'USD_CAMERA_TENTHS_TO_STAGE_UNIT', 'U_R_TRANSFORM', 'U_W_TRANSFORM', 'Usd', 'UsdGeom', 'Vt', 'W_U_TRANSFORM', 'add_reference_to_stage', 'camera', 'camera_view', 'carb', 'copy', 'define_prim', 'distort_point_kannala_brandt', 'distort_point_rational_polynomial', 'extension', 'get_all_camera_objects', 'get_all_matching_child_prims', 'get_carb_setting', 'get_prim_at_path', 'get_prim_path', 'get_prim_type_name', 'get_resolution', 'is_prim_path_valid', 'math', 'np', 'np_utils', 'og', 'omni', 'point_to_theta', 'rep', 'reset_and_set_xform_ops', 'set_camera_prim_path', 'set_resolution', 'single_view_depth_sensor', 'tests', 'torch', 'torch_utils', 'warp_utils', 'wp']
EXTENSION_NAME: str = 'Isaac Sensor'
FTHETA_ATTRIBUTE_MAP: list = ['k0', 'k1', 'k2', 'k3', 'k4']
KANNALA_BRANDT_K3_ATTRIBUTE_MAP: list = ['k0', 'k1', 'k2', 'k3']
OPENCV_FISHEYE_ATTRIBUTE_MAP: list = ['k1', 'k2', 'k3', 'k4']
OPENCV_PINHOLE_ATTRIBUTE_MAP: list = ['k1', 'k2', 'p1', 'p2', 'k3', 'k4', 'k5', 'k6', 's1', 's2', 's3', 's4']
RAD_TAN_THIN_PRISM_ATTRIBUTE_MAP: list = ['k0', 'k1', 'k2', 'k3', 'k4', 'k5', 'p0', 'p1', 's0', 's1', 's2', 's3']
R_U_TRANSFORM: numpy.ndarray  # value = array([[ 1,  0,  0,  0],...
USD_CAMERA_TENTHS_TO_STAGE_UNIT: float = 10.0
U_R_TRANSFORM: numpy.ndarray  # value = array([[ 1,  0,  0,  0],...
U_W_TRANSFORM: numpy.ndarray  # value = array([[ 0, -1,  0,  0],...
W_U_TRANSFORM: numpy.ndarray  # value = array([[ 0,  0, -1,  0],...
