from __future__ import annotations
import carb as carb
import omni.kit.viewport.menubar.camera.camera_widget_delegate_manager
from omni.kit.viewport.menubar.camera.camera_widget_delegate_manager import CameraWidgetDelegateManager
import omni.kit.viewport.menubar.core.delegate.icon_menu_delegate
from omni.kit.viewport.menubar.core.delegate.icon_menu_delegate import IconMenuDelegate
import omni.kit.viewport.menubar.core.model.usd_attribute_model
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDAttributeModel
from omni import ui
import omni.ui._ui
import pxr.Sdf
from pxr import Sdf
__all__: list = ['CameraListDelegate']
class CameraListDelegate(omni.kit.viewport.menubar.core.delegate.icon_menu_delegate.IconMenuDelegate):
    model: omni.kit.viewport.menubar.core.model.usd_attribute_model.USDAttributeModel
    def _CameraListDelegate__build_custom_widgets(self, item: omni.ui._ui.MenuItem):
        ...
    def _CameraListDelegate__get_icon_name(self):
        ...
    def _CameraListDelegate__toggle_lock(self):
        ...
    def __init__(self, viewport_api, widget_delegate_manager: omni.kit.viewport.menubar.camera.camera_widget_delegate_manager.CameraWidgetDelegateManager):
        ...
    def _build_icon(self):
        ...
    def _on_lock_changed(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def destroy(self):
        ...
    @property
    def camera_path(self) -> pxr.Sdf.Path:
        ...
    @camera_path.setter
    def camera_path(self, path):
        ...
