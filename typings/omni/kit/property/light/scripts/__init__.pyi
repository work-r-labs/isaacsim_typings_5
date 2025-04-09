"""
This module provides the LightPropertyExtension class for adding a custom light properties widget to the Omniverse Kit.
"""
from __future__ import annotations
from omni.kit.property.light.scripts.light_properties import LightPropertyExtension
from omni.kit.property.light.scripts.prim_light_widget import LightSchemaAttributesWidget
from . import light_properties
from . import prim_light_widget
__all__: list = ['LightPropertyExtension', 'LightSchemaAttributesWidget']
