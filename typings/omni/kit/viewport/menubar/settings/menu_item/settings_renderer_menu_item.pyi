from __future__ import annotations
import carb as carb
from functools import partial
from omni.kit.viewport.menubar.core.delegate.checkbox_menu_delegate import CheckboxMenuDelegate
from omni.kit.viewport.menubar.core.delegate.combobox_menu_delegate import ComboBoxMenuDelegate
import omni.kit.viewport.menubar.core.model.combobox_model
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxItem
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxModel
from omni.kit.viewport.menubar.core.model.combobox_model import SettingComboBoxModel
import omni.kit.viewport.menubar.core.model.reset_button
from omni.kit.viewport.menubar.core.model.reset_button import ResetHelper
from omni.kit.viewport.menubar.settings.menu_item.custom_resolution.custom_resolution_menu_item import CustomResolutionMenuItem
from omni.kit.viewport.menubar.settings.menu_item.resolution_collection.menu import ResolutionCollectionMenu
from omni.kit.viewport.menubar.settings.menu_item.resolution_collection.model import ComboBoxResolutionModel
from omni import ui
import omni.ui._ui
from pxr import Sdf
import pxr.Sdf
__all__: list = ['SettingsRendererMenuItem']
class SettingsRendererMenuItem(omni.ui._ui.Menu):
    """
    The menu with the viewport settings
    """
    def _SettingsRendererMenuItem__on_render_settings_changed(self, camera_path: pxr.Sdf.Path, resolution: typing.Tuple[int, int], viewport_api):
        ...
    def _SettingsRendererMenuItem__on_resolution_index_changed(self, index_model: omni.ui._ui.SimpleIntModel) -> None:
        ...
    def _SettingsRendererMenuItem__sync_model(self, combo_model: omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxModel, value: typing.Any, select_first: bool = False):
        ...
    def __del__(self):
        ...
    def __init__(self, text: str = '', factory: typing.Optional[typing.Dict] = None, **kwargs):
        ...
    def build_fn(self, factory: typing.Dict):
        ...
    def destroy(self):
        ...
    def reset(self) -> None:
        ...
class _ComboBoxApertureFitModel(omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxModel):
    """
    The aperture model
    """
    def __init__(self, viewport_api, settings):
        ...
    def _on_current_item_changed(self, item: omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxItem) -> None:
        ...
class _ComboBoxResolutionScaleModel(omni.kit.viewport.menubar.core.model.combobox_model.SettingComboBoxModel, omni.kit.viewport.menubar.core.model.reset_button.ResetHelper):
    """
    The resolution scale model has all the resolution scales and sets the viewport resolution scale
    """
    def __init__(self, viewport_api, resolution_scale_setting, settings):
        ...
    def _on_current_item_changed(self, item: omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxItem) -> None:
        ...
    def get_default(self):
        ...
    def get_value(self):
        ...
    def restore_default(self) -> None:
        ...
class _FillViewportModel(omni.ui._ui.AbstractValueModel, omni.kit.viewport.menubar.core.model.reset_button.ResetHelper):
    def _FillViewportModel__on_setting_changed(self, *args, **kwargs):
        ...
    def _FillViewportModel__on_value_changed(self, model: omni.ui._ui.AbstractValueModel):
        ...
    def __init__(self, resolution_setter, fill_viewport_settings, isettings: carb.settings._settings.ISettings):
        ...
    def destroy(self):
        ...
    def get_default(self):
        ...
    def get_value(self):
        ...
    def get_value_as_bool(self) -> bool:
        ...
    def restore_default(self) -> None:
        ...
    def set_value(self, value: bool, save_restore: bool = False):
        ...
class _ViewportResolutionSetter:
    """
    Simple class that forwards resolution menu item changes to the proper underlying object
    """
    fill_viewport: bool
    def __init__(self, factory_dict: dict, fill_viewport: bool):
        ...
    def set_resolution(self, resolution) -> None:
        ...
    @property
    def fill_frame(self) -> bool:
        ...
    @property
    def full_resolution(self) -> typing.Tuple[float, float]:
        ...
    @property
    def viewport_api(self):
        ...
    @property
    def viewport_widget(self):
        ...
def _resolve_viewport_setting(viewport_id: str, setting_name: str, isettings: carb.settings._settings.ISettings, legacy_key: typing.Optional[str] = None):
    ...
SETTING_APERTURE: str = '/app/hydra/aperture/conform'
SETTING_RENDER_SCALE_LIST: str = '/app/renderer/resolution/multiplierList'
