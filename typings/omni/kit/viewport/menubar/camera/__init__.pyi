"""
Manages the camera settings integration into the viewport menu bar
"""
from __future__ import annotations
from omni.kit.viewport.menubar.camera.abstract_camera_widget_delegate import AbstractCameraButtonDelegate
from omni.kit.viewport.menubar.camera.abstract_camera_widget_delegate import AbstractCameraMenuItemDelegate
from omni.kit.viewport.menubar.camera.abstract_camera_widget_delegate import AbstractWidgetDelegate
from omni.kit.viewport.menubar.camera.extension import ViewportCameraMenuBarExtension
from omni.kit.viewport.menubar.camera.extension import get_instance
from omni.kit.viewport.menubar.camera.menu_item.single_camera_menu_item import SingleCameraMenuItemBase
from . import abstract_camera_widget_delegate
from . import camera_list_delegate
from . import camera_menu_container
from . import camera_widget_delegate_manager
from . import commands
from . import extension
from . import menu_item
from . import style
from . import utils
__all__: list = ['AbstractCameraButtonDelegate', 'AbstractCameraMenuItemDelegate', 'AbstractWidgetDelegate', 'get_instance', 'ViewportCameraMenuBarExtension', 'SingleCameraMenuItemBase']
