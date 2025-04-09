from __future__ import annotations
import carb as carb
from functools import partial
from omni.kit.viewport.menubar.core.delegate.checkbox_menu_delegate import CheckboxMenuDelegate
from omni.kit.viewport.menubar.core.delegate.combobox_menu_delegate import ComboBoxMenuDelegate
from omni.kit.viewport.menubar.core.delegate.slider_menu_delegate import SliderMenuDelegate
import omni.kit.viewport.menubar.core.model.combobox_model
from omni.kit.viewport.menubar.core.model.combobox_model import ComboBoxItem
from omni.kit.viewport.menubar.core.model.combobox_model import SettingComboBoxModel
import omni.kit.viewport.menubar.core.model.reset_button
from omni.kit.viewport.menubar.core.model.reset_button import ResetHelper
from omni.kit.viewport.menubar.core.model.setting_model import SettingModelWithDefaultValue
from omni import ui
import omni.ui._ui
__all__: list = ['SettingsTransformManipulator']
class SettingsTransformManipulator(omni.ui._ui.Menu):
    """
    The menu with the transform manipulator settings
    """
    def __init__(self, text: str = '', factory: typing.Optional[typing.Dict] = None, **kwargs):
        ...
    def build_fn(self, factory: typing.Dict):
        ...
class _ManipulatorRotationTypeModel(omni.kit.viewport.menubar.core.model.combobox_model.SettingComboBoxModel, omni.kit.viewport.menubar.core.model.reset_button.ResetHelper):
    def __init__(self):
        ...
    def _on_current_item_changed(self, item: omni.kit.viewport.menubar.core.model.combobox_model.ComboBoxItem) -> None:
        ...
    def get_default(self):
        ...
    def get_value(self):
        ...
    def restore_default(self) -> None:
        ...
FREE_ROTATION_TYPE_CLAMPED: str = 'Clamped'
FREE_ROTATION_TYPE_CONTINUOUS: str = 'Continuous'
MENU_WIDTH: int = 350
SETTING_FREE_ROTATION_ENABLED: str = '/persistent/exts/omni.kit.manipulator.transform/manipulator/freeRotationEnabled'
SETTING_FREE_ROTATION_TYPE: str = '/persistent/exts/omni.kit.manipulator.transform/manipulator/freeRotationType'
SETTING_INTERSECTION_THICKNESS: str = '/persistent/exts/omni.kit.manipulator.transform/manipulator/intersectionThickness'
SETTING_SCALE: str = '/persistent/exts/omni.kit.manipulator.transform/manipulator/scaleMultiplier'
