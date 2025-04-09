"""
This module imports and consolidates functionalities from commands and extension submodules within the omni.kit.property.material.scripts package.
"""
from __future__ import annotations
from omni.kit.property.material.scripts.commands.disconnect_command import UsdShadeDisconnectCommand
from omni.kit.property.material.scripts.commands.set_info_attribute_command import SetUsdShadeInfoAttributeCommand
from omni.kit.property.material.scripts.extension import MaterialPropertyExtension
from . import commands
from . import extension
from . import usd_binding_widget
from . import widgets
__all__: list = ['UsdShadeDisconnectCommand', 'SetUsdShadeInfoAttributeCommand', 'MaterialPropertyExtension']
