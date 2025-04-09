"""

Page building class.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import enum as enum
import omni as omni
from omni.kit.widget.settings.settings_widget import SettingType
from omni.kit.widget.settings.settings_widget import create_setting_widget
from omni.kit.widget.settings.settings_widget import create_setting_widget_combo
from omni.kit.widget.settings.style import get_style
from omni.kit.widget.settings.style import get_ui_style_name
from omni import ui
import os as os
import typing
__all__: list = ['create_setting_widget', 'create_setting_widget_combo', 'get_style', 'get_ui_style_name', 'PreferenceBuilder', 'PageItem', 'PageModel', 'PreferenceBuilderUI']
class PageItem(omni.ui._ui.AbstractItem):
    """
    Single item of the model
    """
    def __init__(self, pages):
        ...
class PageModel(omni.ui._ui.AbstractItemModel):
    def __init__(self, page_list: typing.List[str]):
        ...
    def get_item_children(self, item: PageItem) -> typing.List[omni.kit.window.preferences.scripts.preference_builder.PageItem]:
        ...
    def get_item_value_model(self, item: PageItem, column_id: int) -> omni.ui._ui.SimpleStringModel:
        ...
    def get_item_value_model_count(self, item: PageItem) -> int:
        """
        The number of columns
        """
class PreferenceBuilder:
    """
    
        Page building class
        
    """
    WINDOW_NAME: typing.ClassVar[str] = 'Preferences'
    def __del__(self):
        ...
    def __init__(self, title):
        ...
    def add_frame(self, name: str) -> omni.ui._ui.CollapsableFrame:
        """
        
                Create a UI collapsable frame.
        
                Args:
                    name: Name to be in frame
        
                Returns:
                    :class:`ui.Widget` connected with the setting on the path specified.
                
        """
    def cleanup_slashes(self, path: str, is_directory: bool = False) -> str:
        """
        
                Makes path/slashes uniform
        
                Args:
                    path: path
                    is_directory is path a directory, so final slash can be added
        
                Returns:
                    path
                
        """
    def create_setting_widget(self, label_name: str, setting_path: str, setting_type: omni.kit.widget.settings.settings_widget.SettingType, **kwargs) -> omni.ui._ui.Widget:
        """
        
                Create a UI widget connected with a setting.
        
                If ``range_from`` >= ``range_to`` there is no limit. Undo/redo operations are also supported, because changing setting
                goes through the :mod:`omni.kit.commands` module, using :class:`.ChangeSettingCommand`.
        
                Args:
                    setting_path: Path to the setting to show and edit.
                    setting_type: Type of the setting to expect.
                    range_from: Limit setting value lower bound.
                    range_to: Limit setting value upper bound.
        
                Returns:
                    :class:`ui.Widget` connected with the setting on the path specified.
                
        """
    def create_setting_widget_combo(self, name: str, setting_path: str, list: typing.List[str], setting_is_index: bool | None = None, **kwargs) -> omni.ui._ui.Widget:
        """
        
                Creating a Combo Setting widget.
        
        
                This function creates a combo box that shows a provided list of names and it is connected with setting by path
                specified. Underlying setting values are used from values of `items` dict.
        
                Args:
                    setting_path: Path to the setting to show and edit.
                    items: Can be either :py:obj:`dict` or :py:obj:`list`. For :py:obj:`dict` keys are UI displayed names, values are
                        actual values set into settings. If it is a :py:obj:`list` UI displayed names are equal to setting values.
                    setting_is_index:
                        None - Detect type from setting_path value. If the type is int, set to True.
                        True - setting_path value is index into items list
                        False - setting_path value is string in items list (default)
                
        """
    def get_title(self) -> str:
        """
        
                Gets the page title
        
                Args:
                    None
        
                Returns:
                    str name of the page
                
        """
    def label(self, name: str, tooltip: str = None):
        """
        
                Create a UI widget label.
        
                Args:
                    name: Name to be in label
                    tooltip: The Tooltip string to be displayed when mouse hovers on the label
        
                Returns:
                    :class:`ui.Widget` connected with the setting on the path specified.
                
        """
    def show_page(self) -> bool:
        """
        
                Page is visible. Function can be overridden in subclasses to hide pages.
        
                Returns:
                    True or False
                
        """
    def spacer(self) -> omni.ui._ui.Spacer:
        """
        
                Create a UI spacer.
        
                Args:
                    None
        
                Returns:
                    :class:`ui.Widget` connected with the setting on the path specified.
                
        """
class PreferenceBuilderUI:
    """
    
        Preferences "page" display functions.
    
        
    """
    def __del__(self):
        ...
    def __init__(self, visibility_changed_fn: typing.Callable):
        ...
    def _build_page(self, pages: typing.List[omni.kit.window.preferences.scripts.preference_builder.PreferenceBuilder]) -> None:
        ...
    def _on_visibility_changed_fn(self, visible) -> None:
        ...
    def _show_window(self, menu, value):
        ...
    def create_window(self):
        """
        
                Create omni.ui.window
        
                Args:
                    None
        
                Returns:
                    None
                
        """
    def destroy(self):
        """
        
                Destroy class and cleanup.
                
        """
    def hide_window(self) -> None:
        """
        
                Hides window
        
                Args:
                    None
        
                Returns:
                    None
                
        """
    def rebuild_pages(self) -> None:
        """
        
                Rebuilds window pages using current page list
        
                Args:
                    None
        
                Returns:
                    None
                
        """
    def select_page(self, page: PreferenceBuilder) -> bool:
        """
        
                If found, display the given Preference page and select its title in the TreeView.
        
                Args:
                    page: One of the page from the list of pages.
        
                Returns:
                    bool: A flag indicating if the given page was successfully selected.
                
        """
    def set_active_page(self, page_index: typing.Union[int, str]) -> None:
        """
        
                Set the given page index as the active one.
        
                Args:
                    page_index: Index of page of the page list to set as the active one.
        
                Returns:
                    None
                
        """
    def show_window(self) -> None:
        """
        
                Shows window
        
                Args:
                    None
        
                Returns:
                    None
                
        """
    def update_page_list(self, page_list: typing.List) -> None:
        """
        
                Updates page list
        
                Args:
                    page_list: list of pages
        
                Returns:
                    None
                
        """
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
