"""
This is an extension to capture different graphics resources to a file.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.renderer.capture.scripts.extension import Extension
from omni.kit.renderer_capture._renderer_capture import IRendererCapture
from omni.kit.renderer_capture._renderer_capture import acquire_renderer_capture_interface
from . import scripts
__all__: list = ['acquire_renderer_capture_interface', 'IRendererCapture']
