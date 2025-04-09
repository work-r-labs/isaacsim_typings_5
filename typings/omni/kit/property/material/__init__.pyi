"""
This module provides commands for disconnecting and setting info attributes in USD's shading system, and registers custom widgets for material properties in the OmniKit Editor.
"""
from __future__ import annotations
from omni.kit.property.material.scripts.commands.disconnect_command import UsdShadeDisconnectCommand
from omni.kit.property.material.scripts.commands.set_info_attribute_command import SetUsdShadeInfoAttributeCommand
from omni.kit.property.material.scripts.extension import MaterialPropertyExtension
from . import scripts
__all__: list = ['UsdShadeDisconnectCommand', 'SetUsdShadeInfoAttributeCommand']
