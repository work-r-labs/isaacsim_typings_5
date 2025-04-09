from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.widget.options_menu.option_custom import OptionCustom
from omni.kit.widget.options_menu.option_radio import OptionRadios
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from omni.kit.widget.options_menu.options_menu import OptionsMenu
from omni.kit.widget.options_menu.options_model import OptionsModel
from omni.kit.widget.toolbar.builtin_tools.models.setting_model import BoolSettingModel
from omni.kit.widget.toolbar.builtin_tools.models.setting_model import FloatSettingModel
from omni.kit.widget.toolbar.builtin_tools.models.snap_mode_model import SnapModeModel
from omni.kit.widget.toolbar.widget_group import WidgetGroup
from omni import ui
import typing
__all__: list = ['LegacySnapButtonGroup']
class LegacySnapButtonGroup(omni.kit.widget.toolbar.widget_group.WidgetGroup):
    SNAP_ENABLED_SETTING: typing.ClassVar[str] = '/app/viewport/snapEnabled'
    SNAP_MOVE_X_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/stepMove/x'
    SNAP_MOVE_Y_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/stepMove/y'
    SNAP_MOVE_Z_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/stepMove/z'
    SNAP_ROTATE_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/stepRotate'
    SNAP_SCALE_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/stepScale'
    SNAP_TO_SURFACE_SETTING: typing.ClassVar[str] = '/persistent/app/viewport/snapToSurface'
    def __init__(self):
        ...
    def _build_options_menu(self):
        ...
    def _create_snap_increment_setting_window(self):
        ...
    def _invoke_context_menu(self, button_id: str, min_menu_entries: int = 1):
        """
        
                Function to invoke context menu.
        
                Args:
                    button_id: button_id of the context menu to be invoked.
                    min_menu_entries: minimal number of menu entries required for menu to be visible (default 1).
                
        """
    def _on_show_snap_increment_setting_window(self):
        ...
    def _on_snap_on_off(self, model):
        ...
    def _on_snap_setting_change(self, item, event_type):
        ...
    def _on_snap_setting_menu_clicked(self, snap_to_face):
        ...
    def clean(self):
        ...
    def create(self, default_size):
        ...
    def get_style(self):
        ...
