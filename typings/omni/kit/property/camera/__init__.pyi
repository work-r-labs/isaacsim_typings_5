"""
Provides a property extension for camera schema attributes in the Omniverse Kit, including custom fisheye lens settings and sensor model configurations.
"""
from __future__ import annotations
from omni.kit.property.camera.scripts.camera_properties import CameraPropertyExtension
from . import scripts
__all__: list = ['CameraPropertyExtension']
