"""
This module provides commands for manipulating USD shade properties, including disconnection and setting info attributes.
"""
from __future__ import annotations
from omni.kit.property.material.scripts.commands.disconnect_command import UsdShadeDisconnectCommand
from omni.kit.property.material.scripts.commands.set_info_attribute_command import SetUsdShadeInfoAttributeCommand
from . import disconnect_command
from . import set_info_attribute_command
__all__: list = ['UsdShadeDisconnectCommand', 'SetUsdShadeInfoAttributeCommand']
