from __future__ import annotations
import carb as carb
import omni as omni
import typing
__all__ = ['ACTION_TAG_PREFIX', 'EditorMenu', 'UNKNOWN_EXTENSION', 'carb', 'omni']
class EditorMenu:
    class EditorMenuItem:
        def __del__(self):
            ...
        def __init__(self, menu_path):
            ...
    active_menus: typing.ClassVar[dict]  # value = {'Window/MDL Material Graph': (<MenuItemDescription name:'MDL Material Graph'>, <MenuItemDescription name:'MDL Material Graph'>)}
    omni_kit_menu_utils_loaded: typing.ClassVar[bool] = True
    window_handler: typing.ClassVar[dict] = {}
    @staticmethod
    def add_action_to_menu(*args, **kwargs):
        ...
    @staticmethod
    def add_item(*args, **kwargs):
        ...
    @staticmethod
    def clean_menu_path(path):
        ...
    @staticmethod
    def convert_to_new_menu(menu_path: str, menu_name: typing.Union[str, list], on_click: typing.Callable, toggle: bool, priority: int, value: bool, enabled: bool, original_svg_color: bool, extension_id):
        ...
    @staticmethod
    def get_action_name(menu_path):
        ...
    @staticmethod
    def get_extension_from_stack(func: callable = None):
        ...
    @staticmethod
    def get_value(*args, **kwargs):
        ...
    @staticmethod
    def has_item(*args, **kwargs):
        ...
    @staticmethod
    def print_depreciated_message(func: callable = None):
        ...
    @staticmethod
    def remove_item(menu_path: str):
        ...
    @staticmethod
    def set_action(menu_path: str, action_mapping_path: str, action_name: str):
        ...
    @staticmethod
    def set_enabled(*args, **kwargs):
        ...
    @staticmethod
    def set_hotkey(*args, **kwargs):
        ...
    @staticmethod
    def set_menu_loaded(state: bool):
        ...
    @staticmethod
    def set_on_click(*args, **kwargs):
        ...
    @staticmethod
    def set_on_right_click(menu_path: str, on_click: typing.Callable = None):
        ...
    @staticmethod
    def set_priority(menu_path: str, priority: int):
        ...
    @staticmethod
    def set_value(*args, **kwargs):
        ...
    @staticmethod
    def split_menu_path(menu_path: str):
        ...
    @staticmethod
    def toggle_value(*args, **kwargs):
        ...
    def __init__(self):
        ...
ACTION_TAG_PREFIX: str = 'EMBridge_'
UNKNOWN_EXTENSION: str = 'omni.kit.ui.editor_menu_bridge'
