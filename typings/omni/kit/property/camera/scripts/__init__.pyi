"""
Provides a property extension for camera schema attributes in the Omniverse Kit, including custom fisheye lens settings and sensor model configurations.
"""
from __future__ import annotations
import omni as omni
from omni.kit.property.camera.scripts.camera_properties import CameraPropertyExtension
from omni.kit.property.camera.scripts.camera_properties import CameraSchemaAttributesWidget
from omni.kit.property.usd.usd_property_widget import MultiSchemaPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from omni.kit.property.usd.usd_property_widget import create_primspec_bool
from omni.kit.property.usd.usd_property_widget import create_primspec_float
from omni.kit.property.usd.usd_property_widget import create_primspec_string
from omni.kit.property.usd.usd_property_widget import create_primspec_token
from pxr import Sdf
from pxr import UsdGeom
from pxr import Vt
from . import camera_properties
__all__: list = ['CameraPropertyExtension']
