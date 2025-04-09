"""

omni.kit.window.property template classes
"""
from __future__ import annotations
from omni.kit.window.property.property_widget import PropertyWidget
from omni.kit.window.property.templates.header_context_menu import GroupHeaderContextMenu
from omni.kit.window.property.templates.header_context_menu import GroupHeaderContextMenuEvent
from omni.kit.window.property.templates.simple_property_widget import SimplePropertyWidget
from omni.kit.window.property.templates.simple_property_widget import build_frame_header
from . import header_context_menu
from . import simple_property_widget
__all__ = ['GroupHeaderContextMenu', 'GroupHeaderContextMenuEvent', 'HORIZONTAL_SPACING', 'LABEL_HEIGHT', 'LABEL_WIDTH', 'LABEL_WIDTH_LIGHT', 'PropertyWidget', 'SimplePropertyWidget', 'build_frame_header', 'header_context_menu', 'simple_property_widget']
HORIZONTAL_SPACING: int = 4
LABEL_HEIGHT: int = 18
LABEL_WIDTH: int = 160
LABEL_WIDTH_LIGHT: int = 235
