from __future__ import annotations
from omni.kit.viewport.menubar.camera.abstract_camera_widget_delegate import AbstractCameraButtonDelegate
from omni.kit.viewport.menubar.camera.abstract_camera_widget_delegate import AbstractCameraMenuItemDelegate
import pxr.Sdf
from pxr import Sdf
__all__ = ['AbstractCameraButtonDelegate', 'AbstractCameraMenuItemDelegate', 'CameraWidgetDelegateManager', 'Sdf']
class CameraWidgetDelegateManager:
    def _CameraWidgetDelegateManager__get_all_delegates(self, camera_button_or_menu_item: bool):
        ...
    def build_widgets(self, parent_id, viewport_api, camera_path: pxr.Sdf.Path, camera_button_or_menu_item: bool):
        """
        Build all camera widgets for specific camera path with sort based on their orders.
        """
    def destroy(self):
        ...
    def on_camera_path_changed(self, parent_id, camera_path, camera_button_or_menu_item: bool):
        """
        The camera tracked has changed.
        """
    def on_parent_destroyed(self, parent_id, camera_button_or_menu_item: bool) -> None:
        ...
