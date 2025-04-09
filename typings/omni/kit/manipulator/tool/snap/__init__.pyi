"""
Extension that provides snap functionality to transform manipulator as well as a registry for external snap tools
"""
from __future__ import annotations
from omni.kit.manipulator.tool.snap.extension import SnapToolExt
from omni.kit.manipulator.tool.snap.manager import SnapProviderManager
from omni.kit.manipulator.tool.snap.provider import SnapProvider
from omni.kit.manipulator.tool.snap.registry import RegistrationHelper
from omni.kit.manipulator.tool.snap.registry import SnapProviderRegistry
from omni.kit.manipulator.tool.snap.toolbutton import SnapToolButton
from . import builtin_snap_tools
from . import extension
from . import hotkey
from . import manager
from . import menu
from . import models
from . import provider
from . import registry
from . import settings_constants
from . import snap_button_group
from . import toolbutton
__all__: list = ['SnapToolExt', 'SnapProvider', 'SnapProviderRegistry', 'RegistrationHelper', 'SnapToolButton', 'SnapProviderManager', 'settings_constants', 'PRIM_SNAP_NAME', 'SURFACE_SNAP_NAME', 'GRID_SNAP_NAME']
GRID_SNAP_NAME: str = 'Grid'
PRIM_SNAP_NAME: str = 'Prim (Framebuffer Based)'
SURFACE_SNAP_NAME: str = 'Surface (Framebuffer Based)'
