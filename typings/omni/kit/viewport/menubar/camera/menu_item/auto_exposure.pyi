from __future__ import annotations
import omni.kit.viewport.menubar.camera.menu_item.camera_setting
from omni.kit.viewport.menubar.camera.menu_item.camera_setting import AbstractCameraSetting
from omni.kit.viewport.menubar.core.delegate.checkbox_menu_delegate import CheckboxMenuDelegate
from omni.kit.viewport.menubar.core.delegate.slider_menu_delegate import SliderMenuDelegate
from omni.kit.viewport.menubar.core.delegate.spinner_menu_delegate import SpinnerMenuDelegate
from omni.kit.viewport.menubar.core.model.setting_model import SettingModel
import omni.kit.viewport.menubar.core.model.usd_attribute_model
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDAttributeModel
from omni import ui
import omni.ui._ui
__all__: list = ['CameraAutoExposure', 'SETTING_ISO', 'SETTING_WHITE_SCALE']
class CameraAutoExposure(omni.kit.viewport.menubar.camera.menu_item.camera_setting.AbstractCameraSetting):
    def __init__(self, model: omni.kit.viewport.menubar.core.model.usd_attribute_model.USDAttributeModel, enabled: bool = True):
        ...
    def _build_ui(self) -> typing.List[omni.ui._ui.MenuDelegate]:
        ...
    def _on_auto_exposure_changed(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def destroy(self):
        ...
SETTING_AUTO_EXPOSURE: str = '/rtx/post/histogram/enabled'
SETTING_ISO: str = '/rtx/post/tonemap/filmIso'
SETTING_WHITE_SCALE: str = '/rtx/post/histogram/whiteScale'
