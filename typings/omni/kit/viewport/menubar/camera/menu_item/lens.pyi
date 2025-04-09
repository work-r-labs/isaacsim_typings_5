from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.viewport.menubar.camera.menu_item.camera_setting import AbstractCameraSetting
from omni.kit.viewport.menubar.core.delegate.combobox_menu_delegate import ComboBoxMenuDelegate
from omni.kit.viewport.menubar.core.delegate.separator_menu_delegate import SeparatorDelegate
from omni.kit.viewport.menubar.core.delegate.slider_menu_delegate import SliderMenuDelegate
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxItem
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxModel
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDAttributeModel
from omni.kit.viewport.menubar.core.model.usd_attribute_model import USDFloatAttributeModel
from omni import ui
__all__ = ['AbstractCameraSetting', 'CameraLens', 'ComboBoxItem', 'ComboBoxMenuDelegate', 'ComboBoxModel', 'DEFAULT_LENS', 'SeparatorDelegate', 'SliderMenuDelegate', 'USDAttributeModel', 'USDFloatAttributeModel', 'asyncio', 'omni', 'ui']
class CameraLens(omni.kit.viewport.menubar.camera.menu_item.camera_setting.AbstractCameraSetting):
    def __init__(self, model: omni.kit.viewport.menubar.core.model.usd_attribute_model.USDAttributeModel, enabled: bool = True):
        ...
    def _build_ui(self) -> typing.List[omni.ui._ui.MenuDelegate]:
        ...
    def _on_lens_changed(self, model: _CameraLensModel, item: omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxItem):
        ...
    def destroy(self):
        ...
class _CameraLensModel(omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxModel):
    """
    The camera lens model has all the lens
    """
    def _CameraLensModel__on_lens_changed(self, model: omni.ui._ui.AbstractValueModel):
        ...
    def __init__(self, lens_model: omni.kit.viewport.menubar.core.model.usd_attribute_model.USDFloatAttributeModel):
        ...
    def _on_current_item_changed(self, item: omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxItem) -> None:
        ...
    def destroy(self):
        ...
    @property
    def display(self):
        ...
DEFAULT_LENS: list = [8, 15, 24, 28, 35, 50, 85, 105, 135, 200, (17, 35), (35, 70), (70, 200), (0, 300)]
