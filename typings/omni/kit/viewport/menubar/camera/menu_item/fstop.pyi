from __future__ import annotations
import omni.kit.viewport.menubar.camera.menu_item.camera_setting
from omni.kit.viewport.menubar.camera.menu_item.camera_setting import AbstractCameraSetting
from omni.kit.viewport.menubar.core.delegate.spinner_menu_delegate import SpinnerMenuDelegate
import omni.kit.viewport.menubar.core.model.usd_attribute_model
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDAttributeModel
from omni import ui
__all__: list = ['CameraFStop']
class CameraFStop(omni.kit.viewport.menubar.camera.menu_item.camera_setting.AbstractCameraSetting):
    def __init__(self, model: omni.kit.viewport.menubar.core.model.usd_attribute_model.USDAttributeModel, enabled: bool = True):
        ...
    def _build_ui(self) -> typing.List[omni.ui._ui.MenuDelegate]:
        ...
    def destroy(self):
        ...
