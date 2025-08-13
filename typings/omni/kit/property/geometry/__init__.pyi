"""
This module implements undoable commands for updating primvar and instanceable attributes in USD prims and a geometry property extension for interactive geometry property management using Omni UI and the Omniverse Kit SDK.
"""
from __future__ import annotations
from omni.kit.property.geometry.scripts.geometry_commands import PrimVarCommand
from omni.kit.property.geometry.scripts.geometry_commands import ToggleInstanceableCommand
from omni.kit.property.geometry.scripts.geometry_commands import TogglePrimVarCommand
from omni.kit.property.geometry.scripts.geometry_properties import GeometryPropertyExtension
from omni.kit.property.geometry.scripts.geometry_properties import deregister_custom_visual_attribute
from omni.kit.property.geometry.scripts.geometry_properties import get_instance
from omni.kit.property.geometry.scripts.geometry_properties import register_custom_visual_attribute
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
from . import scripts
__all__: list = ['PrimVarCommand', 'TogglePrimVarCommand', 'ToggleInstanceableCommand', 'get_instance', 'GeometryPropertyExtension']
