from __future__ import annotations
import carb as carb
from carb.input import KeyboardInput as Key
from omni.kit.widget.options_menu.option_radio import OptionRadios
from omni.kit.widget.options_menu.options_menu import OptionsMenu
from omni.kit.widget.options_menu.options_model import OptionsModel
from omni.kit.widget.toolbar.builtin_tools.models.transform_mode_model import LocalGlobalTransformModeModel
from omni.kit.widget.toolbar.builtin_tools.models.transform_mode_model import TransformModeModel
from omni.kit.widget.toolbar.hotkey import Hotkey
import omni.kit.widget.toolbar.widget_group
from omni.kit.widget.toolbar.widget_group import WidgetGroup
from omni import ui
import typing
__all__: list = ['TransformButtonGroup']
class TransformButtonGroup(omni.kit.widget.toolbar.widget_group.WidgetGroup):
    TRANSFORM_MOVE_MODE_SETTING: typing.ClassVar[str] = '/app/transform/moveMode'
    TRANSFORM_ROTATE_MODE_SETTING: typing.ClassVar[str] = '/app/transform/rotateMode'
    def __init__(self):
        ...
    def _build_move_options_model(self):
        ...
    def _build_options_menu(self):
        ...
    def _create_local_global_button(self, op_model, tooltip, button_name, op_setting_path, global_name, local_name, default_size):
        ...
    def _get_op_button_name(self, model, global_name, local_name):
        ...
    def _invoke_context_menu(self, button_id: str, min_menu_entries: int = 1):
        """
        
                Function to invoke context menu.
        
                Args:
                    button_id: button_id of the context menu to be invoked.
                    min_menu_entries: minimal number of menu entries required for menu to be visible (default 1).
                
        """
    def add_custom_move_type(self, entry_name: str, move_type: str):
        ...
    def clean(self):
        ...
    def create(self, default_size):
        ...
    def get_style(self):
        ...
    def remove_custom_move_type(self, entry_name: str):
        ...
MOVE_TOOL_NAME: str = 'Move'
ROTATE_TOOL_NAME: str = 'Rotate'
SCALE_TOOL_NAME: str = 'Scale'
