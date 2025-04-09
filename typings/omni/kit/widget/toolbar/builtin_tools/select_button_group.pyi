from __future__ import annotations
import carb as carb
from carb.input import KeyboardInput as Key
import omni as omni
from omni.kit.widget.options_menu.option_item import OptionItem
from omni.kit.widget.options_menu.option_radio import OptionRadios
from omni.kit.widget.options_menu.option_separator import OptionSeparator
from omni.kit.widget.options_menu.options_menu import OptionsMenu
from omni.kit.widget.options_menu.options_model import OptionsModel
from omni.kit.widget.toolbar.builtin_tools.models.select_include_ref_model import SelectIncludeRefModel
from omni.kit.widget.toolbar.builtin_tools.models.select_mode_model import SelectModeModel
from omni.kit.widget.toolbar.builtin_tools.models.select_no_kinds_model import SelectNoKindsModel
from omni.kit.widget.toolbar.builtin_tools.models.transform_mode_model import TransformModeModel
from omni.kit.widget.toolbar.hotkey import Hotkey
from omni.kit.widget.toolbar.widget_group import WidgetGroup
from omni import ui
import pathlib as pathlib
from pxr import Kind
__all__: list = ['SelectButtonGroup']
class SelectButtonGroup(omni.kit.widget.toolbar.widget_group.WidgetGroup):
    def __init__(self):
        ...
    def _build_options_menu(self):
        ...
    def _build_select_menu_model(self):
        ...
    def _create_selection_list(self, selections):
        ...
    def _enable_no_kinds_option(self, b):
        ...
    def _get_select_mode_button_name(self):
        ...
    def _get_select_mode_tooltip(self):
        ...
    def _get_select_op_button_name(self, model):
        ...
    def _get_select_tooltip(self):
        ...
    def _invoke_context_menu(self, button_id: str, min_menu_entries: int = 1):
        """
        
                Function to invoke context menu.
        
                Args:
                    button_id: button_id of the context menu to be invoked.
                    min_menu_entries: minimal number of menu entries required for menu to be visible (default 1).
                
        """
    def _plugin_kinds(self):
        ...
    def _update_selection_mode_button(self):
        ...
    def _usd_kinds(self):
        ...
    def _usd_kinds_display(self):
        ...
    def add_custom_select_type(self, entry_name: str, selection_types: list):
        ...
    def clean(self):
        ...
    def create(self, default_size):
        ...
    def get_style(self):
        ...
    def remove_custom_select(self, entry_name):
        ...
def get_extension_folder_path() -> pathlib.Path:
    ...
LIGHT_TYPES: str = 'type:CylinderLight;type:DiskLight;type:DistantLight;type:DomeLight;type:GeometryLight;type:Light;type:RectLight;type:SphereLight'
SELECT_MODEL_MODE_TOOL_NAME: str = 'Model'
SELECT_MODE_BUTTON_ENABLED_SETTING_PATH: str = '/exts/omni.kit.widget.toolbar/SelectionButton/SelectMode/enabled'
SELECT_PRIM_MODE_TOOL_NAME: str = 'Prim'
SELECT_TOOL_NAME: str = 'Select'
